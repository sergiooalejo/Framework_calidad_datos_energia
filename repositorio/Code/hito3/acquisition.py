"""Descargas Socrata inmutables con :id, páginas originales y manifiesto.

La fecha de captura no es fecha de publicación. Dos peticiones independientes
pueden devolver versiones diferentes; la comparación nunca fuerza igualdad.
"""
from __future__ import annotations

from datetime import datetime, timezone
import json
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import uuid

from .core import ROOT, digest, write_csv, compare_rows, read_csv

DATASETS = {'EPM': 'sfcd-b3ey', 'CHEC': 'c698-wqig', 'SSPD_PLAN': 'vfjy-6fka'}
BASE = ROOT / 'Data/bronze/descargas_hito3'


def request_json(url):
    request = Request(url, headers={'Accept': 'application/json', 'User-Agent': 'FrameworkCalidadEnergia/0.1 investigacion'})
    with urlopen(request, timeout=45) as response:
        raw = response.read()
    return raw, json.loads(raw)


def download(source, base=BASE, fetch=request_json, page_size=10000):
    dataset = DATASETS[source]
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ') + '_' + uuid.uuid4().hex[:8]
    folder = Path(base) / source / stamp
    folder.mkdir(parents=True, exist_ok=False)
    manifest = dict(fuente=source, dataset_id=dataset, inicio_utc=datetime.now(timezone.utc).isoformat(),
                    estado='incompleta', paginas=[], nota='Captura real por API; no acredita fecha histórica de publicación.')
    try:
        metadata_url = f'https://www.datos.gov.co/api/views/{dataset}.json'
        raw, metadata = fetch(metadata_url)
        (folder / 'metadatos.json').write_bytes(raw)
        columns = [c['fieldName'] for c in metadata['columns'] if not c['fieldName'].startswith(':')]
        if len(columns) != len(set(columns)) or not columns:
            raise ValueError('Metadatos sin contrato único de columnas')
        url = f'https://www.datos.gov.co/resource/{dataset}.json'
        _, count_before = fetch(url + '?' + urlencode({'$select': 'count(*) as n'}))
        expected = int(count_before[0]['n'])
        rows, ids = [], []
        offset = 0
        while True:
            query = urlencode({'$select': '*, :id', '$order': ':id', '$limit': page_size, '$offset': offset})
            page_url = url + '?' + query
            raw, page = fetch(page_url)
            if not isinstance(page, list):
                raise ValueError('Respuesta API sin lista de registros')
            filename = f'pagina_{offset:09d}.json'
            (folder / filename).write_bytes(raw)
            manifest['paginas'].append(dict(url=page_url, archivo=filename, sha256=digest(folder / filename), filas=len(page)))
            for record in page:
                if ':id' not in record:
                    raise ValueError('La API no entregó :id; no se inventa identificador del publicador')
                ids.append(str(record[':id']))
                row = {}
                for col in columns:
                    value = record.get(col, '')
                    row[col] = '' if value is None else (json.dumps(value, ensure_ascii=False, sort_keys=True) if isinstance(value, (dict, list)) else str(value))
                rows.append(row)
            if len(page) < page_size:
                break
            offset += page_size
        _, count_after = fetch(url + '?' + urlencode({'$select': 'count(*) as n'}))
        if len(set(ids)) != len(ids) or len(rows) != expected or int(count_after[0]['n']) != expected:
            raise ValueError('La fuente cambió durante la paginación o hay :id repetidos; captura incompleta')
        write_csv(folder / 'datos.csv', rows, columns)
        from .core import content_key
        write_csv(folder / 'identificadores.csv', [dict(api_row_id=i, clave_contenido=content_key(r)) for i, r in zip(ids, rows)],
                  ['api_row_id', 'clave_contenido'])
        manifest.update(estado='completa', filas=len(rows), columnas=columns, url_metadatos=metadata_url,
                        sha256_datos=digest(folder / 'datos.csv'), sha256_metadatos=digest(folder / 'metadatos.json'),
                        sha256_identificadores=digest(folder / 'identificadores.csv'),
                        consistencia_paginacion='conteos antes/después e identificadores únicos; API sin aislamiento transaccional')
    except Exception as exc:
        manifest['error'] = f'{type(exc).__name__}: {exc}'
        raise
    finally:
        manifest['fin_utc'] = datetime.now(timezone.utc).isoformat()
        (folder / 'manifiesto.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return folder


def compare_downloads(base=BASE):
    results = []
    for source in DATASETS:
        captures = []
        for path in sorted((Path(base) / source).glob('*/manifiesto.json')):
            doc = json.loads(path.read_text(encoding='utf-8'))
            if doc['estado'] == 'completa':
                captures.append((path.parent, doc))
        if len(captures) < 2:
            results.append(dict(fuente=source, estado='pendiente_dos_descargas', capturas_completas=len(captures)))
            continue
        (a, ma), (b, mb) = captures[-2:]
        for folder, manifest in ((a, ma), (b, mb)):
            for filename, key in (('datos.csv', 'sha256_datos'), ('metadatos.json', 'sha256_metadatos'), ('identificadores.csv', 'sha256_identificadores')):
                if digest(folder / filename) != manifest[key]:
                    raise ValueError(f'Captura alterada: {folder / filename}')
            for page in manifest['paginas']:
                if digest(folder / page['archivo']) != page['sha256']:
                    raise ValueError('Página API alterada')
        result = compare_rows(read_csv(a / 'datos.csv'), read_csv(b / 'datos.csv'))
        results.append(dict(fuente=source, estado='comparadas', primera=str(a.relative_to(ROOT)), segunda=str(b.relative_to(ROOT)),
                            sha256_primera=ma['sha256_datos'], sha256_segunda=mb['sha256_datos'], **result))
    return results


def main():
    errors = []
    for source in DATASETS:
        for _ in range(2):
            try:
                print('Descarga:', download(source), flush=True)
            except Exception as exc:
                errors.append(dict(fuente=source, error=str(exc)))
                print(f'{source}: {exc}', flush=True)
                break
    out = ROOT / 'Data/gold/outputs/hito3'
    out.mkdir(parents=True, exist_ok=True)
    (out / 'comparacion_descargas.json').write_text(json.dumps(dict(comparaciones=compare_downloads(), errores=errors), ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    if errors:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
