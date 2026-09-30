# LifeSide: memory, user modeling, privacy and simulated companionship

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-06<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2606.04660)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](lifeside.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Full substantive paper and appendix reading completed for the stated version; experiments were not independently reproduced.

Read all 28 pages: §§1–5, limitations/ethics and Appendices A–D, including implementation configurations, metric equations, all psychological scoring anchors and all supplied prompt templates. Visually checked the main results and metric/example page.

[arXiv v1 / 2026-06-03](https://arxiv.org/pdf/2606.04660v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement

A manager schedules persona events and pressures; a simulated user converts hidden thoughts into partly disclosed speech; critics validate consistency. Agents receive visible histories, while the companionship judge can inspect latent states. Tasks separate Structured Episodic Recall (SER: infer missing event attributes), Event Chain Tracking (ECT: reconstruct emotion changes across related events), evolving user models, recipient-conditioned privacy and multi-turn support (§2).

For example, an absence message to a supervisor should convey the necessary delay information while withholding protected personal details, including when the recipient pressures the agent for more specificity (Figure 10). Completeness and disclosure are therefore separate outcomes.

### Measurement genealogy

LifeSide joins conversational-memory evaluation from LoCoMo/LongMemEval with personalized-support work such as ES-MemEval. Its added coordinate is incomplete user disclosure within evolving environmental conditions. A useful next step tests observability and permission boundaries independently, rather than treating a latent-state judge’s preference as proof of real companionship.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental setup

The corpus has 2,000 personas and 111,674 tasks over 24–36 months, but experiments use the first 100 profiles. Frontier models use visible full histories when they fit, at temperature 0; RAG/memory methods supply top-8 records. Table 2 names GPT-5-mini as their answerer; Appendix B names GPT-5.1-mini. Exact evaluated task counts, simulator/judge identities, support-rollout budgets and repeat counts are unspecified. ECT averages LCS-F1 and normalized edit similarity; privacy averages attribute fractions (§3; Appendix B).
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## Selected quantitative evidence

Selected reported values. Every row uses tasks from the first 100 profiles; task-specific sample counts are not reported. Emotional percentages normalize the six 0–5 dimensions; violation is leaked protected attributes divided by protected attributes within each task, then aggregated, not an any-leak rate.

| System / comparison | Dataset / denominator | Metric / unit | Result | Conditions | Source |
| --- | --- | --- | --- | --- | --- |
| Gemini-3-Flash / SER | LifeSide first 100 profiles; SER task count unstated | Exact Match (%) | 41.24 | Visible full context when fitting; temperature 0 | Table 2, p.6 |
| GPT-5-mini / companionship | First 100 profiles; support task count unstated | Six-dimension normalized score (%) | 32.62 | Raw visible history; latent-state LLM judge | Table 2, p.6 |
| Mem0 / companionship | First 100 profiles; support task count unstated | Six-dimension normalized score (%) | 34.13 | Top-8; GPT-5-mini in table, GPT-5.1-mini in appendix | Table 2, p.6 |
| GPT-5-mini / regulation | First 100 profiles; scored support turns not enumerated | Mean rubric score (0–5) | 1.52 | Raw visible history; judge identity unspecified | Table 3, p.7 |
| Letta / regulation | First 100 profiles; scored support turns not enumerated | Mean rubric score (0–5) | 0.85 | 15-turn passages; top-8; answerer identity conflict | Table 3, p.7 |
| GPT-5-mini / Boundary Defense | First 100 profiles; protected attributes per task | Mean attribute violation (%) | 42.98 | Adversarial disclosure pressure; lower is better | Table 2, p.6; Eq.6, p.18 |

Source: [Table 2, p.6; Table 3, p.7; Eq.6, p.18](https://arxiv.org/pdf/2606.04660v1)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and interpretation

Memory can improve one dimension while degrading another; it does not uniformly reduce companionship scores. The headline 50% privacy figure describes a completion-conditioned pattern, not an overall episode leak rate. Synthetic hidden-state labels, unresolved answerer identity and unmatched retrieved/full-history context limit causal conclusions. The paper explicitly excludes clinical validity; human validation of the support judge remains future work.
<!-- EVIDENCE:limitations:END -->

<!-- EVIDENCE:next:START -->
## Next experiment

Resolve model identities, hold answerer and evidence budget fixed, and cross raw histories versus memory representations with independent privacy policies. Audit visible-evidence sufficiency and report both any-leak episodes and attribute-level leakage, alongside support quality judged without privileged hidden facts.
<!-- EVIDENCE:next:END -->
