# Benchmark Library

**中文** | [English](README.en.md) · [返回入口](../README.md)

先按时间看领域最近把什么变成了可测对象，再按领域追完整演化。两个视图都覆盖当前 registry 的全部 benchmark。

## 按时间浏览（全部）

<!-- COMPLETE-TIMELINE:START -->


| 时间 | Benchmark | 领域 | 角色 | 这次改变了什么 |
|---:|---|---|---|---|
| 2026-08-26 | [SCALE-QA](https://arxiv.org/abs/2608.25655) <!-- benchmark-id:scale-qa --> | Agent Memory | 🔭 前沿 | 去掉 session/topic 边界，把“恢复真正约束当前任务的 episode”从隐含假设变成直接评测对象。 |
| 2026-08-24 | [InjecMEM](https://arxiv.org/abs/2608.23471) <!-- benchmark-id:injecmem --> | Agent Memory | 🔭 前沿 | 把一次普通交互的恶意写入连到漂移后的检索与定向生成。 |
| 2026-08-24 | [Snapshot Compatibility Audit](https://arxiv.org/abs/2608.22856) <!-- benchmark-id:snapshot-compatibility-audit --> | RAG / Agentic Retrieval | 🔭 前沿 | 把 corpus snapshot 升级变成减去采样噪声的 compatibility regression。 |
| 2026-08-24 | [The Compaction Cliff](https://arxiv.org/abs/2608.22752) <!-- benchmark-id:compaction-cliff --> | Agent Memory | 🔭 前沿 | 把 safety rule 的精确保留扩展到压缩、分解、检索和下游行为。 |
| 2026-08-22 | [Agent Memory Bench (coding agents)](https://github.com/GiulioDER/agent-memory-bench) <!-- benchmark-id:agent-memory-bench-coding --> | Agent Memory | 🔭 前沿 | 用 neutral feed、proof-of-treatment 和 executable oracle 收紧跨任务记忆效应的因果归因。 |
| 2026-08-22 | [KBGym / Training a Knowledge Base](https://arxiv.org/abs/2608.21829) <!-- benchmark-id:kbgym --> | RAG / Agentic Retrieval | 🔭 前沿 | 把知识库从静态索引变成可监督训练、可冻结并按 coverage 审计的对象。 |
| 2026-08-22 | [membench (staleness)](https://github.com/Ps23102004/membench) <!-- benchmark-id:membench-staleness --> | Agent Memory | 🔭 前沿 | 把 current-vs-stale 排序与弃答、泄露防护做成可执行 memory-store 诊断。 |
| 2026-08-22 | [RAG Collapse](https://arxiv.org/abs/2608.22118) <!-- benchmark-id:rag-collapse --> | RAG / Agentic Retrieval | 🔭 前沿 | 把 recursive feedback 从模型权重训练迁移到 retrieval context。 |
| 2026-08-21 | [Agent Memory Bakeoff](https://github.com/JaysonRawlins/agent-memory-bakeoff) <!-- benchmark-id:agent-memory-bakeoff --> | Agent Memory | 🔭 前沿 | 交叉比较检索策略与写入时 enrichment，使跨词汇记忆访问可单独测量。 |
| 2026-08-21 | [DreamBench-SWE](https://arxiv.org/abs/2608.20664) <!-- benchmark-id:dreambench-swe --> | Agent Memory | 🔭 前沿 | 把“过去状态是否有用”拆成对过期、错作用域、冲突、组合或应忽略记忆的可执行 hygiene 测试。 |
| 2026-08-21 | [Utility Under Attack](https://arxiv.org/abs/2608.21230) <!-- benchmark-id:utility-under-attack --> | Agent Memory | 🔭 前沿 | 用 retained benign utility 暴露 poisoning 与防御引发的 denial-of-service。 |
| 2026-08-20 | [AI4AI-Bench](https://arxiv.org/abs/2608.20318) <!-- benchmark-id:ai4ai-bench --> | Data Agents | 🔭 前沿 | 用 proxy exploration、source-patch 边界和 clean-start 正式运行更紧地隔离学习算法设计。 |
| 2026-08-20 | [DeltaML-Bench](https://arxiv.org/abs/2608.19653) <!-- benchmark-id:deltaml-bench --> | Data Agents | 🔭 前沿 | 把真实研究仓库中的 ML 改进、长算力预算和 anti-gaming audit 绑定为一个可执行协议。 |
| 2026-08-20 | [MemTrapBench](https://arxiv.org/abs/2608.20202) <!-- benchmark-id:memtrapbench --> | Agent Memory | 🔭 前沿 | 把“检索到了相关记忆”与“这段记忆是否应该影响当前推理”拆开，并用 no-memory 配对控制直接测量负效应。 |
| 2026-08-20 | [StateMemBench](https://arxiv.org/abs/2608.19652) <!-- benchmark-id:statemembench --> | Agent Memory | 🔭 前沿 | 把 state drift 从 retrieval/reasoning failure 中隔离出来，用 current-vs-superseded 结果和 anti-trap controls 直接评分。 |
| 2026-08-18 | [BrowseComp-Plus_CM](https://arxiv.org/abs/2608.20317) <!-- benchmark-id:browsecomp-plus-cm --> | RAG / Agentic Retrieval | 🔭 前沿 | 证明固定语料仍可能因 query-conditioned construction 与规模而显著低估证据发现难度。 |
| 2026-08-18 | [VisDocAgentBench](https://arxiv.org/abs/2608.17889) <!-- benchmark-id:visdocagentbench --> | RAG / Agentic Retrieval | 🔭 前沿 | 在统一 top-10 输出下直接比较静态视觉检索与迭代式页面发现、检查。 |
| 2026-08-17 | [Data Exploration Benchmark](https://arxiv.org/abs/2608.16045) <!-- benchmark-id:data-exploration-benchmark --> | Data Agents | 🔭 前沿 | 把通常隐含的数据探索阶段从最终答案的前置假设变成可独立评分、可验证下游价值的对象。 |
| 2026-08-17 | [SP-Mem Privacy-Aware Memory Benchmark](https://arxiv.org/abs/2608.16551) <!-- benchmark-id:sp-mem --> | Agent Memory | 🔭 前沿 | 把个性化收益、授权与泄露风险放进同一记忆生命周期协议。 |
| 2026-08-17 | [The Commercial Tax](https://arxiv.org/abs/2608.16096) <!-- benchmark-id:commercial-tax --> | RAG / Agentic Retrieval | 🔭 前沿 | 把 license、query format、index construction 与 cost 纳入 retrieval number 的可迁移性审计。 |
| 2026-08-10 | [The Recall Trap](https://arxiv.org/abs/2608.14838) <!-- benchmark-id:recall-trap --> | RAG / Agentic Retrieval | 🔭 前沿 | 证明固定槽位下更高 file recall 可能对应更低 repair success，限制 recall 指标的解释。 |
| 2026-08-10 | [WarehouseReliabilityBench](https://arxiv.org/abs/2608.09254) <!-- benchmark-id:warehouse-reliability-bench --> | Data Agents | 🔭 前沿 | 从“SQL 能运行且结果匹配”转向“业务含义正确，并在不该给数字时不虚假成功”。 |
| 2026-08-07 | [DAS-Bench / DAS-Eval](https://arxiv.org/abs/2608.18034) <!-- benchmark-id:das-bench --> | RAG / Agentic Retrieval | 🔭 前沿 | 把学术综述的覆盖、taxonomy、claim、citation、discourse 与成品质量变成 16 项协议。 |
| 2026-08-05 | [SearchAuditBench](https://arxiv.org/abs/2608.05212) <!-- benchmark-id:searchauditbench --> | RAG / Agentic Retrieval | 🔭 前沿 | 从最终答案成败推进到专家标注的关键步骤、六类根因和修复后恢复评测。 |
| 2026-08-04 | [MAPLE](https://arxiv.org/abs/2608.15624) <!-- benchmark-id:maple --> | RAG / Agentic Retrieval | 🔭 前沿 | 不再只问一条 query 是否命中，而是测同一论文跨多个 aspect 的可检索一致性。 |
| 2026-08-04 | [PAST-Bench](https://arxiv.org/abs/2608.04003) <!-- benchmark-id:past-bench --> | Agent Memory | 🔭 前沿 | 用 persistence on/off 配对控制识别跨 episode 记忆是否真的改善可执行任务。 |
| 2026-08 | [DataSpace](https://arxiv.org/abs/2608.03451) <!-- benchmark-id:dataspace --> | Data Agents | 🔭 前沿 | 寻找异构证据和核验完整结果成为一项统一任务。 |
| 2026-08 | [DSAgentBench](https://arxiv.org/abs/2608.10366) <!-- benchmark-id:dsagentbench --> | Data Agents | 🔭 前沿 | 评测进入真实计算机环境，要求多阶段、多工具执行能够可靠衔接。 |
| 2026-08 | [VAKRA](https://arxiv.org/abs/2608.12282) <!-- benchmark-id:vakra --> | RAG / Agentic Retrieval | 🔭 前沿 | 跨来源依据、实际执行和策略一致性出现在同一条轨迹中。 |
| 2026-07-29 | [data-eng-bench](https://github.com/Snowflake-Labs/data-eng-bench) <!-- benchmark-id:data-eng-bench --> | Data Agents | 🔭 前沿 | 用可执行 dbt 任务和隐藏行级核验测数据工程；8 月修复暴露 evaluator reliability 也是测量对象。 |
| 2026-07-27 | [InMind](https://arxiv.org/abs/2607.24368) <!-- benchmark-id:inmind --> | Agent Memory | 🔭 前沿 | 用成对对照把存储失败、知识缺失、检索路由失败和应用失败分开。 |
| 2026-07-21 | [MemFuseBench](https://arxiv.org/abs/2608.18704) <!-- benchmark-id:memfusebench --> | Agent Memory | 🔭 前沿 | 跨异构来源的 linking、causal fusion、conflict 与 provenance 被拆成诊断项。 |
| 2026-07-14 | [WANDR](https://arxiv.org/abs/2608.14747) <!-- benchmark-id:wandr --> | RAG / Agentic Retrieval | 🔭 前沿 | 把实时网页上的开放集合发现、记录扩充与逐条复核合成 wide-and-deep 任务。 |
| 2026-07-09 | [CausalDS](https://arxiv.org/abs/2607.08093) <!-- benchmark-id:causalds --> | Data Agents | 🔭 前沿 | 把数据智能体评测从相关性和预测拓展到 Pearl 三阶因果推理及“无法作答”的识别。 |
| 2026-07-01 | [LitReview Arena / LitReviewBench / LitJudge](https://arxiv.org/abs/2608.21374) <!-- benchmark-id:litreview-arena --> | RAG / Agentic Retrieval | 🔭 前沿 | 用 topic-matched 专家偏好校准文献综述评价，而非依赖通用 LLM judge。 |
| 2026-07 | [AgenticDataBench](https://arxiv.org/abs/2607.01647) <!-- benchmark-id:agenticdatabench --> | Data Agents | 🔭 前沿 | 除了总成功率，还能审计这套基准覆盖了哪些技能。 |
| 2026-07 | [LoCoMo-Plus](https://aclanthology.org/2026.acl-long.1150/) <!-- benchmark-id:locomo-plus --> | Agent Memory | 🔭 前沿 | 目标从显式事实召回转向用户目标、价值和约束的一致应用。 |
| 2026-07 | [Mem-Gallery](https://aclanthology.org/2026.acl-long.1892/) <!-- benchmark-id:mem-gallery --> | Agent Memory | 🔭 前沿 | 视觉保留、多模态推理和记忆组织被放进同一套评测。 |
| 2026-07 | [Mem2ActBench](https://aclanthology.org/2026.acl-long.370/) <!-- benchmark-id:mem2actbench --> | Agent Memory | 🔭 前沿 | 记忆对行动的作用可以直接评分，而不再只通过问答间接判断。 |
| 2026-07 | [PerMemSafe](https://aclanthology.org/2026.findings-acl.320/) <!-- benchmark-id:permemsafe --> | Agent Memory | 🔭 前沿 | 把用户状态记忆扩展到随时间变化的个性化安全与有用性权衡。 |
| 2026-06-23 | [MEMPROBE](https://arxiv.org/abs/2606.24595) <!-- benchmark-id:memprobe --> | Agent Memory | 🔭 前沿 | 由下游回答间接推断记忆，转为直接审计记忆产物本身。 |
| 2026-06-22 | [DynamicMem](https://arxiv.org/abs/2606.22877) <!-- benchmark-id:dynamicmem --> | Agent Memory | 🔭 前沿 | 把用户记忆推进到百万 token、长期漂移和跨应用隐式证据。 |
| 2026-06-22 | [StatABench](https://arxiv.org/abs/2606.22977) <!-- benchmark-id:statabench --> | Data Agents | 🔭 前沿 | 把封闭式统计问答和工具调用与端到端开放建模纳入同一套能力坐标。 |
| 2026-06-17 | [GateMem](https://arxiv.org/abs/2606.18829) <!-- benchmark-id:gatemem --> | Agent Memory | 🔭 前沿 | 长期记忆由单用户私有存储扩展到带权限和遗忘义务的共享治理。 |
| 2026-06-13 | [IRTS-ToolBench](https://arxiv.org/abs/2606.15107) <!-- benchmark-id:irts-toolbench --> | Data Agents | 🔭 前沿 | 把规则采样这一默认假设移除，直接测量非规则性处理与工具落地推理。 |
| 2026-06-11 | [EvoBrowseComp](https://arxiv.org/abs/2606.13120) <!-- benchmark-id:evobrowsecomp --> | RAG / Agentic Retrieval | 🔭 前沿 | 引入可自动更新的双语实时网络问题生成流程，以降低静态测试集污染。 |
| 2026-06-11 | [LoHoSearch](https://arxiv.org/abs/2606.12837) <!-- benchmark-id:lohosearch --> | RAG / Agentic Retrieval | 🔭 前沿 | 用知识图谱系统控制搜索空间与结构复杂度，而非仅依赖人工主观设难。 |
| 2026-06-03 | [MPBench](https://arxiv.org/abs/2606.04329) <!-- benchmark-id:mpbench --> | Agent Memory | ↗ 过渡 | 从同会话 prompt injection 推进到分离写入与检索会话的 persistent poisoning。 |
| 2026-06 | [LifeSide](https://arxiv.org/abs/2606.04660) <!-- benchmark-id:lifeside --> | Agent Memory | 🔭 前沿 | 记忆开始与持续用户建模、隐私边界和环境情境一起考察。 |
| 2026-05-28 | [WorldMemArena](https://arxiv.org/abs/2605.29341) <!-- benchmark-id:worldmemarena --> | Agent Memory | 🔭 前沿 | 把记忆拆成可诊断的写入、维护、检索和使用四个阶段。 |
| 2026-05-27 | [LiveBrowseComp](https://arxiv.org/abs/2605.28721) <!-- benchmark-id:livebrowsecomp --> | RAG / Agentic Retrieval | 🔭 前沿 | 使用构建前 90 天内的事实，并以闭卷和移除答案来源实验区分发现与验证。 |
| 2026-05-19 | [ScholarQuest](https://arxiv.org/abs/2606.20235) <!-- benchmark-id:scholarquest --> | RAG / Agentic Retrieval | 🔭 前沿 | 把学术搜索定义为集合检索，并提供统一的大规模后端、意图切片和效率指标。 |
| 2026-05-18 | [EvoMemBench](https://arxiv.org/abs/2605.18421) <!-- benchmark-id:evomembench --> | Agent Memory | 🔭 前沿 | 把分散的问答、工具、搜索和具身任务组织成自演化记忆的共同坐标系。 |
| 2026-05-14 | [GroupMemBench](https://arxiv.org/abs/2605.14498) <!-- benchmark-id:groupmembench --> | Agent Memory | 🔭 前沿 | 长期记忆由单用户双边对话扩展到具有参与者和群体结构的共享交流。 |
| 2026-05-14 | [MemEye](https://arxiv.org/abs/2605.15128) <!-- benchmark-id:memeye --> | Agent Memory | 🔭 前沿 | 系统必须保留真正必要的视觉信息，不能只依赖图片描述。 |
| 2026-05-14 | [MEMLENS](https://arxiv.org/abs/2605.14906) <!-- benchmark-id:memlens --> | Agent Memory | 🔭 前沿 | 在统一长度轴上比较原生长上下文模型与外部记忆智能体的视觉记忆。 |
| 2026-05-12 | [MedMemoryBench](https://arxiv.org/abs/2605.11814) <!-- benchmark-id:medmemorybench --> | Agent Memory | 🔭 前沿 | 由静态历史问答转向边构建记忆边评测的高风险纵向场景。 |
| 2026-05-04 | [DataClawBench](https://arxiv.org/abs/2605.02503) <!-- benchmark-id:dataclawbench --> | Data Agents | 🔭 前沿 | 把数据源和模式发现从默认前提变成被测能力，并用里程碑区分有效进展与无效探索。 |
| 2026-05 | [LongMemEval-V2](https://arxiv.org/abs/2605.12493) <!-- benchmark-id:longmemeval-v2 --> | Agent Memory | 🔭 前沿 | 智能体积累的环境经验成为记忆对象，而不只是用户历史。 |
| 2026-05 | [SGR-Bench](https://arxiv.org/abs/2605.22219) <!-- benchmark-id:sgr-bench --> | RAG / Agentic Retrieval | 🔭 前沿 | 找到正确来源和把来源配置到正确状态，被拆成两个问题。 |
| 2026-04-30 | [Bright-Pro](https://aclanthology.org/2026.acl-long.1705/) <!-- benchmark-id:bright-pro --> | RAG / Agentic Retrieval | 🔭 前沿 | 把 BRIGHT 的窄正例排序扩展为多要点证据组合，并纳入迭代搜索中的检索器贡献。 |
| 2026-04-19 | [MuDABench](https://aclanthology.org/2026.findings-acl.341/) <!-- benchmark-id:mudabench --> | RAG / Agentic Retrieval | 🔭 前沿 | 把多文档问答从少量支持文档扩展到集合级分析，并增加中间事实覆盖诊断。 |
| 2026-04-17 | [MemEvoBench](https://arxiv.org/abs/2604.15774) <!-- benchmark-id:memevobench --> | Agent Memory | 🔭 前沿 | 把记忆安全从单次攻击扩展为持续更新中的行为漂移。 |
| 2026-04-15 | [MERRIN](https://arxiv.org/abs/2604.13418) <!-- benchmark-id:merrin --> | RAG / Agentic Retrieval | 🔭 前沿 | 加入无模态提示的图像、视频、音频和图表证据，以及冲突与噪声来源。 |
| 2026-04-14 | [EnterpriseRAG-Bench](https://arxiv.org/abs/2605.05253) <!-- benchmark-id:enterpriserag-bench --> | RAG / Agentic Retrieval | 🔭 前沿 | 引入跨九类企业来源保持一致的合成公司语料，并系统加入噪声、重复和冲突。 |
| 2026-04-09 | [ImplicitMemBench](https://aclanthology.org/2026.acl-long.1301/) <!-- benchmark-id:implicitmembench --> | Agent Memory | 🔭 前沿 | 由询问模型记得什么，转向观察经历是否会自动改变行为。 |
| 2026-04-07 | [LeakDojo](https://aclanthology.org/2026.findings-acl.287/) <!-- benchmark-id:leakdojo --> | RAG / Agentic Retrieval | 🔭 前沿 | 把数据库抽取攻击、模型、语料、查询预算和防御纳入同一可控安全诊断框架。 |
| 2026-04-01 | [AutoResearchBench](https://arxiv.org/abs/2604.25256) <!-- benchmark-id:autoresearchbench --> | RAG / Agentic Retrieval | 🔭 前沿 | 区分找到一篇目标论文与穷举未知规模论文集合，使搜索停止策略可测。 |
| 2026-03-12 | [AgentFuel](https://arxiv.org/abs/2603.12483) <!-- benchmark-id:agentfuel --> | Data Agents | 🔭 前沿 | 从通用静态问答转向可按领域定制、依赖历史状态和事件上下文的评测。 |
| 2026-03-05 | [TML-Bench](https://arxiv.org/abs/2603.05764) <!-- benchmark-id:tml-bench --> | Data Agents | 🔭 前沿 | 从单次代码或得分比较扩展到时间—性能曲线、成功率与多次运行稳定性。 |
| 2026-03 | [Data Agent Benchmark (DAB)](https://arxiv.org/abs/2603.20576) <!-- benchmark-id:data-agent-benchmark --> | Data Agents | 🔭 前沿 | 企业数据问题从单条 SQL 扩展到跨数据库流程。 |
| 2026-03 | [LifeBench](https://arxiv.org/abs/2603.03781) <!-- benchmark-id:lifebench --> | Agent Memory | 🔭 前沿 | 评测不再局限于显式事实，也覆盖习惯和做事方法。 |
| 2026-02-27 | [DARE-bench](https://arxiv.org/abs/2602.24288) <!-- benchmark-id:dare-bench --> | Data Agents | 🔭 前沿 | 不再只看最终预测分数，还客观检查智能体是否按要求完成了过程。 |
| 2026-02-26 | [MTRAG-UN](https://aclanthology.org/2026.findings-acl.503/) <!-- benchmark-id:mtrag-un --> | RAG / Agentic Retrieval | 🔭 前沿 | 在常规多轮检索与生成之外，加入了四类可诊断的会话失败情形。 |
| 2026-02-22 | [MC-Search](https://arxiv.org/abs/2603.00873) <!-- benchmark-id:mc-search --> | RAG / Agentic Retrieval | 🔭 前沿 | 从只看最终答案推进到带结构的多模态搜索链与逐步规划、检索诊断。 |
| 2026-02-18 | [MemoryArena](https://arxiv.org/abs/2602.16313) <!-- benchmark-id:memoryarena --> | Agent Memory | 🔭 前沿 | 长期记忆与未来任务行动被放到同一项评测中。 |
| 2026-02-06 | [GISA](https://arxiv.org/abs/2602.08543) <!-- benchmark-id:gisa --> | RAG / Agentic Retrieval | 🔭 前沿 | 把人工问题、稳定与实时子集、确定性评分和完整人工搜索轨迹统一到一个基准中。 |
| 2026-02-05 | [SAGE](https://arxiv.org/abs/2602.05975) <!-- benchmark-id:sage --> | RAG / Agentic Retrieval | 🔭 前沿 | 把科学检索拆成定向与开放式任务，并显式比较智能体与检索器的适配关系。 |
| 2026-02-03 | [MemGUI-Bench](https://arxiv.org/abs/2602.06075) <!-- benchmark-id:memgui-bench --> | Agent Memory | 🔭 前沿 | 把记忆从对话问答带入可执行的移动 GUI 行为与重复任务学习。 |
| 2026-02 | [AgenticRAGTracer](https://arxiv.org/abs/2602.19127) <!-- benchmark-id:agenticragtracer --> | RAG / Agentic Retrieval | 🔭 前沿 | 能够定位整条轨迹究竟在哪一步失败。 |
| 2026-02 | [AMA-Bench](https://arxiv.org/abs/2602.22769) <!-- benchmark-id:ama-bench --> | Agent Memory | 🔭 前沿 | 记忆来源从对话扩展到带有因果结构的环境经历。 |
| 2026-02 | [StructMemEval](https://arxiv.org/abs/2602.11243) <!-- benchmark-id:structmemeval --> | Agent Memory | 🔭 前沿 | 记忆的组织方式本身成为可观察能力。 |
| 2026-01-22 | [DSGym](https://arxiv.org/abs/2601.16344) <!-- benchmark-id:dsgym --> | Data Agents | 🔭 前沿 | 把碎片化基准统一到同一执行接口，并显式检查任务是否真的需要使用数据。 |
| 2026-01-20 | [DSAEval](https://arxiv.org/abs/2601.13591) <!-- benchmark-id:dsaeval --> | Data Agents | 🔭 前沿 | 从单轮表格任务推进到需要多模态感知和项目上下文累积的真实问题序列。 |
| 2026-01-15 | [CAME-Bench](https://aclanthology.org/2026.findings-acl.584/) <!-- benchmark-id:came-bench --> | Agent Memory | 🔭 前沿 | 把长程检索中的语义相似干扰和目标上下文错配显式化。 |
| 2026-01 | [RealMem](https://aclanthology.org/2026.findings-acl.703/) <!-- benchmark-id:realmem --> | Agent Memory | 🔭 前沿 | 评测由一般对话历史走向持续变化的项目状态与用户目标。 |
| 2025-12 | [DAComp](https://arxiv.org/abs/2512.04324) <!-- benchmark-id:dacomp --> | Data Agents | 🔭 前沿 | 数据工程与分析被放进更完整的数据智能生命周期。 |
| 2025-11-30 | [DDR-Bench](https://arxiv.org/abs/2602.02039) <!-- benchmark-id:ddr-bench --> | Data Agents | 🔭 前沿 | 把评价对象从“完成给定分析问题”改为“自己判断什么值得调查并证明发现”。 |
| 2025-10-22 | [LIT-RAGBench](https://arxiv.org/abs/2603.06198) <!-- benchmark-id:lit-ragbench --> | RAG / Agentic Retrieval | 🔭 前沿 | 隔离检索质量影响，在统一双语协议下诊断五类 RAG 生成能力。 |
| 2025-10-18 | [AgentDS](https://arxiv.org/abs/2603.19005) <!-- benchmark-id:agentds --> | Data Agents | ↗ 过渡 | 把领域专家贡献和人机协作设为直接比较轴，而不只比较自主智能体。 |
| 2025-10 | [BEAM](https://arxiv.org/abs/2510.27246) <!-- benchmark-id:beam --> | Agent Memory | ↗ 过渡 | 直接观察超大规模连续历史下的记忆退化。 |
| 2025-10 | [RAGCap-Bench](https://arxiv.org/abs/2510.13910) <!-- benchmark-id:ragcap-bench --> | RAG / Agentic Retrieval | 🔭 前沿 | 中间能力可以独立诊断，不必只从最终答案倒推原因。 |
| 2025-09 | [FDABench](https://arxiv.org/abs/2509.02473) <!-- benchmark-id:fdabench --> | Data Agents | 🔭 前沿 | 异构分析、推理过程、延迟和 token 成本可以同时观察。 |
| 2025-08 | [BrowseComp-Plus](https://arxiv.org/abs/2508.06600) <!-- benchmark-id:browsecomp-plus --> | RAG / Agentic Retrieval | ↗ 过渡 | 固定且经过核验的语料降低了实时搜索带来的黑箱性和复现困难。 |
| 2025-07 | [MemoryAgentBench](https://arxiv.org/abs/2507.05257) <!-- benchmark-id:memoryagentbench --> | Agent Memory | ↗ 过渡 | 记忆由读取静态历史，变成持续吸收、更新、使用和遗忘的在线过程。 |
| 2025-06-30 | [DABstep](https://arxiv.org/abs/2506.23719) <!-- benchmark-id:dabstep --> | Data Agents | ↗ 过渡 | 从单表或单步问答转向跨数据与文档的长链推理，并保持结果精确可自动核验。 |
| 2025-06-06 | [KramaBench](https://arxiv.org/abs/2506.06541) <!-- benchmark-id:kramabench --> | Data Agents | ↗ 过渡 | 把问题从“给定数据写代码”推进到“在整个数据湖中找到证据并交付可运行管线”。 |
| 2025-06 | [DeepResearch Bench](https://arxiv.org/abs/2506.11763) <!-- benchmark-id:deepresearch-bench --> | RAG / Agentic Retrieval | ↗ 过渡 | 目标不再只是找到短答案，还要交付完整研究报告。 |
| 2025-06 | [MemBench](https://arxiv.org/abs/2506.21605) <!-- benchmark-id:membench --> | Agent Memory | ↗ 过渡 | 评测范围由答题准确率扩展到记忆层次、交互角色和资源开销。 |
| 2025-05-28 | [LiveSQLBench](https://livesqlbench.ai/) <!-- benchmark-id:livesqlbench --> | Data Agents | 🔭 前沿 | 把静态 Text-to-SQL 推进到带隐藏更新、大模式、业务知识和数据库写操作的持续评测。 |
| 2025-05-14 | [T²-RAGBench](https://aclanthology.org/2026.eacl-long.8/) <!-- benchmark-id:t2-ragbench --> | RAG / Agentic Retrieval | ↗ 过渡 | 去除原有问答数据的先验正确上下文，使检索和数值推理能够端到端联合评测。 |
| 2025-05-12 | [MLE-Dojo](https://arxiv.org/abs/2505.07782) <!-- benchmark-id:mle-dojo --> | Data Agents | ↗ 过渡 | 从 terminal submission 评分推进到带执行和真实分数反馈的训练/评测轨迹。 |
| 2025-04 | [BrowseComp](https://arxiv.org/abs/2504.12516) <!-- benchmark-id:browsecomp --> | RAG / Agentic Retrieval | ↗ 过渡 | 任务从单次检索扩展为持续的信息搜寻。 |
| 2025-02 | [DataSciBench](https://arxiv.org/abs/2502.13897) <!-- benchmark-id:datascibench --> | Data Agents | ↗ 过渡 | 任务范围扩大后，不同分析目标开始使用各自合适的评判器。 |
| 2024-11 | [Spider 2.0](https://arxiv.org/abs/2411.07763) <!-- benchmark-id:spider-2 --> | Data Agents | ↗ 过渡 | 一次语义解析被扩展为长程企业任务。 |
| 2024-10-09 | [MLE-bench](https://arxiv.org/abs/2410.07095) <!-- benchmark-id:mle-bench --> | Data Agents | 🧱 基石 | 把 end-to-end ML engineering 做成 75 个 from-scratch、human-relative 的竞赛环境。 |
| 2024-10 | [DA-Code](https://aclanthology.org/2024.emnlp-main.748/) <!-- benchmark-id:da-code --> | Data Agents | ↗ 过渡 | 在静态代码题与智能体式数据工作之间建立了可执行的过渡任务。 |
| 2024-10 | [LongMemEval](https://arxiv.org/abs/2410.10813) <!-- benchmark-id:longmemeval --> | Agent Memory | 🧱 基石 | 将更新、时间推理和拒答从笼统的事实召回中拆分出来。 |
| 2024-08 | [LoCoMo](https://aclanthology.org/2024.acl-long.747/) <!-- benchmark-id:locomo --> | Agent Memory | 🧱 基石 | 在 Beyond Goldfish Memory 的基础上，形成了可复用的超长对话多任务评测。 |
| 2024-07 | [BRIGHT](https://arxiv.org/abs/2407.12883) <!-- benchmark-id:bright --> | RAG / Agentic Retrieval | ↗ 过渡 | 暴露仅靠语义相似度难以解决的检索任务。 |
| 2024-07 | [InsightBench](https://arxiv.org/abs/2407.06423) <!-- benchmark-id:insightbench --> | Data Agents | ↗ 过渡 | 目标从完成指定代码任务扩展到发现并表达有用结论。 |
| 2024-07 | [RAGBench](https://arxiv.org/abs/2407.11005) <!-- benchmark-id:ragbench --> | RAG / Agentic Retrieval | ↗ 过渡 | 评判器质量和可用于诊断的错误标签也成为评测对象。 |
| 2024-06 | [CRAG](https://arxiv.org/abs/2406.04744) <!-- benchmark-id:crag --> | RAG / Agentic Retrieval | ↗ 过渡 | 新鲜度、事实变化和长尾知识进入 RAG 评测。 |
| 2024-01 | [MultiHop-RAG](https://arxiv.org/abs/2401.15391) <!-- benchmark-id:multihop-rag --> | RAG / Agentic Retrieval | ↗ 过渡 | 多跳任务的错误可以落到检索或推理环节，而不只看最终答案。 |
| 2024-01 | [RAGTruth](https://arxiv.org/abs/2401.00396) <!-- benchmark-id:ragtruth --> | RAG / Agentic Retrieval | ↗ 过渡 | 忠实度问题由整题标签细化到具体文本片段。 |
| 2023-10 | [MLAgentBench](https://arxiv.org/abs/2310.03302) <!-- benchmark-id:mlagentbench --> | Data Agents | ↗ 过渡 | 一次性代码生成变成由执行反馈驱动的实验过程。 |
| 2023-09 | [RGB](https://arxiv.org/abs/2309.01431) <!-- benchmark-id:rgb --> | RAG / Agentic Retrieval | 🧱 基石 | “能否正确使用检索内容”被拆成几项独立能力。 |
| 2023-05 | [BIRD](https://arxiv.org/abs/2305.03111) <!-- benchmark-id:bird --> | Data Agents | ↗ 过渡 | Text-to-SQL 开始面对数据值丰富但不整洁的数据库，SQL 效率也纳入评测。 |
| 2022-11 | [DS-1000](https://arxiv.org/abs/2211.11501) <!-- benchmark-id:ds-1000 --> | Data Agents | 🧱 基石 | 在 SQL 之外建立了可复现的实用数据科学代码评测。 |
| 2022-05 | [Beyond Goldfish Memory](https://aclanthology.org/2022.acl-long.356/) <!-- benchmark-id:beyond-goldfish-memory --> | Agent Memory | 🌱 前身 | 跨会话的对话连续性由此成为独立评测问题。 |
| 2021-04 | [BEIR](https://arxiv.org/abs/2104.08663) <!-- benchmark-id:beir --> | RAG / Agentic Retrieval | 🧱 基石 | 不再用单一 IR 数据集的最好成绩代替跨域鲁棒性。 |
| 2020-09 | [KILT](https://arxiv.org/abs/2009.02252) <!-- benchmark-id:kilt --> | RAG / Agentic Retrieval | 🧱 基石 | 正确性与来源追踪被放进共享、可复用的评测基础设施。 |
| 2018-10 | [HotpotQA](https://aclanthology.org/D18-1259/) <!-- benchmark-id:hotpotqa --> | RAG / Agentic Retrieval | 🌱 前身 | 多文档证据组合和可解释支撑事实由此成为可测目标。 |
| 2018-10 | [Spider](https://aclanthology.org/D18-1425/) <!-- benchmark-id:spider --> | Data Agents | 🧱 基石 | Text-to-SQL 从单表生成走向复杂查询和跨 schema 泛化。 |
| 2017-08 | [WikiSQL](https://arxiv.org/abs/1709.00103) <!-- benchmark-id:wikisql --> | Data Agents | 🌱 前身 | 大规模、可执行的自然语言数据库访问由此成为标准任务。 |<!-- COMPLETE-TIMELINE:END -->

## 按领域浏览（全部）

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
| ↗ 过渡 | [MPBench](https://arxiv.org/abs/2606.04329) <!-- benchmark-id:mpbench --> | 2026-06-03 | 跨会话 persistent-memory poisoning 的写入成功、条件检索成功与防御 operating point。 | 把良性 memory fidelity 扩展为跨会话 persistent poisoning。 |
| 🔭 前沿 | [GateMem](https://arxiv.org/abs/2606.18829) <!-- benchmark-id:gatemem --> | 2026-06-17 | 多人共享记忆能否同时保持可用、阻止越权泄露并执行删除请求。 | 长期记忆由单用户私有存储扩展到带权限和遗忘义务的共享治理。 |
| 🔭 前沿 | [DynamicMem](https://arxiv.org/abs/2606.22877) <!-- benchmark-id:dynamicmem --> | 2026-06-22 | 从十五个月、多个应用的零散行为中推断并更新用户属性、习惯和偏好。 | 把用户记忆推进到百万 token、长期漂移和跨应用隐式证据。 |
| 🔭 前沿 | [MEMPROBE](https://arxiv.org/abs/2606.24595) <!-- benchmark-id:memprobe --> | 2026-06-23 | 普通协助结束后，能否从智能体留下的记忆产物中恢复隐藏的用户状态。 | 由下游回答间接推断记忆，转为直接审计记忆产物本身。 |
| 🔭 前沿 | [LoCoMo-Plus](https://aclanthology.org/2026.acl-long.1150/) <!-- benchmark-id:locomo-plus --> | 2026-07 | 后续问题没有复述旧约束时，能否继续正确应用它。 | 目标从显式事实召回转向用户目标、价值和约束的一致应用。 |
| 🔭 前沿 | [Mem-Gallery](https://aclanthology.org/2026.acl-long.1892/) <!-- benchmark-id:mem-gallery --> | 2026-07 | 多模态长期对话中的记忆抽取、适应、推理和知识管理。 | 视觉保留、多模态推理和记忆组织被放进同一套评测。 |
| 🔭 前沿 | [Mem2ActBench](https://aclanthology.org/2026.acl-long.370/) <!-- benchmark-id:mem2actbench --> | 2026-07 | 长期记忆是否会影响工具选择和参数填写。 | 记忆对行动的作用可以直接评分，而不再只通过问答间接判断。 |
| 🔭 前沿 | [PerMemSafe](https://aclanthology.org/2026.findings-acl.320/) <!-- benchmark-id:permemsafe --> | 2026-07 | 能否从长期历史中识别隐含的个体风险，并在风险缓解后及时更新判断。 | 把用户状态记忆扩展到随时间变化的个性化安全与有用性权衡。 |
| 🔭 前沿 | [MemFuseBench](https://arxiv.org/abs/2608.18704) <!-- benchmark-id:memfusebench --> | 2026-07-21 | 跨异构事件流的来源连接、因果融合、冲突裁决与溯源记忆基准。 | 跨异构来源的 linking、causal fusion、conflict 与 provenance 被拆成诊断项。 |
| 🔭 前沿 | [InMind](https://arxiv.org/abs/2607.24368) <!-- benchmark-id:inmind --> | 2026-07-27 | 旧事实与新问题词义相远、只有借助常识才能建立联系时，记忆能否被正确调出并应用。 | 用成对对照把存储失败、知识缺失、检索路由失败和应用失败分开。 |
| 🔭 前沿 | [PAST-Bench](https://arxiv.org/abs/2608.04003) <!-- benchmark-id:past-bench --> | 2026-08-04 | 通过配对持久状态控制，检验跨 episode 经验是否因果改善后续可执行工作的基准。 | 用 persistence on/off 配对控制识别跨 episode 记忆是否真的改善可执行任务。 |
| 🔭 前沿 | [SP-Mem Privacy-Aware Memory Benchmark](https://arxiv.org/abs/2608.16551) <!-- benchmark-id:sp-mem --> | 2026-08-17 | 联合测量回答质量、个性化、同意处理、精确值暴露与成本的隐私感知记忆基准。 | 把个性化收益、授权与泄露风险放进同一记忆生命周期协议。 |
| 🔭 前沿 | [MemTrapBench](https://arxiv.org/abs/2608.20202) <!-- benchmark-id:memtrapbench --> | 2026-08-20 | 同题 memory/no-memory 对照下，相关历史记忆是否会造成 reasoning fixation 或 belief distortion。 | 把“能否回忆”推进到“回忆到的内容是否应该被当前任务采用”。 |
| 🔭 前沿 | [StateMemBench](https://arxiv.org/abs/2608.19652) <!-- benchmark-id:statemembench --> | 2026-08-20 | 多会话状态修订中的 current-vs-superseded 跟踪、依赖更新与 stale-state 抵抗。 | 把 stale-state failure 从检索失败与一般推理失败中单独隔离并评分。 |
| 🔭 前沿 | [Agent Memory Bakeoff](https://github.com/JaysonRawlins/agent-memory-bakeoff) <!-- benchmark-id:agent-memory-bakeoff --> | 2026-08-21 | 交叉比较检索策略与写入时 enrichment，测合成组织记忆中的跨词汇检索。 | 把 memory write enrichment 作为可控干预，与三类检索策略直接交叉。 |
| 🔭 前沿 | [DreamBench-SWE](https://arxiv.org/abs/2608.20664) <!-- benchmark-id:dreambench-swe --> | 2026-08-21 | 用隐藏 oracle 执行式评测多会话软件 agent 的 memory hygiene。 | 把受控 repository continuation 与保持、过期、作用域、权威、组合、source-of-truth、错误经验拒绝和弃答放入同一协议。 |
| 🔭 前沿 | [Utility Under Attack](https://arxiv.org/abs/2608.21230) <!-- benchmark-id:utility-under-attack --> | 2026-08-21 | 虚假记忆下的良性 utility 保留，以及筛查与 provenance ranking 的防御代价。 | 把 retained utility 与 defense-induced evidence loss 设为安全评价对象。 |
| 🔭 前沿 | [Agent Memory Bench (coding agents)](https://github.com/GiulioDER/agent-memory-bench) <!-- benchmark-id:agent-memory-bench-coding --> | 2026-08-22 | 在真实仓库任务中用 neutral feed、proof-of-treatment 与隐藏执行 oracle 测跨任务记忆是否改善编码行动。 | 将 PAST-Bench 式持久状态对照推进到产品可插拔 coding memory，并显式核验 treatment。 |
| 🔭 前沿 | [membench (staleness)](https://github.com/Ps23102004/membench) <!-- benchmark-id:membench-staleness --> | 2026-08-22 | 用 current-vs-stale 排序、弃答与泄露防护诊断 memory store 的更新和冲突处理。 | 修正 top-k staleness 并关闭 abstention gaming，使 stale-fact 排名更可解释。 |
| 🔭 前沿 | [InjecMEM](https://arxiv.org/abs/2608.23471) <!-- benchmark-id:injecmem --> | 2026-08-24 | 单次无特权交互写入后，恶意记忆的检索成功、条件生成与端到端攻击成功。 | 把 write→drift→retrieve→generate 做成端到端攻击轨迹。 |
| 🔭 前沿 | [The Compaction Cliff](https://arxiv.org/abs/2608.22752) <!-- benchmark-id:compaction-cliff --> | 2026-08-24 | 反复压缩、分解与检索中的安全约束精确保留及下游行动遵从。 | 把安全规则的 exact preservation 绑定到三类 context operator 和行为。 |
| 🔭 前沿 | [SCALE-QA](https://arxiv.org/abs/2608.25655) <!-- benchmark-id:scale-qa --> | 2026-08-26 | 无显式边界的交错长对话中重建当前任务真正绑定的 episode 与局部约束。 | 从 LongMemEval 的结构化跨 session 记忆推进到 episode boundary 本身未知的混合线程，并用精确 evidence trace 区分可见性与 episode integrity。 |
<!-- COMPLETE-MAP:agent-memory:END -->

[进入 Agent Memory Radar](https://github.com/H20Zhang/Agent-Memory-Radar)

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
| 🔭 前沿 | [LitReview Arena / LitReviewBench / LitJudge](https://arxiv.org/abs/2608.21374) <!-- benchmark-id:litreview-arena --> | 2026-07-01 | 领域专家对文献综述的覆盖、依据、结构、研究建议与总体 utility 做 pairwise 评价。 | 用领域专家偏好数据校准开放式综述 judge。 |
| 🔭 前沿 | [WANDR](https://arxiv.org/abs/2608.14747) <!-- benchmark-id:wandr --> | 2026-07-14 | 面向实时网页 wide-and-deep 记录收集的基准，包含分层任务和无需穷举金标的逐条核验。 | 把实时网页上的开放集合发现、记录扩充与逐条复核合成 wide-and-deep 任务。 |
| 🔭 前沿 | [VAKRA](https://arxiv.org/abs/2608.12282) <!-- benchmark-id:vakra --> | 2026-08 | 组合调用 API、检索文档、完成多跳推理，并遵守工具策略。 | 跨来源依据、实际执行和策略一致性出现在同一条轨迹中。 |
| 🔭 前沿 | [MAPLE](https://arxiv.org/abs/2608.15624) <!-- benchmark-id:maple --> | 2026-08-04 | 测量同一论文能否在动机、方法与结果等多个 aspect 下持续被找回的科学检索基准。 | 不再只问一条 query 是否命中，而是测同一论文跨多个 aspect 的可检索一致性。 |
| 🔭 前沿 | [SearchAuditBench](https://arxiv.org/abs/2608.05212) <!-- benchmark-id:searchauditbench --> | 2026-08-05 | 考察审计模型能否在超长搜索轨迹中定位错误、归因根因并生成可执行修复。 | 从最终答案成败推进到专家标注的关键步骤、六类根因和修复后恢复评测。 |
| 🔭 前沿 | [DAS-Bench / DAS-Eval](https://arxiv.org/abs/2608.18034) <!-- benchmark-id:das-bench --> | 2026-08-07 | 对文献覆盖、taxonomy、claim、citation、discourse 与渲染成品质量评分的学术综述基准及评测器。 | 把学术综述的覆盖、taxonomy、claim、citation、discourse 与成品质量变成 16 项协议。 |
| 🔭 前沿 | [The Recall Trap](https://arxiv.org/abs/2608.14838) <!-- benchmark-id:recall-trap --> | 2026-08-10 | 有效性审计：在固定槽位代码检索协议下，更高 file recall 可能降低下游修复成功率。 | 证明固定槽位下更高 file recall 可能对应更低 repair success，限制 recall 指标的解释。 |
| 🔭 前沿 | [The Commercial Tax](https://arxiv.org/abs/2608.16096) <!-- benchmark-id:commercial-tax --> | 2026-08-17 | 把原始 embedder 分数绑定到许可、query format、索引构造与部署成本的检索复现性审计。 | 把 license、query format、index construction 与 cost 纳入 retrieval number 的可迁移性审计。 |
| 🔭 前沿 | [BrowseComp-Plus_CM](https://arxiv.org/abs/2608.20317) <!-- benchmark-id:browsecomp-plus-cm --> | 2026-08-18 | 在独立构建的 5.53 亿文档 ClimbMix 语料中，测多跳证据发现、答案正确率、evidence recall 与工具调用。 | 以 matched corpus swap 限定 BrowseComp-Plus：固定语料还不足以控制 query-conditioned construction 与规模。 |
| 🔭 前沿 | [VisDocAgentBench](https://arxiv.org/abs/2608.17889) <!-- benchmark-id:visdocagentbench --> | 2026-08-18 | 在统一页面排序协议下比较静态 ranker 与迭代视觉/OCR agent 的视觉文档检索基准。 | 在统一 top-10 输出下直接比较静态视觉检索与迭代式页面发现、检查。 |
| 🔭 前沿 | [KBGym / Training a Knowledge Base](https://arxiv.org/abs/2608.21829) <!-- benchmark-id:kbgym --> | 2026-08-22 | 监督式知识库编辑在冻结后对覆盖分层问题的准确率与行动成本。 | 把 static corpus 改成受监督编辑后冻结评测的 non-parametric model。 |
| 🔭 前沿 | [RAG Collapse](https://arxiv.org/abs/2608.22118) <!-- benchmark-id:rag-collapse --> | 2026-08-22 | 递归检索中 self-authored sources 对独立来源的挤出与反馈崩塌。 | 把 self-authored source feedback 变成独立 validity diagnostic。 |
| 🔭 前沿 | [Snapshot Compatibility Audit](https://arxiv.org/abs/2608.22856) <!-- benchmark-id:snapshot-compatibility-audit --> | 2026-08-24 | corpus snapshot 增长造成的超额答案 churn 与稳定翻转。 | 把 corpus 版本升级引发的稳定答案翻转从随机生成噪声中隔离。 |<!-- COMPLETE-MAP:rag:END -->

[进入 Agentic RAG Radar](https://github.com/H20Zhang/Agentic-RAG-Radar)

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
| 🧱 基石 | [MLE-bench](https://arxiv.org/abs/2410.07095) <!-- benchmark-id:mle-bench --> | 2024-10-09 | 在重建 Kaggle 环境中从零完成端到端 ML engineering，并按历史私榜 medal threshold 评分。 | 建立 from-scratch、human-relative 的端到端 ML engineering 基石。 |
| ↗ 过渡 | [Spider 2.0](https://arxiv.org/abs/2411.07763) <!-- benchmark-id:spider-2 --> | 2024-11 | 在巨大 schema、多种 SQL 方言、元数据、代码库和云数据库中完成企业 SQL 工作流。 | 一次语义解析被扩展为长程企业任务。 |
| ↗ 过渡 | [DataSciBench](https://arxiv.org/abs/2502.13897) <!-- benchmark-id:datascibench --> | 2025-02 | 覆盖多类数据科学任务，并为不同任务配置程序化指标和人工核验答案。 | 任务范围扩大后，不同分析目标开始使用各自合适的评判器。 |
| ↗ 过渡 | [MLE-Dojo](https://arxiv.org/abs/2505.07782) <!-- benchmark-id:mle-dojo --> | 2025-05-12 | 在 Gym-style 环境中用代码执行、错误与 HumanRank 反馈迭代 ML engineering 轨迹。 | 加入可训练交互环境、分数反馈和 train/eval split。 |
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
| 🔭 前沿 | [data-eng-bench](https://github.com/Snowflake-Labs/data-eng-bench) <!-- benchmark-id:data-eng-bench --> | 2026-07-29 | 面向仓库规模 dbt 转换的可执行数据工程基准，在 DuckDB 与 Snowflake 上做隐藏行级核验。 | 用可执行 dbt 任务和隐藏行级核验测数据工程；8 月修复暴露 evaluator reliability 也是测量对象。 |
| 🔭 前沿 | [DataSpace](https://arxiv.org/abs/2608.03451) <!-- benchmark-id:dataspace --> | 2026-08 | 在混合数据库、文件、文档和多媒体的工作区中完成可验证分析。 | 寻找异构证据和核验完整结果成为一项统一任务。 |
| 🔭 前沿 | [DSAgentBench](https://arxiv.org/abs/2608.10366) <!-- benchmark-id:dsagentbench --> | 2026-08 | 使用笔记本、IDE、终端、浏览器和数据库完成完整数据科学工作流。 | 评测进入真实计算机环境，要求多阶段、多工具执行能够可靠衔接。 |
| 🔭 前沿 | [WarehouseReliabilityBench](https://arxiv.org/abs/2608.09254) <!-- benchmark-id:warehouse-reliability-bench --> | 2026-08-10 | 面对语义歧义、不可回答、模式漂移和对抗输入时，返回业务真值或正确地澄清、弃答、拒答。 | 从“SQL 能运行且结果匹配”转向“业务含义正确，并在不该给数字时不虚假成功”。 |
| 🔭 前沿 | [Data Exploration Benchmark](https://arxiv.org/abs/2608.16045) <!-- benchmark-id:data-exploration-benchmark --> | 2026-08-17 | 在下游分析前，构建包含逻辑表、列语义、键关系和质量信号的结构化数据理解产物。 | 把通常隐含的数据探索阶段从最终答案的前置假设变成可独立评分、可验证下游价值的对象。 |
| 🔭 前沿 | [AI4AI-Bench](https://arxiv.org/abs/2608.20318) <!-- benchmark-id:ai4ai-bench --> | 2026-08-20 | 在冻结训练仓库中诊断并修改学习算法，以 proxy 探索、源码交付和 clean-start 正式运行隔离成绩。 | 把 algorithm design 与 run-side tuning 分开观察，并以 source patch 作为探索和最终训练之间的边界。 |
| 🔭 前沿 | [DeltaML-Bench](https://arxiv.org/abs/2608.19653) <!-- benchmark-id:deltaml-bench --> | 2026-08-20 | 在真实研究仓库中修复训练管线、迭代机器学习实验、提高论文基线并抵抗 specification gaming。 | 把“改进已发表 ML 基线”与 repository realism、长算力预算和提交完整性放入同一执行对象。 |<!-- COMPLETE-MAP:data-agent:END -->

[进入 Data Agent Radar](https://github.com/H20Zhang/Data-Agent-Radar)

## Protocol Audits

- [DSAgentBench](../benchmarks/dsagentbench.md)
- [DataSpace](../benchmarks/dataspace.md)
- [VAKRA](../benchmarks/vakra.md)
- [LoCoMo-Plus](../benchmarks/locomo-plus.md)

## 按 Genealogy 阅读

| Role | 读法 |
|---|---|
| 🌱 前身 | 问题最初如何被形式化 |
| 🧱 基石 | 后续工作继承了什么坐标系 |
| ↗ 过渡 | 哪个旧限制开始被显式修正 |
| 🔭 前沿 | 当前正在把什么变成可测对象 |

## 按 Measurement Coordinate 阅读

- **Capability：** recall、reasoning、action、analysis、tool use、verification
- **Environment：** static corpus、live web、state-gated site、heterogeneous workspace、real computer
- **Protocol：** interface、hints、retry、stopping、judge、executable validation
- **Validity / Cost：** contamination、drift、harness sensitivity、indexing/writing、token、latency、energy
- **Long-horizon state：** memory update、workflow state、persistent user/project state、irreversible actions

## 数据与方法

- [Canonical registry](../data/benchmarks.json)
- [Research compactions](../digests/README.md)
- [Curation](../CURATION.md) · [Schema](../SCHEMA.md)
