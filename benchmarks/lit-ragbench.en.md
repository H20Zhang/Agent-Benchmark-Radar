# LIT-RAGBench: remove the retriever and test whether the generator can use RAG context

[中文](lit-ragbench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2603.06198) · [Code](https://github.com/Koki-Itai/LIT-RAGBench)

## What it measures

LIT-RAGBench has 114 human-constructed Japanese questions with machine-translated, human-curated English counterparts. Positive and negative chunks are supplied directly, and generator behavior is evaluated across Logic, Integration, Table, Reasoning, and Abstention.

## Compared with what

In many RAG benchmarks, final-answer failure can come from either retrieval or generation. LIT-RAGBench controls retrieval away, making failures visible even when the required evidence is already present.

## Score boundary

Category accuracy supports context-use ability under the supplied-context contract; it does not support claims about retrievers or agentic search. The small dataset, translation, and fictional task design can also shift difficulty across languages.

## Fair comparison conditions

Align supplied chunks, prompt template, generator, judge, and language version, and report capability categories and languages separately.

## Next evaluation coordinate

The next step reconnects these diagnostics to a retrieval loop: after detecting an integration or abstention failure, can the system search again or repair the context?

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use LIT-RAGBench to diagnose integration, tables, logic, and abstention without retriever variation. Its scope is generation over supplied context. Higher scores do not establish improvements in indexing, retrieval, or multi-step tool orchestration.

### What a concrete task looks like

Illustrative task: a model receives text and table passages and must combine their conditions or abstain when information is missing. Visibility of every passage does not guarantee cross-passage reasoning, which is why generator-only diagnosis is useful.

### Most discriminating experiment

Vary passage order, distractor ratio, and language over matched contexts with one evaluator. Report capability slices and inspect language-version differences. For system-level RAG claims, connect real retrieved contexts and test whether the local advantage survives.

### Pair with

[rgb](rgb.en.md) · [t2-ragbench](t2-ragbench.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->
