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
