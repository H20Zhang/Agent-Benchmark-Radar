# RAGCap-Bench: test intermediate agentic-RAG capabilities before collapsing everything into end-to-end score

[中文](ragcap-bench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2510.13910)

## What it measures

RAGCap-Bench extracts targeted capability tests from recurring tasks and failure patterns in agentic-RAG workflows, including retrieval planning and intermediate reasoning. Its goal is not another monolithic final-answer benchmark but an evaluation layer that decomposes black-box failure into separately testable skills.

## Compared with what

Conventional RAG evaluation can observe lower end-to-end accuracy without knowing whether retrieval, planning, or reasoning caused it. RAGCap-Bench makes capability decomposition itself an evaluation layer and provides a local capability profile before system-level experimentation.

## Score boundary

A capability score supports performance on an isolated task and prompt harness. It matters for systems only if it predicts matched end-to-end behavior. Strong isolated planning does not guarantee correct planning under real tool budgets, error propagation, and stopping pressure.

## Fair comparison conditions

Align capability definitions, prompt harness, backbone, and resource budget, and report capability-to-system transfer when possible rather than only local accuracy rankings.

## Next evaluation coordinate

The key next step is intervention validity: improve a measured weak capability and test whether real agentic-RAG trajectories improve in the predicted way.
