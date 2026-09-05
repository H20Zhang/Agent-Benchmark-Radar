# LeakDojo: RAG evaluation should also ask how much database content an attacker can extract

[中文](leakdojo.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://aclanthology.org/2026.findings-acl.287/) · [Code](https://github.com/yeasen-z/LeakDojo)

## What it measures

LeakDojo is a configurable RAG-leakage diagnostic. The paper compares six existing attacks across 14 LLMs and four datasets—FIQA, SciFact, NFCorpus, and Enron—while the current codebase implements seven attacks. Metrics include query-budget scaling, ROUGE-L recall, unique chunk recovery, and defense ablations.

## Compared with what

Earlier leakage studies often demonstrate one attack on one model or pipeline. LeakDojo turns attacks, models, retrievers, corpora, and defenses into a controlled comparison matrix, making database-extraction risk a reusable RAG evaluation object.

## Score boundary

Recovered text or chunks support extraction risk under the named attack budget, chunking, query generator, and RAG pipeline. They do not cover authorization, API secrets, cross-tenant access, or real incident impact.

## Fair comparison conditions

Align corpus/chunking, attack implementation, query budget, generator, model, retriever, and leakage threshold. Different budgets should be shown as curves rather than one maximum value.

## Next evaluation coordinate

The next step combines extraction with authorization boundaries, sensitive-field severity, and production consequences instead of weighting all chunks equally.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use LeakDojo to compare corpus-extraction risk and defenses under controlled RAG configurations. Recovered text depends on query budget and chunking. It does not replace cross-tenant authorization or production-incident evaluation, nor should one attack's maximum leakage summarize the system.

### What a concrete task looks like

Illustrative task: an attacker uses bounded queries to recover restricted corpus content while a defense preserves legitimate QA. Repeating the same text and recovering new chunks create different cumulative exposure, requiring distinct accounting.

### Most discriminating experiment

Fix corpus, chunking, retriever, and query budget, reporting unique recovered chunks alongside benign QA quality. Cross attacks with models to test whether a defense reduces inappropriate evidence exposure rather than suppressing one output style.

### Pair with

[gatemem](gatemem.en.md) · [injecmem](injecmem.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->
