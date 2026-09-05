# HotpotQA: making multi-hop evidence composition an explicit evaluation target

[中文](hotpotqa.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://aclanthology.org/D18-1259/)

## What it measures

HotpotQA contains roughly 113K Wikipedia questions with sentence-level supporting facts. Systems must retrieve complementary evidence across documents and perform multi-hop reasoning, so the benchmark can inspect both the final answer and whether the evidence that supports it was found.

## Compared with what

Earlier open-domain QA often reduced retrieval and reasoning to a single-hop hit. HotpotQA makes cross-document composition and supporting-fact supervision part of the benchmark contract, becoming an important precursor to MultiHop-RAG, agentic retrieval, and evidence-grounded QA.

## Decisive evidence and score boundary

Its durable contribution is that answer accuracy and evidence coverage can be observed separately: a correct answer does not imply correct supporting facts. Modern models can also exploit dataset shortcuts, parametric memory, or stronger readers, so high current scores do not by themselves establish a better retriever or multi-hop policy. Without a matched retriever-reader interface, end-to-end EM/F1 is packaged-system evidence.

## Fair comparison conditions

Align the fullwiki/distractor setting, corpus snapshot, retriever, reader, supporting-fact metric, and candidate budget. Results on static Wikipedia should not be directly ranked against live-web search agents.

## Next evaluation coordinate

HotpotQA does not cover web drift, tool state, search cost, or query reformulation. Stronger successors should let the system decide when to continue searching, how to repair the retrieval path, and whether the evidence portfolio actually drives the final answer.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use HotpotQA as a foundation for multi-document evidence composition, not a complete proxy for live search agents. Distinguish supplied candidate paragraphs from full-corpus retrieval: they impose different demands on retrieval, so answer scores should not be pooled.

### What a concrete task looks like

Illustrative task: one document identifies an intermediate entity and another supplies the final attribute. The system needs both an answer and facts supporting the two steps. Guessing the answer does not establish a correct evidence chain.

### Most discriminating experiment

Fix the answerer and compare single-shot retrieval, iterative retrieval, and supplied supporting facts, reporting evidence recall and answer quality separately. Remove a required fact to probe shortcuts. Do not attribute gains from a larger candidate pool entirely to multi-hop planning.

### Pair with

[multihop-rag](multihop-rag.en.md) · [browsecomp-plus](browsecomp-plus.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->
