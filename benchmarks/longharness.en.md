# LongHarness Bench: selective retrieval and verification under resource constraints

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-09-29<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2609.38137v1)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](longharness.md) · **English** · [Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope
Read the full main text and Appendices A–C; checked the official dataset card, release metadata and scorer. No benchmark reproduction or independent figure-pixel inspection.
[arXiv:2609.38137v1](https://arxiv.org/html/2609.38137v1) · [scorer commit 6e3da81](https://github.com/StringNLPLAB/longharness/blob/6e3da81caa79a0fa53c150aa458b7e4e0c074e87/score.py)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## What changes in the measurement
The 200 instances split equally across four suites. Find five qualifying people among 160; find 15 inconsistent memos among 700; trace eight dependent operations through 320 stored computation cells; or find five matching pairs among 200 Python programs. Search order, verification and reuse matter: checking a selective condition first can shrink later work.

Compared with LongBench-v2 and OOLONG-Synth, the intended coordinate is retrieval that changes with intermediate findings and supports different accuracy–cost strategies. BRIGHT and BrowseComp are relevant retrieval ancestors; this is an early diagnostic signal, not evidence of a durable field trend or cross-session memory learning.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Protocol and fair comparisons
Four suites of 50; exact-set scoring gives no primary partial credit. Program tracing uses format-tolerant answer-and-citation rescoring: the public scorer requires the final value and unique supporting-ID set, not citation order. Program-pair equivalence is established by tests/probes, not formal proof. GitHub supplies eight examples; the full 200-instance package is on Hugging Face.

GPT-5.6-sol uses high reasoning effort; ReAct uses BAAI/bge-m3 retrieval. Tools differ across Direct, file/shell agents, RLM and ReAct. The stated 3M cumulative input/output cap conflicts with Appendix A, including Kimi/OpenCode's 5.83M mean tracing input tokens. Enforcement/accounting is unresolved. Costs use reported API/cache rates; Qwen is API-equivalent self-hosted cost. Neither latency nor equal-budget superiority follows. Harness runners/raw traces and repeated-trial uncertainty were not established from public artifacts.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Selected primary evidence
Table 2 and Appendix A; GPT-5.6-sol, high reasoning, four 50-instance suites; reported exact accuracy (%) and mean estimated USD per instance. Nominal budget enforcement unresolved.

| Harness | Constraint accuracy (%) | Memo accuracy (%) | Macro accuracy (%) | Macro USD/instance |
|---|---|---|---|---|
| Direct | 58 | 44 | 60.0 | 0.822 |
| mini-swe-agent | 42 | 100 | 68.0 | 0.816 |
| RLM | 44 | 92 | 53.5 | 4.30 |

[Table 2; Appendix A](https://arxiv.org/html/2609.38137v1). The macro improvement hides a constraint-task regression. Figure 4's task-dependent gains therefore support system-specific trade-offs, not universal harness superiority. The observed 68% maximum is not a ceiling. No normalized comparable result track is published while budget/runner provenance remains unresolved.
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and next coordinate
Synthetic worlds, public keys and exact-set metrics leave real workloads, leakage and partial success uncertain. The LongBench-v2 comparison uses 42 hard and eight easy cases, not the full distribution; cross-benchmark percentages are not normalized difficulty. Next: publish raw accounting, pin runners and extraction rules, then test matched budgets, partial-credit diagnostics and unseen changing corpora. Repository commit dates alone do not prove first public availability.
<!-- EVIDENCE:limitations:END -->
