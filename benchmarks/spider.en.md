# Spider: from single-table SQL to compositional generalization over unseen databases

[中文](spider.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

## What it measures

Spider contains 10,181 questions and 5,693 unique complex SQL queries over 200 databases in 138 domains. Databases are split across train and test, requiring joins, nested queries, aggregation, and schema grounding on unseen schemas.

## Compared with what

WikiSQL focuses mostly on single-table operations with much simpler schema transfer. Spider makes cross-database generalization and compositional multi-table SQL central evaluation requirements.

## Score boundary

Execution or exact-match supports text-to-SQL generalization on static relational schemas. It does not measure database exploration, external documentation, business rules, writes, or multi-turn analysis. Stronger schema-linking prompts also change the comparison contract.

## Fair comparison conditions

Align Spider version, schema/value access, execution evaluator, test databases, and external retrieval policy. Different schema hints require separate tracks.

## Next evaluation coordinate

BIRD adds larger real databases and external knowledge, while Spider 2.0 expands toward enterprise SQL, multiple dialects, and database operations.
