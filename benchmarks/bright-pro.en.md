# Bright-Pro: retrieval should cover complementary reasoning aspects, not just relevant passages

<!-- RELEASE-REFERENCE:START -->
> **Historical paper reference (initial version unverified)** · 2026-05-05 · historical paper snapshot<br>
> **BGE-Reasoner-8B — α-nDCG@25: 68%** (Static retrieval · Overall α-nDCG@25)<br>
> Selected original-track results; metrics, subsets, and systems are not pooled into one winner. [Original source](https://arxiv.org/abs/2605.04018)<br>
> From a previously curated original-paper record, for historical reference; not rerun in this update and not current SOTA.
<!-- RELEASE-REFERENCE:END -->

[中文](bright-pro.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

Reviewed the stated primary paper in full for methods, experimental setup, results and limitations; no independent reproduction.

Read Sections 1–7 and limitations; appendices inspected: A–H, metric formulas, reference validation, prompts, decoding, all seven dataset examples, full result tables and five qualitative trace cases; visual checks: Tables 3–4 checked on rendered PDF page 8. Not performed: No training or evaluation rerun; no repository audit

[ACL 2026 — ACL 2026 proceedings, pp. 36776–36806; no claim of arXiv v1 equivalence](https://aclanthology.org/2026.acl-long.1705.pdf)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## What changes relative to nearby evaluations

The following is an editorial protocol comparison, not an assertion of direct inheritance unless stated.

Bright-Pro extends BRIGHT-style reasoning relevance with weighted aspects and coverage/generation evaluation. The question becomes whether evidence combinations cover required facets, allowing static ranking and agent answer quality to order systems differently.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

Experts re-audit evidence from seven BRIGHT StackExchange domains, decompose each query into complementary reasoning aspects, and normalize 1–5 importance ratings. Weak evidence is removed, overlapping same-source passages are merged, new evidence is collected, and a second domain annotator reviews each example. Static evaluation covers 739 queries: α-nDCG with α=0.5 discounts repeated hits on the same aspect, while weighted aspect recall credits the importance of aspects covered at least once. Agentic evaluation uses the same 175 questions, retrieving five passages per round under either exactly one to three rounds or adaptive stopping. RTriever-Synth contains 140,000 query bundles built by decomposing reference answers into aspects and generating complementary positives and topically close negatives that omit essential evidence. Actual training still samples one positive and one negative per query per step to LoRA-tune Qwen3-Embedding-4B.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Conditions needed to interpret the results

Static evaluation uses 739 questions; agentic evaluation fixes 175, twenty-five per domain. Each call returns five passages capped at 2,048 tokens using Qwen3-0.6B tokenization, without a full-document reader. GPT-5-mini-08-07 uses medium effort and output limits of 30,000 per turn and 10,000 final tokens; Qwen3.5-122B-A10B-GPTQ-Int4 runs on vLLM 0.19.1 with 25,600/12,800 limits. Fixed runs take exactly one to three rounds; adaptive runs cap at 100. GPT-5 generates references and judges: aspect coverage 0/0.5/1 is weight-averaged to w and mapped to round(4w+1) for completeness; overall quality is 1–5. Per-example AER is quality×exp[-0.05(R−1)].
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Static ranking versus three-round answer ranking

Static evaluation uses 739 queries and α-nDCG×100; three-round evaluation uses 175 queries and GPT-5-mini with top five passages per round. Overall quality is the mean GPT-5 judge score on a 1–5 scale. Values across these protocols are not direct gains.

| Retriever | Static alpha-nDCG@25 | Round-3 alpha-nDCG@15 | Round-3 overall |
|---|---|---|---|
| BGE-Reasoner-8B | 68.0 | 63.04 | 4.31 |
| DIVER-4B-1020 | 63.7 | 51.56 | 4.16 |
| DIVER-4B | 59.9 | 53.08 | 4.29 |
| RTriever-4B | 55.3 | 50.79 | 4.25 |

Source: Table 2 and Table 3 · [Paper](https://aclanthology.org/2026.acl-long.1705.pdf)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Adaptive quality and search rounds

The same 175 queries with GPT-5-mini; rounds are per-query means, quality is on a 1–5 scale, and AER averages per-example quality discounted by exp[-0.05(R−1)]. It cannot be reconstructed exactly from the reported means.

| Retriever | Mean rounds | Overall quality | AER |
|---|---|---|---|
| BGE-Reasoner-8B | 5.1 | 4.43 | 3.65 |
| GTE-7B | 6.67 | 4.51 | 3.44 |
| BM25 | 5.73 | 4.42 | 3.53 |

Source: Table 4; Equation 1 · [Paper](https://aclanthology.org/2026.acl-long.1705.pdf)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:interpretation:START -->
## What the comparisons establish

Static rankings do not fully survive agent integration: DIVER-4B-1020 has higher static α-nDCG@25 than DIVER-4B, yet lower GPT-5-mini answer quality after three fixed rounds, 4.16 versus 4.29. Under adaptive stopping, GTE-7B has higher answer quality than BGE, 4.51 versus 4.43, but needs 6.67 rather than 5.10 rounds and scores 3.44 rather than 3.65 on AER. AER discounts quality by round count; it is not a measurement of tokens, dollars or latency, so quality and rounds should remain visible.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source discrepancies and next test

The full static set differs from the 175-question agentic subset, and static α-nDCG@25 is not directly comparable with cumulative @5/@10/@15 across rounds. The reported κ=0.742 validates importance ratings on 50 questions only. Reference validation on 40 examples uses one author as rater and does not establish independent human agreement with the final judge. Expert-added aspects can favor broader answers than a narrow reading of the question. Next, add the untouched 4B base and matched-budget training ablations, paired confidence intervals, independent judges, and measured token, latency and repeated-evidence costs.

The abstract and conclusion claim substantial improvement over the Qwen3-Embedding-4B base, but reviewed result tables include Qwen3-8B rather than an untrained Qwen3-4B control. A causal training gain over the exact base is not numerically established here. Appendix F initially calls LLM-side settings shared, but specifies different per-turn and final output limits across GPT and Qwen backends. Matching is within backend, not equal compute across backends. Section 6.2 says the upper tier is 4–14 points above every general embedder, whereas Table 2 includes BGE 68.0 versus Qwen3-8B 49.5, an 18.5-point gap. Use table rows rather than the range. The note’s exact totals of 2,763 aspects and 5,272 gold passages are not directly reported in the reviewed paper tables, which give rounded per-query averages. They require dataset verification; do not present them as paper-verified counts.
<!-- EVIDENCE:limitations:END -->
