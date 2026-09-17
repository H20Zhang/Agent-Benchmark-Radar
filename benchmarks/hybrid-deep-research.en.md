# HybridDeepResearch

## Measurement object

Tests whether agents preserve entities, filters and candidate sets while composing SQL database queries with web evidence.

## What changed compared with predecessors

Adds directional SQL-to-search, search-to-SQL and parallel-fusion handoffs rather than grading SQL and search independently.

## Protocol and comparison controls

S2SQL is graded by read-only execution and aligned result tables. SQL2S and parallel answers use an LLM judge. Pass@8 means at least one success in eight attempts; Avg@8 averages attempts. Web and frozen-corpus settings must remain separate.

## Decisive evidence and score ceiling

The repository distinguishes preview (paper results) from release: 88 questions were rewritten, with gold answers and reference SQL unchanged. The hard subset is not representative of all 380 tasks.

## Strongest confounders and limitations

The official blog dates the introduction June 3 while the README says June 2. Retain June precision until reconciled; the September 8 paper is a later event, not the benchmark launch. Judge, hints, search backend and retry budget remain confounders.

## Coverage gap and next experiment

Public SQLite development and governed Snowflake evaluation are different environments; scores do not isolate the cross-source handoff mechanism.

Compare no bridge hint, oracle bridge entity and full reference handoff under the same model and budget. This separates entity transfer from failures inside either SQL or search.

## Genealogy and use

[LiveSQLBench](livesqlbench.en.md) · [DataSpace](dataspace.en.md) · [FDABench](fdabench.en.md)

This entry is an `early_signal`: acceptance of a useful evaluation object does not promote one paper into a durable field-map claim.

## Primary sources and version

[Paper](https://arxiv.org/abs/2609.09410) · [Reviewed full text](https://arxiv.org/html/2609.09410v1)

[code](https://github.com/Snowflake-AI-Research/HybridDeepResearch)

[data](https://huggingface.co/datasets/Snowflake/HybridDeepResearch)

[Earlier announcement](https://www.snowflake.com/en/blog/engineering/hybrid-deep-research-benchmark/)

First public event: **2026-06**. Reviewed: **2026-09-17**. Source release and Radar acceptance are separate events.

[中文](hybrid-deep-research.md) · [Complete index](../library/README.en.md)
