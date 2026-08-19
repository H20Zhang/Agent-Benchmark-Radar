# 🧭 Agent Benchmark Radar

**A living map of benchmarks for Agent Memory, RAG / Agentic Retrieval, and Data Agents.**

Use it in two directions: **Latest → what the field is starting to care about now**, and **Foundation → how the definition of progress got here**.

⭐ **Star this repo to follow new benchmarks, benchmark revisions, and shifts in what the field considers worth measuring.**

**Last updated:** 2026-08-20 · **34 benchmarks tracked** · [New & Notable](#-new--notable) · [Field Evolution](#-what-benchmark-evolution-says-about-the-field) · [Memory](#-agent-memory) · [RAG](#-rag--agentic-retrieval) · [Data Agents](#-data-agents)

> **Core idea:** a new benchmark is often a critique of the previous generation. The interesting question is not only *who scores highest?* but **what did the old benchmark fail to measure badly enough that a new one had to exist?**

> **Comparison rule:** a higher leaderboard score is system-level evidence unless model, accessible state, tool interface, prompts/hints, retries, stopping rule, evaluator, and relevant cost budgets are sufficiently matched.

## 🔥 New & Notable

These are the newest benchmarks that materially change the evaluation object—not simply new datasets with more examples.

| Benchmark | Area | Released | What is newly exposed | Signal for the field |
|---|---|---:|---|---|
| [VAKRA](https://arxiv.org/abs/2608.12282) | RAG / Agents | 2026-08 | Reasoning across **executable APIs + retrieved documents + tool-use policies** | Retrieval is becoming a cross-source execution problem, not a text-search primitive |
| [DSAgentBench](https://arxiv.org/abs/2608.10366) | Data Agent | 2026-08 | Full data-science workflows inside a **real computer environment** | Data-agent evaluation is moving from answer/code quality to grounded multi-tool execution |
| [DataSpace](https://arxiv.org/abs/2608.03451) | Data Agent | 2026-08 | Verifiable analytics over databases, files, documents, and multimedia | Heterogeneous evidence discovery + deterministic output checking is becoming central |
| [LoCoMo-Plus](https://aclanthology.org/2026.acl-long.1150/) | Agent Memory | 2026-07 | Applying **latent user constraints** when later cues do not restate them | Memory is moving beyond explicit factual recall toward user-state and cognitive consistency |
| [AgenticDataBench](https://arxiv.org/abs/2607.01647) | Data Agent | 2026-07 | Fine-grained **data-science skill coverage** across realistic domains | Aggregate task success is no longer enough; the field wants capability-level diagnosis |
| [LifeSide](https://arxiv.org/abs/2606.04660) | Agent Memory | 2026-06 | Memory–emotion–environment loops, privacy control, persistent user models | Long-term memory is becoming part of a broader lifelong-user model |
| [SGR-Bench](https://arxiv.org/abs/2605.22219) | RAG / Search | 2026-05 | **Retrieval-state control**: filters, hierarchy, scope, site-specific views | “Found the right website” is no longer equivalent to “retrieved the right evidence” |
| [LongMemEval-V2](https://arxiv.org/abs/2605.12493) | Agent Memory | 2026-05 | Memory over accumulated **agent-environment experience** up to 115M-token histories | Memory is shifting from conversation history toward reusable workflow/environment experience |

## 🧬 What Benchmark Evolution Says About the Field

Benchmarks are useful as a **history of changing bottlenecks**. Read each arrow as: *the previous evaluation target became too easy, too narrow, or too unrealistic*.

| Area | Evolution | What the field increasingly cares about |
|---|---|---|
| **Agent Memory** | conversation recall → temporal/update/forget → memory structure → agent trajectories → procedural/implicit user knowledge | Not merely *can I retrieve an old fact?*, but **what should be written, updated, structured, forgotten, inferred, and reused to change future behavior?** |
| **RAG / Search** | static retrieval → multi-hop/dynamic facts → persistent web search → research synthesis → stateful & cross-source execution | Retrieval intelligence is moving from ranking documents toward **controlling an information environment under changing state, tools, and budgets** |
| **Data Agents** | NL→SQL → cross-schema SQL → large real DBs → enterprise workflows → heterogeneous analytics → real-computer data science | The target is moving from query generation toward **autonomous data work: discover, transform, join, analyze, verify, and communicate** |

### Legend

`🌱 Precursor` introduced an evaluation object inherited by later agent benchmarks · `🧱 Foundation` established a durable modern coordinate system · `↗ Transition` materially expanded realism/capability coverage · `🔭 Frontier` reflects a current direction and is intentionally time-relative.

---

## 🧠 Agent Memory

### Evolution in one line

**LoCoMo / LongMemEval** made long-term conversational memory measurable → **MemBench / MemoryAgentBench / BEAM** asked whether memory also updates, forgets, scales, and works incrementally → **AMA-Bench / LifeBench / StructMemEval / LongMemEval-V2 / LifeSide / LoCoMo-Plus** move toward agent experience, memory organization, procedural knowledge, persistent user models, and implicit constraints.

| Role | Benchmark | Year | What it actually measures | Why it changed the question |
|---|---|---:|---|---|
| 🧱 | [LoCoMo](https://aclanthology.org/2024.acl-long.747/) | 2024 | Very-long multi-session conversational memory; QA, event summarization, multimodal dialogue | Established long-horizon conversation as a memory problem rather than ordinary context use |
| 🧱 | [LongMemEval](https://arxiv.org/abs/2410.10813) | 2024 | Extraction, multi-session reasoning, temporal reasoning, **knowledge update**, abstention | Showed that “remembering” contains qualitatively different operations, especially time and update |
| ↗ | [MemBench](https://arxiv.org/abs/2506.21605) | 2025 | Factual vs reflective memory; participation vs observation; effectiveness, efficiency, capacity | Expanded evaluation beyond one accuracy number and one interaction regime |
| ↗ | [MemoryAgentBench](https://arxiv.org/abs/2507.05257) | 2025 / ICLR'26 | Accurate retrieval, test-time learning, long-range understanding, selective forgetting under incremental interaction | Treats memory as an **online process**, not a frozen context handed to a model |
| ↗ | [BEAM](https://arxiv.org/abs/2510.27246) | 2025 | Coherent long-term memory from 1M toward 10M-token conversations | Makes memory degradation at truly massive horizons directly visible |
| 🔭 | [StructMemEval](https://arxiv.org/abs/2602.11243) | 2026 | Whether an agent chooses/maintains useful structures such as ledgers, lists, and trees | Asks whether **organization** itself is a memory capability |
| 🔭 | [AMA-Bench](https://arxiv.org/abs/2602.22769) | 2026 | Memory over real + scalable synthetic **agent-environment trajectories** | Moves from dialogue-centric memory toward causality and machine-generated experience |
| 🔭 | [LifeBench](https://arxiv.org/abs/2603.03781) | 2026 | Declarative + non-declarative memory including habitual/procedural knowledge across digital traces | Explicit facts are no longer assumed to be the whole memory problem |
| 🔭 | [LongMemEval-V2](https://arxiv.org/abs/2605.12493) | 2026 | Static/dynamic state, workflow knowledge, environment gotchas, premise awareness from huge trajectory histories | “Experienced colleague” knowledge becomes the target rather than user-history recall |
| 🔭 | [LifeSide](https://arxiv.org/abs/2606.04660) | 2026 | Persistent user understanding, privacy control, emotional companionship over long horizons | Couples memory with evolving user/environment state rather than scoring recall in isolation |
| 🔭 | [LoCoMo-Plus](https://aclanthology.org/2026.acl-long.1150/) | 2026 | Latent constraints such as user state/goals/values under cue–trigger semantic disconnect | Pushes memory from explicit facts toward **cognitive consistency** |

**Current memory signal:** the frontier is fragmenting in a productive way. “Memory quality” is no longer one axis: **write/update/forget**, **structure**, **agent experience**, **procedural knowledge**, and **persistent user state** are becoming separate evaluation objects. The important missing step is still causal: *does this memory make a future agent execute better under matched latency, context, and cost?*

---

## 🔎 RAG / Agentic Retrieval

### Evolution in one line

**HotpotQA / KILT / BEIR** established multi-document reasoning, provenance, and robust retrieval → **MultiHop-RAG / CRAG / RAGBench** made RAG itself the evaluated system and introduced multi-hop, freshness, and evaluator quality → **BrowseComp / DeepResearch Bench** shifted toward autonomous information seeking → **RAGCap / AgenticRAGTracer / SGR-Bench / VAKRA** expose intermediate capability, retrieval state, and cross-source execution.

| Role | Benchmark | Year | What it actually measures | Why it changed the question |
|---|---|---:|---|---|
| 🌱 | [HotpotQA](https://aclanthology.org/D18-1259/) | 2018 | Multi-document evidence retrieval/reasoning with supporting facts | Made evidence composition and explainability a core multi-hop QA target |
| 🧱 | [KILT](https://arxiv.org/abs/2009.02252) | 2020 | Knowledge-intensive tasks on one shared Wikipedia snapshot with provenance | Established that downstream correctness **and where evidence came from** should be evaluated together |
| 🧱 | [BEIR](https://arxiv.org/abs/2104.08663) | 2021 | Zero-shot retrieval generalization across heterogeneous domains/tasks | Made retriever robustness across datasets more important than winning one IR benchmark |
| ↗ | [MultiHop-RAG](https://arxiv.org/abs/2401.15391) | 2024 | Retrieval + reasoning over multiple supporting pieces inside a RAG pipeline | Exposed single-shot retrieval as insufficient for compositional questions |
| ↗ | [CRAG](https://arxiv.org/abs/2406.04744) | 2024 | Dynamic factual QA, long-tail entities, web/KG retrieval, hallucination | Brought **freshness and factual dynamism** into mainstream RAG evaluation; KDD Cup 2024 anchor |
| ↗ | [RAGBench](https://arxiv.org/abs/2407.11005) | 2024 | Explainable evaluation labels for retrieval and generation quality | Made the **quality of the RAG evaluator** itself a benchmark problem |
| ↗ | [BrowseComp](https://arxiv.org/abs/2504.12516) | 2025 | Persistent web browsing for hard-to-find short answers | Shifted from “retrieve a passage” to **keep searching until obscure evidence is found** |
| ↗ | [DeepResearch Bench](https://arxiv.org/abs/2506.11763) | 2025 | Multi-step web research, effective citations, citation accuracy, long-form synthesis | Raised the output target from answer retrieval to analyst-style research reports |
| 🔭 | [RAGCap-Bench](https://arxiv.org/abs/2510.13910) | 2025 | Intermediate capabilities inside agentic-RAG workflows | Final-answer accuracy is no longer sufficient for diagnosing why an agentic RAG system fails |
| 🔭 | [AgenticRAGTracer](https://arxiv.org/abs/2602.19127) | 2026 | Hop-level validation and step allocation in multi-step retrieval reasoning | Makes failure location inside a retrieval trajectory observable |
| 🔭 | [SGR-Bench](https://arxiv.org/abs/2605.22219) | 2026 | Search when evidence is gated behind site-specific filters/views/scopes | Makes **environment state configuration** part of retrieval competence |
| 🔭 | [VAKRA](https://arxiv.org/abs/2608.12282) | 2026 | Executable APIs + document retrieval + multi-hop reasoning + policy constraints | Pushes retrieval into **cross-source tool execution**, where identity/grounding must stay coherent across modalities of access |

**Current RAG signal:** “retrieval” is expanding from a model primitive into a **control problem over an information environment**. What matters increasingly is *when to search, where, through which interface, under which state, how to compose heterogeneous evidence, and when to stop*—not only retriever Recall@k.

---

## 🗄️ Data Agents

### Evolution in one line

**WikiSQL / Spider / DS-1000** established executable language→data/code tasks → **BIRD / Spider 2.0 / DataSciBench** introduced large real databases, metadata, enterprise workflows, and broader analysis → **FDABench / DAB / AgenticDataBench / DataSpace / DSAgentBench** make heterogeneous evidence, skills, full workflows, and real-computer execution the target.

| Role | Benchmark | Year | What it actually measures | Why it changed the question |
|---|---|---:|---|---|
| 🌱 | [WikiSQL](https://arxiv.org/abs/1709.00103) | 2017 | NL→SQL over single Wikipedia tables with execution accuracy | Established executable natural-language database access at large scale |
| 🧱 | [Spider](https://aclanthology.org/D18-1425/) | 2018 | Complex multi-table SQL and generalization to **unseen database schemas** | Became the canonical cross-domain text-to-SQL coordinate system |
| 🧱 | [DS-1000](https://arxiv.org/abs/2211.11501) | 2022 | Data-science code generation across seven Python libraries with reliable execution tests | Added executable data-science programming as a separate foundation beyond SQL |
| ↗ | [BIRD](https://arxiv.org/abs/2305.03111) | 2023 | Large real DBs, dirty values, external knowledge, SQL efficiency | Moves text-to-SQL closer to realistic database contents and operational efficiency |
| ↗ | [Spider 2.0](https://arxiv.org/abs/2411.07763) | 2024 | Enterprise SQL workflows, huge schemas, metadata/docs/code search, multiple dialects | Turns text-to-SQL into a **long-horizon agent workflow** rather than one generated query |
| ↗ | [DataSciBench](https://arxiv.org/abs/2502.13897) | 2025 | Broader data-science prompts with task-specific programmatic evaluation | Expands the object beyond SQL toward heterogeneous analytical work |
| 🔭 | [FDABench](https://arxiv.org/abs/2509.02473) | 2025 / KDD'26 | 2,007 multi-source analytical tasks over structured, unstructured, web, and multimodal data | Makes heterogeneous analysis, traces, latency, and token cost visible together |
| 🔭 | [Data Agent Benchmark (DAB)](https://arxiv.org/abs/2603.20576) | 2026 | Enterprise questions across multiple DBMSes, awkward joins, text transforms, domain knowledge | Evaluates the integration→transformation→analysis pipeline rather than isolated query translation |
| 🔭 | [AgenticDataBench](https://arxiv.org/abs/2607.01647) | 2026 | Realistic workflows with a fine-grained taxonomy of data-science skills | Introduces **skill coverage** as a way to ask what a data-agent benchmark actually spans |
| 🔭 | [DataSpace](https://arxiv.org/abs/2608.03451) | 2026 | Verifiable tabular analytics over heterogeneous task-local workspaces | Combines discovery across CSV/JSON/DB/docs/PDF/video with deterministic complete-result checking |
| 🔭 | [DSAgentBench](https://arxiv.org/abs/2608.10366) | 2026 | End-to-end data-science lifecycle inside notebooks, IDEs, terminals, browsers, and DBs | Puts agents in a **real computer** and evaluates multi-stage tool orchestration, not code snippets |

**Current data-agent signal:** text-to-SQL is becoming a substrate, not the end task. The emerging target is an agent that can **discover data, understand semantics, transform and join heterogeneous sources, execute tools, react to intermediate outputs, and return verifiable analytical artifacts**.

---

## 🕳️ What Is Still Poorly Measured

**1. Component causality under matched harnesses.** Most leaderboards still change model, prompts, tools, retries, memory/retrieval implementation, and budgets together. They tell us which *system* won, much less often *why*.

**2. Lifecycle resource cost.** Memory writing/indexing, retrieval/search calls, tool retries, context tokens, judge calls, latency, and energy are often charged inconsistently. A design can move cost between stages and look like progress.

**3. Longitudinal closed-loop value.** Memory benchmarks still frequently end in QA; retrieval benchmarks end in answers/reports; data-agent benchmarks often end in read-only artifacts. We still lack strong evaluation of **how accumulated context changes future actions over weeks/months**, including writes, permissions, irreversible mistakes, and recovery.

**4. Benchmark validity over time.** Web drift, contamination, benchmark saturation, synthetic-data shortcuts, grader dependence, and environment versioning are increasingly first-order problems. A benchmark needs maintenance, not only publication.

## 📚 Recommended Reading Paths

| If you want to understand… | Read these benchmarks in order | The conceptual shift |
|---|---|---|
| **Why agent memory is more than retrieval** | LoCoMo → LongMemEval → MemoryAgentBench → AMA-Bench → LongMemEval-V2 → LoCoMo-Plus | factual history → update/forget → agent experience → implicit knowledge |
| **How RAG became agentic search** | HotpotQA → KILT → CRAG → BrowseComp → DeepResearch Bench → SGR-Bench → VAKRA | evidence retrieval → freshness → persistent search → state/tool-controlled information seeking |
| **How text-to-SQL became the data-agent problem** | WikiSQL → Spider → BIRD → Spider 2.0 → DAB → DataSpace → DSAgentBench | query generation → enterprise workflow → heterogeneous autonomous data work |

## 🧠 Research Compactions

The daily maintenance task also compacts benchmark changes at multiple time scales:

- **Weekly** — what new evaluation object appeared or what protocol changed.
- **Monthly** — which capabilities are becoming well measured, and where apparent progress is mostly model/harness drift.
- **Yearly** — durable changes in what the community considers a valid evaluation target.

See [`digests/`](digests/).

## Machine-readable Registry

The README is the public entry point; [`data/benchmarks.json`](data/benchmarks.json) is the canonical machine-readable registry. Each record stores capability, environment, protocol, scale, landmark role, measurement strength, coverage gap, confounders, and verified first-party artifacts.

See [`SCHEMA.md`](SCHEMA.md) and [`CURATION.md`](CURATION.md).

## Scope & Contributing

**In scope:** benchmarks that materially define evaluation for agent memory, RAG / search agents, or data agents, plus older precursor/foundation benchmarks needed to understand how today's evaluation targets emerged.

**Not enough for inclusion:** a method paper that merely reports results on existing datasets, or a new dataset that adds examples without changing coverage, realism, diagnostics, or validity.

Corrections are especially welcome for missing landmark benchmarks, benchmark/version lineage, protocol details, evaluator configuration, public artifacts, contamination, benchmark drift, and apples-to-oranges leaderboard comparisons.

**The goal is not the largest benchmark list. It is the shortest list that still explains how the field's definition of progress is changing.**
