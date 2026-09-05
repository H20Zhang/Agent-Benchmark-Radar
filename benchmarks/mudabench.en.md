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

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use MuDABench for extraction and aggregation across large document collections, not merely finding a few relevant sources. Analytical questions require coverage of the set that should enter the calculation. High top-k relevance can still miss documents that change the aggregate.

### What a concrete task looks like

Illustrative task: extract comparable values from financial reports, align entities and periods, and aggregate them. Correct extraction from one report is insufficient: missing an in-scope entity or mixing definitions can produce a precise-looking but wrong result.

### Most discriminating experiment

Score document coverage, field extraction, and final aggregation separately, with supplied-complete-document-set and supplied-correct-intermediate-table controls. Pin annotation revisions and PDF parsing to locate discovery, extraction, or computation bottlenecks rather than labeling all failures reasoning errors.

### Pair with

[t2-ragbench](t2-ragbench.en.md) · [dataspace](dataspace.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->
