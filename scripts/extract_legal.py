"""Preparación del material literal: sólo los artículos transcritos en el PDF del usuario."""
from pathlib import Path
import re, json, collections
ROOT=Path(__file__).resolve().parents[1]
TEXT=ROOT.parent/'tmp/pdfs'

# Distractores del mismo tipo; la pregunta pide reconstruir texto, no elegir sinónimos.
SETS=[
 ['discriminación directa','discriminación indirecta','acción positiva','presencia equilibrada'],
 ['acoso sexual','acoso por razón de sexo','negociación colectiva','conciliación laboral'],
 ['violencia física','violencia psicológica','violencia sexual','violencia económica'],
 ['igualdad de trato','seguridad jurídica','jerarquía normativa','autonomía organizativa'],
 ['igualdad de oportunidades','libertad de empresa','protección del patrimonio','estabilidad presupuestaria'],
 ['perspectiva de género','criterio de antigüedad','interés recaudatorio','prioridad presupuestaria'],
 ['lenguaje no sexista','lenguaje exclusivamente técnico','lenguaje reservado','lenguaje exclusivamente jurídico'],
 ['presencia equilibrada','mayoría absoluta','unanimidad','representación exclusivamente masculina'],
 ['corresponsabilidad','competitividad','subordinación','exclusividad'],
 ['conciliación','recaudación','expropiación','prescripción'],
 ['Consejo de Gobierno','Consejo de Ministros','Tribunal Constitucional','Tribunal de Cuentas'],
 ['Instituto Andaluz de la Mujer','Consejo Audiovisual de Andalucía','Defensor del Pueblo','Tribunal Superior de Justicia'],
 ['Consejo Audiovisual de Andalucía','Instituto Andaluz de la Mujer','Consejo de Estado','Tribunal Supremo'],
 ['Consejo Andaluz de Participación de las Mujeres','Consejo de Ministros','Consejo General del Poder Judicial','Tribunal de Cuentas'],
 ['Observatorio','Registro','Tribunal','Secretariado'],
 ['Administraciones públicas','entidades exclusivamente privadas','órganos judiciales exclusivamente','colegios profesionales exclusivamente'],
 ['representación equilibrada','representación exclusiva','mayoría de dos tercios','elección unánime'],
 ['negociación colectiva','subasta pública','expropiación forzosa','revisión constitucional'],
 ['planes de igualdad','planes de urbanismo','planes de recaudación','planes de archivo'],
 ['plan de igualdad','reglamento tributario','inventario patrimonial','presupuesto general'],
 ['informes de impacto de género','informes de recaudación','informes de inventario','informes de archivo histórico'],
 ['informe de impacto de género','informe de tesorería','inventario de bienes','acta de arqueo'],
 ['impacto de género','rango jerárquico','antigüedad documental','densidad urbana'],
 ['desagregados por sexo','sin clasificación alguna','ordenados por antigüedad exclusivamente','agrupados sólo por municipio'],
 ['derecho necesario mínimo indisponible','recomendación sin efectos','derecho máximo negociable','normativa exclusivamente voluntaria'],
 ['protección colectiva','protección individual','protección patrimonial','protección documental'],
 ['protección individual','protección colectiva','protección tributaria','protección electoral'],
 ['riesgo grave e inminente','daño ya consumado','riesgo exclusivamente remoto','riesgo necesariamente leve'],
 ['equipos de trabajo','equipos de protección individual','documentos de constancia','órganos de gobierno'],
 ['equipo de trabajo','equipo de protección individual','documento de decisión','órgano consultivo'],
 ['condición de trabajo','daño derivado del trabajo','documento de constancia','acto de trámite'],
 ['carga de la prueba','competencia territorial','capacidad económica','jerarquía normativa'],
 ['proceso penal','proceso laboral','procedimiento administrativo','proceso civil'],
 ['presunción de inocencia','presunción de culpabilidad','presunción de antigüedad','presunción de unanimidad'],
 ['prescripción','convalidación','conservación','conversión'],
 ['nulidad','anulabilidad','caducidad','incompetencia'],
 ['anulabilidad','nulidad','caducidad','prescripción'],
 ['convalidación','conversión','caducidad','suspensión'],
 ['de oficio','exclusivamente a petición privada','sólo por sentencia firme','sólo por convenio privado'],
 ['medios electrónicos','medios exclusivamente verbales','medios exclusivamente impresos','medios exclusivamente telefónicos'],
 ['personas jurídicas','personas físicas no obligadas','menores de edad exclusivamente','órganos judiciales exclusivamente'],
 ['personas físicas','personas jurídicas exclusivamente','entidades sin personalidad exclusivamente','órganos colegiados exclusivamente'],
 ['registro electrónico','registro exclusivamente manual','archivo histórico','padrón de habitantes'],
 ['notificación','publicación','certificación','digitalización'],
 ['notificaciones','publicaciones','certificaciones','compulsas'],
 ['resolución judicial','orden verbal policial','consentimiento de tercero no autorizado','decisión de empresa privada'],
 ['ley orgánica','ley ordinaria','reglamento municipal','orden ministerial'],
 ['Cortes Generales','Consejo de Ministros','Tribunal Supremo','Consejo de Estado'],
 ['derecho de petición','derecho de propiedad','libertad de empresa','derecho a herencia'],
 ['recurso de amparo','recurso de casación','recurso de reposición','recurso de alzada'],
 ['dominio público','dominio exclusivamente privado','patrimonio exclusivamente histórico','mercado exclusivamente privado'],
 ['servicio público','servicio privado exclusivamente','servicio voluntario sin regulación','servicio mercantil exclusivamente'],
 ['intimidad','publicidad','antigüedad','recaudación'],
 ['confidencialidad','publicidad indiscriminada','difusión obligatoria','identificación pública de víctimas'],
 ['gratuita','de pago obligatorio','limitada a personas jurídicas','condicionada exclusivamente a renta alta'],
 ['graves','leves','muy graves','no sancionables'],
 ['muy graves','graves','leves','no sancionables'],
 ['leves','graves','muy graves','no sancionables'],
 ['deberán','podrán','no podrán','evitarán'],
 ['deberá','podrá','no podrá','evitará'],
 ['garantizarán','prohibirán','suspenderán','eliminarán'],
 ['garantizará','prohibirá','suspenderá','eliminará'],
 ['promoverán','prohibirán','suspenderán','eliminarán'],
 ['promoverá','prohibirá','suspenderá','eliminará'],
 ['fomentarán','prohibirán','restringirán','suspenderán'],
 ['fomentará','prohibirá','restringirá','suspenderá'],
 ['podrán','deberán','no podrán','evitarán'],
 ['podrá','deberá','no podrá','evitará'],
 ['prohibida','autorizada siempre','voluntaria siempre','obligatoria siempre'],
 ['prohibidos','autorizados siempre','voluntarios siempre','obligatorios siempre'],
 ['obligatorio','voluntario','prohibido','excepcionalmente opcional'],
 ['obligatoria','voluntaria','prohibida','excepcionalmente opcional'],
 ['prevención','sanción','recaudación','expropiación'],
 ['formación','recaudación','fiscalización tributaria','expropiación'],
 ['coeducación','segregación obligatoria','evaluación tributaria','ordenación registral'],
 ['accesibilidad','exclusividad','confiscación','jerarquización'],
 ['participación','subordinación','exclusión','confiscación'],
 ['maternidad','antigüedad tributaria','propiedad inmobiliaria','rango administrativo'],
 ['embarazo','recargo tributario','rango jerárquico','estado civil exclusivamente'],
 ['lactancia','recaudación','sucesión patrimonial','antigüedad documental'],
 ['vivienda','tributación','contratación mercantil exclusivamente','propiedad intelectual exclusivamente'],
 ['salud','patrimonio','tesorería','urbanismo exclusivamente'],
 ['educación','recaudación','expropiación','archivo histórico'],
 ['cultura','recaudación','inspección tributaria','registro mercantil'],
 ['deporte','recaudación','expropiación','tesorería'],
 ['empleo','patrimonio exclusivamente','catastro exclusivamente','sanción exclusivamente'],
 ['estadísticas','sanciones','expropiaciones','resoluciones judiciales'],
 ['asistencia social integral','asistencia exclusivamente tributaria','asistencia sólo documental','asistencia exclusivamente mercantil'],
 ['asistencia jurídica','recaudación tributaria','certificación catastral','inspección patrimonial'],
 ['seguridad y salud','productividad exclusivamente','recaudación exclusivamente','antigüedad exclusivamente'],
 ['probabilidad','antigüedad documental','rango jerárquico','número de registros'],
 ['severidad','antigüedad documental','rango jerárquico','número de oficinas'],
]
TIME=['diez días','quince días','tres meses','seis meses','cuatro años','cinco años','un año','dos años','tres años','dieciocho meses','doce meses','seis meses','veinticuatro meses','setenta y dos horas']
NUMSETS=[['cuarenta por ciento','sesenta por ciento','treinta por ciento','setenta y cinco por ciento'],['50','25','100','250'],['6.000','60.000','120.000','600'],['60.001','6.001','120.001','600.001'],['120.000','60.000','6.000','600'],['treinta por ciento','veinte por ciento','cuarenta por ciento','cincuenta por ciento']]
SETS=NUMSETS+[TIME]+SETS
# Topics -> legal text boundaries, 1-indexed original extracted lines.
SPECS=[(1,'Constitución Española', 'tema1.txt',243,None,6),
       (2,'LO 3/2007','tema2.txt',389,1055,33),
       (2,'LO 1/2004','tema2.txt',1056,1486,33),
       (2,'Ley 12/2007 de Andalucía','tema2.txt',1491,2984,33),
       (2,'Ley 13/2007 de Andalucía','tema2.txt',2993,4050,33),
       (3,'Ley 31/1995','tema3.txt',197,None,132),
       (4,'RD 208/1996','tema4.txt',200,417,140),
       (4,'Ley 39/2015','tema4.txt',420,861,140),
       (5,'Ley 39/2015','tema5.txt',316,None,164)]

def clean_line(line):
    if re.match(r'^=====|^SUBALTERNO|^Todos los derechos|^T[ÍI]TULO|^CAP[ÍI]TULO|^SECCI[ÓO]N|^Sección|^¡IMPORTANTE|^Ejemplo|^Conclusión',line):return ''
    if line.isupper() and len(line)>8:return ''
    return line.strip()

def matches(sentence):
    candidates=[]
    for priority,choices in enumerate(SETS):
        for target in choices:
            m=re.search(r'(?<!\w)'+re.escape(target)+r'(?!\w)',sentence,re.I)
            if m:
                wrong=list(dict.fromkeys(x for x in choices if x.lower()!=target.lower()))
                if len(wrong)>=3:candidates.append((m.start(),m.end(),m.group(),wrong[:3],priority))
    # Prefer a whole phrase such as «muy graves» or «no podrá» over its fragment.
    candidates=[m for m in candidates if not any(n[0]<=m[0] and n[1]>=m[1] and n[1]-n[0]>m[1]-m[0] for n in candidates)]
    found=[]
    for m in sorted(candidates,key=lambda x:x[4]):
        if not any(m[0]<e and m[1]>b for b,e,*_ in found):found.append(m[:4])
    return found

def extract():
    result=[];seen=set()
    for topic,law,file,start,end,page0 in SPECS:
        lines=(TEXT/file).read_text().splitlines();page=page0;blocks=[];article=None;title='';buf=[];firstpage=page
        def finish():
            if article and buf:blocks.append((article,title,firstpage,' '.join(buf)))
        for idx,line in enumerate(lines,1):
            p=re.search(r'===== PÁGINA (\d+)',line)
            if p:page=int(p.group(1))
            if idx<start or (end and idx>end):continue
            h=re.match(r'^(?=A)Art[íi]culo\s+(\d+)(?:\s+(bis|ter|quater))?(?:\.\s*|\s+(?=\()|$)(.*)',line,re.I)
            if h:
                finish();article=h.group(1)+(' '+h.group(2).lower() if h.group(2) else '');title=h.group(3).strip().rstrip('.');buf=[];firstpage=page;continue
            line=clean_line(line)
            if line and article:buf.append(line)
        finish()
        for art,title,p,text in blocks:
            text=re.sub(r'\([^)]*EXAMEN[^)]*\)','',text,flags=re.I)
            text=re.sub(r'\b(?:EXAMEN|EXAMENES|IMPORTANTE)\b','',text)
            # Entire sentences/subsections only; do not drop qualifying clauses.
            sentences=re.split(r'(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÑ0-9])|\s+(?=[a-z]\)\s)',text)
            for sentence in sentences:
                sentence=re.sub(r'^(?:\d+\.|[a-z]\))\s*','',sentence).strip()
                sentence=re.sub(r'\s+',' ',sentence)
                words=sentence.split()
                if not 9<=len(words)<=95 or len(sentence)>780:continue
                if any(x in sentence for x in ['Ejemplo','¡','📌','→','>>','Por ejemplo']):continue
                if not re.search(r'[.!?]$',sentence):continue
                ms=matches(sentence)
                # At most two targets, in different meaningful locations, in longer clauses.
                chosen=ms[:1]
                if len(words)>=28 and len(ms)>1:
                    for m in ms[1:]:
                        if abs(m[0]-chosen[0][0])>=35:chosen.append(m);break
                for a,b,correct,wrong in chosen:
                    key=(law,art,sentence,a)
                    if key in seen:continue
                    seen.add(key)
                    prompt=f'{law}, artículo {art}. Completa la regla: «{sentence[:a]}____{sentence[b:]}»'
                    result.append(dict(topic=topic,section=f'{law}: artículo {art}',prompt=prompt,correct=correct,wrong=wrong,
                        explanation=f'El artículo {art} recoge: «{sentence}»',source={'kind':'manual','label':'Temario · septiembre 2026','reference':f'PDF {p} · {law}, art. {art}'},format='literal',coverage=f'{law}:{art}'))
    return result

if __name__=='__main__':
    result=extract();(ROOT/'data/legal-candidates.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
    print('Literal candidates:',dict(sorted(collections.Counter(q['topic'] for q in result).items())))
    print('Legal articles:',dict(sorted(collections.Counter(set((q['topic'],q['coverage']) for q in result)).items())) if False else len(set((q['topic'],q['coverage']) for q in result)))
