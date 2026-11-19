"""Regresiones H6: origen vigente, población única, integridad y revisiones."""
import csv
import gzip
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from Code.external_validation import generar_muestra_alertas as M


class MuestraTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.input = self.root / "z_findings/results/experiments/puntajes_reales.csv.gz"
        self.calibration = self.input.with_name("calibracion.csv")
        self.h4_manifest = self.input.with_name("manifiesto.json")
        self.output = self.root / "muestra.csv"
        for name, value in (("ROOT", self.root), ("INPUT", self.input), ("CALIBRATION", self.calibration),
                            ("H4_MANIFEST", self.h4_manifest), ("OUTPUT", self.output)):
            p = patch.object(M, name, value)
            p.start()
            self.addCleanup(p.stop)
        self.rows = [self.row(i) for i in range(60)]
        self.rows += [self.row(100, fuente="CHEC"), self.row(101, referencia="24"), self.row(102, flag="0")]
        self.input.parent.mkdir(parents=True)
        with self.calibration.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["referencia", "tasa_objetivo", "banco", "metodo", "umbral"])
            w.writeheader()
            w.writerows(dict(referencia=36, tasa_objetivo=.05, banco="EPM:W36:2020-12", metodo=m, umbral=.5) for m in M.METHODS)
        self.write_input()

    def row(self, i, fuente="EPM", referencia="36", flag="1"):
        row = dict(fuente=fuente, referencia=referencia, banco="EPM:W36:2020-12", sid=f"serie-{i:03d}",
                   categoria='["Monomia", "I"]', medida="compartido", nivel="Nivel_I", periodo="2021-01")
        for m in M.METHODS:
            row[f"puntaje_{m}"] = ".1"
            row[f"alerta_{m}"] = "0"
        row.update(puntaje_R12=".8" if flag == "1" else ".1", alerta_R12=flag)
        return row

    def write_input(self):
        with gzip.open(self.input, "wt", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(self.rows[0]))
            w.writeheader()
            w.writerows(self.rows)
        self.refresh_manifest()

    def refresh_manifest(self):
        evidence = self.root / "evidencia.txt"
        if not evidence.exists():
            evidence.write_text("original", encoding="utf-8")
        doc = dict(protocolo=M.PROTOCOL, ejecucion_utc="2026-11-14T00:00:00Z",
                   entradas={"evidencia.txt": M.digest(evidence)}, entradas_auxiliares={}, codigo={},
                   cuarentena=dict(archivo="evidencia.txt", sha256=M.digest(evidence)),
                   salidas={M.relative(p): M.digest(p) for p in (self.input, self.calibration)})
        self.h4_manifest.write_text(json.dumps(doc), encoding="utf-8")

    def read_sample(self, target):
        with target.open(encoding="utf-8-sig", newline="") as f:
            return list(csv.DictReader(f))

    def test_escenario_principal_unico_y_metodos_vigentes(self):
        target = M.main([])
        rows = self.read_sample(target)
        self.assertEqual(len(rows), 50)
        self.assertEqual(len({r["id_alerta"] for r in rows}), 50)
        self.assertEqual({r["fuente"] for r in rows}, {"EPM"})
        self.assertEqual({r["referencia"] for r in rows}, {"36"})
        self.assertEqual({r["clasificacion"] for r in rows}, {"pendiente"})
        self.assertTrue(all(r["serie"] == "Monomia|I" for r in rows))
        for method in ("LOF", "KNN"):
            self.assertIn(f"alerta_{method}", rows[0])
            self.assertIn(f"umbral_{method}", rows[0])
        doc = json.loads(target.with_suffix(".manifiesto.json").read_text(encoding="utf-8"))
        self.assertEqual(doc["muestra"]["sha256"], M.digest(target))
        self.assertEqual(doc["candidatos_por_fuente"], {"EPM": 60})
        self.assertEqual(doc["ids_seleccionados"], [r["id_alerta"] for r in rows])
        self.assertEqual(doc["entradas"][M.relative(self.input)], M.digest(self.input))

    def test_sorteo_independiente_del_orden(self):
        first = self.read_sample(M.main(["--salida", str(self.root / "primera.csv")]))
        self.rows.reverse()
        self.write_input()
        second = self.read_sample(M.main(["--salida", str(self.root / "segunda.csv")]))
        self.assertEqual(first, second)

    def test_no_sobrescribe_muestra_revisada_ni_manifiesto(self):
        self.output.write_text("revision irremplazable", encoding="utf-8")
        old_manifest = self.output.with_suffix(".manifiesto.json")
        old_manifest.write_text("evidencia previa", encoding="utf-8")
        created = M.main([])
        self.assertNotEqual(created, self.output)
        self.assertEqual(self.output.read_text(encoding="utf-8"), "revision irremplazable")
        self.assertEqual(old_manifest.read_text(encoding="utf-8"), "evidencia previa")
        with self.assertRaises(FileExistsError):
            M.main(["--salida", str(self.output)])

    def test_no_sobrescribe_manifiesto_sin_csv(self):
        self.output.with_suffix(".manifiesto.json").write_text("previo", encoding="utf-8")
        with self.assertRaises(FileExistsError):
            M.main(["--salida", str(self.output)])
        self.assertFalse(self.output.exists())

    def test_cuota_insuficiente_no_duplica_ni_completa_con_otras_fuentes(self):
        self.rows = self.rows[:49] + [self.row(100 + i, fuente="CHEC") for i in range(100)]
        self.write_input()
        with self.assertRaisesRegex(RuntimeError, "49 observaciones únicas"):
            M.main([])
        self.assertFalse(self.output.exists())

    def test_rechaza_observacion_duplicada_aunque_cambie_el_banco(self):
        self.rows.append(dict(self.rows[0], banco="otro"))
        self.write_input()
        with self.assertRaisesRegex(ValueError, "Observación repetida"):
            M.main([])

    def test_rechaza_salida_h4_alterada(self):
        with self.input.open("ab") as f:
            f.write(b"cambio")
        with self.assertRaisesRegex(ValueError, "alterada o desactualizada"):
            M.main([])
        self.assertFalse(self.output.exists())

    def test_rechaza_referencia_alterada(self):
        (self.root / "evidencia.txt").write_text("modificada", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "alterada o desactualizada"):
            M.main([])

    def test_rechaza_protocolo_historico(self):
        doc = json.loads(self.h4_manifest.read_text(encoding="utf-8"))
        doc["protocolo"] = "historico"
        self.h4_manifest.write_text(json.dumps(doc), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Se requiere el protocolo"):
            M.main([])

    def test_rechaza_banderas_inconsistentes_y_no_finitos(self):
        self.rows[0]["alerta_R12"] = "0"
        self.write_input()
        with self.assertRaisesRegex(ValueError, "Bandera no coincide"):
            M.main([])
        self.rows[0]["alerta_R12"] = "1"
        self.rows[0]["puntaje_R12"] = "nan"
        self.write_input()
        with self.assertRaisesRegex(ValueError, "inválidos"):
            M.main([])

    def test_rechaza_columnas_faltantes(self):
        for row in self.rows:
            del row["alerta_LOF"]
        self.write_input()
        with self.assertRaisesRegex(ValueError, "Faltan columnas H4"):
            M.main([])


if __name__ == "__main__":
    unittest.main()
