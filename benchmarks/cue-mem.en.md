# CUE-Mem: remembering recurring peripheral cues

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-09-26<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2609.32574v1)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](cue-mem.md) · **English** · [Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope
Read sections 1–6 and Appendices A–G for methods, settings, key results and limitations; no independent reproduction.
[arXiv:2609.32574v1](https://arxiv.org/html/2609.32574v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Measurement and predecessor
Beyond Mem-Gallery/MemLens, CUE-Mem targets recurring background objects and sounds, such as meows behind voice messages. Profile-conditioned synthetic histories support four-choice recall, pattern, recommendation and refusal tasks: 20 users, 648 sessions, 2674 questions. Explicit/implicit samples are unpaired.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Comparison controls
Chinese histories use GPT-5.4 Medium image captions and Gemini 3.1 Pro Hint audio captions. RQ1/RQ2: temperature 0, 1024 output tokens; global seed 42 is passed only to Qwen-compatible APIs, with Qwen thinking disabled. Non-refusal filtering requires all six question-only answers correct, three per backbone. Full Memory has a 4096-word recall cap. Memory Avg. equally weights three non-refusal tasks; total question counts are not implicit-cell denominators.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Evidence and inference boundary
Table 2; implicit Memory Avg., percentage accuracy, macro-average across three non-refusal tasks; compare within backbone. Oracle supplies synthesis-source text.

| Backbone | Strongest non-oracle method | Non-oracle (%) | Oracle (%) |
|---|---|---|---|
| Qwen3.6-35B-A3B | MemGPT | 38.5 | 80.8 |
| GPT-5.4-mini | Reflexion | 41.9 | 78.4 |

[Table 2, Appendices C–D](https://arxiv.org/html/2609.32574v1). Gaps combine representation, retrieval and evidence use. Figure 5 exposes richer-caption input costs; alignment with Appendix D.2's cost statistics remains unresolved; do not combine them. No normalized cross-implementation result track is established.
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:limitations:START -->
## Limitations and next coordinate
Split uses clean synthetic audio stems, not mixed-audio separation; caption interventions also alter answer options. Three-run auditing covers five profiles, not every result. Synthetic multiple-choice and model-filtered questions limit generalization; drift, contradiction repair and forgetting remain unmeasured. Next: matched input/options, real mixtures and unseen users.

This is an early genealogy signal, not a field-wide trend. [Code](https://github.com/yulinlp/CUE-MEM) and [data](https://huggingface.co/datasets/Kkryptonite/CUE-Mem) are available; examples need not match paper configurations.
<!-- EVIDENCE:limitations:END -->
