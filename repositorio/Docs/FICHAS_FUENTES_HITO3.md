# Fichas de caracterización vigentes · Hito 3

Las definiciones detalladas y evidencia histórica se conservan en REFERENCIA_TECNICA.md.

## EPM · sfcd-b3ey

- Archivo: `Data/bronze/datos/Datos_seleccionados/EPM/epm_sfcd-b3ey.csv`.
- SHA-256: `b974a37a171b9178476fbd2baba21470e8845076af105ef9c178e80690f09920`.
- 3623 filas; 12 columnas; 61 períodos distintos de 2016-12 a 2021-12.
- Consumidores: usuarios tarifarios, comercializadores e investigadores de tarifas.
- Datos críticos: período, clave de negocio y medidas. Clave: tipodeinformacion, tipodetarifa, tipodedato, rangodeconsumo, nivel. Medidas: propiedadepm, compartido, propiedaddelcliente, punta, fueradepunta.
- Ausentes por columna: {"tipodeinformacion": 0, "tipodetarifa": 0, "tipodedato": 0, "rangodeconsumo": 0, "nivel": 0, "propiedadepm": 1, "compartido": 1, "propiedaddelcliente": 1, "punta": 1, "fueradepunta": 1, "year": 1, "mes": 1}.

Tarifas/componentes: las unidades y aplicabilidades exactas dependen de concepto, nivel y modalidad; los catálogos internos no son confirmación del publicador. Exactitud disponible solo para el alcance contrastado. Oportunidad histórica pendiente.

## CHEC · c698-wqig

- Archivo: `Data/bronze/datos/Datos_seleccionados/CHEC/chec_c698-wqig.csv`.
- SHA-256: `1f34f85ada431220a39b2bacf10a1dd09bd440b3e7eab61b61d53094508af08c`.
- 40609 filas; 24 columnas; 225 períodos distintos de 2008-01 a 2026-09.
- Consumidores: usuarios tarifarios, comercializadores e investigadores de costos unitarios.
- Datos críticos: período, clave de negocio y medidas. Clave: comercializador_codigo, mercado_codigo, costounitariotarifa_tipomed, nivel_tension_codigo, modalidadcobro_propiedad, claseservicio_codigo, costounitariotarifa_rangoconsumo, costounitariotarifa_tipomercado. Medidas: costounitariotarifa_cu, costounitariotarifa_valor_tarifa.
- Ausentes por columna: {"costounitariotarifa_ano": 0, "costounitariotarifa_mes": 0, "comercializador_codigo": 0, "comercializador_nombre": 0, "mercado_codigo": 0, "mercado_nombre": 0, "costounitariotarifa_tipomed": 0, "nivel_tension_codigo": 0, "modalidadcobro_propiedad": 0, "claseservicio_codigo": 0, "claseservicio_descri": 0, "claseservicio_estrato": 0, "costounitariotarifa_rangoconsumo": 0, "costounitariotarifa_tipomercado": 0, "costounitariotarifa_generacion": 0, "costounitariotarifa_transmision": 0, "costounitariotarifa_distribucion": 11, "costounitariotarifa_comercializacion": 11, "costounitariotarifa_perdidas": 11, "costounitariotarifa_restricciones": 11, "costounitariotarifa_cu": 0, "costounitariotarifa_cureal": 0, "costounitariotarifa_subcon": 11, "costounitariotarifa_valor_tarifa": 0}.

Tarifas/componentes: las unidades y aplicabilidades exactas dependen de concepto, nivel y modalidad; los catálogos internos no son confirmación del publicador. Exactitud disponible solo para el alcance contrastado. Oportunidad histórica pendiente.

## SSPD · ebby-cjha

- Archivo: `Data/silver/datos/Datos_seleccionados/SSPD/sspd_ebby-cjha_mensual.csv`.
- SHA-256: `cc92ffc4f89ecab6336304feace83e87b049a2e488e17d1e88c2851e784becbe`.
- 15075 filas; 18 columnas; 59 períodos distintos de 2017-07 a 2022-05.
- Consumidores: analistas de facturación y consumo de empresas ZNI.
- Datos críticos: período, clave de negocio y medidas. Clave: identificador_empresa, estrato_sector, ubicacion, tipo_conexion, tipo_lectura, tipo_factura. Medidas: consumo_basico_sum, consumo_compl_sum, consumo_mayor800_sum, valor_total_sum.
- Ausentes por columna: {"identificador_empresa": 0, "anio": 0, "periodo": 0, "estrato_sector": 0, "ubicacion": 0, "tipo_conexion": 0, "tipo_lectura": 0, "tipo_factura": 0, "n_registros": 0, "consumo_basico_sum": 0, "consumo_basico_min": 0, "consumo_basico_max": 0, "consumo_compl_sum": 0, "consumo_mayor800_sum": 0, "fact_basico_sum": 0, "valor_total_sum": 0, "valor_subsidio_sum": 0, "dias_facturados_sum": 0}.

Unidad y agregación: véanse diccionarios versionados SSPD/XM y ficha histórica. No se aplican relaciones de propiedad de EPM a consumo/demanda. Exactitud independiente y oportunidad siguen delimitadas por evidencia.

## XM · c1b851

- Archivo: `Data/silver/datos/Datos_seleccionados/XM_piloto/xm_demanda_mensual_piloto.csv`.
- SHA-256: `fe51fd1cdcbd229ef66b44e81d5312d0f3537ce237873bf52d4a25397f48e975`.
- 61 filas; 10 columnas; 61 períodos distintos de 2020-01 a 2025-01.
- Consumidores: analistas del mercado y demanda energética; demanda no equivale a consumo facturado.
- Datos críticos: período, clave de negocio y medidas. Clave: CodigoSICAgente, MercadoComercializacion, SistemaTransmision. Medidas: demanda_kwh.
- Ausentes por columna: {"periodo": 0, "CodigoSICAgente": 0, "MercadoComercializacion": 0, "SistemaTransmision": 0, "Version_seleccionada": 0, "horas": 0, "horas_unicas": 0, "horas_esperadas": 0, "demanda_kwh": 0, "publicacion_declarada": 1}.

Unidad y agregación: véanse diccionarios versionados SSPD/XM y ficha histórica. No se aplican relaciones de propiedad de EPM a consumo/demanda. Exactitud independiente y oportunidad siguen delimitadas por evidencia.

## SSPD_PLAN · vfjy-6fka

- Archivo: `Data/bronze/datos/Datos_seleccionados/SSPD_PLAN/sspd_vfjy-6fka.csv`.
- SHA-256: `2077441a4650b239c30d99d06c0466dd124d3e6aaa6d79aad5ede9b570c131b8`.
- 5396 filas; 16 columnas; 8 períodos distintos de 2022-03 a 2023-06.
- Consumidores: analistas de subsidios, contribuciones y FOES; supervisión y contabilidad sectorial.
- Datos críticos: período, clave de negocio y medidas. Clave: id_empresa, id_mercado, estra_sector. Medidas: subsidios, contribuciones, cont_no_recau_a_6m, cont_recau_last_conc, g_rec_mmin_fssri_pgn, giros_recib_otros, giros_efect_mminas, giros_efect_otros, foes, devolucion_foes.
- Ausentes por columna: {"anio": 0, "mes": 0, "estra_sector": 0, "subsidios": 0, "contribuciones": 0, "cont_no_recau_a_6m": 0, "cont_recau_last_conc": 0, "g_rec_mmin_fssri_pgn": 0, "giros_recib_otros": 0, "giros_efect_mminas": 0, "giros_efect_otros": 0, "foes": 0, "devolucion_foes": 0, "id_mercado": 0, "id_empresa": 0, "empresa": 0}.

Los metadatos oficiales definen importes contables en pesos, año/mes contables y estrato/sector. No contiene Rango de Consumo: la afirmación de 2.143 ausentes no se puede atribuir a este esquema. Los ocho períodos no alcanzan 49 meses; solo reglas transversales. Los códigos de estrato/sector requieren catálogo autorizado. Véanse las dos capturas y sus metadatos originales.
