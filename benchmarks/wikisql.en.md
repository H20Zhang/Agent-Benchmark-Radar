# WikiSQL: single-table SQL generation on held-out tables

<!-- RELEASE-REFERENCE:START -->
> **Best at release (historical reference)** · 2017-08-31 · paper v1<br>
> **Seq2SQL — Execution accuracy: 60.3%**; **Seq2SQL — Logical-form accuracy: 49.2%**<br>
> Initial-version Seq2SQL execution and logical-form accuracy, with 87,726 examples in v1. The later v7 values 59.4% / 48.3% and 80,654 examples are separate revision evidence. [Original source](https://arxiv.org/abs/1709.00103v1)<br>
> Historical difficulty reference, not current SOTA; tasks, versions, and experimental conditions are not interchangeable.
<!-- RELEASE-REFERENCE:END -->

[中文](wikisql.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and versions

Full substantive paper and appendix reading completed for the stated primary version; experiments were not independently reproduced.

Read all substantive main text and Appendices A–C of both v1 and v7, including collection, baseline details and predictions.

[arXiv 1709.00103v7 · 2017-11-09](https://arxiv.org/pdf/1709.00103v7) · [arXiv 1709.00103v1 · 2017-08-31](https://arxiv.org/pdf/1709.00103v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## What the method measures

WikiSQL holds out tables but restricts each query to one table. Seq2SQL separates aggregation and selection, then trains WHERE generation with execution rewards. That feedback is a training mechanism, not inference-time repair.

<!-- EDITORIAL-METHOD:START -->
Questions originate from SQL templates over Wikipedia HTML tables, followed by crowd paraphrasing and verification. Outputs are restricted to a selected column, optional aggregation and WHERE conditions, without joins. An illustrative input is an athlete table and a request for one country’s mean age; the output selects age, applies AVG and filters country. Seq2SQL restricts pointer outputs, predicts aggregation/selection separately and learns conditions with execution reward. Since reordering conditions need not change meaning, reward-based learning addresses a weakness of imitating only one reference sequence.

Editorial placement: compared with generic sequence-to-sequence semantic parsing, WikiSQL combines larger table-disjoint evaluation with executable supervision. Spider extends the coordinate to multi-table and nested SQL. The contribution concerns training objectives and structured decoding, not an already interactive database agent.
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental setup

The v7 dataset contains 80,654 examples over 24,241 tables. Training runs for at most 300 epochs with development-execution early stopping. Inference uses question and schema; table contents support training rewards and evaluation.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## Selected quantitative evidence

V7 Table 2; table-disjoint test split; EX = execution accuracy, LF = logical-form accuracy, both percentages of test examples. Same training/evaluation family.

| System / comparison | Dataset / denominator | Metric / unit | Result | Conditions | Source |
| --- | --- | --- | --- | --- | --- |
| Aug Ptr Network | WikiSQL v7 test | EX / LF (%) | 53.3% / 43.3% | Restricted pointer outputs | Table 2, p. 7 |
| Seq2SQL (no RL) | WikiSQL v7 test | EX / LF (%) | 57.1% / 47.4% | Structured decoder; teacher forcing | Table 2, p. 7 |
| Seq2SQL | WikiSQL v7 test | EX / LF (%) | 59.4% / 48.3% | WHERE policy gradient after pretraining | Table 2, p. 7 |

Fact source: [Table 2, p. 7](https://arxiv.org/pdf/1709.00103v7)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and interpretation

The no-RL comparison supports a 2.3-point EX gain within v7, while the full baseline gap bundles changes. The header gives true v1 values, EX 60.3% and LF 49.2%, with 87,726 examples and a 100-epoch cap; the body uses v7’s 80,654 examples and 300-epoch cap. Keep them separate. LF can reject equivalent SQL; EX can accept accidental result agreement.

<!-- EDITORIAL-NEXT:START -->
Next, hold the pointer architecture and split fixed while changing only WHERE supervision, then perturb table contents to expose accidental result equality. Add join tasks separately to test transfer instead of extrapolating cross-database capability from single-table scores.
<!-- EDITORIAL-NEXT:END -->
<!-- EVIDENCE:limitations:END -->
