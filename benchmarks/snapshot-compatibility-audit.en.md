# Snapshot Compatibility Audit

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-08-24<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2608.22856)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](snapshot-compatibility-audit.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

Reviewed the stated primary paper in full for methods, experimental setup, results and limitations; no independent reproduction.

Read Complete Sections 1–7, equations 1–8, all results tables/figures and ethical/validity discussion; appendices inspected: No separate appendices; detailed prompts and ledgers are artifact references rather than printed templates. Not performed: No artifact verification, semantic relabeling or experiment rerun

[arXiv v1, 2026-08-24](https://arxiv.org/pdf/2608.22856v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## What changes relative to nearby evaluations

The following is an editorial protocol comparison, not an assertion of direct inheritance unless stated.

Compared with controlled-noise tests such as RGB and accuracy-only corpus-scaling studies, this audit changes corpus access while measuring within-state repeat noise. It adds behavioral compatibility: answer distributions can move despite little net utility change.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

The audit asks whether a fixed single-turn retriever-generator preserves answers after a corpus-snapshot change. Each question receives two independent generations at each endpoint. Average the two within-snapshot similarities as w and the four cross-snapshot similarities as c; mean w−c is excess answer churn D. Subtracting repeat noise yields an agreement gap, not the proportion of questions that changed. Normalized exact equality and blinded semantic equivalence are co-primary measures. Under equality, population D is half the squared difference between answer distributions; semantic judgments need not be positive-semidefinite or transitive, so their gap is not automatically MMD. A post-hoc strict flip requires semantic agreement within each endpoint and disagreement for all four cross-endpoint pairs.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Conditions needed to interpret the results

Confirmatory NQ uses four hundred hash-selected questions after excluding 2,400 development IDs; supportive TriviaQA independently uses two hundred. DeepResearchGym exposes fixed FineWeb prefixes of zero, one, three and seven shards. Each nonzero condition retrieves eight documents from the unchanged question, rendering at most 1,200 whitespace-compacted characters each. This is neither an iterative agent nor a temporal refresh. Main deepseek-v4-flash runs as independent singleton sessions through a Claude CLI DeepSeek adapter at low effort without tools or session persistence. Temperature/top-p are unset and provider-default numbers unrecorded. Answers are capped at 512 UTF-8 bytes. A blind semantic judge labels all twenty-eight pairs of eight anonymous answers before gold is unlocked for EM/F1. Fifty thousand whole-question bootstrap draws preserve repeated-output clusters. Confirmation requires exact D≥3 points and positive one-sided 95% lower bounds for both kernels.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Excess churn after repeat-noise subtraction

NQ has four hundred questions, TriviaQA two hundred; deepseek-v4-flash, one-to-seven shards, two independent generations per state and fifty thousand question-cluster bootstrap draws. Agreement columns are percentages; differences and intervals are percentage points. TriviaQA is supportive and unpooled.

| Study / kernel | Within agreement percent | Cross agreement percent | Excess churn pp | 95% two-sided CI pp |
|---|---|---|---|---|
| NQ / exact | 25.25 | 18.813 | 6.438 | [4.188, 8.750] |
| NQ / semantic | 89.125 | 78.875 | 10.25 | [7.188, 13.438] |
| TriviaQA / semantic | 96.75 | 94.625 | 2.125 | [0.125, 4.500] |

Source: Table 2 · [Paper](https://arxiv.org/pdf/2608.22856v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Small utility changes can hide answer changes

EM averages normalized exact matches over two answers; changes/churn are percentage points. Strict flips count questions and are post-hoc diagnostics. V4-Pro is a post-hoc joint same-family model/serving change; its EM-change interval [−2.00,8.50] does not establish significant improvement.

| Study / generator | Questions | EM change pp | Semantic excess churn pp | Strict semantic flips |
|---|---|---|---|---|
| NQ / V4-Flash | 400 | -1.5 | 10.25 | 40/400 |
| TriviaQA / V4-Flash | 200 | 1.25 | 2.125 | 5/200 |
| NQ subset / V4-Pro | 100 | 3.0 | 8.75 | 6/100 |

Source: Sections 5.2–5.4; Table 4 · [Paper](https://arxiv.org/pdf/2608.22856v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:interpretation:START -->
## What the comparisons establish

NQ cross-state semantic disagreement is 21.125 percent, but same-state repeat disagreement is already 10.875 percent; the corrected gap is 10.250 percentage points. Neither all raw disagreement nor a deterministic 10.25-percent changed-question rate is justified. Net EM falls only 1.50 points because forty-six match-to-nonmatch and thirty-four reverse transitions cancel among eight hundred matched-repeat pairs; another 155 pairs change between distinct EM-nonmatching answers. Strict semantic flips separately occur on forty of four hundred questions, thirty-five with all four outputs EM-nonmatching and thus invisible to EM. Changes can include improvements, aliases, ambiguity and errors; churn is not harm or an automatic release-blocking criterion.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source discrepancies and next test

One fixed shard path confounds scale with added-document identity and ranking. Two repeats are the minimum identifiable design, not a precise estimate of each answer distribution. Bootstrap intervals concern selected-question sampling, not alternate paths, dates or models. Retrieval EM is below closed-book EM at every main-study scale, so this is not an optimized production RAG stack. EM nonmatch need not be false, and semantic judgments can be style-sensitive without human validation. Next randomize multiple corpus paths, collect more repeats with recorded decoding controls, replicate across model families and real refreshes, and have humans assess factual and practical risks of high-impact flips.

No decisive numerical inconsistency found in the selected main tables. Exact output controls are intentionally interface-level: provider-default temperature and top-p values were not recorded. Absolute shard document/token counts and a fully specified retriever encoder/ranking configuration are not given in the reviewed paper; do not invent a universal sevenfold corpus-size effect. The semantic-judge robustness check is a fifty-question second-model audit, not human validation, and its raw execution trace was not retained. V4-Pro replication changes both generator and serving interface, and its four-answer judge packets differ from V4-Flash eight-answer packets; it is not a pure model ablation.
<!-- EVIDENCE:limitations:END -->

Related benchmarks: [crag](crag.en.md) · [rag-collapse](rag-collapse.en.md)
