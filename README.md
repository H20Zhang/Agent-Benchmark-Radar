# 🧭 Agent Benchmark Radar

**A living research map of benchmarks for Agent Memory, RAG, and Data Agents.**  
Track new benchmarks, understand what they actually measure, and see where current evaluation still gives a misleading picture of agent capability.

⭐ **Star this repo to follow new benchmarks, protocol changes, and evaluation-level research synthesis.**

**Last updated:** 2026-08-19 · [Latest Benchmarks](#-latest-benchmarks) · [Benchmark Map](#-benchmark-map) · [What Is Actually Measured](#-what-is-actually-measured) · [Coverage Gaps](#-coverage-gaps)

> **Current thesis:** agent evaluation is bottlenecked less by the number of benchmarks than by **measurement validity**. Two benchmarks with similar labels can test very different things because the environment, accessible state, tool interface, judge, cost budget, and temporal horizon differ. This Radar treats those choices as first-class data.

## 🔥 Latest Benchmarks

### [LongMemEval-V2](https://github.com/xiaowu0162/LongMemEval-V2)
`Agent Memory` · `agentic experience` `multimodal trajectories` `long horizon` · **★★★★★** · 2026

**Why it matters:** moves long-term memory evaluation from conversational recall toward memory over accumulated agent experience in customized environments. It tests static state, dynamic state, workflows, environment-specific gotchas, and premise awareness over histories that can scale to very large trajectory collections.

**Do not over-read:** it still evaluates memory through downstream question answering rather than full closed-loop future task execution.

### [SGR-Bench](https://arxiv.org/abs/2605.22219)
`RAG / Search Agent` · `state-gated retrieval` `web tools` `structured answers` · **★★★★★** · 2026-05

**Why it matters:** separates “finding the right source” from “establishing the right retrieval state.” Filters, hierarchy, scope, and site-specific views become part of retrieval competence rather than invisible interface details.

**Do not over-read:** it targets a specific but important retrieval regime; gains here do not automatically imply better open-web research or generic document RAG.

### [Data Agent Benchmark (DAB)](https://github.com/ucbepic/DataAgentBench)
`Data Agent` · `multi-database` `heterogeneous data` `enterprise analysis` · **★★★★★** · 2026-03

**Why it matters:** stresses realistic enterprise data work across multiple databases, awkward joins, unstructured transformations, and domain knowledge instead of reducing the data-agent problem to text-to-SQL.

**Do not over-read:** leaderboard comparisons must account for model choice, hints, number of trials, and agent harness.

### [FDABench](https://github.com/fdabench/FDAbench)
`Data Agent` · `heterogeneous analytics` `reports` `cost/latency` · **★★★★☆** · 2026

**Why it matters:** expands evaluation across heterogeneous analytical workloads and multiple task forms, while exposing accuracy together with execution cost and latency.

**Do not over-read:** a large task count does not by itself guarantee broad causal coverage of planning, tool selection, semantic interpretation, and error recovery.

### [AgenticRAGTracer](https://arxiv.org/abs/2602.19127)
`RAG` · `multi-hop` `hop-level diagnosis` `reasoning trajectory` · **★★★★☆** · 2026-02

**Why it matters:** adds intermediate hop-level validation, allowing failure localization beyond final-answer accuracy.

**Do not over-read:** automatically generated benchmark structure can itself introduce artifacts; diagnostic resolution is only useful when hop annotations correspond to meaningful causal steps.

### [RAGCap-Bench](https://arxiv.org/abs/2510.13910)
`RAG` · `capability decomposition` `intermediate tasks` · **★★★★☆** · 2025-10

**Why it matters:** asks whether an agent has the intermediate capabilities needed by agentic RAG workflows rather than only whether the final answer is correct.

**Do not over-read:** capability scores are not equivalent to end-to-end system quality unless the mapping from intermediate skill to realized agent behavior is validated.

### [MemoryAgentBench](https://arxiv.org/abs/2507.05257)
`Agent Memory` · `incremental interaction` `retrieval` `conflict resolution` `test-time learning` · **★★★★☆** · 2025-07

**Why it matters:** broadens memory beyond static retrieval by evaluating memory formation and use across incremental multi-turn interactions.

**Do not over-read:** different memory systems can still look incomparable if the surrounding LLM, embeddings, answerer, or judge are not normalized.

## 🗺️ Benchmark Map

| Area | Benchmark | Primary object being tested | Environment / substrate | Evaluation signal | Main confounder to watch |
|---|---|---|---|---|---|
| Agent Memory | LongMemEval-V2 | memory over accumulated agent experience | multimodal web/enterprise trajectories | answer quality + retrieval latency | QA proxy vs future task execution |
| Agent Memory | MemoryAgentBench | remembering, updating, resolving, adapting | incremental interactions | task-specific accuracy | harness/model normalization |
| RAG | SGR-Bench | retrieval-state control | public data websites | item/row-level answer quality | site-interface specificity |
| RAG | AgenticRAGTracer | multi-hop retrieval reasoning | constructed multi-domain corpora | final + hop-level correctness | synthetic-chain artifacts |
| RAG | RAGCap-Bench | intermediate agentic-RAG capabilities | capability-oriented tasks | capability scores | mapping to end-to-end behavior |
| Data Agent | DAB | enterprise data-question answering | multiple DBMSes + heterogeneous sources | pass@1 / executable validation | trials, hints, harness, model |
| Data Agent | FDABench | heterogeneous analytical workflows | databases + unstructured sources | accuracy/rubric + cost/latency | task diversity ≠ causal coverage |

## 🔬 What Is Actually Measured

A benchmark is described along three independent axes rather than by a single topical label:

**Capability** — retrieval, state tracking, temporal reasoning, conflict resolution, workflow learning, planning, cross-source joins, semantic interpretation, execution, verification, recovery, or adaptation.

**Environment** — static corpus, evolving conversation, multimodal trajectory history, public website, multi-database enterprise environment, code execution sandbox, or mixed structured/unstructured workspace.

**Protocol** — what the agent can observe and do; whether evaluation checks final answers, intermediate states, executable outputs, trajectories, latency, token/tool cost, robustness, or repeated trials; and whether an LLM judge is involved.

This separation is intentional. “Agent memory benchmark” and “RAG benchmark” are often too coarse to support a scientific comparison.

## 🕳️ Coverage Gaps

**1. Closed-loop value of memory.** Many memory benchmarks still ask questions about past experience. The harder systems question is whether stored experience improves *future action* under matched context, latency, and cost budgets.

**2. Lifecycle cost accounting.** Evaluation often measures answer accuracy while ignoring ingestion, indexing, memory writing, retrieval, tool calls, retries, and judge cost. A system can move cost between stages without becoming more efficient.

**3. Harness sensitivity.** Agent benchmarks frequently entangle the model, prompt, tool interface, stopping rules, retries, hints, and memory/retrieval component. A leaderboard movement is not automatically evidence that the named component improved.

## 🧠 Research Compactions

This repository will maintain benchmark-level synthesis at multiple time scales:

- **Weekly:** newly released benchmarks, material protocol changes, and newly exposed measurement blind spots.
- **Monthly:** which capabilities are becoming well measured, which benchmark families are converging, and which apparent progress is mostly harness/model drift.
- **Yearly:** durable shifts in what the community considers a valid evaluation target.

See [`digests/`](digests/) as these reports accumulate.

## 📐 Curation Principle

A benchmark belongs here when it provides a reusable evaluation coordinate system, not merely an experiment section. Priority goes to work with public task definitions, data or executable environments, reproducible metrics, clear baselines, and enough protocol detail to diagnose what a score means.

We track **relevance** separately from **importance**. A benchmark may be in scope yet low-impact if it mostly repackages an existing task under a new name.

See [`CURATION.md`](CURATION.md), [`SCHEMA.md`](SCHEMA.md), and [`data/benchmarks.json`](data/benchmarks.json).

## Scope

**In scope:** agent memory, long-term memory, RAG and agentic retrieval, search agents when retrieval behavior is the evaluated object, data agents, semantic data analysis, database/data-science agents, and evaluation suites that directly expose important measurement assumptions in these areas.

**Out of scope by default:** generic reasoning leaderboards, generic coding agents, benchmarks where retrieval/memory/data interaction is incidental, and papers that only evaluate a proposed method on existing datasets without contributing a reusable benchmark or materially changed protocol.

## Contributing

Corrections are especially welcome for benchmark scope, protocol details, judge configuration, public artifacts, contamination concerns, and apples-to-oranges leaderboard comparisons. The goal is not to maximize benchmark count; it is to make benchmark claims auditable.
