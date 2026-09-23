#!/usr/bin/env python3
"""Temporary read-only inspection of already accepted benchmark sources.
No model calls, paid services, credentials, or canonical mutations.
"""
import concurrent.futures
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import time
import urllib.error
import urllib.request

ROOT=Path(__file__).resolve().parents[1]
class Reader(HTMLParser):
    def __init__(self):
        super().__init__(); self.parts=[]; self.skip=0
    def handle_starttag(self,tag,attrs):
        if tag in ('script','style'): self.skip+=1
        if tag in ('p','h1','h2','h3','h4','figcaption','tr','table','figure'): self.parts.append('\n')
        if tag in ('td','th'): self.parts.append(' | ')
    def handle_endtag(self,tag):
        if tag in ('script','style'): self.skip=max(0,self.skip-1)
        if tag in ('p','h1','h2','h3','h4','figcaption','tr','table','figure'): self.parts.append('\n')
    def handle_data(self,data):
        if not self.skip: self.parts.append(data)

def inspect(r):
    a=r.get('artifacts',{}); urls=[a.get('preprint',''),a.get('paper','')]
    arxiv=next((re.search(r'arxiv\.org/(?:abs|html|pdf)/(\d{4}\.\d{4,5})',u) for u in urls if re.search(r'arxiv\.org/(?:abs|html|pdf)/(\d{4}\.\d{4,5})',u)),None)
    if not arxiv:
        return {'id':r['id'],'status':'no-arxiv-link-in-canonical-artifacts'}
    source='https://arxiv.org/html/'+arxiv.group(1)+'v1'
    try:
        request=urllib.request.Request(source,headers={'User-Agent':'Agent-Benchmark-Radar historical-reference audit (read-only)'})
        with urllib.request.urlopen(request,timeout=12) as response:
            if 'html' not in response.headers.get('Content-Type',''): raise ValueError('Not HTML')
            raw=response.read(5000000).decode('utf-8','replace')
        parser=Reader(); parser.feed(raw)
        text=''.join(parser.parts)
        lines=[re.sub(r'\s+',' ',x).strip() for x in text.splitlines() if x.strip()]
        # Show actual result tables and prose, with bounded primary-source context.
        blocks=[]
        for m in re.finditer(r'<figure\b[^>]*class="[^"]*ltx_table[^"]*"[^>]*>.*?</figure>',raw,re.S):
            pp=Reader(); pp.feed(m.group(0)); t='\n'.join(re.sub(r'\s+',' ',x).strip() for x in ''.join(pp.parts).splitlines() if x.strip())
            if re.search(r'result|performance|accuracy|comparison|evaluation|score|success',t[:900],re.I) and not re.search(r'dataset statistics|statistical comparison|comparison.*(?:existing benchmarks|memory benchmarks)',t[:500],re.I):
                blocks.append(t[:8000])
        snippets=[x for x in lines if re.search(r'\d',x) and re.search(r'best|highest|strongest|achieve|reach|accuracy|success rate|overall|F1',x,re.I) and not x.startswith('|') and len(x)>40 and len(x)<2500]
        return {'id':r['id'],'source':source,'status':'read','tables':blocks[:2],'snippets':snippets[:3]}
    except Exception as e:
        return {'id':r['id'],'source':source,'status':'unavailable','error':str(e)[:180]}
    finally:
        time.sleep(1.1)

records=json.loads((ROOT/'data/benchmarks.json').read_text())
# Read unfilled sources first; well-known launch references were inspected separately.
skip={'locomo','longmemeval','membench','memoryagentbench','beam','ama-bench','pm-bench','wikisql','spider','ds-1000','bird','spider-2','mle-bench','datascibench','livedrbench'}
for area in ('agent-memory','rag','data-agent'):
    group=[r for r in records if r['area']==area and r['id'] not in skip]
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        for result in pool.map(inspect,group):
            print('PRIMARY_RESULT_EVIDENCE '+json.dumps(result,ensure_ascii=False,separators=(',',':')),flush=True)
print('SOURCE_INSPECTION_COMPLETE; no canonical data or notes were modified.')
