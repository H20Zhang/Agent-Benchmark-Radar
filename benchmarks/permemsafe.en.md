# PerMemSafe: risk-aware responses from implicit and resolved personal context

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-07<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://aclanthology.org/2026.findings-acl.320/)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](permemsafe.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Full substantive paper and appendix reading completed for the stated version; experiments were not independently reproduced.

Read all 19 proceedings pages, pp.6415–6433, main §§1–6, limitations and Appendices A–G, including stronger-model results, generation filters, both track-specific safety/helpfulness rubrics, human matrices, failure cases and all SentinelMem prompts. Visually checked Figure 5 and Tables 3–4.

[ACL 2026 / 2026-07 / 2026.findings-acl.320](https://aclanthology.org/2026.findings-acl.320.pdf)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement

Synthetic histories encode an annotated personal risk indirectly and interleave over 90% irrelevant interactions. Trigger queries are retained when memory-free responses show no safety concern. Safety Perception (SP) checks awareness of the prior risk; Dynamic Evolution (DE) requires explicit acknowledgement and evidence that it has been mitigated or resolved (§3; Appendix E).

In one case, late-night online gambling and disrupted work precede a request to optimize card rewards. Retrieved fragments mention the behavior, but a generic optimization answer receives low personalized-safety credit (Appendix F). The test concerns context use under the assigned risk label, not diagnosis or observed financial harm. SentinelMem extracts inferred risks, maintains separate preference/risk profiles, and keeps current plus preceding states with response guidance.

### Measurement genealogy

Earlier personalized-safety work supplies explicit user context in a single turn; PersonaMem supplies dynamic-profile and distractor ideas, while LoCoMo emphasizes recall. PerMemSafe moves the risk evidence into noisy history and scores risk resolution. It adds a relevant coordinate without covering every evolving-risk trajectory.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental setup

The paper reports 276 conversations and 750 test instances across five domains, but does not provide explicit per-track counts or history-token lengths. Memory retrieval uses top-3 entries. Agent and judge temperatures are 0, response cap 2,048 tokens, results averaged over three runs. GPT-4o receives gold risk and relevant history when judging. Personalized Safety Rate (PSR) is binary rubric compliance; Personalized Helpfulness Score (PHS) is a 1–5 rating multiplied by 20, hence 20–100 in practice, despite the paper’s 0–100 wording. One hundred cases are checked against three AI/NLP graduate annotators.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## Selected quantitative evidence

Selected overall and ablation facts. PUP means proactive user profiling. Table 3 does not restate its backbone; GPT-4o-mini is inferred from its full-system row matching Figure 5. Overall values average the two reported tracks, whose separate denominators are not specified.

| System / comparison | Dataset / denominator | Metric / unit | Result | Conditions | Source |
| --- | --- | --- | --- | --- | --- |
| Mem0 | PerMemSafe overall; 750 total instances stated, track counts unspecified | PSR (%) / PHS (1–5 ×20; actual range 20–100) | 39.20 / 56.40 | GPT-4o-mini; top-3; T=0; 2,048 output tokens; three runs; GPT-4o judge | Table 2, p.6420 (PDF p.6) |
| SentinelMem | PerMemSafe overall; 750 total instances stated, track counts unspecified | PSR (%) / PHS (1–5 ×20; actual range 20–100) | 48.53 / 64.00 | GPT-4o-mini; top-3; T=0; 2,048 output tokens; three runs; GPT-4o judge | Figure 5, p.6422 (PDF p.8) |
| Vanilla ablation baseline | PerMemSafe overall; 750 total instances stated, track counts unspecified | PSR (%) / PHS (1–5 ×20; actual range 20–100) | 25.20 / 56.20 | GPT-4o-mini (inferred from matching full row); top-3; T=0; 2,048 output tokens; three runs; GPT-4o judge | Table 3, p.6422 (PDF p.8) |
| Vanilla + PUP | PerMemSafe overall; 750 total instances stated, track counts unspecified | PSR (%) / PHS (1–5 ×20; actual range 20–100) | 43.60 / 57.40 | GPT-4o-mini (inferred from matching full row); top-3; T=0; 2,048 output tokens; three runs; GPT-4o judge | Table 3, p.6422 (PDF p.8) |
| Mem0 / stronger backbone | PerMemSafe overall; 750 total instances stated, track counts unspecified | PSR (%) / PHS (1–5 ×20; actual range 20–100) | 72.93 / 80.60 | GPT-5.1; top-3; T=0; 2,048 output tokens; three runs; GPT-4o judge | Table 4, p.6426 (PDF p.12) |

Source: [Table 2, p.6420 (PDF p.6); Figure 5, p.6422 (PDF p.8); Table 3, p.6422 (PDF p.8); Table 4, p.6426 (PDF p.12)](https://aclanthology.org/2026.findings-acl.320.pdf)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and interpretation

SP can pass for demonstrating risk awareness in reasoning without proving the final action is harmless; DE penalizes a reasonable generic answer that omits explicit resolution attribution. Thus PSR is not an incident-free rate. The headline 23.8% matches a relative gain from 39.20 to 48.53, not a 23.8-point gain or an average across backbones. Appendix C reaches 72.93 with Mem0/GPT-5.1, so the roughly-50% ceiling applies only to the lightweight main comparison. Risk inference can over-pathologize ambiguous users; no no-risk false-positive control, clinical validation or deployment privacy audit is supplied.
<!-- EVIDENCE:limitations:END -->

<!-- EVIDENCE:next:START -->
## Next experiment

Pair the same query with active-risk, resolved-risk, ambiguous and no-risk histories. Judge actual harmful guidance separately from mentioning the risk, and score useful clarification without requiring disclosure of sensitive inferred labels. Match memory bytes and retrieval tokens across component ablations; report uncertainty, false positives and resolved-risk over-caution.
<!-- EVIDENCE:next:END -->
