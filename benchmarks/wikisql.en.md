# WikiSQL: an early executable text-to-SQL anchor, limited to single-table queries

[中文](wikisql.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

## What it measures

WikiSQL contains 80,654 natural-language/SQL examples over 24,241 Wikipedia tables. The contract maps a question to executable SQL and scores the execution result, primarily covering single-table selection, filtering, and aggregation.

## Compared with what

Earlier semantic-parsing datasets were small and domain-specific. WikiSQL scaled text-to-SQL across many schemas and helped establish execution accuracy as a standard metric for natural-language database interfaces.

## Score boundary

High execution accuracy supports single-table schema grounding and SQL generation. It does not support multi-table joins, business semantics, database exploration, or agentic analysis. Near-saturation on WikiSQL therefore says little about whether real data agents are solved.

## Fair comparison conditions

Align split, schema serialization, execution engine, value access, and decoding constraints. Systems receiving extra schema/value hints belong in a different track from pure text-to-SQL.

## Next evaluation coordinate

Spider moves to unseen multi-table databases; broader data-agent evaluation must additionally cover multiple systems, unstructured data, analysis workflows, and business correctness.
