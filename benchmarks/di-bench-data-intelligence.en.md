# DI-Bench (Data Intelligence)

## Measurement object

Tests analytical computation with retrieved business rules using executable ground truth and a graph-based benchmark-generation protocol.

## What changed compared with predecessors

Compared with SQL correctness alone, makes business-rule application and in-domain task generation explicit evaluation targets.

## Protocol and comparison controls

The pipeline links tables, dimensions, metrics and documents, executes gold queries, then validates generated questions. Agents receive the schema and SQL/knowledge tools with a 20-turn budget. LLM-based task admission must not be confused with final-answer grading.

## Decisive evidence and score ceiling

On the matched 175-task rule-grounded slice, the reported average is 32.5% with rules and 32.7% with oracle rules, versus 52.9% for the no-rule counterparts. This localizes a problem beyond rule retrieval on that slice, not universally.

## Strongest confounders and limitations

This is the data-intelligence DI-Bench, not the similarly named dependency-inference benchmark. The public paper defines a reusable construction/evaluation protocol; an independently runnable task-package download was not verified in this review.

## Coverage gap and next experiment

Two domains with constructed business documents do not establish generalization to real enterprise governance or undocumented rules.

Keep matched rule/no-rule questions and audit the executed computation against a rule trace. Add genuine enterprise documentation before claiming realistic organizational transfer.

## Genealogy and use

[FDABench](fdabench.en.md) · [WarehouseReliabilityBench](warehouse-reliability-bench.en.md)

This entry is an `early_signal`: acceptance of a useful evaluation object does not promote one paper into a durable field-map claim.

## Primary sources and version

[Paper](https://arxiv.org/abs/2609.05776) · [Reviewed full text](https://arxiv.org/html/2609.05776v1)

First public event: **2026-09-04**. Reviewed: **2026-09-17**. Source release and Radar acceptance are separate events.

[中文](di-bench-data-intelligence.md) · [Complete index](../library/README.en.md)
