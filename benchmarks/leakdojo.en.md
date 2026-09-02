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
