#!/usr/bin/env python3
"""One-shot historical reference publication; excluded from the final main tree.

No network requests or model calls. Existing canonical/citation/result data stays
byte-for-byte unchanged. Every numeric selection below is explicitly authored.
"""
from __future__ import annotations
from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
BASE='deb08a4204dd9f31abb6a23662ffd2d48efbd42f'
CHECKED='2026-09-23'
def write(path,text):
    p=ROOT/path;p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(text.rstrip()+'\n',encoding='utf-8')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
protected=[ROOT/'data/benchmarks.json',ROOT/'data/freshness.json',ROOT/'data/locales/zh/benchmarks.json']+list((ROOT/'data/results').glob('*.json'))
before={str(p):digest(p) for p in protected}
# Explicit HTML line breaks keep the compact block readable without trailing whitespace.
rpath=ROOT/'scripts/render-release-references.py'
rtext=rpath.read_text().replace("'  '","'<br>'").replace("}  '","}<br>'").replace(")  '",")<br>'")
write('scripts/render-release-references.py',rtext)
spec=importlib.util.spec_from_file_location('historical_ref',rpath)
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
items=json.loads((ROOT/'data/benchmarks.json').read_text())
assert len(items)==146,'Canonical membership changed; reconcile before publication'
refs={r['id']:mod.fallback(r) for r in items}
curated=[]
def add(ident,date,source,rows,zh,en,locator,status='release-best',caveat=None,period=None):
    initial=False if status=='later-version' else (None if status=='paper-reference' else True)
    r={'status':status,'period':period or {'zh':date+' · 论文 v1','en':date+' · paper v1'},
       'results':[{'system':a,'metric':b,'score':c} for a,b,c in rows],
       'scope':{'zh':zh,'en':en},'source':source,'locator':locator,
       'initial_release':initial,'checked_at':CHECKED,
       'caveat':{'zh':'仅供了解当时难度，不代表当前最佳；不同任务、版本和实验条件不能直接混比。','en':'Historical difficulty reference, not current SOTA; tasks, versions, and experimental conditions are not interchangeable.'}}
    if status=='release-best':r['comparison_scope']=en
    if caveat:r['caveat']={'zh':caveat[0],'en':caveat[1]}
    assert ident in refs,ident
    refs[ident]=r;curated.append(ident)

add('locomo','2024-02-27','https://arxiv.org/html/2402.17753v1',
 [('GPT-3.5-turbo-16K + observation RAG (top-5)','QA overall F1','41.4'),('GPT-3.5-turbo','Event-summary FactScore F1','45.9')],
 '分别为表 2–3 的自动 QA 最佳与表 4 的事件总结 F1 最佳；不含人类对照。',
 'Best automated QA overall F1 in Tables 2–3 and event-summary F1 in Table 4, respectively; human controls excluded.',
 'Tables 2–4: observation RAG top-5; GPT-3.5-turbo event-summary row.')
add('longmemeval','2024-10-14','https://arxiv.org/html/2410.10813v1',
 [('GPT-4o + round values / fact-expanded keys (top-10)','LongMemEval-M QA accuracy','72.0%')],
 '表 2 索引设计实验的最佳端到端 QA；不是 LongMemEval-S、oracle 条件或跨所有预算的统一上限。',
 'Best end-to-end QA in the indexing-design experiment of Table 2; not LongMemEval-S, oracle retrieval, or a maximum across all budgets.',
 'Table 2: Value=Round, K=V+fact, GPT-4o Top-10=0.720.')
add('membench','2025-06','https://arxiv.org/html/2506.21605v1',
 [('RetrievalMemory / Qwen2.5-7B','Factual participation @100K accuracy','83.3%'),('RetrievalMemory / Qwen2.5-7B','Factual observation @100K accuracy','93.3%')],
 '表 3、固定 Qwen2.5-7B 的两个 100K factual-memory 设置分别比较；不合成反思记忆总分。',
 'Separate best 100K factual-memory settings in Table 3 with Qwen2.5-7B fixed; no synthetic overall score including reflective memory.',
 'Table 3, 100K factual participation and observation.')
add('memoryagentbench','2025-07','https://arxiv.org/html/2507.05257v1',
 [('NV-Embed-v2 RAG / GPT-4o-mini','RULER-QA','83.0'),('Contriever RAG / GPT-4o-mini','FactCon-MH accuracy','7.0%')],
 '主表 2 中两个子任务的最佳配置；不把整套基准的不同能力合成一个总分。',
 'Best configurations for two selected subtasks in main Table 2; different capabilities are not reduced to a synthetic overall score.',
 'Table 2, RULER-QA and FactCon-MH.',caveat=('仅指表 2 的比较范围，不含后续消融；多跳冲突按表中 7.0 记录，正文“至多 6”与表格不一致。','Table 2 scope only, excluding later ablations. Its 7.0 multi-hop conflict entry differs from the prose claim of at most 6.'))
add('beam','2025-10','https://arxiv.org/html/2510.27246v1',
 [('LIGHT / Llama-4-Maverick','Average @500K','0.359'),('LIGHT / Llama-4-Maverick','Average @10M','0.266')],
 '表 1 对应长度下的十类能力均值最佳；500K 与 10M 是不同设置。',
 'Best ten-ability averages at the selected lengths in Table 1; 500K and 10M are different settings.',
 'Table 1, LIGHT with Llama-4-Maverick.')
add('ama-bench','2026-02','https://arxiv.org/html/2602.22769v1',
 [('AMA-Agent','Average accuracy','57.22%')],
 '首版摘要报告的 AMA-Agent 平均准确率最佳；属于记忆问答协议，不是环境行动成功率。',
 'Best AMA-Agent average accuracy reported in the v1 abstract under the memory-QA protocol, not downstream action success.',
 'v1 abstract: AMA-Agent average accuracy.')
add('pm-bench','2026-07-14','https://arxiv.org/html/2607.12385v1',
 [('GPT-5.4 + optional heartbeat','Per-model Set-F1','79.1%'),('Optional heartbeat (8-model aggregate)','Macro Set-F1','65.1%')],
 '按表 3 记录单模型最佳、按表 2 记录跨模型最佳策略均值；二者分母不同。',
 'Per-model best from Table 3 and best cross-model scaffold average from Table 2, with different denominators.',
 'Tables 2 and 3, optional-heartbeat rows.',caveat=('摘要将 65.1% 关联到 GPT-5.4，与表格不一致；此处保留表 2/3 的明确口径，不代表当前最佳。','The abstract associates 65.1% with GPT-5.4, unlike the tables. This reference follows the explicit Table 2/3 scopes, not current SOTA.'))
add('wikisql','2017-08','https://arxiv.org/abs/1709.00103',
 [('Seq2SQL','Execution accuracy','59.4%'),('Seq2SQL','Logical-form accuracy','48.3%')],
 '原论文摘要中的 Seq2SQL 结果；execution 与 logical-form 是两种不同指标。',
 'Seq2SQL results in the original abstract; execution and logical-form accuracy are different metrics.',
 'Original paper abstract: Seq2SQL.',period={'zh':'2017-08 · 发布论文','en':'2017-08 · release paper'})
add('spider','2018-09-24','https://arxiv.org/abs/1809.08887v1',
 [('Best model in v1 abstract (name not verified)','Database-split exact match','14.3%')],
 '首版摘要明确报告的数据库切分最佳成绩；模型名称尚未核验，不用后续版本的 12.4% 替换。',
 'Best database-split score explicitly reported in the v1 abstract; model name unverified. The later 12.4% figure is not substituted.',
 'v1 abstract, database-split best reported score.')
add('ds-1000','2022-11-18','https://arxiv.org/abs/2211.11501v1',
 [('Codex-002','Accuracy','43.3%')],
 '首版摘要报告的最佳公开系统，在原版功能与表面约束判分下评测。',
 'Best public system reported by the v1 abstract, under original functional and surface-constraint evaluation.',
 'v1 abstract, Codex-002.')
add('bird','2023','https://arxiv.org/abs/2305.03111',
 [('ChatGPT','Execution accuracy','40.08%')],
 '发布论文摘要中的历史模型结果；该页为 v3，未将其冒充已单独复核的 v1。',
 'Historical model result in the release-paper abstract. The available page is v3, not a separately verified v1.',
 'Available v3 abstract, ChatGPT execution accuracy.',status='later-version',period={'zh':'2023 · 发布论文 v3','en':'2023 · release-paper v3'})
add('spider-2','2024-11-12','https://arxiv.org/abs/2411.07763v1',
 [('o1-preview + paper code-agent framework','Task success','17.0%')],
 '首版摘要中的代码智能体结果，对应原版任务集合；不与后来的 Lite、Snow 或修改后的任务集混比。',
 'Code-agent result in the initial abstract on the original task collection; not later Lite, Snow, or revised sets.',
 'v1 abstract: o1-preview code-agent result.',status='release-reference')
add('mle-bench','2024-10-09','https://arxiv.org/abs/2410.07095v1',
 [('o1-preview + AIDE','Competitions with at least bronze','16.9%')],
 '首版 75 场 Kaggle 竞赛的最佳主实验配置；不是单题准确率或后续延长预算的榜单结果。',
 'Best main-experiment setup in the initial 75-competition benchmark; not per-question accuracy or a later extended-budget board.',
 'v1 abstract and main evaluation, o1-preview + AIDE.')
add('datascibench','2025-02','https://arxiv.org/html/2502.13897v1',
 [('GPT-4o-2024-05-13','Table 2 overall Score','64.51'),('GPT-4o-2024-05-13','Collected-prompts success','19.82%')],
 '分别是表 2 综合评分最佳与表 5 自采集问题成功率最佳；后者不是整个混合题集的准确率。',
 'Best overall Score in Table 2 and best success on collected prompts in Table 5; the latter is not whole-mixture accuracy.',
 'Tables 2 and 5, GPT-4o-2024-05-13 rows.')
add('livedrbench','2025-08-06','https://arxiv.org/abs/2508.04183v1',
 [('OpenAI deep research','Overall F1','0.55')],
 '初始实验中最佳的深度研究系统；在 100 个任务的结构化主张发现上计分，不是报告文风评分。',
 'Best deep-research system in the initial experiment, scoring structured claim discovery across 100 tasks, not report style.',
 'v1 paper abstract and original overall comparison.')
add('lifebench','2026-03','https://arxiv.org/html/2603.03781v1',
 [('MemOS / GPT-5.1-Mini','Overall accuracy','55.22%')],
 '首版 4.3 节整体准确率最佳；GPT-5.1-Mini 同时承担记忆、回答与判分，原始 2,003 题。',
 'Best overall accuracy in v1 Section 4.3; GPT-5.1-Mini for memory, answers, and judging on the original 2,003 questions.',
 'Sections 4.2 and 4.3: setup and overall accuracy.')
add('inmind','2026-07','https://arxiv.org/html/2607.24368v1',
 [('Naive RAG / text-embedding-3-large / GPT-5-mini','Indirect application, Table 1','16.0%'),('Always-in-state / GPT-5-mini','Indirect application, Table 2','68.8%')],
 '125 题；分别保留表 1 检索配置最佳和表 2 常驻状态诊断。84.0% 的 oracle 不当成正常检索成绩。',
 '125 tasks: best retrieval configuration in Table 1 and always-visible-state diagnostic in Table 2. The 84.0% oracle is not a normal retrieval score.',
 'Tables 1 and 2; indirect application.',status='diagnostic')
add('groupmembench','2026-05-14','https://arxiv.org/abs/2605.14498v1',
 [('Best memory system in v1 (name not verified)','Average accuracy','46.0%')],
 '首版摘要明确报告的最佳记忆系统平均分；尚未核验对应系统名称，不据此猜测模型。',
 'Best memory-system average explicitly reported by the v1 abstract; the matching system name remains unverified rather than guessed.',
 'v1 abstract, best memory-system average.')
add('sgr-bench','2026-05','https://arxiv.org/html/2605.22219v1',
 [('GPT-5.5 / CLI agent','Overall Item-F1','66.18%'),('GPT-5.5 / CLI agent','Overall Row-F1','43.37%')],
 '表 2/3、100 个任务中的最佳配置；Item-F1 与整行正确性的 Row-F1 分开保留。',
 'Best configuration in Tables 2–3 on 100 tasks; item and full-row F1 remain separate metrics.',
 'Tables 2 and 3, GPT-5.5 CLI.')
add('livebrowsecomp','2026-05','https://arxiv.org/html/2605.28721v1',
 [('GPT-5.4 / search-augmented agent','LiveBrowseComp avg@4','43.2%')],
 '表 3/5 的 LiveBrowseComp 平均正确率最佳；avg@4 不是四次中任选一次成功的 pass@4。',
 'Best LiveBrowseComp average accuracy in Tables 3 and 5; avg@4 is not success on any of four attempts (pass@4).',
 'Tables 3 and 5, GPT-5.4 search-augmented.')
add('evobrowsecomp','2026-06','https://arxiv.org/html/2606.13120v1',
 [('Claude-Opus-4.6 + tools','English accuracy','44.8%'),('Claude-Opus-4.6 + tools','Chinese accuracy','36.8%')],
 '表 2 的有工具设置，按语言分别比较；保留原版搜索预算，不与无工具或当前榜单混比。',
 'Best tool-enabled entries in Table 2, compared separately by language under the original search budget.',
 'Table 2, tool-enabled Claude-Opus-4.6.')
add('searchauditbench','2026-08','https://arxiv.org/html/2608.05212v1',
 [('SearchAuditor / GPT-5.5','Full Pass Score (FPS)','32.26%'),('SearchAuditor / GPT-5.5','CS-Strict','44.89%')],
 '表 2 的轨迹审计配置最佳；FPS 判完整审计、CS-Strict 判关键错误步骤，不是搜索任务最终答案成功率。',
 'Best trajectory-auditing configuration in Table 2; FPS grades a complete audit and CS-Strict the critical step, not search-answer success.',
 'Table 2, SearchAuditor with GPT-5.5.')
add('crag','2024-06','https://arxiv.org/html/2406.04744v1',
 [('Copilot Pro','Human-eval Score_h (equal-weighted)','50.6'),('GPT-4 Turbo + Task-3 RAG','Auto-eval accuracy','43.6%')],
 '分别为表 6 商业系统人工评分最佳和表 5 Task-3 基线准确率最佳；两类评分及挑战赛分数不可互换。',
 'Best industry-system human score in Table 6 and best Task-3 baseline accuracy in Table 5; these scoring protocols and challenge scores differ.',
 'Tables 5 and 6; equal-weighted industry evaluation and Task-3 baseline.')
add('da-code','2024-10-09','https://arxiv.org/html/2410.07331v1',
 [('DA-Agent / GPT-4','Total score','30.5')],
 '首版表 3 总分最佳；不是代码可执行率 76.8%，也不是预算内产出结果的完成率 99.4%。',
 'Best total score in v1 Table 3; distinct from 76.8% executable code and 99.4% within-budget completion.',
 'Table 3, GPT-4 total score.')
add('dabstep','2025-06-30','https://arxiv.org/html/2506.23719v1',
 [('o4-mini','Hard accuracy','14.55%'),('GPT-4.1','Easy accuracy','80.56%')],
 '表 1 隐藏测试集；Hard 与 Easy 各自的最佳模型不同，不合成单一模型成绩。',
 'Hidden test set, Table 1. Hard and Easy have different best models; these are not one model’s combined result.',
 'Table 1, hidden Easy and Hard subsets.')
add('data-agent-benchmark','2026-03-21','https://arxiv.org/html/2603.20576v1',
 [('Gemini-3-Pro / paper ReAct agent','Pass@1','38%')],
 '表 3 五个通用模型基线最佳，每题 50 次、跨 12 数据集平均；不含 PromptQL 个案或后续验证器重算榜单。',
 'Best of five generic-model baselines in Table 3: 50 trials per query and a 12-dataset average. Excludes the PromptQL case study and later rescored boards.',
 'Table 3, generic ReAct-agent baselines.',caveat=('仅为原论文口径的历史参考。后续验证器、hints 和专用提示变化后的成绩不直接对比。','Original-paper history only; later validators, hints, and task-specific prompts change comparability.'))
add('dataspace','2026-08','https://arxiv.org/html/2608.03451v1',
 [('Grok 4.5 / DataSpace-Agent','Task accuracy (272/410)','66.34%')],
 '表 3 固定 DataSpace-Agent 比较六个模型时最佳；410 题，不是不同模型与 harness 任意组合的上限。',
 'Best of six backbones with DataSpace-Agent fixed in Table 3, on 410 tasks; not a maximum over arbitrary model/harness combinations.',
 'Table 3, controlled backbone comparison; Section 6.1 budgets.')
add('browsecomp','2025-04-10','https://openai.com/index/browsecomp/',
 [('OpenAI deep research','Accuracy','51.5%')],
 '首发官方文章的最佳模型成绩；原始 1,266 题。作者说明 deep research 的训练专门覆盖此类任务。',
 'Best model in the official launch article, on the original 1,266 questions. The authors state that deep research was trained specifically for this task type.',
 'Performance of OpenAI models table and deep-research training footnote.',period={'zh':'2025-04-10 · 官方首发','en':'2025-04-10 · official launch'})
add('autoresearchbench','2026-04','https://arxiv.org/html/2604.25256v1',
 [('Claude-Opus-4.6 / ReAct','Deep Research accuracy','9.39%'),('Gemini-3.1-Pro-Preview / ReAct','Wide Research IoU','9.31%')],
 '表 2 受控 ReAct 比较中的分项最佳；不混入只跑 50 题的端到端系统测试，也不把 IoU 当准确率。',
 'Subtask bests within the controlled ReAct comparison of Table 2; excludes 50-question end-to-end-system tests and distinguishes IoU from accuracy.',
 'Tables 2, 8 and 9, controlled ReAct evaluation.')

# Explicit frozen source-ledger references. Never choose a live-board maximum.
selections={'deepresearch-bench':[48.88,90.24],'deltaml-bench':[33.9,49.0],'statemembench':[36.3],'compaction-cliff':[96.0],'mpbench':[34.25,66.67],'scale-qa':[29.8],'bright-pro':[68.0],'browsecomp-plus-cm':[80.7],'litreview-arena':[0.792]}
special={
 'mpbench':('攻击成功率：越高表示攻击更有效，不是防御系统更好。','Attack-success rates: higher indicates a stronger attack, not a better defender.'),
 'statemembench':('指定模型下的状态记忆配置；不声明跨模型或跨协议的完整榜首。','A state-memory configuration under the specified model, not a full cross-model or cross-protocol winner.'),
 'compaction-cliff':('指定压缩协议后的约束保留率，不是通用任务成功率。','Constraint retention after the named compaction protocol, not general task success.'),
 'litreview-arena':('评分器与人工判断的相关性，不是研究智能体的任务得分。','Evaluator correlation with human judgment, not a research-agent task score.'),
 'scale-qa':('原文全上下文基线；不把单条已记录成绩当成首发榜首。','Original full-context baseline, not a launch winner inferred from one recorded score.'),
 'deltaml-bench':('4×6h 与 2×12h 的单次运行成功率分开报告，不混成一种预算。','The 4×6h and 2×12h per-run success rates are separate budget conditions.'),
}
imported=[]
for ident,scores in selections.items():
    if ident in curated:continue
    path=ROOT/f'data/results/{ident}.json'
    packet=json.loads(path.read_text())
    chosen=[]
    for number in scores:
        found=[(t,e) for t in packet.get('tracks',[]) for e in t.get('entries',[]) if isinstance(e.get('score'),(int,float)) and abs(e['score']-number)<1e-8]
        if len(found)!=1:
            print('Keep unknown; source-ledger identity ambiguous:',ident,number,len(found));chosen=[];break
        chosen.append(found[0])
    if not chosen:continue
    rows=[];versions=[];days=[];origins=[]
    for track,entry in chosen:
        source=entry['source'];protocol=track.get('protocol_version','')
        versions.append(bool(re.search(r'v1(?:$|[/?#-])',source) or re.search(r'(^|[-_])v1($|[-_])',protocol)))
        metric=track.get('metric',{})
        label=metric.get('label',metric.get('name',metric.get('id','Recorded metric')))
        if isinstance(label,dict):label=label.get('en',str(label))
        system=entry.get('method') or entry.get('agent') or 'Recorded system'
        model=entry.get('model')
        if isinstance(model,str) and model not in system:system+=' / '+model
        scope=track.get('label')
        if not isinstance(scope,dict) or not scope.get('zh') or not scope.get('en'):
            text=str(track.get('split') or track.get('task') or protocol or 'Source-defined track');scope={'zh':text,'en':text}
        value=format(entry['score'],'.10g')+('%' if metric.get('unit')=='%' else '')
        rows.append({'system':system,'metric':label,'score':value,'scope':{'zh':scope['zh'],'en':scope['en']},'source':source})
        origins.append({'track_id':track.get('track_id',track.get('id')),'entry_id':entry.get('id'),'score':entry['score']})
        if entry.get('date'):days.append(entry['date'])
    initial=all(versions)
    status='release-reference' if initial else 'paper-reference'
    if initial and ident in ('mpbench','statemembench','compaction-cliff','litreview-arena'):status='diagnostic'
    date=', '.join(sorted(set(days))) or 'date not established'
    zh,en=special.get(ident,('保留原始轨道中的指定结果，不把不同指标、子集或系统拼成一个榜首。','Selected original-track results; metrics, subsets, and systems are not pooled into one winner.'))
    refs[ident]={'status':status,'period':{'zh':date+(' · 论文 v1 快照' if initial else ' · 历史论文快照'),'en':date+(' · paper v1 snapshot' if initial else ' · historical paper snapshot')},
       'results':rows,'scope':{'zh':zh,'en':en},'source':rows[0]['source'],'initial_release':True if initial else None,
       'locator':'Explicit frozen source-ledger selection: '+json.dumps(origins,ensure_ascii=False),
       'caveat':{'zh':'来自此前保存的原论文结果记录，仅作历史参考；本次未重跑实验，也不声明当前最佳。','en':'From a previously curated original-paper record, for historical reference; not rerun in this update and not current SOTA.'},
       'source_record':'https://github.com/H20Zhang/Agent-Benchmark-Radar/blob/'+BASE+f'/data/results/{ident}.json',
       'source_verified_at':packet.get('verified_at'),'transcribed_at':CHECKED}
    imported.append(ident)
for ident,r in refs.items():mod.validate_record(ident,r)
write('data/release-references.json',json.dumps({'schema_version':1,'purpose':'Frozen source-bounded historical references; never a current leaderboard.','benchmarks':dict(sorted(refs.items()))},ensure_ascii=False,indent=2))

# Root publication invokes the detail-header projection, including check-only mode.
p=ROOT/'scripts/render-readme.mjs';s=p.read_text()
if "from 'node:child_process'" not in s:s="import {spawnSync} from 'node:child_process';\n"+s
if '// FROZEN-RELEASE-REFERENCES' not in s:
    s+="\n// FROZEN-RELEASE-REFERENCES: frozen editorial data, not current scores.\nconst releaseArgs=[resolve(root,'scripts/render-release-references.py')];\nif(process.argv.includes('--check')) releaseArgs.push('--check');\nconst releaseCheck=spawnSync(process.env.PYTHON||'python3',releaseArgs,{cwd:root,stdio:'inherit'});\nif(releaseCheck.error){console.error(releaseCheck.error.message);process.exitCode=1;}\nelse if(releaseCheck.status!==0){process.exitCode=releaseCheck.status||1;}\n"
write('scripts/render-readme.mjs',s)

# Repair the PM-Bench aggregate/per-model attribution at its source sentence.
for lang,ext in [('zh',''),('en','.en')]:
    p=ROOT/f'benchmarks/pm-bench{ext}.md';text=p.read_text()
    marker='<!-- RELEASE-TABLE-CORRECTION:START -->'
    if marker in text:continue
    if lang=='zh':
        paragraph='**原版表格口径：** 表 2 的 65.1% 是 optional-heartbeat 在八个模型上的 Macro Set-F1；表 3 的单模型最佳是 GPT-5.4 + optional heartbeat，Set-F1 为 79.1%。摘要将 65.1% 关联到 GPT-5.4，与表格不一致；此处以表 2/3 的明确分母为准。[原文表 2–3](https://arxiv.org/html/2607.12385v1)'
    else:
        paragraph='**Original-table scope:** the 65.1% in Table 2 is optional heartbeat’s Macro Set-F1 over eight models. The best individual-model result in Table 3 is GPT-5.4 + optional heartbeat at 79.1% Set-F1. The abstract associates 65.1% with GPT-5.4, unlike the tables; the explicit Table 2/3 denominators govern this reference. [Original Tables 2–3](https://arxiv.org/html/2607.12385v1)'
    paragraphs=text.split('\n\n')
    for i,para in enumerate(paragraphs):
        if '65.1' not in para or 'GPT-5.4' not in para:continue
        parts=re.split(r'(?<=[。.!?])\s+',para) if lang=='en' else re.split(r'(?<=[。！？])',para)
        keep=[x for x in parts if not ('65.1' in x and 'GPT-5.4' in x)]
        paragraphs[i]=(' '.join(keep) if lang=='en' else ''.join(keep)).strip()
    text='\n\n'.join(x for x in paragraphs if x)
    addition=marker+'\n\n'+paragraph+'\n\n<!-- RELEASE-TABLE-CORRECTION:END -->\n\n'
    target='<!-- RESEARCH-DECISION:START -->'
    text=text.replace(target,addition+target,1) if target in text else text+'\n\n'+addition
    write(f'benchmarks/pm-bench{ext}.md',text)

p=ROOT/'docs/README_PUBLICATION.md';text=p.read_text()
if 'RELEASE_REFERENCES.md' not in text:
    text+='\n## Historical result headers\n\nEvery benchmark note carries a frozen historical reference directly under its title.\nEdit `data/release-references.json`, not generated blocks or current leaderboard data.\nThe normal renderer updates both languages and `--check` validates them. See\n[Historical release references](RELEASE_REFERENCES.md) for version, scope, and missing-evidence rules.\n'
write('docs/README_PUBLICATION.md',text)
assert all(digest(Path(path))==value for path,value in before.items()),'Protected canonical or result data changed'
print('Authored original-source references:',len(curated))
print('Retained frozen ledger references:',len(imported),imported)
print('Final reference states:',dict(Counter(r['status'] for r in refs.values())))
print('All 146 identities, timestamps, citation snapshots, and 44 result files are unchanged.')
