# Agent Benchmark Radar

**中文** | [English](README.en.md)

<a id="frontier-signals"></a>
## 近 30 天：三个变化

<!-- FRONTIER-SIGNALS:START -->
| 方向 | 真正变化 | 代表 Benchmark |
|---|---|---|
| **Agent Memory** | 从“能不能召回”推进到**记忆是否因果改变后续行动，以及持久状态能否被安全治理**。PAST-Bench 用 persistence on/off 配对控制直接测 memory 的后续作用；SP-Mem 把 personalization、consent 与 leakage 放进同一协议；InMind 把 storage / knowledge / routing / use failure 拆开。 | [PAST-Bench](https://arxiv.org/abs/2608.04003) · [SP-Mem](https://arxiv.org/abs/2608.16551) · [InMind](https://arxiv.org/abs/2607.24368) |
| **RAG / Agentic Retrieval** | 重点从“recall 高不高”转向**retrieval metric 是否真的预测下游成功、搜索过程能否被审计、结果能否跨部署条件复现**。The Recall Trap 给出 recall 与 repair success 脱钩的直接反例；SearchAuditBench 测 failure localization / repair；The Commercial Tax 把 license、query format、index construction 与 cost 纳入可迁移性。 | [The Recall Trap](https://arxiv.org/abs/2608.14838) · [SearchAuditBench](https://arxiv.org/abs/2608.05212) · [The Commercial Tax](https://arxiv.org/abs/2608.16096) |
| **Data Agents** | 评价对象继续从“SQL / code 能跑”推到**先理解数据、再完成可验证工作，并在业务语义不清时正确追问或拒答**。Data Exploration Benchmark 把 exploration 单独计分；WarehouseReliabilityBench 测 business truth / clarification / abstention；data-eng-bench 的 evaluator 修复说明评测器本身也会成为可靠性瓶颈。 | [Data Exploration Benchmark](https://arxiv.org/abs/2608.16045) · [WarehouseReliabilityBench](https://arxiv.org/abs/2608.09254) · [data-eng-bench](https://github.com/Snowflake-Labs/data-eng-bench) |
<!-- FRONTIER-SIGNALS:END -->

最后更新：**2026-08-21**

<a id="release-timeline"></a>
## 最近半年 Benchmark 时间线

<!-- TABLE-FIRST:RECENT:START -->
| 时间 | 方向 | Benchmark | 考察内容 |
|---|---|---|---|
| 2026-08-18 | RAG | [VisDocAgentBench](https://arxiv.org/abs/2608.17889) <!-- benchmark-id:visdocagentbench --> | 在统一页面排序协议下比较静态 ranker 与迭代视觉/OCR agent 的视觉文档检索基准。 |
| 2026-08-17 | Data Agent | [Data Exploration Benchmark](https://arxiv.org/abs/2608.16045) <!-- benchmark-id:data-exploration-benchmark --> | 在下游分析前，构建包含逻辑表、列语义、键关系和质量信号的结构化数据理解产物。 |
| 2026-08-17 | Agent Memory | [SP-Mem Privacy-Aware Memory Benchmark](https://arxiv.org/abs/2608.16551) <!-- benchmark-id:sp-mem --> | 联合测量回答质量、个性化、同意处理、精确值暴露与成本的隐私感知记忆基准。 |
| 2026-08-17 | RAG | [The Commercial Tax](https://arxiv.org/abs/2608.16096) <!-- benchmark-id:commercial-tax --> | 把原始 embedder 分数绑定到许可、query format、索引构造与部署成本的检索复现性审计。 |
| 2026-08-10 | RAG | [The Recall Trap](https://arxiv.org/abs/2608.14838) <!-- benchmark-id:recall-trap --> | 有效性审计：在固定槽位代码检索协议下，更高 file recall 可能降低下游修复成功率。 |
| 2026-08-10 | Data Agent | [WarehouseReliabilityBench](https://arxiv.org/abs/2608.09254) <!-- benchmark-id:warehouse-reliability-bench --> | 面对语义歧义、不可回答、模式漂移和对抗输入时，返回业务真值或正确地澄清、弃答、拒答。 |
| 2026-08-07 | RAG | [DAS-Bench / DAS-Eval](https://arxiv.org/abs/2608.18034) <!-- benchmark-id:das-bench --> | 对文献覆盖、taxonomy、claim、citation、discourse 与渲染成品质量评分的学术综述基准及评测器。 |
| 2026-08-05 | RAG | [SearchAuditBench](https://arxiv.org/abs/2608.05212) <!-- benchmark-id:searchauditbench --> | 考察审计模型能否在超长搜索轨迹中定位错误、归因根因并生成可执行修复。 |
| 2026-08-04 | RAG | [MAPLE](https://arxiv.org/abs/2608.15624) <!-- benchmark-id:maple --> | 测量同一论文能否在动机、方法与结果等多个 aspect 下持续被找回的科学检索基准。 |
| 2026-08-04 | Agent Memory | [PAST-Bench](https://arxiv.org/abs/2608.04003) <!-- benchmark-id:past-bench --> | 通过配对持久状态控制，检验跨 episode 经验是否因果改善后续可执行工作的基准。 |
| 2026-08 | Data Agent | [DataSpace](https://arxiv.org/abs/2608.03451) <!-- benchmark-id:dataspace --> | 在混合数据库、文件、文档和多媒体的工作区中完成可验证分析。 |
| 2026-08 | Data Agent | [DSAgentBench](https://arxiv.org/abs/2608.10366) <!-- benchmark-id:dsagentbench --> | 使用笔记本、IDE、终端、浏览器和数据库完成完整数据科学工作流。 |
| 2026-08 | RAG | [VAKRA](https://arxiv.org/abs/2608.12282) <!-- benchmark-id:vakra --> | 组合调用 API、检索文档、完成多跳推理，并遵守工具策略。 |
| 2026-07-29 | Data Agent | [data-eng-bench](https://github.com/Snowflake-Labs/data-eng-bench) <!-- benchmark-id:data-eng-bench --> | 面向仓库规模 dbt 转换的可执行数据工程基准，在 DuckDB 与 Snowflake 上做隐藏行级核验。 |
| 2026-07-27 | Agent Memory | [InMind](https://arxiv.org/abs/2607.24368) <!-- benchmark-id:inmind --> | 旧事实与新问题词义相远、只有借助常识才能建立联系时，记忆能否被正确调出并应用。 |
| 2026-07-21 | Agent Memory | [MemFuseBench](https://arxiv.org/abs/2608.18704) <!-- benchmark-id:memfusebench --> | 跨异构事件流的来源连接、因果融合、冲突裁决与溯源记忆基准。 |
| 2026-07-14 | RAG | [WANDR](https://arxiv.org/abs/2608.14747) <!-- benchmark-id:wandr --> | 面向实时网页 wide-and-deep 记录收集的基准，包含分层任务和无需穷举金标的逐条核验。 |
| 2026-07-09 | Data Agent | [CausalDS](https://arxiv.org/abs/2607.08093) <!-- benchmark-id:causalds --> | 在可执行数据科学环境中覆盖因果预测、识别、效应估计、反事实、不确定性与弃答。 |
| 2026-07 | Data Agent | [AgenticDataBench](https://arxiv.org/abs/2607.01647) <!-- benchmark-id:agenticdatabench --> | 用细粒度技能分类检查真实数据科学工作流的覆盖情况。 |
| 2026-07 | Agent Memory | [LoCoMo-Plus](https://aclanthology.org/2026.acl-long.1150/) <!-- benchmark-id:locomo-plus --> | 后续问题没有复述旧约束时，能否继续正确应用它。 |
| 2026-07 | Agent Memory | [Mem-Gallery](https://aclanthology.org/2026.acl-long.1892/) <!-- benchmark-id:mem-gallery --> | 多模态长期对话中的记忆抽取、适应、推理和知识管理。 |
| 2026-07 | Agent Memory | [Mem2ActBench](https://aclanthology.org/2026.acl-long.370/) <!-- benchmark-id:mem2actbench --> | 长期记忆是否会影响工具选择和参数填写。 |
| 2026-07 | Agent Memory | [PerMemSafe](https://aclanthology.org/2026.findings-acl.320/) <!-- benchmark-id:permemsafe --> | 能否从长期历史中识别隐含的个体风险，并在风险缓解后及时更新判断。 |
| 2026-06-23 | Agent Memory | [MEMPROBE](https://arxiv.org/abs/2606.24595) <!-- benchmark-id:memprobe --> | 普通协助结束后，能否从智能体留下的记忆产物中恢复隐藏的用户状态。 |
| 2026-06-22 | Agent Memory | [DynamicMem](https://arxiv.org/abs/2606.22877) <!-- benchmark-id:dynamicmem --> | 从十五个月、多个应用的零散行为中推断并更新用户属性、习惯和偏好。 |
| 2026-06-22 | Data Agent | [StatABench](https://arxiv.org/abs/2606.22977) <!-- benchmark-id:statabench --> | 同时评估统计知识、工具选择与参数设置，以及开放式建模和报告。 |
| 2026-06-17 | Agent Memory | [GateMem](https://arxiv.org/abs/2606.18829) <!-- benchmark-id:gatemem --> | 多人共享记忆能否同时保持可用、阻止越权泄露并执行删除请求。 |
| 2026-06-13 | Data Agent | [IRTS-ToolBench](https://arxiv.org/abs/2606.15107) <!-- benchmark-id:irts-toolbench --> | 在异步、缺失且采样频率不一的非规则时间序列上选择工具并完成可核验问答。 |
| 2026-06-11 | RAG | [EvoBrowseComp](https://arxiv.org/abs/2606.13120) <!-- benchmark-id:evobrowsecomp --> | 考察英语和中文智能体对持续变化网络知识的广度搜索与多步推理。 |
| 2026-06-11 | RAG | [LoHoSearch](https://arxiv.org/abs/2606.12837) <!-- benchmark-id:lohosearch --> | 考察超大候选空间、复杂约束结构、长程搜索和上下文管理。 |
| 2026-06 | Agent Memory | [LifeSide](https://arxiv.org/abs/2606.04660) <!-- benchmark-id:lifeside --> | 跨会话记忆、用户理解、隐私控制，以及情绪与环境的互动。 |
| 2026-05-28 | Agent Memory | [WorldMemArena](https://arxiv.org/abs/2605.29341) <!-- benchmark-id:worldmemarena --> | 从多模态观察、行动和反馈中写入、维护、检索并使用不断变化的世界状态。 |
| 2026-05-27 | RAG | [LiveBrowseComp](https://arxiv.org/abs/2605.28721) <!-- benchmark-id:livebrowsecomp --> | 考察智能体能否检索近期、低显著性的网络事实，而非只验证模型已有知识。 |
| 2026-05-19 | RAG | [ScholarQuest](https://arxiv.org/abs/2606.20235) <!-- benchmark-id:scholarquest --> | 考察智能体按研究意图迭代检索论文、扩展引文和控制结果范围。 |
| 2026-05-18 | Agent Memory | [EvoMemBench](https://arxiv.org/abs/2605.18421) <!-- benchmark-id:evomembench --> | 在回合内与跨回合、知识型与执行型两条轴上统一比较记忆系统。 |
| 2026-05-14 | Agent Memory | [GroupMemBench](https://arxiv.org/abs/2605.14498) <!-- benchmark-id:groupmembench --> | 多人群聊中的说话者信念、群体动态、术语差异和面向不同受众的表达。 |
| 2026-05-14 | Agent Memory | [MemEye](https://arxiv.org/abs/2605.15128) <!-- benchmark-id:memeye --> | 细粒度视觉证据、视觉状态变化，以及纯文本捷径检查。 |
| 2026-05-14 | Agent Memory | [MEMLENS](https://arxiv.org/abs/2605.14906) <!-- benchmark-id:memlens --> | 在 32K 到 256K 的多模态多会话历史中进行提取、更新、时间推理和拒答。 |
| 2026-05-12 | Agent Memory | [MedMemoryBench](https://arxiv.org/abs/2605.11814) <!-- benchmark-id:medmemorybench --> | 在持续增长的医疗对话中追踪病情、时间变化和复杂临床信息，并观察记忆饱和。 |
| 2026-05-04 | Data Agent | [DataClawBench](https://arxiv.org/abs/2605.02503) <!-- benchmark-id:dataclawbench --> | 在几乎没有先验提示时，自主探索陌生、含噪、跨域金融数据并形成可验证结论。 |
| 2026-05 | Agent Memory | [LongMemEval-V2](https://arxiv.org/abs/2605.12493) <!-- benchmark-id:longmemeval-v2 --> | 大量网页智能体轨迹中的环境状态、操作流程和易错点。 |
| 2026-05 | RAG | [SGR-Bench](https://arxiv.org/abs/2605.22219) <!-- benchmark-id:sgr-bench --> | 在证据受站点筛选、层级、范围或视图状态控制时完成搜索。 |
| 2026-04-30 | RAG | [Bright-Pro](https://aclanthology.org/2026.acl-long.1705/) <!-- benchmark-id:bright-pro --> | 考察推理密集型检索、推理要点覆盖，以及检索器在静态与智能体搜索中的实际效用。 |
| 2026-04-19 | RAG | [MuDABench](https://aclanthology.org/2026.findings-acl.341/) <!-- benchmark-id:mudabench --> | 考察大规模财务文档集合中的信息抽取、跨文档聚合和定量分析。 |
| 2026-04-17 | Agent Memory | [MemEvoBench](https://arxiv.org/abs/2604.15774) <!-- benchmark-id:memevobench --> | 误导性记忆、噪声工具结果和偏置反馈在多轮写回后会不会使行为逐步失去安全性。 |
| 2026-04-15 | RAG | [MERRIN](https://arxiv.org/abs/2604.13418) <!-- benchmark-id:merrin --> | 考察智能体在嘈杂网络中自主选择模态、检索多模态证据并进行多跳推理。 |
| 2026-04-14 | RAG | [EnterpriseRAG-Bench](https://arxiv.org/abs/2605.05253) <!-- benchmark-id:enterpriserag-bench --> | 考察企业式知识库中的检索、多文档推理、冲突处理、完整性和无答案识别。 |
| 2026-04-09 | Agent Memory | [ImplicitMemBench](https://aclanthology.org/2026.acl-long.1301/) <!-- benchmark-id:implicitmembench --> | 干扰之后，模型能否在首次尝试中自动表现出已学程序、启动效应或条件联结。 |
| 2026-04-07 | RAG | [LeakDojo](https://aclanthology.org/2026.findings-acl.287/) <!-- benchmark-id:leakdojo --> | 考察攻击者从 RAG 数据库抽取文本内容的能力，以及不同管线和防御下的泄露风险。 |
| 2026-04-01 | RAG | [AutoResearchBench](https://arxiv.org/abs/2604.25256) <!-- benchmark-id:autoresearchbench --> | 考察科学文献中的目标论文追踪、条件约束、开放集合搜集和停止判断。 |
| 2026-03-12 | Data Agent | [AgentFuel](https://arxiv.org/abs/2603.12483) <!-- benchmark-id:agentfuel --> | 面向具体领域的时序对话智能体功能测试，重点覆盖有状态与事故型查询。 |
| 2026-03-05 | Data Agent | [TML-Bench](https://arxiv.org/abs/2603.05764) <!-- benchmark-id:tml-bench --> | 在固定时间预算和隐藏标签下，产出有效且有竞争力的表格机器学习提交。 |
| 2026-03 | Data Agent | [Data Agent Benchmark (DAB)](https://arxiv.org/abs/2603.20576) <!-- benchmark-id:data-agent-benchmark --> | 跨多个 DBMS 完成数据集成、转换、分析和可执行核验。 |
| 2026-03 | Agent Memory | [LifeBench](https://arxiv.org/abs/2603.03781) <!-- benchmark-id:lifebench --> | 多源长期轨迹中的事件、语义、习惯和程序性记忆。 |
| 2026-02-27 | Data Agent | [DARE-bench](https://arxiv.org/abs/2602.24288) <!-- benchmark-id:dare-bench --> | 用可验证真值同时评估机器学习建模效果与对指定数据科学流程的遵循。 |
| 2026-02-26 | RAG | [MTRAG-UN](https://aclanthology.org/2026.findings-acl.503/) <!-- benchmark-id:mtrag-un --> | 考察多轮 RAG 对不可回答、信息不足、非独立问题和含糊回复的处理。 |
| 2026-02-22 | RAG | [MC-Search](https://arxiv.org/abs/2603.00873) <!-- benchmark-id:mc-search --> | 考察多模态搜索规划、模态选择、逐跳证据检索和长链推理一致性。 |
| 2026-02-18 | Agent Memory | [MemoryArena](https://arxiv.org/abs/2602.16313) <!-- benchmark-id:memoryarena --> | 在跨会话的智能体—环境循环中，用早期行动与反馈指导后续行动。 |
| 2026-02-06 | RAG | [GISA](https://arxiv.org/abs/2602.08543) <!-- benchmark-id:gisa --> | 考察真实信息需求下的搜索规划、纵向推理、横向汇总和结构化作答。 |
| 2026-02-05 | RAG | [SAGE](https://arxiv.org/abs/2602.05975) <!-- benchmark-id:sage --> | 考察深度研究智能体在受控科学论文库中的定向找文与开放式文献搜集。 |
| 2026-02-03 | Agent Memory | [MemGUI-Bench](https://arxiv.org/abs/2602.06075) <!-- benchmark-id:memgui-bench --> | 移动端操作中的跨步骤保持、跨应用迁移、跨会话学习和失败恢复。 |
| 2026-02 | RAG | [AgenticRAGTracer](https://arxiv.org/abs/2602.19127) <!-- benchmark-id:agenticragtracer --> | 对多步检索与推理逐跳核验，并检查步骤分配。 |
| 2026-02 | Agent Memory | [AMA-Bench](https://arxiv.org/abs/2602.22769) <!-- benchmark-id:ama-bench --> | 真实和可扩展合成的智能体—环境轨迹上的长程记忆。 |
| 2026-02 | Agent Memory | [StructMemEval](https://arxiv.org/abs/2602.11243) <!-- benchmark-id:structmemeval --> | 智能体能否维护账本、列表、树等符合任务需要的记忆结构。 |<!-- TABLE-FIRST:RECENT:END -->

<a id="timeline"></a><a id="latest"></a><a id="frontier"></a>
<a id="periods"></a><a id="changes"></a><a id="evolution"></a>
<a id="field-map"></a>
## Benchmark 地图

<a id="benchmark-memory"></a>
### Agent Memory
从跨会话事实召回，逐步走向在线更新、结构化记忆、多模态证据、行动、权限与隐式用户状态。

**主干：** [Beyond Goldfish Memory](https://aclanthology.org/2022.acl-long.356/) → [LoCoMo](https://aclanthology.org/2024.acl-long.747/) / [LongMemEval](https://arxiv.org/abs/2410.10813) → [MemoryAgentBench](https://arxiv.org/abs/2507.05257) → [StructMemEval](https://arxiv.org/abs/2602.11243) / [MemoryArena](https://arxiv.org/abs/2602.16313) → [MemEye](https://arxiv.org/abs/2605.15128) / [WorldMemArena](https://arxiv.org/abs/2605.29341) → [DynamicMem](https://arxiv.org/abs/2606.22877) / [LoCoMo-Plus](https://aclanthology.org/2026.acl-long.1150/) → [GateMem](https://arxiv.org/abs/2606.18829) / [Mem2ActBench](https://aclanthology.org/2026.acl-long.370/) / [PAST-Bench](https://arxiv.org/abs/2608.04003) / [SP-Mem](https://arxiv.org/abs/2608.16551)

<a id="benchmark-rag"></a>
### RAG / Agentic Retrieval
从文档相关性，逐步走向多跳证据组合、实时搜索、停止判断、跨来源执行与轨迹审计。

**主干：** [HotpotQA](https://aclanthology.org/D18-1259/) → [BEIR](https://arxiv.org/abs/2104.08663) / [BRIGHT](https://arxiv.org/abs/2407.12883) → [BrowseComp](https://arxiv.org/abs/2504.12516) → [AutoResearchBench](https://arxiv.org/abs/2604.25256) / [Bright-Pro](https://aclanthology.org/2026.acl-long.1705/) → [LiveBrowseComp](https://arxiv.org/abs/2605.28721) / [LoHoSearch](https://arxiv.org/abs/2606.12837) → [SearchAuditBench](https://arxiv.org/abs/2608.05212) / [VAKRA](https://arxiv.org/abs/2608.12282) → [MAPLE](https://arxiv.org/abs/2608.15624) / [VisDocAgentBench](https://arxiv.org/abs/2608.17889) / [WANDR](https://arxiv.org/abs/2608.14747)

**前沿信号：** 评价已由相关性推进到跨 aspect/path/hierarchy 的结构化证据覆盖，并把 live-web discovery 与 visual-document inspection 拆开计量；新的 validity audit 还要求把 retrieval number 绑定 packing、query format、license、cost 与 downstream execution。

**当前最大缺口：** 在 interface / harness / model / budget 匹配的情况下做 causal attribution，尤其是 live environment 会持续 drift 的 long-horizon setting。

[查看完整的 RAG 基准表 →](library/README.md#rag--agentic-retrieval) · [进入 Agentic RAG 方法与系统 →](https://github.com/H20Zhang/Agentic-RAG-Radar#field-map)

<a id="benchmark-data"></a>
### Data Agents
从 Text-to-SQL / code generation，逐步走向完整数据工作流、探索、统计/因果分析与业务语义可靠性。

**主干：** [WikiSQL](https://arxiv.org/abs/1709.00103) → [Spider](https://aclanthology.org/D18-1425/) / [DS-1000](https://arxiv.org/abs/2211.11501) → [MLAgentBench](https://arxiv.org/abs/2310.03302) / [InsightBench](https://arxiv.org/abs/2407.06423) → [Spider 2.0](https://arxiv.org/abs/2411.07763) / [KramaBench](https://arxiv.org/abs/2506.06541) → [DataClawBench](https://arxiv.org/abs/2605.02503) / [DSGym](https://arxiv.org/abs/2601.16344) → [StatABench](https://arxiv.org/abs/2606.22977) / [CausalDS](https://arxiv.org/abs/2607.08093) → [DataSpace](https://arxiv.org/abs/2608.03451) / [DSAgentBench](https://arxiv.org/abs/2608.10366) → [Data Exploration Benchmark](https://arxiv.org/abs/2608.16045) / [WarehouseReliabilityBench](https://arxiv.org/abs/2608.09254) / [data-eng-bench](https://github.com/Snowflake-Labs/data-eng-bench)

<a id="all-benchmarks"></a>
## 按领域查看全部 Benchmark

以下是 registry 中的全部 105 个基准。这里的表格是 README 的一等阅读界面，不因为长度而下沉到 Library。

### Agent Memory

<!-- TABLE-FIRST:AREA:agent-memory:START -->
| 阶段 | Benchmark | 时间 | 考察内容 |
|---|---|---:|---|
| 🌱 前身 | [Beyond Goldfish Memory](https://aclanthology.org/2022.acl-long.356/) <!-- benchmark-id:beyond-goldfish-memory --> | 2022-05 | 多次真人聊天之间的开放域长期记忆与前后自洽。 |
| 🧱 基石 | [LoCoMo](https://aclanthology.org/2024.acl-long.747/) <!-- benchmark-id:locomo --> | 2024-08 | 超长多会话对话中的 QA、事件总结和多模态对话生成。 |
| 🧱 基石 | [LongMemEval](https://arxiv.org/abs/2410.10813) <!-- benchmark-id:longmemeval --> | 2024-10 | 长期助手历史中的信息抽取、跨会话推理、时间推理、知识更新和拒答。 |
| ↗ 过渡 | [MemBench](https://arxiv.org/abs/2506.21605) <!-- benchmark-id:membench --> | 2025-06 | 事实记忆与反思记忆、参与者与观察者场景，以及效果、效率和容量。 |
| ↗ 过渡 | [MemoryAgentBench](https://arxiv.org/abs/2507.05257) <!-- benchmark-id:memoryagentbench --> | 2025-07 | 增量多轮交互中的检索、测试时学习、长程理解和选择性遗忘。 |
| ↗ 过渡 | [BEAM](https://arxiv.org/abs/2510.27246) <!-- benchmark-id:beam --> | 2025-10 | 百万到千万 token 的连贯对话记忆。 |
| 🔭 前沿 | [RealMem](https://aclanthology.org/2026.findings-acl.703/) <!-- benchmark-id:realmem --> | 2026-01 | 跨会话、目标和产物持续变化的项目型长期记忆。 |
| 🔭 前沿 | [CAME-Bench](https://aclanthology.org/2026.findings-acl.584/) <!-- benchmark-id:came-bench --> | 2026-01-15 | 相同实体在不同目标段反复出现时，能否找回与当前意图相符的证据。 |
| 🔭 前沿 | [AMA-Bench](https://arxiv.org/abs/2602.22769) <!-- benchmark-id:ama-bench --> | 2026-02 | 真实和可扩展合成的智能体—环境轨迹上的长程记忆。 |
| 🔭 前沿 | [StructMemEval](https://arxiv.org/abs/2602.11243) <!-- benchmark-id:structmemeval --> | 2026-02 | 智能体能否维护账本、列表、树等符合任务需要的记忆结构。 |
| 🔭 前沿 | [MemGUI-Bench](https://arxiv.org/abs/2602.06075) <!-- benchmark-id:memgui-bench --> | 2026-02-03 | 移动端操作中的跨步骤保持、跨应用迁移、跨会话学习和失败恢复。 |
| 🔭 前沿 | [MemoryArena](https://arxiv.org/abs/2602.16313) <!-- benchmark-id:memoryarena --> | 2026-02-18 | 在跨会话的智能体—环境循环中，用早期行动与反馈指导后续行动。 |
| 🔭 前沿 | [LifeBench](https://arxiv.org/abs/2603.03781) <!-- benchmark-id:lifebench --> | 2026-03 | 多源长期轨迹中的事件、语义、习惯和程序性记忆。 |
| 🔭 前沿 | [ImplicitMemBench](https://aclanthology.org/2026.acl-long.1301/) <!-- benchmark-id:implicitmembench --> | 2026-04-09 | 干扰之后，模型能否在首次尝试中自动表现出已学程序、启动效应或条件联结。 |
| 🔭 前沿 | [MemEvoBench](https://arxiv.org/abs/2604.15774) <!-- benchmark-id:memevobench --> | 2026-04-17 | 误导性记忆、噪声工具结果和偏置反馈在多轮写回后会不会使行为逐步失去安全性。 |
| 🔭 前沿 | [LongMemEval-V2](https://arxiv.org/abs/2605.12493) <!-- benchmark-id:longmemeval-v2 --> | 2026-05 | 大量网页智能体轨迹中的环境状态、操作流程和易错点。 |
| 🔭 前沿 | [MedMemoryBench](https://arxiv.org/abs/2605.11814) <!-- benchmark-id:medmemorybench --> | 2026-05-12 | 在持续增长的医疗对话中追踪病情、时间变化和复杂临床信息，并观察记忆饱和。 |
| 🔭 前沿 | [GroupMemBench](https://arxiv.org/abs/2605.14498) <!-- benchmark-id:groupmembench --> | 2026-05-14 | 多人群聊中的说话者信念、群体动态、术语差异和面向不同受众的表达。 |
| 🔭 前沿 | [MemEye](https://arxiv.org/abs/2605.15128) <!-- benchmark-id:memeye --> | 2026-05-14 | 细粒度视觉证据、视觉状态变化，以及纯文本捷径检查。 |
| 🔭 前沿 | [MEMLENS](https://arxiv.org/abs/2605.14906) <!-- benchmark-id:memlens --> | 2026-05-14 | 在 32K 到 256K 的多模态多会话历史中进行提取、更新、时间推理和拒答。 |
| 🔭 前沿 | [EvoMemBench](https://arxiv.org/abs/2605.18421) <!-- benchmark-id:evomembench --> | 2026-05-18 | 在回合内与跨回合、知识型与执行型两条轴上统一比较记忆系统。 |
| 🔭 前沿 | [WorldMemArena](https://arxiv.org/abs/2605.29341) <!-- benchmark-id:worldmemarena --> | 2026-05-28 | 从多模态观察、行动和反馈中写入、维护、检索并使用不断变化的世界状态。 |
| 🔭 前沿 | [LifeSide](https://arxiv.org/abs/2606.04660) <!-- benchmark-id:lifeside --> | 2026-06 | 跨会话记忆、用户理解、隐私控制，以及情绪与环境的互动。 |
| 🔭 前沿 | [GateMem](https://arxiv.org/abs/2606.18829) <!-- benchmark-id:gatemem --> | 2026-06-17 | 多人共享记忆能否同时保持可用、阻止越权泄露并执行删除请求。 |
| 🔭 前沿 | [DynamicMem](https://arxiv.org/abs/2606.22877) <!-- benchmark-id:dynamicmem --> | 2026-06-22 | 从十五个月、多个应用的零散行为中推断并更新用户属性、习惯和偏好。 |
| 🔭 前沿 | [MEMPROBE](https://arxiv.org/abs/2606.24595) <!-- benchmark-id:memprobe --> | 2026-06-23 | 普通协助结束后，能否从智能体留下的记忆产物中恢复隐藏的用户状态。 |
| 🔭 前沿 | [LoCoMo-Plus](https://aclanthology.org/2026.acl-long.1150/) <!-- benchmark-id:locomo-plus --> | 2026-07 | 后续问题没有复述旧约束时，能否继续正确应用它。 |
| 🔭 前沿 | [Mem-Gallery](https://aclanthology.org/2026.acl-long.1892/) <!-- benchmark-id:mem-gallery --> | 2026-07 | 多模态长期对话中的记忆抽取、适应、推理和知识管理。 |
| 🔭 前沿 | [Mem2ActBench](https://aclanthology.org/2026.acl-long.370/) <!-- benchmark-id:mem2actbench --> | 2026-07 | 长期记忆是否会影响工具选择和参数填写。 |
| 🔭 前沿 | [PerMemSafe](https://aclanthology.org/2026.findings-acl.320/) <!-- benchmark-id:permemsafe --> | 2026-07 | 能否从长期历史中识别隐含的个体风险，并在风险缓解后及时更新判断。 |
| 🔭 前沿 | [MemFuseBench](https://arxiv.org/abs/2608.18704) <!-- benchmark-id:memfusebench --> | 2026-07-21 | 跨异构事件流的来源连接、因果融合、冲突裁决与溯源记忆基准。 |
| 🔭 前沿 | [InMind](https://arxiv.org/abs/2607.24368) <!-- benchmark-id:inmind --> | 2026-07-27 | 旧事实与新问题词义相远、只有借助常识才能建立联系时，记忆能否被正确调出并应用。 |
| 🔭 前沿 | [PAST-Bench](https://arxiv.org/abs/2608.04003) <!-- benchmark-id:past-bench --> | 2026-08-04 | 通过配对持久状态控制，检验跨 episode 经验是否因果改善后续可执行工作的基准。 |
| 🔭 前沿 | [SP-Mem Privacy-Aware Memory Benchmark](https://arxiv.org/abs/2608.16551) <!-- benchmark-id:sp-mem --> | 2026-08-17 | 联合测量回答质量、个性化、同意处理、精确值暴露与成本的隐私感知记忆基准。 |<!-- TABLE-FIRST:AREA:agent-memory:END -->

### RAG / Agentic Retrieval

<!-- TABLE-FIRST:AREA:rag:START -->
| 阶段 | Benchmark | 时间 | 考察内容 |
|---|---|---:|---|
| 🌱 前身 | [HotpotQA](https://aclanthology.org/D18-1259/) <!-- benchmark-id:hotpotqa --> | 2018-10 | 从多个 Wikipedia 文档中找证据、组合推理，并标出支撑事实。 |
| 🧱 基石 | [KILT](https://arxiv.org/abs/2009.02252) <!-- benchmark-id:kilt --> | 2020-09 | 在同一份 Wikipedia 快照上评测多种知识密集任务，同时检查答案和证据来源。 |
| 🧱 基石 | [BEIR](https://arxiv.org/abs/2104.08663) <!-- benchmark-id:beir --> | 2021-04 | 检索器在不同领域和任务上的零样本泛化。 |
| 🧱 基石 | [RGB](https://arxiv.org/abs/2309.01431) <!-- benchmark-id:rgb --> | 2023-09 | RAG 面对噪声、不可回答问题、信息整合和反事实材料时的表现。 |
| ↗ 过渡 | [MultiHop-RAG](https://arxiv.org/abs/2401.15391) <!-- benchmark-id:multihop-rag --> | 2024-01 | 在 RAG 流程中检索多份支撑证据并完成多跳推理。 |
| ↗ 过渡 | [RAGTruth](https://arxiv.org/abs/2401.00396) <!-- benchmark-id:ragtruth --> | 2024-01 | RAG 输出中的样例级、词级幻觉和依据错误。 |
| ↗ 过渡 | [CRAG](https://arxiv.org/abs/2406.04744) <!-- benchmark-id:crag --> | 2024-06 | 动态事实、长尾实体，以及网页和知识图谱上的事实型 RAG。 |
| ↗ 过渡 | [BRIGHT](https://arxiv.org/abs/2407.12883) <!-- benchmark-id:bright --> | 2024-07 | 相关性判断本身需要推理的真实查询。 |
| ↗ 过渡 | [RAGBench](https://arxiv.org/abs/2407.11005) <!-- benchmark-id:ragbench --> | 2024-07 | 跨行业场景的检索与生成质量标签，以及 RAG 评判器。 |
| ↗ 过渡 | [BrowseComp](https://arxiv.org/abs/2504.12516) <!-- benchmark-id:browsecomp --> | 2025-04 | 为寻找隐蔽答案持续浏览实时网页、改写查询并导航。 |
| ↗ 过渡 | [T²-RAGBench](https://aclanthology.org/2026.eacl-long.8/) <!-- benchmark-id:t2-ragbench --> | 2025-05-14 | 考察真实财务报告中的文本与表格检索，以及检索后的数值推理。 |
| ↗ 过渡 | [DeepResearch Bench](https://arxiv.org/abs/2506.11763) <!-- benchmark-id:deepresearch-bench --> | 2025-06 | 多步网页研究、证据收集、引用质量和长篇报告生成。 |
| ↗ 过渡 | [BrowseComp-Plus](https://arxiv.org/abs/2508.06600) <!-- benchmark-id:browsecomp-plus --> | 2025-08 | 在固定语料上进行深度研究，并分析检索贡献和答案准确率。 |
| 🔭 前沿 | [RAGCap-Bench](https://arxiv.org/abs/2510.13910) <!-- benchmark-id:ragcap-bench --> | 2025-10 | 分别评测 Agentic RAG 中的规划、检索和中间推理能力。 |
| 🔭 前沿 | [LIT-RAGBench](https://arxiv.org/abs/2603.06198) <!-- benchmark-id:lit-ragbench --> | 2025-10-22 | 在已给定检索上下文时，考察生成器的逻辑、整合、表格、推理与拒答能力。 |
| 🔭 前沿 | [AgenticRAGTracer](https://arxiv.org/abs/2602.19127) <!-- benchmark-id:agenticragtracer --> | 2026-02 | 对多步检索与推理逐跳核验，并检查步骤分配。 |
| 🔭 前沿 | [SAGE](https://arxiv.org/abs/2602.05975) <!-- benchmark-id:sage --> | 2026-02-05 | 考察深度研究智能体在受控科学论文库中的定向找文与开放式文献搜集。 |
| 🔭 前沿 | [GISA](https://arxiv.org/abs/2602.08543) <!-- benchmark-id:gisa --> | 2026-02-06 | 考察真实信息需求下的搜索规划、纵向推理、横向汇总和结构化作答。 |
| 🔭 前沿 | [MC-Search](https://arxiv.org/abs/2603.00873) <!-- benchmark-id:mc-search --> | 2026-02-22 | 考察多模态搜索规划、模态选择、逐跳证据检索和长链推理一致性。 |
| 🔭 前沿 | [MTRAG-UN](https://aclanthology.org/2026.findings-acl.503/) <!-- benchmark-id:mtrag-un --> | 2026-02-26 | 考察多轮 RAG 对不可回答、信息不足、非独立问题和含糊回复的处理。 |
| 🔭 前沿 | [AutoResearchBench](https://arxiv.org/abs/2604.25256) <!-- benchmark-id:autoresearchbench --> | 2026-04-01 | 考察科学文献中的目标论文追踪、条件约束、开放集合搜集和停止判断。 |
| 🔭 前沿 | [LeakDojo](https://aclanthology.org/2026.findings-acl.287/) <!-- benchmark-id:leakdojo --> | 2026-04-07 | 考察攻击者从 RAG 数据库抽取文本内容的能力，以及不同管线和防御下的泄露风险。 |
| 🔭 前沿 | [EnterpriseRAG-Bench](https://arxiv.org/abs/2605.05253) <!-- benchmark-id:enterpriserag-bench --> | 2026-04-14 | 考察企业式知识库中的检索、多文档推理、冲突处理、完整性和无答案识别。 |
| 🔭 前沿 | [MERRIN](https://arxiv.org/abs/2604.13418) <!-- benchmark-id:merrin --> | 2026-04-15 | 考察智能体在嘈杂网络中自主选择模态、检索多模态证据并进行多跳推理。 |
| 🔭 前沿 | [MuDABench](https://aclanthology.org/2026.findings-acl.341/) <!-- benchmark-id:mudabench --> | 2026-04-19 | 考察大规模财务文档集合中的信息抽取、跨文档聚合和定量分析。 |
| 🔭 前沿 | [Bright-Pro](https://aclanthology.org/2026.acl-long.1705/) <!-- benchmark-id:bright-pro --> | 2026-04-30 | 考察推理密集型检索、推理要点覆盖，以及检索器在静态与智能体搜索中的实际效用。 |
| 🔭 前沿 | [SGR-Bench](https://arxiv.org/abs/2605.22219) <!-- benchmark-id:sgr-bench --> | 2026-05 | 在证据受站点筛选、层级、范围或视图状态控制时完成搜索。 |
| 🔭 前沿 | [ScholarQuest](https://arxiv.org/abs/2606.20235) <!-- benchmark-id:scholarquest --> | 2026-05-19 | 考察智能体按研究意图迭代检索论文、扩展引文和控制结果范围。 |
| 🔭 前沿 | [LiveBrowseComp](https://arxiv.org/abs/2605.28721) <!-- benchmark-id:livebrowsecomp --> | 2026-05-27 | 考察智能体能否检索近期、低显著性的网络事实，而非只验证模型已有知识。 |
| 🔭 前沿 | [EvoBrowseComp](https://arxiv.org/abs/2606.13120) <!-- benchmark-id:evobrowsecomp --> | 2026-06-11 | 考察英语和中文智能体对持续变化网络知识的广度搜索与多步推理。 |
| 🔭 前沿 | [LoHoSearch](https://arxiv.org/abs/2606.12837) <!-- benchmark-id:lohosearch --> | 2026-06-11 | 考察超大候选空间、复杂约束结构、长程搜索和上下文管理。 |
| 🔭 前沿 | [WANDR](https://arxiv.org/abs/2608.14747) <!-- benchmark-id:wandr --> | 2026-07-14 | 面向实时网页 wide-and-deep 记录收集的基准，包含分层任务和无需穷举金标的逐条核验。 |
| 🔭 前沿 | [VAKRA](https://arxiv.org/abs/2608.12282) <!-- benchmark-id:vakra --> | 2026-08 | 组合调用 API、检索文档、完成多跳推理，并遵守工具策略。 |
| 🔭 前沿 | [MAPLE](https://arxiv.org/abs/2608.15624) <!-- benchmark-id:maple --> | 2026-08-04 | 测量同一论文能否在动机、方法与结果等多个 aspect 下持续被找回的科学检索基准。 |
| 🔭 前沿 | [SearchAuditBench](https://arxiv.org/abs/2608.05212) <!-- benchmark-id:searchauditbench --> | 2026-08-05 | 考察审计模型能否在超长搜索轨迹中定位错误、归因根因并生成可执行修复。 |
| 🔭 前沿 | [DAS-Bench / DAS-Eval](https://arxiv.org/abs/2608.18034) <!-- benchmark-id:das-bench --> | 2026-08-07 | 对文献覆盖、taxonomy、claim、citation、discourse 与渲染成品质量评分的学术综述基准及评测器。 |
| 🔭 前沿 | [The Recall Trap](https://arxiv.org/abs/2608.14838) <!-- benchmark-id:recall-trap --> | 2026-08-10 | 有效性审计：在固定槽位代码检索协议下，更高 file recall 可能降低下游修复成功率。 |
| 🔭 前沿 | [The Commercial Tax](https://arxiv.org/abs/2608.16096) <!-- benchmark-id:commercial-tax --> | 2026-08-17 | 把原始 embedder 分数绑定到许可、query format、索引构造与部署成本的检索复现性审计。 |
| 🔭 前沿 | [VisDocAgentBench](https://arxiv.org/abs/2608.17889) <!-- benchmark-id:visdocagentbench --> | 2026-08-18 | 在统一页面排序协议下比较静态 ranker 与迭代视觉/OCR agent 的视觉文档检索基准。 |<!-- TABLE-FIRST:AREA:rag:END -->

### Data Agents

<!-- TABLE-FIRST:AREA:data-agent:START -->
| 阶段 | Benchmark | 时间 | 考察内容 |
|---|---|---:|---|
| 🌱 前身 | [WikiSQL](https://arxiv.org/abs/1709.00103) <!-- benchmark-id:wikisql --> | 2017-08 | 根据自然语言问题，在单个 Wikipedia 表格上生成可执行 SQL。 |
| 🧱 基石 | [Spider](https://aclanthology.org/D18-1425/) <!-- benchmark-id:spider --> | 2018-10 | 在未见过的 schema 上生成复杂的多表 SQL，并测试跨领域泛化。 |
| 🧱 基石 | [DS-1000](https://arxiv.org/abs/2211.11501) <!-- benchmark-id:ds-1000 --> | 2022-11 | 使用七类 Python 数据科学库生成代码，并通过执行检查正确性。 |
| ↗ 过渡 | [BIRD](https://arxiv.org/abs/2305.03111) <!-- benchmark-id:bird --> | 2023-05 | 处理大型真实数据库中的脏值、外部知识、复杂 SQL 和执行效率。 |
| ↗ 过渡 | [MLAgentBench](https://arxiv.org/abs/2310.03302) <!-- benchmark-id:mlagentbench --> | 2023-10 | 反复设计、运行、检查并改进机器学习实验。 |
| ↗ 过渡 | [InsightBench](https://arxiv.org/abs/2407.06423) <!-- benchmark-id:insightbench --> | 2024-07 | 从提出问题、探索性分析到形成洞见和行动建议的业务分析。 |
| ↗ 过渡 | [DA-Code](https://aclanthology.org/2024.emnlp-main.748/) <!-- benchmark-id:da-code --> | 2024-10 | 在真实数据上完成数据整理、EDA、机器学习规划和可执行代码生成。 |
| ↗ 过渡 | [Spider 2.0](https://arxiv.org/abs/2411.07763) <!-- benchmark-id:spider-2 --> | 2024-11 | 在巨大 schema、多种 SQL 方言、元数据、代码库和云数据库中完成企业 SQL 工作流。 |
| ↗ 过渡 | [DataSciBench](https://arxiv.org/abs/2502.13897) <!-- benchmark-id:datascibench --> | 2025-02 | 覆盖多类数据科学任务，并为不同任务配置程序化指标和人工核验答案。 |
| 🔭 前沿 | [LiveSQLBench](https://livesqlbench.ai/) <!-- benchmark-id:livesqlbench --> | 2025-05-28 | 在持续演化的工业数据库与分层知识库上执行查询和管理类 SQL，并适应业务规则漂移。 |
| ↗ 过渡 | [KramaBench](https://arxiv.org/abs/2506.06541) <!-- benchmark-id:kramabench --> | 2025-06-06 | 在杂乱异构数据湖上完成发现、清洗、整合、分析与建模的端到端管线。 |
| ↗ 过渡 | [DABstep](https://arxiv.org/abs/2506.23719) <!-- benchmark-id:dabstep --> | 2025-06-30 | 结合交易数据、业务文档与领域规则完成多步金融分析。 |
| 🔭 前沿 | [FDABench](https://arxiv.org/abs/2509.02473) <!-- benchmark-id:fdabench --> | 2025-09 | 在结构化数据、非结构化材料、网页和多模态来源上完成多源分析。 |
| ↗ 过渡 | [AgentDS](https://arxiv.org/abs/2603.19005) <!-- benchmark-id:agentds --> | 2025-10-18 | 在六个行业的领域预测任务上比较纯 AI 与人机协作方案。 |
| 🔭 前沿 | [DDR-Bench](https://arxiv.org/abs/2602.02039) <!-- benchmark-id:ddr-bench --> | 2025-11-30 | 只给实体和数据库元数据，要求智能体自主设定目标、探索、形成假设并发现可核验洞见。 |
| 🔭 前沿 | [DAComp](https://arxiv.org/abs/2512.04324) <!-- benchmark-id:dacomp --> | 2025-12 | 代码仓库级数据工程和开放式数据分析。 |
| 🔭 前沿 | [DSAEval](https://arxiv.org/abs/2601.13591) <!-- benchmark-id:dsaeval --> | 2026-01-20 | 在表格、图像与文本数据上进行连续多轮数据科学项目，并综合评价推理、代码和结果。 |
| 🔭 前沿 | [DSGym](https://arxiv.org/abs/2601.16344) <!-- benchmark-id:dsgym --> | 2026-01-22 | 在统一、隔离、可执行环境中评测经捷径过滤的数据分析、预测与领域任务。 |
| 🔭 前沿 | [DARE-bench](https://arxiv.org/abs/2602.24288) <!-- benchmark-id:dare-bench --> | 2026-02-27 | 用可验证真值同时评估机器学习建模效果与对指定数据科学流程的遵循。 |
| 🔭 前沿 | [Data Agent Benchmark (DAB)](https://arxiv.org/abs/2603.20576) <!-- benchmark-id:data-agent-benchmark --> | 2026-03 | 跨多个 DBMS 完成数据集成、转换、分析和可执行核验。 |
| 🔭 前沿 | [TML-Bench](https://arxiv.org/abs/2603.05764) <!-- benchmark-id:tml-bench --> | 2026-03-05 | 在固定时间预算和隐藏标签下，产出有效且有竞争力的表格机器学习提交。 |
| 🔭 前沿 | [AgentFuel](https://arxiv.org/abs/2603.12483) <!-- benchmark-id:agentfuel --> | 2026-03-12 | 面向具体领域的时序对话智能体功能测试，重点覆盖有状态与事故型查询。 |
| 🔭 前沿 | [DataClawBench](https://arxiv.org/abs/2605.02503) <!-- benchmark-id:dataclawbench --> | 2026-05-04 | 在几乎没有先验提示时，自主探索陌生、含噪、跨域金融数据并形成可验证结论。 |
| 🔭 前沿 | [IRTS-ToolBench](https://arxiv.org/abs/2606.15107) <!-- benchmark-id:irts-toolbench --> | 2026-06-13 | 在异步、缺失且采样频率不一的非规则时间序列上选择工具并完成可核验问答。 |
| 🔭 前沿 | [StatABench](https://arxiv.org/abs/2606.22977) <!-- benchmark-id:statabench --> | 2026-06-22 | 同时评估统计知识、工具选择与参数设置，以及开放式建模和报告。 |
| 🔭 前沿 | [AgenticDataBench](https://arxiv.org/abs/2607.01647) <!-- benchmark-id:agenticdatabench --> | 2026-07 | 用细粒度技能分类检查真实数据科学工作流的覆盖情况。 |
| 🔭 前沿 | [CausalDS](https://arxiv.org/abs/2607.08093) <!-- benchmark-id:causalds --> | 2026-07-09 | 在可执行数据科学环境中覆盖因果预测、识别、效应估计、反事实、不确定性与弃答。 |
| 🔭 前沿 | [data-eng-bench](https://github.com/Snowflake-Labs/data-eng-bench) <!-- benchmark-id:data-eng-bench --> | 2026-07-29 | 面向仓库规模 dbt 转换的可执行数据工程基准，在 DuckDB 与 Snowflake 上做隐藏行级核验。 |
| 🔭 前沿 | [DataSpace](https://arxiv.org/abs/2608.03451) <!-- benchmark-id:dataspace --> | 2026-08 | 在混合数据库、文件、文档和多媒体的工作区中完成可验证分析。 |
| 🔭 前沿 | [DSAgentBench](https://arxiv.org/abs/2608.10366) <!-- benchmark-id:dsagentbench --> | 2026-08 | 使用笔记本、IDE、终端、浏览器和数据库完成完整数据科学工作流。 |
| 🔭 前沿 | [WarehouseReliabilityBench](https://arxiv.org/abs/2608.09254) <!-- benchmark-id:warehouse-reliability-bench --> | 2026-08-10 | 面对语义歧义、不可回答、模式漂移和对抗输入时，返回业务真值或正确地澄清、弃答、拒答。 |
| 🔭 前沿 | [Data Exploration Benchmark](https://arxiv.org/abs/2608.16045) <!-- benchmark-id:data-exploration-benchmark --> | 2026-08-17 | 在下游分析前，构建包含逻辑表、列语义、键关系和质量信号的结构化数据理解产物。 |<!-- TABLE-FIRST:AREA:data-agent:END -->

## 目前仍然测不好的重要问题

| 还缺什么 | 为什么重要 |
|---|---|
| **真实用户的长期效应** | 用户偏好、项目状态和延迟后果都在变化，很难压缩成静态 QA。 |
| **不可逆操作与权限** | 工具可以花钱、改写状态或使用过期权限时，只做到“检索正确”远远不够。 |
| **全生命周期成本** | 建索引、写记忆、重试、控制器调用、工具延迟和重新获取信息的成本经常被拆开报告或直接省略。 |
| **变化中的生产环境** | 网页、schema、工具和运行环境的变化可能主导结果，即使模型本身没有变。 |
| **业务语义正确性** | SQL 或代码可以执行，不代表它回答了正确的业务问题；追问和拒答也很少有干净的评价目标。 |

<a id="reading-paths"></a>
## 阅读路径

| 你想理解什么 | 从这里开始 | 然后进入 |
|---|---|---|
| **记忆评测如何从回忆走向行动与治理？** | Multi-Session Chat → LoCoMo / LongMemEval → MemoryArena / WorldMemArena → GateMem / PerMemSafe / InMind | [Agent Memory Radar](https://github.com/H20Zhang/Agent-Memory-Radar#field-map) |
| **检索评测如何变成实时、可审计的搜索？** | BEIR / BRIGHT → BrowseComp / LiveBrowseComp → Bright-Pro / LoHoSearch / SearchAuditBench / VAKRA → MAPLE / VisDocAgentBench / WANDR | [Agentic RAG Radar](https://github.com/H20Zhang/Agentic-RAG-Radar#field-map) |
| **数据智能体评测如何从 SQL/代码走到可靠的数据工作？** | Spider / DS-1000 → KramaBench / DABstep → DataClawBench / DSGym → DataSpace / DSAgentBench / WarehouseReliabilityBench | [Data Agent Radar](https://github.com/H20Zhang/Data-Agent-Radar#field-map) |

<a id="library"></a>
## Benchmark Library

- **[按时间、领域、演化关系和评测维度继续浏览](library/README.md)**
- [Canonical registry](data/benchmarks.json)
- [Research compactions](digests/README.md)

这里整理“测什么、为什么这样测”；具体方法和系统放在三个专题 Radar 中，避免重复维护同一份综述。

[English](README.en.md) · [Curation](CURATION.md) · [Schema](SCHEMA.md)
