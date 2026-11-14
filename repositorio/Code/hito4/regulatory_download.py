"""Conserva fuentes oficiales completas; no atribuye causalidad a una coincidencia."""
from datetime import datetime,timezone
from html.parser import HTMLParser
import json
from pathlib import Path
from urllib.request import Request,urlopen
import uuid

from Code.hito3.core import ROOT,digest

DOCUMENTS=('0015_2018','0078_2019','0156_2019','0012_2020','0152_2020','0003_2021')


class Text(HTMLParser):
    def __init__(self):
        super().__init__();self.parts=[];self.skip=0
    def handle_starttag(self,tag,attrs):
        if tag in ('script','style'):self.skip+=1
        if tag in ('p','div','br','tr','h1','h2','h3'):self.parts.append('\n')
    def handle_endtag(self,tag):
        if tag in ('script','style'):self.skip=max(0,self.skip-1)
    def handle_data(self,data):
        if not self.skip:self.parts.append(data)


def main():
    folder=ROOT/'Data/bronze/normativa_hito4'/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'_'+uuid.uuid4().hex[:8])
    folder.mkdir(parents=True,exist_ok=False)
    records=[]
    for code in DOCUMENTS:
        url=f'https://gestornormativo.creg.gov.co/gestor/entorno/docs/resolucion_creg_{code}.htm'
        with urlopen(Request(url,headers={'User-Agent':'FrameworkCalidadEnergia/0.1 investigacion'}),timeout=45) as response:
            raw=response.read();charset=response.headers.get_content_charset() or 'utf-8'
        original=folder/(code+'.htm');original.write_bytes(raw)
        try:html=raw.decode(charset)
        except UnicodeDecodeError:html=raw.decode('cp1252')
        parser=Text();parser.feed(html)
        lines=[' '.join(line.split()) for line in ''.join(parser.parts).splitlines()]
        content='\n'.join(line for line in lines if line)+'\n'
        extracted=folder/(code+'.txt');extracted.write_text(content,encoding='utf-8')
        records.append(dict(id=code,url=url,archivo=original.relative_to(ROOT).as_posix(),texto=extracted.relative_to(ROOT).as_posix(),
                            sha256=digest(original),sha256_texto=digest(extracted),fecha_captura_utc=datetime.now(timezone.utc).isoformat(),
                            alcance='HTML completo capturado; el análisis cita apartados específicos. Fórmulas en imágenes no se transcriben por inferencia. Texto consolidado puede incluir modificaciones posteriores al período analizado.'))
        print('Capturada',code,flush=True)
    (folder/'manifiesto.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')


if __name__=='__main__':main()
