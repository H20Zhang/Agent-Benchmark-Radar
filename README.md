# Agent Benchmark Radar

**中文** | [English](README.en.md)

收录 Agent Memory、Agentic RAG 和 Data Agent 方向的基准，按发布时间和研究方向整理。方法与系统见对应的专题 Radar。

[Agent Memory Radar](https://github.com/H20Zhang/Agent-Memory-Radar) · [Agentic RAG Radar](https://github.com/H20Zhang/Agentic-RAG-Radar) · [Data Agent Radar](https://github.com/H20Zhang/Data-Agent-Radar)

[最近半年](#frontier) · [三个方向](#evolution) · [按领域查看全部](#area-timelines) · [阅读路径](#reading-paths) · [Benchmark Library](#library)

最后更新：**2026-08-20**

读表时要注意：模型、工具接口、提示、重试次数、停止条件和预算不一致时，分数反映的是整套系统，不能直接归因于某个组件。

<a id="frontier"></a>
## 最近半年 Benchmark 时间线

范围随 registry 中最近的核验日期滚动，向前覆盖六个月。部分论文只有月份信息，因此边界月整月保留。表中不做精选，窗口内的基准全部列出。

<!-- RECENT-TIMELINE:START -->
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
<!-- RECENT-TIMELINE:END -->

### 进一步看四个 Benchmark

<details><summary><strong>DSAgentBench：把数据科学评测搬进真实计算机环境</strong></summary>

过去的数据智能体基准往往分别测试 SQL、代码生成、分析答案，或工作流中的某一个阶段。DSAgentBench 要求智能体在真实计算机环境中完成整套数据科学任务：协调多种工具，并根据中间结果决定下一步。

它包含 **275 个任务**，用确定性检查核验分析结果、可视化和模型表现。论文报告最强系统的任务成功率为 **56.70%**，所有开源系统低于 1%。不过，模型、运行框架、工具可靠性、操作系统交互和长程推理在这里同时变化，因此这些数字比较的是整套系统。它的价值在于换了评测环境和协议，而不只是多了一张排行榜。

</details>

<details><summary><strong>DataSpace：问题不只在分析，还在找到证据</strong></summary>

DataSpace 只给智能体一个问题，以及一个任务专属的混合工作区，其中可能同时出现 CSV、JSON、SQLite、Markdown、PDF 和视频。智能体既要找到证据、跨来源关联数据，也要交付完整的表格结果。

数据集包含 **410 个任务和 7,439 个文件**。论文还发现，固定底座模型后，仅更换运行框架就会带来 **15.36 分**的差距。这说明数据智能体的分数对执行框架非常敏感；DataSpace 扩大了可测范围，却不能单凭总分判断究竟是控制器、检索还是其他组件带来了提升。

</details>

<details><summary><strong>LoCoMo-Plus：没有复述的约束还算不算记住</strong></summary>

传统长期记忆问答通常会在后续问题中留下与旧事实相近的词面或语义提示。LoCoMo-Plus 刻意切断这种提示：用户没有再次说出旧约束，智能体仍要记住并正确应用它。

问题由“能否找回旧事实”变成“过去记住的用户状态能否约束未来行为”。尚未解决的是，这种一致性测试能否迁移到长期运行的真实智能体：用户偏好会变化、权限会变化，行动还可能不可逆。

</details>

<details><summary><strong>VAKRA：检索、API 与策略放进同一条执行轨迹</strong></summary>

VAKRA 要求智能体在同一条轨迹中调用 API、检索文档、完成多跳推理，并遵守工具使用策略。API 任务和文档问答分开测试时看不到的问题——例如身份不一致、跨来源依据错误和违反策略的执行——因此会直接暴露出来。

它衡量的是整条执行轨迹能否自洽，不能把总分直接归因于某一种检索策略。新增的考察重点，是跨来源信息在实际执行中能否保持一致。

</details>

<a id="evolution"></a>
## 三个方向的演化

| 方向 | 大致变化 | 现在关注什么 | 专题 Radar |
|---|---|---|---|
| **Agent Memory** | 跨会话回忆 → 更新、遗忘与结构 → 多模态和行动 → 隐式用户状态、共享治理与安全 | 记忆写了什么、谁能看到、何时该更新或删除，以及它是否真正改变后续行动？ | [Agent Memory Radar](https://github.com/H20Zhang/Agent-Memory-Radar) |
| **RAG / Agentic Retrieval** | 文档排序 → 鲁棒性与忠实度 → 深度研究与证据组合 → 实时搜索、跨来源执行与轨迹审计 | 智能体能否在变化的网页、来源、工具和预算下找到完整证据，并说明失败在哪里？ | [Agentic RAG Radar](https://github.com/H20Zhang/Agentic-RAG-Radar) |
| **Data Agents** | 自然语言转 SQL/代码 → 实验与工作流 → 数据探索、统计与因果分析 → 真实环境中的端到端可靠性 | 智能体能否先理解数据再执行分析，并在语义不清或证据不足时追问、弃答或拒答？ | [Data Agent Radar](https://github.com/H20Zhang/Data-Agent-Radar) |

<a id="area-timelines"></a>
## 按领域查看全部 Benchmark

以下是 registry 中的全部 95 个基准，按发布时间从早到晚排列。

### Agent Memory

<!-- COMPLETE-MAP:agent-memory:START -->
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
<!-- COMPLETE-MAP:agent-memory:END -->

最近的工作已经把写入、更新、遗忘、组织、多模态信息保真、隐式用户状态、行动、共享权限和安全分开考察。仍然缺少的，是在权限和预算可比的真实长期环境中，观察数周或数月的状态变化以及不可逆行动带来的后果。

[Agent Memory 方法与系统 →](https://github.com/H20Zhang/Agent-Memory-Radar)

### RAG / Agentic Retrieval

<!-- COMPLETE-MAP:rag:START -->
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
<!-- COMPLETE-MAP:rag:END -->

检索评测已经从文档排序扩展到证据组合、实时网页、长程搜索和轨迹审计，来源状态、工具调用、停止时机与跨来源执行都开始计入结果。最大的困难仍是公平归因——只有接口、运行框架、模型和预算可比时，才能判断提升究竟来自哪里；实时环境持续变化又让这件事更难。

[Agentic RAG 方法与系统 →](https://github.com/H20Zhang/Agentic-RAG-Radar)

### Data Agents

<!-- COMPLETE-MAP:data-agent:START -->
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
<!-- COMPLETE-MAP:data-agent:END -->

数据智能体的评测正从 SQL 或代码生成走向完整数据工作：先探索和理解数据，再做统计、因果或时序分析，组织工具、核验过程并交付结果。可靠性基准已经开始考察澄清、弃答和拒答，但真实企业语义、长期运行状态与治理要求仍覆盖不足。

[Data Agent 方法与系统 →](https://github.com/H20Zhang/Data-Agent-Radar)

## 目前仍然测不好的重要问题

有些问题还没有合适的基准，但这不等于它们不重要。

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
| **记忆评测如何从回忆走向行动与治理？** | Multi-Session Chat → LoCoMo / LongMemEval → MemoryArena / WorldMemArena → GateMem / PerMemSafe / InMind | [Agent Memory Radar](https://github.com/H20Zhang/Agent-Memory-Radar) |
| **检索评测如何变成实时、可审计的搜索？** | BEIR / BRIGHT → BrowseComp / LiveBrowseComp → Bright-Pro / LoHoSearch / SearchAuditBench → VAKRA | [Agentic RAG Radar](https://github.com/H20Zhang/Agentic-RAG-Radar) |
| **数据智能体评测如何从 SQL/代码走到可靠的数据工作？** | Spider / DS-1000 → KramaBench / DABstep → DataClawBench / DSGym → DataSpace / DSAgentBench / WarehouseReliabilityBench | [Data Agent Radar](https://github.com/H20Zhang/Data-Agent-Radar) |

<a id="library"></a>
## Benchmark Library

- **[按时间、领域、演化关系和评测维度浏览](library/README.md)**
- [结构化 registry](data/benchmarks.json)
- [阶段性研究总结](digests/README.md)

## 这个仓库与专题 Radar

这里整理“测什么、为什么这样测”；具体方法和系统放在三个专题 Radar 中，避免重复维护同一份综述。

[English](README.en.md) · [Curation](CURATION.md) · [Schema](SCHEMA.md)
