# MuDABench: from finding a few supporting documents to collection-wide extraction and aggregation

[中文](mudabench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://aclanthology.org/2026.findings-acl.341/) · [Code](https://github.com/Zhanli-Li/MuDABench)

## What it measures

MuDABench contains 332 financial analytical questions over more than 80K report pages; the current repository organizes 166 simple and 166 complex questions with 589 source PDFs. Tasks require collection-scale extraction, aggregation, and numerical or code-assisted reasoning, with intermediate-fact coverage as a diagnostic.

## Compared with what

Multi-document QA often needs only a few supporting sources. MuDABench expands the candidate collection to report-scale evidence, requiring systems to discover many dispersed facts before aggregation or calculation.

## Score boundary

Final accuracy and intermediate-fact coverage support collection-scale analysis under the current document release, extraction pipeline, and harness. Annotation and document coverage evolve, so results need explicit version binding.

## Fair comparison conditions

Align PDF corpus, annotation version, extraction pipeline, retrieval budget, agent harness, and numerical evaluator. Revised annotations should not be mixed with earlier snapshots.

## Next evaluation coordinate

The next step measures confidence in evidence completeness and missing-document detection: can the system recognize when its collection is incomplete rather than simply produce a number?
