"""Rendered publication regression gate. Local --offline renders exact build bytes;
CI uses a real HTTP origin for navigation, reload, history and language round-trips.
"""
import argparse, asyncio, base64, contextlib, functools, http.server, json, os, re, threading
from pathlib import Path
from urllib.parse import urljoin, urlsplit, unquote, parse_qs
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[2]
DIST=ROOT/'web/dist'; BASE='/Agent-Benchmark-Radar'
PRIMARY=['','timeline/','benchmarks/','evaluate/','compare/','frontier/','opportunities/','methodology/','areas/agent-memory/','areas/rag/','areas/data-agent/']

def static_audit():
    pages={BASE+'/'+p.parent.relative_to(DIST).as_posix().strip('./')+'/':p for p in DIST.rglob('index.html')}
    pages={k.replace('//','/'):v for k,v in pages.items()}
    parsed={k:BeautifulSoup(p.read_text(),'html.parser') for k,p in pages.items()}
    errors=[]
    for path,soup in parsed.items():
        def require(condition,message):
            if not condition: errors.append(f'{path}: {message}')
        require(len(soup.find_all('h1'))==1,'exactly one h1')
        require(soup.find('main') is not None,'main landmark')
        ids=[el['id'] for el in soup.select('[id]')]
        require(len(ids)==len(set(ids)),'duplicate element id')
        text=soup.get_text(' ',strip=True)
        require('RESEARCH-DECISION:' not in text,'maintenance marker leaked')
        require(not re.search(r'\]\([^)]*\.md(?:#[^)]*)?\)',text),'unrendered relative Markdown link')
        if path!=BASE+'/':
            require(soup.select_one('meta[name="robots"]').get('content')=='index,follow','public page not indexable')
            require(soup.select_one('link[rel="canonical"]').get('href')=='https://h20zhang.github.io'+path,'canonical mismatch')
        for a in soup.select('a[href],link[rel="alternate"][href]'):
            url=urlsplit(urljoin('https://h20zhang.github.io'+path,a['href']))
            if url.netloc!='h20zhang.github.io' or not url.path.startswith(BASE+'/'):continue
            target=unquote(url.path)
            if not target.endswith('/'):target+='/'
            if target not in parsed:
                # Non-HTML static resources may be linked.
                resource=DIST/unquote(url.path[len(BASE)+1:])
                require(resource.is_file(),f'missing internal target {a["href"]}')
            elif url.fragment:
                require(parsed[target].find(id=unquote(url.fragment)) is not None,f'missing fragment {a["href"]}')
    assert not errors,'\n'.join(errors[:60])
    registry=json.loads((ROOT/'data/benchmarks.json').read_text())
    for lang in ['zh','en']:
        timeline=parsed[f'{BASE}/{lang}/timeline/']
        require_ids={r['id'] for r in registry if r['status'] in ['active','verified']}
        assert {r['data-id'] for r in timeline.select('[data-timeline-record]')}==require_ids
        library=parsed[f'{BASE}/{lang}/benchmarks/']
        assert {r['data-benchmark-id'] for r in library.select('[data-benchmark-id]')}=={r['id'] for r in registry}
        for item in registry:assert f'{BASE}/{lang}/benchmarks/{item["id"]}/' in parsed
    sources=list((ROOT/'data/results').glob('*.json'))
    budget_count=0
    for file in sources:
        record=json.loads(file.read_text())
        for lang in ['zh','en']:
            panel=parsed[f'{BASE}/{lang}/benchmarks/{record["benchmark_id"]}/'].select_one('#results')
            assert panel is not None, f'{record["benchmark_id"]}: missing result panel'
            rendered=panel.get_text(' ',strip=True)
            for track in record['tracks']:
                for entry in track['entries']:
                    for key in ['budget','context']:
                        if entry.get(key):
                            assert entry[key] in rendered, f'{record["benchmark_id"]}/{lang}: dropped {key}'
                            if key=='budget':budget_count+=1
    zh_cards=parsed[f'{BASE}/zh/benchmarks/'].select('[data-benchmark-id]')
    en_cards=parsed[f'{BASE}/en/benchmarks/'].select('[data-benchmark-id]')
    assert {e['data-benchmark-id']:e['data-search'] for e in zh_cards}=={e['data-benchmark-id']:e['data-search'] for e in en_cards},'search corpus differs across languages'
    print(f'Preserved {budget_count} bilingual entry budgets; bilingual search corpus identical.',flush=True)
    return {'html_pages':len(parsed),'benchmark_details':2*len(registry),'internal_links':'all targets and fragments resolved'},pages

@functools.lru_cache(None)
def module_data(path):
    source=path.read_text()
    source=re.sub(r'(from|import)([\"\'])(\./[^\"\']+)\2',lambda m:m[1]+m[2]+module_data((path.parent/m[3]).resolve())+m[2],source)
    return 'data:text/javascript;base64,'+base64.b64encode(source.encode()).decode()

def offline_document(relative):
    soup=BeautifulSoup((DIST/relative/'index.html').read_text(),'html.parser')
    for link in soup.select('link[rel="stylesheet"]'):
        style=soup.new_tag('style');style.string=(DIST/link['href'].split(BASE+'/')[1]).read_text();link.replace_with(style)
    scripts=soup.select('script[src]')
    for script in scripts:
        url=module_data((DIST/script['src'].split(BASE+'/')[1]).resolve());del script['src']
        script.string=f'import "{url}"; window.__verifyModules++;'
    soup.head.insert(0,soup.new_tag('base',href='https://h20zhang.github.io'+BASE+'/'+relative+'/'))
    shim=soup.new_tag('script');shim.string='window.__verifyModules=0;window.__historyWrites=[];history.replaceState=function(s,t,u){window.__historyWrites.push(u)};history.pushState=history.replaceState;';soup.head.insert(1,shim)
    return str(soup),len(scripts)

class Handler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self,path):
        clean=unquote(urlsplit(path).path)
        if clean.startswith(BASE+'/'):clean=clean[len(BASE)+1:]
        return str(DIST/clean.lstrip('/'))
    def log_message(self,*args):pass

async def browser_audit(args,pages,origin):
    metrics=[];checks=[];errors=[]
    async with async_playwright() as p:
        executable=os.environ.get('CHROMIUM_EXECUTABLE') or ('/usr/bin/chromium' if Path('/usr/bin/chromium').exists() else None)
        browser=await p.chromium.launch(executable_path=executable,args=['--no-sandbox','--disable-dev-shm-usage'])
        async def load(context,relative,query=''):
            page=await context.new_page();page.on('pageerror',lambda error:errors.append(f'{relative}: {error}'))
            if args.offline:
                html,count=offline_document(relative.rstrip('/'));await page.set_content(html)
                await page.wait_for_function('(n)=>window.__verifyModules===n',arg=count)
            else:
                await page.goto(origin+BASE+'/'+relative+query,wait_until='load')
            return page
        async def measure(page,path,viewport):
            result=await page.evaluate("""() => ({scrollWidth:document.documentElement.scrollWidth,viewport:innerWidth,height:document.documentElement.scrollHeight,h1Size:parseFloat(getComputedStyle(document.querySelector('h1')).fontSize),h1Height:document.querySelector('h1').getBoundingClientRect().height,nav:[...document.querySelectorAll('.site-nav>a')].map(e=>({text:e.textContent,visible:!!e.getClientRects().length,href:e.getAttribute('href')})),firstRecord:document.querySelector('[data-timeline-record]:not([hidden])')?.getBoundingClientRect().y,proseDisplay:document.querySelector('.deep-read__content')?getComputedStyle(document.querySelector('.deep-read__content')).display:null})""")
            assert result['scrollWidth']<=result['viewport']+1,f'{path}/{viewport} document overflow: {result}'
            assert result['h1Size']<=48,f'{path}: oversized h1 {result}'
            if result['nav']:assert len(result['nav'])>=7 and all(n['visible'] for n in result['nav']),f'{path}: missing nav'
            if result['proseDisplay']:assert result['proseDisplay']=='block',f'{path}: prose not normal flow'
            if result.get('firstRecord') is not None and viewport==390:assert result['firstRecord']<844,f'{path}: no first-fold record'
            metrics.append({'path':path,'width':viewport,**result})
        for width in [390,768,1440]:
            context=await browser.new_context(viewport={'width':width,'height':844 if width==390 else 1000},locale='zh-CN')
            for lang in ['zh','en']:
                for route in PRIMARY:
                    relative=f'{lang}/{route}';page=await load(context,relative)
                    await measure(page,relative,width)
                    if args.output:
                        await page.screenshot(path=str(args.output/f'{lang}-{route.strip("/").replace("/","-") or "home"}-{width}.png'))
                    await page.close()
            await context.close()
        # Render every non-primary content route at a narrow viewport: catch data-specific overflows.
        context=await browser.new_context(viewport={'width':390,'height':844})
        primary={f'{lang}/{r}' for lang in ['zh','en'] for r in PRIMARY}
        for path in sorted(pages):
            relative=path[len(BASE)+1:]
            if not relative or relative in primary:continue
            page=await load(context,relative);await measure(page,relative,390);await page.close()
        await context.close()
        context=await browser.new_context(viewport={'width':1440,'height':1000})
        page=await load(context,'zh/benchmarks/')
        async def assert_count(n):
            await page.wait_for_function('(n)=>Number(document.querySelector("[data-result-count]").textContent)===n',arg=n)
            assert await page.locator('[data-benchmark-id]:visible').count()==n,'visible result set differs from counter'
        await page.locator('input[name=q]').fill('zzzz_no_match_09876');await assert_count(0)
        if args.output:await page.screenshot(path=str(args.output/'regression-filter-zero.png'))
        checks.append('zero query => zero visible cards, zero count')
        await page.locator('[data-filter-form] button[type=reset]').click();await assert_count(131)
        facets=json.loads((ROOT/'data/taxonomy.json').read_text())['facets']
        keys=[f'{f["id"]}:{o["id"]}' for id in ['conversation','answer-quality'] for f in facets for o in f['options'] if o['id']==id]
        await page.locator('details.refine-panel > summary').click()
        for key in keys:
            control=page.locator(f'input[name=facet][value="{key}"]')
            await control.evaluate('(e)=>e.closest("details").open=true');await control.check()
        await assert_count(16);checks.append('cross-facet intersection => 16 visible records')
        if args.output:await page.screenshot(path=str(args.output/'regression-filter-intersection.png'))
        if not args.offline:
            selected=await page.locator('[data-benchmark-id]:visible').evaluate_all('(es)=>es.map(e=>e.dataset.benchmarkId).sort()')
            await page.reload();await assert_count(16)
            assert selected==await page.locator('[data-benchmark-id]:visible').evaluate_all('(es)=>es.map(e=>e.dataset.benchmarkId).sort()')
            await page.locator('[data-language-path]').click();await assert_count(16)
            checks.append('filter reload and language switch preserve exact visible IDs')
        await page.close()
        page=await load(context,'zh/evaluate/')
        await page.locator('[data-recipe="memory-governance"]').click()
        assert await page.locator('[data-suite-selection] li').count()==4
        compare_url=await page.locator('[data-compare-suite]').get_attribute('href')
        assert len(parse_qs(urlsplit(compare_url).query)['benchmark'])==4
        checks.append('four-item governance suite => four-item comparison URL')
        await page.locator('[data-suite-selection] button').first.click()
        assert '自定义' in await page.locator('[data-suite-title]').inner_text()
        assert '原研究主张不适用' in await page.locator('[data-suite-boundary]').inner_text()
        if not args.offline:
            await page.reload();assert await page.locator('[data-suite-selection] li').count()==3
            assert '自定义' in await page.locator('[data-suite-title]').inner_text()
            checks.append('custom suite survives reload without regaining original claim')
        while await page.locator('[data-suite-selection] button').count():await page.locator('[data-suite-selection] button').first.click()
        assert await page.locator('[data-copy-suite]').is_disabled()
        assert await page.locator('[data-compare-suite]').get_attribute('href') is None
        if args.output:await page.screenshot(path=str(args.output/'regression-suite-empty.png'))
        checks.append('empty suite invalidates claim and disables export / comparison')
        if not args.offline:
            await page.reload();assert await page.locator('[data-suite-selection] li').count()==0
            await page.goto(origin+compare_url)
            assert await page.locator('table thead th').count()==5
            assert 'The Compaction Cliff' in await page.locator('table thead').inner_text()
            await page.locator('[data-language-path]').click()
            assert await page.locator('table thead th').count()==5
            await page.goto(origin+BASE+'/zh/evaluate/?area=data-agent')
            assert 'data-sql' in page.url and 'Text-to-SQL' in await page.locator('[data-suite-title]').inner_text()
            await page.locator('[data-recipe="memory-governance"]').click()
            await page.go_back();assert 'Text-to-SQL' in await page.locator('[data-suite-title]').inner_text()
            checks.append('four comparison columns, language state, area deep link, back/forward verified')
        await page.close()
        page=await load(context,'zh/timeline/')
        await page.locator('select[name=window]').select_option('all')
        assert await page.locator('[data-timeline-record]:visible').count()==131
        await page.locator('select[name=area]').select_option('data-agent')
        assert await page.locator('[data-timeline-record]:visible').count()==36
        await page.locator('select[name=area]').select_option('')
        await page.locator('select[name=month]').select_option('2024-02')
        assert await page.locator('[data-timeline-record][data-id=locomo]').is_visible()
        checks.append('timeline all history / area / corrected month filtering')
        if not args.offline:
            await page.reload();assert await page.locator('[data-timeline-record][data-id=locomo]').is_visible()
            checks.append('timeline month state survives reload')
        await page.close()
        page=await load(context,'zh/benchmarks/structmemeval/')
        assert '这些能力尚未覆盖。' in await page.locator('.deep-read__content').inner_text()
        await page.locator('#interpretation').scroll_into_view_if_needed()
        if args.output:await page.screenshot(path=str(args.output/'regression-prose-flow.png'))
        checks.append('authored negation preserved in normal document flow')
        if not args.offline:
            # Use actual canonical URLs: set_content cannot validate URL hydration or history.
            await page.goto(origin+BASE+'/zh/benchmarks/?capability=temporal-reasoning&year=2024&year=2026')
            initial_ids=await page.locator('[data-benchmark-id]:visible').evaluate_all('(es)=>es.map(e=>e.dataset.benchmarkId).sort()')
            assert initial_ids, 'legacy filter became empty unexpectedly'
            await page.locator('select[name=sort]').select_option('name')
            assert parse_qs(urlsplit(page.url).query)['capability']==['temporal-reasoning']
            assert set(parse_qs(urlsplit(page.url).query)['year'])=={'2024','2026'}
            assert initial_ids==await page.locator('[data-benchmark-id]:visible').evaluate_all('(es)=>es.map(e=>e.dataset.benchmarkId).sort()')
            await page.reload()
            assert initial_ids==await page.locator('[data-benchmark-id]:visible').evaluate_all('(es)=>es.map(e=>e.dataset.benchmarkId).sort()')
            checks.append('legacy constraints and repeated years survive UI edits and reload')
            await page.goto(origin+BASE+'/zh/benchmarks/?q=%E9%95%BF%E6%9C%9F')
            query_ids=await page.locator('[data-benchmark-id]:visible').evaluate_all('(es)=>es.map(e=>e.dataset.benchmarkId).sort()')
            assert len(query_ids)==7, query_ids
            await page.locator('[data-language-path]').click()
            assert query_ids==await page.locator('[data-benchmark-id]:visible').evaluate_all('(es)=>es.map(e=>e.dataset.benchmarkId).sort()')
            await page.reload()
            assert query_ids==await page.locator('[data-benchmark-id]:visible').evaluate_all('(es)=>es.map(e=>e.dataset.benchmarkId).sort()')
            checks.append('Chinese query returns identical seven IDs across locales and reload')
            resultsets=[json.loads(f.read_text()) for f in (ROOT/'data/results').glob('*.json')]
            expected={r['benchmark_id'] for r in resultsets if r['tracking_status']=='paper-snapshot'}
            await page.goto(origin+BASE+'/zh/benchmarks/?status=tracked&source=paper-snapshot')
            assert set(await page.locator('[data-benchmark-id]:visible').evaluate_all('(es)=>es.map(e=>e.dataset.benchmarkId)'))==expected
            if args.output:await page.screenshot(path=str(args.output/'regression-source-intersection.png'))
            await page.goto(origin+BASE+'/zh/benchmarks/?status=untracked&source=paper-snapshot')
            assert await page.locator('[data-benchmark-id]:visible').count()==0
            await page.goto(origin+BASE+'/zh/benchmarks/?facet=retrieval-quality')
            assert await page.locator('[data-benchmark-id]:visible').count()==0
            assert '歧义' in await page.locator('[data-filter-form] [role=status]').inner_text()
            checks.append('source type AND availability; ambiguous legacy facet is restrictive and explained')
            await page.goto(origin+BASE+'/zh/benchmarks/structmemeval/#note-什么时候值得用')
            await page.locator('[data-language-path]').click()
            fragment=unquote(urlsplit(page.url).fragment)
            assert fragment=='note-when-to-use-it',fragment
            assert await page.locator('[id="'+fragment+'"]').count()==1
            checks.append('translated note fragment resolves to paired section, not a broken anchor')
            await page.goto(origin+BASE+'/zh/compare/?benchmark=deltaml-bench&benchmark=browsecomp-plus-cm')
            comparison=await page.locator('[data-compare-table]').inner_text()
            assert '4 runs' in comparison and '60.2' in comparison
            assert '结果数据切分' in comparison and '结果协议版本' in comparison
            if args.output:await page.screenshot(path=str(args.output/'regression-compare-conditions.png'),full_page=True)
            checks.append('comparison exposes task, split, protocol, context and both original budgets')
        await page.close()
        for lang in ['zh','en']:
            for slug in ['sgr-bench','searchauditbench','bright-pro','evobrowsecomp','ragcap-bench','deltaml-bench']:
                page=await load(context,f'{lang}/benchmarks/{slug}/')
                await page.locator('#interpretation').scroll_into_view_if_needed()
                if args.output:await page.screenshot(path=str(args.output/f'review-{lang}-{slug}-prose.png'))
                if slug=='deltaml-bench':
                    await page.locator('#results').scroll_into_view_if_needed()
                    if args.output:await page.screenshot(path=str(args.output/f'review-{lang}-{slug}-results.png'))
                await page.close()
        await context.close();await browser.close()
    assert not errors,'\n'.join(errors)
    return {'browser_mode':'offline build bytes; history captured, not navigated' if args.offline else 'real HTTP origin', 'rendered_views':len(metrics),'checks':checks,'page_errors':errors,'page_metrics':metrics}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--offline',action='store_true');parser.add_argument('--output',type=Path);parser.add_argument('--static-only',action='store_true');args=parser.parse_args()
    if args.output:args.output.mkdir(parents=True,exist_ok=True)
    result,pages=static_audit()
    if not args.static_only:
        server=http.server.ThreadingHTTPServer(('127.0.0.1',0),Handler)
        thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
        try:result.update(asyncio.run(browser_audit(args,pages,f'http://127.0.0.1:{server.server_port}')))
        finally:server.shutdown()
    if args.output:(args.output/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
    print(json.dumps({k:v for k,v in result.items() if k!='page_metrics'},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
