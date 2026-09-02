# Data Agent Benchmark (DAB): real enterprise data questions span DBMSes and data forms

[中文](data-agent-benchmark.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2603.20576) · [Code and leaderboard](https://github.com/ucbepic/DataAgentBench)

## What it measures

DAB contains 54 queries over 12 datasets, nine domains, and four DBMSes—PostgreSQL, MongoDB, SQLite, and DuckDB. Grounded in an enterprise workload study, it stresses multi-database integration, ill-formatted key joins, unstructured-text transformation, and domain knowledge rather than one text-to-SQL translation.

## Compared with what

Spider and BIRD largely assume the needed facts live inside one relational database. DAB makes one question span database systems, heterogeneous keys, and textual fields, forcing integration, transformation, and analysis.

## How to interpret current scores

The official leaderboard uses Pass@1 and requires at least five trials per query; the site can recompute historical submissions with current validators. Result tracks therefore need a recomputation/protocol date rather than copying submission-time numbers. High Pass@1 supports reliability of the full agent stack on the 54-query suite and does not isolate one integration, reasoning, or model component.

## Fair comparison conditions

Align dataset/ground-truth revision, validators, trials per query, hints, DBMS versions, agent scaffold, and model mixture. Five-trial submissions and 50-trial paper baselines are different protocols.

## Next evaluation coordinate

DAB captures cross-database complexity but has only 54 queries. The next step adds more schema drift, permissions, writes, analyst artifacts, and business-semantic correctness.
