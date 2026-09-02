# Spider 2.0: enterprise text-to-SQL becomes an agent workflow

[中文](spider-2.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2411.07763) · [Project](https://spider2-sql.github.io/)

## What it actually measures

Spider 2.0 evaluates **real-world enterprise text-to-SQL workflows**, not isolated query generation. Its 632 problems use real application databases, often with more than 1,000 columns and cloud systems such as BigQuery and Snowflake; solving them can require metadata search, dialect documentation, project code, multiple queries, and workflows exceeding 100 SQL lines.

## What changed relative to prior evaluation

Spider 1.0 asks for generalization to unseen schemas; BIRD adds realistic database values. Spider 2.0 changes the unit of work itself: an agent must navigate a large data environment and construct a multi-step SQL workflow, closer to data engineering/analytics than one semantic-parsing prediction.

## Decisive evidence

The original evaluation reports an o1-preview-based code agent at only 17.0% success on Spider 2.0, versus 91.2% on Spider 1.0 and 73.0% on BIRD. The collapse is direct evidence that prior benchmark saturation did not transfer to enterprise workflow complexity.

## What the score supports

Spider 2.0 supports end-to-end competence at enterprise SQL workflow construction under its environment. It does not isolate SQL reasoning from metadata retrieval, long-context management, dialect knowledge, code navigation, or agent scaffold quality.

## Fair comparison contract

Pin database/cloud snapshots, SQL dialects, metadata and codebase access, agent harness, model, execution/retry budget, and evaluator. A system given preselected relevant tables is solving a materially easier task than one required to discover them.

## What remains unmeasured

Business definitions, ambiguous stakeholder intent, governance, permission, production writes, and persistent maintenance remain only partially represented. Real warehouses also evolve continuously rather than staying frozen for one benchmark run.

## Next discriminating validation

Decompose performance into metadata discovery, semantic/schema resolution, workflow planning, query execution, and repair using oracle interventions. This would tell whether the 17% bottleneck is mostly retrieval/context or SQL/program synthesis.

## Genealogy

`single query → complex unseen schema → large enterprise SQL workflow`

Spider 2.0 is where text-to-SQL evaluation becomes unmistakably an agent-systems problem.