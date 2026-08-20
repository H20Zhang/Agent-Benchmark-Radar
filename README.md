# Agent Benchmark Radar

**中文** | [English](README.en.md)

**整个 Research Radar family 的默认入口，也是横向 evaluation layer。**

先从这里理解：**Agent Memory、Agentic RAG、Data Agent 分别正在被要求做什么，这些 evaluation target 为什么一路演化到今天，以及一个 benchmark score 到底能支持什么结论。** 然后再进入对应 domain radar 看方法与系统。

**研究 Radar：** [Agent Memory](https://github.com/H20Zhang/Agent-Memory-Radar) · [Agentic RAG](https://github.com/H20Zhang/Agentic-RAG-Radar) · [Data Agent](https://github.com/H20Zhang/Data-Agent-Radar)

[30 秒：前沿](#frontier) · [5 分钟：领域演化](#evolution) · [15 分钟：阅读路径](#reading-paths) · [浏览全部](#library)

> **核心想法：** 一个真正有用的新 benchmark，往往是在隐含地批评上一代：**旧 benchmark 到底太简单、太窄、太静态、太 synthetic、太 opaque，还是诊断能力太弱？**
>
> **比较规则：** 如果 model、accessible state、tool interface、prompt/hints、retry、stopping rule、evaluator 与关键 resource budget 没有充分匹配，那么 leaderboard 上更高的 score 首先只是 **system-level evidence**，不能直接归因给某个 component。

最后更新：**2026-08-20**

<a id="frontier"></a>
## 最新值得关注的 Benchmark

| Benchmark | Area | 新测到了什么 | 它说明领域开始关心什么 |
|---|---|---|---|
| [DSAgentBench](https://arxiv.org/abs/2608.10366) | Data Agent | **真实 computer environment** 里的端到端 data-science workflow | 评价对象从 code/answer quality 转向 grounded multi-tool work |
| [VAKRA](https://arxiv.org/abs/2608.12282) | RAG / Agents | API + retrieved documents + policy constraints 出现在同一 executable trajectory | Retrieval 正在变成 cross-source execution，而不只是 ranking |
| [DataSpace](https://arxiv.org/abs/2608.03451) | Data Agent | DB、file、document、multimedia 上的 verifiable analytics | heterogeneous evidence discovery 与 deterministic verification 必须一起看 |
| [LoCoMo-Plus](https://arxiv.org/abs/2602.10715) | Agent Memory | 后续 query 不重述条件时，仍要应用 latent user constraint | Memory 从 explicit recall 走向 persistent user state |
| [Mem2ActBench](https://aclanthology.org/2026.acl-long.370/) | Agent Memory | memory 是否真正影响 tool selection 与 parameter grounding | Memory 开始按**是否改变 action**评价，而不仅是能否回答 |
| [RealMem](https://aclanthology.org/2026.findings-acl.703/) | Agent Memory | 长时间、跨 session 的 project state 与 evolving goal | 长期 memory 从 casual dialogue 走向 persistent project work |
| [AgenticDataBench](https://arxiv.org/abs/2607.01647) | Data Agent | 细粒度 **data-science skill coverage** | aggregate success 不够，benchmark coverage 本身开始可审计 |
| [SGR-Bench](https://arxiv.org/abs/2605.22219) | RAG / Search | evidence 被 filter、hierarchy、scope、site state 挡住时如何 search | 找到 source 不等于正确配置 information environment |

<details><summary><strong>为什么 DSAgentBench 改变了 evaluation target</strong></summary>

过去很多 data-agent benchmark 把 SQL、code generation、analytics answer 或某个 workflow stage 分开测。DSAgentBench 把完整 data-science workflow 放进真实 computer environment，agent 需要协调多种工具，并依据 intermediate outputs 做后续决策。

Benchmark 包含 **275 个任务**，用 deterministic evaluator 检查 analytical correctness、visual outputs 与 model performance。论文报告最强 agent 的 task success 为 **56.70%**，所有 open-source agents 低于 1%。但这里 model、harness、tool reliability、OS grounding 与 long-horizon reasoning 同时变化，所以结论首先是 system-level。它真正改变的是 **environment + protocol**，而不是谁排第一。

</details>

<details><summary><strong>为什么 DataSpace 不只是又一个 analytics dataset</strong></summary>

DataSpace 只给 agent 一个问题和一个 task-local heterogeneous workspace，其中可能混合 CSV、JSON、SQLite、Markdown、PDF、video；最终必须输出完整 tabular result。它把 **evidence discovery、cross-source join、multimodal access、deterministic answer verification** 放到同一个任务里。

它包含 **410 个任务、7,439 个 artifacts**。论文还报告：固定 backbone 时，仅 harness 选择就造成 **15.36 points** 的差距。这本身就是重要的 validity warning——data-agent score 对 harness 很敏感。DataSpace 扩大了可测对象，但仍不能把 system-level gain 干净归因给某个 controller 或 retrieval component。

</details>

<details><summary><strong>为什么 LoCoMo-Plus 超出了 factual recall</strong></summary>

传统 long-term-memory QA 往往让后续问题和旧事实有直接 lexical/semantic cue。LoCoMo-Plus 测的是 **cue–trigger semantic disconnect**：之后的 query 没有重新说出旧约束，但 agent 仍应记住并正确应用 latent user constraint。

评价对象因此从“能否找回旧事实”变成“remembered user state 是否正确约束未来行为”。接下来更难的问题是：这种 constraint-consistency evaluation 能否迁移到真实 persistent acting agent，其中 preference 会 drift、权限会变化、action 可能不可逆。

</details>

<details><summary><strong>为什么 VAKRA 改变了 RAG evaluation</strong></summary>

VAKRA 把 executable API call、document retrieval、multi-hop reasoning 与 tool-use policy 放在同一条 trajectory 中。这样能暴露 API benchmark 或 document QA 分开测时看不到的 failure：identity mismatch、cross-source grounding failure、policy-inconsistent execution。

它支持的是 trajectory-level system claim，而不是某个 retrieval policy 的 clean attribution。它真正新增的 measurement coordinate 是 **cross-source executable coherence**。

</details>

<a id="evolution"></a>
## Benchmark 演化告诉我们：领域正在把什么当成“进步”

| Area | 演化 | 现在越来越关心什么 | 继续深入 |
|---|---|---|---|
| **Agent Memory** | multi-session recall → time/update/forget → structure/scale/multimodality → **implicit user state + memory-guided action** | 什么该写、更新、推断、遗忘，并真正改变未来行为？ | [Agent Memory Radar](https://github.com/H20Zhang/Agent-Memory-Radar) |
| **RAG / Agentic Retrieval** | retrieval quality → robustness/faithfulness → deep research → **stateful, controlled, cross-source execution** | Agent 能否在变化的 state、tool 与 budget 下控制整个 information environment？ | [Agentic RAG Radar](https://github.com/H20Zhang/Agentic-RAG-Radar) |
| **Data Agents** | NL→SQL/code → experimentation/workflows → heterogeneous analytics → **real-computer end-to-end data work** | Agent 能否 discover、transform、analyze、verify、recover 并交付真正可用的 artifact？ | [Data Agent Radar](https://github.com/H20Zhang/Data-Agent-Radar) |

## 三个领域的完整 Benchmark 时间线

按时间从早到晚读：每一行都在回答“上一代还没测好什么”。当前 registry 的 benchmark 全部列出，不做代表性截断。

### Agent Memory

**演化主线：** Multi-Session Chat → LoCoMo / LongMemEval → MemBench / MemoryAgentBench / BEAM → multimodal / agent-experience memory → MemoryArena / Mem2ActBench / LoCoMo-Plus / RealMem

<!-- COMPLETE-MAP:agent-memory:START -->
| 角色 | Benchmark | 时间 | 实际测什么 | 为什么改变了问题 |
|---|---|---:|---|---|
| 🌱 前身 | [Beyond Goldfish Memory](https://aclanthology.org/2022.acl-long.356/) <!-- benchmark-id:beyond-goldfish-memory --> | 2022-05 | 跨多个真人聊天 session 的开放域长期对话记忆与前后自洽。 | 将跨 session 对话连续性确立为现代 memory-agent benchmark 之前的独立评价对象。 |
| 🧱 基石 | [LoCoMo](https://aclanthology.org/2024.acl-long.747/) <!-- benchmark-id:locomo --> | 2024-08 | 超长多 session 对话中的 QA、事件总结与多模态对话生成。 | 相比 Beyond Goldfish Memory，把超长对话记忆固化为可复用的多任务评价坐标。 |
| 🧱 基石 | [LongMemEval](https://arxiv.org/abs/2410.10813) <!-- benchmark-id:longmemeval --> | 2024-10 | 长期助手历史中的抽取、跨 session 推理、时间推理、知识更新与拒答。 | 相比 LoCoMo，将更新、时间推理和拒答从一般 recall 中明确拆分出来。 |
| ↗ 过渡 | [MemBench](https://arxiv.org/abs/2506.21605) <!-- benchmark-id:membench --> | 2025-06 | factual/reflective memory、参与/观察场景，以及效果、效率和容量。 | 相比 LoCoMo 与 LongMemEval，从答题准确率扩展到记忆层次、交互角色和资源表现。 |
| ↗ 过渡 | [MemoryAgentBench](https://arxiv.org/abs/2507.05257) <!-- benchmark-id:memoryagentbench --> | 2025-07 | 增量多轮交互中的检索、test-time learning、长程理解与选择性遗忘。 | 相比 LongMemEval 与 MemBench，把 memory 从静态历史读出改为持续吸收、更新、使用和遗忘的在线过程。 |
| ↗ 过渡 | [BEAM](https://arxiv.org/abs/2510.27246) <!-- benchmark-id:beam --> | 2025-10 | 从百万到千万 token 的连贯对话长期记忆。 | 相比 LoCoMo，直接暴露超大规模连贯历史下的 memory degradation。 |
| 🔭 前沿 | [RealMem](https://aclanthology.org/2026.findings-acl.703/) <!-- benchmark-id:realmem --> | 2026-01 | 跨 session、目标和 artifact 持续变化的项目型长期记忆。 | 相比 LoCoMo，把评价对象从一般对话历史推进到 persistent project state 与 evolving goals。 |
| 🔭 前沿 | [AMA-Bench](https://arxiv.org/abs/2602.22769) <!-- benchmark-id:ama-bench --> | 2026-02 | 真实与可扩展合成 agent-environment trajectory 上的长程记忆。 | 相比 MemoryAgentBench，把记忆来源从对话交互扩展到具有因果结构的 agent-environment experience。 |
| 🔭 前沿 | [StructMemEval](https://arxiv.org/abs/2602.11243) <!-- benchmark-id:structmemeval --> | 2026-02 | Agent 是否维护 ledger、list、tree 等适合任务的 memory structure。 | 相比 MemoryAgentBench，使 memory 的组织方式本身成为可观察能力。 |
| 🔭 前沿 | [MemoryArena](https://arxiv.org/abs/2602.16313) <!-- benchmark-id:memoryarena --> | 2026-02-18 | 多 session Agent-Environment loop 中，早期行动与反馈是否指导后续行动。 | 相比 MemoryAgentBench，直接把长期记忆与未来 task action 耦合起来。 |
| 🔭 前沿 | [LifeBench](https://arxiv.org/abs/2603.03781) <!-- benchmark-id:lifebench --> | 2026-03 | 跨多源长期轨迹的 episodic、semantic、habit 与 procedural memory。 | 相比 LoCoMo 和 LongMemEval，把评价对象从显式事实扩展到习惯与程序性知识。 |
| 🔭 前沿 | [LongMemEval-V2](https://arxiv.org/abs/2605.12493) <!-- benchmark-id:longmemeval-v2 --> | 2026-05 | 大规模 web-agent trajectory 中的环境状态、workflow knowledge 与 gotcha。 | 结合 LongMemEval 与 AMA-Bench，把累积环境经验而非仅用户历史设为 memory target。 |
| 🔭 前沿 | [MemEye](https://arxiv.org/abs/2605.15128) <!-- benchmark-id:memeye --> | 2026-05-14 | 细粒度视觉证据记忆、视觉状态演化与 text-only shortcut 检查。 | 相比 LoCoMo，要求系统保留真正必要的视觉证据，而不能只依赖 caption 或文本线索。 |
| 🔭 前沿 | [LifeSide](https://arxiv.org/abs/2606.04660) <!-- benchmark-id:lifeside --> | 2026-06 | 多 session memory、用户理解、隐私控制和情绪—环境动态。 | 相比 LoCoMo 与 LifeBench，把 memory 与 persistent user model、privacy boundary 和环境情境联结起来。 |
| 🔭 前沿 | [LoCoMo-Plus](https://aclanthology.org/2026.acl-long.1150/) <!-- benchmark-id:locomo-plus --> | 2026-07 | 后续 cue 不重述条件时，仍能保留并应用 latent user constraints。 | 相比 LoCoMo，把目标从显式事实 recall 推进到对用户目标、价值和约束的一致应用。 |
| 🔭 前沿 | [Mem-Gallery](https://aclanthology.org/2026.acl-long.1892/) <!-- benchmark-id:mem-gallery --> | 2026-07 | 多模态长期对话中的 memory extraction、适应、推理与知识管理。 | 结合 LoCoMo 与 MemEye，使视觉保留、多模态推理和 memory organization 成为统一评价对象。 |
| 🔭 前沿 | [Mem2ActBench](https://aclanthology.org/2026.acl-long.370/) <!-- benchmark-id:mem2actbench --> | 2026-07 | 长期 memory 是否主动决定 tool selection 并为参数提供 grounding。 | 相比 MemoryAgentBench 与 MemoryArena，使 action-level memory utilization 可以直接评分。 |
<!-- COMPLETE-MAP:agent-memory:END -->

**前沿信号：** write/update/forget、organization、multimodal fidelity、persistent user state 与 memory-guided action 正在成为分开的评价对象。

**最大缺口：** 真正 persistent environment 里的 longitudinal causality：匹配 cost/context budget、权限、不可逆 action 与数周/数月的 state evolution。

[Agent Memory 方法与系统 →](https://github.com/H20Zhang/Agent-Memory-Radar)

### RAG / Agentic Retrieval

**演化主线：** HotpotQA / KILT / BEIR → RGB / RAGTruth / CRAG / BRIGHT → BrowseComp / DeepResearch Bench → SGR-Bench / AgenticRAGTracer / VAKRA

<!-- COMPLETE-MAP:rag:START -->
| 角色 | Benchmark | 时间 | 实际测什么 | 为什么改变了问题 |
|---|---|---:|---|---|
| 🌱 前身 | [HotpotQA](https://aclanthology.org/D18-1259/) <!-- benchmark-id:hotpotqa --> | 2018-10 | 跨多个 Wikipedia 文档的 evidence retrieval、组合推理与 supporting facts。 | 将多文档证据组合和可解释 supporting facts 确立为可测的 retrieval-reasoning 目标。 |
| 🧱 基石 | [KILT](https://arxiv.org/abs/2009.02252) <!-- benchmark-id:kilt --> | 2020-09 | 同一 Wikipedia snapshot 上的多种知识密集任务、任务质量与 provenance。 | 相比 HotpotQA，把正确性与证据来源放进共享、可复用的评价基础设施。 |
| 🧱 基石 | [BEIR](https://arxiv.org/abs/2104.08663) <!-- benchmark-id:beir --> | 2021-04 | 异构领域与任务上的 zero-shot retrieval generalization。 | 不再以单一 IR dataset 的最优结果代表 retriever robustness，而是直接测跨域泛化。 |
| 🧱 基石 | [RGB](https://arxiv.org/abs/2309.01431) <!-- benchmark-id:rgb --> | 2023-09 | RAG 的噪声鲁棒性、负例拒绝、信息整合与反事实鲁棒性。 | 相比 KILT，把“是否正确使用 retrieved context”拆成多个独立能力。 |
| ↗ 过渡 | [MultiHop-RAG](https://arxiv.org/abs/2401.15391) <!-- benchmark-id:multihop-rag --> | 2024-01 | RAG pipeline 中跨多份 supporting evidence 的检索与推理。 | 结合 HotpotQA 与 RGB，使 multi-hop retrieval failure 在 RAG pipeline 内部可见。 |
| ↗ 过渡 | [RAGTruth](https://arxiv.org/abs/2401.00396) <!-- benchmark-id:ragtruth --> | 2024-01 | RAG 输出中 case-level 与 word-level hallucination 和 grounding failure。 | 相比 RGB，把 faithfulness failure 从整体答案标签细化到局部文本跨度。 |
| ↗ 过渡 | [CRAG](https://arxiv.org/abs/2406.04744) <!-- benchmark-id:crag --> | 2024-06 | dynamic facts、long-tail entity、web 与 knowledge-graph retrieval 上的 factual RAG。 | 相比 KILT 与 RGB，把 freshness、事实动态性和长尾知识带入 RAG 评价。 |
| ↗ 过渡 | [BRIGHT](https://arxiv.org/abs/2407.12883) <!-- benchmark-id:bright --> | 2024-07 | relevance 判断本身需要显著推理的真实查询检索。 | 相比 BEIR，暴露 semantic similarity 无法覆盖的 reasoning-intensive retrieval。 |
| ↗ 过渡 | [RAGBench](https://arxiv.org/abs/2407.11005) <!-- benchmark-id:ragbench --> | 2024-07 | 跨行业领域的 retrieval/generation 质量标签与 RAG evaluator。 | 相比 RGB 与 RAGTruth，把 evaluator 质量和可行动 failure label 本身变成 benchmark 问题。 |
| ↗ 过渡 | [BrowseComp](https://arxiv.org/abs/2504.12516) <!-- benchmark-id:browsecomp --> | 2025-04 | 为寻找隐蔽答案而持续浏览 live web、改写 query 与导航。 | 相比 BEIR 与 CRAG，把评价对象从一次 retrieval 推进到 persistent information seeking。 |
| ↗ 过渡 | [DeepResearch Bench](https://arxiv.org/abs/2506.11763) <!-- benchmark-id:deepresearch-bench --> | 2025-06 | 多步 web research、证据收集、citation quality 与长篇报告生成。 | 相比 BrowseComp，把目标从找到短答案提升到生成 analyst-style research artifact。 |
| ↗ 过渡 | [BrowseComp-Plus](https://arxiv.org/abs/2508.06600) <!-- benchmark-id:browsecomp-plus --> | 2025-08 | 固定语料上的 deep research、retriever attribution 与 answer accuracy。 | 相比 BrowseComp，用固定 verified corpus 降低 live-search 黑盒带来的公平性和复现问题。 |
| 🔭 前沿 | [RAGCap-Bench](https://arxiv.org/abs/2510.13910) <!-- benchmark-id:ragcap-bench --> | 2025-10 | Agentic RAG workflow 内的 planning、retrieval 与 intermediate reasoning 能力。 | 相比 MultiHop-RAG 与 BrowseComp-Plus，使中间能力可独立诊断，而不只看最终答案。 |
| 🔭 前沿 | [AgenticRAGTracer](https://arxiv.org/abs/2602.19127) <!-- benchmark-id:agenticragtracer --> | 2026-02 | 多步 retrieval-reasoning chain 的 hop-level validation 与 step allocation。 | 相比 MultiHop-RAG 与 RAGCap-Bench，使 failure location 在 trajectory 内可见。 |
| 🔭 前沿 | [SGR-Bench](https://arxiv.org/abs/2605.22219) <!-- benchmark-id:sgr-bench --> | 2026-05 | evidence 受 site filter、hierarchy、scope 或 view state 控制时的 search。 | 相比 BrowseComp 与 CRAG，区分找到正确 source 与配置正确 retrieval state。 |
| 🔭 前沿 | [VAKRA](https://arxiv.org/abs/2608.12282) <!-- benchmark-id:vakra --> | 2026-08 | executable API、document retrieval、multi-hop reasoning 与 tool-use policy 的组合执行。 | 结合 SGR-Bench 与 AgenticRAGTracer，把跨 source grounding、执行和 policy consistency 放进同一 trajectory。 |
<!-- COMPLETE-MAP:rag:END -->

**前沿信号：** retrieval 正从 document ranking 扩张为 information-environment control，source state、tool、stopping 与 cross-source execution 都进入评价对象。

**最大缺口：** 在 interface、harness、model 与 budget 匹配时做 causal attribution，尤其是持续 drift 的 live environment。

[Agentic RAG 方法与系统 →](https://github.com/H20Zhang/Agentic-RAG-Radar)

### Data Agents

**演化主线：** WikiSQL / Spider / DS-1000 → BIRD / MLAgentBench / InsightBench / Spider 2.0 → DataSciBench / DAComp / DAB → DataSpace / DSAgentBench

<!-- COMPLETE-MAP:data-agent:START -->
| 角色 | Benchmark | 时间 | 实际测什么 | 为什么改变了问题 |
|---|---|---:|---|---|
| 🌱 前身 | [WikiSQL](https://arxiv.org/abs/1709.00103) <!-- benchmark-id:wikisql --> | 2017-08 | 单个 Wikipedia table 上从自然语言生成可执行 SQL。 | 将大规模、可执行的自然语言数据库访问确立为 benchmarkable task。 |
| 🧱 基石 | [Spider](https://aclanthology.org/D18-1425/) <!-- benchmark-id:spider --> | 2018-10 | 未见 schema 上的复杂 multi-table SQL 与跨域泛化。 | 相比 WikiSQL，把 text-to-SQL 从单表生成推进到复杂查询和 cross-schema generalization。 |
| 🧱 基石 | [DS-1000](https://arxiv.org/abs/2211.11501) <!-- benchmark-id:ds-1000 --> | 2022-11 | 七类 Python data-science library 上的代码生成与 execution-grounded correctness。 | 在 SQL lineage 之外，建立了可复现的实用 data-science code 执行评价。 |
| ↗ 过渡 | [BIRD](https://arxiv.org/abs/2305.03111) <!-- benchmark-id:bird --> | 2023-05 | 大型真实数据库中的脏值、外部知识、复杂 SQL 与执行效率。 | 相比 Spider，把 text-to-SQL 推进到 value-rich、messy database，并使 SQL efficiency 可见。 |
| ↗ 过渡 | [MLAgentBench](https://arxiv.org/abs/2310.03302) <!-- benchmark-id:mlagentbench --> | 2023-10 | Agent 迭代设计、运行、检查并改进 machine-learning experiment。 | 相比 DS-1000，把一次代码生成改成由执行反馈驱动的科学实验过程。 |
| ↗ 过渡 | [InsightBench](https://arxiv.org/abs/2407.06423) <!-- benchmark-id:insightbench --> | 2024-07 | 从问题形成、exploratory analysis 到 insight 和行动建议的 business analytics。 | 相比 DS-1000 与 MLAgentBench，把目标从完成给定代码任务扩展到发现并沟通有用分析。 |
| ↗ 过渡 | [DA-Code](https://aclanthology.org/2024.emnlp-main.748/) <!-- benchmark-id:da-code --> | 2024-10 | 真实数据上的 data wrangling、EDA、ML planning 与 grounded executable code。 | 相比 DS-1000 与 MLAgentBench，在静态代码题和 agent-style data work 之间建立可执行桥梁。 |
| ↗ 过渡 | [Spider 2.0](https://arxiv.org/abs/2411.07763) <!-- benchmark-id:spider-2 --> | 2024-11 | 巨大 schema、多 SQL dialect、metadata、codebase 与 cloud DB 中的企业 SQL workflow。 | 相比 Spider 与 BIRD，把 one-shot semantic parsing 变成长程 enterprise workflow。 |
| ↗ 过渡 | [DataSciBench](https://arxiv.org/abs/2502.13897) <!-- benchmark-id:datascibench --> | 2025-02 | 异构 data-science prompt、task-specific programmatic metric 与人工核验 ground truth。 | 相比 DA-Code 与 MLAgentBench，扩大任务覆盖并为不同分析目标使用专门 evaluator。 |
| 🔭 前沿 | [FDABench](https://arxiv.org/abs/2509.02473) <!-- benchmark-id:fdabench --> | 2025-09 | structured、unstructured、web 和 multimodal source 上的多源分析 workflow。 | 相比 DataSciBench 与 InsightBench，把异构分析、reasoning trace、latency 和 token cost 一起暴露。 |
| 🔭 前沿 | [DAComp](https://arxiv.org/abs/2512.04324) <!-- benchmark-id:dacomp --> | 2025-12 | repository-level data engineering 与 open-ended data analysis。 | 结合 Spider 2.0 与 InsightBench，覆盖 data engineering 和 analysis 的更完整 lifecycle。 |
| 🔭 前沿 | [Data Agent Benchmark (DAB)](https://arxiv.org/abs/2603.20576) <!-- benchmark-id:data-agent-benchmark --> | 2026-03 | 多种 DBMS 间的数据 integration、transformation、analysis 与 executable validation。 | 相比 Spider 2.0，把企业数据问题从单一 SQL workflow 扩展到跨数据库完整 pipeline。 |
| 🔭 前沿 | [AgenticDataBench](https://arxiv.org/abs/2607.01647) <!-- benchmark-id:agenticdatabench --> | 2026-07 | 真实 data-science workflow 中的细粒度 skill taxonomy 与组合覆盖。 | 相比 DataSciBench，使 benchmark 的 skill coverage 本身可以审计。 |
| 🔭 前沿 | [DataSpace](https://arxiv.org/abs/2608.03451) <!-- benchmark-id:dataspace --> | 2026-08 | DB、file、document 与 multimedia 混合 workspace 上的 verifiable analytics。 | 结合 FDABench 与 DAB，把 heterogeneous evidence discovery 与 deterministic complete-result checking 统一起来。 |
| 🔭 前沿 | [DSAgentBench](https://arxiv.org/abs/2608.10366) <!-- benchmark-id:dsagentbench --> | 2026-08 | notebook、IDE、terminal、browser 与 DB 中的完整 data-science workflow。 | 结合 MLAgentBench 与 DAComp，把评价放进真实 computer environment，并要求 grounded multi-stage tool execution。 |
<!-- COMPLETE-MAP:data-agent:END -->

**前沿信号：** 评价对象正从 query/code generation 变成完整 data work：heterogeneous discovery、tool orchestration、verification 与 artifact delivery。

**最大缺口：** 真实 enterprise semantics、business-definition ambiguity、long-running workflow state、governance 与可靠 clarification/abstention。

[Data Agent 方法与系统 →](https://github.com/H20Zhang/Data-Agent-Radar)

## 目前仍然测不好的重要问题

**Benchmark coverage 不等于这个领域。** 有些问题在出现干净 benchmark 之前，就已经值得研究。

| 缺失 measurement coordinate | 为什么会改变研究结论 |
|---|---|
| **真实用户的长期效应** | preference drift、project evolution、delayed consequence 很难压成静态 QA。 |
| **不可逆 action + authority** | tool 可以花钱、改 state、使用过期权限时，“检索正确”远远不够。 |
| **Lifecycle cost** | construction/indexing/memory-writing、retry、controller calls、tool latency、re-acquisition 经常被拆开或省略。 |
| **生产环境 drift 下的 reliability** | web、schema、tool、environment 的变化可能主导结果，即使 model 没变。 |
| **Business-semantic correctness** | SQL/code 可执行仍可能返回错误 business meaning；clarification 与 abstention 也经常没有干净评价目标。 |

<a id="reading-paths"></a>
## 阅读路径

| 你想理解什么 | 从这里开始 | 然后进入 |
|---|---|---|
| **Memory 怎么从 recall 走到 action？** | Multi-Session Chat → LoCoMo → LongMemEval → MemoryArena / Mem2ActBench / LoCoMo-Plus | [Agent Memory Radar](https://github.com/H20Zhang/Agent-Memory-Radar) |
| **Retrieval 怎么变成 stateful control problem？** | HotpotQA / BEIR → BrowseComp → SGR-Bench → VAKRA | [Agentic RAG Radar](https://github.com/H20Zhang/Agentic-RAG-Radar) |
| **Data Agent 怎么从 SQL/code 走到真实 workspace？** | WikiSQL / Spider / DS-1000 → AgenticDataBench → DataSpace → DSAgentBench | [Data Agent Radar](https://github.com/H20Zhang/Data-Agent-Radar) |

<a id="library"></a>
## Benchmark Library

- **[按时间 / 领域 / genealogy / measurement coordinate 浏览](library/README.md)**
- [Canonical registry](data/benchmarks.json)
- [Research compactions](digests/README.md)

## About

Benchmark Radar 之所以适合作为整个 family 的入口，是因为 genealogy 能先给新人一个紧凑答案：**领域想提升什么能力、旧 target 为什么不够、现在什么 evidence 才算进步。** 然后再把读者送到 domain radar，而不是在这里重复方法综述。

[English](README.en.md) · [Curation](CURATION.md) · [Schema](SCHEMA.md)
