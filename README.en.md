# Agent Benchmark Radar

[中文](README.md) | **English**

Benchmarks for Agent Memory, Agentic RAG, and Data Agents, organized by release date and research area. See the topic radars for methods and systems.

[Agent Memory Radar](https://github.com/H20Zhang/Agent-Memory-Radar) · [Agentic RAG Radar](https://github.com/H20Zhang/Agentic-RAG-Radar) · [Data Agent Radar](https://github.com/H20Zhang/Data-Agent-Radar)

[Last six months](#frontier) · [Three areas](#evolution) · [All benchmarks by area](#area-timelines) · [Reading paths](#reading-paths) · [Benchmark Library](#library)

Last updated: **2026-08-20**

A note on scores: when models, tool interfaces, prompts, retries, stopping rules, or budgets differ, the score describes the whole system and cannot be attributed to one component.

<a id="frontier"></a>
## Benchmark Timeline: Last Six Months

The window rolls six months back from the registry's latest verification date. Since some releases have only month-level precision, the whole boundary month is retained. The table is complete for that window, not curated.

<!-- RECENT-TIMELINE:START -->
| Released | Area | Benchmark | What it evaluates | What changed |
|---|---|---|---|---|
| 2026-08 | Data Agent | [DataSpace](https://arxiv.org/abs/2608.03451) <!-- benchmark-id:dataspace --> | Verifiable analytics over heterogeneous workspaces spanning databases, files, documents, and multimedia. | Unifies heterogeneous evidence discovery with deterministic complete-result evaluation. |
| 2026-08 | Data Agent | [DSAgentBench](https://arxiv.org/abs/2608.10366) <!-- benchmark-id:dsagentbench --> | Complete data-science workflows inside real computer environments using notebooks, IDEs, terminals, browsers, and databases. | Moves evaluation into grounded multi-stage, multi-tool execution. |
| 2026-08 | RAG | [VAKRA](https://arxiv.org/abs/2608.12282) <!-- benchmark-id:vakra --> | Composition of executable APIs, document retrieval, multi-hop reasoning, and tool-use policies. | Places cross-source grounding, execution, and policy consistency in one trajectory. |
| 2026-07 | Data Agent | [AgenticDataBench](https://arxiv.org/abs/2607.01647) <!-- benchmark-id:agenticdatabench --> | Fine-grained skill coverage across realistic data-science workflows. | Makes benchmark capability coverage auditable beyond aggregate task success. |
| 2026-07 | Agent Memory | [LoCoMo-Plus](https://aclanthology.org/2026.acl-long.1150/) <!-- benchmark-id:locomo-plus --> | Retaining and applying latent user constraints when later cues do not restate them. | Moves from explicit recall to consistent application of user state, goals, and values. |
| 2026-07 | Agent Memory | [Mem-Gallery](https://aclanthology.org/2026.acl-long.1892/) <!-- benchmark-id:mem-gallery --> | Memory extraction, adaptation, reasoning, and knowledge management in multimodal long-term conversations. | Makes visual retention, multimodal reasoning, and memory organization a unified target. |
| 2026-07 | Agent Memory | [Mem2ActBench](https://aclanthology.org/2026.acl-long.370/) <!-- benchmark-id:mem2actbench --> | Whether long-term memory drives tool selection and parameter grounding. | Makes action-level memory utilization directly measurable. |
| 2026-06 | Agent Memory | [LifeSide](https://arxiv.org/abs/2606.04660) <!-- benchmark-id:lifeside --> | Multi-session memory, user understanding, privacy control, and emotional-environment dynamics. | Connects memory to persistent user models, privacy boundaries, and environmental context. |
| 2026-05-14 | Agent Memory | [MemEye](https://arxiv.org/abs/2605.15128) <!-- benchmark-id:memeye --> | Fine-grained visual evidence, temporal visual-state synthesis, and text-only shortcut checks. | Requires genuinely necessary visual evidence rather than coarse captions or textual cues. |
| 2026-05 | Agent Memory | [LongMemEval-V2](https://arxiv.org/abs/2605.12493) <!-- benchmark-id:longmemeval-v2 --> | Environment state, workflow knowledge, and gotchas accumulated in web-agent trajectories. | Makes accumulated environment experience—not only user-history recall—a memory target. |
| 2026-05 | RAG | [SGR-Bench](https://arxiv.org/abs/2605.22219) <!-- benchmark-id:sgr-bench --> | Search when evidence is gated by site filters, hierarchy, scope, or view state. | Separates finding the right source from configuring the right retrieval state. |
| 2026-03 | Data Agent | [Data Agent Benchmark (DAB)](https://arxiv.org/abs/2603.20576) <!-- benchmark-id:data-agent-benchmark --> | Integration, transformation, analysis, and executable validation across multiple DBMSs. | Expands enterprise data questions from isolated SQL to a cross-database pipeline. |
| 2026-03 | Agent Memory | [LifeBench](https://arxiv.org/abs/2603.03781) <!-- benchmark-id:lifebench --> | Episodic, semantic, habitual, and procedural memory across long multi-source trajectories. | Extends the target beyond explicit facts to habits and procedural knowledge. |
| 2026-02-18 | Agent Memory | [MemoryArena](https://arxiv.org/abs/2602.16313) <!-- benchmark-id:memoryarena --> | Whether earlier actions and feedback guide later actions in multi-session Agent-Environment loops. | Directly couples long-term memory with future task action. |
| 2026-02 | RAG | [AgenticRAGTracer](https://arxiv.org/abs/2602.19127) <!-- benchmark-id:agenticragtracer --> | Hop-level validation and step allocation in multi-step retrieval-reasoning chains. | Makes the location of trajectory failures observable. |
| 2026-02 | Agent Memory | [AMA-Bench](https://arxiv.org/abs/2602.22769) <!-- benchmark-id:ama-bench --> | Long-horizon memory over real and scalable synthetic agent-environment trajectories. | Expands memory from dialogue to causally structured agent-environment experience. |
| 2026-02 | Agent Memory | [StructMemEval](https://arxiv.org/abs/2602.11243) <!-- benchmark-id:structmemeval --> | Whether agents maintain task-appropriate structures such as ledgers, lists, and trees. | Makes memory organization itself an observable capability. |
<!-- RECENT-TIMELINE:END -->

### Four Benchmarks in More Detail

<details><summary><strong>Why DSAgentBench changes the evaluation target</strong></summary>

Earlier data-agent benchmarks often isolate SQL, code generation, analytics answers, or selected workflow stages. DSAgentBench instead evaluates complete data-science work inside a real computer environment, where the agent must coordinate tools and ground later decisions in intermediate outputs.

The benchmark contains **275 tasks** across the data-science lifecycle and uses deterministic checks for analytical correctness, visual outputs, and model performance. The paper reports **56.70% task success for the strongest evaluated agent**, while open-source agents remain below 1%. The result is system-level evidence: model, harness, tool-use reliability, OS grounding, and long-horizon reasoning all move together. Its importance is therefore the **environment/protocol shift**, not one model ranking.

</details>

<details><summary><strong>Why DataSpace is different from another analytics dataset</strong></summary>

DataSpace gives the agent only a question and a task-local heterogeneous workspace containing combinations of CSV, JSON, SQLite, Markdown, PDF, and video, then requires the complete requested tabular result. That couples **evidence discovery, cross-source joins, multimodal access, and deterministic answer verification**.

It contains **410 tasks and 7,439 artifacts**. The paper reports a **15.36-point spread from harness choice with the backbone fixed**, which is itself a warning: data-agent scores are highly harness-sensitive. DataSpace therefore measures a broader information environment, but it does not isolate which controller or retrieval component caused a system-level gain.

</details>

<details><summary><strong>Why LoCoMo-Plus matters beyond factual recall</strong></summary>

Conventional long-term-memory QA often gives later questions cues that overlap directly with stored facts. LoCoMo-Plus targets **cue–trigger semantic disconnect**: the agent must preserve and apply a latent user constraint even when the later query does not restate it.

That changes the evaluation object from “can I retrieve an old fact?” toward “does remembered user state constrain future behavior correctly?” The remaining validity question is whether constraint-consistency evaluation transfers to persistent acting agents with real preference drift, permissions, and irreversible decisions.

</details>

<details><summary><strong>Why VAKRA changes RAG evaluation</strong></summary>

VAKRA combines executable API calls, document retrieval, multi-hop reasoning, and tool-use policies in the same trajectory. This exposes failures that disappear when API use and document QA are benchmarked separately: identity mismatch, cross-source grounding failure, and policy-inconsistent execution.

The benchmark supports trajectory-level system claims, not a clean attribution to retrieval policy. Its value is making **cross-source executable coherence** observable.

</details>

<a id="evolution"></a>
## Three Areas

| Area | Broad shift | Current question | Topic radar |
|---|---|---|---|
| **Agent Memory** | multi-session recall → time/update/forget → structure/scale/multimodality → **implicit user state + memory-guided action** | What should be written, updated, inferred, forgotten, and applied to future behavior? | [Agent Memory Radar](https://github.com/H20Zhang/Agent-Memory-Radar) |
| **RAG / Agentic Retrieval** | retrieval quality → robustness/faithfulness → deep research → **stateful, controlled, cross-source execution** | Can the agent configure and navigate an information environment under changing state and budgets? | [Agentic RAG Radar](https://github.com/H20Zhang/Agentic-RAG-Radar) |
| **Data Agents** | NL→SQL/code → experimentation/workflows → heterogeneous analytics → **real-computer end-to-end data work** | Can an agent discover, transform, analyze, verify, recover, and deliver useful artifacts? | [Data Agent Radar](https://github.com/H20Zhang/Data-Agent-Radar) |

<a id="area-timelines"></a>
## All Benchmarks by Area

All 48 benchmarks in the registry are listed below, from oldest to newest.

### Agent Memory

<!-- COMPLETE-MAP:agent-memory:START -->
| Role | Benchmark | Released | What it evaluates | Why it changed the question |
|---|---|---:|---|---|
| 🌱 Precursor | [Beyond Goldfish Memory](https://aclanthology.org/2022.acl-long.356/) <!-- benchmark-id:beyond-goldfish-memory --> | 2022-05 | Benchmarks long-term open-domain conversation across multiple human-human chat sessions where partners must remember and remain consistent with prior interactions. | Established cross-session conversation as a distinct long-term-memory setting before modern memory-agent benchmarks. |
| 🧱 Foundation | [LoCoMo](https://aclanthology.org/2024.acl-long.747/) <!-- benchmark-id:locomo --> | 2024-08 | Long-horizon conversational-memory benchmark spanning QA, event summarization, and multimodal dialogue generation over very long multi-session conversations. | Established very-long-term conversational memory as a first-class evaluation target rather than a short-context dialogue property. |
| 🧱 Foundation | [LongMemEval](https://arxiv.org/abs/2410.10813) <!-- benchmark-id:longmemeval --> | 2024-10 | Evaluates sustained chat-assistant memory across extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention. | Made update, temporal reasoning, and abstention explicit instead of collapsing long-term memory into factual recall. |
| ↗ Transition | [MemBench](https://arxiv.org/abs/2506.21605) <!-- benchmark-id:membench --> | 2025-06 | Broadens memory evaluation across factual and reflective memory, participation and observation scenarios, and effectiveness, efficiency, and capacity. | Expanded evaluation from answer accuracy toward different memory levels, interaction roles, efficiency, and capacity. |
| ↗ Transition | [MemoryAgentBench](https://arxiv.org/abs/2507.05257) <!-- benchmark-id:memoryagentbench --> | 2025-07 | Evaluates memory agents under incremental multi-turn interaction across retrieval, test-time learning, long-range understanding, and selective forgetting. | Shifted the object from a static long context to a memory agent that must incrementally absorb, update, use, and forget information. |
| ↗ Transition | [BEAM](https://arxiv.org/abs/2510.27246) <!-- benchmark-id:beam --> | 2025-10 | Tests long-term memory on coherent conversations extending from million-token to multi-million-token horizons. | Made memory degradation with truly massive, coherent histories directly measurable. |
| 🔭 Frontier | [RealMem](https://aclanthology.org/2026.findings-acl.703/) <!-- benchmark-id:realmem --> | 2026-01 | Evaluates long-term memory over project-oriented cross-session interactions whose goals, artifacts, and relevant state evolve over time. | Moves long-term-memory evaluation from casual conversation toward persistent project state and evolving user goals. |
| 🔭 Frontier | [AMA-Bench](https://arxiv.org/abs/2602.22769) <!-- benchmark-id:ama-bench --> | 2026-02 | Evaluates long-horizon memory over real and synthetic agent-environment trajectories rather than dialogue-only histories. | Moved agent memory from human-agent dialogue toward machine-generated agent-environment experience and causality. |
| 🔭 Frontier | [StructMemEval](https://arxiv.org/abs/2602.11243) <!-- benchmark-id:structmemeval --> | 2026-02 | Tests whether agents organize memory into task-appropriate structures such as ledgers, lists, and trees rather than only retrieving facts. | Makes memory structure itself observable as a capability. |
| 🔭 Frontier | [MemoryArena](https://arxiv.org/abs/2602.16313) <!-- benchmark-id:memoryarena --> | 2026-02-18 | Evaluates memory inside multi-session Memory-Agent-Environment loops where earlier actions and feedback must be distilled and used to guide later actions. | Directly couples long-term memorization with future action instead of evaluating recall and acting as separate abilities. |
| 🔭 Frontier | [LifeBench](https://arxiv.org/abs/2603.03781) <!-- benchmark-id:lifebench --> | 2026-03 | Evaluates long-horizon multi-source memory spanning declarative and non-declarative information such as habits and procedures. | Expands memory beyond explicit facts to inferred habitual and procedural knowledge across heterogeneous traces. |
| 🔭 Frontier | [LongMemEval-V2](https://arxiv.org/abs/2605.12493) <!-- benchmark-id:longmemeval-v2 --> | 2026-05 | Evaluates whether memory systems internalize environment-specific experience from large web-agent trajectory histories. | Makes accumulated environment experience and workflow knowledge a memory target, not merely user-history recall. |
| 🔭 Frontier | [MemEye](https://arxiv.org/abs/2605.15128) <!-- benchmark-id:memeye --> | 2026-05-14 | Benchmarks visual-centric agent memory across fine-grained visual evidence and temporal visual-state synthesis while checking whether visual evidence is genuinely necessary. | Forces systems to retain genuinely necessary visual evidence rather than succeeding through text-only shortcuts or coarse captions. |
| 🔭 Frontier | [LifeSide](https://arxiv.org/abs/2606.04660) <!-- benchmark-id:lifeside --> | 2026-06 | Benchmarks lifelong digital companions through multi-session memory, user understanding, privacy control, and emotional-environment dynamics. | Connects memory to persistent user models, privacy boundaries, and emotional/environmental context. |
| 🔭 Frontier | [LoCoMo-Plus](https://aclanthology.org/2026.acl-long.1150/) <!-- benchmark-id:locomo-plus --> | 2026-07 | Evaluates cognitive memory where agents must retain and apply latent user constraints even when later cues are semantically disconnected. | Moves the target from remembering explicit facts to applying latent user state, goals, and values when the cue no longer restates them. |
| 🔭 Frontier | [Mem-Gallery](https://aclanthology.org/2026.acl-long.1892/) <!-- benchmark-id:mem-gallery --> | 2026-07 | Evaluates multimodal long-term conversational memory across extraction and test-time adaptation, reasoning, and memory knowledge management. | Makes visual retention, multimodal reasoning, and memory organization first-class long-term-memory evaluation targets. |
| 🔭 Frontier | [Mem2ActBench](https://aclanthology.org/2026.acl-long.370/) <!-- benchmark-id:mem2actbench --> | 2026-07 | Evaluates whether long-term memory is proactively used for tool selection and parameter grounding during tool-based assistant actions. | Makes action-level memory utilization directly measurable instead of reading memory quality only through answers about past context. |
<!-- COMPLETE-MAP:agent-memory:END -->

Recent work now tests writing, updating, forgetting, organization, multimodal fidelity, user state, and action separately. What remains missing is longitudinal causality in real persistent environments, with comparable budgets and permissions and enough time for state changes and irreversible actions to matter.

[Continue into Agent Memory methods and systems →](https://github.com/H20Zhang/Agent-Memory-Radar)

### RAG / Agentic Retrieval

<!-- COMPLETE-MAP:rag:START -->
| Role | Benchmark | Released | What it evaluates | Why it changed the question |
|---|---|---:|---|---|
| 🌱 Precursor | [HotpotQA](https://aclanthology.org/D18-1259/) <!-- benchmark-id:hotpotqa --> | 2018-10 | A foundational multi-hop QA benchmark requiring evidence retrieval and reasoning across multiple supporting documents. | Established multi-document evidence composition and explainable supporting facts as measurable retrieval-reasoning targets. |
| 🧱 Foundation | [KILT](https://arxiv.org/abs/2009.02252) <!-- benchmark-id:kilt --> | 2020-09 | Unifies knowledge-intensive tasks against one Wikipedia snapshot and evaluates downstream task quality together with provenance. | Made retrieval provenance and reusable retrieval infrastructure first-class across multiple downstream tasks. |
| 🧱 Foundation | [BEIR](https://arxiv.org/abs/2104.08663) <!-- benchmark-id:beir --> | 2021-04 | A heterogeneous benchmark for zero-shot information retrieval generalization across diverse domains and retrieval tasks. | Established cross-domain robustness as a retriever requirement instead of optimizing only one benchmark such as MS MARCO. |
| 🧱 Foundation | [RGB](https://arxiv.org/abs/2309.01431) <!-- benchmark-id:rgb --> | 2023-09 | Decomposes retrieval-augmented generation into noise robustness, negative rejection, information integration, and counterfactual robustness. | Made correct use of retrieved context a multi-dimensional evaluation target rather than a single end-to-end answer score. |
| ↗ Transition | [MultiHop-RAG](https://arxiv.org/abs/2401.15391) <!-- benchmark-id:multihop-rag --> | 2024-01 | A RAG-specific benchmark requiring retrieval and reasoning over multiple pieces of supporting evidence. | Made multi-hop retrieval failure visible inside a RAG pipeline instead of treating retrieval as single-shot relevance. |
| ↗ Transition | [RAGTruth](https://arxiv.org/abs/2401.00396) <!-- benchmark-id:ragtruth --> | 2024-01 | Provides fine-grained manual annotations of hallucinations in naturally generated RAG responses for evaluating grounding and hallucination detection. | Makes localized grounding failures in RAG outputs measurable instead of reducing faithfulness to one document- or answer-level label. |
| ↗ Transition | [CRAG](https://arxiv.org/abs/2406.04744) <!-- benchmark-id:crag --> | 2024-06 | A factual RAG benchmark spanning dynamic facts, long-tail entities, web search, and knowledge-graph retrieval. | Made freshness, popularity, and factual dynamism central to RAG evaluation and powered the KDD Cup 2024 challenge. |
| ↗ Transition | [BRIGHT](https://arxiv.org/abs/2407.12883) <!-- benchmark-id:bright --> | 2024-07 | Benchmarks retrieval on real-world queries where identifying relevant documents itself requires substantial reasoning. | Shows that semantic similarity alone under-tests retrieval when relevance depends on reasoning about the query and candidate documents. |
| ↗ Transition | [RAGBench](https://arxiv.org/abs/2407.11005) <!-- benchmark-id:ragbench --> | 2024-07 | A large-scale labeled benchmark for explainable evaluation of RAG systems across industry-oriented domains. | Shifted attention from only benchmarking RAG systems to benchmarking the evaluators and actionable failure labels used to judge them. |
| ↗ Transition | [BrowseComp](https://arxiv.org/abs/2504.12516) <!-- benchmark-id:browsecomp --> | 2025-04 | Benchmarks browsing agents on hard-to-find questions that require persistent web navigation and creative information seeking. | Made persistence and creativity in web information seeking a simple, widely reusable agent benchmark. |
| ↗ Transition | [DeepResearch Bench](https://arxiv.org/abs/2506.11763) <!-- benchmark-id:deepresearch-bench --> | 2025-06 | Evaluates deep-research agents on multi-step web research, evidence collection, citation quality, and long-form report synthesis. | Expanded search-agent evaluation from finding an answer to producing analyst-style, citation-rich research artifacts. |
| ↗ Transition | [BrowseComp-Plus](https://arxiv.org/abs/2508.06600) <!-- benchmark-id:browsecomp-plus --> | 2025-08 | Recasts deep-research evaluation over a fixed, curated corpus to isolate retriever and agent contributions and improve fairness and reproducibility. | Makes BrowseComp-style deep research reproducible enough to attribute gains to retrieval and agent behavior rather than an opaque live search stack. |
| 🔭 Frontier | [RAGCap-Bench](https://arxiv.org/abs/2510.13910) <!-- benchmark-id:ragcap-bench --> | 2025-10 | Decomposes agentic RAG into intermediate capabilities and evaluates those capabilities independently of final-answer quality. | Made intermediate agentic-RAG skills an explicit evaluation object rather than attributing end-to-end failures to a black box. |
| 🔭 Frontier | [AgenticRAGTracer](https://arxiv.org/abs/2602.19127) <!-- benchmark-id:agenticragtracer --> | 2026-02 | Diagnoses multi-step agentic RAG by providing hop-aware intermediate validation rather than only final questions and answers. | Makes where a retrieval-reasoning chain fails observable at hop granularity. |
| 🔭 Frontier | [SGR-Bench](https://arxiv.org/abs/2605.22219) <!-- benchmark-id:sgr-bench --> | 2026-05 | Benchmarks search agents when answer-bearing evidence appears only after the agent establishes the correct site-specific retrieval state. | Separates finding the right source from configuring the right filters, hierarchy, scope, or view inside that source. |
| 🔭 Frontier | [VAKRA](https://arxiv.org/abs/2608.12282) <!-- benchmark-id:vakra --> | 2026-08 | Evaluates agents that must compose executable APIs, document retrieval, multi-hop reasoning, and natural-language tool-use policies. | Unifies structured API interaction and unstructured retrieval in one executable evaluation with policy constraints. |
<!-- COMPLETE-MAP:rag:END -->

Retrieval evaluation now extends beyond document ranking to source state, tool use, stopping, and cross-source execution. Attribution remains difficult: interfaces, harnesses, models, and budgets must be comparable, while live environments keep changing underneath the evaluation.

[Continue into Agentic RAG methods and systems →](https://github.com/H20Zhang/Agentic-RAG-Radar)

### Data Agents

<!-- COMPLETE-MAP:data-agent:START -->
| Role | Benchmark | Released | What it evaluates | Why it changed the question |
|---|---|---:|---|---|
| 🌱 Precursor | [WikiSQL](https://arxiv.org/abs/1709.00103) <!-- benchmark-id:wikisql --> | 2017-08 | A large early benchmark for translating natural-language questions into executable SQL over individual Wikipedia tables. | Made executable natural-language database querying a large-scale benchmarkable task. |
| 🧱 Foundation | [Spider](https://aclanthology.org/D18-1425/) <!-- benchmark-id:spider --> | 2018-10 | A foundational cross-domain text-to-SQL benchmark requiring generalization to unseen database schemas and complex multi-table SQL. | Made cross-schema generalization and complex SQL the canonical database-language benchmark rather than memorizing one schema. |
| 🧱 Foundation | [DS-1000](https://arxiv.org/abs/2211.11501) <!-- benchmark-id:ds-1000 --> | 2022-11 | A natural benchmark for data-science code generation across major Python data libraries with execution-grounded evaluation. | Established reliable executable evaluation for practical data-science coding beyond SQL. |
| ↗ Transition | [BIRD](https://arxiv.org/abs/2305.03111) <!-- benchmark-id:bird --> | 2023-05 | A large database-grounded text-to-SQL benchmark emphasizing real database values, dirty content, external knowledge, and SQL efficiency. | Moved text-to-SQL toward large, messy, value-rich databases and made SQL efficiency visible. |
| ↗ Transition | [MLAgentBench](https://arxiv.org/abs/2310.03302) <!-- benchmark-id:mlagentbench --> | 2023-10 | Benchmarks agents that iteratively design, execute, inspect, and improve machine-learning experiments rather than merely generating code once. | Turns data-science coding into an iterative scientific-experimentation problem with feedback from executed results. |
| ↗ Transition | [InsightBench](https://arxiv.org/abs/2407.06423) <!-- benchmark-id:insightbench --> | 2024-07 | Evaluates end-to-end business analytics from question formulation through insight extraction and actionable recommendations. | Moves data-agent evaluation from answering a given query toward discovering and communicating useful analysis. |
| ↗ Transition | [DA-Code](https://aclanthology.org/2024.emnlp-main.748/) <!-- benchmark-id:da-code --> | 2024-10 | Evaluates grounded executable data-analysis code over diverse real data, spanning wrangling, exploratory analysis, and machine learning. | Bridges static code generation and agent-style data work by requiring planning and executable grounding in task data. |
| ↗ Transition | [Spider 2.0](https://arxiv.org/abs/2411.07763) <!-- benchmark-id:spider-2 --> | 2024-11 | Evaluates language models on realistic enterprise text-to-SQL workflows involving huge schemas, multiple SQL dialects, metadata, codebases, and cloud databases. | Turned text-to-SQL from a one-shot semantic parsing task into a long-horizon enterprise workflow problem. |
| ↗ Transition | [DataSciBench](https://arxiv.org/abs/2502.13897) <!-- benchmark-id:datascibench --> | 2025-02 | Benchmarks LLM agents on diverse data-science tasks with programmatic Task-Function-Code evaluation and human-verified ground truth. | Broadened evaluation beyond easily graded single tasks toward heterogeneous data-science prompts and task-specific metrics. |
| 🔭 Frontier | [FDABench](https://arxiv.org/abs/2509.02473) <!-- benchmark-id:fdabench --> | 2025-09 | Evaluates data agents on analytical queries over heterogeneous structured, unstructured, web, and multimodal data. | Expanded data-agent evaluation from SQL or code to multi-source analytical workflows, while exposing cost and reasoning traces. |
| 🔭 Frontier | [DAComp](https://arxiv.org/abs/2512.04324) <!-- benchmark-id:dacomp --> | 2025-12 | Benchmarks both repository-level data engineering and open-ended data analysis to cover a broader data-intelligence lifecycle. | Separates and jointly covers data engineering and analysis, moving evaluation toward the full data-intelligence lifecycle rather than isolated query or code tasks. |
| 🔭 Frontier | [Data Agent Benchmark (DAB)](https://arxiv.org/abs/2603.20576) <!-- benchmark-id:data-agent-benchmark --> | 2026-03 | Evaluates enterprise data agents on questions requiring integration, transformation, and analysis across multiple heterogeneous database systems. | Targets the full enterprise data-question pipeline rather than isolated SQL generation or small in-context tables. |
| 🔭 Frontier | [AgenticDataBench](https://arxiv.org/abs/2607.01647) <!-- benchmark-id:agenticdatabench --> | 2026-07 | Benchmarks data agents across realistic data-science workflows using a skill taxonomy to quantify fine-grained coverage. | Makes data-science skill coverage itself explicit, enabling diagnosis beyond aggregate task success. |
| 🔭 Frontier | [DataSpace](https://arxiv.org/abs/2608.03451) <!-- benchmark-id:dataspace --> | 2026-08 | Evaluates verifiable analytics over heterogeneous workspaces where evidence spans databases, files, documents, and multimedia. | Unifies heterogeneous evidence discovery with deterministic complete-result evaluation in a task-local workspace. |
| 🔭 Frontier | [DSAgentBench](https://arxiv.org/abs/2608.10366) <!-- benchmark-id:dsagentbench --> | 2026-08 | Evaluates agents on complete data-science workflows inside real computer environments using notebooks, IDEs, terminals, browsers, and databases. | Moves data-agent evaluation into real computer environments where success requires multi-stage, multi-tool execution grounded in intermediate outputs. |
<!-- COMPLETE-MAP:data-agent:END -->

Data-agent benchmarks are moving from SQL or code generation toward complete data work: finding heterogeneous evidence, coordinating tools, checking results, and delivering artifacts. They still cover little of real enterprise semantics, ambiguous business definitions, long-running state, governance, or when an agent should clarify or abstain.

[Continue into Data Agent methods and systems →](https://github.com/H20Zhang/Data-Agent-Radar)

## What Is Still Poorly Measured

Some important questions still lack a clean benchmark.

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
| **How did memory move from recall to action?** | Multi-Session Chat → LoCoMo → LongMemEval → MemoryArena / Mem2ActBench / LoCoMo-Plus | [Agent Memory Radar](https://github.com/H20Zhang/Agent-Memory-Radar) |
| **How did retrieval become a stateful control problem?** | HotpotQA / BEIR → BrowseComp → SGR-Bench → VAKRA | [Agentic RAG Radar](https://github.com/H20Zhang/Agentic-RAG-Radar) |
| **How did data-agent evaluation move from SQL/code to real workspaces?** | WikiSQL / Spider / DS-1000 → AgenticDataBench → DataSpace → DSAgentBench | [Data Agent Radar](https://github.com/H20Zhang/Data-Agent-Radar) |

<a id="library"></a>
## Benchmark Library

- **[Browse by time / area / genealogy / measurement coordinate](library/README.en.md)**
- [Canonical registry](data/benchmarks.json)
- [Research compactions](digests/README.md)

## This Repository and the Topic Radars

This repository tracks what is measured and why. Methods and systems belong in the three topic radars, so the same survey does not need to be maintained twice.

[中文](README.md) · [Curation](CURATION.md) · [Schema](SCHEMA.md)
