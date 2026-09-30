# CrossModalQA

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-08-31<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2609.05518)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](crossmodalqa.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

Reviewed the stated primary paper in full for methods, experimental setup, results and limitations; no independent reproduction.

Read Sections 1–5, construction, path/hop definitions, retrieval/generation metrics and all comparisons; appendices inspected: A–D, sampling algorithm, implementation, micro-aggregation, hop analyses, mini oracle and every generation prompt. Not performed: No implementation audit, human validation or model rerun; generator/judge exact settings incomplete

[arXiv 2609.05518v1 — arXiv 2609.05518v1; PDF margin dated 2026-08-31](https://arxiv.org/pdf/2609.05518v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## What changes relative to nearby evaluations

The following is an editorial protocol comparison, not an assertion of direct inheritance unless stated.

Adjacent to MultiModalQA’s candidate-context setting and MC-Search’s multimodal paths, this uses text-only inputs and explicitly covers image intersections and sets. Visual descriptions must first become retrieval targets before relation composition; corpus scale and oracle shortcuts limit open-search transfer.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

The 1,863 text-only questions require retrieving text and images; V/T denotes traversed evidence modalities, not query inputs. Categories contain 366 vision-to-text, 383 text-to-vision, 411 vision-to-text-to-vision, 391 multi-image intersection and 312 image-set questions. Visually rich August 2025 FineWiki articles supply GPT-5.1-extracted facts, Wikidata-linked images and visual verification; GPT-5.4 generates questions from connected multimodal subgraphs with rule/model filtering. The final corpus retains 4,987 referenced articles and 4,431 images. Hop count is the maximum shortest-path distance from retained evidence nodes to the answer, including image–entity edges; mean 3.50 is not tool-call count.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Conditions needed to interpret the results

M2RAG and adapted mKG-RAG share GPT-4o generation; without an input image, mKG-RAG uses text-to-image or text-to-text variants. Retrieval Recall covers gold evidence in the corresponding modality universe, while Hit only requires one item; image-only and multimodal denominators differ. Responses are atomized and an unnamed judge assigns TP/FP/FN. EM requires no extra or missing atoms; F1 micro-aggregates atoms rather than averaging questions. Dated models, decoding, generation limits, retriever configuration and context budgets are incompletely specified, so a common generator does not establish all-factor matching. Oracles directly supply gold text, images or both, potentially revealing a target entity the system would otherwise need to infer.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Retrieval systems and oracle evidence

All 1,863 questions; EM averages questions and F1 pools atom TP/FP/FN. Oracle supplies gold evidence directly. Retrieval context budgets are incompletely disclosed, preventing equal-information/resource interpretation.

| Setting | Overall atom EM percent | Overall micro atom F1 percent |
|---|---|---|
| GPT-4o closed-book | 24.3 | 27.6 |
| M2RAG + GPT-4o | 14.2 | 27.5 |
| mKG-RAG T2I + GPT-4o | 19.0 | 20.1 |
| GPT-4o + gold text and images | 66.1 | 70.3 |

Source: Tables 2–3 · [Paper](https://arxiv.org/pdf/2609.05518v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Visual-oracle shortcuts and set-level difficulty

Same GPT-4o; percentage of questions with exact atom sets. Oracle modalities differ in information and advance target-entity disclosure. These are not image-versus-multimodal retriever scores.

| Question mode | Questions | Gold images EM percent | Gold text and images EM percent |
|---|---|---|---|
| Text-to-vision | 383 | 66.6 | 64.2 |
| Vision-to-text-to-vision | 411 | 74.7 | 70.1 |
| Image-set | 312 | 29.2 | 29.2 |

Source: Table 2 · [Paper](https://arxiv.org/pdf/2609.05518v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:interpretation:START -->
## What the comparisons establish

GPT-4o closed-book EM is 24.3 percent, versus 14.2 for M2RAG and 19.0/19.2 for the mKG variants, while the joint oracle reaches 66.1. This shows headroom in retrieval/context handling under this protocol, not universal retrieval harm. Image-only oracles exceed joint evidence on text-to-vision EM,66.6 versus 64.2, and vision-to-text-to-vision,74.7 versus 70.1; more evidence is not monotonically better. Image-set EM remains 29.2 even with complete oracle evidence, exposing residual set-level visual reasoning limits.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source discrepancies and next test

Final corpus selection is conditioned on retained questions and contains fewer than ten thousand items; open-domain does not mean web scale. Model construction/verification lacks independent human agreement, and textual clues or parametric knowledge may bypass visual necessity. A nonzero closed-book score prevents per-item guarantees. Image oracles reveal target entities; comparing retrieval gains with model scaling changes information and reasoning demands rather than establishing matched-resource causality. Next disclose judges/context settings, human-audit image deletion and entity anonymization, add independent distractor pools and matched-token retrieval controls, and report complete required-hop coverage.

Figure 2 includes 1.4% one-hop questions despite broad prose describing every instance as multi-hop. Hop count reflects graph structure, not verified minimal necessary reasoning. Appendix A.1 says the English FineWiki subset has more than 61 million articles; that scope/number is not verified here and is unnecessary for the final corpus count. The main text references Table 2 for hop statistics, but Table 2 is oracle results; the hop distribution is Figure 2. Retrieval metric universes differ across methods, so image-only Recall 46.6 and multimodal Recall 38.4 are not a common-denominator ranking. Micro-F1 can fall below mean EM in a category because their aggregation weights differ; such cells should not automatically be corrected.
<!-- EVIDENCE:limitations:END -->
