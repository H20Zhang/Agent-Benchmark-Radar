# GroupMemBench: memory in multi-party conversations

[中文](groupmembench.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2605.14498)

## What it actually measures

GroupMemBench evaluates memory in **multi-party conversations** where identity and audience matter. It targets group dynamics, speaker-grounded beliefs, and audience-adapted language, so the same term or proposition can mean different things depending on who said it and who is asking.

## What changed relative to prior evaluation

Most agent-memory systems and benchmarks are dyadic: one user talks to one agent. Concatenating several one-on-one histories does not preserve reply structure, per-speaker beliefs, shared versus private context, or Theory-of-Mind effects. GroupMemBench generates graph-grounded conversations and binds each adversarial query to a specific asker.

## Decisive evidence

The benchmark covers six query categories including multi-hop reasoning, knowledge update, term ambiguity, user-implicit reasoning, temporal reasoning, and abstention. The strongest evaluated memory system reaches only 46.0% average accuracy; knowledge update is 27.1% and term ambiguity 37.7%. A simple BM25 baseline matches or exceeds most agent-memory systems, suggesting current ingestion pipelines erase lexical and structural signals that group memory needs.

## What the score supports

This is strong evidence that **speaker/audience structure is not a cosmetic metadata field**. Still, the benchmark is synthetic and does not isolate whether failure comes from ingestion, indexing, retrieval, or final Theory-of-Mind reasoning.

## Fair comparison contract

Fix conversation graph, speaker identities, asker identity, backbone, retrieval budget, and visible audience metadata. Preserve exact lexical forms when comparing ingestion schemes; summarizing one system's memory more aggressively can destroy the very ambiguity cues being tested.

## What remains unmeasured

Real group spaces include permissions, private threads, changing membership, moderation, and cross-channel identity. Social consequences of exposing one person's belief to another are governance questions beyond answer accuracy.

## Next discriminating validation

Add oracle speaker-aware retrieval and compare raw-message, per-user, thread, and graph memory under the same answer model. This would reveal whether the main loss happens when memories are written or when the model reasons over correctly retrieved social state.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use GroupMemBench for speaker identity, beliefs, and audience conditioning in multi-party interaction. Flattening a group log into one user's memory removes the central variables. A true statement can still fail through incorrect attribution or role-specific terminology.

### What a concrete task looks like

Illustrative task: participants hold different beliefs about a plan, and a term has different meanings across teams. The asker's identity changes the appropriate interpretation. Retrieval must retain speakers, reply relations, and audience context together with content.

### Most discriminating experiment

Keep dialogue text fixed while retaining, hiding, or shuffling roles and reply structure, and score by asker. Failure with correct metadata points to belief reasoning. Benefits restricted to human-provided role labels do not establish autonomous group-memory construction.

### Pair with

[gatemem](gatemem.en.md) · [came-bench](came-bench.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->

## Genealogy

`single-user memory → speaker-grounded group memory → socially governed shared state`

GroupMemBench shows that multi-user memory is not simply more text; it is relational state.