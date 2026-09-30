# RAGTruth: moving RAG hallucination evaluation from answer-level to word-level

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2024-01<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2401.00396)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](ragtruth.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

Reviewed the stated primary paper in full for methods, experimental setup, results and limitations; no independent reproduction.

main sections 1–7; Appendices A–C: examples, generation/detection prompts; Tables 1–10; Tables 5–6 visually verified

[arXiv v1 — v1, PDF header 2023-12-31](https://arxiv.org/pdf/2401.00396v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## What changes relative to nearby evaluations

The following is an editorial protocol comparison, not an assertion of direct inheritance unless stated.

Compared with RGB’s controlled stress tests, RAGTruth locates unsupported spans in actual model responses using human annotation. It shifts from whole-question correctness to hallucination location and detector quality; response selection remains distinct from active retrieval repair.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

2973 inputs generate 17838 responses from six models. Humans annotate evident/subtle conflict or unsupported additions. Incorrect refusals and null-as-false cases receive separate controls.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Conditions needed to interpret the results

The test contains 450 source instances, 150 per task, with six model responses per instance rather than only 450 responses. The detector uses Llama2-13B LoRA with learning rate 3e-4, three epochs and four A100 GPUs. Response F1 detects hallucination presence; span F1 measures character overlap, not token or exact-span match. The SelfCheck comparison uses responses from five other models rather than repeated samples from the same model.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Detection versus localization

The test has 450 source instances, 150 per task, with multiple model responses per instance; F1 is in percent, at response level for hallucination presence and span level for character overlap.

| Method | Response_F1 | Char_span_F1 |
|---|---|---|
| GPT-4-turbo prompt | 68.3 | 32.7 |
| Finetuned Llama2-13B | 80.7 | 54.8 |

Source: Tables 5–6 · [Paper](https://arxiv.org/pdf/2401.00396v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Selection reduces hallucination with coverage loss

Paired Llama 2-7B and Mistral 7B candidates for 450 source instances; returned count is in responses, and hallucination rate is a percentage of responses actually returned in each row.

| Selection | Returned_count | Hallucination_rate |
|---|---|---|
| Random | 450 | 55.1 |
| Fewest detected spans | 450 | 43.1 |
| No detected spans | 326 | 23.9 |

Source: Table 7, section 6.3 · [Paper](https://arxiv.org/pdf/2401.00396v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:interpretation:START -->
## What the comparisons establish

The paper tests candidate selection, not active search/revision. No-detected-span selection returns 326/450; report coverage alongside hallucination.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source discrepancies and next test

v1 lacks sufficient quantified annotation agreement; tasks/six generators bound distribution. Next: held-out generators/domains and completeness-aware repair.

Table 6 fine-tuned span F1=54.8; §6.2 prose says 48.4. Preserve table attribution. Table 7 group 2 random 10.4→fewest 5.3 is labelled 41.0% reduction; rounded cells imply~49%, unresolved.
<!-- EVIDENCE:limitations:END -->

Related benchmarks: [ragbench](ragbench.en.md) · [claimprobe](claimprobe.en.md)
