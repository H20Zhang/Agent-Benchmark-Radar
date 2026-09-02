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
