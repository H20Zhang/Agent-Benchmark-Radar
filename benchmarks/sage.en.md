# SAGE: scientific search should separate finding one target paper from collecting a complete evidence set

[中文](sage.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2602.05975) · [Code](https://github.com/HughieHu/Sage)

## What it measures

SAGE provides 1,200 expert queries across computer science, healthcare, humanities, and natural science: 600 short-form target-paper queries and 600 open-ended discovery queries over a controlled corpus of about 200K papers. The former uses exact-paper retrieval while the latter uses weighted recall for evidence-set coverage.

## Compared with what

Literature-search benchmarks often focus on title or known-item retrieval. SAGE separates targeted lookup from open-ended evidence collection and performs agent-retriever ablations, making backend quality observable inside the same search agent.

## Score boundary

Exact-paper retrieval and weighted recall support scientific discovery under the named corpus snapshot, index, and search budget. Open-ended gold sets can be incomplete, and the released repository does not package a turnkey copy of the full 200K-paper environment, so artifact availability is part of reproducibility.

## Fair comparison conditions

Align corpus snapshot, indexing configuration, agent subquery generation, budget, and gold-set version. Short-form and open-ended tracks should not be collapsed into one SOTA number.

## Next evaluation coordinate

The next step integrates citation graphs, full text, and changing scholarly databases while making completeness ceilings and search cost explicit.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use SAGE to distinguish targeted paper finding from open-ended scientific evidence collection. Their tolerance for missed results differs: finding one correct paper does not establish field coverage. Reproduction also depends on access to the full corpus and search environment.

### What a concrete task looks like

Illustrative task: one query identifies a particular paper from clues, while another collects several works supporting a research topic. A retriever may excel at pinpointing one paper while repeatedly returning the same cluster during broad collection.

### Most discriminating experiment

Fix search interfaces and budgets over the same paper corpus and separately evaluate target discovery and weighted coverage. Document deduplication, metadata, and full-text access. Separate missing-environment limitations from algorithmic failure so inconsistent indexes do not drive the comparison.

### Pair with

[autoresearchbench](autoresearchbench.en.md) · [scholarquest](scholarquest.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->
