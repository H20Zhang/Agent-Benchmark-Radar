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
| Time | Area | Benchmark | What it tests | What changed |
|---|---|---|---|---|
| 2026-08-18 | RAG | [VisDocAgentBench](https://arxiv.org/abs/2608.17889) <!-- benchmark-id:visdocagentbench --> | Visual-document retrieval benchmark that compares static rankers and iterative visual/OCR agents under one ranked-page contract. | Compares static visual retrieval with iterative page discovery and inspection under one top-10 contract. |
| 2026-08-17 | Data Agent | [Data Exploration Benchmark](https://arxiv.org/abs/2608.16045) <!-- benchmark-id:data-exploration-benchmark --> | Structured dataset understanding before analysis, including logical tables, semantics, keys, relationships, and profiling signals. | Turns implicit data exploration from a prerequisite hidden behind final-answer accuracy into a directly scored artifact with measured downstream value. |
| 2026-08-17 | Agent Memory | [SP-Mem Privacy-Aware Memory Benchmark](https://arxiv.org/abs/2608.16551) <!-- benchmark-id:sp-mem --> | Privacy-aware memory benchmark that jointly measures response quality, personalization, consent handling, exact-value exposure, and cost. | Places personalization benefit, authorization, and leakage risk in one memory-lifecycle protocol. |
| 2026-08-17 | RAG | [The Commercial Tax](https://arxiv.org/abs/2608.16096) <!-- benchmark-id:commercial-tax --> | Retrieval reproducibility audit that binds raw embedder scores to licensing, query formatting, index construction, and deployment cost. | Audits retrieval-number transferability against license, query format, index construction, and cost. |
| 2026-08-10 | RAG | [The Recall Trap](https://arxiv.org/abs/2608.14838) <!-- benchmark-id:recall-trap --> | Validity audit showing that higher file recall can reduce downstream repair success under a fixed-slot code-retrieval protocol. | Shows that higher file recall can lower repair success under fixed slots, limiting recall's interpretation. |
| 2026-08-10 | Data Agent | [WarehouseReliabilityBench](https://arxiv.org/abs/2608.09254) <!-- benchmark-id:warehouse-reliability-bench --> | Business-correct analytics plus appropriate clarification, abstention, or refusal under ambiguity, unanswerability, drift, and attacks. | Moves beyond executable SQL to business truth and correct non-answer behavior when returning a number would be false success. |
| 2026-08-07 | RAG | [DAS-Bench / DAS-Eval](https://arxiv.org/abs/2608.18034) <!-- benchmark-id:das-bench --> | Academic-survey benchmark and evaluator that score literature coverage, taxonomy, claims, citations, discourse, and rendered artifact quality. | Turns coverage, taxonomy, claims, citations, discourse, and artifact quality into a 16-criterion survey protocol. |
| 2026-08-05 | RAG | [SearchAuditBench](https://arxiv.org/abs/2608.05212) <!-- benchmark-id:searchauditbench --> | Localization, root-cause attribution, and repair of failures in long deep-search trajectories. | Adds expert critical-step labels, a six-way cause taxonomy, and repair-based recovery evaluation. |
| 2026-08-04 | RAG | [MAPLE](https://arxiv.org/abs/2608.15624) <!-- benchmark-id:maple --> | Scientific retrieval benchmark that measures whether one paper remains retrievable across motivation, method, and result aspects. | Measures whether one paper stays retrievable across aspects instead of only one-query relevance. |
| 2026-08-04 | Agent Memory | [PAST-Bench](https://arxiv.org/abs/2608.04003) <!-- benchmark-id:past-bench --> | Paired persistent-state benchmark that tests whether retained cross-episode experience causally improves later executable work. | Uses persistence-on/off controls to attribute executable cross-episode benefit to retained state. |
| 2026-08 | Data Agent | [DataSpace](https://arxiv.org/abs/2608.03451) <!-- benchmark-id:dataspace --> | Evaluates verifiable analytics over heterogeneous workspaces where evidence spans databases, files, documents, and multimedia. | Unifies heterogeneous evidence discovery with deterministic complete-result evaluation in a task-local workspace. |
| 2026-08 | Data Agent | [DSAgentBench](https://arxiv.org/abs/2608.10366) <!-- benchmark-id:dsagentbench --> | Evaluates agents on complete data-science workflows inside real computer environments using notebooks, IDEs, terminals, browsers, and databases. | Moves data-agent evaluation into real computer environments where success requires multi-stage, multi-tool execution grounded in intermediate outputs. |
| 2026-08 | RAG | [VAKRA](https://arxiv.org/abs/2608.12282) <!-- benchmark-id:vakra --> | Evaluates agents that must compose executable APIs, document retrieval, multi-hop reasoning, and natural-language tool-use policies. | Unifies structured API interaction and unstructured retrieval in one executable evaluation with policy constraints. |
| 2026-07-29 | Data Agent | [data-eng-bench](https://github.com/Snowflake-Labs/data-eng-bench) <!-- benchmark-id:data-eng-bench --> | Executable data-engineering benchmark for repository-scale dbt transformations with hidden row-level verification on DuckDB and Snowflake. | Uses executable dbt tasks and hidden row-level checks; an August fix makes evaluator reliability part of the measurement object. |
| 2026-07-27 | Agent Memory | [InMind](https://arxiv.org/abs/2607.24368) <!-- benchmark-id:inmind --> | Retrieval and use of a personal fact whose relevance to the query depends on world knowledge. | Paired controls separate storage, knowledge, routing, and final-use failures. |
| 2026-07-21 | Agent Memory | [MemFuseBench](https://arxiv.org/abs/2608.18704) <!-- benchmark-id:memfusebench --> | Cross-source memory benchmark for linking, causal fusion, conflict arbitration, and provenance over heterogeneous event streams. | Separates linking, causal fusion, conflict handling, and provenance across heterogeneous sources. |
| 2026-07-14 | RAG | [WANDR](https://arxiv.org/abs/2608.14747) <!-- benchmark-id:wandr --> | Live-web benchmark for wide-and-deep record collection with hierarchical tasks and reference-free record verification. | Combines open-set discovery, enrichment, and record-level verification on the live web. |
| 2026-07-09 | Data Agent | [CausalDS](https://arxiv.org/abs/2607.08093) <!-- benchmark-id:causalds --> | Executable causal data science across prediction, identification, effects, counterfactuals, uncertainty, and abstention. | Extends data-agent evaluation beyond association and prediction to all Pearl rungs and recognition of unwarranted answers. |
| 2026-07 | Data Agent | [AgenticDataBench](https://arxiv.org/abs/2607.01647) <!-- benchmark-id:agenticdatabench --> | Benchmarks data agents across realistic data-science workflows using a skill taxonomy to quantify fine-grained coverage. | Makes data-science skill coverage itself explicit, enabling diagnosis beyond aggregate task success. |
| 2026-07 | Agent Memory | [LoCoMo-Plus](https://aclanthology.org/2026.acl-long.1150/) <!-- benchmark-id:locomo-plus --> | Evaluates cognitive memory where agents must retain and apply latent user constraints even when later cues are semantically disconnected. | Moves the target from remembering explicit facts to applying latent user state, goals, and values when the cue no longer restates them. |
| 2026-07 | Agent Memory | [Mem-Gallery](https://aclanthology.org/2026.acl-long.1892/) <!-- benchmark-id:mem-gallery --> | Evaluates multimodal long-term conversational memory across extraction and test-time adaptation, reasoning, and memory knowledge management. | Makes visual retention, multimodal reasoning, and memory organization first-class long-term-memory evaluation targets. |
| 2026-07 | Agent Memory | [Mem2ActBench](https://aclanthology.org/2026.acl-long.370/) <!-- benchmark-id:mem2actbench --> | Evaluates whether long-term memory is proactively used for tool selection and parameter grounding during tool-based assistant actions. | Makes action-level memory utilization directly measurable instead of reading memory quality only through answers about past context. |
| 2026-07 | Agent Memory | [PerMemSafe](https://aclanthology.org/2026.findings-acl.320/) <!-- benchmark-id:permemsafe --> | Recognition and updating of implicit personalized risk across long, noise-heavy histories. | Extends user-state memory to evolving personalized safety while retaining helpfulness. |
| 2026-06-23 | Agent Memory | [MEMPROBE](https://arxiv.org/abs/2606.24595) <!-- benchmark-id:memprobe --> | Recovery of hidden user state from the memory artifact left after ordinary assistance. | Moves from indirect downstream behavior to direct auditing of the stored memory artifact. |
| 2026-06-22 | Agent Memory | [DynamicMem](https://arxiv.org/abs/2606.22877) <!-- benchmark-id:dynamicmem --> | Inference and updating of user attributes, habits, and preferences from fifteen months of multi-app behavior. | Moves user memory to multi-million-token histories, long-term drift, and implicit evidence distributed across applications. |
| 2026-06-22 | Data Agent | [StatABench](https://arxiv.org/abs/2606.22977) <!-- benchmark-id:statabench --> | Statistical knowledge, tool selection and parameterization, plus open end-to-end modeling and reporting. | Connects closed statistical diagnostics and tool use with open-ended modeling projects in one coordinate system. |
| 2026-06-17 | Agent Memory | [GateMem](https://arxiv.org/abs/2606.18829) <!-- benchmark-id:gatemem --> | Utility, access control, and active forgetting in multi-principal shared memory. | Extends private single-user memory to shared memory with authorization and deletion obligations. |
| 2026-06-13 | Data Agent | [IRTS-ToolBench](https://arxiv.org/abs/2606.15107) <!-- benchmark-id:irts-toolbench --> | Tool-grounded QA over asynchronous, missing, variably sampled irregular time series. | Removes the regular-grid assumption and directly measures irregularity handling and grounded tool choice. |
| 2026-06-11 | RAG | [EvoBrowseComp](https://arxiv.org/abs/2606.13120) <!-- benchmark-id:evobrowsecomp --> | Broad English and Chinese web search over evolving knowledge. | Introduces an automatically refreshable bilingual live-web question-generation pipeline. |
| 2026-06-11 | RAG | [LoHoSearch](https://arxiv.org/abs/2606.12837) <!-- benchmark-id:lohosearch --> | Long-horizon search under large candidate spaces, complex constraints, and context-management pressure. | Controls search-space size and structural complexity through a knowledge graph rather than annotator intuition alone. |
| 2026-06 | Agent Memory | [LifeSide](https://arxiv.org/abs/2606.04660) <!-- benchmark-id:lifeside --> | Benchmarks lifelong digital companions through multi-session memory, user understanding, privacy control, and emotional-environment dynamics. | Connects memory to persistent user models, privacy boundaries, and emotional/environmental context. |
| 2026-05-28 | Agent Memory | [WorldMemArena](https://arxiv.org/abs/2605.29341) <!-- benchmark-id:worldmemarena --> | Writing, maintaining, retrieving, and using multimodal memory from actions, observations, and feedback. | Turns the memory lifecycle into four separately diagnosable stages instead of one end score. |
| 2026-05-27 | RAG | [LiveBrowseComp](https://arxiv.org/abs/2605.28721) <!-- benchmark-id:livebrowsecomp --> | Retrieval of recent low-salience web facts rather than verification of parametric knowledge. | Uses facts from the preceding 90 days plus closed-book and source-removal diagnostics. |
| 2026-05-19 | RAG | [ScholarQuest](https://arxiv.org/abs/2606.20235) <!-- benchmark-id:scholarquest --> | Intent-conditioned iterative paper retrieval, citation expansion, scope control, and set coverage. | Frames academic search as set retrieval with a shared large-scale backend, intent slices, and efficiency signals. |
| 2026-05-18 | Agent Memory | [EvoMemBench](https://arxiv.org/abs/2605.18421) <!-- benchmark-id:evomembench --> | Memory comparison across in-episode versus cross-episode scope and knowledge versus execution content. | Organizes heterogeneous QA, tool, search, and embodied tasks into one self-evolving-memory coordinate system. |
| 2026-05-14 | Agent Memory | [GroupMemBench](https://arxiv.org/abs/2605.14498) <!-- benchmark-id:groupmembench --> | Speaker-grounded beliefs, group dynamics, terminology, and audience adaptation in multi-party conversations. | Extends long-term memory from dyadic single-user dialogue to participant- and group-structured communication. |
| 2026-05-14 | Agent Memory | [MemEye](https://arxiv.org/abs/2605.15128) <!-- benchmark-id:memeye --> | Benchmarks visual-centric agent memory across fine-grained visual evidence and temporal visual-state synthesis while checking whether visual evidence is genuinely necessary. | Forces systems to retain genuinely necessary visual evidence rather than succeeding through text-only shortcuts or coarse captions. |
| 2026-05-14 | Agent Memory | [MEMLENS](https://arxiv.org/abs/2605.14906) <!-- benchmark-id:memlens --> | Multimodal extraction, updating, temporal reasoning, and abstention from 32K to 256K contexts. | Compares native long-context models and external-memory agents on one controlled visual-memory length axis. |
| 2026-05-12 | Agent Memory | [MedMemoryBench](https://arxiv.org/abs/2605.11814) <!-- benchmark-id:medmemorybench --> | Clinical-state tracking, temporal change, and memory saturation during streaming medical histories. | Moves from static history QA to evaluate-while-constructing assessment in a high-stakes longitudinal domain. |
| 2026-05-04 | Data Agent | [DataClawBench](https://arxiv.org/abs/2605.02503) <!-- benchmark-id:dataclawbench --> | Low-prior exploratory analysis over unfamiliar, noisy, cross-domain financial data with verifiable conclusions. | Turns source and schema discovery into measured abilities and uses milestones to distinguish useful progress from aimless exploration. |
| 2026-05 | Agent Memory | [LongMemEval-V2](https://arxiv.org/abs/2605.12493) <!-- benchmark-id:longmemeval-v2 --> | Evaluates whether memory systems internalize environment-specific experience from large web-agent trajectory histories. | Makes accumulated environment experience and workflow knowledge a memory target, not merely user-history recall. |
| 2026-05 | RAG | [SGR-Bench](https://arxiv.org/abs/2605.22219) <!-- benchmark-id:sgr-bench --> | Benchmarks search agents when answer-bearing evidence appears only after the agent establishes the correct site-specific retrieval state. | Separates finding the right source from configuring the right filters, hierarchy, scope, or view inside that source. |
| 2026-04-30 | RAG | [Bright-Pro](https://aclanthology.org/2026.acl-long.1705/) <!-- benchmark-id:bright-pro --> | Reasoning-intensive retrieval, aspect coverage, and retriever utility in static and agentic search. | Extends BRIGHT from narrow relevance ranking to multi-aspect evidence portfolios and retriever-in-the-loop utility. |
| 2026-04-19 | RAG | [MuDABench](https://aclanthology.org/2026.findings-acl.341/) <!-- benchmark-id:mudabench --> | Information extraction, cross-document aggregation, and quantitative analysis over large financial collections. | Scales multi-document QA to collection-wide analysis and adds intermediate-fact coverage as a process signal. |
| 2026-04-17 | Agent Memory | [MemEvoBench](https://arxiv.org/abs/2604.15774) <!-- benchmark-id:memevobench --> | Safety drift under repeated writes of misleading memories, noisy tool outputs, and biased feedback. | Extends memory safety from one-shot attacks to behavioral degradation across successive updates. |
| 2026-04-15 | RAG | [MERRIN](https://arxiv.org/abs/2604.13418) <!-- benchmark-id:merrin --> | Uncued modality selection, multimodal evidence retrieval, and multi-hop reasoning on the noisy web. | Adds image, video, audio, and chart evidence with conflicting and partially relevant web results. |
| 2026-04-14 | RAG | [EnterpriseRAG-Bench](https://arxiv.org/abs/2605.05253) <!-- benchmark-id:enterpriserag-bench --> | Enterprise retrieval, multi-document reasoning, conflict handling, completeness, and not-found behavior. | Adds a coherent nine-source enterprise corpus with controlled noise, duplicates, conflicts, and missing information. |
| 2026-04-09 | Agent Memory | [ImplicitMemBench](https://aclanthology.org/2026.acl-long.1301/) <!-- benchmark-id:implicitmembench --> | First-attempt procedural learning, priming, and conditioning after an interference phase. | Moves from asking what an agent recalls to observing what experience automatically changes in its behavior. |
| 2026-04-07 | RAG | [LeakDojo](https://aclanthology.org/2026.findings-acl.287/) <!-- benchmark-id:leakdojo --> | Extraction of RAG database content across attacks, models, pipelines, budgets, and defenses. | Adds a controlled security diagnostic for comparing knowledge-extraction attacks and mitigations across RAG configurations. |
| 2026-04-01 | RAG | [AutoResearchBench](https://arxiv.org/abs/2604.25256) <!-- benchmark-id:autoresearchbench --> | Target-paper tracing, constrained literature search, open-set collection, and stopping decisions. | Separates finding one target from exhaustively collecting an unknown-size paper set. |
| 2026-03-12 | Data Agent | [AgentFuel](https://arxiv.org/abs/2603.12483) <!-- benchmark-id:agentfuel --> | Domain-customized functional evaluation of conversational time-series agents, especially stateful and incident-specific queries. | Moves from generic static questions to evaluations tailored to domain state and incident context. |
| 2026-03-05 | Data Agent | [TML-Bench](https://arxiv.org/abs/2603.05764) <!-- benchmark-id:tml-bench --> | Reliable end-to-end tabular-ML submissions under fixed wall-clock budgets and hidden labels. | Extends one-shot code or score comparisons to time-performance scaling, submission success, and run-to-run stability. |
| 2026-03 | Data Agent | [Data Agent Benchmark (DAB)](https://arxiv.org/abs/2603.20576) <!-- benchmark-id:data-agent-benchmark --> | Evaluates enterprise data agents on questions requiring integration, transformation, and analysis across multiple heterogeneous database systems. | Targets the full enterprise data-question pipeline rather than isolated SQL generation or small in-context tables. |
| 2026-03 | Agent Memory | [LifeBench](https://arxiv.org/abs/2603.03781) <!-- benchmark-id:lifebench --> | Evaluates long-horizon multi-source memory spanning declarative and non-declarative information such as habits and procedures. | Expands memory beyond explicit facts to inferred habitual and procedural knowledge across heterogeneous traces. |
| 2026-02-27 | Data Agent | [DARE-bench](https://arxiv.org/abs/2602.24288) <!-- benchmark-id:dare-bench --> | Verifiable ML-model quality and fidelity to prescribed data-science instructions and processes. | Adds objective process adherence to outcome scoring instead of treating a good predictive score as sufficient. |
| 2026-02-26 | RAG | [MTRAG-UN](https://aclanthology.org/2026.findings-acl.503/) <!-- benchmark-id:mtrag-un --> | Multi-turn RAG handling of unanswerable, underspecified, non-standalone, and unclear turns. | Adds four explicit conversational failure modes to reusable retrieval and generation evaluation. |
| 2026-02-22 | RAG | [MC-Search](https://arxiv.org/abs/2603.00873) <!-- benchmark-id:mc-search --> | Multimodal search planning, modality choice, hop-level retrieval, and long-chain reasoning fidelity. | Adds structured multimodal search chains and process metrics beyond final-answer accuracy. |
| 2026-02-18 | Agent Memory | [MemoryArena](https://arxiv.org/abs/2602.16313) <!-- benchmark-id:memoryarena --> | Evaluates memory inside multi-session Memory-Agent-Environment loops where earlier actions and feedback must be distilled and used to guide later actions. | Directly couples long-term memorization with future action instead of evaluating recall and acting as separate abilities. |
| 2026-02-06 | RAG | [GISA](https://arxiv.org/abs/2602.08543) <!-- benchmark-id:gisa --> | Search planning, deep reasoning, broad aggregation, and structured answering for authentic information needs. | Combines human queries, stable and live subsets, deterministic scoring, and complete human search trajectories. |
| 2026-02-05 | RAG | [SAGE](https://arxiv.org/abs/2602.05975) <!-- benchmark-id:sage --> | Targeted and open-ended scientific literature retrieval for deep-research agents. | Separates exact-paper discovery from broad evidence collection and makes agent-retriever fit measurable. |
| 2026-02-03 | Agent Memory | [MemGUI-Bench](https://arxiv.org/abs/2602.06075) <!-- benchmark-id:memgui-bench --> | Cross-step retention, cross-app transfer, cross-session learning, and recovery in mobile GUI tasks. | Moves memory evaluation from conversational readout into executable mobile interaction and repeated-task learning. |
| 2026-02 | RAG | [AgenticRAGTracer](https://arxiv.org/abs/2602.19127) <!-- benchmark-id:agenticragtracer --> | Diagnoses multi-step agentic RAG by providing hop-aware intermediate validation rather than only final questions and answers. | Makes where a retrieval-reasoning chain fails observable at hop granularity. |
| 2026-02 | Agent Memory | [AMA-Bench](https://arxiv.org/abs/2602.22769) <!-- benchmark-id:ama-bench --> | Evaluates long-horizon memory over real and synthetic agent-environment trajectories rather than dialogue-only histories. | Moved agent memory from human-agent dialogue toward machine-generated agent-environment experience and causality. |
| 2026-02 | Agent Memory | [StructMemEval](https://arxiv.org/abs/2602.11243) <!-- benchmark-id:structmemeval --> | Tests whether agents organize memory into task-appropriate structures such as ledgers, lists, and trees rather than only retrieving facts. | Makes memory structure itself observable as a capability. |
<!-- TABLE-FIRST:RECENT:END -->

<a id="timeline"></a><a id="latest"></a><a id="frontier"></a>
## Accepted-item deep reads

This secondary layer retains v2 acceptance/provenance semantics. The table above is the primary research chronology by source release time.

<a id="entry-commercial-tax"></a>
<details><summary>2026-08-21 · The Commercial Tax · RAG / deployment validity <!-- timefirst:area=rag-deployment-validity --> — Rebinds a raw retrieval number to license, query format, index construction, and recurring cost. <!-- timefirst:delta=retrieval-number-to-deployment-envelope --></summary>

**Question.** Can a benchmark embedding score transfer to production under licensing, formatting, and cost constraints? <!-- timefirst:question=is-retrieval-performance-portable-to-deployment -->

**Evidence.** 13 embedders paired bootstrap, license provenance, and separated construction/query cost show that similar raw recall does not imply the same deployment meaning. <!-- timefirst:evidence=13-embedders-paired-bootstrap-license-cost~13-embedders-paired-bootstrap -->

**Caveat.** Uneven format tuning, hosted drift, and a single corpus limit portability across models, systems, and time. <!-- timefirst:caveat=uneven-format-tuning-hosted-drift-single-corpus~uneven-format-tuning-hosted-drift -->

**Map.** `reinforces`; this is an auditable evaluation change; one paper is only a signal, and durable map edits require independent support bound to one direction.

**Links.** [Paper](https://arxiv.org/abs/2608.16096) · [Code](https://github.com/Toryx-AI/commercial-tax-multihop-retrieval) · [Reproduction artifact](https://doi.org/10.5281/zenodo.21972866) · [Local deep note](benchmarks/commercial-tax.en.md)

</details>

<a id="entry-das-bench"></a>
<details><summary>2026-08-21 · DAS-Bench / DAS-Eval · RAG / academic-survey artifact <!-- timefirst:area=rag-academic-survey-artifact --> — Extends retrieval/drafting into a revisable protocol for literature, taxonomy, claims, citations, discourse, and rendered artifacts. <!-- timefirst:delta=answer-quality-to-publication-oriented-survey-protocol --></summary>

**Question.** Can a system assemble literature evidence into an auditable, readable, publication-oriented survey? <!-- timefirst:question=assemble-grounded-and-auditable-academic-surveys -->

**Evidence.** 30 topics 16 criteria combine deterministic citation checks with blinded expert comparison across evidence, taxonomy, claims, discourse, and artifact quality. <!-- timefirst:evidence=30-topics-16-criteria-expert-comparison~30-topics-16-criteria -->

**Caveat.** Generation backbone main judge coupling plus closed-system native configurations keep cross-system gaps at the system level. <!-- timefirst:caveat=generation-backbone-and-main-judge-coupling~generation-backbone-main-judge -->

**Map.** `early_signal`; this is an auditable evaluation change; one paper is only a signal, and durable map edits require independent support bound to one direction.

**Links.** [Paper](https://arxiv.org/abs/2608.18034) · [Benchmark and evaluator](https://github.com/ZhikaiXu24/DAS) · [Data](https://huggingface.co/datasets/ZhikaiXu24/DAS-Bench) · [Local deep note](benchmarks/das-bench.en.md)

</details>

<a id="entry-data-eng-bench"></a>
<details><summary>2026-08-21 · data-eng-bench · Data Agent / executable data engineering <!-- timefirst:area=data-agent-executable-data-engineering --> — Moves code generation into repository-scale dbt transformation with hidden row-level verification. <!-- timefirst:delta=code-generation-to-repository-scale-verified-transformation --></summary>

**Question.** Can an agent implement, execute, and repair data transformations under real project constraints? <!-- timefirst:question=implement-and-verify-production-shaped-dbt-work -->

**Evidence.** Across 103 dbt tasks hidden verifiers on DuckDB and Snowflake, hidden row-level verifiers inspect outputs; the August repair exposes evaluator reliability as a measurement condition. <!-- timefirst:evidence=103-dbt-tasks-hidden-row-level-verifiers~103-dbt-tasks-hidden-verifiers -->

**Caveat.** The Snowflake verifier without rerun means pre-fix leaderboard results are not directly comparable with the repaired environment. <!-- timefirst:caveat=snowflake-verifier-fix-without-rerun~snowflake-verifier-without-rerun -->

**Map.** `early_signal`; this is an auditable evaluation change; one paper is only a signal, and durable map edits require independent support bound to one direction.

**Links.** [Benchmark repository](https://github.com/Snowflake-Labs/data-eng-bench) · [Protocol fix](https://github.com/Snowflake-Labs/data-eng-bench/commit/35b83370bd9ae06d9ac8a2beb95d2544c90d88a5) · [Local deep note](benchmarks/data-eng-bench.en.md)

</details>

<a id="entry-maple"></a>
<details><summary>2026-08-21 · MAPLE · RAG / multi-aspect scientific retrieval <!-- timefirst:area=rag-multi-aspect-scientific-retrieval --> — Splits single-query relevance from consistent retrieval of one paper across motivation, method, and result aspects. <!-- timefirst:delta=single-query-relevance-to-cross-aspect-consistency --></summary>

**Question.** Can a retriever recover the same target paper across queries about different aspects? <!-- timefirst:question=retrieve-one-paper-across-multiple-aspects -->

**Evidence.** Across 2095 queries 210 papers, the matched single-query recall versus AllAspect gap shows how one-hit relevance hides cross-aspect failure. <!-- timefirst:evidence=2095-queries-210-papers-allaspect-gap~2095-queries-210-papers -->

**Caveat.** Generated queries single domain, and model-validated hard negatives can introduce style bias and label noise. <!-- timefirst:caveat=generated-queries-single-domain-and-label-noise~generated-queries-single-domain -->

**Map.** `reinforces`; this is an auditable evaluation change; one paper is only a signal, and durable map edits require independent support bound to one direction.

**Links.** [Paper](https://arxiv.org/abs/2608.15624) · [Code](https://github.com/Ggballs/MAPLE) · [Data](https://huggingface.co/datasets/kai-02/MAPLE) · [Local deep note](benchmarks/maple.en.md)

</details>

<a id="entry-memfusebench"></a>
<details><summary>2026-08-21 · MemFuseBench · Agent Memory / cross-source fusion <!-- timefirst:area=memory-cross-source-fusion --> — Moves from single-history recall to linking, causal fusion, conflict handling, and provenance across devices, users, and time. <!-- timefirst:delta=single-history-recall-to-multi-source-fusion --></summary>

**Question.** Can a system select, fuse, and arbitrate source-tagged memories without losing provenance? <!-- timefirst:question=link-fuse-and-arbitrate-source-tagged-memory -->

**Evidence.** The 357 questions 7823 events, and six diagnostics isolate linking, causal fusion, conflict handling, and provenance. <!-- timefirst:evidence=357-questions-7823-events-six-diagnostics~357-questions-7823-events -->

**Caveat.** Synthetic generation human ceiling evidence is absent; model-guided verification and do not establish external validity on real user histories. <!-- timefirst:caveat=synthetic-generation-without-human-ceiling~synthetic-generation-human-ceiling -->

**Map.** `early_signal`; this is an auditable evaluation change; one paper is only a signal, and durable map edits require independent support bound to one direction.

**Links.** [Paper](https://arxiv.org/abs/2608.18704) · [Data](https://github.com/Darwin-Agent/Mi-Memory/tree/master/MemFuse/MemFuseBench) · [Local deep note](benchmarks/memfusebench.en.md)

</details>

<a id="entry-past-bench"></a>
<details><summary>2026-08-21 · PAST-Bench · Agent Memory / cross-episode causal attribution <!-- timefirst:area=memory-cross-episode-causal-attribution --> — Moves from visible-history recall to whether persistence causally improves later executable tasks. <!-- timefirst:delta=visible-history-recall-to-persistent-state-attribution --></summary>

**Question.** After context clearing, does retained state actually cause better downstream task performance? <!-- timefirst:question=does-retained-state-cause-later-executable-benefit -->

**Evidence.** Across 26 families 204 episodes, persistence-on/off runs match seeds, prompts, and graders and retain artifact/trace evidence. <!-- timefirst:evidence=26-families-204-episodes-paired-persistence~26-families-204-episodes -->

**Caveat.** Generated tasks related graders can create model-family template familiarity, and the study does not cover months-long deployment. <!-- timefirst:caveat=generated-task-and-grader-coupling~generated-tasks-related-graders -->

**Map.** `early_signal`; this is an auditable evaluation change; one paper is only a signal, and durable map edits require independent support bound to one direction.

**Links.** [Paper](https://arxiv.org/abs/2608.04003) · [Code](https://github.com/Gen-Verse/PAST-Bench) · [Local deep note](benchmarks/past-bench.en.md)

</details>

<a id="entry-recall-trap"></a>
<details><summary>2026-08-21 · The Recall Trap · RAG / retrieval validity <!-- timefirst:area=rag-retrieval-validity --> — Audits the proxy assumption that higher recall is better using downstream executable outcomes. <!-- timefirst:delta=recall-proxy-to-downstream-causal-audit --></summary>

**Question.** Under fixed context slots, does higher file recall actually improve issue resolution? <!-- timefirst:question=does-higher-recall-improve-executable-resolution -->

**Evidence.** Paired fixed pack Docker evaluation shows that higher recall can coincide with a lower resolve rate for dense retrieval, with an open-weight replication. <!-- timefirst:evidence=paired-fixed-pack-official-docker-grading~paired-fixed-pack-docker -->

**Caveat.** The compound dedup fixed slots treatment changes breadth, depth, rank, position, tokens, and distractors together; the causal result is limited to fixed slots. <!-- timefirst:caveat=compound-dedup-treatment-under-fixed-slots~compound-dedup-fixed-slots -->

**Map.** `reinforces`; this is an auditable evaluation change; one paper is only a signal, and durable map edits require independent support bound to one direction.

**Links.** [Paper](https://arxiv.org/abs/2608.14838) · [Reproduction artifact](https://doi.org/10.5281/zenodo.21879550) · [Local deep note](benchmarks/recall-trap.en.md)

</details>

<a id="entry-sp-mem"></a>
<details><summary>2026-08-21 · SP-Mem Privacy-Aware Memory Benchmark · Agent Memory / lifecycle privacy <!-- timefirst:area=memory-lifecycle-privacy --> — Places memory utility, consent, authorization, exact-value exposure, and cost in one protocol. <!-- timefirst:delta=memory-utility-to-consent-aware-privacy-tradeoff --></summary>

**Question.** Can personalized memory be used only when necessary and authorized without exposing private values? <!-- timefirst:question=balance-personalization-authorization-and-exposure -->

**Evidence.** Matched modes over 1000 profiles 5400 queries, and four domains score response quality, authorization requests, and exact-value exposure together. <!-- timefirst:evidence=1000-profiles-5400-queries-four-domains~1000-profiles-5400-queries -->

**Caveat.** An explicit consent exact string proxy omits inference, re-identification, and adversarial multi-turn disclosure. <!-- timefirst:caveat=explicit-consent-and-exact-string-proxy~explicit-consent-exact-string -->

**Map.** `early_signal`; this is an auditable evaluation change; one paper is only a signal, and durable map edits require independent support bound to one direction.

**Links.** [Paper](https://arxiv.org/abs/2608.16551) · [Code and data](https://github.com/Jensassss/SP-Mem) · [Local deep note](benchmarks/sp-mem.en.md)

</details>

<a id="entry-visdocagentbench"></a>
<details><summary>2026-08-21 · VisDocAgentBench · RAG / agentic visual-document retrieval <!-- timefirst:area=rag-agentic-visual-document-retrieval --> — Compares static rankers with search/inspection agents under the same ranked-page output. <!-- timefirst:delta=static-page-ranking-to-iterative-discovery-and-inspection --></summary>

**Question.** Can an agent use search, visual inspection, and OCR to place distributed evidence pages in the top 10? <!-- timefirst:question=rank-visual-pages-through-search-and-inspection -->

**Evidence.** Across 2375 pages 120 queries, a shared top-10 contract plus support interventions and ablations makes discovery and inspection visible. <!-- timefirst:evidence=2375-pages-120-queries-shared-top10-contract~2375-pages-120-queries -->

**Caveat.** The 120 queries, six cross-document paths, and unmatched agent routes limit causal attribution to a planner or vision component. <!-- timefirst:caveat=small-query-set-and-unmatched-agent-routes~120-queries-six-cross-document -->

**Map.** `reinforces`; this is an auditable evaluation change; one paper is only a signal, and durable map edits require independent support bound to one direction.

**Links.** [Paper](https://arxiv.org/abs/2608.17889) · [Code](https://github.com/hulx2002/VisDocAgentBench) · [Data](https://huggingface.co/datasets/hulx2002/VisDocAgentBench) · [Local deep note](benchmarks/visdocagentbench.en.md)

</details>

<a id="entry-wandr"></a>
<details><summary>2026-08-21 · WANDR · RAG / live wide-and-deep search <!-- timefirst:area=rag-wide-deep-live-web --> — Extends answer search to open-set discovery, hierarchical enrichment, and record-level refetch verification. <!-- timefirst:delta=answer-search-to-open-set-record-collection --></summary>

**Question.** Can an agent discover, enrich, and verify live-web records without knowing the complete set? <!-- timefirst:question=discover-enrich-and-verify-live-web-records -->

**Evidence.** 500 Harbor task packages use required-volume denominators and URL/excerpt refetch to expose losses in discovery, support, and enrichment. <!-- timefirst:evidence=500-harbor-packages-record-refetch-verification~500-harbor-task-packages -->

**Caveat.** Unmatched stacks shared fetch, web drift, and an LLM judge make the results system-level evidence only. <!-- timefirst:caveat=unmatched-stacks-shared-fetch-and-web-drift~unmatched-stacks-shared-fetch -->

**Map.** `reinforces`; this is an auditable evaluation change; one paper is only a signal, and durable map edits require independent support bound to one direction.

**Links.** [Paper](https://arxiv.org/abs/2608.14747) · [Benchmark](https://github.com/perplexityai/wandr) · [Local deep note](benchmarks/wandr.en.md)

</details>

<a id="entry-dsagentbench"></a>
<details><summary>2026-08 · DSAgentBench · Data Agent / end-to-end data science in real computers <!-- timefirst:area=data-agent-real-computer-workflow --> — Moves evaluation from isolated code/answer stages to complete multi-tool workflows grounded in intermediate outputs. <!-- timefirst:delta=isolated-stages-to-end-to-end-workflow --></summary>

**Question.** Can an agent complete data-science work across wrangling, modeling, visualization, and validation in a real computer environment? <!-- timefirst:question=end-to-end-data-science-execution -->

**Evidence.** Its 275 tasks use deterministic checks for analytical correctness, visual outputs, and model performance; the paper reports 56.70% for the strongest agent and below 1% for open-source agents. <!-- timefirst:evidence=275-tasks-deterministic-evaluation-56.70~analytical-correctness-visual-outputs -->

**Caveat.** Model, harness, tool reliability, OS grounding, and recovery change together, so the result is system-level evidence rather than an isolated planner effect. <!-- timefirst:caveat=system-level-harness-confounding~model-harness-tool-reliability -->

**Map.** `early_signal`; the new coordinate is real-computer environment + protocol, and one record does not rewrite the durable map.

**Links.** [Paper](https://arxiv.org/abs/2608.10366) · [Local deep note](benchmarks/dsagentbench.en.md)

</details>

<a id="entry-vakra"></a>
<details><summary>2026-08 · VAKRA · RAG / cross-source executable coherence <!-- timefirst:area=rag-cross-source-executable-coherence --> — Places APIs, document retrieval, multi-hop reasoning, and policy constraints in one re-executable trajectory. <!-- timefirst:delta=apis-retrieval-policy-one-trajectory --></summary>

**Question.** Can an agent preserve identity, grounding, and policy consistency across structured APIs and unstructured documents? <!-- timefirst:question=cross-source-identity-grounding-policy -->

**Evidence.** VAKRA exposes 8,000+ locally hosted executable APIs across 62 domains and re-executes predicted tool calls; compositional and policy-constrained settings are substantially harder than single-hop endpoint tasks. <!-- timefirst:evidence=8000-apis-62-domains-composition-gap~predicted-tool-calls -->

**Caveat.** A fixed ReAct harness improves model comparability but binds conclusions to one interface/controller contract and does not compare alternative agent architectures. <!-- timefirst:caveat=fixed-react-harness-binding~interface-controller-contract -->

**Map.** `early_signal`; cross-source executable coherence gains a coordinate without yet constituting independent trend evidence.

**Links.** [Paper](https://arxiv.org/abs/2608.12282) · [Local deep note](benchmarks/vakra.en.md)

</details>

<a id="entry-dataspace"></a>
<details><summary>2026-08 · DataSpace · Data Agent / heterogeneous-workspace analytics <!-- timefirst:area=data-agent-heterogeneous-workspace-analytics --> — Couples evidence discovery, cross-source computation, and deterministic complete-result verification in one evaluation object. <!-- timefirst:delta=discovery-computation-deterministic-verification --></summary>

**Question.** Given only a question and task-local workspace, can an agent find evidence across databases, files, documents, and multimedia and return the complete table? <!-- timefirst:question=heterogeneous-evidence-to-complete-table -->

**Evidence.** Its 410 tasks span 7,439 artifacts; the paper reports a 15.36-point harness spread with the backbone fixed, a harness sensitivity spread that directly exposes system-level sensitivity. <!-- timefirst:evidence=410-tasks-7439-artifacts-15.36-harness-gap~harness-sensitivity-spread -->

**Caveat.** Frozen task-local workspaces omit enterprise drift, permissions, writes, business-definition ambiguity, and persistent project state. <!-- timefirst:caveat=frozen-workspace-omits-enterprise-state~enterprise-drift-permissions-writes -->

**Map.** `early_signal`; heterogeneous evidence plus deterministic verification is a new joint coordinate, while harness effects prevent component attribution.

**Links.** [Paper](https://arxiv.org/abs/2608.03451) · [Local deep note](benchmarks/dataspace.en.md)

</details>

<a id="entry-locomo-plus"></a>
<details><summary>2026-07 · LoCoMo-Plus · Agent Memory / latent user constraints <!-- timefirst:area=memory-latent-user-constraints --> — Moves the target from retrieving stated facts to applying remembered user state when the later query supplies no direct cue. <!-- timefirst:delta=explicit-recall-to-implicit-state-application --></summary>

**Question.** When a later query does not restate an old constraint, can latent user state still constrain the current response correctly? <!-- timefirst:question=cue-disconnected-constraint-application -->

**Evidence.** The benchmark uses cue–trigger semantic disconnect and constraint consistency to distinguish explicit recall from application of implicit state. <!-- timefirst:evidence=cue-trigger-disconnect-constraint-consistency~cue-trigger-semantic-disconnect -->

**Caveat.** Constraint construction and evaluation are load-bearing, and the current conversational response evaluation does not cover preference drift or irreversible action. <!-- timefirst:caveat=evaluator-construction-and-no-actions~conversational-response-evaluation -->

**Map.** `early_signal`; it links factual recall to future memory-guided action without independently rewriting the longitudinal-causality map.

**Links.** [ACL paper](https://aclanthology.org/2026.acl-long.1150/) · [Local deep note](benchmarks/locomo-plus.en.md)

</details>

<a id="entry-mem2actbench"></a>
<details><summary>2026-07 · Mem2ActBench · Agent Memory / memory-guided tool action <!-- timefirst:area=memory-guided-tool-action --> — Directly tests whether memory changes tool selection and parameter grounding rather than only helping answer questions. <!-- timefirst:delta=answers-to-tool-selection-and-parameters --></summary>

**Question.** Is long-term memory proactively used to choose tools and ground action parameters? <!-- timefirst:question=proactive-memory-use-in-tool-actions -->

**Evidence.** The evaluation places memory utilization in tool-based assistant actions, making action-level effects more direct than inference from answers about past context. <!-- timefirst:evidence=action-level-memory-utilization~tool-based-assistant -->

**Caveat.** Tool-call tasks remain narrower than long-horizon environments where actions change persistent state and mistakes have downstream consequences, creating a persistent state consequence risk beyond the core protocol. <!-- timefirst:caveat=tool-calls-omit-persistent-consequences~persistent-state-consequence-risk -->

**Map.** `early_signal`; it adds an action coordinate, but a single work cannot establish a durable trend.

**Links.** [ACL paper](https://aclanthology.org/2026.acl-long.370/)

</details>

<a id="entry-agenticdatabench"></a>
<details><summary>2026-07 · AgenticDataBench · Data Agent / data-science skill coverage <!-- timefirst:area=data-agent-skill-coverage --> — Uses a fine-grained skill taxonomy to make benchmark coverage auditable below aggregate success. <!-- timefirst:delta=aggregate-score-to-auditable-skill-coverage --></summary>

**Question.** Which realistic data-science skills does an evaluation cover, and which does it omit? <!-- timefirst:question=covered-and-missing-data-science-skills -->

**Evidence.** The benchmark organizes workflows with a skill taxonomy so capability coverage can be diagnosed as a skill taxonomy coverage audit beneath the system's total score. <!-- timefirst:evidence=skill-taxonomy-below-aggregate-score~skill-taxonomy-coverage-audit -->

**Caveat.** Skill taxonomies and generated tasks may omit organization-specific semantics, evolving data, and governance constraints. <!-- timefirst:caveat=taxonomy-omits-org-semantics-and-drift~organization-specific-semantics -->

**Map.** `early_signal`; coverage audit is a new diagnostic coordinate, not evidence of reliable delivery in real workflows.

**Links.** [Paper](https://arxiv.org/abs/2607.01647)

</details>

<a id="entry-sgr-bench"></a>
<details><summary>2026-05 · SGR-Bench · RAG / state-gated retrieval <!-- timefirst:area=rag-state-gated-retrieval --> — Separates finding the right source from configuring its filters, hierarchy, scope, and site state correctly. <!-- timefirst:delta=source-finding-to-environment-configuration --></summary>

**Question.** When answer-bearing evidence appears only in the correct site-specific retrieval state, can a search agent establish that state? <!-- timefirst:question=establish-site-specific-retrieval-state -->

**Evidence.** The protocol makes filters, hierarchy, scope, or view settings prerequisites for evidence access, exposing control failures after source discovery. <!-- timefirst:evidence=filters-hierarchy-scope-as-access-gates~filters-hierarchy-scope -->

**Caveat.** State-gated retrieval is narrower than general web research, document RAG, or arbitrary tool orchestration and cannot represent the whole field. <!-- timefirst:caveat=narrower-than-general-agentic-retrieval~state-gated-retrieval -->

**Map.** `early_signal`; it adds an information-environment configuration coordinate without independent evidence for a durable map promotion.

**Links.** [Paper](https://arxiv.org/abs/2605.22219)

</details>

<a id="entry-realmem"></a>
<details><summary>2026-01 · RealMem · Agent Memory / persistent project state <!-- timefirst:area=memory-persistent-project-state --> — Extends long-term memory from casual dialogue to cross-session project work with evolving goals, artifacts, and relevant state. <!-- timefirst:delta=casual-dialogue-to-cross-session-project-work --></summary>

**Question.** Can an agent preserve the right evolving goals, artifacts, and state across long-running project-oriented interactions? <!-- timefirst:question=preserve-evolving-goals-artifacts-state -->

**Evidence.** The evaluation puts cross-session memory into project-oriented interaction, making persistent task state rather than casual conversation measurable. <!-- timefirst:evidence=project-oriented-cross-session-evaluation~project-oriented-interaction -->

**Caveat.** Synthetic multi-agent trajectory generation and dialogue-only interaction abstract away real collaborative writes, permissions, and tooling. <!-- timefirst:caveat=synthetic-dialogue-omits-real-collaboration~collaborative-writes-permissions -->

**Map.** `early_signal`; persistent project state is a frontier coordinate without longitudinal causal attribution.

**Links.** [ACL Findings paper](https://aclanthology.org/2026.findings-acl.703/)

</details>

<a id="periods"></a><a id="changes"></a>
## 7 days / 30 days: What Changed in the Evaluation Object

<a id="last-7-days"></a>
### Last 7 days: 2026-08-15—2026-08-21

- **`reinforced` · structured evidence coverage: evaluation is moving from single-hit relevance to structured coverage across aspects, paths, and hierarchies.** <!-- timefirst:direction key="structured-evidence-coverage" state="reinforced" supports="maple,visdocagentbench,wandr" confidence="high" implication="measure-coverage-not-only-single-hit-relevance" timing="radar_published_at" synthesized="2026-08-21T00:48:57Z" prior="field-map" -->
  Supports: [MAPLE](#entry-maple) · [VisDocAgentBench](#entry-visdocagentbench) · [WANDR](#entry-wandr); confidence: **high**; timing basis: `radar_published_at`; prior map evidence: [RAG Field Map](#field-map). Research-design implication (measure coverage not only single hit relevance): report aspect/set/path coverage and discovery loss instead of letting one hit stand in for complete evidence acquisition. Exact synthesis time: `2026-08-21T00:48:57Z` (UTC).

- **`reinforced` · retrieval harness validity: retrieval scores must be bound to packing, format, license, cost, and downstream execution envelope.** <!-- timefirst:direction key="retrieval-harness-validity" state="reinforced" supports="commercial-tax,recall-trap" confidence="high" implication="bind-retrieval-scores-to-harness-and-deployment" timing="radar_published_at" synthesized="2026-08-21T00:48:57Z" prior="field-map" -->
  Supports: [The Commercial Tax](#entry-commercial-tax) · [The Recall Trap](#entry-recall-trap); confidence: **high**; timing basis: `radar_published_at`; prior map evidence: [RAG Field Map](#field-map). Research-design implication (bind retrieval scores to harness and deployment): matching the model is insufficient; packing, query format, index, licensing, and cost must be fixed, and recall proxies checked against downstream outcomes. Exact synthesis time: `2026-08-21T00:48:57Z` (UTC).

- **`new_signal` · memory lifecycle privacy: memory evaluation is starting to measure personalization, authorization, and exposure in one lifecycle.** <!-- timefirst:direction key="memory-lifecycle-privacy" state="new_signal" supports="sp-mem" confidence="medium" implication="score-memory-utility-with-authorization-and-exposure" timing="radar_published_at" synthesized="2026-08-21T00:48:57Z" prior="none" -->
  Supports: [SP-Mem Privacy-Aware Memory Benchmark](#entry-sp-mem); confidence: **medium**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (score memory utility with authorization and exposure): report usefulness separately from necessity, authorization requests, and leakage; one work is only an early signal. Exact synthesis time: `2026-08-21T00:48:57Z` (UTC).

- **`new_signal` · executable verifier reliability: an executable Data Agent benchmark must version its evaluator and backend reliability.** <!-- timefirst:direction key="executable-verifier-reliability" state="new_signal" supports="data-eng-bench" confidence="high" implication="version-verifiers-and-rerun-after-protocol-fixes" timing="radar_published_at" synthesized="2026-08-21T00:48:57Z" prior="none" -->
  Supports: [data-eng-bench](#entry-data-eng-bench); confidence: **high**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (version verifiers and rerun after protocol fixes): rerun after evaluator or environment repairs; old scores cannot silently carry into a new protocol. Exact synthesis time: `2026-08-21T00:48:57Z` (UTC).

<a id="last-30-days"></a>
### Last 30 days: 2026-07-23—2026-08-21

- **`reinforced` · structured evidence coverage: evaluation is moving from single-hit relevance to structured coverage across aspects, paths, and hierarchies.** <!-- timefirst:direction key="structured-evidence-coverage" state="reinforced" supports="maple,visdocagentbench,wandr" confidence="high" implication="measure-coverage-not-only-single-hit-relevance" timing="radar_published_at" synthesized="2026-08-21T00:48:57Z" prior="field-map" -->
  Supports: [MAPLE](#entry-maple) · [VisDocAgentBench](#entry-visdocagentbench) · [WANDR](#entry-wandr); confidence: **high**; timing basis: `radar_published_at`; prior map evidence: [RAG Field Map](#field-map). Research-design implication (measure coverage not only single hit relevance): report aspect/set/path coverage and discovery loss instead of letting one hit stand in for complete evidence acquisition. Exact synthesis time: `2026-08-21T00:48:57Z` (UTC).

- **`reinforced` · retrieval harness validity: retrieval scores must be bound to packing, format, license, cost, and downstream execution envelope.** <!-- timefirst:direction key="retrieval-harness-validity" state="reinforced" supports="commercial-tax,recall-trap" confidence="high" implication="bind-retrieval-scores-to-harness-and-deployment" timing="radar_published_at" synthesized="2026-08-21T00:48:57Z" prior="field-map" -->
  Supports: [The Commercial Tax](#entry-commercial-tax) · [The Recall Trap](#entry-recall-trap); confidence: **high**; timing basis: `radar_published_at`; prior map evidence: [RAG Field Map](#field-map). Research-design implication (bind retrieval scores to harness and deployment): matching the model is insufficient; packing, query format, index, licensing, and cost must be fixed, and recall proxies checked against downstream outcomes. Exact synthesis time: `2026-08-21T00:48:57Z` (UTC).

- **`new_signal` · memory lifecycle privacy: memory evaluation is starting to measure personalization, authorization, and exposure in one lifecycle.** <!-- timefirst:direction key="memory-lifecycle-privacy" state="new_signal" supports="sp-mem" confidence="medium" implication="score-memory-utility-with-authorization-and-exposure" timing="radar_published_at" synthesized="2026-08-21T00:48:57Z" prior="none" -->
  Supports: [SP-Mem Privacy-Aware Memory Benchmark](#entry-sp-mem); confidence: **medium**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (score memory utility with authorization and exposure): report usefulness separately from necessity, authorization requests, and leakage; one work is only an early signal. Exact synthesis time: `2026-08-21T00:48:57Z` (UTC).

- **`new_signal` · executable verifier reliability: an executable Data Agent benchmark must version its evaluator and backend reliability.** <!-- timefirst:direction key="executable-verifier-reliability" state="new_signal" supports="data-eng-bench" confidence="high" implication="version-verifiers-and-rerun-after-protocol-fixes" timing="radar_published_at" synthesized="2026-08-21T00:48:57Z" prior="none" -->
  Supports: [data-eng-bench](#entry-data-eng-bench); confidence: **high**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (version verifiers and rerun after protocol fixes): rerun after evaluator or environment repairs; old scores cannot silently carry into a new protocol. Exact synthesis time: `2026-08-21T00:48:57Z` (UTC).

<a id="evolution"></a>
## Three Areas

| Area | Broad shift | Current question | Topic radar |
|---|---|---|---|
| **Agent Memory** | multi-session recall → update/forget/structure → multimodality and action → implicit user state, shared governance, and safety | What was written, who may access it, when should it change or be deleted, and does it alter later action? | [Agent Memory Radar](https://github.com/H20Zhang/Agent-Memory-Radar#field-map) |
| **RAG / Agentic Retrieval** | document ranking → robustness and faithfulness → deep research and evidence portfolios → live search, cross-source execution, and trace auditing | Can the agent assemble complete evidence under changing pages, sources, tools, and budgets—and explain where it failed? | [Agentic RAG Radar](https://github.com/H20Zhang/Agentic-RAG-Radar#field-map) |
| **Data Agents** | NL→SQL/code → experimentation and workflows → exploration, statistics, and causal analysis → end-to-end reliability in real environments | Can the agent understand data before analyzing it, then clarify, abstain, or refuse when meaning or evidence is insufficient? | [Data Agent Radar](https://github.com/H20Zhang/Data-Agent-Radar#field-map) |

<a id="field-map"></a>
## Benchmark Map

<a id="benchmark-memory"></a>
### Agent Memory
From cross-session factual recall toward online updating, structured memory, multimodal evidence, action, authority, and implicit user state.

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

<a id="all-benchmarks"></a>
## All Benchmarks by Area

All 105 benchmarks in the registry remain directly scannable here. The Library is an alternate canonical browse surface, not a reason to remove these tables from README.

### Agent Memory

<!-- TABLE-FIRST:AREA:agent-memory:START -->
| Role | Benchmark | Released | What it evaluates | Why it changed the question |
|---|---|---:|---|---|
| 🌱 Precursor | [Beyond Goldfish Memory](https://aclanthology.org/2022.acl-long.356/) <!-- benchmark-id:beyond-goldfish-memory --> | 2022-05 | Benchmarks long-term open-domain conversation across multiple human-human chat sessions where partners must remember and remain consistent with prior interactions. | Established cross-session conversation as a distinct long-term-memory setting before modern memory-agent benchmarks. |
| 🧱 Foundation | [LoCoMo](https://aclanthology.org/2024.acl-long.747/) <!-- benchmark-id:locomo --> | 2024-08 | Long-horizon conversational-memory benchmark spanning QA, event summarization, and multimodal dialogue generation over very long multi-session conversations. | Established very-long-term conversational memory as a first-class evaluation target rather than a short-context dialogue property. |
| 🧱 Foundation | [LongMemEval](https://arxiv.org/abs/2410.10813) <!-- benchmark-id:longmemeval --> | 2024-10 | Evaluates sustained chat-assistant memory across extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention. | Made update, temporal reasoning, and abstention explicit instead of collapsing long-term memory into factual recall. |
| ↗ Transition | [MemBench](https://arxiv.org/abs/2506.21605) <!-- benchmark-id:membench --> | 2025-06 | Broadens memory evaluation across factual and reflective memory, participation and observation scenarios, and effectiveness, efficiency, and capacity. | Expanded evaluation from answer accuracy toward different memory levels, interaction roles, efficiency, and capacity. |
| ↗ Transition | [MemoryAgentBench](https://arxiv.org/abs/2507.05257) <!-- benchmark-id:memoryagentbench --> | 2025-07 | Evaluates memory agents under incremental multi-turn interaction across retrieval, test-time learning, long-range understanding, and selective forgetting. | Shifted the object from a static long context to a memory agent that must incrementally absorb, update, use, and forget information. |
| ↗ Transition | [BEAM](https://arxiv.org/abs/2510.27246) <!-- benchmark-id:beam --> | 2025-10 | Tests long-term memory on coherent conversations extending from million-token to multi-million-token horizons. | Made memory degradation with truly massive, coherent histories directly measurable. |
| 🔭 Frontier | [RealMem](https://aclanthology.org/2026.findings-acl.703/) <!-- benchmark-id:realmem --> | 2026-01 | Evaluates long-term memory over project-oriented cross-session interactions whose goals, artifacts, and relevant state evolve over time. | Moves long-term-memory evaluation from casual conversation toward persistent project state and evolving user goals. |
| 🔭 Frontier | [CAME-Bench](https://aclanthology.org/2026.findings-acl.584/) <!-- benchmark-id:came-bench --> | 2026-01-15 | Intent-compatible retrieval when the same entities recur under different goals. | Makes contextual interference and goal-mismatched retrieval explicit in long trajectories. |
| 🔭 Frontier | [AMA-Bench](https://arxiv.org/abs/2602.22769) <!-- benchmark-id:ama-bench --> | 2026-02 | Evaluates long-horizon memory over real and synthetic agent-environment trajectories rather than dialogue-only histories. | Moved agent memory from human-agent dialogue toward machine-generated agent-environment experience and causality. |
| 🔭 Frontier | [StructMemEval](https://arxiv.org/abs/2602.11243) <!-- benchmark-id:structmemeval --> | 2026-02 | Tests whether agents organize memory into task-appropriate structures such as ledgers, lists, and trees rather than only retrieving facts. | Makes memory structure itself observable as a capability. |
| 🔭 Frontier | [MemGUI-Bench](https://arxiv.org/abs/2602.06075) <!-- benchmark-id:memgui-bench --> | 2026-02-03 | Cross-step retention, cross-app transfer, cross-session learning, and recovery in mobile GUI tasks. | Moves memory evaluation from conversational readout into executable mobile interaction and repeated-task learning. |
| 🔭 Frontier | [MemoryArena](https://arxiv.org/abs/2602.16313) <!-- benchmark-id:memoryarena --> | 2026-02-18 | Evaluates memory inside multi-session Memory-Agent-Environment loops where earlier actions and feedback must be distilled and used to guide later actions. | Directly couples long-term memorization with future action instead of evaluating recall and acting as separate abilities. |
| 🔭 Frontier | [LifeBench](https://arxiv.org/abs/2603.03781) <!-- benchmark-id:lifebench --> | 2026-03 | Evaluates long-horizon multi-source memory spanning declarative and non-declarative information such as habits and procedures. | Expands memory beyond explicit facts to inferred habitual and procedural knowledge across heterogeneous traces. |
| 🔭 Frontier | [ImplicitMemBench](https://aclanthology.org/2026.acl-long.1301/) <!-- benchmark-id:implicitmembench --> | 2026-04-09 | First-attempt procedural learning, priming, and conditioning after an interference phase. | Moves from asking what an agent recalls to observing what experience automatically changes in its behavior. |
| 🔭 Frontier | [MemEvoBench](https://arxiv.org/abs/2604.15774) <!-- benchmark-id:memevobench --> | 2026-04-17 | Safety drift under repeated writes of misleading memories, noisy tool outputs, and biased feedback. | Extends memory safety from one-shot attacks to behavioral degradation across successive updates. |
| 🔭 Frontier | [LongMemEval-V2](https://arxiv.org/abs/2605.12493) <!-- benchmark-id:longmemeval-v2 --> | 2026-05 | Evaluates whether memory systems internalize environment-specific experience from large web-agent trajectory histories. | Makes accumulated environment experience and workflow knowledge a memory target, not merely user-history recall. |
| 🔭 Frontier | [MedMemoryBench](https://arxiv.org/abs/2605.11814) <!-- benchmark-id:medmemorybench --> | 2026-05-12 | Clinical-state tracking, temporal change, and memory saturation during streaming medical histories. | Moves from static history QA to evaluate-while-constructing assessment in a high-stakes longitudinal domain. |
| 🔭 Frontier | [GroupMemBench](https://arxiv.org/abs/2605.14498) <!-- benchmark-id:groupmembench --> | 2026-05-14 | Speaker-grounded beliefs, group dynamics, terminology, and audience adaptation in multi-party conversations. | Extends long-term memory from dyadic single-user dialogue to participant- and group-structured communication. |
| 🔭 Frontier | [MemEye](https://arxiv.org/abs/2605.15128) <!-- benchmark-id:memeye --> | 2026-05-14 | Benchmarks visual-centric agent memory across fine-grained visual evidence and temporal visual-state synthesis while checking whether visual evidence is genuinely necessary. | Forces systems to retain genuinely necessary visual evidence rather than succeeding through text-only shortcuts or coarse captions. |
| 🔭 Frontier | [MEMLENS](https://arxiv.org/abs/2605.14906) <!-- benchmark-id:memlens --> | 2026-05-14 | Multimodal extraction, updating, temporal reasoning, and abstention from 32K to 256K contexts. | Compares native long-context models and external-memory agents on one controlled visual-memory length axis. |
| 🔭 Frontier | [EvoMemBench](https://arxiv.org/abs/2605.18421) <!-- benchmark-id:evomembench --> | 2026-05-18 | Memory comparison across in-episode versus cross-episode scope and knowledge versus execution content. | Organizes heterogeneous QA, tool, search, and embodied tasks into one self-evolving-memory coordinate system. |
| 🔭 Frontier | [WorldMemArena](https://arxiv.org/abs/2605.29341) <!-- benchmark-id:worldmemarena --> | 2026-05-28 | Writing, maintaining, retrieving, and using multimodal memory from actions, observations, and feedback. | Turns the memory lifecycle into four separately diagnosable stages instead of one end score. |
| 🔭 Frontier | [LifeSide](https://arxiv.org/abs/2606.04660) <!-- benchmark-id:lifeside --> | 2026-06 | Benchmarks lifelong digital companions through multi-session memory, user understanding, privacy control, and emotional-environment dynamics. | Connects memory to persistent user models, privacy boundaries, and emotional/environmental context. |
| 🔭 Frontier | [GateMem](https://arxiv.org/abs/2606.18829) <!-- benchmark-id:gatemem --> | 2026-06-17 | Utility, access control, and active forgetting in multi-principal shared memory. | Extends private single-user memory to shared memory with authorization and deletion obligations. |
| 🔭 Frontier | [DynamicMem](https://arxiv.org/abs/2606.22877) <!-- benchmark-id:dynamicmem --> | 2026-06-22 | Inference and updating of user attributes, habits, and preferences from fifteen months of multi-app behavior. | Moves user memory to multi-million-token histories, long-term drift, and implicit evidence distributed across applications. |
| 🔭 Frontier | [MEMPROBE](https://arxiv.org/abs/2606.24595) <!-- benchmark-id:memprobe --> | 2026-06-23 | Recovery of hidden user state from the memory artifact left after ordinary assistance. | Moves from indirect downstream behavior to direct auditing of the stored memory artifact. |
| 🔭 Frontier | [LoCoMo-Plus](https://aclanthology.org/2026.acl-long.1150/) <!-- benchmark-id:locomo-plus --> | 2026-07 | Evaluates cognitive memory where agents must retain and apply latent user constraints even when later cues are semantically disconnected. | Moves the target from remembering explicit facts to applying latent user state, goals, and values when the cue no longer restates them. |
| 🔭 Frontier | [Mem-Gallery](https://aclanthology.org/2026.acl-long.1892/) <!-- benchmark-id:mem-gallery --> | 2026-07 | Evaluates multimodal long-term conversational memory across extraction and test-time adaptation, reasoning, and memory knowledge management. | Makes visual retention, multimodal reasoning, and memory organization first-class long-term-memory evaluation targets. |
| 🔭 Frontier | [Mem2ActBench](https://aclanthology.org/2026.acl-long.370/) <!-- benchmark-id:mem2actbench --> | 2026-07 | Evaluates whether long-term memory is proactively used for tool selection and parameter grounding during tool-based assistant actions. | Makes action-level memory utilization directly measurable instead of reading memory quality only through answers about past context. |
| 🔭 Frontier | [PerMemSafe](https://aclanthology.org/2026.findings-acl.320/) <!-- benchmark-id:permemsafe --> | 2026-07 | Recognition and updating of implicit personalized risk across long, noise-heavy histories. | Extends user-state memory to evolving personalized safety while retaining helpfulness. |
| 🔭 Frontier | [MemFuseBench](https://arxiv.org/abs/2608.18704) <!-- benchmark-id:memfusebench --> | 2026-07-21 | Cross-source memory benchmark for linking, causal fusion, conflict arbitration, and provenance over heterogeneous event streams. | Separates linking, causal fusion, conflict handling, and provenance across heterogeneous sources. |
| 🔭 Frontier | [InMind](https://arxiv.org/abs/2607.24368) <!-- benchmark-id:inmind --> | 2026-07-27 | Retrieval and use of a personal fact whose relevance to the query depends on world knowledge. | Paired controls separate storage, knowledge, routing, and final-use failures. |
| 🔭 Frontier | [PAST-Bench](https://arxiv.org/abs/2608.04003) <!-- benchmark-id:past-bench --> | 2026-08-04 | Paired persistent-state benchmark that tests whether retained cross-episode experience causally improves later executable work. | Uses persistence-on/off controls to attribute executable cross-episode benefit to retained state. |
| 🔭 Frontier | [SP-Mem Privacy-Aware Memory Benchmark](https://arxiv.org/abs/2608.16551) <!-- benchmark-id:sp-mem --> | 2026-08-17 | Privacy-aware memory benchmark that jointly measures response quality, personalization, consent handling, exact-value exposure, and cost. | Places personalization benefit, authorization, and leakage risk in one memory-lifecycle protocol. |
<!-- TABLE-FIRST:AREA:agent-memory:END -->

### RAG / Agentic Retrieval

<!-- TABLE-FIRST:AREA:rag:START -->
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
| ↗ Transition | [T²-RAGBench](https://aclanthology.org/2026.eacl-long.8/) <!-- benchmark-id:t2-ragbench --> | 2025-05-14 | Text-and-table retrieval followed by numerical reasoning over financial reports. | Removes oracle context from source QA datasets so retrieval and reasoning are evaluated end to end. |
| ↗ Transition | [DeepResearch Bench](https://arxiv.org/abs/2506.11763) <!-- benchmark-id:deepresearch-bench --> | 2025-06 | Evaluates deep-research agents on multi-step web research, evidence collection, citation quality, and long-form report synthesis. | Expanded search-agent evaluation from finding an answer to producing analyst-style, citation-rich research artifacts. |
| ↗ Transition | [BrowseComp-Plus](https://arxiv.org/abs/2508.06600) <!-- benchmark-id:browsecomp-plus --> | 2025-08 | Recasts deep-research evaluation over a fixed, curated corpus to isolate retriever and agent contributions and improve fairness and reproducibility. | Makes BrowseComp-style deep research reproducible enough to attribute gains to retrieval and agent behavior rather than an opaque live search stack. |
| 🔭 Frontier | [RAGCap-Bench](https://arxiv.org/abs/2510.13910) <!-- benchmark-id:ragcap-bench --> | 2025-10 | Decomposes agentic RAG into intermediate capabilities and evaluates those capabilities independently of final-answer quality. | Made intermediate agentic-RAG skills an explicit evaluation object rather than attributing end-to-end failures to a black box. |
| 🔭 Frontier | [LIT-RAGBench](https://arxiv.org/abs/2603.06198) <!-- benchmark-id:lit-ragbench --> | 2025-10-22 | Generator logic, integration, table use, reasoning, and abstention with supplied RAG contexts. | Controls away retriever quality and diagnoses five generator capabilities under one bilingual protocol. |
| 🔭 Frontier | [AgenticRAGTracer](https://arxiv.org/abs/2602.19127) <!-- benchmark-id:agenticragtracer --> | 2026-02 | Diagnoses multi-step agentic RAG by providing hop-aware intermediate validation rather than only final questions and answers. | Makes where a retrieval-reasoning chain fails observable at hop granularity. |
| 🔭 Frontier | [SAGE](https://arxiv.org/abs/2602.05975) <!-- benchmark-id:sage --> | 2026-02-05 | Targeted and open-ended scientific literature retrieval for deep-research agents. | Separates exact-paper discovery from broad evidence collection and makes agent-retriever fit measurable. |
| 🔭 Frontier | [GISA](https://arxiv.org/abs/2602.08543) <!-- benchmark-id:gisa --> | 2026-02-06 | Search planning, deep reasoning, broad aggregation, and structured answering for authentic information needs. | Combines human queries, stable and live subsets, deterministic scoring, and complete human search trajectories. |
| 🔭 Frontier | [MC-Search](https://arxiv.org/abs/2603.00873) <!-- benchmark-id:mc-search --> | 2026-02-22 | Multimodal search planning, modality choice, hop-level retrieval, and long-chain reasoning fidelity. | Adds structured multimodal search chains and process metrics beyond final-answer accuracy. |
| 🔭 Frontier | [MTRAG-UN](https://aclanthology.org/2026.findings-acl.503/) <!-- benchmark-id:mtrag-un --> | 2026-02-26 | Multi-turn RAG handling of unanswerable, underspecified, non-standalone, and unclear turns. | Adds four explicit conversational failure modes to reusable retrieval and generation evaluation. |
| 🔭 Frontier | [AutoResearchBench](https://arxiv.org/abs/2604.25256) <!-- benchmark-id:autoresearchbench --> | 2026-04-01 | Target-paper tracing, constrained literature search, open-set collection, and stopping decisions. | Separates finding one target from exhaustively collecting an unknown-size paper set. |
| 🔭 Frontier | [LeakDojo](https://aclanthology.org/2026.findings-acl.287/) <!-- benchmark-id:leakdojo --> | 2026-04-07 | Extraction of RAG database content across attacks, models, pipelines, budgets, and defenses. | Adds a controlled security diagnostic for comparing knowledge-extraction attacks and mitigations across RAG configurations. |
| 🔭 Frontier | [EnterpriseRAG-Bench](https://arxiv.org/abs/2605.05253) <!-- benchmark-id:enterpriserag-bench --> | 2026-04-14 | Enterprise retrieval, multi-document reasoning, conflict handling, completeness, and not-found behavior. | Adds a coherent nine-source enterprise corpus with controlled noise, duplicates, conflicts, and missing information. |
| 🔭 Frontier | [MERRIN](https://arxiv.org/abs/2604.13418) <!-- benchmark-id:merrin --> | 2026-04-15 | Uncued modality selection, multimodal evidence retrieval, and multi-hop reasoning on the noisy web. | Adds image, video, audio, and chart evidence with conflicting and partially relevant web results. |
| 🔭 Frontier | [MuDABench](https://aclanthology.org/2026.findings-acl.341/) <!-- benchmark-id:mudabench --> | 2026-04-19 | Information extraction, cross-document aggregation, and quantitative analysis over large financial collections. | Scales multi-document QA to collection-wide analysis and adds intermediate-fact coverage as a process signal. |
| 🔭 Frontier | [Bright-Pro](https://aclanthology.org/2026.acl-long.1705/) <!-- benchmark-id:bright-pro --> | 2026-04-30 | Reasoning-intensive retrieval, aspect coverage, and retriever utility in static and agentic search. | Extends BRIGHT from narrow relevance ranking to multi-aspect evidence portfolios and retriever-in-the-loop utility. |
| 🔭 Frontier | [SGR-Bench](https://arxiv.org/abs/2605.22219) <!-- benchmark-id:sgr-bench --> | 2026-05 | Benchmarks search agents when answer-bearing evidence appears only after the agent establishes the correct site-specific retrieval state. | Separates finding the right source from configuring the right filters, hierarchy, scope, or view inside that source. |
| 🔭 Frontier | [ScholarQuest](https://arxiv.org/abs/2606.20235) <!-- benchmark-id:scholarquest --> | 2026-05-19 | Intent-conditioned iterative paper retrieval, citation expansion, scope control, and set coverage. | Frames academic search as set retrieval with a shared large-scale backend, intent slices, and efficiency signals. |
| 🔭 Frontier | [LiveBrowseComp](https://arxiv.org/abs/2605.28721) <!-- benchmark-id:livebrowsecomp --> | 2026-05-27 | Retrieval of recent low-salience web facts rather than verification of parametric knowledge. | Uses facts from the preceding 90 days plus closed-book and source-removal diagnostics. |
| 🔭 Frontier | [EvoBrowseComp](https://arxiv.org/abs/2606.13120) <!-- benchmark-id:evobrowsecomp --> | 2026-06-11 | Broad English and Chinese web search over evolving knowledge. | Introduces an automatically refreshable bilingual live-web question-generation pipeline. |
| 🔭 Frontier | [LoHoSearch](https://arxiv.org/abs/2606.12837) <!-- benchmark-id:lohosearch --> | 2026-06-11 | Long-horizon search under large candidate spaces, complex constraints, and context-management pressure. | Controls search-space size and structural complexity through a knowledge graph rather than annotator intuition alone. |
| 🔭 Frontier | [WANDR](https://arxiv.org/abs/2608.14747) <!-- benchmark-id:wandr --> | 2026-07-14 | Live-web benchmark for wide-and-deep record collection with hierarchical tasks and reference-free record verification. | Combines open-set discovery, enrichment, and record-level verification on the live web. |
| 🔭 Frontier | [VAKRA](https://arxiv.org/abs/2608.12282) <!-- benchmark-id:vakra --> | 2026-08 | Evaluates agents that must compose executable APIs, document retrieval, multi-hop reasoning, and natural-language tool-use policies. | Unifies structured API interaction and unstructured retrieval in one executable evaluation with policy constraints. |
| 🔭 Frontier | [MAPLE](https://arxiv.org/abs/2608.15624) <!-- benchmark-id:maple --> | 2026-08-04 | Scientific retrieval benchmark that measures whether one paper remains retrievable across motivation, method, and result aspects. | Measures whether one paper stays retrievable across aspects instead of only one-query relevance. |
| 🔭 Frontier | [SearchAuditBench](https://arxiv.org/abs/2608.05212) <!-- benchmark-id:searchauditbench --> | 2026-08-05 | Localization, root-cause attribution, and repair of failures in long deep-search trajectories. | Adds expert critical-step labels, a six-way cause taxonomy, and repair-based recovery evaluation. |
| 🔭 Frontier | [DAS-Bench / DAS-Eval](https://arxiv.org/abs/2608.18034) <!-- benchmark-id:das-bench --> | 2026-08-07 | Academic-survey benchmark and evaluator that score literature coverage, taxonomy, claims, citations, discourse, and rendered artifact quality. | Turns coverage, taxonomy, claims, citations, discourse, and artifact quality into a 16-criterion survey protocol. |
| 🔭 Frontier | [The Recall Trap](https://arxiv.org/abs/2608.14838) <!-- benchmark-id:recall-trap --> | 2026-08-10 | Validity audit showing that higher file recall can reduce downstream repair success under a fixed-slot code-retrieval protocol. | Shows that higher file recall can lower repair success under fixed slots, limiting recall's interpretation. |
| 🔭 Frontier | [The Commercial Tax](https://arxiv.org/abs/2608.16096) <!-- benchmark-id:commercial-tax --> | 2026-08-17 | Retrieval reproducibility audit that binds raw embedder scores to licensing, query formatting, index construction, and deployment cost. | Audits retrieval-number transferability against license, query format, index construction, and cost. |
| 🔭 Frontier | [VisDocAgentBench](https://arxiv.org/abs/2608.17889) <!-- benchmark-id:visdocagentbench --> | 2026-08-18 | Visual-document retrieval benchmark that compares static rankers and iterative visual/OCR agents under one ranked-page contract. | Compares static visual retrieval with iterative page discovery and inspection under one top-10 contract. |
<!-- TABLE-FIRST:AREA:rag:END -->

### Data Agents

<!-- TABLE-FIRST:AREA:data-agent:START -->
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
| 🔭 Frontier | [LiveSQLBench](https://livesqlbench.ai/) <!-- benchmark-id:livesqlbench --> | 2025-05-28 | Query and management SQL over evolving industrial databases, hierarchical knowledge, and drifting business rules. | Moves static text-to-SQL to a live protocol with hidden refreshes, large schemas, business knowledge, and database-changing operations. |
| ↗ Transition | [KramaBench](https://arxiv.org/abs/2506.06541) <!-- benchmark-id:kramabench --> | 2025-06-06 | End-to-end discovery, cleaning, integration, analysis, and modeling over messy heterogeneous data lakes. | Moves from coding over selected inputs to finding evidence and building a working whole-lake data-to-insight pipeline. |
| ↗ Transition | [DABstep](https://arxiv.org/abs/2506.23719) <!-- benchmark-id:dabstep --> | 2025-06-30 | Multi-step financial analysis grounded in transactions, heterogeneous documentation, and domain rules. | Moves from single-table or single-step answers to long reasoning chains across data and documentation with objective checks. |
| 🔭 Frontier | [FDABench](https://arxiv.org/abs/2509.02473) <!-- benchmark-id:fdabench --> | 2025-09 | Evaluates data agents on analytical queries over heterogeneous structured, unstructured, web, and multimodal data. | Expanded data-agent evaluation from SQL or code to multi-source analytical workflows, while exposing cost and reasoning traces. |
| ↗ Transition | [AgentDS](https://arxiv.org/abs/2603.19005) <!-- benchmark-id:agentds --> | 2025-10-18 | AI-only versus human-AI collaborative performance on domain-specific predictive data-science challenges across six industries. | Makes domain expertise and human-AI collaboration a direct comparison axis rather than evaluating autonomy alone. |
| 🔭 Frontier | [DDR-Bench](https://arxiv.org/abs/2602.02039) <!-- benchmark-id:ddr-bench --> | 2025-11-30 | Autonomous goal setting, exploration, hypothesis testing, and verifiable insight discovery from only an entity and database metadata. | Changes the object from completing an assigned analysis question to deciding what is worth investigating and substantiating the findings. |
| 🔭 Frontier | [DAComp](https://arxiv.org/abs/2512.04324) <!-- benchmark-id:dacomp --> | 2025-12 | Benchmarks both repository-level data engineering and open-ended data analysis to cover a broader data-intelligence lifecycle. | Separates and jointly covers data engineering and analysis, moving evaluation toward the full data-intelligence lifecycle rather than isolated query or code tasks. |
| 🔭 Frontier | [DSAEval](https://arxiv.org/abs/2601.13591) <!-- benchmark-id:dsaeval --> | 2026-01-20 | Cumulative multi-query data-science projects over tabular, image, and text data, scored on reasoning, code, and results. | Moves from single-query tabular tasks to multimodal project sequences whose context accumulates across queries. |
| 🔭 Frontier | [DSGym](https://arxiv.org/abs/2601.16344) <!-- benchmark-id:dsgym --> | 2026-01-22 | Shortcut-filtered analysis, prediction, and domain tasks in a unified isolated execution framework. | Unifies fragmented benchmarks under one executable interface and explicitly audits whether tasks require the data. |
| 🔭 Frontier | [DARE-bench](https://arxiv.org/abs/2602.24288) <!-- benchmark-id:dare-bench --> | 2026-02-27 | Verifiable ML-model quality and fidelity to prescribed data-science instructions and processes. | Adds objective process adherence to outcome scoring instead of treating a good predictive score as sufficient. |
| 🔭 Frontier | [Data Agent Benchmark (DAB)](https://arxiv.org/abs/2603.20576) <!-- benchmark-id:data-agent-benchmark --> | 2026-03 | Evaluates enterprise data agents on questions requiring integration, transformation, and analysis across multiple heterogeneous database systems. | Targets the full enterprise data-question pipeline rather than isolated SQL generation or small in-context tables. |
| 🔭 Frontier | [TML-Bench](https://arxiv.org/abs/2603.05764) <!-- benchmark-id:tml-bench --> | 2026-03-05 | Reliable end-to-end tabular-ML submissions under fixed wall-clock budgets and hidden labels. | Extends one-shot code or score comparisons to time-performance scaling, submission success, and run-to-run stability. |
| 🔭 Frontier | [AgentFuel](https://arxiv.org/abs/2603.12483) <!-- benchmark-id:agentfuel --> | 2026-03-12 | Domain-customized functional evaluation of conversational time-series agents, especially stateful and incident-specific queries. | Moves from generic static questions to evaluations tailored to domain state and incident context. |
| 🔭 Frontier | [DataClawBench](https://arxiv.org/abs/2605.02503) <!-- benchmark-id:dataclawbench --> | 2026-05-04 | Low-prior exploratory analysis over unfamiliar, noisy, cross-domain financial data with verifiable conclusions. | Turns source and schema discovery into measured abilities and uses milestones to distinguish useful progress from aimless exploration. |
| 🔭 Frontier | [IRTS-ToolBench](https://arxiv.org/abs/2606.15107) <!-- benchmark-id:irts-toolbench --> | 2026-06-13 | Tool-grounded QA over asynchronous, missing, variably sampled irregular time series. | Removes the regular-grid assumption and directly measures irregularity handling and grounded tool choice. |
| 🔭 Frontier | [StatABench](https://arxiv.org/abs/2606.22977) <!-- benchmark-id:statabench --> | 2026-06-22 | Statistical knowledge, tool selection and parameterization, plus open end-to-end modeling and reporting. | Connects closed statistical diagnostics and tool use with open-ended modeling projects in one coordinate system. |
| 🔭 Frontier | [AgenticDataBench](https://arxiv.org/abs/2607.01647) <!-- benchmark-id:agenticdatabench --> | 2026-07 | Benchmarks data agents across realistic data-science workflows using a skill taxonomy to quantify fine-grained coverage. | Makes data-science skill coverage itself explicit, enabling diagnosis beyond aggregate task success. |
| 🔭 Frontier | [CausalDS](https://arxiv.org/abs/2607.08093) <!-- benchmark-id:causalds --> | 2026-07-09 | Executable causal data science across prediction, identification, effects, counterfactuals, uncertainty, and abstention. | Extends data-agent evaluation beyond association and prediction to all Pearl rungs and recognition of unwarranted answers. |
| 🔭 Frontier | [data-eng-bench](https://github.com/Snowflake-Labs/data-eng-bench) <!-- benchmark-id:data-eng-bench --> | 2026-07-29 | Executable data-engineering benchmark for repository-scale dbt transformations with hidden row-level verification on DuckDB and Snowflake. | Uses executable dbt tasks and hidden row-level checks; an August fix makes evaluator reliability part of the measurement object. |
| 🔭 Frontier | [DataSpace](https://arxiv.org/abs/2608.03451) <!-- benchmark-id:dataspace --> | 2026-08 | Evaluates verifiable analytics over heterogeneous workspaces where evidence spans databases, files, documents, and multimedia. | Unifies heterogeneous evidence discovery with deterministic complete-result evaluation in a task-local workspace. |
| 🔭 Frontier | [DSAgentBench](https://arxiv.org/abs/2608.10366) <!-- benchmark-id:dsagentbench --> | 2026-08 | Evaluates agents on complete data-science workflows inside real computer environments using notebooks, IDEs, terminals, browsers, and databases. | Moves data-agent evaluation into real computer environments where success requires multi-stage, multi-tool execution grounded in intermediate outputs. |
| 🔭 Frontier | [WarehouseReliabilityBench](https://arxiv.org/abs/2608.09254) <!-- benchmark-id:warehouse-reliability-bench --> | 2026-08-10 | Business-correct analytics plus appropriate clarification, abstention, or refusal under ambiguity, unanswerability, drift, and attacks. | Moves beyond executable SQL to business truth and correct non-answer behavior when returning a number would be false success. |
| 🔭 Frontier | [Data Exploration Benchmark](https://arxiv.org/abs/2608.16045) <!-- benchmark-id:data-exploration-benchmark --> | 2026-08-17 | Structured dataset understanding before analysis, including logical tables, semantics, keys, relationships, and profiling signals. | Turns implicit data exploration from a prerequisite hidden behind final-answer accuracy into a directly scored artifact with measured downstream value. |
<!-- TABLE-FIRST:AREA:data-agent:END -->

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
