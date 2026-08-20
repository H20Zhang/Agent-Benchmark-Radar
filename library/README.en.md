# Benchmark Library

[中文](README.md) | **English** · [Back to entry](../README.en.md)

Use this library for long-lived questions: **why did a benchmark appear, what predecessor limitation was it reacting to, and which measurement coordinate changed?**

## Frontier Protocol Audits

- [DSAgentBench](../benchmarks/dsagentbench.en.md): real-computer end-to-end data science; the score is system-level evidence over model × harness × tool/OS stack.
- [DataSpace](../benchmarks/dataspace.en.md): heterogeneous workspace + deterministic tabular verification; harness changes materially move scores even with the backbone fixed.
- [VAKRA](../benchmarks/vakra.en.md): API + RAG + policy inside cross-source executable trajectories; composition/grounding is the target, not one retrieval score.
- [LoCoMo-Plus](../benchmarks/locomo-plus.en.md): moves memory evaluation from explicit factual recall toward latent user-constraint consistency.

## Browse by Area

### Agent Memory

`Multi-Session Chat → LoCoMo / LongMemEval → MemoryAgentBench / BEAM → MemoryArena / Mem2ActBench / LoCoMo-Plus / RealMem`

- **Precursor / Foundation:** Multi-Session Chat, LoCoMo, LongMemEval
- **Transition:** MemBench, MemoryAgentBench, BEAM
- **Frontier:** multimodal, acting, persistent-user-state, and project-state benchmarks
- [Continue to Agent Memory Radar](https://github.com/H20Zhang/Agent-Memory-Radar)

### RAG / Agentic Retrieval

`HotpotQA / KILT / BEIR → RGB / RAGTruth / CRAG / BRIGHT → BrowseComp / DeepResearch Bench → SGR-Bench / VAKRA`

- **Foundation:** evidence composition, provenance, cross-domain retrieval
- **Transition:** robustness, faithfulness, reasoning-intensive retrieval, freshness
- **Frontier:** stateful information-environment control and cross-source executable trajectories
- [Continue to Agentic RAG Radar](https://github.com/H20Zhang/Agentic-RAG-Radar)

### Data Agents

`WikiSQL / Spider / DS-1000 → BIRD / MLAgentBench / InsightBench / Spider 2.0 → AgenticDataBench / DataSpace / DSAgentBench`

- **Foundation:** executable NL→SQL and data-science code
- **Transition:** realistic schemas, experimentation, business insight, enterprise workflows
- **Frontier:** heterogeneous workspaces, real computers, end-to-end verification
- [Continue to Data Agent Radar](https://github.com/H20Zhang/Data-Agent-Radar)

## Browse by Genealogy

Genealogy is not a prestige ranking. It asks: **what was insufficient in the previous generation, and which coordinate did the successor make observable?**

| Role | Meaning | How to read it |
|---|---|---|
| `precursor` | Introduced an evaluation object inherited by later agent benchmarks | How was the problem first formalized? |
| `foundation` | Established a durable coordinate system | Which axes did later work implicitly inherit? |
| `transition` | Materially expanded realism, capability, or protocol | Which limitation became explicit? |
| `frontier` | Current time-relative measurement direction | What is the field trying to make observable now? |

See [`data/benchmarks.json`](../data/benchmarks.json) for the canonical structured registry.

## Browse by Measurement Coordinate

- **Capability:** recall, reasoning, action, analysis, tool use, verification
- **Environment:** static corpus, live web, state-gated site, heterogeneous workspace, real computer
- **Protocol:** tool interface, hints, retries, stopping rule, judge, executable validation
- **Validity:** contamination, saturation, judge dependence, harness sensitivity, environment drift
- **Cost:** indexing/writing, retrieval/tool calls, tokens/latency, retries, controller/evaluator cost
- **Long-horizon state:** memory update, workflow state, persistent user/project state, irreversible actions

## Browse by Year

Chronology is mainly for provenance and release lookup. For research understanding, prefer area, genealogy, or measurement coordinate.

- [Research compactions](../digests/README.md)
- [Canonical registry](../data/benchmarks.json)

## Keep one limitation visible

**What benchmarks can measure is not the same as what matters.** If an important research problem lacks a clean benchmark, keep it in the entry page’s poorly-measured section rather than deleting it from the research map.
