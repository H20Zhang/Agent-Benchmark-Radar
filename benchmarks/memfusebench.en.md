# MemFuseBench: fusing source-tagged events without losing provenance

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-07-21<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2608.18704)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](memfusebench.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

The full primary paper was read for methods, setup, results and limitations; experiments were not independently reproduced.

The complete main paper and Appendices A–E were read, including all published construction, fusion, retrieval, reader and judge prompts. The appendix explicitly selects from a larger prompt library; unpublished prompts were not reviewed. No experiments were rerun.

[Full primary paper](https://arxiv.org/pdf/2608.18704v1) · arXiv:2608.18704v1
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## Relation to neighboring evaluations

Compared with LoCoMo/LongMemEval conversation memory, this distributes one episode across devices, applications, users and time, requiring complementary evidence, conflict resolution and perspective tracking. It is adjacent to LifeBench/SMMBench, but uses semantic events generated from shared latent scenarios rather than independently collected real multimodal streams. The added axis is source fusion, not raw sensor perception.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

Scene-to-Sensor generates personas/devices, causal timelines and timestamped observations limited to each device’s view. It then generates six question types, removes duplicates/common-sense shortcuts and injects similar distractors without changing answers. Stagewise review/correction is followed by three strong full-context models and human correction of disagreements; about twenty percent of questions receive revisions. Six scenarios contain 7,823 events and 357 questions, requiring 9.4 evidence events on average. The 71 fusion questions need 15.2 events, while 70 conflict questions need 2.8. An example combines household dialogue, a work calendar and a call while rejecting a wrong-day record. MemFuse preserves immutable events, uses fused summaries as retrieval entries and connects membership, causal and semantic edges for evidence recovery.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental setup and scoring

Qwen3-30B-A3B, GPT-4.1 Mini and Gemini 3.1 Flash Lite each supply both system-specific calls and final answering, with BGE-M3 embeddings. Full context receives the entire scenario; other systems return twenty context entries, without matched tokens or compute. MemFuse uses thirty retrieval seed candidates, up to three rewrites, two causal hops, one semantic hop, threshold 0.8 and two to five answer-time retrieval rounds. The appendix permits three fused summaries with up to ten members each; summaries consume entry slots, with a 128,000-character cap. Answers use temperature one and 2,048 output tokens; construction/planning use 4,096. GPT-4.1 Mini judges at temperature zero with 4,096 tokens. Checklist coverage is averaged per question, not equally across categories, and has no independent penalty for extra hallucinations. Unresolved scoring failures withhold aggregates after retries rather than count as zero.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Quality and token cost under one backbone

Overall averages 357 questions on a zero-to-one scale; Fusion has 71. Bounded systems return twenty entries, unlike full context. Token totals cover the evaluation, not per-query prices; dashes mean unavailable/inapplicable.

| System | Overall checklist score | Fusion score | Ingest tokens millions | Inference tokens millions |
|---|---|---|---|---|
| Naive RAG | 0.3289 | 0.1823 | — | 0.76 |
| EverMemOS | 0.455 | 0.3945 | 55.3 | 12.31 |
| MemFuse | 0.4574 | 0.3308 | 29.73 | 7.1 |
| Long context | 0.5223 | 0.4219 | — | — |

Source: Table 2, GPT-4.1 Mini block · [Paper](https://arxiv.org/pdf/2608.18704v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Larger effect from answer-time retrieval than prebuilt structure

Same 357 questions, Gemini 3.1 Flash Lite, twenty final entries and GPT-4.1 Mini judge; zero-to-one mean coverage. One component is removed at a time without equalized calls/tokens; no intervals.

| Variant | Overall checklist score |
|---|---|
| MemFuse | 0.4698 |
| Without agentic retrieval | 0.3662 |
| Without retrieval constraints | 0.4185 |
| Without graph | 0.4514 |
| Without fused memory | 0.4618 |

Source: Figure 4 and ablation discussion · [Paper](https://arxiv.org/pdf/2608.18704v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:interpretation:START -->
## What the evidence supports

MemFuse has the highest overall point estimate among bounded-entry systems under all three backbones, but full context is stronger under GPT/Gemini, and the GPT margin over EverMemOS is only 0.0024. Removing Gemini answer-time iterative retrieval loses 0.1036, versus 0.0080 without fused summaries, pointing toward search as a major contributor. These ablations also change compute, preventing pure graph attribution. Qwen ingestion uses 93.27 million tokens versus EverMemOS’s 76.52 million, so cost savings are not universal.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source gaps and next test

Only six synthetic scenarios underlie the 357 questions; source realism, authority and causal links inherit generation assumptions. Model-guided revisions do not establish an independent human ceiling or label agreement. One tested backbone shares the judge family, and checklist coverage does not verify provenance for every claim. Memory units vary in length/compression, reader prompts differ slightly and single-pass estimates lack intervals. Next cluster uncertainty by scenario, match final tokens/search calls, remove evidence events to test source necessity, and validate on independently collected records with human provenance/hallucination audits.

The main text describes twenty atomic events, while Appendix C admits fused summaries first and charges them as entries; implementation is needed to resolve packing. The main ranking description mentions temporal decay, but the explicit appendix equation lists graph-hop decay, RRF, path priors and a date boost set to zero here; no unreported temporal constant should be inferred. The complete prompt library and precise synthesis-model role configuration are not published.
<!-- EVIDENCE:limitations:END -->
