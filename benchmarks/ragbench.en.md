# RAGBench: benchmarking not only RAG systems, but how RAG is judged

[中文](ragbench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2407.11005) · [Data](https://huggingface.co/datasets/rungalileo/ragbench)

## What it measures

RAGBench provides roughly 100K examples across five industry-oriented domains with trace-style labels for retrieval/generation quality and for benchmarking RAG evaluators themselves. The target is not only whether a system answers correctly, but whether an evaluator produces interpretable failure signals.

## Compared with what

Many RAG benchmarks implicitly trust the judge. RAGBench makes the evaluator an evaluation object, exposing consistency and failure modes of automatic metrics such as faithfulness or context relevance across domains.

## Decisive evidence and score boundary

The large labeled set allows evaluator predictions to be compared with reference labels. An evaluator score supports its ability to identify a failure type on the named domain mixture; it does not establish that a RAG architecture rated highly by that judge is causally better. Label construction and source systems shape the observed error distribution.

## Fair comparison conditions

Align dataset/domain subset, label schema, source RAG outputs, and evaluator model/prompt. Different judge generations or domain mixtures require separate result tracks.

## Next evaluation coordinate

The stronger test asks whether evaluator signals actually improve retrieval policy: when a failure label triggers more search, do evidence coverage and task success reproducibly increase?
