# WikiSQL: executable text-to-SQL at scale, before cross-schema reasoning

[中文](wikisql.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/1709.00103)

## What it actually measures

WikiSQL evaluates natural-language-to-SQL generation over **single Wikipedia tables** with executable supervision. The original release contains 80,654 manually annotated question–SQL pairs over 24,241 tables and focuses on a constrained SQL grammar without multi-table joins.

## What changed relative to prior evaluation

Before WikiSQL, semantic-parsing datasets were much smaller and often tied to limited domains. WikiSQL made execution-grounded text-to-SQL large enough for neural training and evaluation, while Seq2SQL also used database execution as a learning signal for unordered query components.

## Decisive evidence

The Seq2SQL paper reports execution accuracy improving from 35.9% for an attentional sequence-to-sequence baseline to 59.4%, with logical-form accuracy improving from 23.4% to 48.3%. The benchmark therefore demonstrated both the value of SQL structure and the usefulness of execution as supervision.

## What the score supports

WikiSQL scores support competence at mapping a question to a simple executable query over one known table. They are weak evidence for enterprise database agents: schema discovery, joins, nested queries, business semantics, database values, and workflow planning are largely absent.

## Fair comparison contract

Fix the official split, table contents, SQL grammar, execution engine, and whether execution-guided decoding is allowed. Report execution accuracy separately from exact logical-form matching because semantically equivalent SQL can differ syntactically.

## What remains unmeasured

The benchmark does not test generalization to complex unseen multi-table schemas in the sense later introduced by Spider, nor data cleaning, external knowledge, dialect differences, or interactive database exploration.

## Next discriminating validation

Use WikiSQL mainly as a controlled lower rung in a scaling curve—single table → unseen multi-table schema → large dirty database → enterprise workflow—rather than as a frontier endpoint.

## Genealogy

`natural-language database query → executable single-table SQL → cross-domain schema generalization`

WikiSQL is important as a foundation precisely because later benchmarks expose how much its constrained setting leaves out.