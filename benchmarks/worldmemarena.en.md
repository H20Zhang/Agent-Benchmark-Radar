# WorldMemArena: auditing multimodal memory with staged questions

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-05-28<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2605.29341)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](worldmemarena.md) | **English**

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Reviewed the stated paper version, method, experimental setup, key results and limitations; no independent reproduction.

All substantive main 1–8 and Appendices A–F read; selected setup, metrics and tables crosschecked explicit v2 PDF. Official README and dataset card checked, not implementation audited. Figure curves not digitized. Paper contains no full judge-prompt appendix; no rerun.

[arXiv2605.29341v2 (2026-06-01)](https://arxiv.org/html/2605.29341v2)

The frozen release reference is preserved. Newly reviewed versions and conditions do not replace initial-release results.
[Fixed-version PDF 2605.29341v2](https://arxiv.org/pdf/2605.29341v2)
[Official source observed 2026-09-30 (mutable page)](https://github.com/UCSB-AI/WorldMemArena)
[Official source observed 2026-09-30 (mutable page)](https://huggingface.co/datasets/LCZZZZ/WorldMemArena)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Task construction and memory observation

Organize recorded GUI/embodied traces and generated evolving-life/project sessions into temporal streams. Annotate memory points, updates, distractors and QA evidence; inspect snapshots, retrieval and answers separately. For example, after plan A changes to B, test whether stale A remains stored and whether later QA still uses it.

Editorial placement: Compared with conversation memory such as LoCoMo, WorldMemArena broadens evidence to embodied, GUI, project and personal-life trajectories with images and updates. The core evaluation remains post-trajectory QA, so the extension does not establish closed-loop action competence. This is an evaluation-coordinate comparison, not a claim of direct dataset inheritance.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental conditions and scoring targets

The v2 body and dataset card report 461 trajectories/8489 sessions/15595 images/24258 QA. Card breakdown: 203 GUI, 220 embodied, 18 project, 20 personal. Table 2 engineered systems use GPT-5.4-nano and its caption names GPT-5.4-mini judge; Appendix A instead says the judge inherits the answer model, unresolved. Retrieval cap 10; 128,000-token context with 8000 reserved; up to 5 images/question and 45 MB; temperature 0 and 16,384 completion tokens.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## More writing coverage need not yield better answers

Main text specifies shared GPT-5.4-nano, caption GPT-5.4-mini judge; retain Appendix A conflict. RC is judge-based coverage of top 10, distinct from deterministic Recall@K.

Per-trajectory means; advertised full corpus 461 trajectories/24258 QA; actual valid-label counts not supplied; IntRej only trajectories with interference.

| System | Memory recall (%) | Update (%) | Interference rejection (%) | QA-C (%) | Retrieval coverage RC (%) |
|---|---|---|---|---|---|
| Qwen3-VL-Embedding-8B | 86.22 | 59.02 | 28.21 | 51.86 | 73.44 |
| A-Mem | 52.54 | 58.86 | 58.94 | 54.63 | 74.19 |
| M2A | 86.83 | 56.41 | 23.42 | 50.14 | 64.62 |

Locator: v2 Table 2, selected columns/rows · [Source](https://arxiv.org/html/2605.29341v2)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Update gives partial credit to stale-fact coexistence

Metric definition, not a new experiment. Half credit for coexistence means Update is not strict correction rate.

Gold updates pooled within each instance, then averaged across instances

| Post-update state | Update credit |
|---|---|
| New fact only | 1.0 |
| Old and new coexist | 0.5 |
| Old fact only | 0.0 |

Locator: Appendix B Eq 3, metric definition · [Source](https://arxiv.org/html/2605.29341v2)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:limitations:START -->
## Supported conclusions and unresolved questions

Higher writing coverage need not coincide with higher QA, but this association does not identify a causal bottleneck. Modalities, captions, calls and adapters vary. Metrics aggregate within trajectories then average across them; QA denominators include valid judge labels, with per-system valid counts unspecified. No independent human judge-error validation or oracle-stage intervention results establish a ceiling.

400 on arXiv abstract vs 461 in v2 PDF/body and official dataset card. Main §4.4 says 12 axes, Appendix B/Table 4 enumerate 11. Table 2 GPT-5.4-mini judge versus Appendix A inherited-answer-model judge. Harness prose GPT-5.4 vs Table 3/repository GPT-5.4-nano; table Qwen3.5 plus versus appendix/repo Qwen3.6 plus. Table 2 MemGPT/prose MemoryGPT versus official README MGMemory described as Mem-Gallery text; exact mapping unresolved. Selected evidence avoids this identity. MIRIX Corr/Hallu/Irrel 73.50/5.15/1.58 sum 80.23 despite mutually exclusive nonempty-item formula; no fabricated reconciliation. Dataset card total turns 59239 vs body 59858 steps, and GUI/embodied subcategory counts differ; do not silently combine. Current repository includes 150-sample small split; paper does not explicitly identify per-row completed subset counts.

Next experiment: Hold trajectories, backbone, images and budget fixed; substitute gold write/update/retrieval artifacts stage by stage on paired QA. Report strict stale-fact removal separately from half-credit coexistence and exact semantic retrieval separately from session-ID matches. Add executable tasks to test transfer from diagnostic gains to action outcomes.
<!-- EVIDENCE:limitations:END -->
