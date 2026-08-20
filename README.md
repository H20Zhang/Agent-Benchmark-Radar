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
| 2026-08 | Data Agent | [DataSpace](https://arxiv.org/abs/2608.03451) <!-- benchmark-id:dataspace --> | 在混合数据库、文件、文档和多媒体的工作区中完成可验证分析。 | 把寻找异构证据和核验完整结果放进同一项任务。 |
| 2026-08 | Data Agent | [DSAgentBench](https://arxiv.org/abs/2608.10366) <!-- benchmark-id:dsagentbench --> | 使用笔记本、IDE、终端、浏览器和数据库完成数据科学工作流。 | 评测进入真实计算机环境，结果取决于多阶段、多工具执行能否衔接。 |
| 2026-08 | RAG | [VAKRA](https://arxiv.org/abs/2608.12282) <!-- benchmark-id:vakra --> | 组合调用 API、检索文档、进行多跳推理，并遵守工具使用策略。 | 结构化 API 与非结构化检索出现在同一条可执行轨迹中。 |
| 2026-07 | Data Agent | [AgenticDataBench](https://arxiv.org/abs/2607.01647) <!-- benchmark-id:agenticdatabench --> | 用细粒度技能分类检查真实数据科学工作流的覆盖情况。 | 除了总成功率，还能看到这套基准究竟覆盖了哪些技能。 |
| 2026-07 | Agent Memory | [LoCoMo-Plus](https://aclanthology.org/2026.acl-long.1150/) <!-- benchmark-id:locomo-plus --> | 后续问题没有复述旧约束时，智能体能否继续正确应用它。 | 记忆不再只考事实召回，也考用户目标、价值和约束能否持续影响行为。 |
| 2026-07 | Agent Memory | [Mem-Gallery](https://aclanthology.org/2026.acl-long.1892/) <!-- benchmark-id:mem-gallery --> | 多模态长期对话中的记忆抽取、适应、推理和知识管理。 | 视觉信息的保留、推理和组织被放到同一套评测中。 |
| 2026-07 | Agent Memory | [Mem2ActBench](https://aclanthology.org/2026.acl-long.370/) <!-- benchmark-id:mem2actbench --> | 长期记忆是否会影响工具选择和参数填写。 | 记忆是否真正改变行动，可以直接评分，而不再只通过问答间接判断。 |
| 2026-06 | Agent Memory | [LifeSide](https://arxiv.org/abs/2606.04660) <!-- benchmark-id:lifeside --> | 跨会话记忆、用户理解、隐私控制，以及情绪与环境的相互作用。 | 长期记忆开始与持续用户建模、隐私边界和环境情境一起考察。 |
| 2026-05-14 | Agent Memory | [MemEye](https://arxiv.org/abs/2605.15128) <!-- benchmark-id:memeye --> | 细粒度视觉证据、视觉状态变化，以及纯文本捷径检查。 | 系统必须保留确实有用的视觉证据，不能只靠图片描述或文本线索。 |
| 2026-05 | Agent Memory | [LongMemEval-V2](https://arxiv.org/abs/2605.12493) <!-- benchmark-id:longmemeval-v2 --> | 从大量网页智能体轨迹中记住环境状态、操作流程和易错点。 | 记忆对象从用户历史扩展到智能体在环境中积累的经验。 |
| 2026-05 | RAG | [SGR-Bench](https://arxiv.org/abs/2605.22219) <!-- benchmark-id:sgr-bench --> | 当证据受站点筛选条件、层级、范围或视图状态控制时完成搜索。 | 找到正确来源和把来源配置到正确状态，被拆成两个问题。 |
| 2026-03 | Data Agent | [Data Agent Benchmark (DAB)](https://arxiv.org/abs/2603.20576) <!-- benchmark-id:data-agent-benchmark --> | 跨多个 DBMS 完成数据集成、转换、分析和可执行核验。 | 企业数据问题从单条 SQL 扩展到跨数据库的完整流程。 |
| 2026-03 | Agent Memory | [LifeBench](https://arxiv.org/abs/2603.03781) <!-- benchmark-id:lifebench --> | 从多源长期轨迹中保留事件、语义、习惯和程序性知识。 | 评测内容超出显式事实，开始覆盖习惯与做事方法。 |
| 2026-02-18 | Agent Memory | [MemoryArena](https://arxiv.org/abs/2602.16313) <!-- benchmark-id:memoryarena --> | 在跨会话的智能体—环境循环中，用早期行动和反馈指导后续行动。 | 长期记忆和未来任务执行不再分开测试。 |
| 2026-02 | RAG | [AgenticRAGTracer](https://arxiv.org/abs/2602.19127) <!-- benchmark-id:agenticragtracer --> | 逐跳核验多步检索与推理过程，并检查步骤分配。 | 最终答案之外，还能定位整条轨迹在哪一步出错。 |
| 2026-02 | Agent Memory | [AMA-Bench](https://arxiv.org/abs/2602.22769) <!-- benchmark-id:ama-bench --> | 在真实和可扩展合成的智能体—环境轨迹上测试长程记忆。 | 记忆来源从人机对话扩展到带有因果关系的环境经历。 |
| 2026-02 | Agent Memory | [StructMemEval](https://arxiv.org/abs/2602.11243) <!-- benchmark-id:structmemeval --> | 智能体能否按任务需要维护账本、列表、树等记忆结构。 | 不只考能否找回事实，也考记忆是怎样组织的。 |
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
| **Agent Memory** | 跨会话回忆 → 时间、更新与遗忘 → 结构、规模和多模态 → 用户状态与行动 | 哪些信息该写入、更新、推断或遗忘？记忆有没有真正改变后续行为？ | [Agent Memory Radar](https://github.com/H20Zhang/Agent-Memory-Radar) |
| **RAG / Agentic Retrieval** | 检索质量 → 鲁棒性与忠实度 → 深度研究 → 有状态的跨来源执行 | 智能体能否在来源、工具和预算不断变化时控制整个信息环境？ | [Agentic RAG Radar](https://github.com/H20Zhang/Agentic-RAG-Radar) |
| **Data Agents** | 自然语言转 SQL/代码 → 实验与工作流 → 异构分析 → 真实计算机中的端到端数据工作 | 智能体能否找到、转换、分析并核验数据，最后交付可用结果？ | [Data Agent Radar](https://github.com/H20Zhang/Data-Agent-Radar) |

<a id="area-timelines"></a>
## 按领域查看全部 Benchmark

以下是 registry 中的全部 48 个基准，按发布时间从早到晚排列。

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
| 🔭 前沿 | [AMA-Bench](https://arxiv.org/abs/2602.22769) <!-- benchmark-id:ama-bench --> | 2026-02 | 真实和可扩展合成的智能体—环境轨迹上的长程记忆。 | 记忆来源从对话扩展到带有因果结构的环境经历。 |
| 🔭 前沿 | [StructMemEval](https://arxiv.org/abs/2602.11243) <!-- benchmark-id:structmemeval --> | 2026-02 | 智能体能否维护账本、列表、树等符合任务需要的记忆结构。 | 记忆的组织方式本身成为可观察能力。 |
| 🔭 前沿 | [MemoryArena](https://arxiv.org/abs/2602.16313) <!-- benchmark-id:memoryarena --> | 2026-02-18 | 在跨会话的智能体—环境循环中，用早期行动与反馈指导后续行动。 | 长期记忆与未来任务行动被放到同一项评测中。 |
| 🔭 前沿 | [LifeBench](https://arxiv.org/abs/2603.03781) <!-- benchmark-id:lifebench --> | 2026-03 | 多源长期轨迹中的事件、语义、习惯和程序性记忆。 | 评测不再局限于显式事实，也覆盖习惯和做事方法。 |
| 🔭 前沿 | [LongMemEval-V2](https://arxiv.org/abs/2605.12493) <!-- benchmark-id:longmemeval-v2 --> | 2026-05 | 大量网页智能体轨迹中的环境状态、操作流程和易错点。 | 智能体积累的环境经验成为记忆对象，而不只是用户历史。 |
| 🔭 前沿 | [MemEye](https://arxiv.org/abs/2605.15128) <!-- benchmark-id:memeye --> | 2026-05-14 | 细粒度视觉证据、视觉状态变化，以及纯文本捷径检查。 | 系统必须保留真正必要的视觉信息，不能只依赖图片描述。 |
| 🔭 前沿 | [LifeSide](https://arxiv.org/abs/2606.04660) <!-- benchmark-id:lifeside --> | 2026-06 | 跨会话记忆、用户理解、隐私控制，以及情绪与环境的互动。 | 记忆开始与持续用户建模、隐私边界和环境情境一起考察。 |
| 🔭 前沿 | [LoCoMo-Plus](https://aclanthology.org/2026.acl-long.1150/) <!-- benchmark-id:locomo-plus --> | 2026-07 | 后续问题没有复述旧约束时，能否继续正确应用它。 | 目标从显式事实召回转向用户目标、价值和约束的一致应用。 |
| 🔭 前沿 | [Mem-Gallery](https://aclanthology.org/2026.acl-long.1892/) <!-- benchmark-id:mem-gallery --> | 2026-07 | 多模态长期对话中的记忆抽取、适应、推理和知识管理。 | 视觉保留、多模态推理和记忆组织被放进同一套评测。 |
| 🔭 前沿 | [Mem2ActBench](https://aclanthology.org/2026.acl-long.370/) <!-- benchmark-id:mem2actbench --> | 2026-07 | 长期记忆是否会影响工具选择和参数填写。 | 记忆对行动的作用可以直接评分，而不再只通过问答间接判断。 |
<!-- COMPLETE-MAP:agent-memory:END -->

最近的工作已经把写入、更新、遗忘、组织、多模态信息保真、用户状态和行动分开考察。仍然缺少的，是在权限和预算可比的真实长期环境中，观察数周或数月的状态变化以及不可逆行动带来的后果。

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
| ↗ 过渡 | [DeepResearch Bench](https://arxiv.org/abs/2506.11763) <!-- benchmark-id:deepresearch-bench --> | 2025-06 | 多步网页研究、证据收集、引用质量和长篇报告生成。 | 目标不再只是找到短答案，还要交付完整研究报告。 |
| ↗ 过渡 | [BrowseComp-Plus](https://arxiv.org/abs/2508.06600) <!-- benchmark-id:browsecomp-plus --> | 2025-08 | 在固定语料上进行深度研究，并分析检索贡献和答案准确率。 | 固定且经过核验的语料降低了实时搜索带来的黑箱性和复现困难。 |
| 🔭 前沿 | [RAGCap-Bench](https://arxiv.org/abs/2510.13910) <!-- benchmark-id:ragcap-bench --> | 2025-10 | 分别评测 Agentic RAG 中的规划、检索和中间推理能力。 | 中间能力可以独立诊断，不必只从最终答案倒推原因。 |
| 🔭 前沿 | [AgenticRAGTracer](https://arxiv.org/abs/2602.19127) <!-- benchmark-id:agenticragtracer --> | 2026-02 | 对多步检索与推理逐跳核验，并检查步骤分配。 | 能够定位整条轨迹究竟在哪一步失败。 |
| 🔭 前沿 | [SGR-Bench](https://arxiv.org/abs/2605.22219) <!-- benchmark-id:sgr-bench --> | 2026-05 | 在证据受站点筛选、层级、范围或视图状态控制时完成搜索。 | 找到正确来源和把来源配置到正确状态，被拆成两个问题。 |
| 🔭 前沿 | [VAKRA](https://arxiv.org/abs/2608.12282) <!-- benchmark-id:vakra --> | 2026-08 | 组合调用 API、检索文档、完成多跳推理，并遵守工具策略。 | 跨来源依据、实际执行和策略一致性出现在同一条轨迹中。 |
<!-- COMPLETE-MAP:rag:END -->

检索评测已经从文档排序扩展到对整个信息环境的控制：来源状态、工具调用、停止时机和跨来源执行都开始计入结果。最大的困难仍是公平归因——只有接口、运行框架、模型和预算可比时，才能判断提升究竟来自哪里；实时环境持续变化又让这件事更难。

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
| 🔭 前沿 | [FDABench](https://arxiv.org/abs/2509.02473) <!-- benchmark-id:fdabench --> | 2025-09 | 在结构化数据、非结构化材料、网页和多模态来源上完成多源分析。 | 异构分析、推理过程、延迟和 token 成本可以同时观察。 |
| 🔭 前沿 | [DAComp](https://arxiv.org/abs/2512.04324) <!-- benchmark-id:dacomp --> | 2025-12 | 代码仓库级数据工程和开放式数据分析。 | 数据工程与分析被放进更完整的数据智能生命周期。 |
| 🔭 前沿 | [Data Agent Benchmark (DAB)](https://arxiv.org/abs/2603.20576) <!-- benchmark-id:data-agent-benchmark --> | 2026-03 | 跨多个 DBMS 完成数据集成、转换、分析和可执行核验。 | 企业数据问题从单条 SQL 扩展到跨数据库流程。 |
| 🔭 前沿 | [AgenticDataBench](https://arxiv.org/abs/2607.01647) <!-- benchmark-id:agenticdatabench --> | 2026-07 | 用细粒度技能分类检查真实数据科学工作流的覆盖情况。 | 除了总成功率，还能审计这套基准覆盖了哪些技能。 |
| 🔭 前沿 | [DataSpace](https://arxiv.org/abs/2608.03451) <!-- benchmark-id:dataspace --> | 2026-08 | 在混合数据库、文件、文档和多媒体的工作区中完成可验证分析。 | 寻找异构证据和核验完整结果成为一项统一任务。 |
| 🔭 前沿 | [DSAgentBench](https://arxiv.org/abs/2608.10366) <!-- benchmark-id:dsagentbench --> | 2026-08 | 使用笔记本、IDE、终端、浏览器和数据库完成完整数据科学工作流。 | 评测进入真实计算机环境，要求多阶段、多工具执行能够可靠衔接。 |
<!-- COMPLETE-MAP:data-agent:END -->

数据智能体的评测正从 SQL 或代码生成走向完整数据工作：寻找异构证据、组织工具、核验过程并交付结果。现有基准仍很少覆盖真实企业语义、含糊的业务口径、长期运行状态、治理要求，以及何时应该追问或拒答。

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
| **记忆评测如何从回忆走向行动？** | Multi-Session Chat → LoCoMo → LongMemEval → MemoryArena / Mem2ActBench / LoCoMo-Plus | [Agent Memory Radar](https://github.com/H20Zhang/Agent-Memory-Radar) |
| **检索评测如何变成对信息环境的控制？** | HotpotQA / BEIR → BrowseComp → SGR-Bench → VAKRA | [Agentic RAG Radar](https://github.com/H20Zhang/Agentic-RAG-Radar) |
| **数据智能体评测如何从 SQL/代码走到真实工作区？** | WikiSQL / Spider / DS-1000 → AgenticDataBench → DataSpace → DSAgentBench | [Data Agent Radar](https://github.com/H20Zhang/Data-Agent-Radar) |

<a id="library"></a>
## Benchmark Library

- **[按时间、领域、演化关系和评测维度浏览](library/README.md)**
- [结构化 registry](data/benchmarks.json)
- [阶段性研究总结](digests/README.md)

## 这个仓库与专题 Radar

这里整理“测什么、为什么这样测”；具体方法和系统放在三个专题 Radar 中，避免重复维护同一份综述。

[English](README.en.md) · [Curation](CURATION.md) · [Schema](SCHEMA.md)
