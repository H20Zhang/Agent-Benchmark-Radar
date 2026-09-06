"""Post-deployment gate: verify public Pages bytes and real browser workflows.

Requires a concrete expected build SHA, so a successful deployment API response
cannot be mistaken for a current CDN response. Evidence contains no credentials.
"""
import argparse
import asyncio
import json
import time
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import urlsplit, unquote
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

ORIGIN = 'https://h20zhang.github.io/Agent-Benchmark-Radar'
ROUTES = ['', 'timeline/', 'benchmarks/', 'evaluate/', 'compare/', 'frontier/',
          'opportunities/', 'methodology/', 'areas/agent-memory/', 'areas/rag/', 'areas/data-agent/']

def wait_for_public_build(sha):
    last = 'no response'
    for attempt in range(30):
        try:
            req = Request(f'{ORIGIN}/zh/?deployment={sha}&probe={attempt}', headers={'Cache-Control': 'no-cache'})
            with urlopen(req, timeout=20) as response:
                soup = BeautifulSoup(response.read(), 'html.parser')
            tag = soup.select_one('meta[name="radar-build"]')
            last = tag.get('content') if tag else 'missing build stamp'
            if last == sha:
                return
        except Exception as error:
            last = str(error)
        time.sleep(5)
    raise RuntimeError(f'Public build did not converge to {sha}: {last}')

async def verify(args):
    records, errors = [], []
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for width in [390, 1440]:
            context = await browser.new_context(viewport={'width': width, 'height': 844 if width == 390 else 1000})
            page = await context.new_page()
            page.on('pageerror', lambda e: errors.append(str(e)))
            for lang in ['zh', 'en']:
                for route in ROUTES:
                    path=f'{lang}/{route}'
                    response=await page.goto(f'{ORIGIN}/{path}', wait_until='networkidle')
                    assert response and response.status == 200, f'{path}: HTTP failure'
                    build=await page.locator('meta[name="radar-build"]').get_attribute('content')
                    assert build == args.sha, f'{path}: stale build {build}'
                    assert await page.locator('h1').count() == 1
                    assert await page.locator('.site-nav>a:visible').count() >= 7
                    assert await page.evaluate('document.documentElement.scrollWidth <= innerWidth + 1'), f'{path}: overflow'
                    if width == 390 and route == 'timeline/':
                        y=await page.locator('[data-timeline-record]:visible').first.evaluate('(e)=>e.getBoundingClientRect().y')
                        assert y < 844, f'{path}: timeline not visible in first screen'
                    filename=f'{lang}-{route.strip("/").replace("/","-") or "home"}-{width}.png'
                    await page.screenshot(path=str(args.output/filename))
                    records.append({'path':path, 'width':width, 'status':response.status, 'build':build})
            await context.close()
        context=await browser.new_context(viewport={'width':1440,'height':1000})
        page=await context.new_page()
        page.on('pageerror',lambda e:errors.append(str(e)))
        await page.goto(f'{ORIGIN}/zh/benchmarks/?q=zzzz_deployment_no_match_873')
        assert await page.locator('[data-benchmark-id]:visible').count() == 0
        await page.goto(f'{ORIGIN}/zh/benchmarks/?q=%E9%95%BF%E6%9C%9F')
        ids=await page.locator('[data-benchmark-id]:visible').evaluate_all('(es)=>es.map(e=>e.dataset.benchmarkId).sort()')
        assert len(ids) == 7
        await page.locator('[data-language-path]').click()
        assert ids==await page.locator('[data-benchmark-id]:visible').evaluate_all('(es)=>es.map(e=>e.dataset.benchmarkId).sort()')
        await page.reload()
        assert ids==await page.locator('[data-benchmark-id]:visible').evaluate_all('(es)=>es.map(e=>e.dataset.benchmarkId).sort()')
        await page.goto(f'{ORIGIN}/zh/evaluate/?recipe=memory-governance')
        assert await page.locator('[data-suite-selection] li').count()==4
        assert await page.locator('.suite-role').count()==4
        await page.locator('[data-compare-suite]').click()
        assert await page.locator('table thead th').count()==5
        assert 'The Compaction Cliff' in await page.locator('table thead').inner_text()
        await page.goto(f'{ORIGIN}/zh/benchmarks/structmemeval/#note-什么时候值得用')
        await page.locator('[data-language-path]').click()
        assert unquote(urlsplit(page.url).fragment)=='note-when-to-use-it'
        await context.close()
        await browser.close()
    assert not errors, '\n'.join(errors)
    return {'expected_build':args.sha,'public_views':records,'workflow_checks':['zero-results visibility','bilingual Chinese query and reload','four-item suite to compare','translated note fragment'], 'page_errors':errors}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--sha',required=True);parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
    args.output.mkdir(parents=True,exist_ok=True)
    wait_for_public_build(args.sha)
    result=asyncio.run(verify(args))
    (args.output/'live-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
    print(f'Public deployment {args.sha}: {len(result["public_views"])} page views and all live workflow checks passed.')
