# Agent Benchmark Radar

[中文](README.md) | **English**

**The entry point to the Research Radar family — and its evaluation layer.**

Start here to see **what Agent Memory, Agentic RAG, and Data Agents are being asked to do, how those targets evolved, and what current scores actually support**. Then continue into the corresponding domain radar for methods and systems.

**Research Radars:** [Agent Memory](https://github.com/H20Zhang/Agent-Memory-Radar) · [Agentic RAG](https://github.com/H20Zhang/Agentic-RAG-Radar) · [Data Agent](https://github.com/H20Zhang/Data-Agent-Radar)

[30 sec: Frontier](#frontier) · [5 min: Field Evolution](#evolution) · [15 min: Reading Paths](#reading-paths) · [Browse all](#library)

> **Core idea.** A useful new benchmark is often an implicit critique of the previous generation: **what was too easy, narrow, static, synthetic, opaque, or weakly diagnosed?**
>
> **Comparison rule.** A higher leaderboard score is system-level evidence unless model, accessible state, tool interface, prompts/hints, retries, stopping rule, evaluator, and relevant cost budgets are sufficiently matched.

Last updated: **2026-08-20**

<a id="frontier"></a>
## New & Notable

| Benchmark | Area | What becomes measurable | Field signal |
|---|---|---|---|
| [DSAgentBench](https://arxiv.org/abs/2608.10366) | Data Agent | End-to-end data-science workflows in a **real computer environment** | Evaluation is moving from code/answer quality to grounded multi-tool work |
| [VAKRA](https://arxiv.org/abs/2608.12282) | RAG / Agents | Executable APIs + retrieved documents + policy constraints in one trajectory | Retrieval is becoming cross-source execution, not only ranking |
| [DataSpace](https://arxiv.org/abs/2608.03451) | Data Agent | Verifiable analytics over DBs, files, documents, and multimedia | Heterogeneous evidence discovery + deterministic output verification matter jointly |
| [LoCoMo-Plus](https://arxiv.org/abs/2602.10715) | Agent Memory | Applying latent user constraints when later cues do not restate them | Memory is moving beyond explicit recall toward persistent user state |
| [Mem2ActBench](https://aclanthology.org/2026.acl-long.370/) | Agent Memory | Memory used for tool selection and parameter grounding | Memory is being judged by whether it changes **action**, not only answers |
| [RealMem](https://aclanthology.org/2026.findings-acl.703/) | Agent Memory | Evolving project state across long-running cross-session work | Long-term memory is moving toward persistent project work |
| [AgenticDataBench](https://arxiv.org/abs/2607.01647) | Data Agent | Fine-grained **data-science skill coverage** across realistic tasks | Aggregate success is no longer enough; capability coverage itself becomes auditable |
| [SGR-Bench](https://arxiv.org/abs/2605.22219) | RAG / Search | Search when evidence is gated behind filters, hierarchy, scope, and site state | Reaching a source is not equivalent to configuring the information environment correctly |

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
## What Benchmark Evolution Says About the Field

| Area | Evolution | What the field increasingly cares about | Continue |
|---|---|---|---|
| **Agent Memory** | multi-session recall → time/update/forget → structure/scale/multimodality → **implicit user state + memory-guided action** | What should be written, updated, inferred, forgotten, and applied to future behavior? | [Agent Memory Radar](https://github.com/H20Zhang/Agent-Memory-Radar) |
| **RAG / Agentic Retrieval** | retrieval quality → robustness/faithfulness → deep research → **stateful, controlled, cross-source execution** | Can the agent configure and navigate an information environment under changing state and budgets? | [Agentic RAG Radar](https://github.com/H20Zhang/Agentic-RAG-Radar) |
| **Data Agents** | NL→SQL/code → experimentation/workflows → heterogeneous analytics → **real-computer end-to-end data work** | Can an agent discover, transform, analyze, verify, recover, and deliver useful artifacts? | [Data Agent Radar](https://github.com/H20Zhang/Data-Agent-Radar) |

## Field Maps

### Agent Memory

**Defining chain:** [Multi-Session Chat](https://aclanthology.org/2022.acl-long.356/) → [LoCoMo](https://aclanthology.org/2024.acl-long.747/) / [LongMemEval](https://arxiv.org/abs/2410.10813) → [MemoryAgentBench](https://arxiv.org/abs/2507.05257) → [Mem2ActBench](https://aclanthology.org/2026.acl-long.370/) / [LoCoMo-Plus](https://arxiv.org/abs/2602.10715)

**Frontier signal:** the target is splitting into write/update/forget, organization, multimodal fidelity, persistent user state, procedural knowledge, and memory-guided action.

**Biggest gap:** longitudinal causality in persistent environments with matched cost/context budgets, permissions, irreversible actions, and weeks/months of state evolution.

[Continue into Agent Memory methods/systems →](https://github.com/H20Zhang/Agent-Memory-Radar)

<details><summary><strong>Open the fuller memory genealogy</strong></summary>

`Multi-Session Chat → LoCoMo / LongMemEval → MemBench / MemoryAgentBench / BEAM → Mem-Gallery / MemEye / StructMemEval / LongMemEval-V2 → MemoryArena / Mem2ActBench / LoCoMo-Plus / RealMem`

Use the [Benchmark Library](#library) for the complete registry and roles.

</details>

### RAG / Agentic Retrieval

**Defining chain:** [HotpotQA](https://aclanthology.org/D18-1259/) → [BEIR](https://arxiv.org/abs/2104.08663) → [BrowseComp](https://arxiv.org/abs/2504.12516) → [SGR-Bench](https://arxiv.org/abs/2605.22219) → [VAKRA](https://arxiv.org/abs/2608.12282)

**Frontier signal:** retrieval is expanding from ranking documents toward controlling an information environment, including source state, tools, stopping, and cross-source execution.

**Biggest gap:** causal attribution under matched interface/harness/model/budget, especially for long-horizon live environments where web state drifts.

[Continue into Agentic RAG methods/systems →](https://github.com/H20Zhang/Agentic-RAG-Radar)

### Data Agents

**Defining chain:** [WikiSQL](https://arxiv.org/abs/1709.00103) → [Spider](https://aclanthology.org/D18-1425/) / [DS-1000](https://arxiv.org/abs/2211.11501) → [AgenticDataBench](https://arxiv.org/abs/2607.01647) → [DataSpace](https://arxiv.org/abs/2608.03451) → [DSAgentBench](https://arxiv.org/abs/2608.10366)

**Frontier signal:** the evaluation object is becoming full data work rather than query/code generation: heterogeneous discovery, tool orchestration, intermediate-state grounding, verification, and artifact delivery.

**Biggest gap:** real enterprise semantics, business-definition ambiguity, long-running workflow state, deployment/monitoring, governance, and reliable verification when the requested answer itself is underspecified.

[Continue into Data Agent methods/systems →](https://github.com/H20Zhang/Data-Agent-Radar)

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
| **How did memory move from recall to action?** | Multi-Session Chat → LoCoMo → LongMemEval → MemoryArena / Mem2ActBench / LoCoMo-Plus | [Agent Memory Radar](https://github.com/H20Zhang/Agent-Memory-Radar) |
| **How did retrieval become a stateful control problem?** | HotpotQA / BEIR → BrowseComp → SGR-Bench → VAKRA | [Agentic RAG Radar](https://github.com/H20Zhang/Agentic-RAG-Radar) |
| **How did data-agent evaluation move from SQL/code to real workspaces?** | WikiSQL / Spider / DS-1000 → AgenticDataBench → DataSpace → DSAgentBench | [Data Agent Radar](https://github.com/H20Zhang/Data-Agent-Radar) |

<a id="library"></a>
## Benchmark Library

- **[Browse by area / genealogy / measurement coordinate / year](library/README.en.md)**
- [Canonical registry](data/benchmarks.json)
- [Research compactions](digests/README.md)

## About

This Radar is the default entry to the family because benchmark genealogy gives a compact first answer to **what capability matters, why the older target became insufficient, and what current evidence counts as progress**. It should route to domain radars rather than duplicate their method surveys.

[中文](README.md) · [Curation](CURATION.md) · [Schema](SCHEMA.md)
