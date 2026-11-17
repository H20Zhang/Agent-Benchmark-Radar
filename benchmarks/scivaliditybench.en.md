# SciValidityBench: scientific constraints on memory use

<!-- RELEASE-REFERENCE:START -->
> **Release diagnostic (historical reference)** · Initial release: 2026-10-26<br>
> **Qwen3-14B / Flat SSG — Scientific-use-valid decision rate: 0.991**; **Qwen3-14B / SVL — Scientific-use-valid decision rate: 0.981**<br>
> Table 3, Qwen3-14B, temperature 0; scientific-use-valid decision rate on 64 TaskSpecs × 10 seeds, TaskSpec-weighted. Not a cross-system best claim. [Original source](https://arxiv.org/html/2610.34767v1)<br>
> Short synthetic histories and deterministically compiled state; no universal graph-serialization or real-world long-term scientific-memory claim.
<!-- RELEASE-REFERENCE:END -->

[中文](scivaliditybench.md) · **English** · [Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope
Read the main paper and protocol, controls, results and limitations in Appendices A–I; checked the official repository file inventory. No experiment reproduction or independent figure-pixel inspection.
[arXiv:2610.34767v1](https://arxiv.org/html/2610.34767v1) · [Official code](https://github.com/SciValidityBench/SciValidityBench)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## What changes in the measurement
A remembered fact can be accurate but inadmissible for a decision. SciValidityBench makes preregistration, selection, stopping, construct definitions, informative absence and sunk costs explicit. Five modules comprise 24 Inferential Ledger, 8 Blind Memory, 12 Construct Drift, 12 Absence Algebra and 8 Sunk Cost TaskSpecs across six synthetic scientific domains. Relative to MemCalib and The Memory Trust Gap, this adds executable scientific-use constraints rather than another recall test. This is an early diagnostic signal, not a durable map revision.

A TaskSpec defines world generation, a deterministic state compiler, legal actions, an oracle and interventions. SciStateForge derives relations such as Selected_From, Stopped_After and Sealed_Until from public events. Flat SSG and typed SVL expose the same derived state. The hidden oracle is not supplied to the reader, but the compiler and oracle share a designed task ontology.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Protocol and fair comparison
There are 640 worlds and 1,920 public event records: short structured histories, not a long-context stress test. Main comparisons contain 12,800 original decisions plus 5,120 paired companions. The 68,320 decisions across six matrices are not independent worlds. Raw history, BM25 top-5 chunks, a generic event graph, Flat SSG and typed SVL are tested with Qwen3-14B, Gemma-3-12B-IT, Mistral-7B-Instruct-v0.3 and Phi-3.5-mini-instruct.

Deterministic scoring checks scientific validity against the TaskSpec oracle, without an LLM judge. Invalid JSON, refusals and illegal or unparseable actions count as failures; there are no outcome-conditioned retries. Seed-level paired differences are aggregated within TaskSpec and then equally across 64 tasks; uncertainty uses 20,000 TaskSpec bootstrap samples. Counterfactual flip/invariance and both-correct validity must remain separate: a reader can consistently choose the wrong action. Corruption and exact inverse repair are compared with size-matched irrelevant repairs. The official repository contains generators, compiler, reader interfaces, corruption operators, scoring and tests; availability was checked, not execution.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Selected primary evidence
Table 3: four frozen readers, temperature 0, identical requests and finite legal actions within each comparison; scientific-use-valid decision rates on 64 TaskSpecs × 10 seeds, equally weighted by TaskSpec.

| Reader | Raw scientific-use-valid decision rate | Event Graph scientific-use-valid decision rate | Flat SSG scientific-use-valid decision rate | SVL scientific-use-valid decision rate |
|---|---|---|---|---|
| Qwen3-14B | 0.798 | 0.794 | 0.991 | 0.981 |
| Gemma-3-12B-IT | 0.733 | 0.719 | 0.903 | 0.902 |
| Mistral-7B-Instruct-v0.3 | 0.556 | 0.566 | 0.692 | 0.678 |
| Phi-3.5-mini-instruct | 0.480 | 0.478 | 0.609 | 0.570 |

[Table 3; Appendices D/G/I](https://arxiv.org/html/2610.34767v1). Flat SSG exceeds typed SVL in every main row: this is not evidence of universal graph superiority. In a separate family-balanced, token-matched source control, Flat minus matched source is +0.194 for Qwen, +0.193 for Mistral, +0.011 for Gemma (interval crosses zero) and −0.295 for Phi. These are different subsets and controls, not replacements for Table 3. Removing 22 tasks with literal state/action overlap leaves positive SVL–Event Graph contrasts on 42 tasks, but does not eliminate broader synthetic-template shortcuts.
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and next coordinate
The compiler pre-computes decision-relevant relationships. Results therefore measure state compilation plus reading, not learned memory writing/retrieval in an autonomous laboratory. Finite actions, short histories, synthetic worlds and shared task ontology constrain generalization. More explicit state also hurts Qwen/Gemma in Sunk Cost, and exact repair does not improve every reader. An observed near-perfect cell is neither saturation of scientific reasoning nor a real-world validity guarantee.

Next: independently generated long histories and unseen scientific workflows, learned compilers with error accounting, and matched facts/tokens/interfaces across representations. Preserve reader-specific regressions and both-correct counterfactual scores. The strongest supported claim is that controlled scientific-use constraints can be measured, not that a graph memory is generally best.
<!-- EVIDENCE:limitations:END -->
