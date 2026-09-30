# KILT: making provenance part of knowledge-intensive evaluation on one snapshot

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2020-09<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2009.02252)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](kilt.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

Reviewed the stated primary paper in full for methods, experimental setup, results and limitations; no independent reproduction.

main sections 1–9; Appendix 11: annotation, mapping, retrieval/classifier details, interface; Tables 1–17; Table 4 visually verified

[v1,2020-09-04](https://arxiv.org/pdf/2009.02252v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## What changes relative to nearby evaluations

The following is an editorial protocol comparison, not an assertion of direct inheritance unless stated.

KILT maps previously separate knowledge-intensive tasks onto one Wikipedia snapshot. Shared provenance and evidence-gated scoring make comparisons more interpretable, without equalizing training budgets or eliminating incomplete provenance labels.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

Map 11 datasets/five tasks onto the 2019-08-01 Wikipedia snapshot (5.9M pages), using redirects and highest-BLEU span alignment; filter evaluation mappings below 0.5. Score output, retrieval and provenance-gated KILT metrics separately.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Conditions needed to interpret the results

DPR indexes 22,220,793 disjoint 100-word passages. BART+DPR uses the top three passages from a fixed DPR model; RAG uses five and updates the query encoder, so training also differs. KILT metrics retain the answer score only when R-precision=1 for at least one complete gold provenance set. The selected test sets contain 1,444 NQ and 5,569 HotpotQA questions. Scoring is reference- and provenance-based, without an LLM judge.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Answer-versus-provenance gap

Test denominators are 1,444 NQ and 5,569 HotpotQA questions; all metrics are percentages, and KILT-EM requires a correct answer plus R-precision=1 for at least one complete provenance set.

| Dataset / system | Answer_EM | R_precision | KILT_EM |
|---|---|---|---|
| NQ / BART+DPR | 41.27 | 54.29 | 30.06 |
| NQ / RAG | 44.39 | 59.49 | 32.69 |
| HotpotQA / BART+DPR | 25.18 | 25.04 | 1.96 |
| HotpotQA / RAG | 26.97 | 30.59 | 3.21 |

Source: Tables 2–4, Appendix Tables 13–14 · [Paper](https://arxiv.org/pdf/2009.02252v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:interpretation:START -->
## What the comparisons establish

A shared snapshot does not unify abilities: RAG HotpotQA EM 26.97 falls to provenance-gated 3.21. RAG versus fixed DPR also changes training and passage count.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source discrepancies and next test

All tasks are designed to be answerable inside the knowledge base. Provenance can be incomplete or extended after system outputs are seen. Human provenance annotation agreement is κ=0.3 for NQ and κ=0.1 for ELI5. Next, match passage counts and expand equivalent provenance labels.

Appendix discusses BERT+DPR classifier whereas one main-text sentence says BART+DPR; use method/table naming.
<!-- EVIDENCE:limitations:END -->

Related benchmarks: [beir](beir.en.md) · [crag](crag.en.md)
