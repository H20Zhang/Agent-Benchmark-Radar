# InMind: when relevant memory is not similar to the query

[中文](inmind.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2607.24368) · [Project](https://keep-it-inmind.github.io/) · [Code](https://github.com/imlrz/InMind)

## What it actually measures

InMind targets an **implicit-association retrieval blind spot**: the memory that matters for a query may be semantically dissimilar to the query, and its relevance becomes visible only after combining the personal fact with outside world knowledge. The benchmark therefore separates “the model could use this memory if shown” from “the memory system can discover that it should be shown.”

## What changed relative to prior evaluation

Most memory retrieval is query-conditioned by lexical or embedding similarity, and many benchmarks reward direct fact recall. InMind creates paired direct and indirect controls over the same underlying personal facts. The indirect version requires an association such as a preference or constraint becoming relevant through external knowledge rather than surface similarity.

## Decisive evidence

The suite contains 125 expert-verified tasks across 10 domains, with 113 tasks grounded in public sources. When the decisive memory is placed directly in context, the backbone answers 84.0% of indirect questions; when a memory system must retrieve it, six vector-, graph-, and agentic-memory approaches reach at most 14.4%, while direct recall can reach 100%. A diagnostic probe that keeps the memory visible recovers most of the gap.

## What the score supports

This is unusually strong evidence that the bottleneck can lie in the **query-to-memory interface**, not storage capacity or answer reasoning. It still does not prove that similarity retrieval should be discarded: the benchmark is constructed specifically around cases where similarity is insufficient.

## Fair comparison contract

Use the same background memory trace, backbone, world-knowledge access, retrieval budget, and paired direct/indirect tasks. Report oracle-in-context, target-recall, and end-answer accuracy together. Without the oracle condition, retrieval failure and answerer failure are confounded.

## What remains unmeasured

The benchmark is small and intentionally adversarial to direct similarity. Real workload prevalence of such indirect relevance is not yet established, and active search over world knowledge can add substantial cost and hallucination risk.

## Next discriminating validation

Measure how often indirect relevance occurs in real personal-agent logs and compare three interfaces under equal cost: query expansion, world-knowledge-conditioned retrieval, and agentic search. The systems question is whether a cheap trigger can detect when ordinary similarity retrieval is unsafe.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use InMind when relevance depends on a world-knowledge bridge rather than semantic similarity. It challenges the assumption that similarity retrieval suffices. Failure on an indirect query may also reflect missing bridge knowledge in the backbone, so controls are needed before blaming retrieval.

### What a concrete task looks like

Illustrative task: a personal fact is stored in history, while a new query uses different concepts whose relation requires world knowledge. Direct recall may succeed without the system knowing when to retrieve the fact proactively.

### Most discriminating experiment

Pair direct and indirect queries for each fact and add an in-context-fact condition. First test whether the backbone can make the bridge with evidence supplied, then evaluate retrieval routing. Add lexically similar but irrelevant distractors to check whether a method merely broadens recall.

### Pair with

[locomo-plus](locomo-plus.en.md) · [came-bench](came-bench.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->

## Genealogy

`semantic recall → query-conditioned retrieval → knowledge-mediated relevance discovery`

InMind exposes a structural limit of treating the current query as a sufficient retrieval key.