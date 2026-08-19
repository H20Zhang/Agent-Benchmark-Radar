# 🧭 Agent Benchmark Radar

**A living map of benchmarks for Agent Memory, RAG / Agentic Retrieval, and Data Agents.**

Use it in two directions: **Latest → what the field is starting to care about now**, and **Foundation → how the definition of progress got here**.

⭐ **Star this repo to follow new benchmarks, benchmark revisions, and shifts in what the field considers worth measuring.**

**Last updated:** 2026-08-20 · [New & Notable](#-new--notable) · [Field Evolution](#-what-benchmark-evolution-says-about-the-field) · [Memory](#-agent-memory) · [RAG](#-rag--agentic-retrieval) · [Data Agents](#-data-agents)

> **Core idea:** a new benchmark is often a critique of the previous generation. The interesting question is not only *who scores highest?* but **what did the old benchmark fail to measure badly enough that a new one had to exist?**

> **Comparison rule:** a higher leaderboard score is system-level evidence unless model, accessible state, tool interface, prompts/hints, retries, stopping rule, evaluator, and relevant cost budgets are sufficiently matched.

## 🔥 New & Notable

These are the newest benchmarks that materially change the evaluation object—not simply new datasets with more examples.

| Benchmark | Area | Released | What is newly exposed | Signal for the field |
|---|---|---:|---|---|
| [VAKRA](https://arxiv.org/abs/2608.12282) | RAG / Agents | 2026-08 | **Executable APIs + retrieved documents + tool-use policies** in one trajectory | Retrieval is becoming a cross-source execution problem, not a text-search primitive |
| [DSAgentBench](https://arxiv.org/abs/2608.10366) | Data Agent | 2026-08 | Full data-science workflows inside a **real computer environment** | Data-agent evaluation is moving from answer/code quality to grounded multi-tool execution |
| [DataSpace](https://arxiv.org/abs/2608.03451) | Data Agent | 2026-08 | Verifiable analytics over DBs, files, documents, and multimedia | Heterogeneous evidence discovery + deterministic output checking is becoming central |
| [LoCoMo-Plus](https://aclanthology.org/2026.acl-long.1150/) | Agent Memory | 2026-07 | Applying **latent user constraints** when later cues do not restate them | Memory is moving beyond explicit factual recall toward persistent user-state |
| [Mem2ActBench](https://aclanthology.org/2026.acl-long.370/) | Agent Memory | 2026-07 | Long-term memory used to select tools and ground parameters | Memory is finally being evaluated by whether it changes **action**, not only answers |
| [RealMem](https://aclanthology.org/2026.findings-acl.703/) | Agent Memory | 2026-07 | Evolving project state across long-running, cross-session interactions | Long-term memory is moving from casual conversation to persistent project work |
| [AgenticDataBench](https://arxiv.org/abs/2607.01647) | Data Agent | 2026-07 | Fine-grained **data-science skill coverage** | Aggregate task success is no longer enough; benchmark coverage itself is becoming auditable |
| [LifeSide](https://arxiv.org/abs/2606.04660) | Agent Memory | 2026-06 | Memory–emotion–environment loops, privacy control, persistent user models | Memory is becoming part of a broader lifelong-user model |
| [SGR-Bench](https://arxiv.org/abs/2605.22219) | RAG / Search | 2026-05 | **Retrieval-state control**: filters, hierarchy, scope, site-specific views | Reaching the right source is no longer equivalent to retrieving the right evidence |
| [LongMemEval-V2](https://arxiv.org/abs/2605.12493) | Agent Memory | 2026-05 | Memory over accumulated **agent-environment experience** | Memory is shifting from conversation history toward reusable workflow/environment experience |

## 🧬 What Benchmark Evolution Says About the Field

Read each arrow as: *the previous evaluation target became too easy, too narrow, too static, or too weakly diagnosed*.

| Area | Evolution | What the field increasingly cares about |
|---|---|---|
| **Agent Memory** | multi-session recall → temporal/update/forget → structure & scale → multimodal/trajectory memory → **memory-guided action & implicit user state** | Not merely *can I retrieve an old fact?*, but **what should be written, updated, structured, forgotten, inferred, and applied to future behavior?** |
| **RAG / Search** | retrieval quality → RAG robustness/faithfulness → multi-hop & dynamic facts → persistent/deep web research → **controlled, stateful, cross-source execution** | Retrieval intelligence is moving from ranking documents toward **controlling an information environment under changing state, tools, and budgets** |
| **Data Agents** | NL→SQL → cross-schema/large DBs → code & experimentation → enterprise workflows → heterogeneous analytics → **real-computer data science** | The target is moving from query generation toward **autonomous data work: discover, transform, join, analyze, verify, and communicate** |

### Legend

`🌱 Precursor` introduced an evaluation object inherited by later agent benchmarks · `🧱 Foundation` established a durable coordinate system · `↗ Transition` materially expanded realism/capability coverage · `🔭 Frontier` reflects a current direction and is intentionally time-relative.

---

## 🧠 Agent Memory

### Evolution in one line

**Multi-Session Chat → LoCoMo / LongMemEval** established long-term conversation and decomposed recall/time/update → **MemBench / MemoryAgentBench / BEAM** made memory more online, multi-aspect, and scalable → **Mem-Gallery / MemEye / StructMemEval / AMA-Bench / LongMemEval-V2** broadened representation, modality, and agent experience → **MemoryArena / Mem2ActBench / LoCoMo-Plus / RealMem** ask whether remembered experience actually changes future decisions, tool use, user consistency, and project state.

| Role | Benchmark | Year | What it actually measures | Why it changed the question |
|---|---|---:|---|---|
| 🌱 | [Multi-Session Chat / Beyond Goldfish Memory](https://aclanthology.org/2022.acl-long.356/) | 2022 | Human-human conversation resumed across sessions; recall and consistency about prior interactions | Established cross-session conversation as a distinct long-term-memory setting |
| 🧱 | [LoCoMo](https://aclanthology.org/2024.acl-long.747/) | 2024 | Very-long multi-session memory; QA, event summarization, multimodal dialogue | Made very-long conversational memory a reusable benchmark coordinate system |
| 🧱 | [LongMemEval](https://arxiv.org/abs/2410.10813) | 2024 | Extraction, multi-session reasoning, temporal reasoning, **knowledge update**, abstention | Showed that “remembering” contains qualitatively different operations |
| ↗ | [MemBench](https://aclanthology.org/2025.findings-acl.989/) | 2025 | Factual vs reflective memory; participation vs observation; effectiveness, efficiency, capacity | Expanded evaluation beyond one accuracy number and one interaction regime |
| ↗ | [MemoryAgentBench](https://arxiv.org/abs/2507.05257) | 2025 / ICLR'26 | Retrieval, test-time learning, long-range understanding, selective forgetting under incremental interaction | Treats memory as an **online process**, not a frozen context |
| ↗ | [BEAM](https://arxiv.org/abs/2510.27246) | 2025 | Coherent conversational memory from 1M toward 10M tokens | Makes degradation at truly massive horizons directly visible |
| 🔭 | [Mem-Gallery](https://aclanthology.org/2026.acl-long.1892/) | 2026 | Multimodal memory extraction/adaptation, reasoning, and knowledge management across sessions | Makes **visual retention and organization** a first-class long-term memory requirement |
| 🔭 | [StructMemEval](https://arxiv.org/abs/2602.11243) | 2026 | Whether an agent maintains useful structures such as ledgers, lists, and trees | Asks whether **organization** itself is a memory capability |
| 🔭 | [MemoryArena](https://arxiv.org/abs/2602.16313) | 2026 | Interdependent multi-session agent tasks where earlier experience must guide later actions | Directly couples memorization with **future action** rather than testing them separately |
| 🔭 | [AMA-Bench](https://arxiv.org/abs/2602.22769) | 2026 | Memory over real + scalable synthetic **agent-environment trajectories** | Moves from dialogue-centric memory toward causality and machine-generated experience |
| 🔭 | [LifeBench](https://arxiv.org/abs/2603.03781) | 2026 | Declarative + non-declarative memory including habitual/procedural knowledge | Explicit facts are no longer assumed to be the whole memory problem |
| 🔭 | [LongMemEval-V2](https://arxiv.org/abs/2605.12493) | 2026 | State, workflow knowledge, environment gotchas, premise awareness from huge trajectory histories | “Experienced colleague” knowledge becomes the target rather than user-history recall |
| 🔭 | [MemEye](https://arxiv.org/abs/2605.15128) | 2026 | Fine-grained visual evidence and temporal visual-state synthesis with shortcut/visual-necessity checks | Forces memory systems to preserve **genuinely necessary visual evidence**, not captions alone |
| 🔭 | [LifeSide](https://arxiv.org/abs/2606.04660) | 2026 | Persistent user understanding, privacy control, emotion/environment dynamics | Couples memory with an evolving user model rather than scoring recall in isolation |
| 🔭 | [RealMem](https://aclanthology.org/2026.findings-acl.703/) | 2026 | Long-running project state and evolving goals across sessions | Moves memory from casual dialogue toward persistent project-oriented interaction |
| 🔭 | [Mem2ActBench](https://aclanthology.org/2026.acl-long.370/) | 2026 | Memory used proactively for tool selection and parameter grounding | Makes **action-level memory utilization** directly measurable |
| 🔭 | [LoCoMo-Plus](https://aclanthology.org/2026.acl-long.1150/) | 2026 | Latent user constraints under cue–trigger semantic disconnect | Pushes memory from explicit facts toward **cognitive consistency** |

**Current memory signal:** the frontier is no longer one-dimensional. It now separates **write/update/forget**, **organization**, **multimodal fidelity**, **agent experience**, **procedural knowledge**, **persistent user state**, and increasingly **memory-guided action**. The next hard step is longitudinal causality in truly persistent environments: matched cost/context budgets, irreversible actions, permissions, failure recovery, and weeks/months of state evolution.

---

## 🔎 RAG / Agentic Retrieval

### Evolution in one line

**HotpotQA / KILT / BEIR** established evidence composition, provenance, and robust retrieval → **RGB / RAGTruth / MultiHop-RAG / CRAG / BRIGHT** separated robustness, faithfulness, reasoning-intensive retrieval, multi-hop, and freshness → **BrowseComp / DeepResearch Bench** moved toward persistent information seeking and research artifacts → **BrowseComp-Plus / RAGCap / AgenticRAGTracer / SGR-Bench / VAKRA** make reproducibility, intermediate diagnosis, environment state, and cross-source execution first-class.

| Role | Benchmark | Year | What it actually measures | Why it changed the question |
|---|---|---:|---|---|
| 🌱 | [HotpotQA](https://aclanthology.org/D18-1259/) | 2018 | Multi-document evidence retrieval/reasoning with supporting facts | Made evidence composition and supporting-fact supervision central to multi-hop QA |
| 🧱 | [KILT](https://arxiv.org/abs/2009.02252) | 2020 | Knowledge-intensive tasks on one shared Wikipedia snapshot with provenance | Established that correctness **and where evidence came from** should be evaluated together |
| 🧱 | [BEIR](https://arxiv.org/abs/2104.08663) | 2021 | Zero-shot retrieval generalization across heterogeneous domains/tasks | Made cross-domain robustness more important than winning one IR dataset |
| 🧱 | [RGB](https://arxiv.org/abs/2309.01431) | 2023 | Noise robustness, negative rejection, information integration, counterfactual robustness | Decomposed **using retrieved context correctly** into distinct RAG abilities |
| ↗ | [RAGTruth](https://arxiv.org/abs/2401.00396) | 2024 | Case- and word-level hallucinations in RAG outputs | Made fine-grained grounding/faithfulness under retrieved context directly measurable |
| ↗ | [MultiHop-RAG](https://arxiv.org/abs/2401.15391) | 2024 | Retrieval + reasoning over multiple supporting pieces inside a RAG pipeline | Exposed single-shot retrieval as insufficient for compositional questions |
| ↗ | [CRAG](https://arxiv.org/abs/2406.04744) | 2024 | Dynamic factual QA, long-tail entities, web/KG retrieval, hallucination | Brought **freshness and factual dynamism** into mainstream RAG evaluation |
| ↗ | [RAGBench](https://arxiv.org/abs/2407.11005) | 2024 | Explainable labels/evaluators for retrieval and generation quality | Made the **quality of the RAG evaluator** itself a benchmark problem |
| ↗ | [BRIGHT](https://arxiv.org/abs/2407.12883) | 2024 | Retrieval where identifying relevant documents itself requires substantial reasoning | Shows semantic similarity alone under-tests real retrieval difficulty |
| ↗ | [BrowseComp](https://arxiv.org/abs/2504.12516) | 2025 | Persistent live-web browsing for hard-to-find answers | Shifted from “retrieve a passage” to **keep searching until obscure evidence is found** |
| ↗ | [DeepResearch Bench](https://arxiv.org/abs/2506.11763) | 2025 | Multi-step web research, citations, and long-form synthesis | Raised the target from answer retrieval to analyst-style research reports |
| ↗ | [BrowseComp-Plus](https://arxiv.org/abs/2508.06600) | 2025 | BrowseComp-style deep research over a fixed corpus with verified positives and hard negatives | Explicitly fixes **fairness, reproducibility, and retriever attribution** problems of black-box live search |
| 🔭 | [RAGCap-Bench](https://arxiv.org/abs/2510.13910) | 2025 | Intermediate capabilities inside agentic-RAG workflows | Final-answer accuracy is no longer sufficient for diagnosis |
| 🔭 | [AgenticRAGTracer](https://arxiv.org/abs/2602.19127) | 2026 | Hop-level validation and step allocation in multi-step retrieval reasoning | Makes failure location inside a retrieval trajectory observable |
| 🔭 | [SGR-Bench](https://arxiv.org/abs/2605.22219) | 2026 | Search when evidence is gated behind site-specific filters/views/scopes | Makes **environment state configuration** part of retrieval competence |
| 🔭 | [VAKRA](https://arxiv.org/abs/2608.12282) | 2026 | Executable APIs + document retrieval + multi-hop reasoning + policy constraints | Pushes retrieval into **cross-source tool execution** with coherent grounding across access modes |

**Current RAG signal:** “retrieval” is expanding from a model primitive into a **control problem over an information environment**. Meanwhile, BrowseComp → BrowseComp-Plus exposes a second trend: the field increasingly cares not only about realism, but about **experimental identifiability**—can we tell whether a gain came from the model, retriever, corpus, interface, or search budget? citeturn871211view4

---

## 🗄️ Data Agents

### Evolution in one line

**WikiSQL / Spider / DS-1000** established executable language→SQL/code → **BIRD / MLAgentBench / InsightBench / DA-Code / Spider 2.0** introduced realistic database content, experimentation, business insight, grounded code, metadata, and enterprise workflows → **DataSciBench / FDABench / DAComp / DAB / AgenticDataBench / DataSpace / DSAgentBench** broaden toward the whole data-intelligence lifecycle, heterogeneous workspaces, capability coverage, and real-computer execution.

| Role | Benchmark | Year | What it actually measures | Why it changed the question |
|---|---|---:|---|---|
| 🌱 | [WikiSQL](https://arxiv.org/abs/1709.00103) | 2017 | NL→SQL over single Wikipedia tables with execution accuracy | Established executable natural-language database access at large scale |
| 🧱 | [Spider](https://aclanthology.org/D18-1425/) | 2018 | Complex multi-table SQL and generalization to **unseen schemas** | Became the canonical cross-domain text-to-SQL coordinate system |
| 🧱 | [DS-1000](https://arxiv.org/abs/2211.11501) | 2022 | Data-science code generation across seven Python libraries with execution tests | Added executable data-science programming as a foundation beyond SQL |
| ↗ | [BIRD](https://arxiv.org/abs/2305.03111) | 2023 | Large real DBs, dirty values, external knowledge, SQL efficiency | Moves text-to-SQL closer to real database contents and operational efficiency |
| ↗ | [MLAgentBench](https://arxiv.org/abs/2310.03302) | 2023 | Agents iteratively design, run, inspect, and improve ML experiments | Makes **scientific experimentation** an agent task rather than code generation |
| ↗ | [InsightBench](https://arxiv.org/abs/2407.06423) | 2024 | End-to-end business analytics: formulate questions, extract insights, recommend actions | Moves evaluation from answering a query to **discovering useful analysis** |
| ↗ | [DA-Code](https://arxiv.org/abs/2410.07331) | 2024 | Grounded, executable data wrangling/analytics code requiring planning | Bridges static code generation and agent-style data-science work |
| ↗ | [Spider 2.0](https://arxiv.org/abs/2411.07763) | 2024 | Enterprise SQL workflows, huge schemas, metadata/docs/code search, multiple dialects | Turns text-to-SQL into a **long-horizon enterprise workflow** |
| ↗ | [DataSciBench](https://arxiv.org/abs/2502.13897) | 2025 | Broader data-science prompts with task-specific programmatic evaluation | Expands the object beyond SQL toward heterogeneous analytical work |
| 🔭 | [FDABench](https://arxiv.org/abs/2509.02473) | 2025 / KDD'26 | Multi-source analytical tasks over structured, unstructured, web, and multimodal data | Makes heterogeneous analysis, traces, latency, and token cost visible together |
| 🔭 | [DAComp](https://arxiv.org/abs/2512.04324) | 2025 | Repository-level data engineering + open-ended data analysis | Covers the **full data-intelligence lifecycle** instead of only analysis/querying |
| 🔭 | [Data Agent Benchmark (DAB)](https://arxiv.org/abs/2603.20576) | 2026 | Enterprise questions across multiple DBMSes, awkward joins, text transforms, domain knowledge | Evaluates integration→transformation→analysis rather than isolated query translation |
| 🔭 | [AgenticDataBench](https://arxiv.org/abs/2607.01647) | 2026 | Realistic workflows with a fine-grained taxonomy of data-science skills | Makes **skill coverage** itself auditable |
| 🔭 | [DataSpace](https://arxiv.org/abs/2608.03451) | 2026 | Verifiable analytics over CSV/JSON/DB/docs/PDF/video workspaces | Unifies heterogeneous evidence discovery with deterministic complete-result checking |
| 🔭 | [DSAgentBench](https://arxiv.org/abs/2608.10366) | 2026 | End-to-end data-science lifecycle inside notebooks, IDEs, terminals, browsers, and DBs | Puts agents in a **real computer** and evaluates multi-stage tool orchestration |

**Current data-agent signal:** text-to-SQL is becoming a substrate, not the end task. The emerging target is an agent that can **discover data, understand semantics, engineer/transform sources, iteratively analyze intermediate results, execute heterogeneous tools, verify outputs, and communicate useful artifacts**. The new tension is realism vs attribution: more realistic environments expose the actual workflow, but also make results increasingly harness- and environment-sensitive. citeturn850939academia2turn850939academia3turn871211view7

---

## 🕳️ What Is Still Poorly Measured

**1. Component causality under matched harnesses.** Most leaderboards still change model, prompts, tools, retries, memory/retrieval implementation, and budgets together. They tell us which *system* won, much less often *why*.

**2. Lifecycle resource cost.** Memory writing/indexing, retrieval/search calls, tool retries, context tokens, judge calls, latency, and energy are charged inconsistently. A design can move cost between stages and look like progress.

**3. Truly longitudinal closed-loop value.** MemoryArena and Mem2ActBench are important because they begin to couple memory with later action, but the field still lacks strong evaluation over **weeks/months of persistent state**, permissions, writes, irreversible mistakes, recovery, and shared resource budgets. citeturn488253view0turn871211view0

**4. Benchmark validity over time.** Web drift, contamination, saturation, synthetic-data shortcuts, grader dependence, and environment versioning are increasingly first-order problems. BrowseComp-Plus is a useful signal that **benchmark controllability itself** is becoming a research concern. citeturn871211view4

## 📚 Recommended Reading Paths

| If you want to understand… | Read these benchmarks in order | The conceptual shift |
|---|---|---|
| **Why agent memory is more than retrieval** | Multi-Session Chat → LoCoMo → LongMemEval → MemoryAgentBench → MemoryArena → Mem2ActBench → LoCoMo-Plus | conversation recall → update/forget → experience → action → latent user state |
| **How RAG became agentic information seeking** | HotpotQA → KILT → RGB → CRAG → BrowseComp → BrowseComp-Plus → DeepResearch Bench → SGR-Bench → VAKRA | evidence → robust use → freshness → persistent search → controlled experiments → state/tool-controlled retrieval |
| **How text-to-SQL became the data-agent problem** | WikiSQL → Spider → BIRD → MLAgentBench / InsightBench → Spider 2.0 → DAComp / DAB → DataSpace → DSAgentBench | query generation → real data → iterative work → enterprise workflow → heterogeneous autonomous data work |

## 🧠 Research Compactions

The daily maintenance task compacts benchmark changes at multiple time scales:

- **Weekly** — what new evaluation object appeared, what benchmark was revised, and what old assumption it attacks.
- **Monthly** — which capabilities are becoming well measured, where realism is increasing, and where apparent progress is mostly model/harness drift.
- **Yearly** — durable changes in what the community considers a valid evaluation target and which former frontier benchmarks became foundations.

See [`digests/`](digests/).

## Machine-readable Registry

[`data/benchmarks.json`](data/benchmarks.json) stores structured benchmark metadata used by maintenance and synthesis: capability, environment, protocol, scale, evolution role, measurement strength, coverage gap, confounders, and verified first-party artifacts.

See [`SCHEMA.md`](SCHEMA.md) and [`CURATION.md`](CURATION.md).

## Scope & Contributing

**In scope:** benchmarks that materially define evaluation for agent memory, RAG / search agents, or data agents, plus older precursor/foundation benchmarks needed to understand how today's evaluation targets emerged.

**Not enough for inclusion:** a method paper that merely reports results on existing datasets, or a new dataset that adds examples without changing coverage, realism, diagnostics, reproducibility, or validity.

Corrections are especially welcome for missing landmark benchmarks, benchmark/version lineage, protocol details, evaluator configuration, public artifacts, contamination, benchmark drift, and apples-to-oranges leaderboard comparisons.

**The goal is not the largest benchmark list. It is the shortest list that still explains how the field's definition of progress is changing.**
