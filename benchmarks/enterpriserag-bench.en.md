# EnterpriseRAG-Bench: enterprise RAG is about cross-source conflict, constraints, and knowing when information is absent

[中文](enterpriserag-bench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2605.05253) · [Code](https://github.com/onyx-dot-app/EnterpriseRAG-Bench)

## What it measures

EnterpriseRAG-Bench constructs roughly 500K coherent synthetic documents across nine enterprise source types and 500 questions in ten diagnostic categories. It evaluates document recall, answer alignment/completeness, source constraints, conflict resolution, and not-found behavior.

## Compared with what

General RAG often looks like one question and one evidence source. Enterprise workspaces contain duplicated, conflicting, or absent facts across email, tickets, wikis, and documents. A coherent cross-source ontology makes those cases part of one reusable contract.

## Score boundary

The combined score supports enterprise-style RAG under the synthetic company ontology, chunking/indexing, and judge. It does not establish real deployment robustness because permissions, organizational drift, and proprietary data distributions are not reproduced.

## Fair comparison conditions

Align generated corpus version, chunking/index, reader, judge, source constraints, and question category. Different corpus generations require distinct snapshots.

## Next evaluation coordinate

The next step adds real authorization, versioned artifacts, and writes, testing whether conflict resolution updates or contaminates shared knowledge state.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use EnterpriseRAG-Bench for noise, duplicates, conflicts, and missing information within a coherent enterprise-style corpus. A synthetic company enables cross-document reasoning but does not automatically provide real permissions or organizational semantics. High scores do not establish deployment reliability.

### What a concrete task looks like

Illustrative task: project decisions are distributed across documents, messages, and other enterprise sources, with duplicates and conflicting versions. The agent must identify operative evidence and answer the full scope; one supporting passage does not show conflict resolution.

### Most discriminating experiment

Fix the corpus snapshot and chunking, then report source-constrained, conflict, completeness, and not-found slices. Add a supplied-correct-document-set condition and scale the corpus to distinguish cross-source reasoning, index coverage, and adaptation to the synthetic company.

### Pair with

[gatemem](gatemem.en.md) · [mudabench](mudabench.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->
