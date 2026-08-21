# Agent Benchmark Radar

**中文** | [English](README.en.md)

**整个 Research Radar family 的默认入口，也是横向 evaluation layer。**

先从这里理解：**Agent Memory、Agentic RAG、Data Agent 分别正在被要求做什么，这些 evaluation target 为什么一路演化到今天，以及一个 benchmark score 到底能支持什么结论。** 然后再进入对应 domain radar 看方法与系统。

**研究 Radar：** [Agent Memory](https://github.com/H20Zhang/Agent-Memory-Radar#field-map) · [Agentic RAG](https://github.com/H20Zhang/Agentic-RAG-Radar#field-map) · [Data Agent](https://github.com/H20Zhang/Data-Agent-Radar#field-map)

[30 秒：最近半年表格](#release-timeline) · [3 分钟：7/30 天变化](#periods) · [5 分钟：领域地图](#field-map) · [全部 Benchmark 表](#all-benchmarks) · [阅读路径](#reading-paths) · [Benchmark Library](#library)

<!-- compatibility: [30 秒：最新时间线](#timeline) · [3 分钟：7/30 天变化](#periods) · [5 分钟：领域地图](#field-map) · [15 分钟：阅读路径](#reading-paths) · [浏览全部](#library) -->

> **比较规则：** 如果 model、accessible state、tool interface、prompt/hints、retry、stopping rule、evaluator 与关键 resource budget 没有充分匹配，那么 leaderboard 上更高的 score 首先只是 **system-level evidence**，不能直接归因给某个 component。

最后更新：**2026-08-20**

<a id="release-timeline"></a>
## 最近半年 Benchmark 时间线

这里按 benchmark / paper 的**原始发布时间**排序，而不是按 Radar 什么时候收录。窗口随 registry 中最近的核验日期滚动，向前覆盖六个月；只有月份精度的记录保留真实月份。表中不做精选，窗口内的基准全部列出。

<!-- TABLE-FIRST:RECENT:START -->
| 时间 | 方向 | Benchmark | 考察内容 | 相较以往 |
|---|---|---|---|---|
| 2026-08-17 | Data Agent | [Data Exploration Benchmark](https://arxiv.org/abs/2608.16045) <!-- benchmark-id:data-exploration-benchmark --> | 在下游分析前，构建包含逻辑表、列语义、键关系和质量信号的结构化数据理解产物。 | 把通常隐含的数据探索阶段从最终答案的前置假设变成可独立评分、可验证下游价值的对象。 |
| 2026-08-10 | Data Agent | [WarehouseReliabilityBench](https://arxiv.org/abs/2608.09254) <!-- benchmark-id:warehouse-reliability-bench --> | 面对语义歧义、不可回答、模式漂移和对抗输入时，返回业务真值或正确地澄清、弃答、拒答。 | 从“SQL 能运行且结果匹配”转向“业务含义正确，并在不该给数字时不虚假成功”。 |
| 2026-08-05 | RAG | [SearchAuditBench](https://arxiv.org/abs/2608.05212) <!-- benchmark-id:searchauditbench --> | 考察审计模型能否在超长搜索轨迹中定位错误、归因根因并生成可执行修复。 | 从最终答案成败推进到专家标注的关键步骤、六类根因和修复后恢复评测。 |
| 2026-08 | Data Agent | [DataSpace](https://arxiv.org/abs/2608.03451) <!-- benchmark-id:dataspace --> | 在混合数据库、文件、文档和多媒体的工作区中完成可验证分析。 | 寻找异构证据和核验完整结果成为一项统一任务。 |
| 2026-08 | Data Agent | [DSAgentBench](https://arxiv.org/abs/2608.10366) <!-- benchmark-id:dsagentbench --> | 使用笔记本、IDE、终端、浏览器和数据库完成完整数据科学工作流。 | 评测进入真实计算机环境，要求多阶段、多工具执行能够可靠衔接。 |
| 2026-08 | RAG | [VAKRA](https://arxiv.org/abs/2608.12282) <!-- benchmark-id:vakra --> | 组合调用 API、检索文档、完成多跳推理，并遵守工具策略。 | 跨来源依据、实际执行和策略一致性出现在同一条轨迹中。 |
| 2026-07-27 | Agent Memory | [InMind](https://arxiv.org/abs/2607.24368) <!-- benchmark-id:inmind --> | 旧事实与新问题词义相远、只有借助常识才能建立联系时，记忆能否被正确调出并应用。 | 用成对对照把存储失败、知识缺失、检索路由失败和应用失败分开。 |
| 2026-07-09 | Data Agent | [CausalDS](https://arxiv.org/abs/2607.08093) <!-- benchmark-id:causalds --> | 在可执行数据科学环境中覆盖因果预测、识别、效应估计、反事实、不确定性与弃答。 | 把数据智能体评测从相关性和预测拓展到 Pearl 三阶因果推理及“无法作答”的识别。 |
| 2026-07 | Data Agent | [AgenticDataBench](https://arxiv.org/abs/2607.01647) <!-- benchmark-id:agenticdatabench --> | 用细粒度技能分类检查真实数据科学工作流的覆盖情况。 | 除了总成功率，还能审计这套基准覆盖了哪些技能。 |
| 2026-07 | Agent Memory | [LoCoMo-Plus](https://aclanthology.org/2026.acl-long.1150/) <!-- benchmark-id:locomo-plus --> | 后续问题没有复述旧约束时，能否继续正确应用它。 | 目标从显式事实召回转向用户目标、价值和约束的一致应用。 |
| 2026-07 | Agent Memory | [Mem-Gallery](https://aclanthology.org/2026.acl-long.1892/) <!-- benchmark-id:mem-gallery --> | 多模态长期对话中的记忆抽取、适应、推理和知识管理。 | 视觉保留、多模态推理和记忆组织被放进同一套评测。 |
| 2026-07 | Agent Memory | [Mem2ActBench](https://aclanthology.org/2026.acl-long.370/) <!-- benchmark-id:mem2actbench --> | 长期记忆是否会影响工具选择和参数填写。 | 记忆对行动的作用可以直接评分，而不再只通过问答间接判断。 |
| 2026-07 | Agent Memory | [PerMemSafe](https://aclanthology.org/2026.findings-acl.320/) <!-- benchmark-id:permemsafe --> | 能否从长期历史中识别隐含的个体风险，并在风险缓解后及时更新判断。 | 把用户状态记忆扩展到随时间变化的个性化安全与有用性权衡。 |
| 2026-06-23 | Agent Memory | [MEMPROBE](https://arxiv.org/abs/2606.24595) <!-- benchmark-id:memprobe --> | 普通协助结束后，能否从智能体留下的记忆产物中恢复隐藏的用户状态。 | 由下游回答间接推断记忆，转为直接审计记忆产物本身。 |
| 2026-06-22 | Agent Memory | [DynamicMem](https://arxiv.org/abs/2606.22877) <!-- benchmark-id:dynamicmem --> | 从十五个月、多个应用的零散行为中推断并更新用户属性、习惯和偏好。 | 把用户记忆推进到百万 token、长期漂移和跨应用隐式证据。 |
| 2026-06-22 | Data Agent | [StatABench](https://arxiv.org/abs/2606.22977) <!-- benchmark-id:statabench --> | 同时评估统计知识、工具选择与参数设置，以及开放式建模和报告。 | 把封闭式统计问答和工具调用与端到端开放建模纳入同一套能力坐标。 |
| 2026-06-17 | Agent Memory | [GateMem](https://arxiv.org/abs/2606.18829) <!-- benchmark-id:gatemem --> | 多人共享记忆能否同时保持可用、阻止越权泄露并执行删除请求。 | 长期记忆由单用户私有存储扩展到带权限和遗忘义务的共享治理。 |
| 2026-06-13 | Data Agent | [IRTS-ToolBench](https://arxiv.org/abs/2606.15107) <!-- benchmark-id:irts-toolbench --> | 在异步、缺失且采样频率不一的非规则时间序列上选择工具并完成可核验问答。 | 把规则采样这一默认假设移除，直接测量非规则性处理与工具落地推理。 |
| 2026-06-11 | RAG | [EvoBrowseComp](https://arxiv.org/abs/2606.13120) <!-- benchmark-id:evobrowsecomp --> | 考察英语和中文智能体对持续变化网络知识的广度搜索与多步推理。 | 引入可自动更新的双语实时网络问题生成流程，以降低静态测试集污染。 |
| 2026-06-11 | RAG | [LoHoSearch](https://arxiv.org/abs/2606.12837) <!-- benchmark-id:lohosearch --> | 考察超大候选空间、复杂约束结构、长程搜索和上下文管理。 | 用知识图谱系统控制搜索空间与结构复杂度，而非仅依赖人工主观设难。 |
| 2026-06 | Agent Memory | [LifeSide](https://arxiv.org/abs/2606.04660) <!-- benchmark-id:lifeside --> | 跨会话记忆、用户理解、隐私控制，以及情绪与环境的互动。 | 记忆开始与持续用户建模、隐私边界和环境情境一起考察。 |
| 2026-05-28 | Agent Memory | [WorldMemArena](https://arxiv.org/abs/2605.29341) <!-- benchmark-id:worldmemarena --> | 从多模态观察、行动和反馈中写入、维护、检索并使用不断变化的世界状态。 | 把记忆拆成可诊断的写入、维护、检索和使用四个阶段。 |
| 2026-05-27 | RAG | [LiveBrowseComp](https://arxiv.org/abs/2605.28721) <!-- benchmark-id:livebrowsecomp --> | 考察智能体能否检索近期、低显著性的网络事实，而非只验证模型已有知识。 | 使用构建前 90 天内的事实，并以闭卷和移除答案来源实验区分发现与验证。 |
| 2026-05-19 | RAG | [ScholarQuest](https://arxiv.org/abs/2606.20235) <!-- benchmark-id:scholarquest --> | 考察智能体按研究意图迭代检索论文、扩展引文和控制结果范围。 | 把学术搜索定义为集合检索，并提供统一的大规模后端、意图切片和效率指标。 |
| 2026-05-18 | Agent Memory | [EvoMemBench](https://arxiv.org/abs/2605.18421) <!-- benchmark-id:evomembench --> | 在回合内与跨回合、知识型与执行型两条轴上统一比较记忆系统。 | 把分散的问答、工具、搜索和具身任务组织成自演化记忆的共同坐标系。 |
| 2026-05-14 | Agent Memory | [GroupMemBench](https://arxiv.org/abs/2605.14498) <!-- benchmark-id:groupmembench --> | 多人群聊中的说话者信念、群体动态、术语差异和面向不同受众的表达。 | 长期记忆由单用户双边对话扩展到具有参与者和群体结构的共享交流。 |
| 2026-05-14 | Agent Memory | [MemEye](https://arxiv.org/abs/2605.15128) <!-- benchmark-id:memeye --> | 细粒度视觉证据、视觉状态变化，以及纯文本捷径检查。 | 系统必须保留真正必要的视觉信息，不能只依赖图片描述。 |
| 2026-05-14 | Agent Memory | [MEMLENS](https://arxiv.org/abs/2605.14906) <!-- benchmark-id:memlens --> | 在 32K 到 256K 的多模态多会话历史中进行提取、更新、时间推理和拒答。 | 在统一长度轴上比较原生长上下文模型与外部记忆智能体的视觉记忆。 |
| 2026-05-12 | Agent Memory | [MedMemoryBench](https://arxiv.org/abs/2605.11814) <!-- benchmark-id:medmemorybench --> | 在持续增长的医疗对话中追踪病情、时间变化和复杂临床信息，并观察记忆饱和。 | 由静态历史问答转向边构建记忆边评测的高风险纵向场景。 |
| 2026-05-04 | Data Agent | [DataClawBench](https://arxiv.org/abs/2605.02503) <!-- benchmark-id:dataclawbench --> | 在几乎没有先验提示时，自主探索陌生、含噪、跨域金融数据并形成可验证结论。 | 把数据源和模式发现从默认前提变成被测能力，并用里程碑区分有效进展与无效探索。 |
| 2026-05 | Agent Memory | [LongMemEval-V2](https://arxiv.org/abs/2605.12493) <!-- benchmark-id:longmemeval-v2 --> | 大量网页智能体轨迹中的环境状态、操作流程和易错点。 | 智能体积累的环境经验成为记忆对象，而不只是用户历史。 |
| 2026-05 | RAG | [SGR-Bench](https://arxiv.org/abs/2605.22219) <!-- benchmark-id:sgr-bench --> | 在证据受站点筛选、层级、范围或视图状态控制时完成搜索。 | 找到正确来源和把来源配置到正确状态，被拆成两个问题。 |
| 2026-04-30 | RAG | [Bright-Pro](https://aclanthology.org/2026.acl-long.1705/) <!-- benchmark-id:bright-pro --> | 考察推理密集型检索、推理要点覆盖，以及检索器在静态与智能体搜索中的实际效用。 | 把 BRIGHT 的窄正例排序扩展为多要点证据组合，并纳入迭代搜索中的检索器贡献。 |
| 2026-04-19 | RAG | [MuDABench](https://aclanthology.org/2026.findings-acl.341/) <!-- benchmark-id:mudabench --> | 考察大规模财务文档集合中的信息抽取、跨文档聚合和定量分析。 | 把多文档问答从少量支持文档扩展到集合级分析，并增加中间事实覆盖诊断。 |
| 2026-04-17 | Agent Memory | [MemEvoBench](https://arxiv.org/abs/2604.15774) <!-- benchmark-id:memevobench --> | 误导性记忆、噪声工具结果和偏置反馈在多轮写回后会不会使行为逐步失去安全性。 | 把记忆安全从单次攻击扩展为持续更新中的行为漂移。 |
| 2026-04-15 | RAG | [MERRIN](https://arxiv.org/abs/2604.13418) <!-- benchmark-id:merrin --> | 考察智能体在嘈杂网络中自主选择模态、检索多模态证据并进行多跳推理。 | 加入无模态提示的图像、视频、音频和图表证据，以及冲突与噪声来源。 |
| 2026-04-14 | RAG | [EnterpriseRAG-Bench](https://arxiv.org/abs/2605.05253) <!-- benchmark-id:enterpriserag-bench --> | 考察企业式知识库中的检索、多文档推理、冲突处理、完整性和无答案识别。 | 引入跨九类企业来源保持一致的合成公司语料，并系统加入噪声、重复和冲突。 |
| 2026-04-09 | Agent Memory | [ImplicitMemBench](https://aclanthology.org/2026.acl-long.1301/) <!-- benchmark-id:implicitmembench --> | 干扰之后，模型能否在首次尝试中自动表现出已学程序、启动效应或条件联结。 | 由询问模型记得什么，转向观察经历是否会自动改变行为。 |
| 2026-04-07 | RAG | [LeakDojo](https://aclanthology.org/2026.findings-acl.287/) <!-- benchmark-id:leakdojo --> | 考察攻击者从 RAG 数据库抽取文本内容的能力，以及不同管线和防御下的泄露风险。 | 把数据库抽取攻击、模型、语料、查询预算和防御纳入同一可控安全诊断框架。 |
| 2026-04-01 | RAG | [AutoResearchBench](https://arxiv.org/abs/2604.25256) <!-- benchmark-id:autoresearchbench --> | 考察科学文献中的目标论文追踪、条件约束、开放集合搜集和停止判断。 | 区分找到一篇目标论文与穷举未知规模论文集合，使搜索停止策略可测。 |
| 2026-03-12 | Data Agent | [AgentFuel](https://arxiv.org/abs/2603.12483) <!-- benchmark-id:agentfuel --> | 面向具体领域的时序对话智能体功能测试，重点覆盖有状态与事故型查询。 | 从通用静态问答转向可按领域定制、依赖历史状态和事件上下文的评测。 |
| 2026-03-05 | Data Agent | [TML-Bench](https://arxiv.org/abs/2603.05764) <!-- benchmark-id:tml-bench --> | 在固定时间预算和隐藏标签下，产出有效且有竞争力的表格机器学习提交。 | 从单次代码或得分比较扩展到时间—性能曲线、成功率与多次运行稳定性。 |
| 2026-03 | Data Agent | [Data Agent Benchmark (DAB)](https://arxiv.org/abs/2603.20576) <!-- benchmark-id:data-agent-benchmark --> | 跨多个 DBMS 完成数据集成、转换、分析和可执行核验。 | 企业数据问题从单条 SQL 扩展到跨数据库流程。 |
| 2026-03 | Agent Memory | [LifeBench](https://arxiv.org/abs/2603.03781) <!-- benchmark-id:lifebench --> | 多源长期轨迹中的事件、语义、习惯和程序性记忆。 | 评测不再局限于显式事实，也覆盖习惯和做事方法。 |
| 2026-02-27 | Data Agent | [DARE-bench](https://arxiv.org/abs/2602.24288) <!-- benchmark-id:dare-bench --> | 用可验证真值同时评估机器学习建模效果与对指定数据科学流程的遵循。 | 不再只看最终预测分数，还客观检查智能体是否按要求完成了过程。 |
| 2026-02-26 | RAG | [MTRAG-UN](https://aclanthology.org/2026.findings-acl.503/) <!-- benchmark-id:mtrag-un --> | 考察多轮 RAG 对不可回答、信息不足、非独立问题和含糊回复的处理。 | 在常规多轮检索与生成之外，加入了四类可诊断的会话失败情形。 |
| 2026-02-22 | RAG | [MC-Search](https://arxiv.org/abs/2603.00873) <!-- benchmark-id:mc-search --> | 考察多模态搜索规划、模态选择、逐跳证据检索和长链推理一致性。 | 从只看最终答案推进到带结构的多模态搜索链与逐步规划、检索诊断。 |
| 2026-02-18 | Agent Memory | [MemoryArena](https://arxiv.org/abs/2602.16313) <!-- benchmark-id:memoryarena --> | 在跨会话的智能体—环境循环中，用早期行动与反馈指导后续行动。 | 长期记忆与未来任务行动被放到同一项评测中。 |
| 2026-02-06 | RAG | [GISA](https://arxiv.org/abs/2602.08543) <!-- benchmark-id:gisa --> | 考察真实信息需求下的搜索规划、纵向推理、横向汇总和结构化作答。 | 把人工问题、稳定与实时子集、确定性评分和完整人工搜索轨迹统一到一个基准中。 |
| 2026-02-05 | RAG | [SAGE](https://arxiv.org/abs/2602.05975) <!-- benchmark-id:sage --> | 考察深度研究智能体在受控科学论文库中的定向找文与开放式文献搜集。 | 把科学检索拆成定向与开放式任务，并显式比较智能体与检索器的适配关系。 |
| 2026-02-03 | Agent Memory | [MemGUI-Bench](https://arxiv.org/abs/2602.06075) <!-- benchmark-id:memgui-bench --> | 移动端操作中的跨步骤保持、跨应用迁移、跨会话学习和失败恢复。 | 把记忆从对话问答带入可执行的移动 GUI 行为与重复任务学习。 |
| 2026-02 | RAG | [AgenticRAGTracer](https://arxiv.org/abs/2602.19127) <!-- benchmark-id:agenticragtracer --> | 对多步检索与推理逐跳核验，并检查步骤分配。 | 能够定位整条轨迹究竟在哪一步失败。 |
| 2026-02 | Agent Memory | [AMA-Bench](https://arxiv.org/abs/2602.22769) <!-- benchmark-id:ama-bench --> | 真实和可扩展合成的智能体—环境轨迹上的长程记忆。 | 记忆来源从对话扩展到带有因果结构的环境经历。 |
| 2026-02 | Agent Memory | [StructMemEval](https://arxiv.org/abs/2602.11243) <!-- benchmark-id:structmemeval --> | 智能体能否维护账本、列表、树等符合任务需要的记忆结构。 | 记忆的组织方式本身成为可观察能力。 |
<!-- TABLE-FIRST:RECENT:END -->

<a id="timeline"></a><a id="latest"></a><a id="frontier"></a>
## 最新条目深读

这一层保留 v2 的 acceptance / provenance 审计语义；上面的表格才是研究者按 source release time 扫描的主时间线。

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
## 三个方向的演化

| 方向 | 大致变化 | 现在关注什么 | 专题 Radar |
|---|---|---|---|
| **Agent Memory** | 跨会话回忆 → 更新、遗忘与结构 → 多模态和行动 → 隐式用户状态、共享治理与安全 | 记忆写了什么、谁能看到、何时该更新或删除，以及它是否真正改变后续行动？ | [Agent Memory Radar](https://github.com/H20Zhang/Agent-Memory-Radar#field-map) |
| **RAG / Agentic Retrieval** | 文档排序 → 鲁棒性与忠实度 → 深度研究与证据组合 → 实时搜索、跨来源执行与轨迹审计 | 智能体能否在变化的网页、来源、工具和预算下找到完整证据，并说明失败在哪里？ | [Agentic RAG Radar](https://github.com/H20Zhang/Agentic-RAG-Radar#field-map) |
| **Data Agents** | 自然语言转 SQL/代码 → 实验与工作流 → 数据探索、统计与因果分析 → 真实环境中的端到端可靠性 | 智能体能否先理解数据再执行分析，并在语义不清或证据不足时追问、弃答或拒答？ | [Data Agent Radar](https://github.com/H20Zhang/Data-Agent-Radar#field-map) |

<a id="field-map"></a>
## Benchmark 地图

<a id="benchmark-memory"></a>
### Agent Memory
从跨会话事实召回，逐步走向在线更新、结构化记忆、多模态证据、行动、权限与隐式用户状态。

<a id="benchmark-rag"></a>
### RAG / Agentic Retrieval
从文档相关性，逐步走向多跳证据组合、实时搜索、停止判断、跨来源执行与轨迹审计。

<a id="benchmark-data"></a>
### Data Agents
从 Text-to-SQL / code generation，逐步走向完整数据工作流、探索、统计/因果分析与业务语义可靠性。

<a id="all-benchmarks"></a>
## 按领域查看全部 Benchmark

以下是 registry 中的全部 95 个基准。这里的表格是 README 的一等阅读界面，不因为长度而下沉到 Library。

### Agent Memory

<!-- TABLE-FIRST:AREA:agent-memory:START -->
| 阶段 | Benchmark | 时间 | 考察内容 | 带来的变化 |
|---|---|---:|---|---|
| 🌱 前身 | [Beyond Goldfish Memory](https://aclanthology.org/2022.acl-long.356/) <!-- benchmark-id:beyond-goldfish-memory --> | 2022-05 | 多次真人聊天之间的开放域长期记忆与前后自洽。 | 跨会话的对话连续性由此成为独立评测问题。 |
| 🧱 基石 | [LoCoMo](https://aclanthology.org/2024.acl-long.747/) <!-- benchmark-id:locomo --> | 2024-08 | 超长多会话对话中的 QA、事件总结和多模态对话生成。 | 在 Beyond Goldfish Memory 的基础上，形成了可复用的超长对话多任务评测。 |
| 🧱 基石 | [LongMemEval](https://arxiv.org/abs/2410.10813) <!-- benchmark-id:longmemeval --> | 2024-10 | 长期助手历史中的信息抽取、跨会话推理、时间推理、知识更新和拒答。 | 将更新、时间推理和拒答从笼统的事实召回中拆分出来。 |
| ↗ 过渡 | [MemBench](https://arxiv.org/abs/2506.21605) <!-- benchmark-id:membench --> | 2025-06 | 事实记忆与反思记忆、参与者与观察者场景，以及效果、效率和容量。 | 评测范围由答题准确率扩展到记忆层次、交互角色和资源开销。 |
| ↗ 过渡 | [MemoryAgentBench](https://arxiv.org/abs/2507.05257) <!-- benchmark-id:memoryagentbench --> | 2025-07 | 增量多轮交互中的检索、测试时学习、长程理解和选择性遗忘。 | 记忆由读取静态历史，变成持续吸收、更新、使用和遗忘的在线过程。 |
| ↗ 过渡 | [BEAM](https://arxiv.org/abs/2510.27246) <!-- benchmark-id:beam --> | 2025-10 | 百万到千万 token 的连贯对话记忆。 | 直接观察超大规模连续历史下的记忆退化。 |
| 🔭 前沿 | [RealMem](https://aclanthology.org/2026.findings-acl.703/) <!-- benchmark-id:realmem --> | 2026-01 | 跨会话、目标和产物持续变化的项目型长期记忆。 | 评测由一般对话历史走向持续变化的项目状态与用户目标。 |
| 🔭 前沿 | [CAME-Bench](https://aclanthology.org/2026.findings-acl.584/) <!-- benchmark-id:came-bench --> | 2026-01-15 | 相同实体在不同目标段反复出现时，能否找回与当前意图相符的证据。 | 把长程检索中的语义相似干扰和目标上下文错配显式化。 |
| 🔭 前沿 | [AMA-Bench](https://arxiv.org/abs/2602.22769) <!-- benchmark-id:ama-bench --> | 2026-02 | 真实和可扩展合成的智能体—环境轨迹上的长程记忆。 | 记忆来源从对话扩展到带有因果结构的环境经历。 |
| 🔭 前沿 | [StructMemEval](https://arxiv.org/abs/2602.11243) <!-- benchmark-id:structmemeval --> | 2026-02 | 智能体能否维护账本、列表、树等符合任务需要的记忆结构。 | 记忆的组织方式本身成为可观察能力。 |
| 🔭 前沿 | [MemGUI-Bench](https://arxiv.org/abs/2602.06075) <!-- benchmark-id:memgui-bench --> | 2026-02-03 | 移动端操作中的跨步骤保持、跨应用迁移、跨会话学习和失败恢复。 | 把记忆从对话问答带入可执行的移动 GUI 行为与重复任务学习。 |
| 🔭 前沿 | [MemoryArena](https://arxiv.org/abs/2602.16313) <!-- benchmark-id:memoryarena --> | 2026-02-18 | 在跨会话的智能体—环境循环中，用早期行动与反馈指导后续行动。 | 长期记忆与未来任务行动被放到同一项评测中。 |
| 🔭 前沿 | [LifeBench](https://arxiv.org/abs/2603.03781) <!-- benchmark-id:lifebench --> | 2026-03 | 多源长期轨迹中的事件、语义、习惯和程序性记忆。 | 评测不再局限于显式事实，也覆盖习惯和做事方法。 |
| 🔭 前沿 | [ImplicitMemBench](https://aclanthology.org/2026.acl-long.1301/) <!-- benchmark-id:implicitmembench --> | 2026-04-09 | 干扰之后，模型能否在首次尝试中自动表现出已学程序、启动效应或条件联结。 | 由询问模型记得什么，转向观察经历是否会自动改变行为。 |
| 🔭 前沿 | [MemEvoBench](https://arxiv.org/abs/2604.15774) <!-- benchmark-id:memevobench --> | 2026-04-17 | 误导性记忆、噪声工具结果和偏置反馈在多轮写回后会不会使行为逐步失去安全性。 | 把记忆安全从单次攻击扩展为持续更新中的行为漂移。 |
| 🔭 前沿 | [LongMemEval-V2](https://arxiv.org/abs/2605.12493) <!-- benchmark-id:longmemeval-v2 --> | 2026-05 | 大量网页智能体轨迹中的环境状态、操作流程和易错点。 | 智能体积累的环境经验成为记忆对象，而不只是用户历史。 |
| 🔭 前沿 | [MedMemoryBench](https://arxiv.org/abs/2605.11814) <!-- benchmark-id:medmemorybench --> | 2026-05-12 | 在持续增长的医疗对话中追踪病情、时间变化和复杂临床信息，并观察记忆饱和。 | 由静态历史问答转向边构建记忆边评测的高风险纵向场景。 |
| 🔭 前沿 | [GroupMemBench](https://arxiv.org/abs/2605.14498) <!-- benchmark-id:groupmembench --> | 2026-05-14 | 多人群聊中的说话者信念、群体动态、术语差异和面向不同受众的表达。 | 长期记忆由单用户双边对话扩展到具有参与者和群体结构的共享交流。 |
| 🔭 前沿 | [MemEye](https://arxiv.org/abs/2605.15128) <!-- benchmark-id:memeye --> | 2026-05-14 | 细粒度视觉证据、视觉状态变化，以及纯文本捷径检查。 | 系统必须保留真正必要的视觉信息，不能只依赖图片描述。 |
| 🔭 前沿 | [MEMLENS](https://arxiv.org/abs/2605.14906) <!-- benchmark-id:memlens --> | 2026-05-14 | 在 32K 到 256K 的多模态多会话历史中进行提取、更新、时间推理和拒答。 | 在统一长度轴上比较原生长上下文模型与外部记忆智能体的视觉记忆。 |
| 🔭 前沿 | [EvoMemBench](https://arxiv.org/abs/2605.18421) <!-- benchmark-id:evomembench --> | 2026-05-18 | 在回合内与跨回合、知识型与执行型两条轴上统一比较记忆系统。 | 把分散的问答、工具、搜索和具身任务组织成自演化记忆的共同坐标系。 |
| 🔭 前沿 | [WorldMemArena](https://arxiv.org/abs/2605.29341) <!-- benchmark-id:worldmemarena --> | 2026-05-28 | 从多模态观察、行动和反馈中写入、维护、检索并使用不断变化的世界状态。 | 把记忆拆成可诊断的写入、维护、检索和使用四个阶段。 |
| 🔭 前沿 | [LifeSide](https://arxiv.org/abs/2606.04660) <!-- benchmark-id:lifeside --> | 2026-06 | 跨会话记忆、用户理解、隐私控制，以及情绪与环境的互动。 | 记忆开始与持续用户建模、隐私边界和环境情境一起考察。 |
| 🔭 前沿 | [GateMem](https://arxiv.org/abs/2606.18829) <!-- benchmark-id:gatemem --> | 2026-06-17 | 多人共享记忆能否同时保持可用、阻止越权泄露并执行删除请求。 | 长期记忆由单用户私有存储扩展到带权限和遗忘义务的共享治理。 |
| 🔭 前沿 | [DynamicMem](https://arxiv.org/abs/2606.22877) <!-- benchmark-id:dynamicmem --> | 2026-06-22 | 从十五个月、多个应用的零散行为中推断并更新用户属性、习惯和偏好。 | 把用户记忆推进到百万 token、长期漂移和跨应用隐式证据。 |
| 🔭 前沿 | [MEMPROBE](https://arxiv.org/abs/2606.24595) <!-- benchmark-id:memprobe --> | 2026-06-23 | 普通协助结束后，能否从智能体留下的记忆产物中恢复隐藏的用户状态。 | 由下游回答间接推断记忆，转为直接审计记忆产物本身。 |
| 🔭 前沿 | [LoCoMo-Plus](https://aclanthology.org/2026.acl-long.1150/) <!-- benchmark-id:locomo-plus --> | 2026-07 | 后续问题没有复述旧约束时，能否继续正确应用它。 | 目标从显式事实召回转向用户目标、价值和约束的一致应用。 |
| 🔭 前沿 | [Mem-Gallery](https://aclanthology.org/2026.acl-long.1892/) <!-- benchmark-id:mem-gallery --> | 2026-07 | 多模态长期对话中的记忆抽取、适应、推理和知识管理。 | 视觉保留、多模态推理和记忆组织被放进同一套评测。 |
| 🔭 前沿 | [Mem2ActBench](https://aclanthology.org/2026.acl-long.370/) <!-- benchmark-id:mem2actbench --> | 2026-07 | 长期记忆是否会影响工具选择和参数填写。 | 记忆对行动的作用可以直接评分，而不再只通过问答间接判断。 |
| 🔭 前沿 | [PerMemSafe](https://aclanthology.org/2026.findings-acl.320/) <!-- benchmark-id:permemsafe --> | 2026-07 | 能否从长期历史中识别隐含的个体风险，并在风险缓解后及时更新判断。 | 把用户状态记忆扩展到随时间变化的个性化安全与有用性权衡。 |
| 🔭 前沿 | [InMind](https://arxiv.org/abs/2607.24368) <!-- benchmark-id:inmind --> | 2026-07-27 | 旧事实与新问题词义相远、只有借助常识才能建立联系时，记忆能否被正确调出并应用。 | 用成对对照把存储失败、知识缺失、检索路由失败和应用失败分开。 |
<!-- TABLE-FIRST:AREA:agent-memory:END -->

### RAG / Agentic Retrieval

<!-- TABLE-FIRST:AREA:rag:START -->
| 阶段 | Benchmark | 时间 | 考察内容 | 带来的变化 |
|---|---|---:|---|---|
| 🌱 前身 | [HotpotQA](https://aclanthology.org/D18-1259/) <!-- benchmark-id:hotpotqa --> | 2018-10 | 从多个 Wikipedia 文档中找证据、组合推理，并标出支撑事实。 | 多文档证据组合和可解释支撑事实由此成为可测目标。 |
| 🧱 基石 | [KILT](https://arxiv.org/abs/2009.02252) <!-- benchmark-id:kilt --> | 2020-09 | 在同一份 Wikipedia 快照上评测多种知识密集任务，同时检查答案和证据来源。 | 正确性与来源追踪被放进共享、可复用的评测基础设施。 |
| 🧱 基石 | [BEIR](https://arxiv.org/abs/2104.08663) <!-- benchmark-id:beir --> | 2021-04 | 检索器在不同领域和任务上的零样本泛化。 | 不再用单一 IR 数据集的最好成绩代替跨域鲁棒性。 |
| 🧱 基石 | [RGB](https://arxiv.org/abs/2309.01431) <!-- benchmark-id:rgb --> | 2023-09 | RAG 面对噪声、不可回答问题、信息整合和反事实材料时的表现。 | “能否正确使用检索内容”被拆成几项独立能力。 |
| ↗ 过渡 | [MultiHop-RAG](https://arxiv.org/abs/2401.15391) <!-- benchmark-id:multihop-rag --> | 2024-01 | 在 RAG 流程中检索多份支撑证据并完成多跳推理。 | 多跳任务的错误可以落到检索或推理环节，而不只看最终答案。 |
| ↗ 过渡 | [RAGTruth](https://arxiv.org/abs/2401.00396) <!-- benchmark-id:ragtruth --> | 2024-01 | RAG 输出中的样例级、词级幻觉和依据错误。 | 忠实度问题由整题标签细化到具体文本片段。 |
| ↗ 过渡 | [CRAG](https://arxiv.org/abs/2406.04744) <!-- benchmark-id:crag --> | 2024-06 | 动态事实、长尾实体，以及网页和知识图谱上的事实型 RAG。 | 新鲜度、事实变化和长尾知识进入 RAG 评测。 |
| ↗ 过渡 | [BRIGHT](https://arxiv.org/abs/2407.12883) <!-- benchmark-id:bright --> | 2024-07 | 相关性判断本身需要推理的真实查询。 | 暴露仅靠语义相似度难以解决的检索任务。 |
| ↗ 过渡 | [RAGBench](https://arxiv.org/abs/2407.11005) <!-- benchmark-id:ragbench --> | 2024-07 | 跨行业场景的检索与生成质量标签，以及 RAG 评判器。 | 评判器质量和可用于诊断的错误标签也成为评测对象。 |
| ↗ 过渡 | [BrowseComp](https://arxiv.org/abs/2504.12516) <!-- benchmark-id:browsecomp --> | 2025-04 | 为寻找隐蔽答案持续浏览实时网页、改写查询并导航。 | 任务从单次检索扩展为持续的信息搜寻。 |
| ↗ 过渡 | [T²-RAGBench](https://aclanthology.org/2026.eacl-long.8/) <!-- benchmark-id:t2-ragbench --> | 2025-05-14 | 考察真实财务报告中的文本与表格检索，以及检索后的数值推理。 | 去除原有问答数据的先验正确上下文，使检索和数值推理能够端到端联合评测。 |
| ↗ 过渡 | [DeepResearch Bench](https://arxiv.org/abs/2506.11763) <!-- benchmark-id:deepresearch-bench --> | 2025-06 | 多步网页研究、证据收集、引用质量和长篇报告生成。 | 目标不再只是找到短答案，还要交付完整研究报告。 |
| ↗ 过渡 | [BrowseComp-Plus](https://arxiv.org/abs/2508.06600) <!-- benchmark-id:browsecomp-plus --> | 2025-08 | 在固定语料上进行深度研究，并分析检索贡献和答案准确率。 | 固定且经过核验的语料降低了实时搜索带来的黑箱性和复现困难。 |
| 🔭 前沿 | [RAGCap-Bench](https://arxiv.org/abs/2510.13910) <!-- benchmark-id:ragcap-bench --> | 2025-10 | 分别评测 Agentic RAG 中的规划、检索和中间推理能力。 | 中间能力可以独立诊断，不必只从最终答案倒推原因。 |
| 🔭 前沿 | [LIT-RAGBench](https://arxiv.org/abs/2603.06198) <!-- benchmark-id:lit-ragbench --> | 2025-10-22 | 在已给定检索上下文时，考察生成器的逻辑、整合、表格、推理与拒答能力。 | 隔离检索质量影响，在统一双语协议下诊断五类 RAG 生成能力。 |
| 🔭 前沿 | [AgenticRAGTracer](https://arxiv.org/abs/2602.19127) <!-- benchmark-id:agenticragtracer --> | 2026-02 | 对多步检索与推理逐跳核验，并检查步骤分配。 | 能够定位整条轨迹究竟在哪一步失败。 |
| 🔭 前沿 | [SAGE](https://arxiv.org/abs/2602.05975) <!-- benchmark-id:sage --> | 2026-02-05 | 考察深度研究智能体在受控科学论文库中的定向找文与开放式文献搜集。 | 把科学检索拆成定向与开放式任务，并显式比较智能体与检索器的适配关系。 |
| 🔭 前沿 | [GISA](https://arxiv.org/abs/2602.08543) <!-- benchmark-id:gisa --> | 2026-02-06 | 考察真实信息需求下的搜索规划、纵向推理、横向汇总和结构化作答。 | 把人工问题、稳定与实时子集、确定性评分和完整人工搜索轨迹统一到一个基准中。 |
| 🔭 前沿 | [MC-Search](https://arxiv.org/abs/2603.00873) <!-- benchmark-id:mc-search --> | 2026-02-22 | 考察多模态搜索规划、模态选择、逐跳证据检索和长链推理一致性。 | 从只看最终答案推进到带结构的多模态搜索链与逐步规划、检索诊断。 |
| 🔭 前沿 | [MTRAG-UN](https://aclanthology.org/2026.findings-acl.503/) <!-- benchmark-id:mtrag-un --> | 2026-02-26 | 考察多轮 RAG 对不可回答、信息不足、非独立问题和含糊回复的处理。 | 在常规多轮检索与生成之外，加入了四类可诊断的会话失败情形。 |
| 🔭 前沿 | [AutoResearchBench](https://arxiv.org/abs/2604.25256) <!-- benchmark-id:autoresearchbench --> | 2026-04-01 | 考察科学文献中的目标论文追踪、条件约束、开放集合搜集和停止判断。 | 区分找到一篇目标论文与穷举未知规模论文集合，使搜索停止策略可测。 |
| 🔭 前沿 | [LeakDojo](https://aclanthology.org/2026.findings-acl.287/) <!-- benchmark-id:leakdojo --> | 2026-04-07 | 考察攻击者从 RAG 数据库抽取文本内容的能力，以及不同管线和防御下的泄露风险。 | 把数据库抽取攻击、模型、语料、查询预算和防御纳入同一可控安全诊断框架。 |
| 🔭 前沿 | [EnterpriseRAG-Bench](https://arxiv.org/abs/2605.05253) <!-- benchmark-id:enterpriserag-bench --> | 2026-04-14 | 考察企业式知识库中的检索、多文档推理、冲突处理、完整性和无答案识别。 | 引入跨九类企业来源保持一致的合成公司语料，并系统加入噪声、重复和冲突。 |
| 🔭 前沿 | [MERRIN](https://arxiv.org/abs/2604.13418) <!-- benchmark-id:merrin --> | 2026-04-15 | 考察智能体在嘈杂网络中自主选择模态、检索多模态证据并进行多跳推理。 | 加入无模态提示的图像、视频、音频和图表证据，以及冲突与噪声来源。 |
| 🔭 前沿 | [MuDABench](https://aclanthology.org/2026.findings-acl.341/) <!-- benchmark-id:mudabench --> | 2026-04-19 | 考察大规模财务文档集合中的信息抽取、跨文档聚合和定量分析。 | 把多文档问答从少量支持文档扩展到集合级分析，并增加中间事实覆盖诊断。 |
| 🔭 前沿 | [Bright-Pro](https://aclanthology.org/2026.acl-long.1705/) <!-- benchmark-id:bright-pro --> | 2026-04-30 | 考察推理密集型检索、推理要点覆盖，以及检索器在静态与智能体搜索中的实际效用。 | 把 BRIGHT 的窄正例排序扩展为多要点证据组合，并纳入迭代搜索中的检索器贡献。 |
| 🔭 前沿 | [SGR-Bench](https://arxiv.org/abs/2605.22219) <!-- benchmark-id:sgr-bench --> | 2026-05 | 在证据受站点筛选、层级、范围或视图状态控制时完成搜索。 | 找到正确来源和把来源配置到正确状态，被拆成两个问题。 |
| 🔭 前沿 | [ScholarQuest](https://arxiv.org/abs/2606.20235) <!-- benchmark-id:scholarquest --> | 2026-05-19 | 考察智能体按研究意图迭代检索论文、扩展引文和控制结果范围。 | 把学术搜索定义为集合检索，并提供统一的大规模后端、意图切片和效率指标。 |
| 🔭 前沿 | [LiveBrowseComp](https://arxiv.org/abs/2605.28721) <!-- benchmark-id:livebrowsecomp --> | 2026-05-27 | 考察智能体能否检索近期、低显著性的网络事实，而非只验证模型已有知识。 | 使用构建前 90 天内的事实，并以闭卷和移除答案来源实验区分发现与验证。 |
| 🔭 前沿 | [EvoBrowseComp](https://arxiv.org/abs/2606.13120) <!-- benchmark-id:evobrowsecomp --> | 2026-06-11 | 考察英语和中文智能体对持续变化网络知识的广度搜索与多步推理。 | 引入可自动更新的双语实时网络问题生成流程，以降低静态测试集污染。 |
| 🔭 前沿 | [LoHoSearch](https://arxiv.org/abs/2606.12837) <!-- benchmark-id:lohosearch --> | 2026-06-11 | 考察超大候选空间、复杂约束结构、长程搜索和上下文管理。 | 用知识图谱系统控制搜索空间与结构复杂度，而非仅依赖人工主观设难。 |
| 🔭 前沿 | [VAKRA](https://arxiv.org/abs/2608.12282) <!-- benchmark-id:vakra --> | 2026-08 | 组合调用 API、检索文档、完成多跳推理，并遵守工具策略。 | 跨来源依据、实际执行和策略一致性出现在同一条轨迹中。 |
| 🔭 前沿 | [SearchAuditBench](https://arxiv.org/abs/2608.05212) <!-- benchmark-id:searchauditbench --> | 2026-08-05 | 考察审计模型能否在超长搜索轨迹中定位错误、归因根因并生成可执行修复。 | 从最终答案成败推进到专家标注的关键步骤、六类根因和修复后恢复评测。 |
<!-- TABLE-FIRST:AREA:rag:END -->

### Data Agents

<!-- TABLE-FIRST:AREA:data-agent:START -->
| 阶段 | Benchmark | 时间 | 考察内容 | 带来的变化 |
|---|---|---:|---|---|
| 🌱 前身 | [WikiSQL](https://arxiv.org/abs/1709.00103) <!-- benchmark-id:wikisql --> | 2017-08 | 根据自然语言问题，在单个 Wikipedia 表格上生成可执行 SQL。 | 大规模、可执行的自然语言数据库访问由此成为标准任务。 |
| 🧱 基石 | [Spider](https://aclanthology.org/D18-1425/) <!-- benchmark-id:spider --> | 2018-10 | 在未见过的 schema 上生成复杂的多表 SQL，并测试跨领域泛化。 | Text-to-SQL 从单表生成走向复杂查询和跨 schema 泛化。 |
| 🧱 基石 | [DS-1000](https://arxiv.org/abs/2211.11501) <!-- benchmark-id:ds-1000 --> | 2022-11 | 使用七类 Python 数据科学库生成代码，并通过执行检查正确性。 | 在 SQL 之外建立了可复现的实用数据科学代码评测。 |
| ↗ 过渡 | [BIRD](https://arxiv.org/abs/2305.03111) <!-- benchmark-id:bird --> | 2023-05 | 处理大型真实数据库中的脏值、外部知识、复杂 SQL 和执行效率。 | Text-to-SQL 开始面对数据值丰富但不整洁的数据库，SQL 效率也纳入评测。 |
| ↗ 过渡 | [MLAgentBench](https://arxiv.org/abs/2310.03302) <!-- benchmark-id:mlagentbench --> | 2023-10 | 反复设计、运行、检查并改进机器学习实验。 | 一次性代码生成变成由执行反馈驱动的实验过程。 |
| ↗ 过渡 | [InsightBench](https://arxiv.org/abs/2407.06423) <!-- benchmark-id:insightbench --> | 2024-07 | 从提出问题、探索性分析到形成洞见和行动建议的业务分析。 | 目标从完成指定代码任务扩展到发现并表达有用结论。 |
| ↗ 过渡 | [DA-Code](https://aclanthology.org/2024.emnlp-main.748/) <!-- benchmark-id:da-code --> | 2024-10 | 在真实数据上完成数据整理、EDA、机器学习规划和可执行代码生成。 | 在静态代码题与智能体式数据工作之间建立了可执行的过渡任务。 |
| ↗ 过渡 | [Spider 2.0](https://arxiv.org/abs/2411.07763) <!-- benchmark-id:spider-2 --> | 2024-11 | 在巨大 schema、多种 SQL 方言、元数据、代码库和云数据库中完成企业 SQL 工作流。 | 一次语义解析被扩展为长程企业任务。 |
| ↗ 过渡 | [DataSciBench](https://arxiv.org/abs/2502.13897) <!-- benchmark-id:datascibench --> | 2025-02 | 覆盖多类数据科学任务，并为不同任务配置程序化指标和人工核验答案。 | 任务范围扩大后，不同分析目标开始使用各自合适的评判器。 |
| 🔭 前沿 | [LiveSQLBench](https://livesqlbench.ai/) <!-- benchmark-id:livesqlbench --> | 2025-05-28 | 在持续演化的工业数据库与分层知识库上执行查询和管理类 SQL，并适应业务规则漂移。 | 把静态 Text-to-SQL 推进到带隐藏更新、大模式、业务知识和数据库写操作的持续评测。 |
| ↗ 过渡 | [KramaBench](https://arxiv.org/abs/2506.06541) <!-- benchmark-id:kramabench --> | 2025-06-06 | 在杂乱异构数据湖上完成发现、清洗、整合、分析与建模的端到端管线。 | 把问题从“给定数据写代码”推进到“在整个数据湖中找到证据并交付可运行管线”。 |
| ↗ 过渡 | [DABstep](https://arxiv.org/abs/2506.23719) <!-- benchmark-id:dabstep --> | 2025-06-30 | 结合交易数据、业务文档与领域规则完成多步金融分析。 | 从单表或单步问答转向跨数据与文档的长链推理，并保持结果精确可自动核验。 |
| 🔭 前沿 | [FDABench](https://arxiv.org/abs/2509.02473) <!-- benchmark-id:fdabench --> | 2025-09 | 在结构化数据、非结构化材料、网页和多模态来源上完成多源分析。 | 异构分析、推理过程、延迟和 token 成本可以同时观察。 |
| ↗ 过渡 | [AgentDS](https://arxiv.org/abs/2603.19005) <!-- benchmark-id:agentds --> | 2025-10-18 | 在六个行业的领域预测任务上比较纯 AI 与人机协作方案。 | 把领域专家贡献和人机协作设为直接比较轴，而不只比较自主智能体。 |
| 🔭 前沿 | [DDR-Bench](https://arxiv.org/abs/2602.02039) <!-- benchmark-id:ddr-bench --> | 2025-11-30 | 只给实体和数据库元数据，要求智能体自主设定目标、探索、形成假设并发现可核验洞见。 | 把评价对象从“完成给定分析问题”改为“自己判断什么值得调查并证明发现”。 |
| 🔭 前沿 | [DAComp](https://arxiv.org/abs/2512.04324) <!-- benchmark-id:dacomp --> | 2025-12 | 代码仓库级数据工程和开放式数据分析。 | 数据工程与分析被放进更完整的数据智能生命周期。 |
| 🔭 前沿 | [DSAEval](https://arxiv.org/abs/2601.13591) <!-- benchmark-id:dsaeval --> | 2026-01-20 | 在表格、图像与文本数据上进行连续多轮数据科学项目，并综合评价推理、代码和结果。 | 从单轮表格任务推进到需要多模态感知和项目上下文累积的真实问题序列。 |
| 🔭 前沿 | [DSGym](https://arxiv.org/abs/2601.16344) <!-- benchmark-id:dsgym --> | 2026-01-22 | 在统一、隔离、可执行环境中评测经捷径过滤的数据分析、预测与领域任务。 | 把碎片化基准统一到同一执行接口，并显式检查任务是否真的需要使用数据。 |
| 🔭 前沿 | [DARE-bench](https://arxiv.org/abs/2602.24288) <!-- benchmark-id:dare-bench --> | 2026-02-27 | 用可验证真值同时评估机器学习建模效果与对指定数据科学流程的遵循。 | 不再只看最终预测分数，还客观检查智能体是否按要求完成了过程。 |
| 🔭 前沿 | [Data Agent Benchmark (DAB)](https://arxiv.org/abs/2603.20576) <!-- benchmark-id:data-agent-benchmark --> | 2026-03 | 跨多个 DBMS 完成数据集成、转换、分析和可执行核验。 | 企业数据问题从单条 SQL 扩展到跨数据库流程。 |
| 🔭 前沿 | [TML-Bench](https://arxiv.org/abs/2603.05764) <!-- benchmark-id:tml-bench --> | 2026-03-05 | 在固定时间预算和隐藏标签下，产出有效且有竞争力的表格机器学习提交。 | 从单次代码或得分比较扩展到时间—性能曲线、成功率与多次运行稳定性。 |
| 🔭 前沿 | [AgentFuel](https://arxiv.org/abs/2603.12483) <!-- benchmark-id:agentfuel --> | 2026-03-12 | 面向具体领域的时序对话智能体功能测试，重点覆盖有状态与事故型查询。 | 从通用静态问答转向可按领域定制、依赖历史状态和事件上下文的评测。 |
| 🔭 前沿 | [DataClawBench](https://arxiv.org/abs/2605.02503) <!-- benchmark-id:dataclawbench --> | 2026-05-04 | 在几乎没有先验提示时，自主探索陌生、含噪、跨域金融数据并形成可验证结论。 | 把数据源和模式发现从默认前提变成被测能力，并用里程碑区分有效进展与无效探索。 |
| 🔭 前沿 | [IRTS-ToolBench](https://arxiv.org/abs/2606.15107) <!-- benchmark-id:irts-toolbench --> | 2026-06-13 | 在异步、缺失且采样频率不一的非规则时间序列上选择工具并完成可核验问答。 | 把规则采样这一默认假设移除，直接测量非规则性处理与工具落地推理。 |
| 🔭 前沿 | [StatABench](https://arxiv.org/abs/2606.22977) <!-- benchmark-id:statabench --> | 2026-06-22 | 同时评估统计知识、工具选择与参数设置，以及开放式建模和报告。 | 把封闭式统计问答和工具调用与端到端开放建模纳入同一套能力坐标。 |
| 🔭 前沿 | [AgenticDataBench](https://arxiv.org/abs/2607.01647) <!-- benchmark-id:agenticdatabench --> | 2026-07 | 用细粒度技能分类检查真实数据科学工作流的覆盖情况。 | 除了总成功率，还能审计这套基准覆盖了哪些技能。 |
| 🔭 前沿 | [CausalDS](https://arxiv.org/abs/2607.08093) <!-- benchmark-id:causalds --> | 2026-07-09 | 在可执行数据科学环境中覆盖因果预测、识别、效应估计、反事实、不确定性与弃答。 | 把数据智能体评测从相关性和预测拓展到 Pearl 三阶因果推理及“无法作答”的识别。 |
| 🔭 前沿 | [DataSpace](https://arxiv.org/abs/2608.03451) <!-- benchmark-id:dataspace --> | 2026-08 | 在混合数据库、文件、文档和多媒体的工作区中完成可验证分析。 | 寻找异构证据和核验完整结果成为一项统一任务。 |
| 🔭 前沿 | [DSAgentBench](https://arxiv.org/abs/2608.10366) <!-- benchmark-id:dsagentbench --> | 2026-08 | 使用笔记本、IDE、终端、浏览器和数据库完成完整数据科学工作流。 | 评测进入真实计算机环境，要求多阶段、多工具执行能够可靠衔接。 |
| 🔭 前沿 | [WarehouseReliabilityBench](https://arxiv.org/abs/2608.09254) <!-- benchmark-id:warehouse-reliability-bench --> | 2026-08-10 | 面对语义歧义、不可回答、模式漂移和对抗输入时，返回业务真值或正确地澄清、弃答、拒答。 | 从“SQL 能运行且结果匹配”转向“业务含义正确，并在不该给数字时不虚假成功”。 |
| 🔭 前沿 | [Data Exploration Benchmark](https://arxiv.org/abs/2608.16045) <!-- benchmark-id:data-exploration-benchmark --> | 2026-08-17 | 在下游分析前，构建包含逻辑表、列语义、键关系和质量信号的结构化数据理解产物。 | 把通常隐含的数据探索阶段从最终答案的前置假设变成可独立评分、可验证下游价值的对象。 |
<!-- TABLE-FIRST:AREA:data-agent:END -->

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
| **检索评测如何变成实时、可审计的搜索？** | BEIR / BRIGHT → BrowseComp / LiveBrowseComp → Bright-Pro / LoHoSearch / SearchAuditBench → VAKRA | [Agentic RAG Radar](https://github.com/H20Zhang/Agentic-RAG-Radar#field-map) |
| **数据智能体评测如何从 SQL/代码走到可靠的数据工作？** | Spider / DS-1000 → KramaBench / DABstep → DataClawBench / DSGym → DataSpace / DSAgentBench / WarehouseReliabilityBench | [Data Agent Radar](https://github.com/H20Zhang/Data-Agent-Radar#field-map) |

<a id="library"></a>
## Benchmark Library

- **[按时间、领域、演化关系和评测维度继续浏览](library/README.md)**
- [Canonical registry](data/benchmarks.json)
- [Research compactions](digests/README.md)

这里整理“测什么、为什么这样测”；具体方法和系统放在三个专题 Radar 中，避免重复维护同一份综述。

[English](README.en.md) · [Curation](CURATION.md) · [Schema](SCHEMA.md)
