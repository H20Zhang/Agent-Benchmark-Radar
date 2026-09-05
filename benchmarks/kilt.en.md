# KILT: making provenance part of knowledge-intensive evaluation on one snapshot

[中文](kilt.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2009.02252) · [Code](https://github.com/facebookresearch/KILT)

## What it measures

KILT maps open-domain QA, fact checking, entity linking, slot filling, and other knowledge-intensive tasks onto one shared Wikipedia snapshot and evaluates downstream task quality together with provenance. A system must not only produce an output but identify where the supporting knowledge came from in the shared source.

## Compared with what

Earlier task suites commonly used different corpora, retrievers, and evidence definitions, making it hard to tell whether retrieval infrastructure generalized across tasks. KILT introduces one snapshot and one provenance contract, turning “where did the knowledge come from?” into a reusable cross-task coordinate and an important foundation for later RAG evaluation.

## Decisive evidence and score boundary

KILT's durable evidence is not a modern saturated leaderboard number; it is that task performance and provenance quality can be compared after controlling the retrieval source. A high KILT score supports performance on a fixed snapshot across several knowledge-intensive tasks. It does not support claims about freshness, live search, or agentic retrieval. End-to-end differences between retriever-generator stacks also do not automatically identify the retrieval component.

## Fair comparison conditions

Lock the KILT Wikipedia snapshot, task split, index, provenance metric, and generator. Updating the corpus or replacing it with external search changes the evaluation object and should not be ranked directly against original KILT results.

## Next evaluation coordinate

KILT controls snapshot differences, but that also removes freshness and environment drift. Stronger successors need time/version change and interactive search control without giving up reproducibility.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use KILT for reusable retrieval and provenance over a shared knowledge source. Its main contribution is a common evidence coordinate across knowledge-intensive tasks. Higher task quality does not necessarily imply more accurate provenance, so retain both readouts.

### What a concrete task looks like

Illustrative task: the same knowledge base supports fact checking, entity linking, and QA, with outputs tied to supporting pages. Retrieval infrastructure may be shared, but output formats and correctness definitions differ; success on one task does not establish success on all.

### Most discriminating experiment

Swap retrievers over a fixed knowledge snapshot while preserving each task's generator and evaluator. Report task and provenance scores separately and test whether the retrieval change transfers across tasks. A single-task improvement calls for task-adaptation checks before claims of general reuse.

### Pair with

[beir](beir.en.md) · [crag](crag.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->
