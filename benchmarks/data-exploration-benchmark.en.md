# Data Exploration Benchmark: understand the data before pretending to analyze it

[中文](data-exploration-benchmark.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2608.16045)

## What it measures

The Data Exploration Benchmark evaluates the stage before analysis. The suite includes one real multi-sheet Vitamin-D workbook and 12 DSBench workbook tasks—four easy, five medium, and three hard—requiring agents to understand sheets, columns, relationships, and data quality and emit a schema-fixed JSON exploration artifact.

## Compared with what

Many data-agent benchmarks assume the relevant schema or tables are already known. This benchmark makes exploration a separate stage and uses raw, self-exploration, and oracle-exploration downstream ablations to test whether better data understanding actually changes later performance.

## Score boundary

Artifact scores and downstream deltas support exploration quality for workbook-style data under the fixed schema and evaluator. They do not establish large database or data-lake discovery, and oracle exploration is only an upper bound.

## Fair comparison conditions

Align workbook release, exploration JSON schema, token/tool budget, downstream agent, and evaluator. Raw, self, and oracle conditions require separate reporting.

## Next evaluation coordinate

The next step scales to multi-source catalogs, permissions, and schema drift and tests whether exploration artifacts can be maintained incrementally rather than generated once.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use the Data Exploration Benchmark for intermediate data understanding, especially logical tables, keys, and column semantics in messy workbooks. Its small spreadsheet-specific scope makes it a mechanism diagnostic. A comprehensive-looking exploration artifact is not proof of downstream value.

### What a concrete task looks like

Illustrative task: a workbook contains several logical tables, merged headers, and implicit relationships. The agent constructs structured understanding before analysis. Mistaking a presentation region for a data table can invalidate later computations even if they execute correctly.

### Most discriminating experiment

Retain raw-data, self-generated-exploration, and oracle-exploration conditions with a fixed downstream analyst. Inspect keys, relationships, and quality issues and test on other workbooks. Charge exploration cost to determine when a reusable representation justifies preprocessing.

### Pair with

[kramabench](kramabench.en.md) · [dataspace](dataspace.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->
