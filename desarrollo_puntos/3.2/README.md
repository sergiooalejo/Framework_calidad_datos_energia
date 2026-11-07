# 3.2 · Fichas de caracterización por fuente (OE2)

Corresponde a la actividad 2 del Hito 3: identidad de la fuente, cobertura, variables,
granularidad, interpretación, usos y limitaciones.

| Fuente | Ficha |
|---|---|
| CHEC · c698-wqig | [Caracterización CHEC](CHEC/Ficha_caracterizacion_01_chec_c698-wqig.md) |
| EPM · sfcd-b3ey | [Caracterización EPM](EPM/Ficha_caracterizacion_02_epm_sfcd-b3ey.md) |
| Superservicios ZNI · ebby-cjha | [Caracterización SSPD](SSPD/Ficha_caracterizacion_03_sspd_ebby-cjha.md) |
| XM/SIMEM · c1b851 | [Caracterización del piloto XM](XM/Ficha_caracterizacion_04_xm_c1b851.md) |

[DECISION_CATALOGOS_CHEC.md](CHEC/DECISION_CATALOGOS_CHEC.md) describe códigos, unidades,
semántica y clave candidata. Pertenece aquí por su contenido de caracterización, aunque
también sustenta las reglas y su aplicación.

En `perfiles/` se conservan:

- `sspd_verificacion_cobertura_seleccion.json`: evidencia de cobertura agregada SSPD;
  no demuestra continuidad individual de cada usuario.
- `xm_piloto_cobertura.json`: perfil del piloto y de su selección de versiones; conserva
  evidencia de la exploración, que debe leerse junto a la ficha actual.
- `perfil_supers_icnr-l4iw.json`: perfil histórico de una fuente en revisión, que no es
  el dataset SSPD ZNI de la matriz principal.

Los resultados históricos del Hito 2 están en [3.3/insumos_hito2](../3.3/insumos_hito2/README.md).
La evaluación de candidatos CREG y XM está en [3.4](../3.4/README.md).
