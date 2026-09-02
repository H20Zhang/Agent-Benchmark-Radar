# MC-Search: multimodal agentic RAG needs planning, modality choice, and hop-level evidence evaluation

[中文](mc-search.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2603.00873) · [Code](https://github.com/YennNing/MC-Search)

## What it measures

MC-Search contains 3,333 tasks averaging about 3.7 hops across five reasoning topologies, with annotations for each subquestion, retrieval modality, supporting evidence, and intermediate answer. The paper describes a knowledge base of roughly 389,750 images and 784,473 text passages, while the current released artifact is smaller, making artifact version part of the contract.

## Compared with what

Standard multimodal QA scores only the final answer, while agentic search often lacks a gold process. MC-Search adds hop-level retrieval, planning accuracy, gold-evidence answering, and rollout deviation so over/under-retrieval, modality errors, and chain drift become separately visible.

## Score boundary

High planning or retrieval scores support agreement with the benchmark's gold trajectory, but a single gold path can penalize alternative valid routes. The mismatch between paper-scale and released artifacts also means every result must bind to a concrete version.

## Fair comparison conditions

Align knowledge-base artifact, multimodal backbone, hop budget, judge, and trajectory policy. Gold-evidence and free-search conditions require separate tracks.

## Next evaluation coordinate

The next step allows multiple valid trajectories and jointly evaluates modality choice, real latency/cost, and final evidence sufficiency.
