# Agent Benchmark Radar

[中文](README.md) | **English**

<a id="frontier-signals"></a>
## Last 30 Days: Three Shifts

<!-- FRONTIER-SIGNALS:START -->
| Area | What actually changed | Representative benchmarks |
|---|---|---|
| **Agent Memory** | Evaluation is moving beyond “can it recall?” toward **whether retained memory causally changes later action and whether persistent state can be governed safely**. PAST-Bench uses persistence-on/off controls to measure downstream memory effects; SP-Mem puts personalization, consent, and leakage in one protocol; InMind separates storage, knowledge, routing, and use failures. | [PAST-Bench](https://arxiv.org/abs/2608.04003) · [SP-Mem](https://arxiv.org/abs/2608.16551) · [InMind](https://arxiv.org/abs/2607.24368) |
| **RAG / Agentic Retrieval** | The question is shifting from “is recall high?” to **whether a retrieval metric predicts downstream success, whether the search process is auditable, and whether results transfer across deployment conditions**. The Recall Trap gives a direct recall-vs-repair counterexample; SearchAuditBench measures failure localization and repair; The Commercial Tax brings license, query format, index construction, and cost into transferability. | [The Recall Trap](https://arxiv.org/abs/2608.14838) · [SearchAuditBench](https://arxiv.org/abs/2608.05212) · [The Commercial Tax](https://arxiv.org/abs/2608.16096) |
| **Data Agents** | The target keeps moving beyond “does SQL/code run?” toward **understanding data first, completing verifiable work, and clarifying or abstaining when business semantics are underspecified**. Data Exploration Benchmark scores exploration directly; WarehouseReliabilityBench tests business truth, clarification, and abstention; data-eng-bench's evaluator fix shows that evaluator reliability itself can be the bottleneck. | [Data Exploration Benchmark](https://arxiv.org/abs/2608.16045) · [WarehouseReliabilityBench](https://arxiv.org/abs/2608.09254) · [data-eng-bench](https://github.com/Snowflake-Labs/data-eng-bench) |
<!-- FRONTIER-SIGNALS:END -->

Last updated: **2026-08-21**

<a id="release-timeline"></a>
## Benchmark Timeline: Last Six Months

<!-- TABLE-FIRST:RECENT:START -->
| Time | Area | Benchmark | What it tests |
|---|---|---|---|
| 2026-08-18 | RAG | [VisDocAgentBench](https://arxiv.org/abs/2608.17889) <!-- benchmark-id:visdocagentbench --> | Visual-document retrieval benchmark that compares static rankers and iterative visual/OCR agents under one ranked-page contract. |
| 2026-08-17 | Data Agent | [Data Exploration Benchmark](https://arxiv.org/abs/2608.16045) <!-- benchmark-id:data-exploration-benchmark --> | Structured dataset understanding before analysis, including logical tables, semantics, keys, relationships, and profiling signals. |
| 2026-08-17 | Agent Memory | [SP-Mem Privacy-Aware Memory Benchmark](https://arxiv.org/abs/2608.16551) <!-- benchmark-id:sp-mem --> | Privacy-aware memory benchmark that jointly measures response quality, personalization, consent handling, exact-value exposure, and cost. |
| 2026-08-17 | RAG | [The Commercial Tax](https://arxiv.org/abs/2608.16096) <!-- benchmark-id:commercial-tax --> | Retrieval reproducibility audit that binds raw embedder scores to licensing, query formatting, index construction, and deployment cost. |
| 2026-08-10 | RAG | [The Recall Trap](https://arxiv.org/abs/2608.14838) <!-- benchmark-id:recall-trap --> | Validity audit showing that higher file recall can reduce downstream repair success under a fixed-slot code-retrieval protocol. |
| 2026-08-10 | Data Agent | [WarehouseReliabilityBench](https://arxiv.org/abs/2608.09254) <!-- benchmark-id:warehouse-reliability-bench --> | Business-correct analytics plus appropriate clarification, abstention, or refusal under ambiguity, unanswerability, drift, and attacks. |
| 2026-08-07 | RAG | [DAS-Bench / DAS-Eval](https://arxiv.org/abs/2608.18034) <!-- benchmark-id:das-bench --> | Academic-survey benchmark and evaluator that score literature coverage, taxonomy, claims, citations, discourse, and rendered artifact quality. |
| 2026-08-05 | RAG | [SearchAuditBench](https://arxiv.org/abs/2608.05212) <!-- benchmark-id:searchauditbench --> | Localization, root-cause attribution, and repair of failures in long deep-search trajectories. |
| 2026-08-04 | RAG | [MAPLE](https://arxiv.org/abs/2608.15624) <!-- benchmark-id:maple --> | Scientific retrieval benchmark that measures whether one paper remains retrievable across motivation, method, and result aspects. |
| 2026-08-04 | Agent Memory | [PAST-Bench](https://arxiv.org/abs/2608.04003) <!-- benchmark-id:past-bench --> | Paired persistent-state benchmark that tests whether retained cross-episode experience causally improves later executable work. |
| 2026-08 | Data Agent | [DataSpace](https://arxiv.org/abs/2608.03451) <!-- benchmark-id:dataspace --> | Evaluates verifiable analytics over heterogeneous workspaces where evidence spans databases, files, documents, and multimedia. |
| 2026-08 | Data Agent | [DSAgentBench](https://arxiv.org/abs/2608.10366) <!-- benchmark-id:dsagentbench --> | Evaluates agents on complete data-science workflows inside real computer environments using notebooks, IDEs, terminals, browsers, and databases. |
| 2026-08 | RAG | [VAKRA](https://arxiv.org/abs/2608.12282) <!-- benchmark-id:vakra --> | Evaluates agents that must compose executable APIs, document retrieval, multi-hop reasoning, and natural-language tool-use policies. |
| 2026-07-29 | Data Agent | [data-eng-bench](https://github.com/Snowflake-Labs/data-eng-bench) <!-- benchmark-id:data-eng-bench --> | Executable data-engineering benchmark for repository-scale dbt transformations with hidden row-level verification on DuckDB and Snowflake. |
| 2026-07-27 | Agent Memory | [InMind](https://arxiv.org/abs/2607.24368) <!-- benchmark-id:inmind --> | Retrieval and use of a personal fact whose relevance to the query depends on world knowledge. |
| 2026-07-21 | Agent Memory | [MemFuseBench](https://arxiv.org/abs/2608.18704) <!-- benchmark-id:memfusebench --> | Cross-source memory benchmark for linking, causal fusion, conflict arbitration, and provenance over heterogeneous event streams. |
| 2026-07-14 | RAG | [WANDR](https://arxiv.org/abs/2608.14747) <!-- benchmark-id:wandr --> | Live-web benchmark for wide-and-deep record collection with hierarchical tasks and reference-free record verification. |
| 2026-07-09 | Data Agent | [CausalDS](https://arxiv.org/abs/2607.08093) <!-- benchmark-id:causalds --> | Executable causal data science across prediction, identification, effects, counterfactuals, uncertainty, and abstention. |
| 2026-07 | Data Agent | [AgenticDataBench](https://arxiv.org/abs/2607.01647) <!-- benchmark-id:agenticdatabench --> | Benchmarks data agents across realistic data-science workflows using a skill taxonomy to quantify fine-grained coverage. |
| 2026-07 | Agent Memory | [LoCoMo-Plus](https://aclanthology.org/2026.acl-long.1150/) <!-- benchmark-id:locomo-plus --> | Evaluates cognitive memory where agents must retain and apply latent user constraints even when later cues are semantically disconnected. |
| 2026-07 | Agent Memory | [Mem-Gallery](https://aclanthology.org/2026.acl-long.1892/) <!-- benchmark-id:mem-gallery --> | Evaluates multimodal long-term conversational memory across extraction and test-time adaptation, reasoning, and memory knowledge management. |
| 2026-07 | Agent Memory | [Mem2ActBench](https://aclanthology.org/2026.acl-long.370/) <!-- benchmark-id:mem2actbench --> | Evaluates whether long-term memory is proactively used for tool selection and parameter grounding during tool-based assistant actions. |
| 2026-07 | Agent Memory | [PerMemSafe](https://aclanthology.org/2026.findings-acl.320/) <!-- benchmark-id:permemsafe --> | Recognition and updating of implicit personalized risk across long, noise-heavy histories. |
| 2026-06-23 | Agent Memory | [MEMPROBE](https://arxiv.org/abs/2606.24595) <!-- benchmark-id:memprobe --> | Recovery of hidden user state from the memory artifact left after ordinary assistance. |
| 2026-06-22 | Agent Memory | [DynamicMem](https://arxiv.org/abs/2606.22877) <!-- benchmark-id:dynamicmem --> | Inference and updating of user attributes, habits, and preferences from fifteen months of multi-app behavior. |
| 2026-06-22 | Data Agent | [StatABench](https://arxiv.org/abs/2606.22977) <!-- benchmark-id:statabench --> | Statistical knowledge, tool selection and parameterization, plus open end-to-end modeling and reporting. |
| 2026-06-17 | Agent Memory | [GateMem](https://arxiv.org/abs/2606.18829) <!-- benchmark-id:gatemem --> | Utility, access control, and active forgetting in multi-principal shared memory. |
| 2026-06-13 | Data Agent | [IRTS-ToolBench](https://arxiv.org/abs/2606.15107) <!-- benchmark-id:irts-toolbench --> | Tool-grounded QA over asynchronous, missing, variably sampled irregular time series. |
| 2026-06-11 | RAG | [EvoBrowseComp](https://arxiv.org/abs/2606.13120) <!-- benchmark-id:evobrowsecomp --> | Broad English and Chinese web search over evolving knowledge. |
| 2026-06-11 | RAG | [LoHoSearch](https://arxiv.org/abs/2606.12837) <!-- benchmark-id:lohosearch --> | Long-horizon search under large candidate spaces, complex constraints, and context-management pressure. |
| 2026-06 | Agent Memory | [LifeSide](https://arxiv.org/abs/2606.04660) <!-- benchmark-id:lifeside --> | Benchmarks lifelong digital companions through multi-session memory, user understanding, privacy control, and emotional-environment dynamics. |
| 2026-05-28 | Agent Memory | [WorldMemArena](https://arxiv.org/abs/2605.29341) <!-- benchmark-id:worldmemarena --> | Writing, maintaining, retrieving, and using multimodal memory from actions, observations, and feedback. |
| 2026-05-27 | RAG | [LiveBrowseComp](https://arxiv.org/abs/2605.28721) <!-- benchmark-id:livebrowsecomp --> | Retrieval of recent low-salience web facts rather than verification of parametric knowledge. |
| 2026-05-19 | RAG | [ScholarQuest](https://arxiv.org/abs/2606.20235) <!-- benchmark-id:scholarquest --> | Intent-conditioned iterative paper retrieval, citation expansion, scope control, and set coverage. |
| 2026-05-18 | Agent Memory | [EvoMemBench](https://arxiv.org/abs/2605.18421) <!-- benchmark-id:evomembench --> | Memory comparison across in-episode versus cross-episode scope and knowledge versus execution content. |
| 2026-05-14 | Agent Memory | [GroupMemBench](https://arxiv.org/abs/2605.14498) <!-- benchmark-id:groupmembench --> | Speaker-grounded beliefs, group dynamics, terminology, and audience adaptation in multi-party conversations. |
| 2026-05-14 | Agent Memory | [MemEye](https://arxiv.org/abs/2605.15128) <!-- benchmark-id:memeye --> | Benchmarks visual-centric agent memory across fine-grained visual evidence and temporal visual-state synthesis while checking whether visual evidence is genuinely necessary. |
| 2026-05-14 | Agent Memory | [MEMLENS](https://arxiv.org/abs/2605.14906) <!-- benchmark-id:memlens --> | Multimodal extraction, updating, temporal reasoning, and abstention from 32K to 256K contexts. |
| 2026-05-12 | Agent Memory | [MedMemoryBench](https://arxiv.org/abs/2605.11814) <!-- benchmark-id:medmemorybench --> | Clinical-state tracking, temporal change, and memory saturation during streaming medical histories. |
| 2026-05-04 | Data Agent | [DataClawBench](https://arxiv.org/abs/2605.02503) <!-- benchmark-id:dataclawbench --> | Low-prior exploratory analysis over unfamiliar, noisy, cross-domain financial data with verifiable conclusions. |
| 2026-05 | Agent Memory | [LongMemEval-V2](https://arxiv.org/abs/2605.12493) <!-- benchmark-id:longmemeval-v2 --> | Evaluates whether memory systems internalize environment-specific experience from large web-agent trajectory histories. |
| 2026-05 | RAG | [SGR-Bench](https://arxiv.org/abs/2605.22219) <!-- benchmark-id:sgr-bench --> | Benchmarks search agents when answer-bearing evidence appears only after the agent establishes the correct site-specific retrieval state. |
| 2026-04-30 | RAG | [Bright-Pro](https://aclanthology.org/2026.acl-long.1705/) <!-- benchmark-id:bright-pro --> | Reasoning-intensive retrieval, aspect coverage, and retriever utility in static and agentic search. |
| 2026-04-19 | RAG | [MuDABench](https://aclanthology.org/2026.findings-acl.341/) <!-- benchmark-id:mudabench --> | Information extraction, cross-document aggregation, and quantitative analysis over large financial collections. |
| 2026-04-17 | Agent Memory | [MemEvoBench](https://arxiv.org/abs/2604.15774) <!-- benchmark-id:memevobench --> | Safety drift under repeated writes of misleading memories, noisy tool outputs, and biased feedback. |
| 2026-04-15 | RAG | [MERRIN](https://arxiv.org/abs/2604.13418) <!-- benchmark-id:merrin --> | Uncued modality selection, multimodal evidence retrieval, and multi-hop reasoning on the noisy web. |
| 2026-04-14 | RAG | [EnterpriseRAG-Bench](https://arxiv.org/abs/2605.05253) <!-- benchmark-id:enterpriserag-bench --> | Enterprise retrieval, multi-document reasoning, conflict handling, completeness, and not-found behavior. |
| 2026-04-09 | Agent Memory | [ImplicitMemBench](https://aclanthology.org/2026.acl-long.1301/) <!-- benchmark-id:implicitmembench --> | First-attempt procedural learning, priming, and conditioning after an interference phase. |
| 2026-04-07 | RAG | [LeakDojo](https://aclanthology.org/2026.findings-acl.287/) <!-- benchmark-id:leakdojo --> | Extraction of RAG database content across attacks, models, pipelines, budgets, and defenses. |
| 2026-04-01 | RAG | [AutoResearchBench](https://arxiv.org/abs/2604.25256) <!-- benchmark-id:autoresearchbench --> | Target-paper tracing, constrained literature search, open-set collection, and stopping decisions. |
| 2026-03-12 | Data Agent | [AgentFuel](https://arxiv.org/abs/2603.12483) <!-- benchmark-id:agentfuel --> | Domain-customized functional evaluation of conversational time-series agents, especially stateful and incident-specific queries. |
| 2026-03-05 | Data Agent | [TML-Bench](https://arxiv.org/abs/2603.05764) <!-- benchmark-id:tml-bench --> | Reliable end-to-end tabular-ML submissions under fixed wall-clock budgets and hidden labels. |
| 2026-03 | Data Agent | [Data Agent Benchmark (DAB)](https://arxiv.org/abs/2603.20576) <!-- benchmark-id:data-agent-benchmark --> | Evaluates enterprise data agents on questions requiring integration, transformation, and analysis across multiple heterogeneous database systems. |
| 2026-03 | Agent Memory | [LifeBench](https://arxiv.org/abs/2603.03781) <!-- benchmark-id:lifebench --> | Evaluates long-horizon multi-source memory spanning declarative and non-declarative information such as habits and procedures. |
| 2026-02-27 | Data Agent | [DARE-bench](https://arxiv.org/abs/2602.24288) <!-- benchmark-id:dare-bench --> | Verifiable ML-model quality and fidelity to prescribed data-science instructions and processes. |
| 2026-02-26 | RAG | [MTRAG-UN](https://aclanthology.org/2026.findings-acl.503/) <!-- benchmark-id:mtrag-un --> | Multi-turn RAG handling of unanswerable, underspecified, non-standalone, and unclear turns. |
| 2026-02-22 | RAG | [MC-Search](https://arxiv.org/abs/2603.00873) <!-- benchmark-id:mc-search --> | Multimodal search planning, modality choice, hop-level retrieval, and long-chain reasoning fidelity. |
| 2026-02-18 | Agent Memory | [MemoryArena](https://arxiv.org/abs/2602.16313) <!-- benchmark-id:memoryarena --> | Evaluates memory inside multi-session Memory-Agent-Environment loops where earlier actions and feedback must be distilled and used to guide later actions. |
| 2026-02-06 | RAG | [GISA](https://arxiv.org/abs/2602.08543) <!-- benchmark-id:gisa --> | Search planning, deep reasoning, broad aggregation, and structured answering for authentic information needs. |
| 2026-02-05 | RAG | [SAGE](https://arxiv.org/abs/2602.05975) <!-- benchmark-id:sage --> | Targeted and open-ended scientific literature retrieval for deep-research agents. |
| 2026-02-03 | Agent Memory | [MemGUI-Bench](https://arxiv.org/abs/2602.06075) <!-- benchmark-id:memgui-bench --> | Cross-step retention, cross-app transfer, cross-session learning, and recovery in mobile GUI tasks. |
| 2026-02 | RAG | [AgenticRAGTracer](https://arxiv.org/abs/2602.19127) <!-- benchmark-id:agenticragtracer --> | Diagnoses multi-step agentic RAG by providing hop-aware intermediate validation rather than only final questions and answers. |
| 2026-02 | Agent Memory | [AMA-Bench](https://arxiv.org/abs/2602.22769) <!-- benchmark-id:ama-bench --> | Evaluates long-horizon memory over real and synthetic agent-environment trajectories rather than dialogue-only histories. |
| 2026-02 | Agent Memory | [StructMemEval](https://arxiv.org/abs/2602.11243) <!-- benchmark-id:structmemeval --> | Tests whether agents organize memory into task-appropriate structures such as ledgers, lists, and trees rather than only retrieving facts. |<!-- TABLE-FIRST:RECENT:END -->

<a id="timeline"></a><a id="latest"></a><a id="frontier"></a>
<a id="periods"></a><a id="changes"></a><a id="evolution"></a>
<a id="field-map"></a>
## Benchmark Map

<a id="benchmark-memory"></a>
### Agent Memory
From cross-session factual recall toward online updating, structured memory, multimodal evidence, action, authority, and implicit user state.

**Defining chain:** [Beyond Goldfish Memory](https://aclanthology.org/2022.acl-long.356/) → [LoCoMo](https://aclanthology.org/2024.acl-long.747/) / [LongMemEval](https://arxiv.org/abs/2410.10813) → [MemoryAgentBench](https://arxiv.org/abs/2507.05257) → [StructMemEval](https://arxiv.org/abs/2602.11243) / [MemoryArena](https://arxiv.org/abs/2602.16313) → [MemEye](https://arxiv.org/abs/2605.15128) / [WorldMemArena](https://arxiv.org/abs/2605.29341) → [DynamicMem](https://arxiv.org/abs/2606.22877) / [LoCoMo-Plus](https://aclanthology.org/2026.acl-long.1150/) → [GateMem](https://arxiv.org/abs/2606.18829) / [Mem2ActBench](https://aclanthology.org/2026.acl-long.370/) / [PAST-Bench](https://arxiv.org/abs/2608.04003) / [SP-Mem](https://arxiv.org/abs/2608.16551)

<a id="benchmark-rag"></a>
### RAG / Agentic Retrieval
From document relevance toward multi-hop evidence composition, live search, stopping, cross-source execution, and trace auditing.

**Defining chain:** [HotpotQA](https://aclanthology.org/D18-1259/) → [BEIR](https://arxiv.org/abs/2104.08663) / [BRIGHT](https://arxiv.org/abs/2407.12883) → [BrowseComp](https://arxiv.org/abs/2504.12516) → [AutoResearchBench](https://arxiv.org/abs/2604.25256) / [Bright-Pro](https://aclanthology.org/2026.acl-long.1705/) → [LiveBrowseComp](https://arxiv.org/abs/2605.28721) / [LoHoSearch](https://arxiv.org/abs/2606.12837) → [SearchAuditBench](https://arxiv.org/abs/2608.05212) / [VAKRA](https://arxiv.org/abs/2608.12282) → [MAPLE](https://arxiv.org/abs/2608.15624) / [VisDocAgentBench](https://arxiv.org/abs/2608.17889) / [WANDR](https://arxiv.org/abs/2608.14747)

**Frontier signal:** evaluation is splitting relevance from aspect coverage, target finding from exhaustive set collection, and final correctness from stopping, calibration, failure localization, repair, security, multimodal evidence, and live-web freshness.

**Biggest gap:** causal attribution under matched interface/harness/model/budget, especially for long-horizon live environments where web state drifts.

[Open the complete RAG benchmark table →](library/README.en.md#rag--agentic-retrieval) · [Continue into Agentic RAG methods/systems →](https://github.com/H20Zhang/Agentic-RAG-Radar#field-map)

<a id="benchmark-data"></a>
### Data Agents
From text-to-SQL / code generation toward complete data workflows, exploration, statistical/causal analysis, and business-semantic reliability.

**Defining chain:** [WikiSQL](https://arxiv.org/abs/1709.00103) → [Spider](https://aclanthology.org/D18-1425/) / [DS-1000](https://arxiv.org/abs/2211.11501) → [MLAgentBench](https://arxiv.org/abs/2310.03302) / [InsightBench](https://arxiv.org/abs/2407.06423) → [Spider 2.0](https://arxiv.org/abs/2411.07763) / [KramaBench](https://arxiv.org/abs/2506.06541) → [DataClawBench](https://arxiv.org/abs/2605.02503) / [DSGym](https://arxiv.org/abs/2601.16344) → [StatABench](https://arxiv.org/abs/2606.22977) / [CausalDS](https://arxiv.org/abs/2607.08093) → [DataSpace](https://arxiv.org/abs/2608.03451) / [DSAgentBench](https://arxiv.org/abs/2608.10366) → [Data Exploration Benchmark](https://arxiv.org/abs/2608.16045) / [WarehouseReliabilityBench](https://arxiv.org/abs/2608.09254) / [data-eng-bench](https://github.com/Snowflake-Labs/data-eng-bench)

<a id="all-benchmarks"></a>
## All Benchmarks by Area

All 105 benchmarks in the registry remain directly scannable here. The Library is an alternate canonical browse surface, not a reason to remove these tables from README.

### Agent Memory

<!-- TABLE-FIRST:AREA:agent-memory:START -->
| Role | Benchmark | Released | What it evaluates |
|---|---|---:|---|
| 🌱 Precursor | [Beyond Goldfish Memory](https://aclanthology.org/2022.acl-long.356/) <!-- benchmark-id:beyond-goldfish-memory --> | 2022-05 | Benchmarks long-term open-domain conversation across multiple human-human chat sessions where partners must remember and remain consistent with prior interactions. |
| 🧱 Foundation | [LoCoMo](https://aclanthology.org/2024.acl-long.747/) <!-- benchmark-id:locomo --> | 2024-08 | Long-horizon conversational-memory benchmark spanning QA, event summarization, and multimodal dialogue generation over very long multi-session conversations. |
| 🧱 Foundation | [LongMemEval](https://arxiv.org/abs/2410.10813) <!-- benchmark-id:longmemeval --> | 2024-10 | Evaluates sustained chat-assistant memory across extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention. |
| ↗ Transition | [MemBench](https://arxiv.org/abs/2506.21605) <!-- benchmark-id:membench --> | 2025-06 | Broadens memory evaluation across factual and reflective memory, participation and observation scenarios, and effectiveness, efficiency, and capacity. |
| ↗ Transition | [MemoryAgentBench](https://arxiv.org/abs/2507.05257) <!-- benchmark-id:memoryagentbench --> | 2025-07 | Evaluates memory agents under incremental multi-turn interaction across retrieval, test-time learning, long-range understanding, and selective forgetting. |
| ↗ Transition | [BEAM](https://arxiv.org/abs/2510.27246) <!-- benchmark-id:beam --> | 2025-10 | Tests long-term memory on coherent conversations extending from million-token to multi-million-token horizons. |
| 🔭 Frontier | [RealMem](https://aclanthology.org/2026.findings-acl.703/) <!-- benchmark-id:realmem --> | 2026-01 | Evaluates long-term memory over project-oriented cross-session interactions whose goals, artifacts, and relevant state evolve over time. |
| 🔭 Frontier | [CAME-Bench](https://aclanthology.org/2026.findings-acl.584/) <!-- benchmark-id:came-bench --> | 2026-01-15 | Intent-compatible retrieval when the same entities recur under different goals. |
| 🔭 Frontier | [AMA-Bench](https://arxiv.org/abs/2602.22769) <!-- benchmark-id:ama-bench --> | 2026-02 | Evaluates long-horizon memory over real and synthetic agent-environment trajectories rather than dialogue-only histories. |
| 🔭 Frontier | [StructMemEval](https://arxiv.org/abs/2602.11243) <!-- benchmark-id:structmemeval --> | 2026-02 | Tests whether agents organize memory into task-appropriate structures such as ledgers, lists, and trees rather than only retrieving facts. |
| 🔭 Frontier | [MemGUI-Bench](https://arxiv.org/abs/2602.06075) <!-- benchmark-id:memgui-bench --> | 2026-02-03 | Cross-step retention, cross-app transfer, cross-session learning, and recovery in mobile GUI tasks. |
| 🔭 Frontier | [MemoryArena](https://arxiv.org/abs/2602.16313) <!-- benchmark-id:memoryarena --> | 2026-02-18 | Evaluates memory inside multi-session Memory-Agent-Environment loops where earlier actions and feedback must be distilled and used to guide later actions. |
| 🔭 Frontier | [LifeBench](https://arxiv.org/abs/2603.03781) <!-- benchmark-id:lifebench --> | 2026-03 | Evaluates long-horizon multi-source memory spanning declarative and non-declarative information such as habits and procedures. |
| 🔭 Frontier | [ImplicitMemBench](https://aclanthology.org/2026.acl-long.1301/) <!-- benchmark-id:implicitmembench --> | 2026-04-09 | First-attempt procedural learning, priming, and conditioning after an interference phase. |
| 🔭 Frontier | [MemEvoBench](https://arxiv.org/abs/2604.15774) <!-- benchmark-id:memevobench --> | 2026-04-17 | Safety drift under repeated writes of misleading memories, noisy tool outputs, and biased feedback. |
| 🔭 Frontier | [LongMemEval-V2](https://arxiv.org/abs/2605.12493) <!-- benchmark-id:longmemeval-v2 --> | 2026-05 | Evaluates whether memory systems internalize environment-specific experience from large web-agent trajectory histories. |
| 🔭 Frontier | [MedMemoryBench](https://arxiv.org/abs/2605.11814) <!-- benchmark-id:medmemorybench --> | 2026-05-12 | Clinical-state tracking, temporal change, and memory saturation during streaming medical histories. |
| 🔭 Frontier | [GroupMemBench](https://arxiv.org/abs/2605.14498) <!-- benchmark-id:groupmembench --> | 2026-05-14 | Speaker-grounded beliefs, group dynamics, terminology, and audience adaptation in multi-party conversations. |
| 🔭 Frontier | [MemEye](https://arxiv.org/abs/2605.15128) <!-- benchmark-id:memeye --> | 2026-05-14 | Benchmarks visual-centric agent memory across fine-grained visual evidence and temporal visual-state synthesis while checking whether visual evidence is genuinely necessary. |
| 🔭 Frontier | [MEMLENS](https://arxiv.org/abs/2605.14906) <!-- benchmark-id:memlens --> | 2026-05-14 | Multimodal extraction, updating, temporal reasoning, and abstention from 32K to 256K contexts. |
| 🔭 Frontier | [EvoMemBench](https://arxiv.org/abs/2605.18421) <!-- benchmark-id:evomembench --> | 2026-05-18 | Memory comparison across in-episode versus cross-episode scope and knowledge versus execution content. |
| 🔭 Frontier | [WorldMemArena](https://arxiv.org/abs/2605.29341) <!-- benchmark-id:worldmemarena --> | 2026-05-28 | Writing, maintaining, retrieving, and using multimodal memory from actions, observations, and feedback. |
| 🔭 Frontier | [LifeSide](https://arxiv.org/abs/2606.04660) <!-- benchmark-id:lifeside --> | 2026-06 | Benchmarks lifelong digital companions through multi-session memory, user understanding, privacy control, and emotional-environment dynamics. |
| 🔭 Frontier | [GateMem](https://arxiv.org/abs/2606.18829) <!-- benchmark-id:gatemem --> | 2026-06-17 | Utility, access control, and active forgetting in multi-principal shared memory. |
| 🔭 Frontier | [DynamicMem](https://arxiv.org/abs/2606.22877) <!-- benchmark-id:dynamicmem --> | 2026-06-22 | Inference and updating of user attributes, habits, and preferences from fifteen months of multi-app behavior. |
| 🔭 Frontier | [MEMPROBE](https://arxiv.org/abs/2606.24595) <!-- benchmark-id:memprobe --> | 2026-06-23 | Recovery of hidden user state from the memory artifact left after ordinary assistance. |
| 🔭 Frontier | [LoCoMo-Plus](https://aclanthology.org/2026.acl-long.1150/) <!-- benchmark-id:locomo-plus --> | 2026-07 | Evaluates cognitive memory where agents must retain and apply latent user constraints even when later cues are semantically disconnected. |
| 🔭 Frontier | [Mem-Gallery](https://aclanthology.org/2026.acl-long.1892/) <!-- benchmark-id:mem-gallery --> | 2026-07 | Evaluates multimodal long-term conversational memory across extraction and test-time adaptation, reasoning, and memory knowledge management. |
| 🔭 Frontier | [Mem2ActBench](https://aclanthology.org/2026.acl-long.370/) <!-- benchmark-id:mem2actbench --> | 2026-07 | Evaluates whether long-term memory is proactively used for tool selection and parameter grounding during tool-based assistant actions. |
| 🔭 Frontier | [PerMemSafe](https://aclanthology.org/2026.findings-acl.320/) <!-- benchmark-id:permemsafe --> | 2026-07 | Recognition and updating of implicit personalized risk across long, noise-heavy histories. |
| 🔭 Frontier | [MemFuseBench](https://arxiv.org/abs/2608.18704) <!-- benchmark-id:memfusebench --> | 2026-07-21 | Cross-source memory benchmark for linking, causal fusion, conflict arbitration, and provenance over heterogeneous event streams. |
| 🔭 Frontier | [InMind](https://arxiv.org/abs/2607.24368) <!-- benchmark-id:inmind --> | 2026-07-27 | Retrieval and use of a personal fact whose relevance to the query depends on world knowledge. |
| 🔭 Frontier | [PAST-Bench](https://arxiv.org/abs/2608.04003) <!-- benchmark-id:past-bench --> | 2026-08-04 | Paired persistent-state benchmark that tests whether retained cross-episode experience causally improves later executable work. |
| 🔭 Frontier | [SP-Mem Privacy-Aware Memory Benchmark](https://arxiv.org/abs/2608.16551) <!-- benchmark-id:sp-mem --> | 2026-08-17 | Privacy-aware memory benchmark that jointly measures response quality, personalization, consent handling, exact-value exposure, and cost. |<!-- TABLE-FIRST:AREA:agent-memory:END -->

### RAG / Agentic Retrieval

<!-- TABLE-FIRST:AREA:rag:START -->
| Role | Benchmark | Released | What it evaluates |
|---|---|---:|---|
| 🌱 Precursor | [HotpotQA](https://aclanthology.org/D18-1259/) <!-- benchmark-id:hotpotqa --> | 2018-10 | A foundational multi-hop QA benchmark requiring evidence retrieval and reasoning across multiple supporting documents. |
| 🧱 Foundation | [KILT](https://arxiv.org/abs/2009.02252) <!-- benchmark-id:kilt --> | 2020-09 | Unifies knowledge-intensive tasks against one Wikipedia snapshot and evaluates downstream task quality together with provenance. |
| 🧱 Foundation | [BEIR](https://arxiv.org/abs/2104.08663) <!-- benchmark-id:beir --> | 2021-04 | A heterogeneous benchmark for zero-shot information retrieval generalization across diverse domains and retrieval tasks. |
| 🧱 Foundation | [RGB](https://arxiv.org/abs/2309.01431) <!-- benchmark-id:rgb --> | 2023-09 | Decomposes retrieval-augmented generation into noise robustness, negative rejection, information integration, and counterfactual robustness. |
| ↗ Transition | [MultiHop-RAG](https://arxiv.org/abs/2401.15391) <!-- benchmark-id:multihop-rag --> | 2024-01 | A RAG-specific benchmark requiring retrieval and reasoning over multiple pieces of supporting evidence. |
| ↗ Transition | [RAGTruth](https://arxiv.org/abs/2401.00396) <!-- benchmark-id:ragtruth --> | 2024-01 | Provides fine-grained manual annotations of hallucinations in naturally generated RAG responses for evaluating grounding and hallucination detection. |
| ↗ Transition | [CRAG](https://arxiv.org/abs/2406.04744) <!-- benchmark-id:crag --> | 2024-06 | A factual RAG benchmark spanning dynamic facts, long-tail entities, web search, and knowledge-graph retrieval. |
| ↗ Transition | [BRIGHT](https://arxiv.org/abs/2407.12883) <!-- benchmark-id:bright --> | 2024-07 | Benchmarks retrieval on real-world queries where identifying relevant documents itself requires substantial reasoning. |
| ↗ Transition | [RAGBench](https://arxiv.org/abs/2407.11005) <!-- benchmark-id:ragbench --> | 2024-07 | A large-scale labeled benchmark for explainable evaluation of RAG systems across industry-oriented domains. |
| ↗ Transition | [BrowseComp](https://arxiv.org/abs/2504.12516) <!-- benchmark-id:browsecomp --> | 2025-04 | Benchmarks browsing agents on hard-to-find questions that require persistent web navigation and creative information seeking. |
| ↗ Transition | [T²-RAGBench](https://aclanthology.org/2026.eacl-long.8/) <!-- benchmark-id:t2-ragbench --> | 2025-05-14 | Text-and-table retrieval followed by numerical reasoning over financial reports. |
| ↗ Transition | [DeepResearch Bench](https://arxiv.org/abs/2506.11763) <!-- benchmark-id:deepresearch-bench --> | 2025-06 | Evaluates deep-research agents on multi-step web research, evidence collection, citation quality, and long-form report synthesis. |
| ↗ Transition | [BrowseComp-Plus](https://arxiv.org/abs/2508.06600) <!-- benchmark-id:browsecomp-plus --> | 2025-08 | Recasts deep-research evaluation over a fixed, curated corpus to isolate retriever and agent contributions and improve fairness and reproducibility. |
| 🔭 Frontier | [RAGCap-Bench](https://arxiv.org/abs/2510.13910) <!-- benchmark-id:ragcap-bench --> | 2025-10 | Decomposes agentic RAG into intermediate capabilities and evaluates those capabilities independently of final-answer quality. |
| 🔭 Frontier | [LIT-RAGBench](https://arxiv.org/abs/2603.06198) <!-- benchmark-id:lit-ragbench --> | 2025-10-22 | Generator logic, integration, table use, reasoning, and abstention with supplied RAG contexts. |
| 🔭 Frontier | [AgenticRAGTracer](https://arxiv.org/abs/2602.19127) <!-- benchmark-id:agenticragtracer --> | 2026-02 | Diagnoses multi-step agentic RAG by providing hop-aware intermediate validation rather than only final questions and answers. |
| 🔭 Frontier | [SAGE](https://arxiv.org/abs/2602.05975) <!-- benchmark-id:sage --> | 2026-02-05 | Targeted and open-ended scientific literature retrieval for deep-research agents. |
| 🔭 Frontier | [GISA](https://arxiv.org/abs/2602.08543) <!-- benchmark-id:gisa --> | 2026-02-06 | Search planning, deep reasoning, broad aggregation, and structured answering for authentic information needs. |
| 🔭 Frontier | [MC-Search](https://arxiv.org/abs/2603.00873) <!-- benchmark-id:mc-search --> | 2026-02-22 | Multimodal search planning, modality choice, hop-level retrieval, and long-chain reasoning fidelity. |
| 🔭 Frontier | [MTRAG-UN](https://aclanthology.org/2026.findings-acl.503/) <!-- benchmark-id:mtrag-un --> | 2026-02-26 | Multi-turn RAG handling of unanswerable, underspecified, non-standalone, and unclear turns. |
| 🔭 Frontier | [AutoResearchBench](https://arxiv.org/abs/2604.25256) <!-- benchmark-id:autoresearchbench --> | 2026-04-01 | Target-paper tracing, constrained literature search, open-set collection, and stopping decisions. |
| 🔭 Frontier | [LeakDojo](https://aclanthology.org/2026.findings-acl.287/) <!-- benchmark-id:leakdojo --> | 2026-04-07 | Extraction of RAG database content across attacks, models, pipelines, budgets, and defenses. |
| 🔭 Frontier | [EnterpriseRAG-Bench](https://arxiv.org/abs/2605.05253) <!-- benchmark-id:enterpriserag-bench --> | 2026-04-14 | Enterprise retrieval, multi-document reasoning, conflict handling, completeness, and not-found behavior. |
| 🔭 Frontier | [MERRIN](https://arxiv.org/abs/2604.13418) <!-- benchmark-id:merrin --> | 2026-04-15 | Uncued modality selection, multimodal evidence retrieval, and multi-hop reasoning on the noisy web. |
| 🔭 Frontier | [MuDABench](https://aclanthology.org/2026.findings-acl.341/) <!-- benchmark-id:mudabench --> | 2026-04-19 | Information extraction, cross-document aggregation, and quantitative analysis over large financial collections. |
| 🔭 Frontier | [Bright-Pro](https://aclanthology.org/2026.acl-long.1705/) <!-- benchmark-id:bright-pro --> | 2026-04-30 | Reasoning-intensive retrieval, aspect coverage, and retriever utility in static and agentic search. |
| 🔭 Frontier | [SGR-Bench](https://arxiv.org/abs/2605.22219) <!-- benchmark-id:sgr-bench --> | 2026-05 | Benchmarks search agents when answer-bearing evidence appears only after the agent establishes the correct site-specific retrieval state. |
| 🔭 Frontier | [ScholarQuest](https://arxiv.org/abs/2606.20235) <!-- benchmark-id:scholarquest --> | 2026-05-19 | Intent-conditioned iterative paper retrieval, citation expansion, scope control, and set coverage. |
| 🔭 Frontier | [LiveBrowseComp](https://arxiv.org/abs/2605.28721) <!-- benchmark-id:livebrowsecomp --> | 2026-05-27 | Retrieval of recent low-salience web facts rather than verification of parametric knowledge. |
| 🔭 Frontier | [EvoBrowseComp](https://arxiv.org/abs/2606.13120) <!-- benchmark-id:evobrowsecomp --> | 2026-06-11 | Broad English and Chinese web search over evolving knowledge. |
| 🔭 Frontier | [LoHoSearch](https://arxiv.org/abs/2606.12837) <!-- benchmark-id:lohosearch --> | 2026-06-11 | Long-horizon search under large candidate spaces, complex constraints, and context-management pressure. |
| 🔭 Frontier | [WANDR](https://arxiv.org/abs/2608.14747) <!-- benchmark-id:wandr --> | 2026-07-14 | Live-web benchmark for wide-and-deep record collection with hierarchical tasks and reference-free record verification. |
| 🔭 Frontier | [VAKRA](https://arxiv.org/abs/2608.12282) <!-- benchmark-id:vakra --> | 2026-08 | Evaluates agents that must compose executable APIs, document retrieval, multi-hop reasoning, and natural-language tool-use policies. |
| 🔭 Frontier | [MAPLE](https://arxiv.org/abs/2608.15624) <!-- benchmark-id:maple --> | 2026-08-04 | Scientific retrieval benchmark that measures whether one paper remains retrievable across motivation, method, and result aspects. |
| 🔭 Frontier | [SearchAuditBench](https://arxiv.org/abs/2608.05212) <!-- benchmark-id:searchauditbench --> | 2026-08-05 | Localization, root-cause attribution, and repair of failures in long deep-search trajectories. |
| 🔭 Frontier | [DAS-Bench / DAS-Eval](https://arxiv.org/abs/2608.18034) <!-- benchmark-id:das-bench --> | 2026-08-07 | Academic-survey benchmark and evaluator that score literature coverage, taxonomy, claims, citations, discourse, and rendered artifact quality. |
| 🔭 Frontier | [The Recall Trap](https://arxiv.org/abs/2608.14838) <!-- benchmark-id:recall-trap --> | 2026-08-10 | Validity audit showing that higher file recall can reduce downstream repair success under a fixed-slot code-retrieval protocol. |
| 🔭 Frontier | [The Commercial Tax](https://arxiv.org/abs/2608.16096) <!-- benchmark-id:commercial-tax --> | 2026-08-17 | Retrieval reproducibility audit that binds raw embedder scores to licensing, query formatting, index construction, and deployment cost. |
| 🔭 Frontier | [VisDocAgentBench](https://arxiv.org/abs/2608.17889) <!-- benchmark-id:visdocagentbench --> | 2026-08-18 | Visual-document retrieval benchmark that compares static rankers and iterative visual/OCR agents under one ranked-page contract. |<!-- TABLE-FIRST:AREA:rag:END -->

### Data Agents

<!-- TABLE-FIRST:AREA:data-agent:START -->
| Role | Benchmark | Released | What it evaluates |
|---|---|---:|---|
| 🌱 Precursor | [WikiSQL](https://arxiv.org/abs/1709.00103) <!-- benchmark-id:wikisql --> | 2017-08 | A large early benchmark for translating natural-language questions into executable SQL over individual Wikipedia tables. |
| 🧱 Foundation | [Spider](https://aclanthology.org/D18-1425/) <!-- benchmark-id:spider --> | 2018-10 | A foundational cross-domain text-to-SQL benchmark requiring generalization to unseen database schemas and complex multi-table SQL. |
| 🧱 Foundation | [DS-1000](https://arxiv.org/abs/2211.11501) <!-- benchmark-id:ds-1000 --> | 2022-11 | A natural benchmark for data-science code generation across major Python data libraries with execution-grounded evaluation. |
| ↗ Transition | [BIRD](https://arxiv.org/abs/2305.03111) <!-- benchmark-id:bird --> | 2023-05 | A large database-grounded text-to-SQL benchmark emphasizing real database values, dirty content, external knowledge, and SQL efficiency. |
| ↗ Transition | [MLAgentBench](https://arxiv.org/abs/2310.03302) <!-- benchmark-id:mlagentbench --> | 2023-10 | Benchmarks agents that iteratively design, execute, inspect, and improve machine-learning experiments rather than merely generating code once. |
| ↗ Transition | [InsightBench](https://arxiv.org/abs/2407.06423) <!-- benchmark-id:insightbench --> | 2024-07 | Evaluates end-to-end business analytics from question formulation through insight extraction and actionable recommendations. |
| ↗ Transition | [DA-Code](https://aclanthology.org/2024.emnlp-main.748/) <!-- benchmark-id:da-code --> | 2024-10 | Evaluates grounded executable data-analysis code over diverse real data, spanning wrangling, exploratory analysis, and machine learning. |
| ↗ Transition | [Spider 2.0](https://arxiv.org/abs/2411.07763) <!-- benchmark-id:spider-2 --> | 2024-11 | Evaluates language models on realistic enterprise text-to-SQL workflows involving huge schemas, multiple SQL dialects, metadata, codebases, and cloud databases. |
| ↗ Transition | [DataSciBench](https://arxiv.org/abs/2502.13897) <!-- benchmark-id:datascibench --> | 2025-02 | Benchmarks LLM agents on diverse data-science tasks with programmatic Task-Function-Code evaluation and human-verified ground truth. |
| 🔭 Frontier | [LiveSQLBench](https://livesqlbench.ai/) <!-- benchmark-id:livesqlbench --> | 2025-05-28 | Query and management SQL over evolving industrial databases, hierarchical knowledge, and drifting business rules. |
| ↗ Transition | [KramaBench](https://arxiv.org/abs/2506.06541) <!-- benchmark-id:kramabench --> | 2025-06-06 | End-to-end discovery, cleaning, integration, analysis, and modeling over messy heterogeneous data lakes. |
| ↗ Transition | [DABstep](https://arxiv.org/abs/2506.23719) <!-- benchmark-id:dabstep --> | 2025-06-30 | Multi-step financial analysis grounded in transactions, heterogeneous documentation, and domain rules. |
| 🔭 Frontier | [FDABench](https://arxiv.org/abs/2509.02473) <!-- benchmark-id:fdabench --> | 2025-09 | Evaluates data agents on analytical queries over heterogeneous structured, unstructured, web, and multimodal data. |
| ↗ Transition | [AgentDS](https://arxiv.org/abs/2603.19005) <!-- benchmark-id:agentds --> | 2025-10-18 | AI-only versus human-AI collaborative performance on domain-specific predictive data-science challenges across six industries. |
| 🔭 Frontier | [DDR-Bench](https://arxiv.org/abs/2602.02039) <!-- benchmark-id:ddr-bench --> | 2025-11-30 | Autonomous goal setting, exploration, hypothesis testing, and verifiable insight discovery from only an entity and database metadata. |
| 🔭 Frontier | [DAComp](https://arxiv.org/abs/2512.04324) <!-- benchmark-id:dacomp --> | 2025-12 | Benchmarks both repository-level data engineering and open-ended data analysis to cover a broader data-intelligence lifecycle. |
| 🔭 Frontier | [DSAEval](https://arxiv.org/abs/2601.13591) <!-- benchmark-id:dsaeval --> | 2026-01-20 | Cumulative multi-query data-science projects over tabular, image, and text data, scored on reasoning, code, and results. |
| 🔭 Frontier | [DSGym](https://arxiv.org/abs/2601.16344) <!-- benchmark-id:dsgym --> | 2026-01-22 | Shortcut-filtered analysis, prediction, and domain tasks in a unified isolated execution framework. |
| 🔭 Frontier | [DARE-bench](https://arxiv.org/abs/2602.24288) <!-- benchmark-id:dare-bench --> | 2026-02-27 | Verifiable ML-model quality and fidelity to prescribed data-science instructions and processes. |
| 🔭 Frontier | [Data Agent Benchmark (DAB)](https://arxiv.org/abs/2603.20576) <!-- benchmark-id:data-agent-benchmark --> | 2026-03 | Evaluates enterprise data agents on questions requiring integration, transformation, and analysis across multiple heterogeneous database systems. |
| 🔭 Frontier | [TML-Bench](https://arxiv.org/abs/2603.05764) <!-- benchmark-id:tml-bench --> | 2026-03-05 | Reliable end-to-end tabular-ML submissions under fixed wall-clock budgets and hidden labels. |
| 🔭 Frontier | [AgentFuel](https://arxiv.org/abs/2603.12483) <!-- benchmark-id:agentfuel --> | 2026-03-12 | Domain-customized functional evaluation of conversational time-series agents, especially stateful and incident-specific queries. |
| 🔭 Frontier | [DataClawBench](https://arxiv.org/abs/2605.02503) <!-- benchmark-id:dataclawbench --> | 2026-05-04 | Low-prior exploratory analysis over unfamiliar, noisy, cross-domain financial data with verifiable conclusions. |
| 🔭 Frontier | [IRTS-ToolBench](https://arxiv.org/abs/2606.15107) <!-- benchmark-id:irts-toolbench --> | 2026-06-13 | Tool-grounded QA over asynchronous, missing, variably sampled irregular time series. |
| 🔭 Frontier | [StatABench](https://arxiv.org/abs/2606.22977) <!-- benchmark-id:statabench --> | 2026-06-22 | Statistical knowledge, tool selection and parameterization, plus open end-to-end modeling and reporting. |
| 🔭 Frontier | [AgenticDataBench](https://arxiv.org/abs/2607.01647) <!-- benchmark-id:agenticdatabench --> | 2026-07 | Benchmarks data agents across realistic data-science workflows using a skill taxonomy to quantify fine-grained coverage. |
| 🔭 Frontier | [CausalDS](https://arxiv.org/abs/2607.08093) <!-- benchmark-id:causalds --> | 2026-07-09 | Executable causal data science across prediction, identification, effects, counterfactuals, uncertainty, and abstention. |
| 🔭 Frontier | [data-eng-bench](https://github.com/Snowflake-Labs/data-eng-bench) <!-- benchmark-id:data-eng-bench --> | 2026-07-29 | Executable data-engineering benchmark for repository-scale dbt transformations with hidden row-level verification on DuckDB and Snowflake. |
| 🔭 Frontier | [DataSpace](https://arxiv.org/abs/2608.03451) <!-- benchmark-id:dataspace --> | 2026-08 | Evaluates verifiable analytics over heterogeneous workspaces where evidence spans databases, files, documents, and multimedia. |
| 🔭 Frontier | [DSAgentBench](https://arxiv.org/abs/2608.10366) <!-- benchmark-id:dsagentbench --> | 2026-08 | Evaluates agents on complete data-science workflows inside real computer environments using notebooks, IDEs, terminals, browsers, and databases. |
| 🔭 Frontier | [WarehouseReliabilityBench](https://arxiv.org/abs/2608.09254) <!-- benchmark-id:warehouse-reliability-bench --> | 2026-08-10 | Business-correct analytics plus appropriate clarification, abstention, or refusal under ambiguity, unanswerability, drift, and attacks. |
| 🔭 Frontier | [Data Exploration Benchmark](https://arxiv.org/abs/2608.16045) <!-- benchmark-id:data-exploration-benchmark --> | 2026-08-17 | Structured dataset understanding before analysis, including logical tables, semantics, keys, relationships, and profiling signals. |<!-- TABLE-FIRST:AREA:data-agent:END -->

## What Is Still Poorly Measured

| Missing coordinate | Why it changes research conclusions |
|---|---|
| **Longitudinal real-user effects** | Preference drift, project evolution, and delayed consequences are difficult to compress into static QA. |
| **Irreversible actions + authority** | Correct retrieval is not enough when tools can spend money, modify state, or act with stale permissions. |
| **Lifecycle cost** | Construction/indexing/memory-writing, retries, controller calls, tool latency, and re-acquisition are often reported separately or omitted. |
| **Production reliability under drift** | Web, schema, tool, and environment changes can dominate a benchmark result without changing the model. |
| **Business-semantic correctness** | Executable SQL/code can still return the wrong business meaning; clarification and abstention often have no clean benchmark target. |

<a id="reading-paths"></a>
## Reading Paths

| Question | Start here | Then continue |
|---|---|---|
| **How did memory move from recall to action and governance?** | Multi-Session Chat → LoCoMo / LongMemEval → MemoryArena / WorldMemArena → GateMem / PerMemSafe / InMind | [Agent Memory Radar](https://github.com/H20Zhang/Agent-Memory-Radar#field-map) |
| **How did retrieval become live, auditable search?** | BEIR / BRIGHT → BrowseComp / LiveBrowseComp → Bright-Pro / LoHoSearch / SearchAuditBench / VAKRA → MAPLE / VisDocAgentBench / WANDR | [Agentic RAG Radar](https://github.com/H20Zhang/Agentic-RAG-Radar#field-map) |
| **How did data-agent evaluation move from SQL/code to reliable data work?** | Spider / DS-1000 → KramaBench / DABstep → DataClawBench / DSGym → DataSpace / DSAgentBench / WarehouseReliabilityBench | [Data Agent Radar](https://github.com/H20Zhang/Data-Agent-Radar#field-map) |

<a id="library"></a>
## Benchmark Library

- **[Continue browsing by time / area / genealogy / measurement coordinate](library/README.en.md)**
- [Canonical registry](data/benchmarks.json)
- [Research compactions](digests/README.md)

This repository tracks what is measured and why. Methods and systems belong in the three topic radars so the same survey does not need to be maintained twice.

[中文](README.md) · [Curation](CURATION.md) · [Schema](SCHEMA.md)
