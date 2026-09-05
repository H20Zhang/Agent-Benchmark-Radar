# MTRAG-UN: multi-turn RAG should not assume every turn is answerable, complete, or standalone

[中文](mtrag-un.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://aclanthology.org/2026.findings-acl.503/) · [Code](https://github.com/IBM/mt-rag-benchmark)

## What it measures

MTRAG-UN derives 666 tasks from 666 conversations with more than 2,800 turns across six domains and explicitly includes unanswerable, underspecified, non-standalone, and unclear turns. It evaluates retrieval ranking, generation, IDK detection, and faithfulness.

## Compared with what

Typical multi-turn RAG assumes the current query can be resolved from history and an answer exists in the corpus. MTRAG-UN adds realistic states where the correct behavior is clarification or abstention rather than immediate answering.

## Score boundary

IDK, faithfulness, and retrieval metrics support uncertainty handling under the fixed corpus, dialogue history, and judge. Query rewriting, collection-model bias, and inherited corpora all affect difficulty, so one aggregate score cannot identify the improved component.

## Fair comparison conditions

Align conversation version, query-rewriting policy, corpus, retriever, answerer, and judge, and report answerable, unanswerable, and underspecified slices separately.

## Next evaluation coordinate

The next step lets clarification actually change dialogue state and retrieval queries, measuring whether one question reduces later search cost and error.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use MTRAG-UN for ellipsis, ambiguity, and unanswerability in multi-turn RAG. A turn may not be a standalone query: retrieving its raw text can fail, while an incorrect rewrite can introduce assumptions the user never made.

### What a concrete task looks like

Illustrative task: after discussing an object, a user asks about an alternative case without restating the scope. The history may not uniquely determine the intended question. The system should resolve context and clarify remaining uncertainty rather than invent the request.

### Most discriminating experiment

Compare raw-turn retrieval, automatic rewriting, and supplied-correct-standalone-question conditions. Measure retrieval, answering, and clarification separately across answerable, unanswerable, and underspecified tasks so blanket rewriting or abstention cannot hide failures.

### Pair with

[rgb](rgb.en.md) · [longmemeval](longmemeval.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->
