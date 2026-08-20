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

## 三个领域的 Benchmark 地图

### Agent Memory

**主干：** [Multi-Session Chat](https://aclanthology.org/2022.acl-long.356/) → [LoCoMo](https://aclanthology.org/2024.acl-long.747/) / [LongMemEval](https://arxiv.org/abs/2410.10813) → [MemoryAgentBench](https://arxiv.org/abs/2507.05257) → [Mem2ActBench](https://aclanthology.org/2026.acl-long.370/) / [LoCoMo-Plus](https://arxiv.org/abs/2602.10715)

**Frontier signal：** evaluation target 已经分裂成 write/update/forget、organization、multimodal fidelity、persistent user state、procedural knowledge 与 memory-guided action。

**当前最大缺口：** persistent environment 里的 longitudinal causality——匹配 cost/context budget、权限、不可逆 action，以及持续数周/数月的 state evolution。

[进入 Agent Memory 方法与系统 →](https://github.com/H20Zhang/Agent-Memory-Radar)

<details><summary><strong>展开更完整的 Memory genealogy</strong></summary>

`Multi-Session Chat → LoCoMo / LongMemEval → MemBench / MemoryAgentBench / BEAM → Mem-Gallery / MemEye / StructMemEval / LongMemEval-V2 → MemoryArena / Mem2ActBench / LoCoMo-Plus / RealMem`

完整 registry 与 role 见 [Benchmark Library](#library)。

</details>

### RAG / Agentic Retrieval

**主干：** [HotpotQA](https://aclanthology.org/D18-1259/) → [BEIR](https://arxiv.org/abs/2104.08663) → [BrowseComp](https://arxiv.org/abs/2504.12516) → [SGR-Bench](https://arxiv.org/abs/2605.22219) → [VAKRA](https://arxiv.org/abs/2608.12282)

**Frontier signal：** retrieval 从 document ranking 扩张为 information-environment control：source state、tool、stopping、cross-source execution 都进入评价对象。

**当前最大缺口：** 在 interface / harness / model / budget 匹配的情况下做 causal attribution，尤其是 live environment 会持续 drift 的 long-horizon setting。

[进入 Agentic RAG 方法与系统 →](https://github.com/H20Zhang/Agentic-RAG-Radar)

### Data Agents

**主干：** [WikiSQL](https://arxiv.org/abs/1709.00103) → [Spider](https://aclanthology.org/D18-1425/) / [DS-1000](https://arxiv.org/abs/2211.11501) → [AgenticDataBench](https://arxiv.org/abs/2607.01647) → [DataSpace](https://arxiv.org/abs/2608.03451) → [DSAgentBench](https://arxiv.org/abs/2608.10366)

**Frontier signal：** 评价对象正在从 query/code generation 变成完整 data work：heterogeneous discovery、tool orchestration、intermediate-state grounding、verification 与 artifact delivery。

**当前最大缺口：** 真实 enterprise semantics、business-definition ambiguity、long-running workflow state、deployment/monitoring、governance，以及“问题本身就定义不清楚”时的可靠 clarification / abstention。

[进入 Data Agent 方法与系统 →](https://github.com/H20Zhang/Data-Agent-Radar)

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

- **[按 area / genealogy / measurement coordinate / year 浏览](library/README.md)**
- [Canonical registry](data/benchmarks.json)
- [Research compactions](digests/README.md)

## About

Benchmark Radar 之所以适合作为整个 family 的入口，是因为 genealogy 能先给新人一个紧凑答案：**领域想提升什么能力、旧 target 为什么不够、现在什么 evidence 才算进步。** 然后再把读者送到 domain radar，而不是在这里重复方法综述。

[English](README.en.md) · [Curation](CURATION.md) · [Schema](SCHEMA.md)
