# CRAG: RAG under freshness, long-tail knowledge, and abstention pressure

[中文](crag.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2406.04744) · [Code](https://github.com/facebookresearch/CRAG)

## What it actually measures

CRAG evaluates factual RAG across changing facts, entity popularity, question complexity, web search, knowledge-graph access, and abstention. Its 4,409 QA pairs span five domains and eight categories, with temporal dynamism ranging from years to seconds.

## What changed relative to prior evaluation

Static QA benchmarks blur model knowledge and retrieval value because many answers are already memorized. CRAG stresses facts whose freshness and long-tail nature make external retrieval necessary and makes hallucination-sensitive correctness central.

## Decisive evidence

The paper reports advanced LLMs at no more than 34% accuracy, straightforward RAG around 44%, and state-of-the-art industry RAG systems answering only 63% of questions without hallucination. Accuracy falls further for more dynamic, less popular, and more complex facts.

## What the score supports

CRAG provides evidence about trustworthy factual QA under its mock web/KG interfaces. The strong freshness effect supports the value of retrieval, but the score remains system-level: model knowledge cutoff, retrieval stack, source handling, and answer policy all matter.

## Fair comparison contract

Fix model snapshot/knowledge cutoff, mock APIs, retrieval budget, KG access, and grading. Report hallucination/abstention separately from raw accuracy; a system that guesses aggressively should not be equated with one that correctly knows when evidence is insufficient.

## What remains unmeasured

Mock APIs improve reproducibility but remove much of live-web navigation, interface variability, authentication, and search-provider drift. The benchmark is factual QA rather than long-form research or open-ended tool use.

## Next discriminating validation

Replay the same factual targets through both frozen mock APIs and live-web agents, measuring the gap due to source discovery and interface control. That would isolate how much modern search-agent difficulty lies outside the retriever itself.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use CRAG for factual freshness, long-tail knowledge, and response behavior under insufficient evidence. Mock retrieval interfaces improve control but do not represent full browser interaction. When a model knows an older answer, separate parametric knowledge from current evidence.

### What a concrete task looks like

Illustrative task: a query asks for a changing fact, while search results and a knowledge graph supply evidence in different forms. The system must resolve temporal applicability and sufficiency rather than answer with a plausible remembered value.

### Most discriminating experiment

Fix interfaces and the evaluation time, then compare closed-book, web-only, graph-only, and combined evidence. Slice by dynamic facts and long-tail entities and separately report abstention and incorrect answers on insufficient-evidence cases so conservative behavior does not obscure utility.

### Pair with

[livebrowsecomp](livebrowsecomp.en.md) · [mtrag-un](mtrag-un.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->

## Genealogy

`static RAG QA → dynamic/long-tail factuality → live information-seeking reliability`

CRAG made knowledge freshness a first-class RAG variable rather than a hidden dataset property.