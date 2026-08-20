# Agent Benchmark Radar

**中文** | [English](README.en.md)

**整个 Research Radar family 的默认入口，也是横向 evaluation layer。**

先从这里理解：**Agent Memory、Agentic RAG、Data Agent 分别正在被要求做什么，这些 evaluation target 为什么一路演化到今天，以及一个 benchmark score 到底能支持什么结论。** 然后再进入对应 domain radar 看方法与系统。

**研究 Radar：** [Agent Memory](https://github.com/H20Zhang/Agent-Memory-Radar#field-map) · [Agentic RAG](https://github.com/H20Zhang/Agentic-RAG-Radar#field-map) · [Data Agent](https://github.com/H20Zhang/Data-Agent-Radar#field-map)

[30 秒：最新时间线](#timeline) · [3 分钟：7/30 天变化](#periods) · [5 分钟：领域地图](#field-map) · [15 分钟：阅读路径](#reading-paths) · [浏览全部](#library)

> **核心想法：** 一个真正有用的新 benchmark，往往是在隐含地批评上一代：**旧 benchmark 到底太简单、太窄、太静态、太 synthetic、太 opaque，还是诊断能力太弱？**
>
> **比较规则：** 如果 model、accessible state、tool interface、prompt/hints、retry、stopping rule、evaluator 与关键 resource budget 没有充分匹配，那么 leaderboard 上更高的 score 首先只是 **system-level evidence**，不能直接归因给某个 component。

最后更新：**2026-08-20**

<a id="timeline"></a><a id="latest"></a><a id="frontier"></a>
## Latest Timeline：最新接受的评测变化

> **迁移说明：** 对于无法重建 Radar 接受时间的旧记录，本节暂按原始发布日期/月份排序，并保留真实的月精度；v2 切换后的新记录统一使用 `radar_published_at`。

<a id="entry-dsagentbench"></a>
<details><summary>2026-08 · DSAgentBench · Data Agent / 真实计算机中的端到端 data-science workflow <!-- timefirst:area=data-agent-real-computer-workflow --> — 把评价对象从分离的 code/answer stage 推到由 intermediate outputs 支撑的多工具完整工作流。 <!-- timefirst:delta=isolated-stages-to-end-to-end-workflow --></summary>

**问题。** Agent 能否在真实 computer environment 中完成跨 wrangling、modeling、visualization 与 validation 的 data-science 任务？ <!-- timefirst:question=end-to-end-data-science-execution -->

**证据。** 275 个任务使用 deterministic evaluator 检查 analytical correctness、visual outputs 与 model performance；论文报告最强 agent 为 56.70%，open-source agents 低于 1%。 <!-- timefirst:evidence=275-tasks-deterministic-evaluation-56.70~analytical-correctness-visual-outputs -->

**限制。** Model、harness、tool reliability、OS grounding 与 recovery 同时变化，所以这是 system-level evidence，不是某个 planner 的独立效果。 <!-- timefirst:caveat=system-level-harness-confounding~model-harness-tool-reliability -->

**地图。** `early_signal`；新坐标是 real-computer environment + protocol，单篇记录不改写持久地图。

**链接。** [论文](https://arxiv.org/abs/2608.10366) · [本地深度笔记](benchmarks/dsagentbench.md)

</details>

<a id="entry-vakra"></a>
<details><summary>2026-08 · VAKRA · RAG / 跨源可执行一致性 <!-- timefirst:area=rag-cross-source-executable-coherence --> — 将 API、document retrieval、multi-hop reasoning 与 policy constraint 放入同一可重执行 trajectory。 <!-- timefirst:delta=apis-retrieval-policy-one-trajectory --></summary>

**问题。** Agent 能否在 structured API 与 unstructured documents 之间维持 identity、grounding 和 policy consistency？ <!-- timefirst:question=cross-source-identity-grounding-policy -->

**证据。** VAKRA 提供 8,000+ locally hosted executable APIs、62 个 domains，并重执行 predicted tool calls；结果显示 compositional 与 policy-constrained setting 明显难于 single-hop endpoint task。 <!-- timefirst:evidence=8000-apis-62-domains-composition-gap~predicted-tool-calls -->

**限制。** 固定 ReAct harness 改善 model 间可比性，但也把结论绑定到一个 interface/controller contract，不能比较替代 agent architecture。 <!-- timefirst:caveat=fixed-react-harness-binding~interface-controller-contract -->

**地图。** `early_signal`；它为 cross-source executable coherence 增加坐标，尚不构成独立趋势证据。

**链接。** [论文](https://arxiv.org/abs/2608.12282) · [本地深度笔记](benchmarks/vakra.md)

</details>

<a id="entry-dataspace"></a>
<details><summary>2026-08 · DataSpace · Data Agent / heterogeneous workspace analytics <!-- timefirst:area=data-agent-heterogeneous-workspace-analytics --> — 把 evidence discovery、cross-source computation 与 deterministic complete-result verification 合并成一个评价对象。 <!-- timefirst:delta=discovery-computation-deterministic-verification --></summary>

**问题。** 只给 question + task-local workspace 时，agent 能否从 DB、files、documents 与 multimedia 中找到证据并返回完整表格？ <!-- timefirst:question=heterogeneous-evidence-to-complete-table -->

**证据。** 410 个任务覆盖 7,439 个 artifacts；论文报告固定 backbone 时 harness 选择造成 15.36 points 差距；这个 harness sensitivity spread 说明了系统级敏感性。 <!-- timefirst:evidence=410-tasks-7439-artifacts-15.36-harness-gap~harness-sensitivity-spread -->

**限制。** Frozen task-local workspace 没有覆盖 enterprise drift、permissions、writes、business-definition ambiguity 与长时间 project state。 <!-- timefirst:caveat=frozen-workspace-omits-enterprise-state~enterprise-drift-permissions-writes -->

**地图。** `early_signal`；异构证据与 deterministic verification 是新的联合坐标，但 harness effect 阻止 component attribution。

**链接。** [论文](https://arxiv.org/abs/2608.03451) · [本地深度笔记](benchmarks/dataspace.md)

</details>

<a id="entry-locomo-plus"></a>
<details><summary>2026-07 · LoCoMo-Plus · Agent Memory / latent user constraint <!-- timefirst:area=memory-latent-user-constraints --> — 把 target 从找回明示旧事实推到在无直接 cue 时仍正确应用 remembered user state。 <!-- timefirst:delta=explicit-recall-to-implicit-state-application --></summary>

**问题。** 后续 query 没有重述旧约束时，agent 是否仍能让 latent user state 约束当前回答？ <!-- timefirst:question=cue-disconnected-constraint-application -->

**证据。** Benchmark 用 cue–trigger semantic disconnect 与 constraint consistency 区分 explicit recall 与对隐式 state 的应用。 <!-- timefirst:evidence=cue-trigger-disconnect-constraint-consistency~cue-trigger-semantic-disconnect -->

**限制。** Constraint construction 与 evaluator 是 load-bearing，且当前仍是 conversational response evaluation，未覆盖 preference drift 和不可逆 action。 <!-- timefirst:caveat=evaluator-construction-and-no-actions~conversational-response-evaluation -->

**地图。** `early_signal`；它连接 factual recall 与未来 memory-guided action，尚未单独重写长期因果地图。

**链接。** [ACL 论文](https://aclanthology.org/2026.acl-long.1150/) · [本地深度笔记](benchmarks/locomo-plus.md)

</details>

<a id="entry-mem2actbench"></a>
<details><summary>2026-07 · Mem2ActBench · Agent Memory / memory-guided tool action <!-- timefirst:area=memory-guided-tool-action --> — 直接测量 memory 是否改变 tool selection 与 parameter grounding，而不只是帮助回答。 <!-- timefirst:delta=answers-to-tool-selection-and-parameters --></summary>

**问题。** 长期 memory 是否会被主动用于选择工具与填充 action parameter？ <!-- timefirst:question=proactive-memory-use-in-tool-actions -->

**证据。** 评价把 memory utilization 放在 tool-based assistant action 上，使 action-level effect 比仅从 past-context answer 推断更直接。 <!-- timefirst:evidence=action-level-memory-utilization~tool-based-assistant -->

**限制。** Tool-call task 仍窄于 action 会改写 persistent state、错误有下游后果的 long-horizon environment，这个 persistent state consequence risk 仍超出核心 protocol。 <!-- timefirst:caveat=tool-calls-omit-persistent-consequences~persistent-state-consequence-risk -->

**地图。** `early_signal`；它把 memory 评价推到 action coordinate，但一项 work 不足以建立持久 trend。

**链接。** [ACL 论文](https://aclanthology.org/2026.acl-long.370/)

</details>

<a id="entry-agenticdatabench"></a>
<details><summary>2026-07 · AgenticDataBench · Data Agent / data-science skill coverage <!-- timefirst:area=data-agent-skill-coverage --> — 用细粒度 skill taxonomy 使 benchmark coverage 本身可审计，不再只看 aggregate success。 <!-- timefirst:delta=aggregate-score-to-auditable-skill-coverage --></summary>

**问题。** 一个 data-agent benchmark 究竟覆盖了哪些现实 data-science skills，缺失了哪些？ <!-- timefirst:question=covered-and-missing-data-science-skills -->

**证据。** Benchmark 用 skill taxonomy 组织 realistic data-science workflows，使系统能力覆盖可以在总分之下被诊断，形成 skill taxonomy coverage audit，位于总分之下。 <!-- timefirst:evidence=skill-taxonomy-below-aggregate-score~skill-taxonomy-coverage-audit -->

**限制。** Skill taxonomy 与 generated tasks 可能不覆盖 organization-specific semantics、evolving data 或 governance constraints。 <!-- timefirst:caveat=taxonomy-omits-org-semantics-and-drift~organization-specific-semantics -->

**地图。** `early_signal`；coverage audit 是新诊断坐标，尚不能证明真实工作流的可靠交付。

**链接。** [论文](https://arxiv.org/abs/2607.01647)

</details>

<a id="entry-sgr-bench"></a>
<details><summary>2026-05 · SGR-Bench · RAG / state-gated retrieval <!-- timefirst:area=rag-state-gated-retrieval --> — 区分“找到正确 source”与“正确配置 filter、hierarchy、scope 和 site state”。 <!-- timefirst:delta=source-finding-to-environment-configuration --></summary>

**问题。** 当答案证据只在正确的 site-specific retrieval state 中可见时，search agent 能否建立该 state？ <!-- timefirst:question=establish-site-specific-retrieval-state -->

**证据。** Protocol 把 filters、hierarchy、scope 或 view 设置变成答案可达的前置条件，因而能看到 source discovery 之后的 control failure。 <!-- timefirst:evidence=filters-hierarchy-scope-as-access-gates~filters-hierarchy-scope -->

**限制。** State-gated retrieval 比 general web research、document RAG 或 arbitrary tool orchestration 更窄，不能代表整个 agentic retrieval 领域。 <!-- timefirst:caveat=narrower-than-general-agentic-retrieval~state-gated-retrieval -->

**地图。** `early_signal`；它增加 information-environment configuration 坐标，但没有独立证据支持地图升级。

**链接。** [论文](https://arxiv.org/abs/2605.22219)

</details>

<a id="entry-realmem"></a>
<details><summary>2026-01 · RealMem · Agent Memory / persistent project state <!-- timefirst:area=memory-persistent-project-state --> — 把 long-term memory 从 casual dialogue 扩展到 goal、artifact 与 relevant state 持续演化的跨 session project work。 <!-- timefirst:delta=casual-dialogue-to-cross-session-project-work --></summary>

**问题。** Agent 能否在长时间 project-oriented interaction 中保持正确的 evolving goals、artifacts 与相关 state？ <!-- timefirst:question=preserve-evolving-goals-artifacts-state -->

**证据。** Evaluation 将 cross-session memory 放入 project-oriented interaction，使持久任务状态而非仅 casual conversation 成为可测对象。 <!-- timefirst:evidence=project-oriented-cross-session-evaluation~project-oriented-interaction -->

**限制。** Synthetic multi-agent trajectory generation 与 dialogue-only interaction 仍抽象掉了真实 collaborative writes、permissions 和 tooling。 <!-- timefirst:caveat=synthetic-dialogue-omits-real-collaboration~collaborative-writes-permissions -->

**地图。** `early_signal`；persistent project state 是新 frontier signal，但尚未提供长期因果 attribution。

**链接。** [ACL Findings 论文](https://aclanthology.org/2026.findings-acl.703/)

</details>

<a id="periods"></a><a id="changes"></a>
## 7 天 / 30 天：评价对象发生了什么变化

<a id="last-7-days"></a>
### 过去 7 天：2026-08-14—2026-08-20

- **`no_material_change` · Benchmark acceptance time：本窗口没有可归入 Radar 接受时间的新方向。** <!-- timefirst:direction key="benchmark-acceptance-time" state="no_material_change" supports="none" confidence="high" implication="require-native-v2-times-for-period-claims" timing="radar_published_at" synthesized="2026-08-20T00:00:00Z" prior="none" -->
  支撑：**none**；置信度：**high**；时间依据：`radar_published_at`；先验地图证据：`none`。研究设计含义（require native v2 times for period claims）：旧 Timeline 记录只作历史语境，不计作支撑；只有带原生 v2 Radar 接受时间的记录才能支持窗口判断。精确合成时间：`2026-08-20T00:00:00Z`（UTC）。

<a id="last-30-days"></a>
### 过去 30 天：2026-07-22—2026-08-20

- **`no_material_change` · Benchmark acceptance time：本窗口没有可归入 Radar 接受时间的新方向。** <!-- timefirst:direction key="benchmark-acceptance-time" state="no_material_change" supports="none" confidence="high" implication="require-native-v2-times-for-period-claims" timing="radar_published_at" synthesized="2026-08-20T00:00:00Z" prior="none" -->
  支撑：**none**；置信度：**high**；时间依据：`radar_published_at`；先验地图证据：`none`。研究设计含义（require native v2 times for period claims）：DSAgentBench、VAKRA、DataSpace、LoCoMo-Plus、Mem2ActBench 与 AgenticDataBench 只作历史语境，不计作本窗口支撑；它们的月精度记录不能证明 Radar 接受时间落在该窗口。精确合成时间：`2026-08-20T00:00:00Z`（UTC）。

<a id="evolution"></a>
## Benchmark 演化告诉我们：领域正在把什么当成“进步”

| Area | 演化 | 现在越来越关心什么 | 继续深入 |
|---|---|---|---|
| **Agent Memory** | 跨会话召回 → 生命周期诊断 → 演化、共享、多模态状态 → **记忆指导行为与行动** | 什么该写、更新、授权、遗忘和使用？失败发生在生命周期的哪一步？ | [Agent Memory Radar](https://github.com/H20Zhang/Agent-Memory-Radar#field-map) |
| **RAG / Agentic Retrieval** | 相关性与忠实度 → 迭代搜索 → 证据集覆盖 → **实时、多模态、可审计搜索** | 能否找到互补证据、适时停止，并定位或修复失败的搜索？ | [Agentic RAG Radar](https://github.com/H20Zhang/Agentic-RAG-Radar#field-map) |
| **Data Agents** | 自然语言转 SQL/代码 → 工作流与探索 → 异构分析 → **业务正确、可靠交付** | 能否发现并理解数据，执行与核验任务，并在不该作答时追问或拒答？ | [Data Agent Radar](https://github.com/H20Zhang/Data-Agent-Radar#field-map) |

<a id="field-map"></a>
## 三个领域的 Benchmark 地图

<a id="benchmark-memory"></a>
### Agent Memory

**主干：** [Multi-Session Chat](https://aclanthology.org/2022.acl-long.356/) → [LoCoMo](https://aclanthology.org/2024.acl-long.747/) / [LongMemEval](https://arxiv.org/abs/2410.10813) → [MemoryAgentBench](https://arxiv.org/abs/2507.05257) → [MemoryArena](https://arxiv.org/abs/2602.16313) / [WorldMemArena](https://arxiv.org/abs/2605.29341) / [InMind](https://arxiv.org/abs/2607.24368) → [Mem2ActBench](https://aclanthology.org/2026.acl-long.370/) / [LoCoMo-Plus](https://aclanthology.org/2026.acl-long.1150/)

**前沿信号：** 生命周期基准开始分别检查写入、维护、检索和使用；其他分支则把隐式行为变化、多模态保留、群体身份、授权与删除、个性化安全和记忆指导行动变成可观测对象。

**当前最大缺口：** persistent environment 里的 longitudinal causality——匹配 cost/context budget、权限、不可逆 action，以及持续数周/数月的 state evolution。

[查看完整的 Agent Memory 基准表 →](library/README.md#agent-memory) · [进入 Agent Memory 方法与系统 →](https://github.com/H20Zhang/Agent-Memory-Radar#field-map)

<details><summary><strong>展开更完整的 Memory genealogy</strong></summary>

`Multi-Session Chat → LoCoMo / LongMemEval → MemBench / MemoryAgentBench / BEAM → MemoryArena / WorldMemArena / InMind → ImplicitMemBench / GateMem / DynamicMem / Mem2ActBench / LoCoMo-Plus`

完整 registry 与 role 见 [Benchmark Library](#library)。

</details>

<a id="benchmark-rag"></a>
### RAG / Agentic Retrieval

**主干：** [HotpotQA](https://aclanthology.org/D18-1259/) → [BEIR](https://arxiv.org/abs/2104.08663) / [BRIGHT](https://arxiv.org/abs/2407.12883) → [BrowseComp](https://arxiv.org/abs/2504.12516) → [AutoResearchBench](https://arxiv.org/abs/2604.25256) / [Bright-Pro](https://aclanthology.org/2026.acl-long.1705/) → [LiveBrowseComp](https://arxiv.org/abs/2605.28721) / [LoHoSearch](https://arxiv.org/abs/2606.12837) → [SearchAuditBench](https://arxiv.org/abs/2608.05212) / [VAKRA](https://arxiv.org/abs/2608.12282)

**前沿信号：** 评价开始区分相关性与维度覆盖、单篇定位与完整集合收集、最终正确与停止判断；校准、失败定位、修复、安全、多模态证据和实时网页新鲜度也进入协议。

**当前最大缺口：** 在 interface / harness / model / budget 匹配的情况下做 causal attribution，尤其是 live environment 会持续 drift 的 long-horizon setting。

[查看完整的 RAG 基准表 →](library/README.md#rag--agentic-retrieval) · [进入 Agentic RAG 方法与系统 →](https://github.com/H20Zhang/Agentic-RAG-Radar#field-map)

<a id="benchmark-data"></a>
### Data Agents

**主干：** [WikiSQL](https://arxiv.org/abs/1709.00103) → [Spider](https://aclanthology.org/D18-1425/) / [DS-1000](https://arxiv.org/abs/2211.11501) → [Spider 2.0](https://arxiv.org/abs/2411.07763) / [DDR-Bench](https://arxiv.org/abs/2602.02039) → [DataClawBench](https://arxiv.org/abs/2605.02503) / [Data Exploration Benchmark](https://arxiv.org/abs/2608.16045) → [CausalDS](https://arxiv.org/abs/2607.08093) / [WarehouseReliabilityBench](https://arxiv.org/abs/2608.09254) / [DataSpace](https://arxiv.org/abs/2608.03451) / [DSAgentBench](https://arxiv.org/abs/2608.10366)

**前沿信号：** 数据发现和数据理解正在成为单独计分的产物；因果识别、流程遵从、业务真值、追问与拒答、恢复、稳定性和成本，也开始与端到端成功率并列。

**当前最大缺口：** 真实 enterprise semantics、business-definition ambiguity、long-running workflow state、deployment/monitoring、governance，以及“问题本身就定义不清楚”时的可靠 clarification / abstention。

[查看完整的 Data Agent 基准表 →](library/README.md#data-agents) · [进入 Data Agent 方法与系统 →](https://github.com/H20Zhang/Data-Agent-Radar#field-map)

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
| **记忆怎样从召回走向可诊断的行动？** | Multi-Session Chat → LoCoMo / LongMemEval → MemoryAgentBench → WorldMemArena / InMind → Mem2ActBench / LoCoMo-Plus | [Agent Memory Radar](https://github.com/H20Zhang/Agent-Memory-Radar#field-map) |
| **检索怎样变成可审计的搜索过程？** | HotpotQA / BEIR → BrowseComp → AutoResearchBench / Bright-Pro → LiveBrowseComp / LoHoSearch → SearchAuditBench | [Agentic RAG Radar](https://github.com/H20Zhang/Agentic-RAG-Radar#field-map) |
| **数据评测怎样从可执行代码走向业务正确的交付？** | WikiSQL / Spider / DS-1000 → DDR-Bench / DataClawBench → Data Exploration Benchmark → WarehouseReliabilityBench / DataSpace / DSAgentBench | [Data Agent Radar](https://github.com/H20Zhang/Data-Agent-Radar#field-map) |

<a id="library"></a>
## Benchmark Library

- **[浏览完整发布时间线与领域表](library/README.md)**
- [按演化关系与测量维度继续阅读](library/README.md#按-genealogy-阅读)
- [Canonical registry](data/benchmarks.json)
- [Research compactions](digests/README.md)

## About

Benchmark Radar 之所以适合作为整个 family 的入口，是因为 genealogy 能先给新人一个紧凑答案：**领域想提升什么能力、旧 target 为什么不够、现在什么 evidence 才算进步。** 然后再把读者送到 domain radar，而不是在这里重复方法综述。

[English](README.en.md) · [Curation](CURATION.md) · [Schema](SCHEMA.md)
