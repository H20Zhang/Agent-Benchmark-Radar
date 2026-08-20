# Agent Benchmark Radar

[中文](README.md) | **English**

**The entry point to the Research Radar family — and its evaluation layer.**

Start here to see **what Agent Memory, Agentic RAG, and Data Agents are being asked to do, how those targets evolved, and what current scores actually support**. Then continue into the corresponding domain radar for methods and systems.

**Research Radars:** [Agent Memory](https://github.com/H20Zhang/Agent-Memory-Radar#field-map) · [Agentic RAG](https://github.com/H20Zhang/Agentic-RAG-Radar#field-map) · [Data Agent](https://github.com/H20Zhang/Data-Agent-Radar#field-map)

[30 sec: Timeline](#timeline) · [3 min: 7/30-day changes](#periods) · [5 min: Field Map](#field-map) · [15 min: Reading Paths](#reading-paths) · [Browse all](#library)

> **Core idea.** A useful new benchmark is often an implicit critique of the previous generation: **what was too easy, narrow, static, synthetic, opaque, or weakly diagnosed?**
>
> **Comparison rule.** A higher leaderboard score is system-level evidence unless model, accessible state, tool interface, prompts/hints, retries, stopping rule, evaluator, and relevant cost budgets are sufficiently matched.

Last updated: **2026-08-20**

<a id="timeline"></a><a id="latest"></a><a id="frontier"></a>
## Latest Timeline

> **Migration notice.** Legacy records whose Radar acceptance time cannot be reconstructed are temporarily ordered by their original release date or month, preserving honest month precision. Every post-v2-cutover record uses `radar_published_at`.

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
### Last 7 days: 2026-08-14—2026-08-20

- **`no_material_change` · Benchmark acceptance time: no new direction is attributable to Radar acceptance time in this window.** <!-- timefirst:direction key="benchmark-acceptance-time" state="no_material_change" supports="none" confidence="high" implication="require-native-v2-times-for-period-claims" timing="radar_published_at" synthesized="2026-08-20T00:00:00Z" prior="none" -->
  Supports: **none**; confidence: **high**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (require native v2 times for period claims): legacy Timeline records are historical context only, not support; only records with native v2 Radar acceptance times can support the window. Exact synthesis time: `2026-08-20T00:00:00Z` (UTC).

<a id="last-30-days"></a>
### Last 30 days: 2026-07-22—2026-08-20

- **`no_material_change` · Benchmark acceptance time: no new direction is attributable to Radar acceptance time in this window.** <!-- timefirst:direction key="benchmark-acceptance-time" state="no_material_change" supports="none" confidence="high" implication="require-native-v2-times-for-period-claims" timing="radar_published_at" synthesized="2026-08-20T00:00:00Z" prior="none" -->
  Supports: **none**; confidence: **high**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (require native v2 times for period claims): DSAgentBench, VAKRA, DataSpace, LoCoMo-Plus, Mem2ActBench, and AgenticDataBench are historical context only, not support for this window; their month-precision records cannot establish a Radar acceptance inside it. Exact synthesis time: `2026-08-20T00:00:00Z` (UTC).

<a id="evolution"></a>
## What Benchmark Evolution Says About the Field

| Area | Evolution | What the field increasingly cares about | Continue |
|---|---|---|---|
| **Agent Memory** | multi-session recall → lifecycle diagnosis → evolving, shared, multimodal state → **memory-guided behavior and action** | What should be written, revised, authorized, forgotten, and then used—and where did failure enter that lifecycle? | [Agent Memory Radar](https://github.com/H20Zhang/Agent-Memory-Radar#field-map) |
| **RAG / Agentic Retrieval** | relevance/faithfulness → iterative search → evidence-set coverage → **live, multimodal, auditable search** | Can the agent find complementary evidence, know when to stop, and localize or repair a failed search? | [Agentic RAG Radar](https://github.com/H20Zhang/Agentic-RAG-Radar#field-map) |
| **Data Agents** | NL→SQL/code → workflows/exploration → heterogeneous analytics → **business-correct, reliable delivery** | Can the agent discover and understand data, execute and verify work, and clarify or abstain instead of returning false success? | [Data Agent Radar](https://github.com/H20Zhang/Data-Agent-Radar#field-map) |

<a id="field-map"></a>
## Field Maps

<a id="benchmark-memory"></a>
### Agent Memory

**Defining chain:** [Multi-Session Chat](https://aclanthology.org/2022.acl-long.356/) → [LoCoMo](https://aclanthology.org/2024.acl-long.747/) / [LongMemEval](https://arxiv.org/abs/2410.10813) → [MemoryAgentBench](https://arxiv.org/abs/2507.05257) → [MemoryArena](https://arxiv.org/abs/2602.16313) / [WorldMemArena](https://arxiv.org/abs/2605.29341) / [InMind](https://arxiv.org/abs/2607.24368) → [Mem2ActBench](https://aclanthology.org/2026.acl-long.370/) / [LoCoMo-Plus](https://aclanthology.org/2026.acl-long.1150/)

**Frontier signal:** lifecycle benchmarks now separate writing, maintenance, retrieval, and use; other branches expose implicit behavior change, multimodal retention, group identity, authorization/deletion, personalized safety, and memory-guided action.

**Biggest gap:** longitudinal causality in persistent environments with matched cost/context budgets, permissions, irreversible actions, and weeks/months of state evolution.

[Open the complete Agent Memory benchmark table →](library/README.en.md#agent-memory) · [Continue into Agent Memory methods/systems →](https://github.com/H20Zhang/Agent-Memory-Radar#field-map)

<details><summary><strong>Open the fuller memory genealogy</strong></summary>

`Multi-Session Chat → LoCoMo / LongMemEval → MemBench / MemoryAgentBench / BEAM → MemoryArena / WorldMemArena / InMind → ImplicitMemBench / GateMem / DynamicMem / Mem2ActBench / LoCoMo-Plus`

Use the [Benchmark Library](#library) for the complete registry and roles.

</details>

<a id="benchmark-rag"></a>
### RAG / Agentic Retrieval

**Defining chain:** [HotpotQA](https://aclanthology.org/D18-1259/) → [BEIR](https://arxiv.org/abs/2104.08663) / [BRIGHT](https://arxiv.org/abs/2407.12883) → [BrowseComp](https://arxiv.org/abs/2504.12516) → [AutoResearchBench](https://arxiv.org/abs/2604.25256) / [Bright-Pro](https://aclanthology.org/2026.acl-long.1705/) → [LiveBrowseComp](https://arxiv.org/abs/2605.28721) / [LoHoSearch](https://arxiv.org/abs/2606.12837) → [SearchAuditBench](https://arxiv.org/abs/2608.05212) / [VAKRA](https://arxiv.org/abs/2608.12282)

**Frontier signal:** evaluation is splitting relevance from aspect coverage, target finding from exhaustive set collection, and final correctness from stopping, calibration, failure localization, repair, security, multimodal evidence, and live-web freshness.

**Biggest gap:** causal attribution under matched interface/harness/model/budget, especially for long-horizon live environments where web state drifts.

[Open the complete RAG benchmark table →](library/README.en.md#rag--agentic-retrieval) · [Continue into Agentic RAG methods/systems →](https://github.com/H20Zhang/Agentic-RAG-Radar#field-map)

<a id="benchmark-data"></a>
### Data Agents

**Defining chain:** [WikiSQL](https://arxiv.org/abs/1709.00103) → [Spider](https://aclanthology.org/D18-1425/) / [DS-1000](https://arxiv.org/abs/2211.11501) → [Spider 2.0](https://arxiv.org/abs/2411.07763) / [DDR-Bench](https://arxiv.org/abs/2602.02039) → [DataClawBench](https://arxiv.org/abs/2605.02503) / [Data Exploration Benchmark](https://arxiv.org/abs/2608.16045) → [CausalDS](https://arxiv.org/abs/2607.08093) / [WarehouseReliabilityBench](https://arxiv.org/abs/2608.09254) / [DataSpace](https://arxiv.org/abs/2608.03451) / [DSAgentBench](https://arxiv.org/abs/2608.10366)

**Frontier signal:** data discovery and understanding are becoming scored artifacts; causal identification, process fidelity, business truth, clarification, abstention, recovery, stability, and cost now sit beside end-to-end task success.

**Biggest gap:** real enterprise semantics, business-definition ambiguity, long-running workflow state, deployment/monitoring, governance, and reliable verification when the requested answer itself is underspecified.

[Open the complete Data Agent benchmark table →](library/README.en.md#data-agents) · [Continue into Data Agent methods/systems →](https://github.com/H20Zhang/Data-Agent-Radar#field-map)

## What Is Still Poorly Measured

Benchmark coverage is **not** the field. Important research questions can matter before a clean benchmark exists.

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
| **How did memory move from recall to diagnosable action?** | Multi-Session Chat → LoCoMo / LongMemEval → MemoryAgentBench → WorldMemArena / InMind → Mem2ActBench / LoCoMo-Plus | [Agent Memory Radar](https://github.com/H20Zhang/Agent-Memory-Radar#field-map) |
| **How did retrieval become an auditable search process?** | HotpotQA / BEIR → BrowseComp → AutoResearchBench / Bright-Pro → LiveBrowseComp / LoHoSearch → SearchAuditBench | [Agentic RAG Radar](https://github.com/H20Zhang/Agentic-RAG-Radar#field-map) |
| **How did data evaluation move from executable code to business-correct delivery?** | WikiSQL / Spider / DS-1000 → DDR-Bench / DataClawBench → Data Exploration Benchmark → WarehouseReliabilityBench / DataSpace / DSAgentBench | [Data Agent Radar](https://github.com/H20Zhang/Data-Agent-Radar#field-map) |

<a id="library"></a>
## Benchmark Library

- **[Browse the complete release chronology and area tables](library/README.en.md)**
- [Follow genealogy and measurement-coordinate routes](library/README.en.md#browse-by-genealogy)
- [Canonical registry](data/benchmarks.json)
- [Research compactions](digests/README.md)

## About

This Radar is the default entry to the family because benchmark genealogy gives a compact first answer to **what capability matters, why the older target became insufficient, and what current evidence counts as progress**. It should route to domain radars rather than duplicate their method surveys.

[中文](README.md) · [Curation](CURATION.md) · [Schema](SCHEMA.md)
