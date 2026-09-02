# BIRD: text-to-SQL grounded in large, dirty database contents

[中文](bird.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2305.03111) · [Project](https://bird-bench.github.io/)

## What it actually measures

BIRD evaluates text-to-SQL against **large database contents**, external knowledge, dirty values, and query efficiency. It contains 12,751 question–SQL pairs over 95 databases totaling 33.4 GB across 37 professional domains.

## What changed relative to prior evaluation

Spider makes unseen schema the main difficulty but abstracts away much of the database-content problem. BIRD adds value grounding: the language in a question may not directly match stored values, data can be noisy, external knowledge may bridge the gap, and two correct SQL queries can have very different execution costs.

## Decisive evidence

The original paper reports ChatGPT + chain-of-thought at 40.08% execution accuracy on test with external knowledge, versus 92.96% human performance. It also introduces efficiency analysis rather than treating all executable correct SQL as equivalent.

## What the score supports

BIRD supports claims about realistic database-value comprehension plus SQL generation. It still does not establish enterprise-agent competence: the task begins with a defined database rather than requiring cross-system discovery, metadata search, or multi-step workflow execution.

## Fair comparison contract

Fix database snapshot, external-knowledge access, schema/value retrieval policy, SQL engine, model, and execution budget. Report execution accuracy and efficiency separately. Value retrieval is part of the measured system and must not be silently replaced with oracle matches.

## What remains unmeasured

Business semantics, permissions, schema drift, multiple database systems, write operations, and clarification are outside the main protocol. Large database size is not the same as a large enterprise catalog.

## Next discriminating validation

Measure whether a BIRD-tuned system transfers to Spider 2.0 and LiveSQLBench without changing its schema/value retrieval strategy. This tests whether value grounding is a reusable capability or benchmark-specific engineering.

## Genealogy

`unseen schema → database-value grounding → enterprise metadata/workflow reasoning`

BIRD is the step where text-to-SQL stops being only semantic parsing and becomes partly a data-retrieval problem.