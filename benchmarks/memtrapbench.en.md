# MemTrapBench

## What it actually measures

MemTrapBench measures **memory applicability judgment**. Even when a historical memory is faithfully stored and semantically relevant to the current question, can an agent decide whether that memory should still influence reasoning rather than reusing it mechanically? It moves the long-term-memory failure mode from “the system forgot” to “the system remembered correctly but used the memory in the wrong situation.”

## What changed relative to predecessors

LoCoMo and LongMemEval-style benchmarks mainly ask whether historical information can be recalled and used for QA, while staleness benchmarks emphasize choosing the current version under update conflicts. MemTrapBench instead creates cases where the historical content can remain true and relevant in surface semantics but **a changed current context makes it an invalid prior for the present decision**. Retrieval relevance and decision relevance become separate coordinates.

## Decisive evidence

The benchmark pairs the same current task under memory and no-memory conditions across **1,050 multi-turn instances** in four subsets covering reasoning fixation and belief distortion. The paper reports that every tested memory strategy underperforms the no-memory condition, with the largest drop exceeding **10 percentage points**. The signal is not that memory is generally harmful, but that a planted prior can continue to dominate reasoning after a context shift.

## What the score supports

The result supports measurable harm from relevant-but-currently-invalid history under deliberately constructed context shifts. It does not support the claim that long-term memory is worse than no memory on average. Final questions are intentionally solvable without the history, so the no-memory condition avoids the planted prior by construction; in natural workloads, old experience can instead be essential evidence.

## Fair comparison contract

Backbone, current task, historical content, memory visibility, retrieval policy, prompt, judge, and no-memory baseline should be held fixed. A stronger diagnostic should also separate three failures: retrieving irrelevant memory, retrieving relevant memory but applying it incorrectly, and applying appropriate memory but reasoning incorrectly. Final accuracy alone cannot identify whether an applicability mechanism works.

## How to use it in research

MemTrapBench is well suited to **retrieve-then-decide, memory gating, contextual-validity classifiers, and confidence-aware memory use**. A memory system that optimizes only recall and precision can increase harmful exposure; researchers should pair accessibility metrics with harmful-reuse rate and treat **accessibility × applicability** as a two-dimensional evaluation surface.

## Next discriminating validation

The largest missing piece is the real prevalence of harmful reuse in natural workflows and whether agents can infer applicability boundaries autonomously in open environments. A high-value next benchmark would mine natural context shifts from coding, data-agent, or personal-assistant trajectories and compare explicit gating, temporal/version metadata, and pure LLM judgment to see whether gains persist beyond manually planted traps.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use MemTrapBench to study when seemingly relevant memory should not be used. It challenges the assumption that faithful storage and retrieval are always beneficial. Constructed traps establish a possible failure mode, not its frequency in natural workloads.

### What a concrete task looks like

Illustrative task: an earlier task establishes a solving habit or belief, while a similar-sounding new task changes the conditions. Reusing the old lesson can perform worse than no memory. The failure concerns applicability rather than retention.

### Most discriminating experiment

Compare no memory, applicable relevant memory, and similar but inapplicable memory for the same current task with a fixed context budget. Report both positive and negative transfer rather than only rejection. Always disabling memory does not solve selective use.

### Pair with

[locomo-plus](locomo-plus.en.md) · [statemembench](statemembench.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->

## Genealogy

`map_delta=early_signal`. Together with staleness/update benchmarks, it supports a **memory validity before use** direction, but the measured object is different: staleness asks which version is currently valid, while MemTrapBench asks whether a true memory is applicable to the current decision at all. One work is still insufficient to rewrite the durable Benchmark Map.

Primary: https://arxiv.org/abs/2608.20202
