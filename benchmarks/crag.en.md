# CRAG: bringing freshness, long-tail knowledge, and abstention into RAG evaluation

[中文](crag.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2406.04744) · [Code](https://github.com/facebookresearch/CRAG)

## What it measures

CRAG contains 4,409 QA pairs across five domains and eight question categories, with mock web and knowledge-graph APIs for dynamic facts, long-tail entities, retrieval, and abstention. Hallucination-sensitive grading makes refusing when evidence is insufficient part of the capability.

## Compared with what

Static RAG benchmarks often treat the corpus as timeless ground truth. CRAG introduces popularity, freshness, and dynamic facts as evaluation variables and was used for the KDD Cup 2024 challenge, making model knowledge cutoff and retrieval source visibly load-bearing.

## Decisive evidence and score boundary

CRAG makes the boundary between static parametric knowledge and dynamic external evidence measurable. A high score supports factual handling under the named mock API/KG snapshot and grading rule; it does not prove that the same system is a better live-web agent because provider ranking, interface complexity, and drift are controlled away.

## Fair comparison conditions

Align mock API/KG version, knowledge cutoff, answer grader, allowed tools, and retrieval budget. Different model cutoffs or real search interfaces belong in separate tracks.

## Next evaluation coordinate

A stronger successor preserves freshness while using replayable web snapshots or recorded tool traces to separate retrieval policy, source quality, and model knowledge.
