"""Pruebas de resolución de procedencia anterior a la migración medallón."""
import hashlib
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import medallon_compat


class MedallonCompatTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.root_patch = patch.object(medallon_compat, 'ROOT', self.root)
        self.root_patch.start()
        self.addCleanup(self.temporary.cleanup)
        self.addCleanup(self.root_patch.stop)

    def create_file(self, relative, content):
        target = self.root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
        return target

    def test_datos_derivados_resuelven_a_silver(self):
        old = self.root / 'Data/datos/Datos_seleccionados/SSPD/sspd_ebby-cjha_mensual.csv'
        target = self.root / 'Data/silver/datos/Datos_seleccionados/SSPD/sspd_ebby-cjha_mensual.csv'
        self.assertEqual(medallon_compat.historical_path(old), target)

    def test_codigo_actual_se_prefiere_si_coincide_la_huella(self):
        current = self.create_file('Code/Modeling/detectores/zscore_robusto.py', b'actual')
        self.create_file('Docs/codigo_historico/Modeling/detectores/zscore_robusto.py', b'anterior')
        expected = hashlib.sha256(b'actual').hexdigest()
        self.assertEqual(medallon_compat.historical_path(current, expected), current)

    def test_salida_historica_solo_se_acepta_si_su_huella_coincide(self):
        old = self.root / 'Outputs/sensibilidad/inyecciones_detalle.csv.gz'
        current = self.create_file('Data/gold/outputs/sensibilidad/inyecciones_detalle.csv.gz', b'nuevo')
        archived = self.create_file('Docs/evidencia_historica/outputs/sensibilidad/inyecciones_detalle.csv.gz', b'original')
        expected = hashlib.sha256(b'original').hexdigest()
        self.assertEqual(medallon_compat.historical_path(old, expected), archived)
        self.assertEqual(medallon_compat.historical_path(old, 'huella-distinta'), current)


if __name__ == '__main__':
    unittest.main()
