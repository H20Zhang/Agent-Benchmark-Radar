# MemProbe: separating valid updates from memory preservation

<!-- RELEASE-REFERENCE:START -->
> **Release result (historical reference; not a best claim)** · 2026-09-24 · paper v1<br>
> **A-MEM (Gemini-3-Flash-preview reader) — Overall probe accuracy: 88.4%**<br>
> Main suite, 56 episodes and 224 probes; A-MEM adapter with Gemini-3-Flash-preview final reader. Selected historical result, not a cross-system best claim. [Original source](https://arxiv.org/abs/2609.30558v1)<br>
> Retrieval budgets, ingestion failures and metadata access differ across adapters; this result establishes neither a causal architecture advantage nor a current leaderboard.
<!-- RELEASE-REFERENCE:END -->

[中文](memprobe-stability-plasticity.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper v1](https://arxiv.org/abs/2609.30558v1) · [Full text](https://arxiv.org/html/2609.30558v1) · [Code and data](https://github.com/jq-ding/MemProbe) · [Pinned implementation notes](https://github.com/jq-ding/MemProbe/blob/9068d8d9a2a47268fe6f7601b99a56a283c37be5/IMPLEMENTATION_DETAILS.md)

## Identity and measurement object

This is Jiaqi Ding and Guorong Wu's *Probing Stability-Plasticity Tradeoffs in Agent Memory through Cognitive Experimental Paradigms*, first submitted on September 24, 2026. It is distinct from [MEMPROBE / MemAudit](memprobe.en.md), Ma et al.'s June work on recovering hidden user state from a final memory artifact. Similar names do not establish a shared benchmark or version lineage.

The reusable contribution is a set of paradigm specifications and a scoring protocol, instantiated in controlled diagnostic suites: should memory accept a legitimate update, retain a fact against unreliable evidence, or preserve its history, source and temporal order? The main suite has 56 episodes, 1,246 sessions and 224 probes, with 14 episodes each for interference, misinformation, consolidation and reconsolidation. It is English text with synthetic/adapted personal, work and tool-state facts. These are controlled episodes, not observed years of real deployment. [Appendix B, Table 8](https://arxiv.org/html/2609.30558v1)

## Compared with what

LongMemEval and MemoryAgentBench already measure updates, temporal behavior and forgetting. This release makes update-versus-preserve behavior and provenance separately inspectable through reusable paradigm specifications and typed probes. It complements MemoryArena's closed-loop action utility rather than replacing it. A new diagnostic coordinate is an early signal; one paper does not justify rewriting a durable area map.

## Evaluation protocol and fair comparison

Each episode starts with a fresh memory store, ingests sessions sequentially, and answers probes with a common Gemini-3-Flash-preview final reader. The reported setup uses Gemini-2.5-Flash for internal memory LLM calls. Typed-field scoring produces overall probe accuracy, plasticity/update accuracy, stability/preservation accuracy, their harmonic balance, and history/source/temporal fidelity. The released bootstrap analysis resamples episodes 2,000 times. [Sections 4.1–4.2 and Appendix C](https://arxiv.org/html/2609.30558v1)

A shared final reader does not equalize the upstream pipeline. Implementation notes pass all final facts for Mem0 and LangMem, top-15 edge facts for Graphiti, top-15 graph context for Cognee, top-15 notes for A-MEM, and top-5 keyword-retrieval evidence for Naive RAG and Time-aware RAG. Embeddings and patches differ. Approximately 178 of roughly 1,100 Graphiti session additions were skipped after malformed-JSON errors. A-MEM also receives session-type tags/categories, a potential metadata advantage requiring audit, not demonstrated leakage. Equal top-k would still not imply equal evidence or token budget. [Pinned adapter details](https://github.com/jq-ding/MemProbe/blob/9068d8d9a2a47268fe6f7601b99a56a283c37be5/IMPLEMENTATION_DETAILS.md)

## Decisive evidence and result boundaries

Table 1 reports A-MEM at 88.4% overall probe accuracy, compared with 88.8% for the full-context reference and 93.3% for Oracle under the main reader. These are reported configurations, not a current leaderboard or universal ceilings. Table 2 reports A-MEM plasticity 91.1%, stability 85.7% and harmonic balance 88.3%; Cognee trades lower plasticity for higher stability. Reader substitutions alter absolute scores and some ordering. [Tables 1–2](https://arxiv.org/html/2609.30558v1)

The [structured source records](../data/results/memprobe-stability-plasticity.json) keep each adapter in a separate single-entry track. They do not label an across-adapter winner. The date is the paper-v1 report date; the experiment execution date is not established. Exact artifact values remain available in the [pinned bootstrap file](https://github.com/jq-ding/MemProbe/blob/9068d8d9a2a47268fe6f7601b99a56a283c37be5/results/suite56/analysis/bootstrap_ci.json). No experiment was independently reproduced here.

## Strongest confounder and remaining gap

A probe failure can come from ingestion, storage, retrieval or answer interpretation. Absence from the retrieved context does not prove absence from storage. Oracle both supplies evidence and removes distractors, so its gain does not cleanly isolate one cause. Correlated paradigm axes and a compact synthetic suite further limit causal attribution.

The separate 40-episode suite jointly changes generator, reader, episode length and fact distribution; its scores must not be pooled with the main suite or presented as a single-factor replication. Main code/suite licensing is MIT; suite40 and derived outputs use CC BY-NC 4.0. Open-world action quality, sustained lifecycle cost and multilingual generalization remain unmeasured.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use it to diagnose valid updating, inappropriate overwriting and provenance retention before treating an aggregate memory score as evidence of trustworthy state management.

### What a concrete task looks like

Illustrative task: a user explicitly changes a work preference, then another session supplies an uncertain contradictory recollection. The system must adopt the valid update without letting the weaker statement overwrite it, while retaining which source changed the state.

### Most discriminating experiment

Fix ingestion success, embeddings, reader, evidence/token budget and metadata access. Compare supplied-correct-evidence, retrieved-evidence and direct-store probes separately. Report update and preservation errors by probe type, along with ingestion failures and bootstrap uncertainty, before making architectural claims.

### Pair with

[LongMemEval](longmemeval.en.md) · [MemoryAgentBench](memoryagentbench.en.md) · [StateMemBench](statemembench.en.md) · [MEMPROBE / MemAudit](memprobe.en.md) · [MemoryArena](memoryarena.en.md)

<!-- RESEARCH-DECISION:END -->

Evidence checked: 2026-09-30. Primary paper and pinned public implementation/result artifacts were inspected; structural validation is not factual certification or independent reproduction.
