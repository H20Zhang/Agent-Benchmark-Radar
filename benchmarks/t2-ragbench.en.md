# T²-RAGBench: text-table financial QA becomes RAG only after oracle context is removed

[中文](t2-ragbench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://aclanthology.org/2026.eacl-long.8/) · [Code](https://github.com/uhh-hcds/g4kmu-paper)

## What it measures

The current T²-RAGBench release contains 23,088 question-context-answer triples over 7,318 financial reports derived from FinQA, first-turn ConvFinQA, and TAT-DQA. The initial paper reported 32,908 before VQAonBD was removed. It evaluates text/table retrieval with MRR@3 and numerical answers, with oracle context as an upper bound.

## Compared with what

Source financial-QA datasets generally provide the correct context, making retrieval invisible. T²-RAGBench removes oracle evidence and connects text-table retrieval to numerical reasoning while retaining an oracle baseline to localize retrieval loss.

## Score boundary

Retrieval MRR and numerical accuracy support performance under the current dataset version, serialization, and reader. Because sample composition changed, the original paper and current artifact are distinct tracks.

## Fair comparison conditions

Align dataset version, document serialization, chunk/index pipeline, reader, and corpus-size setting, and explicitly separate oracle-context from retrieved-context results.

## Next evaluation coordinate

The next step covers longer financial collections, cross-report aggregation, and provenance, testing whether numerical answers are supported by complete evidence chains.
