# Benchmark Library

**中文** | [English](README.en.md) · [返回入口](../README.md)

先按时间看领域最近把什么变成了可测对象，再按领域追完整演化。两个视图都覆盖当前 registry 的全部 benchmark。

## 按时间浏览（全部）

<!-- COMPLETE-TIMELINE:START -->
| 时间 | Benchmark | 领域 | 角色 | 这次改变了什么 |
|---:|---|---|---|---|
| 2026-08 | [DataSpace](https://arxiv.org/abs/2608.03451) <!-- benchmark-id:dataspace --> | Data Agents | 🔭 前沿 | 结合 FDABench 与 DAB，把 heterogeneous evidence discovery 与 deterministic complete-result checking 统一起来。 |
| 2026-08 | [DSAgentBench](https://arxiv.org/abs/2608.10366) <!-- benchmark-id:dsagentbench --> | Data Agents | 🔭 前沿 | 结合 MLAgentBench 与 DAComp，把评价放进真实 computer environment，并要求 grounded multi-stage tool execution。 |
| 2026-08 | [VAKRA](https://arxiv.org/abs/2608.12282) <!-- benchmark-id:vakra --> | RAG / Agentic Retrieval | 🔭 前沿 | 结合 SGR-Bench 与 AgenticRAGTracer，把跨 source grounding、执行和 policy consistency 放进同一 trajectory。 |
| 2026-07 | [AgenticDataBench](https://arxiv.org/abs/2607.01647) <!-- benchmark-id:agenticdatabench --> | Data Agents | 🔭 前沿 | 相比 DataSciBench，使 benchmark 的 skill coverage 本身可以审计。 |
| 2026-07 | [LoCoMo-Plus](https://aclanthology.org/2026.acl-long.1150/) <!-- benchmark-id:locomo-plus --> | Agent Memory | 🔭 前沿 | 相比 LoCoMo，把目标从显式事实 recall 推进到对用户目标、价值和约束的一致应用。 |
| 2026-07 | [Mem-Gallery](https://aclanthology.org/2026.acl-long.1892/) <!-- benchmark-id:mem-gallery --> | Agent Memory | 🔭 前沿 | 结合 LoCoMo 与 MemEye，使视觉保留、多模态推理和 memory organization 成为统一评价对象。 |
| 2026-07 | [Mem2ActBench](https://aclanthology.org/2026.acl-long.370/) <!-- benchmark-id:mem2actbench --> | Agent Memory | 🔭 前沿 | 相比 MemoryAgentBench 与 MemoryArena，使 action-level memory utilization 可以直接评分。 |
| 2026-06 | [LifeSide](https://arxiv.org/abs/2606.04660) <!-- benchmark-id:lifeside --> | Agent Memory | 🔭 前沿 | 相比 LoCoMo 与 LifeBench，把 memory 与 persistent user model、privacy boundary 和环境情境联结起来。 |
| 2026-05-14 | [MemEye](https://arxiv.org/abs/2605.15128) <!-- benchmark-id:memeye --> | Agent Memory | 🔭 前沿 | 相比 LoCoMo，要求系统保留真正必要的视觉证据，而不能只依赖 caption 或文本线索。 |
| 2026-05 | [LongMemEval-V2](https://arxiv.org/abs/2605.12493) <!-- benchmark-id:longmemeval-v2 --> | Agent Memory | 🔭 前沿 | 结合 LongMemEval 与 AMA-Bench，把累积环境经验而非仅用户历史设为 memory target。 |
| 2026-05 | [SGR-Bench](https://arxiv.org/abs/2605.22219) <!-- benchmark-id:sgr-bench --> | RAG / Agentic Retrieval | 🔭 前沿 | 相比 BrowseComp 与 CRAG，区分找到正确 source 与配置正确 retrieval state。 |
| 2026-03 | [Data Agent Benchmark (DAB)](https://arxiv.org/abs/2603.20576) <!-- benchmark-id:data-agent-benchmark --> | Data Agents | 🔭 前沿 | 相比 Spider 2.0，把企业数据问题从单一 SQL workflow 扩展到跨数据库完整 pipeline。 |
| 2026-03 | [LifeBench](https://arxiv.org/abs/2603.03781) <!-- benchmark-id:lifebench --> | Agent Memory | 🔭 前沿 | 相比 LoCoMo 和 LongMemEval，把评价对象从显式事实扩展到习惯与程序性知识。 |
| 2026-02-18 | [MemoryArena](https://arxiv.org/abs/2602.16313) <!-- benchmark-id:memoryarena --> | Agent Memory | 🔭 前沿 | 相比 MemoryAgentBench，直接把长期记忆与未来 task action 耦合起来。 |
| 2026-02 | [AgenticRAGTracer](https://arxiv.org/abs/2602.19127) <!-- benchmark-id:agenticragtracer --> | RAG / Agentic Retrieval | 🔭 前沿 | 相比 MultiHop-RAG 与 RAGCap-Bench，使 failure location 在 trajectory 内可见。 |
| 2026-02 | [AMA-Bench](https://arxiv.org/abs/2602.22769) <!-- benchmark-id:ama-bench --> | Agent Memory | 🔭 前沿 | 相比 MemoryAgentBench，把记忆来源从对话交互扩展到具有因果结构的 agent-environment experience。 |
| 2026-02 | [StructMemEval](https://arxiv.org/abs/2602.11243) <!-- benchmark-id:structmemeval --> | Agent Memory | 🔭 前沿 | 相比 MemoryAgentBench，使 memory 的组织方式本身成为可观察能力。 |
| 2026-01 | [RealMem](https://aclanthology.org/2026.findings-acl.703/) <!-- benchmark-id:realmem --> | Agent Memory | 🔭 前沿 | 相比 LoCoMo，把评价对象从一般对话历史推进到 persistent project state 与 evolving goals。 |
| 2025-12 | [DAComp](https://arxiv.org/abs/2512.04324) <!-- benchmark-id:dacomp --> | Data Agents | 🔭 前沿 | 结合 Spider 2.0 与 InsightBench，覆盖 data engineering 和 analysis 的更完整 lifecycle。 |
| 2025-10 | [BEAM](https://arxiv.org/abs/2510.27246) <!-- benchmark-id:beam --> | Agent Memory | ↗ 过渡 | 相比 LoCoMo，直接暴露超大规模连贯历史下的 memory degradation。 |
| 2025-10 | [RAGCap-Bench](https://arxiv.org/abs/2510.13910) <!-- benchmark-id:ragcap-bench --> | RAG / Agentic Retrieval | 🔭 前沿 | 相比 MultiHop-RAG 与 BrowseComp-Plus，使中间能力可独立诊断，而不只看最终答案。 |
| 2025-09 | [FDABench](https://arxiv.org/abs/2509.02473) <!-- benchmark-id:fdabench --> | Data Agents | 🔭 前沿 | 相比 DataSciBench 与 InsightBench，把异构分析、reasoning trace、latency 和 token cost 一起暴露。 |
| 2025-08 | [BrowseComp-Plus](https://arxiv.org/abs/2508.06600) <!-- benchmark-id:browsecomp-plus --> | RAG / Agentic Retrieval | ↗ 过渡 | 相比 BrowseComp，用固定 verified corpus 降低 live-search 黑盒带来的公平性和复现问题。 |
| 2025-07 | [MemoryAgentBench](https://arxiv.org/abs/2507.05257) <!-- benchmark-id:memoryagentbench --> | Agent Memory | ↗ 过渡 | 相比 LongMemEval 与 MemBench，把 memory 从静态历史读出改为持续吸收、更新、使用和遗忘的在线过程。 |
| 2025-06 | [DeepResearch Bench](https://arxiv.org/abs/2506.11763) <!-- benchmark-id:deepresearch-bench --> | RAG / Agentic Retrieval | ↗ 过渡 | 相比 BrowseComp，把目标从找到短答案提升到生成 analyst-style research artifact。 |
| 2025-06 | [MemBench](https://arxiv.org/abs/2506.21605) <!-- benchmark-id:membench --> | Agent Memory | ↗ 过渡 | 相比 LoCoMo 与 LongMemEval，从答题准确率扩展到记忆层次、交互角色和资源表现。 |
| 2025-04 | [BrowseComp](https://arxiv.org/abs/2504.12516) <!-- benchmark-id:browsecomp --> | RAG / Agentic Retrieval | ↗ 过渡 | 相比 BEIR 与 CRAG，把评价对象从一次 retrieval 推进到 persistent information seeking。 |
| 2025-02 | [DataSciBench](https://arxiv.org/abs/2502.13897) <!-- benchmark-id:datascibench --> | Data Agents | ↗ 过渡 | 相比 DA-Code 与 MLAgentBench，扩大任务覆盖并为不同分析目标使用专门 evaluator。 |
| 2024-11 | [Spider 2.0](https://arxiv.org/abs/2411.07763) <!-- benchmark-id:spider-2 --> | Data Agents | ↗ 过渡 | 相比 Spider 与 BIRD，把 one-shot semantic parsing 变成长程 enterprise workflow。 |
| 2024-10 | [DA-Code](https://aclanthology.org/2024.emnlp-main.748/) <!-- benchmark-id:da-code --> | Data Agents | ↗ 过渡 | 相比 DS-1000 与 MLAgentBench，在静态代码题和 agent-style data work 之间建立可执行桥梁。 |
| 2024-10 | [LongMemEval](https://arxiv.org/abs/2410.10813) <!-- benchmark-id:longmemeval --> | Agent Memory | 🧱 基石 | 相比 LoCoMo，将更新、时间推理和拒答从一般 recall 中明确拆分出来。 |
| 2024-08 | [LoCoMo](https://aclanthology.org/2024.acl-long.747/) <!-- benchmark-id:locomo --> | Agent Memory | 🧱 基石 | 相比 Beyond Goldfish Memory，把超长对话记忆固化为可复用的多任务评价坐标。 |
| 2024-07 | [BRIGHT](https://arxiv.org/abs/2407.12883) <!-- benchmark-id:bright --> | RAG / Agentic Retrieval | ↗ 过渡 | 相比 BEIR，暴露 semantic similarity 无法覆盖的 reasoning-intensive retrieval。 |
| 2024-07 | [InsightBench](https://arxiv.org/abs/2407.06423) <!-- benchmark-id:insightbench --> | Data Agents | ↗ 过渡 | 相比 DS-1000 与 MLAgentBench，把目标从完成给定代码任务扩展到发现并沟通有用分析。 |
| 2024-07 | [RAGBench](https://arxiv.org/abs/2407.11005) <!-- benchmark-id:ragbench --> | RAG / Agentic Retrieval | ↗ 过渡 | 相比 RGB 与 RAGTruth，把 evaluator 质量和可行动 failure label 本身变成 benchmark 问题。 |
| 2024-06 | [CRAG](https://arxiv.org/abs/2406.04744) <!-- benchmark-id:crag --> | RAG / Agentic Retrieval | ↗ 过渡 | 相比 KILT 与 RGB，把 freshness、事实动态性和长尾知识带入 RAG 评价。 |
| 2024-01 | [MultiHop-RAG](https://arxiv.org/abs/2401.15391) <!-- benchmark-id:multihop-rag --> | RAG / Agentic Retrieval | ↗ 过渡 | 结合 HotpotQA 与 RGB，使 multi-hop retrieval failure 在 RAG pipeline 内部可见。 |
| 2024-01 | [RAGTruth](https://arxiv.org/abs/2401.00396) <!-- benchmark-id:ragtruth --> | RAG / Agentic Retrieval | ↗ 过渡 | 相比 RGB，把 faithfulness failure 从整体答案标签细化到局部文本跨度。 |
| 2023-10 | [MLAgentBench](https://arxiv.org/abs/2310.03302) <!-- benchmark-id:mlagentbench --> | Data Agents | ↗ 过渡 | 相比 DS-1000，把一次代码生成改成由执行反馈驱动的科学实验过程。 |
| 2023-09 | [RGB](https://arxiv.org/abs/2309.01431) <!-- benchmark-id:rgb --> | RAG / Agentic Retrieval | 🧱 基石 | 相比 KILT，把“是否正确使用 retrieved context”拆成多个独立能力。 |
| 2023-05 | [BIRD](https://arxiv.org/abs/2305.03111) <!-- benchmark-id:bird --> | Data Agents | ↗ 过渡 | 相比 Spider，把 text-to-SQL 推进到 value-rich、messy database，并使 SQL efficiency 可见。 |
| 2022-11 | [DS-1000](https://arxiv.org/abs/2211.11501) <!-- benchmark-id:ds-1000 --> | Data Agents | 🧱 基石 | 在 SQL lineage 之外，建立了可复现的实用 data-science code 执行评价。 |
| 2022-05 | [Beyond Goldfish Memory](https://aclanthology.org/2022.acl-long.356/) <!-- benchmark-id:beyond-goldfish-memory --> | Agent Memory | 🌱 前身 | 将跨 session 对话连续性确立为现代 memory-agent benchmark 之前的独立评价对象。 |
| 2021-04 | [BEIR](https://arxiv.org/abs/2104.08663) <!-- benchmark-id:beir --> | RAG / Agentic Retrieval | 🧱 基石 | 不再以单一 IR dataset 的最优结果代表 retriever robustness，而是直接测跨域泛化。 |
| 2020-09 | [KILT](https://arxiv.org/abs/2009.02252) <!-- benchmark-id:kilt --> | RAG / Agentic Retrieval | 🧱 基石 | 相比 HotpotQA，把正确性与证据来源放进共享、可复用的评价基础设施。 |
| 2018-10 | [HotpotQA](https://aclanthology.org/D18-1259/) <!-- benchmark-id:hotpotqa --> | RAG / Agentic Retrieval | 🌱 前身 | 将多文档证据组合和可解释 supporting facts 确立为可测的 retrieval-reasoning 目标。 |
| 2018-10 | [Spider](https://aclanthology.org/D18-1425/) <!-- benchmark-id:spider --> | Data Agents | 🧱 基石 | 相比 WikiSQL，把 text-to-SQL 从单表生成推进到复杂查询和 cross-schema generalization。 |
| 2017-08 | [WikiSQL](https://arxiv.org/abs/1709.00103) <!-- benchmark-id:wikisql --> | Data Agents | 🌱 前身 | 将大规模、可执行的自然语言数据库访问确立为 benchmarkable task。 |
<!-- COMPLETE-TIMELINE:END -->

## 按领域浏览（全部）

### Agent Memory

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

[进入 Agent Memory Radar](https://github.com/H20Zhang/Agent-Memory-Radar)

### RAG / Agentic Retrieval

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

[进入 Agentic RAG Radar](https://github.com/H20Zhang/Agentic-RAG-Radar)

### Data Agents

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
