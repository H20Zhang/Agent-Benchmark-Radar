# ChemCLIR-Bench: diagnosing language-pair and ranking-depth failures in patent retrieval

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-09-19<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2609.23231)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](chemclir-bench.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

Reviewed the stated primary paper in full for methods, experimental setup, results and limitations; no independent reproduction.

Read Complete official HTML Sections 1–5, metrics, uncertainty and limitations, checked with same-version PDF; appendices inspected: A.1–A.4 and all supplemental figures/prompts; HTML omitted prompt bodies S.5–S.9, fully read from recovered PDF; visual checks: PDF Figures 2–3 inspected on rendered pages 6–7. Not performed: No model rerun or independent patent-family equivalence audit

[arXiv v1, 2026-09-19](https://arxiv.org/pdf/2609.23231v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## What changes relative to nearby evaluations

The following is an editorial protocol comparison, not an assertion of direct inheritance unless stated.

Unlike language-local MIRACL and English-domain ChemTEB, this controls target identity through patent variants and isolates foreign-language routes. It diagnoses parallel-document retrieval rather than complete prior-art search or scientific QA.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

Relevance links each generated query to language versions of its source patent. Google Patents supplies 23,787 title/abstract versions and 524 queries; EPO supplies 11,315 title/abstract/first-claim versions and 198 queries. EPO covers English/German/French; Google’s Chinese coverage adds 400 GPT-5.5 translations. GPT-5-mini generates three candidates and Sonnet 4.6 selects by faithfulness and query quality. Existing-language, missing-language and all-language modes create both dual-gold and no-home queries. Gold labels recover source versions, not every topically relevant patent.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Conditions needed to interpret the results

Eight sub-billion embedders lack complete checkpoint, prefix, truncation and index specifications. Recall is language-macro-averaged within eligible same/cross-gold queries; Google’s 261 same-gold versus 524 cross-gold queries are not fully paired. Paired analyses use 261 Google plus 198 EPO dual-gold queries. Pooled depth diagnostics use those 459: the 80th percentiles of first same, first foreign and maximum paired rank, censored beyond 1,000; ± denotes bootstrap standard error. XRC compares depths at equal coverage, RRC is foreign-gold any-hit rate, and ARI partitions the top-K shortfall by what remains missing at 1,000.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Same-language strength need not transfer

Language-macro recall on eligible routes; Google 261 same/524 cross queries, EPO 198 dual-gold queries. Source-patent versions define relevance; different denominators prevent a direct paired interpretation.

| Model | Google same R@10 | Google cross R@10 | EPO same R@10 | EPO cross R@10 |
|---|---|---|---|---|
| embeddinggemma | 0.74 | 0.54 | 0.7 | 0.52 |
| bge-m3 | 0.64 | 0.47 | 0.71 | 0.47 |
| e5-large-instruct | 0.73 | 0.09 | 0.63 | 0.12 |

Source: Table 2 · [Paper](https://arxiv.org/pdf/2609.23231v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:interpretation:START -->
## What the comparisons establish

Embeddinggemma leads foreign-version recall, while e5’s strong same-language scores conceal weak cross-language retrieval. However, the seven-percent residual beyond the top thousand is only unrecoverable by reranking that fixed pool. It does not prove permanent irretrievability or isolate alignment as the sole cause. Deeper first-stage retrieval, translation, hybrid search and version-equivalence auditing could change it.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source discrepancies and next test

Patent versions need not be claim-equivalent; language tags do not establish native authorship. The small translation and near-ceiling single-rater quality audits cannot certify all items or poor-query detection. Rank depth is not measured time, tokens or money, and no actual reranker is tested. Next disclose configurations and family/route denominators, audit parallel equivalence, pair content-matched queries and compare translation, lexical/hybrid retrieval and deeper pools.

Human quality audit is 106/mean 8.40 in the main text,106/mean 8.33 in FigureS.2 and 97 in agreement/limitations. Cohort/mean differences are not reconciled. The general statement that every recall averages five languages does not apply literally to EPO, whose queries are only 72 English,58 German and 68 French. EPO prose calls 11315 granted specifications each a triple, while Table 1 defines 11315 corpus documents as single-language versions; use the table unit, not 11315×3. E5 is excluded by a cross-recall<.10 gate despite EPO .12; the exact corpus/aggregation governing this exclusion is not stated. The source’s alignment-only irreducible floor is operationally a top 1000 miss rate; cause and irreducibility beyond that cutoff are not identified.
<!-- EVIDENCE:limitations:END -->

Related benchmarks: [beir](beir.en.md) · [ontologybench](ontologybench.en.md) · [commercial-tax](commercial-tax.en.md)
