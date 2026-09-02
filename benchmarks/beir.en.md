# BEIR: testing zero-shot retriever generalization across heterogeneous domains

[中文](beir.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2104.08663) · [Code](https://github.com/beir-cellar/beir)

## What it measures

BEIR originally combines 18 retrieval datasets from different domains and task types under a common ranking protocol. Its target is whether a retriever trained elsewhere continues to find relevant evidence zero-shot, explicitly separating performance on one familiar benchmark from cross-domain robustness.

## Compared with what

Dense-retrieval progress had often been reported on a single train/test distribution. BEIR makes heterogeneous zero-shot generalization a first-class requirement and exposes trade-offs among lexical, dense, and reranking methods across one shared suite.

## Decisive evidence and score boundary

A durable early finding is that strong dense retrieval on one benchmark does not guarantee zero-shot superiority; lexical baselines such as BM25 remain competitive in several domains. Modern aggregate nDCG values now mix many training regimes and rerankers, so a BEIR average supports ranking quality only for the named dataset mixture and indexing protocol. It does not establish better agentic search or end-to-end RAG.

## Fair comparison conditions

Align the dataset subset/version, preprocessing and indexing, reranker use, training data, and aggregation rule. Partial-suite averages are not directly comparable with full-suite results.

## Next evaluation coordinate

BEIR is static retriever-only evaluation. The next coordinate is cross-domain robustness under iterative retrieval, query reformulation, latency/cost, and actual downstream evidence use.
