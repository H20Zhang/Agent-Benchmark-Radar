# Spider 2.0: moving text-to-SQL toward enterprise database workflows

[中文](spider-2.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Project](https://spider2-sql.github.io/)

## What it measures

Spider 2.0 targets enterprise-like SQL-agent tasks. Current official families include Spider 2.0-Snow, Spider 2.0-Lite, and Spider 2.0-DBT, with public sizes around 547, 547, and 68 tasks respectively and continuing release evolution. Tasks cover large schemas, multiple SQL dialects, complex analytics, and database-management/DBT-style work.

## Compared with what

Original Spider is primarily static text-to-SQL. Spider 2.0 adds schema scale, real database systems, dialect differences, and multi-step operations, requiring exploration and execution rather than one SQL string.

## Score boundary

Success rates bind to a concrete family, release, context setting, and evaluator. Oracle-table and other assisted conditions are different contracts and should not be mixed with full schema-discovery results.

## Fair comparison conditions

Align Snow/Lite/DBT family, release, database version, schema/table hints, agent scaffold, step budget, and evaluator. Oracle conditions must be explicitly separated.

## Next evaluation coordinate

The next step moves beyond SQL-centric workflows to multiple databases, unstructured documents, and business semantics, as in DAB and AgenticDataBench.
