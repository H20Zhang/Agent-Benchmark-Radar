# Data Agent Benchmark (DAB): enterprise questions across heterogeneous databases

[中文](data-agent-benchmark.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2603.20576) · [Project](https://ucbepic.github.io/DataAgentBench/) · [Code](https://github.com/ucbepic/DataAgentBench)

## What it actually measures

DAB evaluates whether agents can answer enterprise data questions when relevant information is **fragmented across multiple heterogeneous database systems**, references are inconsistent, and useful context may be buried in unstructured fields.

## What changed relative to prior evaluation

Text-to-SQL assumes one database and a known schema. DAB moves the target to integration, transformation, and analysis across PostgreSQL, MongoDB, SQLite, and DuckDB, making data-location discovery and cross-system reconciliation part of the task.

## Decisive evidence

DAB contains 54 queries across 12 datasets, nine domains, and four DBMSes, derived from a formative study of enterprise workloads across six industries. The reported best frontier model, Gemini-3-Pro, reaches only 38% pass@1, despite the relatively small query count.

## What the score supports

The benchmark is evidence for end-to-end enterprise data-question answering under a heterogeneous backend. It cannot attribute failure to semantic mapping, integration, transformation, SQL/NoSQL generation, or answer synthesis without trajectory analysis.

## Fair comparison contract

Fix database snapshots, credentials/access, tool interfaces, model, retry policy, and number of trials; the leaderboard asks for at least five trials per query. Report pass@1 and variance, since stochastic agents can look substantially different under best-of-n evaluation.

## What remains unmeasured

The suite is small and read-oriented. Production agents face permissions, writes, lineage, semantic layers, changing schemas, cost constraints, and ambiguous business definitions.

## Next discriminating validation

Annotate each query with a ground-truth integration/semantic plan and score intermediate relation resolution before final execution. That would reveal whether heterogeneous data access or business semantics is the dominant bottleneck.

## Genealogy

`single-database text-to-SQL → cross-database integration → enterprise data agent`

DAB makes backend heterogeneity a first-class evaluation property.