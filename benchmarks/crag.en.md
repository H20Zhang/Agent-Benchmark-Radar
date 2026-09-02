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

## Genealogy

`static RAG QA → dynamic/long-tail factuality → live information-seeking reliability`

CRAG made knowledge freshness a first-class RAG variable rather than a hidden dataset property.