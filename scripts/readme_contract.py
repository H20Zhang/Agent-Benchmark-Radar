"""Reader-facing invariants, independent of the dormant website and template wording."""
from __future__ import annotations
import calendar
from datetime import date
from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
AREAS=('agent-memory','rag','data-agent')
ID=re.compile(r'<!--\s*benchmark-id:([a-z0-9-]+)\s*-->')
LINK=re.compile(r'\[[^\]]*\]\(([^)]+)\)')

def release(record):
    for field in ('first_public_at','publication_at','data_release_at'):
        if record.get(field):return record[field],field,record.get('release_date_evidence',{}).get(field,{}).get('source')
    d=record.get('release_date_evidence',{}).get('legacy_recorded_at',{})
    return d.get('date',record['released']),'legacy_recorded_at',d.get('source')

def table_block(text,label):
    a,b=f'<!-- {label}:START -->',f'<!-- {label}:END -->'
    if text.count(a)!=1 or text.count(b)!=1:raise ValueError(f'expected exactly one {label} block')
    return text.split(a,1)[1].split(b,1)[0]

def validate(zh,en,records):
    errors=[]
    locales=json.loads((ROOT/'data/locales/zh/benchmarks.json').read_text())
    end=date.fromisoformat(json.loads((ROOT/'data/freshness.json').read_text())['discovery_scan_at'])
    m=end.year*12+end.month-1-6;y,month=divmod(m,12);month+=1
    start=date(y,month,min(end.day,calendar.monthrange(y,month)[1]))
    by_id={x['id']:x for x in records}
    def in_window(x):
        value=release(x)[0]
        lo=date.fromisoformat(value+'-01' if len(value)==7 else value)
        hi=date(lo.year,lo.month,calendar.monthrange(lo.year,lo.month)[1]) if len(value)==7 else lo
        return lo<=end and hi>=start
    observations={}
    for filename,text,lang in [('README.md',zh,'zh'),('README.en.md',en,'en')]:
        def fail(message):errors.append(f'{filename}: {message}')
        if 'h20zhang.github.io/Agent-Benchmark-Radar' in text:fail('retired website link returned')
        for word in ('## 最新条目深读','## Three Areas','## 三个方向的演化'):
            if word in text:fail('retired reader surface returned: '+word)
        ids=re.findall(r'<a id="([^"]+)"></a>',text)
        if len(ids)!=len(set(ids)):fail('duplicate local anchors')
        needed=('top','release-timeline','all-benchmarks','registry-memory','registry-rag','registry-data','reading-paths','evaluation-frontiers','library')
        positions=[]
        for target in needed:
            marker=f'<a id="{target}"></a>'
            if text.count(marker)!=1:fail('missing or duplicate '+target)
            else:positions.append(text.index(marker))
        if positions!=sorted(positions):fail('timeline / complete registry / optional reading order drift')
        if not f'{start.isoformat()} — {end.isoformat()}' in text:fail('date window drift')
        for target in LINK.findall(re.sub(r'<!--[\s\S]*?-->','',text)):
            if target.startswith('#') and target[1:] not in ids:fail('missing anchor '+target)
        for label in ('TABLE-FIRST:RECENT',*(f'TABLE-FIRST:AREA:{a}' for a in AREAS)):
            try:body=table_block(text,label)
            except ValueError as ex:fail(str(ex));continue
            columns=4 if label.endswith('RECENT') else 5
            if 'What changed' in body or '带来的变化' in body:fail('parallel change column returned')
            rows=[line for line in body.splitlines() if ID.search(line)]
            found=[ID.search(line)[1] for line in rows]
            expected=[x['id'] for x in records if (in_window(x) if label.endswith('RECENT') else x['area']==label.split(':')[-1])]
            if set(found)!=set(expected) or len(found)!=len(expected):fail(label+' missing, duplicate or unexpected canonical ids')
            observations[(lang,label)]=found
            recorded_dates=[release(by_id[i])[0] for i in found if i in by_id]
            if recorded_dates!=sorted(recorded_dates,reverse=True):fail(label+' not chronological')
            for line in [l for l in body.splitlines() if l.startswith('|')]:
                if len(line.split('|')[1:-1])!=columns:fail(label+f' must have exactly {columns} visible columns')
            for line in rows:
                ident=ID.search(line)[1]
                if ident not in by_id:continue
                x=by_id[ident]; cells=[re.sub(r'<!--.*?-->','',v).strip() for v in line.split('|')[1:-1]]
                if len(cells)!=columns:continue
                description=cells[2]
                expected_description=locales[ident]['summary'] if lang=='zh' else x['summary']
                if description!=expected_description.replace('|','&#124;').replace('\n',' '):fail(ident+' canonical summary drift')
                value,kind,source=release(x)
                links=LINK.findall(line)
                if f'[{value}'+('†' if kind=='legacy_recorded_at' else '') not in cells[0]:fail(ident+' release date/type drift')
                note=f'benchmarks/{ident}{".en" if lang=="en" else ""}.md'
                if note not in links:fail(ident+' has no direct reading note')
                if not (ROOT/note).is_file():fail(ident+' reading note does not exist')
                if source and source not in links:fail(ident+' date source missing')
                for key in ('paper','code','data','project','leaderboard'):
                    url=x.get('artifacts',{}).get(key)
                    if url and url not in links:fail(ident+' missing '+key+' resource')
                if columns==5:
                    c=x.get('citations',{})
                    if c.get('status')=='ok':
                        if cells[4]!=f'[{c["count"]:,}]({c["url"]})':fail(ident+' citation drift')
                    elif cells[4]!='—':fail(ident+' unknown citations must not become zero')
    for label in ('TABLE-FIRST:RECENT',*(f'TABLE-FIRST:AREA:{a}' for a in AREAS)):
        if observations.get(('zh',label))!=observations.get(('en',label)):errors.append('Chinese/English identity or order drift: '+label)
    return errors
