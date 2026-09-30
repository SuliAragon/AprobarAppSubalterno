"""Verifica cada pasaje literal contra el texto extraído del PDF original.
Requiere el manual privado; genera sólo localizaciones y huellas, sin publicar el PDF.
"""
from pathlib import Path
import re,json,hashlib,unicodedata
ROOT=Path(__file__).resolve().parents[1]
TEXT=ROOT.parent/'tmp/pdfs/temario.txt'

def norm(s):return ''.join(ch for ch in unicodedata.normalize('NFKD',s).lower() if ch.isalnum())
raw=TEXT.read_text();chunks=re.split(r'===== PÁGINA (\d+) =====',raw)
page=0;parts=[];offsets=[];offset=0
for i in range(1,len(chunks),2):
    page=int(chunks[i]);lines=[]
    cleaned=re.sub(r'\([^)]*(?:EXAMEN|ES DECIR|ES OPTATIVO|OBLIGACIÓN,|por tanto, la interposición)[^)]*\)','',chunks[i+1],flags=re.I)
    for line in cleaned.splitlines():
        if re.match(r'^SUBALTERNO|^Todos los derechos|^T[ÍI]TULO|^CAP[ÍI]TULO|^SECCI[ÓO]N|^Sección',line):continue
        line=re.sub(r'\([^)]*EXAMEN[^)]*\)','',line,flags=re.I)
        line=re.sub(r'\b(?:EXAMEN|EXAMENES|IMPORTANTE)\b','',line)
        lines.append(line)
    piece=norm(' '.join(lines));offsets.append((offset,offset+len(piece),page));parts.append(piece);offset+=len(piece)
full=''.join(parts);rows=json.loads((ROOT/'data/legal-candidates.json').read_text());result={};unmatched=[]
for q in rows:
    blank=q['prompt'].split('«',1)[1].rsplit('»',1)[0];quote=blank.replace('____',q['correct']);key=hashlib.sha256(quote.encode()).hexdigest()
    needle=norm(quote);start=full.find(needle)
    if start<0:unmatched.append((q['coverage'],quote));continue
    end=start+len(needle)-1
    pages=[p for a,b,p in offsets if a<=start<b or a<=end<b]
    result[key]={'pages':list(dict.fromkeys(pages)),'textMatched':True}
(ROOT/'data/legal-evidence.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('Pasajes verificados:',len(result),'Candidatos:',len(rows),'Sin correspondencia:',len(unmatched))
for law,quote in unmatched[:12]:print(law,quote)
assert not unmatched,'Un pasaje sin correspondencia necesita revisión antes de publicarse.'
