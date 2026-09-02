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
