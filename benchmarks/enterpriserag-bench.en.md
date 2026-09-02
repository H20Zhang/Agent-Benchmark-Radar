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
