#!/usr/bin/env python3
"""One-shot, idempotent publication input; excluded from the final main tree."""
from __future__ import annotations
import copy
import json
import re
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AS_OF = '2026-09-23'
INTAKE = '2026-09-22T23:35:54Z'
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
def load(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))
def write(path, text):
    (ROOT / path).parent.mkdir(parents=True, exist_ok=True)
    (ROOT / path).write_text(text.rstrip() + '\n', encoding='utf-8')
def dump(path, value):
    write(path, json.dumps(value, ensure_ascii=False, indent=2))

# These are accepted instruments, not an unreviewed discovery queue.
NEW = [
 {
  'id':'dolphinbench','name':'DolphinBench','area':'agent-memory','released':'2026-09-21','published_at':'2026-09-21T17:54:35Z','importance':4,'evolution_role':'frontier',
  'summary':'Tests history-dependent actions in simulated work apps with frozen memory checkpoints, paired history certification, and accuracy, total cost, and latency reporting.',
  'capabilities':['history-conditioned-action','long-term-user-context','memory-utility-cost-tradeoff'],
  'environment':['simulated-work-apps','three-personas','chronological-message-ingestion','frozen-memory-checkpoint'],
  'protocol':['600-action-tests','paired-history-certification','per-test-app-reset','deterministic-and-semantic-grading','accuracy-cost-latency'],
  'scale':'Three simulated personas, about 500,000 user-message tokens and 200 tasks each; 600 tasks overall.',
  'measurement_strength':'Moves beyond explicit historical QA by checking recorded actions under a frozen memory checkpoint and requiring lifecycle cost and latency alongside accuracy.',
  'coverage_gap':'Three simulated personas and selector-agent-dependent task certification do not establish natural-user generalization; frozen evaluation does not measure learning across test tasks or real provider-time aging.',
  'confounders':['ingestion-agent-and-model','memory-provider-configuration','task-selection-agent','semantic-grader','provider-processing-completion','lifecycle-cost-accounting','test-state-isolation'],
  'artifacts':{'paper':'https://arxiv.org/abs/2609.24971','code':'https://github.com/mem0ai/dolphinbench','project':'https://dolphinbench.ai'},
  'artifact_access':'Public simulated environment, dataset, runner, graders and reference workflows. Official overview and canonical protocol were reviewed; no independent benchmark run was performed.',
  'protocol_sources':['https://github.com/mem0ai/dolphinbench/blob/main/README.md','https://github.com/mem0ai/dolphinbench/blob/main/docs/CANONICAL_EVALUATION.md'],
  'first_seen_at':'2026-09-22T15:14:30Z',
  'observation_basis':'Earliest retained timestamped Radar mention: commit faa68df6831eee71fe8ec22349cc8ef323f4e7ea. Earlier unlogged discovery is not reconstructed.',
  'zh_summary':'在模拟工作应用中，以冻结记忆、历史依赖对照和逐题状态重置，测任务行动、总成本与延迟。',
  'zh_delta':'相较显式历史问答，把记忆效用落到应用中的实际动作，并要求联合报告生命周期成本与延迟。'
 },
 {
  'id':'memcalib','name':'MemCalib','area':'agent-memory','released':'2026-09-21','published_at':'2026-09-21T08:22:21Z','importance':4,'evolution_role':'frontier',
  'summary':'Tests whether each supplied memory proposition is ignored, used as bounded support, or allowed to control a response at its query-specific target level.',
  'capabilities':['memory-use-calibration','over-use-detection','under-use-detection','query-conditioned-constraint-use'],
  'environment':['supplied-composite-memory','health-assistance-coding','atom-level-targets-and-rubrics'],
  'protocol':['ignore-bound-control-targets','held-out-test-set','sample-calibration-score','exact-calibration','directional-error-reporting'],
  'scale':'15,000 examples with 234,220 atomic propositions: 13,500 training and 1,500 held-out test examples; 1,500 training examples are reserved for validation in the paper.',
  'measurement_strength':'Separates too much memory influence from too little, rather than treating memory access or aggregate answer quality as calibrated use.',
  'coverage_gap':'The evaluated object is use of already supplied context, not retrieval, writing, maintenance, or closed-loop task success; rubric and evaluator implementation affect the reported calibration.',
  'confounders':['ideal-use-annotation','atom-decomposition','rubric-interpretation','evaluator-version','domain-mixture','training-test-separation'],
  'artifacts':{'paper':'https://arxiv.org/abs/2609.24259','project':'https://quark-medical.github.io/MemCalib-Project/','data':'https://huggingface.co/datasets/ZiLaotou/MemCalib'},
  'artifact_access':'Dataset and detailed official project description are public. The advertised code repository contained only a short README at verification; no executable evaluator was verified there.',
  'protocol_sources':['https://github.com/Quark-Medical/MemCalib-Project/blob/main/index.html','https://huggingface.co/datasets/ZiLaotou/MemCalib','https://github.com/Quark-Medical/memcalib'],
  'source_blob_shas':{'https://github.com/Quark-Medical/MemCalib-Project/blob/main/index.html':'b3a4bc58d73b1164b0908a079d387149dc1de1da'},
  'zh_summary':'对上下文中每条记忆命题，测它是否按当前问题所需被忽略、局部使用或作为决定性约束。',
  'zh_delta':'把记忆影响不足与过度影响分开，形成命题级、依赖当前问题的记忆使用校准诊断。'
 },
 {
  'id':'chemclir-bench','name':'ChemCLIR-Bench','area':'rag','released':'2026-09-19','published_at':'2026-09-19T22:18:58Z','importance':3,'evolution_role':'frontier',
  'summary':'Tests chemical-patent retrieval across query and document languages, with language-pair, query-origin, ranking-depth, and recoverability diagnostics.',
  'capabilities':['cross-lingual-retrieval','technical-domain-retrieval','ranking-depth-diagnosis'],
  'environment':['google-patents-and-epo','multilingual-technical-text','generated-and-translated-queries'],
  'protocol':['mteb-corpus-queries-qrels','recall-at-10','mrr-at-10','same-versus-cross-language','query-origin-stratification'],
  'scale':'The paper evaluates eight embedding models across five languages; the public generation pipeline is configurable and supports additional translation languages, so its current configuration is not assumed identical to the paper cohort.',
  'measurement_strength':'Extends heterogeneous retrieval evaluation to language-pair and retrieval-depth failures in industrial technical text.',
  'coverage_gap':'Static retrieval quality does not establish answer correctness or agentic search utility; generated queries and uneven multilingual claim-text coverage constrain external validity.',
  'confounders':['english-seeded-query-generation','synthetic-translation','patent-family-overlap','language-dependent-context-fields','qrel-construction','corpus-and-model-version'],
  'artifacts':{'paper':'https://arxiv.org/abs/2609.23231','code':'https://github.com/MohammadKhodadad/Multi-Lingual-QAC','data':'https://huggingface.co/datasets/MehdiAstaraki/multilingual_GP'},
  'artifact_access':'Public construction and MTEB evaluation pipeline; official README links both Google Patents and EPO dataset releases.',
  'protocol_sources':['https://github.com/MohammadKhodadad/Multi-Lingual-QAC/blob/main/README.md','https://huggingface.co/datasets/MehdiAstaraki/multi-lingual-qac-epo'],
  'source_blob_shas':{'https://github.com/MohammadKhodadad/Multi-Lingual-QAC/blob/main/README.md':'50fdb5882456a34e7e51010f8ffc0b5a8f52858f'},
  'zh_summary':'在化学专利中，按查询与目标语言、原生或翻译查询及排名深度，诊断跨语言检索。',
  'zh_delta':'在异构领域检索之外，把技术文献的语言对差异、翻译来源和相关文档排名深度显式化。'
 },
 {
  'id':'locomo-conv','name':'LoCoMo-Conv','area':'agent-memory','released':'2026-09-03','published_at':'2026-09-03T07:24:33Z','importance':4,'evolution_role':'frontier',
  'summary':'Recasts LoCoMo into dialog, implicit, counterfactual, and composed queries while separating source-evidence recall from conversational response quality.',
  'capabilities':['implicit-memory-retrieval','composed-memory-use','counterfactual-memory-use','conversational-grounding'],
  'environment':['locomo-conversations','rewritten-conversational-queries','source-dia-id-provenance'],
  'protocol':['fixed-original-gold-evidence','four-query-styles','retrieval-recall-precision-f1','top-k-oracle-no-memory-controls','response-quality-judges'],
  'scale':'Four conversational query styles over LoCoMo, including 1,069 composed clusters pairing two source questions; source histories are reused rather than newly collected longitudinal interactions.',
  'measurement_strength':'Holds source histories and evidence fixed while exposing whether explicit QA wording was revealing what memory to retrieve.',
  'coverage_gap':'Rewritten prompts do not establish natural conversational behavior or action success; evidence-ID attribution and response-judge criteria can favor different memory representations.',
  'confounders':['query-rewriting','category-filtering','source-id-attribution','raw-versus-abstractive-memory','retrieval-budget','answerer-and-judge'],
  'artifacts':{'paper':'https://arxiv.org/abs/2609.03467','code':'https://github.com/MiuLab/LoCoMo-Conv','data':'https://github.com/MiuLab/LoCoMo-Conv/tree/main/data'},
  'artifact_access':'Public rewritten queries, composed clusters, retrieval and response evaluators, oracle controls, and variance-analysis scripts.',
  'protocol_sources':['https://github.com/MiuLab/LoCoMo-Conv/blob/main/README.md','https://github.com/MiuLab/LoCoMo-Conv/blob/main/retrieval/compute_retrieval_metrics.py'],
  'source_blob_shas':{'https://github.com/MiuLab/LoCoMo-Conv/blob/main/README.md':'32dfd0ecb370437224061e1e48edd3e7c3d0ba7a','https://github.com/MiuLab/LoCoMo-Conv/blob/main/retrieval/compute_retrieval_metrics.py':'70fd7f3e930aca8a8a18a104feb0b2fe4bd409bc'},
  'first_seen_at':'2026-09-22T15:14:30Z',
  'observation_basis':'Earliest retained timestamped Radar mention: commit faa68df6831eee71fe8ec22349cc8ef323f4e7ea. Earlier unlogged discovery is not reconstructed.',
  'zh_summary':'保留 LoCoMo 的历史和证据，将问题改为对话、隐式、反事实及组合查询，分别测检索与回答。',
  'zh_delta':'固定历史与标准证据，检查显式问答措辞是否泄露了应检索的记忆，并区分检索成功与回答落地。'
 },
 {
  'id':'statformbench','name':'StatFormBench','area':'data-agent','released':'2026-09-02','published_at':'2026-09-02T01:37:17Z','importance':4,'evolution_role':'frontier',
  'summary':'Tests the upstream formulation of a statistical problem: selecting its coarse and fine task category, identifying variables, and assigning their roles.',
  'capabilities':['statistical-task-formulation','method-classification','variable-identification','variable-role-assignment'],
  'environment':['statistics-textbook-problems','data-science-cases','natural-language-analysis-goals'],
  'protocol':['coarse-and-fine-classification-accuracy','variable-set-jaccard','variable-precision-and-recall','variable-role-consistency'],
  'scale':'1,013 samples from five statistics textbooks and a data-science case library, spanning 20 coarse and 85 fine categories; the paper evaluates 14 models.',
  'measurement_strength':'Makes formulation observable before execution instead of assuming that the analysis target and relevant variables have already been correctly specified.',
  'coverage_gap':'Correct formulation is not an executed, statistically valid analysis; textbook category labels may underrepresent ambiguous business goals and multiple valid formulations.',
  'confounders':['taxonomy-choice','textbook-exposure','variable-name-normalization','role-rubrics','prompt-and-model-version','evaluation-parsing'],
  'artifacts':{'paper':'https://arxiv.org/abs/2609.01982','code':'https://github.com/THU-CongLab/StatFormBench','data':'https://huggingface.co/datasets/THU-CongLab/StatFormBench'},
  'artifact_access':'Public dataset, prompts, model runner, evaluation modules and saved outputs. The English entry is lowercase readme.md.',
  'protocol_sources':['https://github.com/THU-CongLab/StatFormBench/blob/main/readme.md','https://github.com/THU-CongLab/StatFormBench/blob/main/src/evaluation/variable_metrics.py'],
  'source_blob_shas':{'https://github.com/THU-CongLab/StatFormBench/blob/main/readme.md':'09300ae5f20bda2f1ac63a0fc2b14e108e11a073','https://github.com/THU-CongLab/StatFormBench/blob/main/src/evaluation/variable_metrics.py':'d6fef2ed6128d63442a9fdefb553cf3fedf10a19'},
  'zh_summary':'在执行分析之前，测统计问题的粗细类别选择、相关变量识别及变量角色分配。',
  'zh_delta':'把通常默认正确的分析目标与变量选择，提前拆成独立于代码执行的诊断对象。'
 },
 {
  'id':'livedrbench','name':'LiveDRBench','area':'rag','released':'2025-08-06','published_at':'2025-08-06T08:09:28Z','importance':4,'evolution_role':'transition','map_delta':'none',
  'summary':'Tests broad research as structured claim discovery, scoring precision, recall, and F1 separately from the writing quality of a long report.',
  'capabilities':['broad-evidence-discovery','structured-claim-synthesis','reference-grounding'],
  'environment':['public-web-research','scientific-and-event-search','structured-output-contract','encrypted-reference-answers'],
  'protocol':['100-research-tasks','category-specific-claim-evaluators','precision-recall-f1','question-level-overall-average','test-only-release'],
  'scale':'100 tasks in eight categories; the official v1-full release was collected in May-June 2025. Future refresh plans do not make that snapshot a live-changing test set.',
  'measurement_strength':'Separates broad discovery of supported claims from report style and provides a missing predecessor for later checklist- and claim-oriented research evaluation.',
  'coverage_gap':'A fixed reference claim set and judge can miss alternative valid evidence; coverage is concentrated in a few scientific and event domains and does not measure report writing quality.',
  'confounders':['web-drift','reference-set-completeness','judge-model','output-schema','question-versus-category-aggregation','test-contamination'],
  'artifacts':{'paper':'https://arxiv.org/abs/2508.04183','code':'https://github.com/microsoft/LiveDRBench','data':'https://huggingface.co/datasets/microsoft/LiveDRBench'},
  'artifact_access':'Public test-only dataset and category-specific evaluation code; official evaluator defaults to a GPT-4o judge. Historical backfill, not a September 2026 release.',
  'protocol_sources':['https://github.com/microsoft/LiveDRBench/blob/main/README.md','https://github.com/microsoft/LiveDRBench/blob/main/src/evaluate.py','https://proceedings.iclr.cc/paper_files/paper/2026/hash/114e1dc345fe31b8b9b0c6f7b55a0644-Abstract-Conference.html'],
  'source_blob_shas':{'https://github.com/microsoft/LiveDRBench/blob/main/README.md':'0f42baf1968b69a56ccf9a355ae4a025cc661c70','https://github.com/microsoft/LiveDRBench/blob/main/src/evaluate.py':'80f43eda40c265b73573954de69fa8db27a55e2e'},
  'zh_summary':'把广泛研究表示为结构化主张发现，以精确率、召回率和 F1 评分，而非评价长报告文风。',
  'zh_delta':'把研究中的证据与主张发现同报告写作拆开，补齐后续清单式、主张式研究评测的历史参照。'
 }
]

# Bilingual authored reasoning. Examples below are explicitly illustrative.
TEXT = {
'dolphinbench': {
 'title':['冻结记忆后，过去的历史能否改善真实动作','testing history-dependent actions under frozen memory'],
 'measure':[
  'DolphinBench 用三个模拟知识工作用户、每人约 500K tokens 的消息历史和 200 个任务，考察历史能否改变工作应用中的正确行动，共 600 题。评测读取动作及应用状态，而不是只问模型是否记得某句话。数据中的应用是模拟环境，不能据此声称已经验证真实企业部署。[官方说明](https://github.com/mem0ai/dolphinbench/blob/main/README.md)',
  'DolphinBench evaluates three simulated knowledge-work personas, each with roughly 500K tokens of user messages and 200 tasks, for 600 tests overall. The target is a correct action in a work application, not merely a verbal recollection. Its applications are simulated; action-grounded evaluation should not be described as evidence from a production deployment. [Official overview](https://github.com/mem0ai/dolphinbench/blob/main/README.md)'],
 'delta':[
  '相较 LoCoMo 的历史问答，它要求历史参与任务完成；相较持续交互和经验学习评测，它的标准测试冻结已建好的记忆，避免前一道测试教会后一道。这个控制测的是既有历史的可用性，不是智能体在 200 道题中越做越好。',
  'Compared with LoCoMo, historical information must support task completion. Compared with evaluations of continued learning across episodes, the standard test freezes the ingested memory so that one test cannot teach the next. This isolates utility of the existing history, not improvement over the 200-test sequence.'],
 'protocol':[
  '按原始时间顺序，通过待测智能体正常的记忆接口摄入消息；确认服务端处理完成并记录 checkpoint。每道测试使用新对话和新应用状态，保持记忆冻结，保存运行、动作与评分证据。任务认证要求指定智能体在两次提供相关历史时都成功、两次不提供时都失败；这是筛选协议下的历史依赖，不是对所有模型的必要性证明。[标准协议](https://github.com/mem0ai/dolphinbench/blob/main/docs/CANONICAL_EVALUATION.md)',
  'Messages are ingested chronologically through the tested agent\'s normal memory interface. Processing must complete before a checkpoint is recorded. Each test starts a fresh conversation and fresh application state while memory remains frozen; trajectories, actions, and grader evidence are retained. Certification requires two successes with relevant history and two failures without it for the specified certification agent. That is a conditional selection test, not proof that every possible model needs the history. [Canonical protocol](https://github.com/mem0ai/dolphinbench/blob/main/docs/CANONICAL_EVALUATION.md)'],
 'evidence':[
  '这次核验的决定性证据是公开、可执行的状态隔离与评分协议；没有独立重跑 600 题，也不把不同 writer、provider 和模型的成绩差直接归因给检索器。官方资料中存在较早的单 persona 参考结果与更新的多配置概览，必须按具体运行的模型、覆盖范围、checkpoint 和修复记录读分数，不能混成同一榜单。',
  'The decisive evidence reviewed here is the public, executable state-isolation and grading protocol. This Radar has not independently rerun the 600 tasks. Differences between ingestion agents, providers, and answer models do not isolate a retriever effect. Official materials include older single-persona reference results alongside newer configuration summaries: interpret a score with its exact model, coverage, checkpoint, and recovery records rather than merging those releases into one ranking.'],
 'gap':[
  '最强混杂来自摄入模型、provider 的异步处理和任务筛选模型。历史里模拟的多年日期也不等于服务真实运行了多年，因此不能据此验证真实时间衰减。成本应分别报告摄入、维护与查询，并明确如何摊销；缺失成本不能记为零。三个模拟用户不足以代表跨用户、权限变化和长期在线学习。',
  'The strongest confounders are the ingestion model, asynchronous provider processing, and certification agent. Dates spanning years inside messages are not years of real provider operation and do not validate real-time decay. Separate ingestion, maintenance, and query costs, specify amortization, and keep missing costs distinct from zero. Three simulated users leave cross-user transfer, permission changes, and long-running online learning unmeasured.'],
 'use':['适合检验长期用户上下文能否改善有状态工作流，以及准确率收益是否值得生命周期成本。','Use it to test whether long-term user context improves stateful workflows and whether that benefit survives lifecycle cost accounting.'],
 'example':['示意：历史中说明了某项目的沟通对象和长期约束；新任务要求在应用中更新项目，不能仅在答案中复述旧约束。','Illustrative task: prior messages identify a project contact and standing constraint; a new request requires updating the project in an application rather than merely repeating the remembered constraint.'],
 'experiment':['固定 writer、执行模型、接口与 grader，比较无记忆、等预算检索和相关历史直接给定；分开报告动作成功、证据访问和总成本。把允许测试期写入的版本列为另一协议，不与冻结版本混比。','Hold the writer, executor, interfaces, and graders fixed; compare no memory, budget-matched retrieval, and supplied relevant history. Report action success, evidence access, and total cost separately. Treat test-time memory updates as a different protocol rather than pooling them with frozen-memory scores.'],
 'pair':['locomo-conv','memoryarena','mem2actbench']
},
'memcalib': {
 'title':['记忆应该影响回答多少，而不只是有没有被找到','calibrating how strongly supplied memory influences a response'],
 'measure':[
  'MemCalib 的对象是已经放进上下文的记忆命题。针对当前问题，每条命题有三级目标：A / Ignore 不应留下特定影响，B / Bound 只提供局部支持，C / Control 应决定关键结论或约束。公开项目页给出 15,000 个样本、234,220 条命题，训练集 13,500、测试集 1,500；论文另从训练部分保留 1,500 个验证样本。[官方数据与协议](https://github.com/Quark-Medical/MemCalib-Project/blob/main/index.html)',
  'MemCalib evaluates propositions already supplied in context. For the current query, an atom should be ignored (A), provide bounded local support (B), or control a material conclusion or constraint (C). The official project specifies 15,000 examples and 234,220 atoms: 13,500 training and 1,500 held-out test examples, with a further 1,500 training examples reserved for validation in the paper. [Official data and protocol](https://github.com/Quark-Medical/MemCalib-Project/blob/main/index.html)'],
 'delta':[
  '相较只问记忆是否相关、是否召回或最终回答是否正确，这里检查的是命题对回答的影响强度。相较 MemTrapBench 等负迁移诊断，它同时保留影响过多与影响不足两个方向；完全忽略历史不能被当成良好的记忆策略。',
  'Compared with relevance, recall, or aggregate answer correctness, the target is the degree of influence each proposition should have. Relative to negative-transfer diagnostics such as MemTrapBench, it keeps both over-use and under-use visible. Ignoring all history is not automatically a well-calibrated memory policy.'],
 'protocol':[
  '样本包含问题、组合记忆块、拆出的命题、理想使用等级和命题级 rubric，覆盖健康、一般助手和编码三类情境。官方页面列出 Sample Calibration Score、Exact Calibration 以及双向错误指标。本次核验了公开数据卡和项目说明；代码仓库目前只有短 README，尚未核验到可执行评分器，因此不能承诺逐项复现其数值。[数据](https://huggingface.co/datasets/ZiLaotou/MemCalib) · [代码发布状态](https://github.com/Quark-Medical/memcalib)',
  'An example contains a query, composite memory blocks, extracted propositions, ideal use levels, and atom-specific rubrics across health, general assistance, and coding. The official page names Sample Calibration Score, Exact Calibration, and directional error metrics. This review checked the dataset card and detailed project description. The advertised code repository currently contains only a short README; no executable scorer was verified, so numerical score reproduction is not certified. [Dataset](https://huggingface.co/datasets/ZiLaotou/MemCalib) · [Code release status](https://github.com/Quark-Medical/memcalib)'],
 'evidence':[
  '公开协议足以把“记忆使用校准”定义为可复用数据与标注任务，因而单独收录这个 benchmark；不把同文的 MemCalib-RL 当作第二个基准。论文报告常见训练方法可能改善一个方向却恶化另一个方向，这一报告提示必须同时读双向指标，不证明某种优化在所有情境都更好。[论文](https://arxiv.org/abs/2609.24259)',
  'The public data and annotation contract define a reusable memory-use task, which is the accepted contribution here; MemCalib-RL is not registered as a second benchmark. The paper reports that common training approaches can improve one error direction while worsening the other. This motivates inspecting both directions, not a claim that one optimization dominates under every setting. [Paper](https://arxiv.org/abs/2609.24259)'],
 'gap':[
  '最需要验证的是 B 与 C 的标注边界、命题拆分和 rubric 解释是否稳定。该评测把记忆直接提供给模型，不测检索、写入、来源权限或环境行动。健康情境的占比也会影响总分；不能把总分直接推广成医疗任务的可靠性结论。',
  'The key validity questions concern the stability of the B/C boundary, atom decomposition, and rubric interpretation. Providing the memories directly leaves retrieval, writing, source authority, and environment actions unmeasured. The health-heavy domain mixture also affects the aggregate; calibration scores are not evidence of clinical reliability.'],
 'use':['适合在检索之后诊断模型是否过度个性化、忽略约束或把局部事实错误提升为全局决策。','Use it after retrieval to diagnose over-personalization, ignored constraints, or promotion of a locally relevant fact into a global decision rule.'],
 'example':['示意：项目使用某种语言是当前实现的硬约束，旧项目偏好只是背景；模型应让前者控制答案，不能机械采用后者。','Illustrative task: the current project\'s implementation language is a binding constraint while a preference from an old project is background. The former should control the answer without mechanically adopting the latter.'],
 'experiment':['保持生成模型和输入记忆不变，比较完整记忆、相关命题 oracle 与移除干扰命题；按 A/B/C 分组报告双向错误，并对边界样本做人类与多评分器一致性检查。发布评分器之前，明确标出本地 rubric 实现与原论文结果不可直接混比。','Keep the generator and supplied memories fixed; compare full memory, an oracle of relevant atoms, and removal of distractors. Report both error directions by A/B/C class and audit boundary cases with human and multiple-evaluator agreement. Until the scorer is released, clearly separate local rubric implementations from the paper\'s reported scores.'],
 'pair':['memtrapbench','memory-trust-gap','locomo-conv']
},
'chemclir-bench': {
 'title':['把跨语言技术检索的失败拆到语言对和排名深度','diagnosing language-pair and ranking-depth failures in patent retrieval'],
 'measure':[
  'ChemCLIR-Bench 在 Google Patents 与 EPO 化学专利材料上比较同语言与跨语言检索。论文评测五种语言、八个 embedding 模型；检索脚本另提供按查询语言、原生或合成翻译来源、目标语言及语言对拆分的 Recall@10 / MRR@10 分析。[论文](https://arxiv.org/abs/2609.23231) · [官方实现](https://github.com/MohammadKhodadad/Multi-Lingual-QAC/blob/main/README.md)',
  'ChemCLIR-Bench compares same-language and cross-language retrieval over chemical-patent material from Google Patents and EPO. The paper evaluates five languages and eight embedding models. The released pipeline additionally reports Recall@10 and MRR@10 by query language, original versus synthetic-translation origin, target language, and language pair. [Paper](https://arxiv.org/abs/2609.23231) · [Official implementation](https://github.com/MohammadKhodadad/Multi-Lingual-QAC/blob/main/README.md)'],
 'delta':[
  '相较 BEIR 的跨领域检索，这里的关键变量是专业领域中查询语言和证据语言不一致。更深的排名诊断可以区分“相关证据完全未找到”和“仍可找到但排得太低”，因此一个总体 Recall 不足以解释系统退化。它不是迭代式搜索或完整 RAG 问答评测。',
  'Compared with BEIR\'s cross-domain retrieval, the controlled contrast is a mismatch between query and evidence language inside technical subject matter. Ranking-depth diagnostics help distinguish missing evidence from evidence that remains recoverable but is ranked too low. One aggregate recall cannot explain that distinction. This is not an iterative-search or end-to-end RAG answer benchmark.'],
 'protocol':[
  '公开流水线导出 MTEB 格式的 corpus、queries 和 qrels。当前生成路径先为文档产生英语问答，经过语言、忠实度与检索质量检查，再翻译到目标语言；运行记录保存数据规模、模型、Git 版本与逐题结果。仓库允许更多翻译语言，不能把当前配置直接等同于论文的五语言实验。',
  'The pipeline exports corpus, queries, and qrels in MTEB retrieval format. Its current generation path creates English QAs, checks language, faithfulness, and retrieval quality, and translates them into target languages. Run metadata records dataset sizes, models, Git revision, and per-query results. The configurable repository supports additional translation languages and is not automatically the same as the five-language paper experiment.'],
 'evidence':[
  '论文摘要报告最佳模型的 Recall@10 从同语言 0.72 降至跨语言 0.53。这是该数据与配置下的结果，不是跨领域通用幅度，更不能直接推算下游答案损失。仓库还明确说明多语言正文和权利要求比标题、摘要稀疏，部分字段主要有英语；不同语言的可见内容必须检查。[结果来源](https://arxiv.org/abs/2609.23231) · [字段限制](https://github.com/MohammadKhodadad/Multi-Lingual-QAC/blob/main/README.md)',
  'The abstract reports a best-model Recall@10 drop from 0.72 in the monolingual setting to 0.53 cross-lingually. That is a source-reported result for its dataset and configuration, not a universal cross-domain effect or a direct estimate of answer degradation. The repository also warns that multilingual descriptions and claims are much sparser than titles and abstracts, with some fields mainly available in English; visible content must therefore be checked per language. [Result source](https://arxiv.org/abs/2609.23231) · [Field limitations](https://github.com/MohammadKhodadad/Multi-Lingual-QAC/blob/main/README.md)'],
 'gap':[
  '最强替代解释是英语种子查询、翻译风格和各语言内容字段不等价，而不只是 embedding 对齐能力。还应检查专利家族重叠、相关性标签构造与样本过滤。公开数据的存在不代表这些混杂已经被完全排除。',
  'The strongest alternative explanation involves English-seeded queries, translation style, and unequal content fields, not only embedding alignment. Patent-family overlap, qrel construction, and filtering also need auditing. Public data availability does not mean these confounders have been eliminated.'],
 'use':['适合多语言企业知识库或技术检索中的语言对诊断，作为下游 RAG 实验的检索层检查。','Use it for language-pair diagnostics in technical or enterprise retrieval, as a retrieval-layer check before downstream RAG experiments.'],
 'example':['示意：中文查询描述一个化学工艺，相关专利只有德文摘要；只在中文结果中命中类似主题并不等于找到支持证据。','Illustrative task: a Chinese query describes a chemical process whose supporting patent has a German abstract; finding topically similar Chinese text is not equivalent to locating the evidence.'],
 'experiment':['固定文档字段、专利家族划分和 qrels，比较多语言 dense、查询翻译加 BM25 与 hybrid；逐语言对报告 Recall/MRR，并把原生问题和翻译问题分开，控制相同检索与重排预算。','Fix document fields, patent-family splits, and qrels; compare multilingual dense retrieval, query translation plus BM25, and hybrid retrieval. Report Recall/MRR per language pair, separate original and translated queries, and match retrieval and reranking budgets.'],
 'pair':['beir','ontologybench','commercial-tax']
},
'locomo-conv': {
 'title':['用户不直接索取旧事实时，记忆还能不能被正确调用','retrieving and using memory without an explicit factual query'],
 'measure':[
  'LoCoMo-Conv 保留 LoCoMo 的历史、标准答案和证据 dia_ids，将查询改为 dialog、implicit、counterfactual、composed 四类，并分别测检索与自由文本回答。组合部分有 1,069 个由两个原始问题构成的多记忆簇。来源是改写后的既有历史，不是新采集的自然长期用户互动。[官方协议与数据](https://github.com/MiuLab/LoCoMo-Conv/blob/main/README.md)',
  'LoCoMo-Conv preserves LoCoMo histories, gold answers, and evidence dia_ids while recasting queries into dialog, implicit, counterfactual, and composed styles. It evaluates retrieval and free-form responses separately. The composed component has 1,069 clusters pairing two source questions. These are rewrites over existing histories, not newly collected natural longitudinal interactions. [Official protocol and data](https://github.com/MiuLab/LoCoMo-Conv/blob/main/README.md)'],
 'delta':[
  '相较 LoCoMo，固定历史后改变的是“当前请求怎样表达”。它能够检查显式问题是否提示了该找什么。与 LoCoMo-Plus 等约束一致性评测也应区分：这里特别保留原始证据标识，便于观察查询形式、检索证据和回答表现之间的差距。',
  'Compared with LoCoMo, the intervention changes how the current request is expressed while keeping the history fixed. It tests whether explicit QA was revealing what to retrieve. Distinguish it from constraint-consistency evaluations such as LoCoMo-Plus: retaining source evidence identifiers makes the query-form, evidence-retrieval, and response-quality gaps particularly inspectable.'],
 'protocol':[
  '公开运行入口包含 top-K、oracle、no-memory、query rewriting 和 CoT 对照。检索脚本将返回内容映射回 dia_ids：原始文本可用子串匹配，抽象记忆可通过 metadata 的 dia_ids 归属；组合题使用成员证据的并集。因而 Recall 不等于返回摘要语义完整，跨表示比较必须保留同等可靠的来源映射。[检索评分代码](https://github.com/MiuLab/LoCoMo-Conv/blob/main/retrieval/compute_retrieval_metrics.py)',
  'Public runners expose top-K, oracle, no-memory, query-rewriting, and CoT controls. The retrieval evaluator maps returned material to dia_ids through turn-text substring matching or metadata provenance for abstractive memories. Composed questions use the union of member evidence. Consequently, evidence recall is not semantic completeness of a returned summary: cross-representation comparisons require equally reliable source attribution. [Retrieval scoring implementation](https://github.com/MiuLab/LoCoMo-Conv/blob/main/retrieval/compute_retrieval_metrics.py)'],
 'evidence':[
  '论文报告隐式与组合查询暴露了 QA 不易看到的检索差距，并区分强检索与好回答。还描述了 implicit 查询中的 silent grounding：历史可能改善回答的情境适配，却不显式复述标准事实。因此不能只用“是否说出 gold fact”代替对话质量，也不能把各 judge 的总分合为一个无条件排名。[论文](https://arxiv.org/abs/2609.03467)',
  'The paper reports retrieval gaps for implicit and composed queries that explicit QA can obscure, and separates strong retrieval from good responses. It also describes silent grounding: memory may improve contextual appropriateness without explicitly stating the gold fact. Gold-fact mention is therefore not a complete conversational-quality metric, and scores from different judges should not be merged into an unconditional ranking. [Paper](https://arxiv.org/abs/2609.03467)'],
 'gap':[
  '最强混杂是改写质量、类别过滤、来源标记完整性和回答评分标准。仅看 raw-turn 与抽象 memory 的 Recall 差，可能把映射或信息保留差异误认为召回算法差异。它仍不测外部应用行动、长期权限治理或持续学习成本。',
  'The strongest confounders are rewriting quality, category filtering, source-ID completeness, and response criteria. A raw-turn versus abstractive-memory recall gap can reflect attribution or information-preservation differences rather than retrieval policy alone. External application actions, long-term permission governance, and continual-learning costs remain unmeasured.'],
 'use':['适合研究显式 QA 之外的日常对话记忆，以及检索成功为什么没有转化为回答质量。','Use it for conversational memory beyond explicit QA and for diagnosing why successful retrieval does not translate into response quality.'],
 'example':['示意：用户只说“这次周末照旧安排吧”，并未直接问过去偏好；系统需要推断应找哪段历史，而不是匹配原 QA 中的名词。','Illustrative task: a user says “plan this weekend as usual” rather than asking for an old preference; the system must infer which history matters without copying the nouns of an explicit QA prompt.'],
 'experiment':['对同一历史和 source question 成对比较显式与隐式版本，固定 embedding、回答器、top-K 和 token 预算；再给定 oracle 证据。分别检查来源召回、记忆语义保留、事实使用和对话适配，避免把多个阶段折成一个总分。','Pair explicit and implicit versions of the same source question and history, fixing embeddings, answerer, top-K, and token budget; then supply oracle evidence. Audit source recall, semantic preservation, fact use, and conversational appropriateness separately rather than collapsing all stages into one score.'],
 'pair':['locomo','locomo-plus','dolphinbench']
},
'statformbench': {
 'title':['代码执行之前，先检验分析问题有没有定义对','testing whether the analysis problem is formulated before code execution'],
 'measure':[
  'StatFormBench 把统计分析的上游步骤拆为问题分类与变量识别、角色分配。它来自五本统计教材和数据科学案例库，含 1,013 个样本、20 个粗粒度和 85 个细粒度类别。目标是分析该怎样定义，而不是一个已经指定好的程序是否输出正确结果。[论文](https://arxiv.org/abs/2609.01982)',
  'StatFormBench decomposes the upstream analysis step into statistical problem classification, variable identification, and role assignment. It contains 1,013 samples from five statistics textbooks and a data-science case library, covering 20 coarse and 85 fine categories. The target is how to formulate the analysis, not whether an already specified program returns the expected result. [Paper](https://arxiv.org/abs/2609.01982)'],
 'delta':[
  '相较 DS-1000 的代码实现和 Spider 的查询生成，它减少了“用户已经给出正确分析目标”这个默认前提。与完整 DataScienceBench 互补：当最后结果出错时，可以先检查方法类别、变量集合和角色是否在执行之前就选错。',
  'Compared with DS-1000 code implementation or Spider query generation, it relaxes the assumption that the user has already supplied the right analysis target. It complements end-to-end DataSciBench: a wrong final result can first be checked for a wrong method category, variable set, or role assignment before execution begins.'],
 'protocol':[
  '官方运行器把样本和 prompt 发给指定模型，评测脚本读取输出并与参考答案匹配，报告粗细分类准确率、变量集合 Jaccard、precision、recall 和角色一致性。已核对的 variable_metrics.py 使用集合交并比计算 Jaccard；这类变量指标不是运行代码后的功能正确率。[运行与评分说明](https://github.com/THU-CongLab/StatFormBench/blob/main/readme.md) · [变量指标](https://github.com/THU-CongLab/StatFormBench/blob/main/src/evaluation/variable_metrics.py)',
  'The official runner sends samples and prompts to named models, then evaluation modules compare parsed outputs with references. Metrics include coarse/fine classification accuracy, variable-set Jaccard, precision, recall, and role consistency. The reviewed variable_metrics.py computes Jaccard from set intersection and union. These variable metrics are not functional correctness after executing code. [Runner and scoring guide](https://github.com/THU-CongLab/StatFormBench/blob/main/readme.md) · [Variable metrics](https://github.com/THU-CongLab/StatFormBench/blob/main/src/evaluation/variable_metrics.py)'],
 'evidence':[
  '论文在 14 个模型上报告最佳零样本细分类准确率 72.0、变量集合重合度 63.2，且两个子任务没有始终占优的同一模型。这些是各指标上的论文报告，不应拼成某一模型的单条成绩，也不表示分析执行有同样的成功率。[结果来源](https://arxiv.org/abs/2609.01982)',
  'Across 14 models, the paper reports best zero-shot fine classification accuracy of 72.0 and variable-set overlap of 63.2, with no model consistently best across both subtasks. These are source-reported best values for different metrics, not a fabricated single-model result and not an analysis-execution success rate. [Result source](https://arxiv.org/abs/2609.01982)'],
 'gap':[
  '教材可能进入训练语料；固定 taxonomy 也可能把多种合理分析压成唯一标签。变量别名、输出解析与角色 rubric 都影响测量。这个基准仍不验证实际数据中的统计假设、数值实现或业务目标含糊时的澄清行为。',
  'Textbooks may have appeared in model training, and a fixed taxonomy can compress multiple reasonable analyses into one label. Variable aliases, output parsing, and role rubrics affect the measurement. Statistical assumptions in actual data, numerical implementation, and clarification of ambiguous business goals remain unmeasured.'],
 'use':['适合给数据智能体增加执行前诊断，判断瓶颈在任务理解还是程序实现。','Use it as a pre-execution diagnostic to distinguish task-understanding failures from implementation failures in a data agent.'],
 'example':['示意：用户问“这次改版有没有改善留存”，模型先判断比较对象、结果变量与可能混杂，再决定分析；直接写出可运行的均值查询仍可能回答错问题。','Illustrative task: a user asks whether a redesign improved retention. The model must identify comparison groups, outcome variables, and possible confounders before choosing an analysis; an executable mean query may still answer the wrong question.'],
 'experiment':['固定执行引擎，把模型自行制定的分析与专家提供的 formulation 交给同一执行器；分别报告 formulation 分数和最终数值正确性，再对多解案例进行盲审。若专家 formulation 消除大部分失败，优先修任务定义，而非堆执行工具。','Feed model-generated versus expert-supplied formulations to the same executor. Report formulation metrics and final numerical correctness separately, then blind-review cases with multiple valid formulations. If expert formulations remove most failures, prioritize problem definition rather than adding execution tools.'],
 'pair':['ds-1000','datascibench','data-agent-benchmark']
},
'livedrbench': {
 'title':['把广泛证据发现同报告写作拆开','separating broad claim discovery from report writing'],
 'measure':[
  'LiveDRBench 把 deep research 定义为从大量来源中发现结构化主张与支持依据，而不是写得很长。官方 v1-full 含八类、100 个任务，数据采集于 2025 年 5—6 月；论文首发为 2025-08-06。此次是历史补录，不把名称里的 Live 或未来更新计划当成测试集持续更新的证据。[官方数据说明](https://github.com/microsoft/LiveDRBench/blob/main/README.md)',
  'LiveDRBench treats deep research as discovery of structured claims and their support across many sources, rather than production of lengthy prose. The official v1-full release has 100 tasks in eight categories, collected in May-June 2025; the paper first appeared on 2025-08-06. This is historical backfill. Neither the name Live nor a plan for future refreshes establishes that this test snapshot is continuously changing. [Official dataset description](https://github.com/microsoft/LiveDRBench/blob/main/README.md)'],
 'delta':[
  '相较报告整体打分，它通过中间的结构化主张把证据覆盖与写作质量分开；相较单答案搜索题，它要求更广的发现集合。这个缺失的历史参照有助于理解后续 ClaimProbe 和 Mr.LHDR 的主张、引用及依赖清单评测，但不能只因补录一篇论文就宣布新的领域趋势。',
  'Compared with holistic report grading, the intermediate claim representation separates evidence coverage from writing quality. Compared with single-answer search, the target requires a broader discovery set. This missing predecessor helps contextualize later claim, citation, and dependency-checklist evaluations such as ClaimProbe and Mr.LHDR; adding one historical record does not establish a new field trend.'],
 'protocol':[
  '任务给出查询与输出结构，参考主张用于 precision、recall 和 F1 评测；代码按类别分发评分器，默认 judge 为 GPT-4o。已核对的 evaluate.py 将缺失预测记为零，overall 对逐题指标平均，而不是把八个类别均值再等权平均。数据仅供测试，参考答案的加密措施不能被当成彻底防污染。[实际评分代码](https://github.com/microsoft/LiveDRBench/blob/main/src/evaluate.py)',
  'Tasks specify a query and output structure; reference claims support precision, recall, and F1 evaluation. Code dispatches category-specific graders with GPT-4o as the default judge. The reviewed evaluate.py assigns zero to missing predictions and computes overall metrics by averaging question-level results, not by equally averaging eight category means. The release is test-only; encrypting references should not be mistaken for complete contamination protection. [Scoring implementation](https://github.com/microsoft/LiveDRBench/blob/main/src/evaluate.py)'],
 'evidence':[
  '论文报告当时最强系统 overall F1 为 0.55，并显示子类别跨度很大。这是初始实验中的系统级结果，不是 2026 年当前最佳成绩。可复用增量在于把覆盖不全暴露出来，而不是证明更长报告或更多搜索调用一定有效。[论文](https://arxiv.org/abs/2508.04183)',
  'The paper reports an overall F1 of 0.55 for the strongest system in its original experiment, with substantial variation across subcategories. This is a historical system-level result, not a current-best claim for 2026. The reusable contribution is exposing incomplete discovery, not proving that longer reports or more search calls necessarily help. [Paper](https://arxiv.org/abs/2508.04183)'],
 'gap':[
  '参考集合可能遗漏其他有效来源，网页会变化，judge 和输出解析也会影响分数。领域集中于部分科学主题与事件，不能代表所有研究工作；高 claim F1 也不等于报告结构、论证或表达优秀。',
  'Reference sets can omit alternative valid evidence, the web drifts, and judges and output parsing affect scores. Coverage is concentrated in selected scientific and event domains, not all research work. High claim F1 also does not establish good report structure, argumentation, or prose.'],
 'use':['适合评测广度搜索与证据覆盖，并给报告质量评测配一个相对独立的内容发现指标。','Use it to evaluate search breadth and evidence coverage alongside a separate report-quality assessment.'],
 'example':['示意：寻找同时满足若干实验条件的材料，需要发现一组候选和各自证据；只找到一个熟悉案例或写出流畅综述都不等于覆盖完整。','Illustrative task: identify materials satisfying several experimental conditions, together with supporting evidence. Finding one familiar case or writing a fluent survey does not establish complete coverage.'],
 'experiment':['固定模型、网页快照和搜索预算，比较单链搜索与多分支探索；保留未完成题并按逐题规则聚合，另外人工核验参考集合外的有效发现。随后单独评估报告，不让文风掩盖证据漏项。','Fix the model, evidence snapshot, and search budget; compare single-chain search with branching exploration. Retain unfinished tasks, aggregate per question, and independently validate correct discoveries outside the references. Score the report separately so prose quality cannot hide missing evidence.'],
 'pair':['deepresearch-bench','claimprobe','mr-lhdr']
}
}

HEADINGS = [
 ('measure','它在测什么','What it measures'),
 ('delta','相比什么前进了','Compared with what'),
 ('protocol','实际怎样评测','Evaluation protocol'),
 ('evidence','决定性证据与分数边界','Decisive evidence and score boundary'),
 ('gap','主要混杂与尚未覆盖的能力','Confounders and remaining coverage gaps')
]

def note(record, lang):
    ident = record['id']; obj = TEXT[ident]; j = 0 if lang == 'zh' else 1
    ext = '' if lang == 'zh' else '.en'
    switch = f'**中文** | [English]({ident}.en.md)' if j == 0 else f'[中文]({ident}.md) | **English**'
    top = f'# {record["name"]}：{obj["title"][j]}' if j == 0 else f'# {record["name"]}: {obj["title"][j]}'
    pieces = [top, f'{switch} · [{"返回入口" if j == 0 else "Home"}](../README{ext}.md) · [Benchmark Library](../library/README{ext}.md)']
    labels = {'paper':('论文','Paper'),'code':('代码','Code'),'data':('数据','Data'),'project':('项目','Project')}
    pieces.append(' · '.join(f'[{labels[k][j]}]({v})' for k,v in record['artifacts'].items() if k in labels))
    for key, zh, en in HEADINGS:
        pieces.extend(['## ' + (zh if j == 0 else en), obj[key][j]])
    pieces += ['<!-- RESEARCH-DECISION:START -->', '## ' + ('研究决策卡' if j == 0 else 'Research decision card')]
    for key, zh, en in [('use','什么时候值得用','When to use it'),('example','一个具体任务长什么样','What a concrete task looks like'),('experiment','最有判别力的实验','Most discriminating experiment')]:
        pieces.extend(['### ' + (zh if j == 0 else en),obj[key][j]])
    pieces.extend(['### ' + ('建议搭配' if j == 0 else 'Pair with'), ' · '.join(f'[{x}]({x}{ext}.md)' for x in obj['pair']), '<!-- RESEARCH-DECISION:END -->'])
    boundary = ('证据核验：' + AS_OF + '。本条依据论文元数据、官方协议及上述公开实现或数据说明；不把结构校验当作事实认证，也未独立复现实验。' if j == 0 else 'Evidence checked: ' + AS_OF + '. This note uses paper metadata and the official protocols, implementations, or dataset descriptions identified above. Structural validation is not factual certification, and experiments were not independently reproduced.')
    pieces.extend(['---', boundary])
    return '\n\n'.join(pieces)

records = load('data/benchmarks.json')
original = copy.deepcopy(records)
by_id = {r['id']:r for r in records}
assert len(by_id) == len(records), 'Duplicate canonical identities before update'
locales = load('data/locales/zh/benchmarks.json')
new_ids = {r['id'] for r in NEW}
accepted_time = next((r.get('radar_published_at') for r in records if r['id'] in new_ids and r.get('radar_published_at')), NOW)
for authored in NEW:
    r = copy.deepcopy(authored)
    ident = r['id']
    zsum = r.pop('zh_summary'); zdelta = r.pop('zh_delta')
    sources = r.pop('protocol_sources')
    blobs = r.pop('source_blob_shas',{})
    basis = r.pop('observation_basis','First retained timestamp for resolved canonical intake in this run; earlier unlogged search leads are not reconstructed.')
    first_seen = r.get('first_seen_at',INTAKE)
    prior = by_id.get(ident)
    if prior:
        assert prior['artifacts']['paper'] == r['artifacts']['paper'], 'Identity collision'
        first_seen = prior['first_seen_at']
    r.update(status='active', last_verified=AS_OF, first_seen_at=first_seen,
             radar_published_at=prior['radar_published_at'] if prior else accepted_time,
             time_provenance='native_v2', map_delta=r.get('map_delta','early_signal'),
             first_public_at=r['released'], publication_at=None, data_release_at=None)
    r['release_date_evidence'] = {'first_public_at':{'source':r['artifacts']['paper'],'precision':'day','kind':'preprint-initial-submission','verified_at':AS_OF,'status':'checked'}}
    r['review_evidence'] = {
        'checked_at':AS_OF,'evidence_level':'official-protocol-or-dataset-review',
        'protocol_sources':sources,'source_blob_shas':blobs,
        'paper_access':'Initial submission metadata and abstract checked. Acceptance relies on the linked official protocol/implementation or detailed dataset description; no paper-PDF review is claimed.',
        'observation_basis':basis,
        'score_ceiling':r['coverage_gap'],
        'next_control':TEXT[ident]['experiment'][1],
        'publication_type':'historical-backfill' if ident == 'livedrbench' else ('missed-release-backfill' if r['released'] < '2026-09-17' else 'recent-discovery')
    }
    r['citations'] = prior['citations'] if prior else {'count':None,'source':'semantic-scholar','updated_at':AS_OF,'status':'unmatched','note':'No verified Semantic Scholar count was obtained for this addition. Unknown is not zero; existing citation snapshots are retained.'}
    if prior:
        records[records.index(prior)] = r
    else:
        assert all(x.get('artifacts',{}).get('paper') != r['artifacts']['paper'] for x in records), 'Duplicate primary paper'
        records.append(r)
    by_id[ident] = r
    locales[ident] = {'summary':zsum}
    authored['_zh_delta'] = zdelta
    for lang in ['zh','en']:
        write(f'benchmarks/{ident}{".en" if lang == "en" else ""}.md',note(r,lang))

# A material existing-instrument audit, not a new benchmark or a new release date.
dab = by_id['data-agent-benchmark']
dab['last_verified'] = AS_OF
for confounder in ['benchmark-tuned-prompt','dataset-hints','dataset-macro-aggregation','validator-revision','missing-and-contaminated-trials']:
    if confounder not in dab['confounders']:
        dab['confounders'].append(confounder)
dab.setdefault('review_evidence',{})['protocol_audit'] = {
    'checked_at':AS_OF,
    'source':'https://github.com/ucbepic/DataAgentBench/blob/main/README.md',
    'source_blob_sha':'4551bce7c0614c3c6a544ed5d9cf68f4db0ed528',
    'aggregation':'Mean over datasets of per-dataset mean per-query pass rate; not best-of-five.',
    'known_validator_events':[{'date':'2026-06-12','detail':'Historical submissions rescored using current validators, including regenerated PATENTS ground truths.'},{'date':'2026-08-18','detail':'DEPS_DEV_V1 query 1 revised to accept any of 95 packages tied at fifth place; submission JSONs rescored.'}],
    'comparison_boundary':'Record tuned-prompt and hints flags, trials, missing/contaminated-run handling, and validator revision. Do not treat the historical paper score as current headroom.'
}
for lang in ['zh','en']:
    j = 0 if lang == 'zh' else 1; ext = '' if j == 0 else '.en'
    path = ROOT / f'benchmarks/data-agent-benchmark{ext}.md'
    text = path.read_text(encoding='utf-8')
    if j == 0:
        text = text.replace('论文报告最好的 frontier model Gemini-3-Pro pass@1 也只有 38%，说明即使 query 数不大，跨系统整合仍远未解决。','论文初始实验报告 Gemini-3-Pro 的 pass@1 为 38%；这是当时模型与协议下的历史结果，不是当前能力上限。')
    # Keep existing authored sections; add a bounded, explicitly dated protocol audit.
    start='<!-- PROTOCOL-AUDIT-20260923:START -->'; end='<!-- PROTOCOL-AUDIT-20260923:END -->'
    if start in text:
        text = re.sub(re.escape(start)+r'.*?'+re.escape(end),'',text,flags=re.S)
    audit_zh = '''## 2026-09-23 协议核验：先看分母、提示和评分版本

官方 Pass@1 是**先计算每题的重复运行通过率，再在数据集内平均，最后对数据集平均**，不是 5 次中成功一次就算成功。提交要求每题 5 次并提供轨迹；缺失、污染或无可验证推导的运行不能从分母中任意删除。[官方方法与提交规则](https://github.com/ucbepic/DataAgentBench/blob/main/README.md)

榜单明确分开 `Tuned prompt` 与 `Hints`。例如官方表中 2026-09-11 的 Permute EQ 记录为 0.9467，2026-09-08 的 Scout 为 0.9062；两者都标注专门调过提示、使用 hints、5 次运行。这里只记录带条件的来源快照，不把系统差异归因给单个模型，也不将其与旧论文的 38% 直接相减。

评分器也发生过实质修订：官方说明 2026-06-12 按更新的验证器及 PATENTS 标准答案重算旧提交；2026-08-18 又修正 DEPS_DEV_V1 第 1 题，接受第 5 名并列的 95 个 package，而不是只接受旧标准答案中的一个。**分数变化可以来自标签与验证器修正，而不是系统进步。** 应保存数据和验证器版本、完整逐题结果、提示与轨迹，才能公平比较。

这次更新保持 DAB 原有首发日期和引用快照不变。上述 2026-09-23 是本 Radar 的协议核验日期，不是新基准发布日期；未独立复跑官方提交。'''
    audit_en = '''## 2026-09-23 protocol audit: inspect denominators, hints, and validator versions

Official Pass@1 first averages repeated-run pass rates per query, then within each dataset, and finally across datasets. It is **not success on at least one of five attempts**. Submissions require five runs per query and execution traces; missing, contaminated, or unsupported runs must not simply disappear from the denominator. [Official methodology and submission rules](https://github.com/ucbepic/DataAgentBench/blob/main/README.md)

The leaderboard separates `Tuned prompt` and `Hints`. For example, the official table records Permute EQ at 0.9467 dated 2026-09-11 and Scout at 0.9062 dated 2026-09-08; both declare tuned prompts, hints, and five trials. These are conditional source snapshots, not isolated backbone effects, and should not be subtracted directly from the historical paper's 38% result.

Validators changed materially. The official methodology records a 2026-06-12 rescore with updated validators and regenerated PATENTS references. On 2026-08-18, DEPS_DEV_V1 query 1 was corrected to accept any of 95 packages tied at fifth place rather than one package in the old reference. **A changed score can reflect repaired labels or validators rather than improved systems.** Preserve database and validator versions, complete per-query outputs, prompts, and traces before comparing results.

This update preserves DAB's original release date and citation snapshot. The date 2026-09-23 identifies this Radar's protocol verification, not a new benchmark release. Official submissions were not independently rerun.'''
    audit = audit_zh if j == 0 else audit_en
    marker='<!-- RESEARCH-DECISION:START -->'
    addition=start+'\n\n'+audit+'\n\n'+end+'\n\n'
    text = text.replace(marker,addition+marker,1) if marker in text else text+'\n\n'+addition
    write(f'benchmarks/data-agent-benchmark{ext}.md',text)

# Replace the earlier partial-discovery note with routes to accepted evidence.
for lang in ['zh','en']:
    ext = '' if lang == 'zh' else '.en'
    text = (ROOT / f'benchmarks/locomo{ext}.md').read_text(encoding='utf-8')
    old_heading = '## 后续对照：对话中的记忆调用与任务完成' if lang == 'zh' else '## Follow-up comparisons: conversational memory use and task completion'
    if old_heading in text:
        begin = text.index(old_heading)
        finish = text.index('<!-- RESEARCH-DECISION:START -->',begin)
        replacement = ('## 后续对照：查询形式、记忆使用与行动结果\n\n[LoCoMo-Conv](locomo-conv.md) 固定历史与证据，改变查询的对话形式；[MemCalib](memcalib.md) 检查已给定记忆命题应该影响回答多少；[DolphinBench](dolphinbench.md) 在冻结记忆和逐题应用重置下测实际动作、成本与延迟。三者分别诊断检索入口、上下文使用与行动落地，不能把总分混成一个榜单。\n\n2026-09-23 已完成这些条目的官方协议或数据说明核验并正式入库。各自详情页说明代码和数据的可用边界；这不表示独立复现实验，也不把仅有项目说明的证据冒充论文全文审计。\n\n' if lang == 'zh' else '## Follow-up comparisons: query form, memory use, and action outcomes\n\n[LoCoMo-Conv](locomo-conv.en.md) changes conversational query form while retaining history and evidence. [MemCalib](memcalib.en.md) tests how strongly supplied propositions should influence a response. [DolphinBench](dolphinbench.en.md) tests actions, cost, and latency with frozen memory and per-test app resets. These diagnose retrieval input, context use, and action outcomes respectively; their aggregate scores are not one interchangeable ranking.\n\nOn 2026-09-23 these instruments were accepted after review of their official protocols or detailed dataset descriptions. Their notes specify code and data availability. Acceptance does not claim independent reproduction or mislabel a project-description review as a paper full-text audit.\n\n')
        text = text[:begin]+replacement+text[finish:]
        write(f'benchmarks/locomo{ext}.md',text)

# Preserve all original records exactly except the explicitly audited DAB record.
for old in original:
    if old['id'] not in new_ids and old['id'] != 'data-agent-benchmark':
        assert by_id[old['id']] == old, 'Unexpected legacy mutation: '+old['id']
assert len(records) == 146, f'Unexpected membership change: {len(records)}'
assert set(by_id) == {r['id'] for r in records}
dump('data/benchmarks.json',records)
dump('data/locales/zh/benchmarks.json',locales)
fresh = load('data/freshness.json')
fresh.update(discovery_scan_at=AS_OF,
    sources=['arXiv initial-submission metadata and benchmark discovery searches','official benchmark protocols, implementation files and dataset descriptions','bounded predecessor and missed-release backfill','official leaderboard methodology and validator corrections'],
    note='Discovery scanned across Agent Memory, RAG / Agentic Retrieval, and Data Agents through 2026-09-23 (UTC+8). This is a bounded review, not an exhaustive census. Intermittent paper access was supplemented by official protocol, implementation, or detailed dataset evidence; unverified candidates are not published. Existing citation and structured-result snapshots remain unchanged; DAB protocol verification is recorded separately.')
dump('data/freshness.json',fresh)

# Retain existing bilingual Library prose and all original rows; insert new rows in canonical order.
new_authored = {r['id']:r for r in NEW}
areas = {'agent-memory':'Agent Memory','rag':'RAG / Agentic Retrieval','data-agent':'Data Agents'}
roles = {'zh':{'precursor':'🌱 前身','foundation':'🧱 基石','transition':'↗ 过渡','frontier':'🔭 前沿'},'en':{'precursor':'🌱 Precursor','foundation':'🧱 Foundation','transition':'↗ Transition','frontier':'🔭 Frontier'}}
by_name = sorted(records,key=lambda r:(r['name'].casefold(),r['id']))
timeline = sorted(by_name,key=lambda r:r['released'],reverse=True)
for lang in ['zh','en']:
    ext = '' if lang == 'zh' else '.en'
    path = ROOT / f'library/README{ext}.md'
    text = path.read_text(encoding='utf-8')
    blocks = [('COMPLETE-TIMELINE',timeline)] + [('COMPLETE-MAP:'+area,sorted([r for r in records if r['area']==area],key=lambda r:(r['released'],r['name'].casefold(),r['id']))) for area in areas]
    for label,items in blocks:
        pattern = re.compile(r'(<!-- '+re.escape(label)+r':START -->)(.*?)(<!-- '+re.escape(label)+r':END -->)',re.S)
        match = pattern.search(text); assert match, label
        body = match.group(2)
        rows = {re.search(r'benchmark-id:([a-z0-9-]+)',line).group(1):line for line in body.splitlines() if 'benchmark-id:' in line}
        headers = [line for line in body.splitlines() if line.startswith('|') and 'benchmark-id:' not in line]
        assert len(headers) == 2, (label,headers)
        for r in items:
            if r['id'] in rows: continue
            authored = new_authored[r['id']]
            title = f'[{r["name"]}]({r["artifacts"]["paper"]}) <!-- benchmark-id:{r["id"]} -->'
            role = roles[lang][r['evolution_role']]
            delta = authored['_zh_delta'] if lang == 'zh' else r['measurement_strength']
            summary = locales[r['id']]['summary'] if lang == 'zh' else r['summary']
            if label == 'COMPLETE-TIMELINE':
                cells=[r['released'],title,areas[r['area']],role,delta]
            else:
                cells=[role,title,r['released'],summary,delta]
            assert all('|' not in v and '\n' not in v for v in cells)
            rows[r['id']]='| '+' | '.join(cells)+' |'
        replacement=match.group(1)+'\n\n'+'\n'.join(headers+[rows[r['id']] for r in items])+'\n\n'+match.group(3)
        text=text[:match.start()]+replacement+text[match.end():]
    write(f'library/README{ext}.md',text)

# Close W38 by acceptance time, never by the release dates of newly accepted work.
zone=timezone(timedelta(hours=8))
start=datetime(2026,9,14,tzinfo=zone); stop=datetime(2026,9,21,tzinfo=zone)
support=[]
for r in records:
    stamp=r.get('radar_published_at')
    if stamp:
        t=datetime.fromisoformat(stamp.replace('Z','+00:00'))
        if start <= t < stop: support.append(r)
assert support and all(r['id'] not in new_ids for r in support)
for lang in ['zh','en']:
    ext='' if lang == 'zh' else '.en'
    path=f'digests/weekly/2026-W38{ext}.md'
    if (ROOT/path).exists(): continue
    references=' · '.join(f'[{r["name"]}](../../benchmarks/{r["id"]}{ext}.md)' for r in sorted(support,key=lambda x:x['id']))
    if lang == 'zh':
        content=f'''# 2026-W38 Benchmark 周报

**周期：** 2026-09-14—2026-09-20（UTC+8）  
**合成时间：** {accepted_time}  
**时间依据：** `radar_published_at`，不是论文首发或维护时间。  
**可核验新增支撑：** {len(support)}；全部来自本周期内的已接受记录。

## 测量对象正在被拆细，不能据此混排系统成绩

本周期接受的 [Q2D-Web](../../benchmarks/q2d-web.md) 测智能体实际发出的检索查询，[OntologyBench](../../benchmarks/ontologybench.md) 测概念和关系约束的满足，[Mr.LHDR](../../benchmarks/mr-lhdr.md) 测依赖一致的中间结论覆盖。它们把检索入口、约束满足和研究过程拆成不同可测对象；相同的“检索”名称不代表分数可互换。这里确认的是测量对象差别，不从三篇不同协议推导统一的技术趋势。

**研究设计含义：** 先确定要隔离哪个阶段，再固定模型、上下文、接口与预算。最终答案改善不能自动证明检索器改善；清单分数也不能视作模型内部推理过程的直接观测。

## 领域语义进入协议，但泛化证据仍有限

[DI-Bench](../../benchmarks/di-bench-data-intelligence.md) 将业务规则如何用于计算纳入评测；[ICM-Bench](../../benchmarks/icm-bench.md) 则把跨片段人物关联和画像依据显式化。两者揭示了领域内的不同缺口，不构成同一方向的独立重复实验。新增基准的价值要回到任务与标签来源，而不是仅看题量或发布频率。

**置信度：** 对上述协议差别为中等；对长期领域趋势保持低置信度。没有新增跨基准统一排名，也没有据此改写持久能力地图。

## 本周期接受的支撑

{references}

9 月 23 日新接受的基准属于之后的周期，即使论文在本周或更早发布，也不倒填为本周接受成果。原始论文、代码和证据边界见各支撑条目；本周报不替代独立复现。

[English](2026-W38.en.md) · [返回周报目录](../README.md)
'''
    else:
        content=f'''# 2026-W38 Benchmark Digest

**Period:** 2026-09-14—2026-09-20 (UTC+8)  
**Synthesized at:** {accepted_time}  
**Timing basis:** `radar_published_at`, not paper release or maintenance time.  
**Verified newly accepted supports:** {len(support)}, all accepted inside this period.

## Separate measurement objects before comparing system scores

Accepted this week, [Q2D-Web](../../benchmarks/q2d-web.en.md) measures queries actually issued by agents, [OntologyBench](../../benchmarks/ontologybench.en.md) tests concept and relation constraints, and [Mr.LHDR](../../benchmarks/mr-lhdr.en.md) scores dependency-consistent intermediate conclusions. They expose different objects: retrieval input, constraint satisfaction, and research progress. A shared retrieval label does not make the scores interchangeable. These protocol differences do not establish one unified technical trend.

**Research-design implication:** choose the stage to isolate, then fix models, accessible context, interfaces, and budgets. Better final answers do not automatically establish a better retriever; checklist scores are not direct observations of hidden reasoning.

## Domain semantics enters the protocol, with limited generalization evidence

[DI-Bench](../../benchmarks/di-bench-data-intelligence.en.md) evaluates use of business rules in computation; [ICM-Bench](../../benchmarks/icm-bench.en.md) exposes cross-episode identity linking and evidence for profiles. They reveal different domain-specific gaps, not independent replications of one direction. Assess tasks and label provenance rather than inferring significance from sample counts or release frequency.

**Confidence:** medium for these protocol distinctions and low for durable landscape trends. No unified cross-benchmark ranking or durable map rewrite follows from this digest.

## Accepted supports in this period

{references}

Benchmarks accepted on September 23 belong to the later acceptance period even when their papers appeared this week or earlier. Each linked note provides primary resources and evidence boundaries. This digest does not replace independent reproduction.

[中文](2026-W38.md) · [Digest index](../README.md)
'''
    write(path,content)

# Synchronize stale maintenance prose with the already-established README-first contract.
write('digests/README.md','''# Research Compactions

Closed-period digests synthesize changes in evaluation objects, protocols, and validity, rather than concatenate paper summaries. The root README presents the rolling six-calendar-month release timeline and the complete three-area registry; editorial interpretation remains in linked notes and guides.

The Daily Agent is the boundary writer. The first successful run after Monday 00:00 in UTC+8 closes the preceding ISO week; the first successful run of a month closes the preceding month. Existing closed digests are immutable. Monthly synthesis re-reads canonical records and notes rather than summarizing weekly prose. No incomplete current period is presented as a closed digest.

Every digest states its inclusive dates, synthesis time, accepted supporting identities, confidence, and research-design implications. Membership follows `radar_published_at`, not a paper's earlier release date. Missing historical acceptance timestamps remain unknown. Candidate and blocked work stays private. Publication is atomic with canonical data and bilingual reader surfaces, not a separate daily run log.

## Published digests

- **2026-W38:** [中文](weekly/2026-W38.md) · [English](weekly/2026-W38.en.md)
- **2026-W37:** [中文](weekly/2026-W37.md) · [English](weekly/2026-W37.en.md)
- **2026-W36:** [中文](weekly/2026-W36.md) · [English](weekly/2026-W36.en.md)
- **2026-W35:** [中文](weekly/2026-W35.md) · [English](weekly/2026-W35.en.md)
- **2026-W34:** [中文](weekly/2026-W34.md) · [English](weekly/2026-W34.en.md)
- **2026-W33:** [中文](weekly/2026-W33.md) · [English](weekly/2026-W33.en.md)
- **2026-08:** [中文](monthly/2026-08.md) · [English](monthly/2026-08.en.md)
''')
pub=ROOT/'docs/README_PUBLICATION.md'
s=pub.read_text(encoding='utf-8').replace('All 131 current\nnotes remain available; the number is not a fixed inclusion limit.','All accepted benchmark\nnotes remain available; there is no fixed inclusion limit.')
write('docs/README_PUBLICATION.md',s)

# Validate membership, timestamp preservation, note existence, and monotonic scan locally.
assert all((ROOT/f'benchmarks/{r["id"]}.md').exists() and (ROOT/f'benchmarks/{r["id"]}.en.md').exists() for r in records)
assert all(by_id[x['id']]['citations']==x['citations'] for x in original if x['id'] not in new_ids)
for x in original:
    if x['id'] not in new_ids:
        assert by_id[x['id']]['released']==x['released']
        for field in ['published_at','first_seen_at','radar_published_at']:
            assert by_id[x['id']].get(field)==x.get(field)
print('Accepted additions:', ', '.join(r['id'] for r in NEW))
print('Canonical counts:', {a:sum(r['area']==a for r in records) for a in areas}, 'total',len(records))
print('Preserved existing identities, release/provenance timestamps, citation snapshots, and structured result files.')
print('Closed W38 supports:',len(support),', '.join(r['id'] for r in support))
print('Acceptance timestamp:',accepted_time)
