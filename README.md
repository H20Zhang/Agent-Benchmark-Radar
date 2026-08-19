# 🧭 Agent Benchmark Radar

**A curated, continuously maintained collection of benchmarks for Agent Memory, RAG / Agentic Retrieval, and Data Agents.**

The goal is not to maximize benchmark count. It is to make the **evaluation coordinate system** easy to inspect: what is measured, under which environment and protocol, and what a score does *not* establish.

⭐ Star this repo to follow new benchmarks, material protocol changes, and benchmark-level research synthesis.

**Last updated:** 2026-08-20 · [New & Notable](#-new--notable) · [Agent Memory](#-agent-memory) · [RAG](#-rag--agentic-retrieval) · [Data Agents](#-data-agents) · [Coverage Gaps](#-coverage-gaps)

> **Evaluation rule:** a higher leaderboard score is system-level evidence unless model, accessible state, tool interface, prompts/hints, retries, stopping rule, evaluator, and relevant cost budgets are sufficiently matched.

## 🔥 New & Notable

| Benchmark | Area | Released | What becomes measurable | Main caveat |
|---|---|---:|---|---|
| [LongMemEval-V2](https://github.com/xiaowu0162/LongMemEval-V2) | Agent Memory | 2026-05 | Memory over accumulated multimodal agent experience, including changing state and workflow knowledge | Still read out mainly through QA rather than future closed-loop task execution |
| [SGR-Bench](https://arxiv.org/abs/2605.22219) | RAG | 2026-05 | Retrieval-state control: filters, hierarchy, scope, and site-specific views | Specialized public-data portals are not a universal proxy for open-web or document RAG |
| [Data Agent Benchmark](https://github.com/ucbepic/DataAgentBench) | Data Agent | 2026-03 | Enterprise analysis across multiple DBMSes, awkward joins, unstructured transformation, and domain knowledge | Model, hints, trials, and harness can dominate leaderboard comparisons |
| [FDABench](https://github.com/fdabench/FDAbench) | Data Agent | 2026 | Heterogeneous analytical workflows with quality, latency, and token-cost signals | Task breadth does not isolate which agent component caused success or failure |
| [AgenticRAGTracer](https://arxiv.org/abs/2602.19127) | RAG | 2026-02 | Hop-level diagnosis of multi-step retrieval/reasoning failures | Generated task structure may introduce synthetic-chain artifacts |

## 🧠 Agent Memory

| Benchmark | Measures | Environment | Evaluation | Why it matters |
|---|---|---|---|---|
| [LongMemEval-V2](https://github.com/xiaowu0162/LongMemEval-V2) | Static/dynamic state, workflow knowledge, environment gotchas, premise awareness | Multimodal web + enterprise trajectories | QA quality + retrieval latency | Moves beyond chat-history recall toward memory over accumulated agent experience |
| [MemoryAgentBench](https://arxiv.org/abs/2507.05257) | Retrieval, conflict resolution, memory update, test-time learning | Incremental multi-turn interactions | Task-specific accuracy | Broadens memory evaluation beyond retrieval from a frozen history |

**Read this section as:** *does the benchmark test storing/recovering past information, or whether experience actually changes future agent behavior?* Most current benchmarks are still stronger on the former.

## 🔎 RAG / Agentic Retrieval

| Benchmark | Measures | Environment | Evaluation | Why it matters |
|---|---|---|---|---|
| [SGR-Bench](https://arxiv.org/abs/2605.22219) | Source discovery + retrieval-state control | Public websites / specialized data portals | Item/row-level answer quality | Separates finding a source from configuring the source into the right retrievable state |
| [AgenticRAGTracer](https://arxiv.org/abs/2602.19127) | Multi-hop retrieval + intermediate reasoning | Multi-domain corpora | Final answer + hop-level validation | Makes intermediate failure locations observable rather than collapsing everything into final accuracy |
| [RAGCap-Bench](https://arxiv.org/abs/2510.13910) | Intermediate agentic-RAG capabilities | Capability-oriented RAG tasks | Capability-level scores | Tests whether prerequisite skills exist before asking whether the full RAG system succeeds |

**Read this section as:** *is the benchmark testing retrieval quality, retrieval control, or the full agent loop?* Those are different objects and should not share a leaderboard interpretation by default.

## 🗃️ Data Agents

| Benchmark | Measures | Environment | Evaluation | Why it matters |
|---|---|---|---|---|
| [Data Agent Benchmark](https://github.com/ucbepic/DataAgentBench) | Multi-database integration, schema navigation, joins, transformations, domain reasoning | DuckDB, PostgreSQL, SQLite, MongoDB, Python | Executable validation / repeated trials | Pushes data-agent evaluation beyond text-to-SQL and single-database assumptions |
| [FDABench](https://github.com/fdabench/FDAbench) | Planning, tool use, heterogeneous analysis, report generation | SQL engines + unstructured sources | Accuracy/rubric + latency + token cost | Treats analytical agents as end-to-end systems rather than SQL generators |

**Read this section as:** *does the benchmark require semantic data work across sources, or mostly query generation?* The former is closer to the data-agent systems problem.

## 🧩 How This Radar Classifies Benchmarks

| Axis | Question | Examples |
|---|---|---|
| **Capability** | What internal ability must succeed? | retrieval, state tracking, conflict resolution, planning, joins, verification |
| **Environment** | What information substrate does the agent act over? | conversation history, multimodal trajectories, websites, multiple databases, mixed structured/unstructured data |
| **Protocol** | What can the agent observe/do, and what is scored? | final answer, executable output, intermediate states, trajectory quality, latency, token/tool cost, repeated trials |

The topical label is deliberately secondary. Two “memory benchmarks” can be scientifically less comparable than a memory benchmark and a retrieval benchmark if their environment and protocol assumptions differ.

## 🕳️ Coverage Gaps

- **Closed-loop value:** memory is commonly evaluated by asking about the past; fewer benchmarks test whether retained experience improves future actions under matched budgets.
- **Lifecycle cost:** ingestion/indexing/memory writing, retrieval/tool calls, retries, generation, and evaluator cost are rarely accounted for together.
- **Harness sensitivity:** model, prompt, tools, hints, retries, stopping rules, and judge often move with the method, making component attribution weak.

These gaps are tracked because the most useful next benchmark is not necessarily a larger one; it is the one that removes a decision-relevant ambiguity.

## 🧠 Research Compactions

Benchmark changes are compacted over time rather than left as a growing flat list:

- **Weekly:** genuinely new evaluation targets, protocol changes, and newly exposed validity problems.
- **Monthly:** capability coverage, benchmark convergence/divergence, saturation, and harness/model drift.
- **Yearly:** durable changes in what the field treats as a valid evaluation target.

Browse [`digests/`](digests/) as reports accumulate.

## 📦 Machine-Readable Registry

The README is the public surface. [`data/benchmarks.json`](data/benchmarks.json) is the canonical machine-readable registry used to keep entries consistent and auditable.

For inclusion rules and field definitions, see [`CURATION.md`](CURATION.md) and [`SCHEMA.md`](SCHEMA.md).

## Contributing

Corrections and additions are welcome when they improve **comparability**: benchmark scope, protocol details, evaluator/judge configuration, public artifacts, contamination concerns, version changes, or apples-to-oranges leaderboard comparisons.

A paper is not added merely because it evaluates on Agent Memory, RAG, or Data Agent tasks. The benchmark/evaluation contribution itself must be reusable.
