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

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use MC-Search to diagnose modality selection, missing evidence, and planning errors in multimodal search chains. Hop annotations provide localization, not necessarily a unique valid path. Differences between paper-scale and released corpora can also change the reproduced task.

### What a concrete task looks like

Illustrative task: textual evidence points to an image, whose detail determines the next search target. The agent must switch between text and vision. Text-only retrieval or final-answer-only grading can conceal modality-selection failures.

### Most discriminating experiment

Fix the released corpus version and separately supply correct modalities, intermediate evidence, and subquestions to measure recovery. Review evidence-supported alternative paths and report paper-scale and public-subset results separately rather than attributing resource differences to policy.

### Pair with

[merrin](merrin.en.md) · [visdocagentbench](visdocagentbench.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->
