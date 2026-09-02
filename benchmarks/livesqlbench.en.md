# LiveSQLBench: SQL benchmarks drift too, and enterprise databases are more than SELECT queries

[中文](livesqlbench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Project](https://livesqlbench.ai/)

## What it measures

LiveSQLBench includes tracks such as Base-Lite (about 270 tasks/18 databases), Base-Full (about 600/22), and Large-v1 (about 480 tasks over 18 industrial databases averaging roughly 1K columns and 54 tables), covering query SQL and management/DDL-style tasks with separate model/agent tracks and evolving hidden releases.

## Compared with what

Spider and BIRD are fixed snapshots. LiveSQLBench makes dataset and validator evolution part of the benchmark lifecycle, reduces overfitting to a permanent test set, increases enterprise schema scale, and includes database operations beyond SELECT.

## Score boundary

Success rate is meaningful only for a concrete track, release, and harness. Hidden tests, rules, and schemas can change, so old and new results cannot be merged into a timeless SOTA.

## Fair comparison conditions

Align Base/Large track, release date, schema hints, database engine, model/agent mode, tool budget, and evaluator rules.

## Next evaluation coordinate

The next step connects SQL execution to business semantic layers, multi-system integration, and persistent operational state.
