# DABstep: multi-step financial analysis with objective final grading

[中文](dabstep.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2506.23719) · [Benchmark](https://huggingface.co/spaces/adyen/DABstep)

## What it actually measures

DABstep evaluates **realistic multi-step data analysis** derived from a financial analytics platform. More than 450 challenges require code-based processing of transaction data together with contextual reasoning over heterogeneous documentation, cross-source lookup, and precise result reporting.

## What changed relative to prior evaluation

Many open-ended analytics benchmarks rely heavily on LLM judges. DABstep keeps a longer agentic workflow but ends in factoid-style answers with automatic correctness checks, making objective grading compatible with realistic multi-step analysis.

## Decisive evidence

Even the best evaluated agent achieves only 14.55% accuracy on the hardest tasks. The environment includes transaction records plus fee structures, merchant metadata, category/country lookup tables, and documentation, so success requires both executable data manipulation and semantic cross-referencing.

## What the score supports

DABstep strongly supports end-to-end analytical execution under a bounded financial data workspace. It does not isolate planning, code quality, documentation retrieval, or semantic interpretation, and its synthetic benchmark environment should not be confused with access to real financial systems.

## Fair comparison contract

Fix benchmark version, files/documentation, tool interface, model, trajectory/call budget, and final scorer. Report difficulty slices separately. A system preloaded with parsed lookup relations or hand-built semantic mappings is solving an easier cross-source problem.

## What remains unmeasured

Production financial analytics includes live schemas, permissions, PII, governance, write actions, audit trails, and changing business logic. Factoid grading also does not capture the quality of a complete analyst-facing deliverable.

## Next discriminating validation

Add deterministic intermediate checkpoints for source selection, joins/mappings, and computed quantities before the final answer. This would retain objective grading while locating where multi-step workflows fail.

## Genealogy

`single-table analysis → heterogeneous documented workspace → objectively graded multi-step data agent`

DABstep shows that realistic agentic analysis need not require fully subjective evaluation.