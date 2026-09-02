# RAGTruth: moving RAG hallucination evaluation from answer-level to word-level

[中文](ragtruth.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2401.00396)

## What it measures

RAGTruth contains nearly 18K naturally generated RAG responses with manual hallucination annotations at case and word level, including severity. The target is localized grounding failure relative to retrieved evidence rather than a single faithful/unfaithful label for an entire answer.

## Compared with what

Earlier hallucination evaluation often depended on automatic judges or coarse answer labels. Fine-grained human spans make it possible to locate exactly where generation exceeds the evidence and to compare failure patterns across domains and source LLMs.

## Decisive evidence and score boundary

The dataset shows that an apparently correct long RAG answer can still contain local unsupported spans with different severity. Detector performance supports hallucination detection on the annotated distribution. It does not measure adaptive retrieval policy, and a lower hallucination rate cannot automatically be credited to the retriever because source LLM and retrieval setup are load-bearing confounders.

## Fair comparison conditions

Align the response set, annotation policy, severity definition, and detector input. Changing the source generator or retrieval pipeline changes the hallucination distribution and belongs in a separate track.

## Next evaluation coordinate

The next step is closed-loop correction: once an unsupported claim is detected, can an agent find missing evidence, revise the answer, and retain a citation-level audit trace?
