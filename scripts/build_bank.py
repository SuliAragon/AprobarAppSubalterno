"""Genera el banco completo de forma reproducible y comprueba sus invariantes."""
from pathlib import Path
import json,random,hashlib,collections,re
from facts import GROUPS
from math_seeds import MATH
from exam_seeds import EXAMS
ROOT=Path(__file__).resolve().parents[1]
QUOTAS={1:240,2:780,3:160,4:340,5:240,6:280,7:200,8:300,9:300,10:160}
LEGAL_QUOTAS={1:50,2:400,3:25,4:120,5:80}
rng=random.Random(20260930)

def signature(q):return json.dumps([re.sub(r'\s+',' ',q['prompt']).strip(),sorted([q['correct']]+q['wrong'])],ensure_ascii=False)
def meta(g,format,key):return dict(topic=g['topic'],section=g['section'],source={'kind':'manual','label':'Temario · septiembre 2026','reference':g['reference']},format=format,coverage=f"fact:{g['section']}:{key}")
primary=[];extras=[]
for g in GROUPS:
    rows=g['rows'];values=list(dict.fromkeys(v for k,v in rows));keys=[k for k,v in rows]
    assert len(values)>=4,g['section']
    for i,(key,value) in enumerate(rows):
        wrong=rng.sample([v for v in values if v!=value],3)
        explanation=f'{key[0].upper()+key[1:]}: {value}. '+g['note']
        primary.append(dict(**meta(g,'supuesto' if 'supuestos' in g['section'].lower() else 'concepto',key),prompt=g['direct'].format(key=key,value=value),correct=value,wrong=wrong,explanation=explanation.strip()))
        if sum(v==value for k,v in rows)==1:
            extras.append(dict(**meta(g,'relación',key),prompt=g['reverse'].format(key=key,value=value),correct=key[0].upper()+key[1:],wrong=[k[0].upper()+k[1:] for k in rng.sample([k for k in keys if k!=key],3)],explanation=explanation.strip()))
        # Pares de claves y atributos exactos, con distractores cruzados.
        indices=[i]+rng.sample([j for j in range(len(rows)) if j!=i],3)
        chosen=[rows[j] for j in indices]
        wrongpairs=[]
        for a,(k,v) in enumerate(chosen[1:],1):
            choices=[xv for xk,xv in rows if xv!=v]
            wrongpairs.append(f'{k[0].upper()+k[1:]} → {rng.choice(choices)}')
        extras.append(dict(**meta(g,'relación',key),prompt=f'En «{g["section"]}», ¿qué asociación está correctamente establecida?',correct=f'{key[0].upper()+key[1:]} → {value}',wrong=wrongpairs,explanation=explanation.strip()))
        falsevalue=rng.choice([v for v in values if v!=value])
        truepairs=[f'{k[0].upper()+k[1:]} → {v}' for k,v in chosen[1:]]
        extras.append(dict(**meta(g,'relación',key),prompt=f'Al repasar «{g["section"]}», señala la asociación incorrecta.',correct=f'{key[0].upper()+key[1:]} → {falsevalue}',wrong=truepairs,explanation=f'La asociación incorrecta atribuye «{falsevalue}» a {key}. Lo que corresponde es «{value}». '+g['note']))

legal=json.loads((ROOT/'data/legal-candidates.json').read_text())
selected=[];seen=set()
def include(q):
    s=signature(q)
    if s in seen:return False
    assert len(set([q['correct']]+q['wrong']))==4,(q['prompt'],q['correct'],q['wrong'])
    seen.add(s);selected.append(q);return True
for topic,quota in QUOTAS.items():
    start=len(selected)
    # Every authored atomic fact and every exam adaptation is represented.
    for q in [q for q in primary+EXAMS if q['topic']==topic]:include(q)
    if topic==8:
        bysection=collections.defaultdict(list)
        for q in MATH:bysection[q['section']].append(q)
        for pool in bysection.values():rng.shuffle(pool)
        mathchoices=[]
        while len(mathchoices)<160:
            for section,pool in bysection.items():
                if pool and len(mathchoices)<160:mathchoices.append(pool.pop())
        for q in mathchoices:include(q)
    if topic in LEGAL_QUOTAS:
        pool=[q for q in legal if q['topic']==topic];rng.shuffle(pool)
        # One question per legal article where possible, then extra distinct rules.
        articles={}
        for q in pool:articles.setdefault(q['coverage'],q)
        mandatory=list(articles.values());rng.shuffle(mandatory)
        n=0
        for q in mandatory:
            if n>=LEGAL_QUOTAS[topic]:break
            if include(q):n+=1
        for q in pool:
            if n>=LEGAL_QUOTAS[topic]:break
            if include(q):n+=1
        assert n==LEGAL_QUOTAS[topic],(topic,n)
    available=[q for q in extras if q['topic']==topic];rng.shuffle(available)
    for q in available:
        if len(selected)-start==quota:break
        include(q)
    assert len(selected)-start==quota,(topic,len(selected)-start,quota)

bank=[]
for topic,quota in QUOTAS.items():
    pool=[q for q in selected if q['topic']==topic];rng.shuffle(pool)
    positions=[pos for pos in range(4) for _ in range(quota//4)];rng.shuffle(positions)
    for q,pos in zip(pool,positions):
        wrong=q['wrong'][:];rng.shuffle(wrong);options=wrong[:pos]+[q['correct']]+wrong[pos:]
        qid=hashlib.sha256(signature(q).encode()).hexdigest()[:14]
        bank.append({k:q[k] for k in ['topic','section','prompt','explanation','source','format']}|{'id':f't{topic:02d}-{qid}','options':options,'answer':pos})
rng.shuffle(bank)
assert len(bank)==3000
assert len({q['id'] for q in bank})==3000
assert collections.Counter(q['answer'] for q in bank)=={0:750,1:750,2:750,3:750}
(ROOT/'public/questions.json').write_text(json.dumps(bank,ensure_ascii=False,separators=(',',':'))+'\n')
report={'total':len(bank),'answerDistribution':{chr(65+k):v for k,v in sorted(collections.Counter(q['answer'] for q in bank).items())},
 'topics':[],'formats':dict(collections.Counter(q['format'] for q in bank)),'examAdaptations':sum(q['source']['kind']=='exam-adapted' for q in bank),
 'uniqueIds':len({q['id'] for q in bank}),'uniqueQuestionSets':len({json.dumps([q['prompt'],sorted(q['options'])],ensure_ascii=False) for q in bank}),
 'authoredFacts':len(primary),'coveredAuthoredFacts':len({q['coverage'] for q in selected if q['coverage'].startswith('fact:')}),
 'legalArticles':len({q['coverage'] for q in selected if q['format']=='literal'})}
for topic,quota in QUOTAS.items():
 pool=[q for q in bank if q['topic']==topic]
 report['topics'].append({'topic':topic,'count':len(pool),'answers':[sum(q['answer']==k for q in pool) for k in range(4)],'sections':sorted({q['section'] for q in pool})})
(ROOT/'data/bank-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='topics'},ensure_ascii=False,indent=2))
print('Topic counts:',{q['topic']:q['count'] for q in report['topics']})
