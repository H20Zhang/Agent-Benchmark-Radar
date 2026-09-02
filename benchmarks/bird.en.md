# BIRD: text-to-SQL meets large databases, real values, and external knowledge

[中文](bird.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

## What it measures

BIRD contains 12,751 text-to-SQL pairs over 95 databases totaling roughly 33.4GB across 37 domains, incorporating database values and external knowledge for SQL generation over larger, more realistic schemas.

## Compared with what

Spider has complex schemas but smaller databases and less realistic value grounding. BIRD adds large database contents, value reasoning, and external knowledge, so schema understanding alone is insufficient.

## Score boundary

Execution accuracy supports SQL correctness under the current BIRD release, value access, and knowledge setup. It remains query answering and does not cover multi-database integration, Python analysis, reporting, or a business semantic layer.

## Fair comparison conditions

Align dataset version, database contents, external-knowledge access, schema/value retrieval, execution engine, and prompt budget. Different knowledge hints require separate tracks.

## Next evaluation coordinate

LiveSQLBench adds drift, management SQL, and evolving schemas; the Data Agent Benchmark moves further toward multiple DBMSes and unstructured text.
