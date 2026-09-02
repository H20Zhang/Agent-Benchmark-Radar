# LiveSQLBench: text-to-SQL under schema and business-rule drift

[中文](livesqlbench.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Project](https://livesqlbench.ai/) · [Code](https://github.com/bird-bench/livesqlbench)

## What it actually measures

LiveSQLBench evaluates SQL agents against **evolving industrial databases**, not one frozen schema. It stresses large schemas, long metadata/context, business-rule drift, and both query and management-style interactions.

## What changed relative to prior evaluation

Spider/BIRD largely freeze the database and task distribution. LiveSQLBench makes temporal change part of the benchmark lifecycle: schema complexity grows, business rules change, and agents must use current context rather than rely on benchmark memorization.

## Decisive evidence

LiveSQLBench-Large-v1 expands to 18 databases with roughly 1K columns each and 480 tasks, with average prompts around 84K tokens and explicit Business Rule Drift. The project also releases an agent framework with per-task DB isolation and multi-provider support.

## What the score supports

Results support text-to-SQL/data-agent robustness under the benchmark's evolving snapshots. They do not isolate model reasoning from schema-linking/harness quality, and live versions require careful version pinning before comparing scores.

## Fair comparison contract

Pin benchmark release, DB snapshot, business-rule documents, SQL dialect, agent framework, model, and execution budget. Never compare scores from different evolving versions as though they came from one static test set.

## What remains unmeasured

Enterprise analytics also requires semantic definitions, permissions, lineage, clarification, write safety, and artifact delivery. Very large schemas still do not reproduce all organization-specific metadata and governance.

## Next discriminating validation

Create paired tasks immediately before and after a schema/business-rule change and measure update latency: how quickly does an agent stop using obsolete semantics without losing stable knowledge?

## Genealogy

`static text-to-SQL → industrial-scale schema → continuously evolving data environment`

LiveSQLBench makes benchmark freshness itself part of data-agent evaluation.