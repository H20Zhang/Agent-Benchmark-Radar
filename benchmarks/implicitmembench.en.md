# ImplicitMemBench: first-response adaptation after distracting dialogue

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-04-09<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://aclanthology.org/2026.acl-long.1301/)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](implicitmembench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Full substantive paper and appendix reading completed for the stated version; experiments were not independently reproduced.

Read all 30 proceedings pages, pp.28232–28261: §§1–5, limitations and Appendices A–H, including judges, sensitivity tests, oracle/agent comparisons, all printed generation/curation/scoring prompts and examples. Visually checked Table 7. Some prompt fields are explicitly omitted by the published PDF; this is a source gap, not a completed code audit.

[ACL 2026 / 2026-07 / 2026.acl-long.1301](https://aclanthology.org/2026.acl-long.1301.pdf)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement

The protocol exposes a rule, theme or repeated outcome, inserts distracting dialogue, and scores the first response to a new task. Procedural and conditioning tasks use binary success; priming compares thematic transfer against a matched neutral-exposure control (§§3–4). For example, a file-copy utility teaches destination-before-source arguments; after distraction, the model must use that reversed order for a new transfer (Figure 7). This is text generation, not demonstrated filesystem execution.

### Measurement genealogy

LoCoMo and LongMemEval principally query retained information. MemoryAgentBench also includes test-time learning, so behavioral transfer is not wholly absent from predecessors. ImplicitMemBench narrows the coordinate to reminder-free first responses following brief exposure and interference. That operational distinction does not establish unconscious cognition or persistence across a context reset.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental setup

There are 100 items per paradigm, generated with GPT-4o-mini and filtered from over 1,000 candidates. The paper targets roughly 500 context tokens, caps responses at 4,096, uses T=0 for procedural/conditioning and T=0.8 only at the priming test. Table 7 averages three runs for binary tasks. Only 18% of procedural items use rule validation; 94% of all items are LLM-judged, chiefly by GPT-4o-mini at T=0. Learning examples remain part of the protocol despite the setup’s “zero-shot” wording.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## Selected quantitative evidence

Selected facts, not the complete leaderboard. Overall is the arithmetic mean of the three displayed paradigm scales. The oracle Mem0 row has privileged manually selected content; it is not a fair automatic-system ranking.

| System / comparison | Dataset / denominator | Metric / unit | Result | Conditions | Source |
| --- | --- | --- | --- | --- | --- |
| DeepSeek-R1 / procedural | 100 procedural items × 3 runs | First-try accuracy (%) | 76.33 | T=0; GPT-4o-mini or rule validator | Table 7, p.28239 (PDF p.8) |
| DeepSeek-R1 / conditioning | 100 conditioning items × 3 runs | First-try accuracy (%) | 69.67 | T=0; GPT-4o-mini judge | Table 7, p.28239 (PDF p.8) |
| DeepSeek-R1 / priming | 100 experimental/control pairs | Priming Influence Score (0–100) | 49.90 | Test T=0.8; GPT-4o-mini judge T=0 | Table 7, p.28239 (PDF p.8) |
| DeepSeek-R1 / overall | Three equally weighted paradigm scores | Mixed overall score (0–100), not accuracy | 65.30 | 100 items per paradigm; max 4,096 output tokens | Table 7, p.28239 (PDF p.8) |
| Mem0 + Key Info / DeepSeek-R1 / overall | Same three paradigms; oracle key information | Mixed overall score (0–100) | 74.12 | Perfect manual storage; not automatic memory extraction | Table 12, p.28244 (PDF p.13) |

Source: [Table 7, p.28239 (PDF p.8); Table 12, p.28244 (PDF p.13)](https://aclanthology.org/2026.acl-long.1301.pdf)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and interpretation

Overall combines two accuracies with a graded influence score; 65.30 is not 65.30% of 300 questions correct. Priming strength need not be useful or compliant behavior. No matched no-exposure control is reported for every procedural/conditioning task; defaults such as HTTPS can pass without learning. The five-person human result is called 100% accuracy even for graded priming, without a reconciliation. Appendix sensitivity lacks model/sample identities; memory-agent comparisons omit enough harness detail to prevent component-level causal attribution. Table 10’s original GLM score disagrees with Table 7, and Figure 6’s correlation caption names a different dependent variable from its plotted axis.
<!-- EVIDENCE:limitations:END -->

<!-- EVIDENCE:next:START -->
## Next experiment

Randomize learned conventions against model defaults, include no-exposure and reversed-association controls, and separate first-action accuracy from priming and format violations. Then test the same items after context reset with budget-matched raw history, extracted memory and oracle rules; report item-level uncertainty and full judge prompts.
<!-- EVIDENCE:next:END -->
