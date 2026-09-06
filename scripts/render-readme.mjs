/** README is the primary publication surface. This uses only Node's standard library. */
import {readFileSync, writeFileSync, existsSync} from 'node:fs';
import {fileURLToPath} from 'node:url';
import {resolve, dirname} from 'node:path';
import {loadRegistry} from '../web/src/lib/registry.mjs';
import {loadChineseSummaries} from '../web/src/lib/readme-localization.mjs';
import {publicationWindow} from '../web/src/lib/publication.mjs';
import {chronological, releaseDate, inReleaseWindow, isoDay} from '../web/src/lib/release-time.mjs';
import {loadAllResultSets} from '../web/src/lib/results.mjs';

const root=resolve(dirname(fileURLToPath(import.meta.url)), '..');
const read=(p)=>readFileSync(resolve(root,p),'utf8');
const records=[...loadRegistry()], chinese=loadChineseSummaries(), results=loadAllResultSets();
const period=publicationWindow(), byId=new Map(records.map(x=>[x.id,x]));
const recipes=JSON.parse(read('data/recipes.json'));
const areas=['agent-memory','rag','data-agent'];
const suffix={'agent-memory':'memory','rag':'rag','data-agent':'data'};
const names={'agent-memory':'Agent Memory',rag:'RAG / Agentic Retrieval','data-agent':'Data Agents'};
const short={zh:{'agent-memory':'记忆',rag:'检索','data-agent':'数据'},en:{'agent-memory':'Memory',rag:'Retrieval','data-agent':'Data'}};
const clean=s=>String(s??'').replaceAll('|','&#124;').replace(/\n+/g,' ');
const primary=x=>x.artifacts.paper||x.artifacts.project||x.artifacts.code||x.artifacts.data;
const note=(x,lang,prefix='')=>`${prefix}benchmarks/${x.id}${lang==='en'?'.en':''}.md`;
const summary=(x,lang)=>lang==='zh'?chinese.get(x.id):x.summary;
const block=(name,body)=>`<!-- ${name}:START -->\n\n${body.trim()}\n\n<!-- ${name}:END -->`;
const anchor=id=>`<a id="${id}"></a>`;
const back=lang=>lang==='zh'?'[回到顶部](#top)':'[Back to top](#top)';
function dateCell(x,lang) {
  const d=releaseDate(x), labels=lang==='zh'?{publication_at:'发表',data_release_at:'数据'}:{publication_at:'publication',data_release_at:'data'};
  let text=d.date+(d.field==='legacy_recorded_at'?'†':'');
  if(labels[d.field]) text+=` (${labels[d.field]})`;
  return `[${text}](${d.source||primary(x)})`;
}
function resources(x,lang) {
  const labels=lang==='zh'?{paper:'论文',code:'代码',data:'数据',project:'项目',leaderboard:'榜单'}:{paper:'Paper',code:'Code',data:'Data',project:'Project',leaderboard:'Board'};
  const seen=new Set();
  return Object.entries(labels).filter(([key])=>x.artifacts[key]&&!seen.has(x.artifacts[key])&&seen.add(x.artifacts[key])).map(([key,label])=>{const u=new URL(x.artifacts[key]); if(key==='paper'&&u.hostname==='github.com'&&!/\.pdf$/i.test(u.pathname))label=lang==='zh'?'仓库':'Repo'; else if(key==='paper'&&u.hostname==='huggingface.co')label=lang==='zh'?'数据':'Data'; return `[${lang==='zh'?label.split('').join('&#8288;'):label}](${x.artifacts[key]})`;}).join(' · ')||'—';
}
function identity(x,lang,prefix='') { return `[${clean(x.name)}](${note(x,lang,prefix)}) <!-- benchmark-id:${x.id} -->`; }
function dateLegend(lang) {
  return lang==='zh'
    ? '日期链接到来源。**†** 为首发时间待核验的历史记录；仅有月份时不补造日期。'
    : 'Dates link to sources. **†** marks a historical date, not a verified first release; month-only dates retain their precision.';
}
function intro(lang) {
  const zh=lang==='zh';
  return `${anchor('top')}\n# Agent Benchmark Radar\n\n${zh?'按时间与领域查找 Agent 评测基准，直接进入论文、代码与评测解读。':'Find agent benchmarks by date and research area, with direct links to papers, code, and evaluation notes.'}\n\n${zh?'**中文** · [English](README.en.md)':'[中文](README.md) · **English**'} · **${records.length} ${zh?'个基准':'benchmarks'}** · ${zh?'发现扫描':'Discovery scan'} **${period.asOf}**\n\n${zh?'[近期时间轴](#release-timeline)':'[Recent timeline](#release-timeline)'} · ${areas.map(a=>`[${names[a]} (${records.filter(x=>x.area===a).length})](#registry-${suffix[a]})`).join(' · ')}\n\n${zh?'名称链接到解读；论文、代码和数据可直接访问。':'Names open reading notes; papers, code, and data are directly accessible.'}`;
}
function recent(lang) {
  const zh=lang==='zh', items=chronological(records).filter(x=>inReleaseWindow(x,period.recent));
  const months=[...new Set(items.map(x=>releaseDate(x).date.slice(0,7)))];
  const table=months.map(month=>{
    const subset=items.filter(x=>releaseDate(x).date.startsWith(month));
    return `${anchor('month-'+month)}\n### ${month} · ${subset.length} ${zh?'项':'records'}\n\n| ${zh?'时间 | Benchmark | 考察内容 | 资&#8288;料':'Time | Benchmark | What it measures | Sources'} |\n|---|---|---|---|\n${subset.map(x=>`| ${dateCell(x,lang)} | ${identity(x,lang)}<br><sub>${short[lang][x.area]}</sub> | ${clean(summary(x,lang))} | ${resources(x,lang)} |`).join('\n')}`;
  }).join('\n\n');
  return `${anchor('release-timeline')}\n${anchor('timeline')}${anchor('latest')}${anchor('periods')}\n## ${zh?'最近六个月':'Last six months'}\n\n**${isoDay(period.recent.start)} — ${period.asOf}** · ${items.length} ${zh?'项；月份精度的边界记录按区间重叠纳入。':'records; month-only boundary records are included by interval overlap.'}\n\n${months.map(m=>`[${m}](#month-${m})`).join(' · ')}\n\n${dateLegend(lang)}\n\n${block('TABLE-FIRST:RECENT',table)}\n\n${back(lang)}`;
}
function fullTables(lang) {
  const zh=lang==='zh';
  const dates=records.filter(x=>x.citations?.status==='ok').map(x=>x.citations.updated_at).sort();
  const stamp=dates[0]===dates.at(-1)?dates[0]:`${dates[0]} — ${dates.at(-1)}`;
  let text=`${anchor('field-map')}${anchor('all-benchmarks')}\n## ${zh?'按领域浏览全部基准':'All benchmarks by area'}\n\n${zh?`全部 ${records.length} 个基准均在本页，按日期倒序；旧基准不会因时间较早而被移除。`:`All ${records.length} benchmarks remain on this page, newest first. Older benchmarks are retained.`}\n\n${block('CITATION-META',zh?`引用数来自 Semantic Scholar，已匹配记录的核验日期为 **${stamp}**。\`—\` 是未知，\`0\` 是已核验零引用；引用数仅供背景参考。`:`Citations come from Semantic Scholar; matched records were checked **${stamp}**. \`—\` means unknown; \`0\` is a verified zero. Counts are background context, not a ranking.`)}\n\n`;
  for(const a of areas){
    const subset=chronological(records.filter(x=>x.area===a));
    const rows=subset.map(x=>{
      const c=x.citations, cite=c?.status==='ok'?`[${c.count.toLocaleString('en-US')}](${c.url})`:'—';
      return `| ${dateCell(x,lang)} | ${identity(x,lang)} | ${clean(summary(x,lang))} | ${resources(x,lang)} | ${cite} |`;
    });
    text+=`${anchor('benchmark-'+suffix[a])}${anchor('registry-'+suffix[a])}\n### ${names[a]} · ${subset.length}\n\n${block('TABLE-FIRST:AREA:'+a,`| ${zh?'时间 | Benchmark | 考察内容 | 资&#8288;料 | 引用数 (S2)':'Time | Benchmark | What it measures | Sources | Citations (S2)'} |\n|---|---|---|---|---:|\n${rows.join('\n')}`)}\n\n${back(lang)}\n\n`;
  }
  return text.trim();
}
function further(lang) {
  const zh=lang==='zh', s=zh?'':'.en';
  return `${anchor('reading-paths')}\n## ${zh?'选评测与深入阅读':'Selection and further reading'}\n\n${zh?'以下是辅助阅读，不是基准质量排名；实验仍需核对任务、模型、工具、预算和判分协议。':'These are reading aids, not benchmark quality rankings. Check tasks, models, tools, budgets, and scoring protocols before choosing an evaluation.'}\n\n${anchor('evaluation-recipes')}\n${anchor('recipe-memory')}${anchor('recipe-rag')}${anchor('recipe-data')}\n${zh?'**按研究问题选评测：**':'**Choose evaluations by research question:**'} [${zh?`${recipes.length} 个组合及适用边界`:`${recipes.length} suites and their claim boundaries`}](library/evaluation-recipes${s}.md)\n\n${anchor('frontier-signals')}${anchor('frontier')}${anchor('changes')}${anchor('evolution')}${anchor('evaluation-frontiers')}\n${zh?'**研究观察与能力地图：**':'**Research observations and capability maps:**'} [${zh?'编辑解读，单独阅读':'Editorial guide'}](docs/reading-guide${s}.md)\n\n${anchor('result-snapshots')}\n${zh?'**结果资料：**':'**Result sources:**'} [${zh?`${results.size} 个基准的来源索引`:`Source index for ${results.size} benchmarks`}](library/results${s}.md)${zh?'。成绩与实验条件在各基准解读和原始来源中查看，不在首页混排。':'. Read scores with their experimental conditions in the notes and original sources; no cross-benchmark score table is shown here.'}\n\n${anchor('library')}\n${zh?'**历史演进与专题方法：**':'**Historical context and related methods:**'} [${zh?'完整 Library':'Full Library'}](library/README${s}.md) · [Memory](https://github.com/H20Zhang/Agent-Memory-Radar#field-map) · [Retrieval](https://github.com/H20Zhang/Agentic-RAG-Radar#field-map) · [Data](https://github.com/H20Zhang/Data-Agent-Radar#field-map)\n\n---\n\n${zh?'README 现为主阅读入口；独立网站已停用。':'The README is the primary reading surface; the standalone website is retired.'} [${zh?'收录规则':'Curation'}](CURATION.md) · [${zh?'日期与证据规范':'Schema'}](SCHEMA.md) · [${zh?'维护说明':'Maintenance'}](docs/README_PUBLICATION.md)\n\n${back(lang)}`;
}
function recipePage(lang){
  const zh=lang==='zh', filename=zh?'README.md':'README.en.md';
  let text=`# ${zh?'按研究问题选评测':'Choose evaluations by research question'}\n\n[${zh?'返回主入口':'Back to the main README'}](../${filename}#evaluation-recipes) · ${zh?'[English](evaluation-recipes.en.md)':'[中文](evaluation-recipes.md)'}\n\n${zh?'这些组合是编辑建议，不自动证明某个研究主张。Core 是核心评测，Complement 是补充评测；更换组合或协议后需重新核验支持范围。':'These suites are editorial suggestions, not automatic evidence for a claim. Core and Complement have different roles. Changing the selection or protocol requires revalidating the supported claim.'}\n\n${block('EVALUATION-RECIPES',areas.map(a=>`${anchor('recipe-'+suffix[a])}\n## ${names[a]}\n\n| ${zh?'研究问题 | 核心（Core） | 补充（Complement） | 支持范围与下一步':'Research question | Core | Complement | Claim boundary and next validation'} |\n|---|---|---|---|\n${recipes.filter(r=>r.area===a).map(r=>`| **${clean(r.claim[lang])}** | ${r.core.map(id=>`[${byId.get(id).name}](${note(byId.get(id),lang,'../')})`).join(' · ')} | ${r.complement.map(id=>`[${byId.get(id).name}](${note(byId.get(id),lang,'../')})`).join(' · ')} | ${clean(r.claim_boundary[lang])}<br>${zh?'下一步：':'Next: '}${clean(r.next_validation[lang])} |`).join('\n')}`).join('\n\n'))}\n`;
  return text;
}
function resultPage(lang){
  const zh=lang==='zh', labels=zh?{'paper-snapshot':'论文快照','verified-snapshot':'来源快照',live:'榜单快照'}:{'paper-snapshot':'Paper snapshot','verified-snapshot':'Source snapshot',live:'Leaderboard snapshot'};
  const rows=chronological(records.filter(x=>results.has(x.id))).map(x=>{
    const r=results.get(x.id);
    return `| ${identity(x,lang,'../')} | ${labels[r.tracking_status]} | ${r.tracks.length} | ${r.verified_at} | [JSON](../data/results/${x.id}.json) |`;
  });
  return `# ${zh?'结果来源索引':'Result source index'}\n\n[${zh?'返回主入口':'Back to the main README'}](../README${zh?'':'.en'}.md#result-snapshots) · ${zh?'[English](results.en.md)':'[中文](results.md)'}\n\n${zh?`${results.size} 个基准已有结构化结果。点击基准名称阅读分数、适用条件及局限；JSON 保留各轨道的原始来源与已记录条件。核验日期不等于榜单实时更新，单条结果不代表当前最佳。`:`${results.size} benchmarks have structured results. Open each note for scores, conditions, and limitations; JSON preserves the source and recorded conditions for each track. Verification dates are not live refresh times, and one recorded result is not a current best.`}\n\n| Benchmark | ${zh?'来源类型 | 轨道数 | 结果核验 | 原始记录':'Source type | Tracks | Result verified | Raw record'} |\n|---|---|---:|---|---|\n${rows.join('\n')}\n`;
}
const outputs=new Map();
for(const lang of ['zh','en']){
  const s=lang==='en'?'.en':'';
  outputs.set(`README${s}.md`,`${block('ONBOARDING',intro(lang))}\n\n${recent(lang)}\n\n${fullTables(lang)}\n\n${further(lang)}\n`);
  outputs.set(`library/evaluation-recipes${s}.md`,recipePage(lang));
  outputs.set(`library/results${s}.md`,resultPage(lang));
}
const stale=[];
for(const [path,value] of outputs){
  if(!existsSync(resolve(root,path))||read(path)!==value){stale.push(path);if(!process.argv.includes('--check'))writeFileSync(resolve(root,path),value);}
}
if(process.argv.includes('--check')&&stale.length){console.error('Stale README projections: '+stale.join(', '));process.exitCode=1;}
else console.log(`README projections ${process.argv.includes('--check')?'verified':'updated'}: ${records.length} benchmarks, ${results.size} result sets; scan remains ${period.asOf}.`);
