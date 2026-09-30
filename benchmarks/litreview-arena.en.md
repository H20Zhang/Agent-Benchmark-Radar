# LitReview Arena / LitReviewBench / LitJudge

<!-- RELEASE-REFERENCE:START -->
> **Release diagnostic (historical reference)** · 2026-07-01 · paper v1 snapshot<br>
> **LitJudge — Spearman ρ: 0.792** (Correlation with expert utility judgments)<br>
> Evaluator correlation with human judgment, not a research-agent task score. [Original source](https://arxiv.org/abs/2608.21374)<br>
> From a previously curated original-paper record, for historical reference; not rerun in this update and not current SOTA.
<!-- RELEASE-REFERENCE:END -->

[中文](litreview-arena.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

Reviewed the stated primary paper in full for methods, experimental setup, results and limitations; no independent reproduction.

Read Sections 1–8 and impact statement; appendices inspected: A.1–A.11, complete protocols/prompts, specialized-system, backbone, biology and annotator analyses; visual checks: Figure 2 workflow and held-out-field radar inspected on rendered page 9. Not performed: No dataset/code audit or reconciliation of calibration splits and generation configurations

[arXiv 2608.21374v1 — arXiv 2608.21374v1; PDF margin dated 2026-07-01, inconsistent with identifier month; no date reconciliation](https://arxiv.org/pdf/2608.21374v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## What changes relative to nearby evaluations

The following is an editorial protocol comparison, not an assertion of direct inheritance unless stated.

Compared with DeepResearch Bench’s automated report rubrics and SciArena’s broader scientific tasks, LitReview Arena topic-matches review experts and collects dimension-specific preferences. Structure and research suggestions guide judge calibration, while factual correctness remains a separate requirement.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

Topics are extracted from over three thousand OpenAlex AI surveys published in 2022–2025 with more than fifty citations and converted into standardized review requests. One hundred five researchers with AI paper-writing experience are topic-matched and compare anonymous, randomly ordered drafts. They vote A/B/tie/both-bad with written reasoning on coverage, claim support, structure, research suggestions and overall utility. Approximately three thousand expert judgments each contain five outcomes, not fifteen thousand independent experts. Frozen battles yield BT/Elo-style rankings. Qwen3-235B-based LitJudge retrieves up to three structure-similar battles, three content-similar battles and three human-review gap anchors, using maximal marginal relevance for anchor relevance/diversity.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Conditions needed to interpret the results

The main leaderboard contains humans and nine systems. Generation prompts, tools/retrieval, dated versions, stopping budgets, total topics/per-pair denominators and human-draft production effort are not fully disclosed, preventing matched-budget agent ablations. Five hundred battles support meta-evaluation/calibration; the paper mentions twenty-percent held-out AI subfields without fully specifying battle/topic disjointness, self-example exclusion or same-topic anchor availability. Figure 2 explicitly draws corresponding human reviews as anchor inputs. Neutral expert labels receive half credit regardless of judge output, so reported accuracy is not ordinary four-class accuracy. Spearman measures system-ranking correlation, unlike expert pairwise agreement. The appendix specifies Elo initialization 1,500, K=32 and half-wins for ties, but not complete BothBad handling in leaderboard construction.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Expert relative ratings and generation tokens

Approximately three thousand five-dimensional expert judgments; exact per-system battle denominators are not given. Ratings are relative BT/Elo quantities, not percentages. Token counts are reported measured means without a clear input/output/tool breakdown; budgets are unmatched.

| System | Tokens per query thousands | Structure rating D3 | Research suggestions rating D4 | Overall rating D5 |
|---|---|---|---|---|
| Human | not reported | 1502.5 | 1521.5 | 1668.8 |
| GPT-5.2 | 38.096 | 1322.4 | 1272.7 | 1449.1 |
| Sonar Deep Research | 322.08 | 1262.1 | 1322.7 | 1285.9 |
| Claude Opus 4.5 | 5.49 | 1177.6 | 1099.9 | 1135.5 |

Source: Table 1 · [Paper](https://arxiv.org/pdf/2608.21374v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Calibration against equal-count random ICL

The five-hundred-battle calibration/meta-evaluation series has incompletely specified disjoint splits. Units are leaderboard Spearman correlations from −1 to 1, not battle accuracy. Random ICL uses the same example count.

| Qwen3-235B evaluator | D2 rank rho | D3 rank rho | D4 rank rho | D5 rank rho |
|---|---|---|---|---|
| Naive | 0.442 | 0.467 | 0.43 | 0.467 |
| Random few-shot ICL | 0.554 | 0.583 | 0.737 | 0.634 |
| LitJudge | 0.673 | 0.649 | 0.842 | 0.792 |

Source: Appendix A.8 Table 5 · [Paper](https://arxiv.org/pdf/2608.21374v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## Human and judge agreement are not one ceiling

All values are zero-to-one; neutral expert labels always receive half credit in judge–expert scoring. Exact effective pair counts are unspecified. Judge–judge compares Qwen and DeepSeek-V3.2; neither pairwise agreement column is Spearman.

| Dimension | Judge-expert adjusted accuracy | Expert-expert accuracy | Judge-judge accuracy |
|---|---|---|---|
| D3 Structure | 0.598 | 0.639 | 0.747 |
| D4 Suggestions | 0.62 | 0.556 | 0.739 |
| D5 Overall | 0.606 | 0.861 | 0.747 |

Source: Table 3 · [Paper](https://arxiv.org/pdf/2608.21374v1)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:interpretation:START -->
## What the comparisons establish

The 23.0-percent result pools all nonhuman systems’ 208 wins in 904 decisive human comparisons; it is not the strongest model’s win rate and excludes ties. GPT-5.2’s overall relative rating is 1,449.1 versus humans’ 1,668.8, but Elo is not ratio-scale performance, so a greater-than-sixty-percent agent advantage cannot be inferred from rating ratios. Qwen LitJudge raises D5 leaderboard correlation from 0.467 to 0.792, versus 0.634 for equal-example-count random ICL. This supports task-matched calibration over that control, not 79.2-percent instance accuracy or demonstrated human-level agreement.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source discrepancies and next test

Preference does not replace factual/citation verification, and human reviews are a reference group rather than an absolute ceiling. Relative ranks depend on opponents, topics, vote distribution and aggregation. Exact independent-topic counts, multi-rater coverage and confidence intervals are absent; 107 questionnaire respondents need not contradict 105 recruited annotators. Calibration may require corresponding human reviews, leaving cold-start judging unestablished. Biology lacks clear sample counts and Table 7 metric units, limiting cross-domain claims. Next lock topic-disjoint calibration data, disclose anchor provenance/self-example exclusion, match generation budgets, and report ordinary four-class instance metrics, ranking bootstraps and human factual audits.

Abstract calls 23% the strongest-system result, but Section 4.1 defines it as pooled nonhuman 208/904 decisive matches. Section 5.2 says expert agreement exceeds judge agreement on D3/D4, but Table 3 reports expert .639/.556 versus judge .747/.739, the opposite. Section 6.2 calls its alignment measure agreement accuracy while the numerical .467→.792 series is Spearman according to Table 5 and Figure 2. The claim comparable to inter-expert consistency compares ranking correlation with pairwise accuracy, unlike quantities. PDF date margin says July 1 although arXiv identifier is August; version/date provenance is unresolved.
<!-- EVIDENCE:limitations:END -->

Related benchmarks: [das-bench](das-bench.en.md) · [deepresearch-bench](deepresearch-bench.en.md)
