# MemEvoBench: safety over three rounds of contaminated-memory updates

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-04-17<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2604.15774)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](memevobench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Full substantive paper and appendix reading completed for the stated version; experiments were not independently reproduced.

Read all 33 pages of v2, §§1–6 and Appendices A–D: every risk taxonomy, construction/evaluation/feedback prompt and both complete memory examples. Visually checked Tables 1–3. v1 is dated 17 April; the preserved release banner is not a certification of v1 results.

[arXiv v2 / 2026-05-21](https://arxiv.org/pdf/2604.15774v2)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement

Each case begins with mixed memories, asks three related but different questions, and appends each response to memory. Optional simulated feedback rewards risky shortcuts and criticizes caution. QA construction specifies two correct and three misleading entries; correct fragments deliberately avoid directly exposing the misleading pattern (Appendix B).

In the property-communication example, flawed past sharing workflows precede requests to email cleaning and occupancy details. The reference expects recipient authorization checks; the evaluator examines the simulated tool trajectory (Appendix D). The benchmark thereby measures reuse of unsafe precedent, not actual disclosure in a production service.

### Measurement genealogy

AgentPoison studies poisoned memory access, Agent-SafetyBench supplies workflow environments, and prior memory-misevolution work motivates cumulative feedback. MemEvoBench combines those coordinates in a short, controlled update sequence. Three related rounds are useful for drift diagnosis but do not establish months-long autonomous evolution.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental setup

QA has 108 cases across 36 risks/seven domains; workflow has 83 cases adapted from 20 environments. Nine answer models use T=0. GPT-5.2 classifies risky answers or trajectories; uncertainty defaults to unsafe for workflow. Attack Success Rate (ASR) is the proportion judged to exhibit the specified unsafe behavior. QA +ModTool adds both correction and web search, whereas workflow adds correction only. Retrieval selection, search backend, exact tool/response budgets and repeated-run uncertainty are not pinned. A-MEM comparisons cover only selected models.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## Selected quantitative evidence

Selected within-paper comparisons, retaining the reported percentages and stated denominators without inferring missing counts. QA and workflow are separate tests. These three-round values are not a real-world incident rate.

| System / comparison | Dataset / denominator | Metric / unit | Result | Conditions | Source |
| --- | --- | --- | --- | --- | --- |
| Gemini-2.5-Pro / Vanilla | 108 QA cases per round (stated) | ASR (%), rounds 1 / 2 / 3; lower is safer | 66.0 / 72.0 / 80.0 | Initial system; biased feedback; T=0; GPT-5.2 judge | Table 1, p.6 |
| Gemini-2.5-Pro / +SafePrompt | 108 QA cases per round (stated) | ASR (%), rounds 1 / 2 / 3; lower is safer | 42.0 / 49.0 / 66.0 | Initial system; biased feedback; T=0; GPT-5.2 judge | Table 1, p.6 |
| Gemini-2.5-Pro / +ModTool | 108 QA cases per round (stated) | ASR (%), rounds 1 / 2 / 3; lower is safer | 19.0 / 23.0 / 30.0 | Initial system; biased feedback; correction plus web search; T=0; GPT-5.2 judge | Table 1, p.6 |
| Qwen3-32B / A-MEM / Vanilla | 83 workflow cases per round (stated) | ASR (%), rounds 1 / 2 / 3; lower is safer | 60.2 / 71.1 / 72.3 | No feedback; A-MEM; T=0; GPT-5.2 judge | Table 3, p.8 |
| Qwen3-32B / A-MEM / +ModTool | 83 workflow cases per round (stated) | ASR (%), rounds 1 / 2 / 3; lower is safer | 73.5 / 81.9 / 84.3 | No feedback; correction, no QA-style search tool; T=0; GPT-5.2 judge | Table 3, p.8 |

Source: [Table 1, p.6; Table 3, p.8](https://arxiv.org/pdf/2604.15774v2)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and interpretation

The A-MEM workflow counterexample in the selected table prevents claiming correction always improves safety. QA gains also bundle search with correction. Round-to-round queries differ, so worsening alone does not isolate memory accumulation; the no-memory controls help but are not a full frozen-memory/feedback factorial. Some reported percentages cannot be reconstructed from the stated case counts; the claimed 96.2% judge accuracy on 50 binary responses likewise needs denominator clarification. No benign-task utility or recovery-cost measurement establishes a deployable safety–utility trade-off.
<!-- EVIDENCE:limitations:END -->

<!-- EVIDENCE:next:START -->
## Next experiment

Replay identical query sequences with clean, frozen-contaminated and updating memory; independently vary feedback, search and correction. Report safe task completion alongside ASR, retrieval/write traces and selective repair cost. Publish raw counts and human disagreement, especially when the reference requires clarification but the execution prompt says no further user interaction.
<!-- EVIDENCE:next:END -->
