# MC-Search: multimodal agentic RAG needs planning, modality choice, and hop-level evidence evaluation

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-02-22<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2603.00873)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](mc-search.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

Reviewed the stated primary paper in full for methods, experimental setup, results and limitations; no independent reproduction.

Read Sections 1–6 and ethics/reproducibility statements; appendices inspected: A–P, all examples, fixed-step baselines, verification, judge studies, training, soft HPS, top-k experiments, case studies, topology proof and prompts; visual checks: Equation 5 absolute-value RD and Table 4 counts verified on rendered pages 5 and 9. Not performed: No code/data or split verification; unresolved table inconsistencies retained

[arXiv 2603.00873v1 — arXiv v1, 2026-03-01; PDF marked ICLR 2026](https://arxiv.org/pdf/2603.00873v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## What changes relative to nearby evaluations

The following is an editorial protocol comparison, not an assertion of direct inheritance unless stated.

Relative to text-only multi-hop QA, MC-Search crosses text and images and labels multiple path topologies. Modality choice and evidence paths become explicit measurements beyond final answers; training gains still require split and path-equivalence checks.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

Approximately 21,000 questions are synthesized from Wikipedia text/image clusters across five structures: text-only, image-initiated, text-initiated, parallel image–text forks and multi-image forks. HAVE removes each evidence item and measures the answer-F1 drop, then checks whether intermediate entities guide later subquestions so navigational steps are retained. Qwen2.5-VL-7B filtering, Gemini-Pro shrinking/revision and Gemini-Flash rechecking yield 3,333 questions averaging 3.79 hops. Each agent iteration selects text-to-text, text-to-image or image-to-image retrieval, generates a sub-answer and chooses whether to continue. Search-Align turns verified chains into conversational process supervision for open-model fine-tuning.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Conditions needed to interpret the results

The knowledge base contains 389,750 images and 784,473 text documents. Topology counts are 945 text-only, 1,306 image-initiated, 169 text-initiated, 680 parallel image–text and 233 multi-image. Main runs use top-one retrieval and shared prompts; exact maximum iterations and decoding values are not fully listed, while proprietary thinking budgets stay at defaults. Answer F1 is token overlap×100. HPS is the percentage of gold-step evidence recovered, deduplicated. RD is the absolute predicted-minus-gold step-count difference, distinct from signed ΔStep. Gemini-2.5-Pro judges accuracy, entities, coherence and alignment on 0–5 scales. Search-Align uses LlamaFactory on four A100s: InternVL trains one epoch at 1e-5, Qwen two at 1e-4. A validation split is mentioned, but train/evaluation sizes and leakage-control details are not specified.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Process supervision on image-initiated chains

The image-initiated category contains 1,306 questions, but exact train/validation denominators are unspecified. Retrieval is top one; F1/HPS use 0–100 scales and RD is mean absolute step-count difference. These are reported results without independently verified leakage control.

| Qwen2.5-VL-7B | Answer F1 | HPS | RD |
|---|---|---|---|
| Base | 26.3 | 16.51 | 4.04 |
| Search-Align | 45.7 | 33.59 | 0.7 |

Source: Table 3; Appendix I · [Paper](https://arxiv.org/pdf/2603.00873v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Exact evidence identity versus semantic matching

The text-only category has 945 questions; the precise evaluated subset size is not restated in the table. HPS is gold-step evidence recovery×100. Relaxing the similarity threshold raises the metric without creating new retrieval capability.

| Gemini-2.5-Pro text-only criterion | HPS |
|---|---|
| Exact match | 21.59 |
| Similarity at least 0.85 | 41.26 |

Source: Appendix J Table 13 · [Paper](https://arxiv.org/pdf/2603.00873v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:interpretation:START -->
## What the comparisons establish

For image-initiated chains, Search-Align raises Qwen2.5-VL-7B F1 from 26.30 to 45.70 and HPS from 16.51 to 33.59 while reducing RD from 4.04 to 0.70. This supports gains in the reported setting, subject to unresolved train/validation split details. HPS is not general factual correctness: Gemini-Pro text-only HPS increases from 21.59 under exact matching to 41.26 at similarity threshold 0.85, showing sensitivity to gold-evidence identity. Training also does not improve every process metric: InternVL text-only HPS falls from 21.81 to 20.54 despite higher F1.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source discrepancies and next test

Filtering depends on a few model families and removes same-cluster alternative evidence to enforce unique chains, potentially penalizing valid open-search paths. HAVE thresholds, train/evaluation isolation and complete retrieval configuration require implementation verification. Human validation covers only 100 Gemini-Pro predictions, and cross-judge rescoring also uses that backbone, so neither establishes fairness across all generators. Next, publish explicit splits and alternative evidence sets, test cross-domain transfer at matched budgets, and add token, latency and human evidence-sufficiency measures.

Table 4 InternVL image counts do not add: 977+7=984, whereas the overall numerator is 861. Several percentages also do not exactly match displayed fractions. Do not infer an overall image coverage rate from this inconsistent block. Qwen aligned Multi-Images Fork HPS is 38.01 in Table 3 but 41.20 in Table 14 for retrieval@1. Gemini-Flash strict-HPS values in Table 13 differ from Table 3; Gemini-Pro values match and are used in selected evidence. The paper calls Golden F1 an upper bound, but it is an oracle-information condition rather than a mathematical upper bound; some trained results exceed the displayed untrained Golden F1. The five-topology completeness proof is conditional on linear or single-fork graphs and treats text-only forks as reducible; it does not cover unrestricted agent DAGs. The text calls fixed two-hop baselines consistently better than single-hop and agentic generally stronger, but Table 5/6 contains counterexamples.
<!-- EVIDENCE:limitations:END -->

Related benchmarks: [merrin](merrin.en.md) · [visdocagentbench](visdocagentbench.en.md)
