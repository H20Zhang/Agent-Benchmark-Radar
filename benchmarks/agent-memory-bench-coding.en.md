# Agent Memory Bench: coding retrieval gains, admission and historical leakage

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-08-22<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://github.com/GiulioDER/agent-memory-bench)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](agent-memory-bench-coding.md) | **English**

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Reviewed the pinned official protocol, settings, result artifacts and limitations; no independent reproduction.

Complete README, site/method.html, docs/STATUS.md and REPLICATION.md; preregistrations 000 and 026; pilot-001 analysis; official-003 summary, analysis and audit reports. Targeted stats/bootstrap and board-loader source inspection. Public revision pinned; no benchmark code executed, no model runs or external-state changes. Joined vendor run provenance was not fully re-audited.

[Official protocol 695dd26a6732174a59386fa28aa844ad31d31a48](https://github.com/GiulioDER/agent-memory-bench/blob/695dd26a6732174a59386fa28aa844ad31d31a48/docs/STATUS.md)

[Official source at pinned revision 695dd26a6732174a59386fa28aa844ad31d31a48](https://github.com/GiulioDER/agent-memory-bench/blob/695dd26a6732174a59386fa28aa844ad31d31a48/README.md)

[Official source at pinned revision 695dd26a6732174a59386fa28aa844ad31d31a48](https://github.com/GiulioDER/agent-memory-bench/blob/695dd26a6732174a59386fa28aa844ad31d31a48/site/method.html)

[Official source at pinned revision 695dd26a6732174a59386fa28aa844ad31d31a48](https://github.com/GiulioDER/agent-memory-bench/blob/695dd26a6732174a59386fa28aa844ad31d31a48/docs/REPLICATION.md)

[Official source at pinned revision 695dd26a6732174a59386fa28aa844ad31d31a48](https://github.com/GiulioDER/agent-memory-bench/blob/695dd26a6732174a59386fa28aa844ad31d31a48/preregistration/000-pilot.md)

[Official source at pinned revision 695dd26a6732174a59386fa28aa844ad31d31a48](https://github.com/GiulioDER/agent-memory-bench/blob/695dd26a6732174a59386fa28aa844ad31d31a48/preregistration/026-official-003-fair-instruction.md)

[Official source at pinned revision 695dd26a6732174a59386fa28aa844ad31d31a48](https://github.com/GiulioDER/agent-memory-bench/blob/695dd26a6732174a59386fa28aa844ad31d31a48/results/pilot-001/analysis.json)

[Official source at pinned revision 695dd26a6732174a59386fa28aa844ad31d31a48](https://github.com/GiulioDER/agent-memory-bench/blob/695dd26a6732174a59386fa28aa844ad31d31a48/results/official-003/leaderboard_summary.json)

[Official source at pinned revision 695dd26a6732174a59386fa28aa844ad31d31a48](https://github.com/GiulioDER/agent-memory-bench/blob/695dd26a6732174a59386fa28aa844ad31d31a48/reports/official-003-analysis.md)

[Official source at pinned revision 695dd26a6732174a59386fa28aa844ad31d31a48](https://github.com/GiulioDER/agent-memory-bench/blob/695dd26a6732174a59386fa28aa844ad31d31a48/reports/official-003-audit.md)

The frozen release reference is preserved; newer paper results do not replace initial-release scores.
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## How tasks create memory demands

Feed identical verbatim transcripts to each arm, then run matched task/seed/fixture cells in isolated repositories. Hidden executable checkers grade produced code pass/fail without an LLM judge. Admission verifies tools, hooks, file digests and isolation, not actual retrieval or causal memory use. A timezone task may depend on a convention recorded only in an earlier session; controls include raw transcripts with grep, no memory, static instructions and content-free placebo text.

Editorial placement: Compared with generic memory QA, this official protocol measures coding-task pass/fail across bare, placebo, project-instruction and retrieved-memory arms. It tests prefilled-corpus retrieval utility rather than long-term memory formation, with historical scores limited by the leakage audit. This is an evaluation-coordinate comparison, not a claim of direct dataset inheritance.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental settings and scoring targets

The current suite has 34 executable tasks; official-003 uses 26 tasks: 73 task-condition combinations × 5 seeds × 8 arms=2920 sessions. Of 365 planned paired cells, 317 are admitted and 48 discarded, with one session per arm/cell. Model deepseek/deepseek-v4-flash through Claude Code. Conditions are present, absent, superseded, contradictory and adjacent. About 4900 documents per condition are bulk-ingested before the grid; writes are disabled during runs, so this evaluates retrieval rather than the full memory lifecycle.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## official-003 leaderboard_summary.json, selected arms

Rates/absolute deltas on 0–1 scale. Baseline [0,0] is self-comparison, not a success-rate confidence interval. Other bounds are reported contrast intervals crossing zero; disclosed label exposure remains.

317 admitted matched task/seed/condition cells; 26 tasks; interval excludes whole-run variability

| Arm | Success rate | Delta vs claude_md | 95% lower bound | 95% upper bound |
|---|---|---|---|---|
| claude_md | 0.5773 | 0 | 0 | 0 |
| recall | 0.6593 | 0.082 | -0.0063 | 0.1808 |
| bare | 0.6593 | 0.082 | -0.0195 | 0.1963 |
| placebo | 0.6719 | 0.0946 | -0.0369 | 0.2493 |

Locator: official-003 leaderboard_summary.json, selected arms · [Source](https://github.com/GiulioDER/agent-memory-bench/blob/695dd26a6732174a59386fa28aa844ad31d31a48/results/official-003/leaderboard_summary.json)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## pilot-001 analysis.json, separate all-task and screened estimands

Historical pilot; per-task mean recall−claude_md, task-cluster bootstrap 95% intervals excluding whole-run variation. Both scopes have McNemar p=1.0. Not directly comparable as progress against official-003.

pilot-001;24 tasks×3 seeds planned 72 cells, 71 admitted; 13 screened tasks retain 38 cells

| Analysis set | Tasks | Paired cells | Recall delta | 95% lower | 95% upper |
|---|---|---|---|---|---|
| All tasks | 24 | 71 | 0.0139 | -0.0278 | 0.0556 |
| After ceiling/floor screening | 13 | 38 | 0.0256 | 0 | 0.0769 |

Locator: pilot-001 analysis.json, separate all-task and screened estimands · [Source](https://github.com/GiulioDER/agent-memory-bench/blob/695dd26a6732174a59386fa28aa844ad31d31a48/results/pilot-001/analysis.json)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## official-003 summary, selected condition counts

Binary checker pass counts; condition difficulty and admitted sets differ, so differences between rows do not isolate a condition effect.

Per-condition admitted cells; same selected arms and seed/task pairing

| Condition | Paired cells | Recall passes | claude_md passes |
|---|---|---|---|
| present | 111 | 56 | 43 |
| contradictory | 51 | 37 | 39 |

Locator: official-003 summary, selected condition counts · [Source](https://github.com/GiulioDER/agent-memory-bench/blob/695dd26a6732174a59386fa28aa844ad31d31a48/results/official-003/leaderboard_summary.json)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and next validation

This is not a clean causal product ranking. official-003 registered after launch without advance announcement. A September 26 audit found stale_/rival_ labels in document names and condition names in paths/namespaces; fixes do not repair historical scores, requiring reruns. Paired admission changes the sample and budgets are unmatched. A failing naive reference does not prove a capable model cannot find another correct solution. Recall is developed by the benchmark authors. No positive significant contrast does not imply memory is useless; 13 screened tasks do not replace the all 24-task pilot estimate.

Old note conflates pilot-001’s 13 screened tasks with all 24 task delta 0.0139. Actual survivor delta 0.0256 across 38 cells; task screening is separate from admission discard. README says one seed per cell; preregistration 026 specifies 5 seeds per task-condition, with one session per resulting cell. Method page general preregistration/only-variable claims conflict with explicitly disclosed mid-run 026 and unequal shipped integration instructions. Prefer dated run records. STATUS preserves stale historical sections saying protocol/vendor arms never ran, superseded by its dated September 26 updates. Do not read all paragraphs as current. Official audit warns published tokensPerTask denominator does not match observed-session rates; no dollar/cost ranking certified here. Prefetch prompt contents were not stored, so zero measured label exposure cannot establish no exposure. Prefetch is a changed-query diagnostic, not a mathematical performance ceiling. Separate vendor runs use joined subsets and specific adapter deviations; do not pool their raw rates with 317-cell main results. Historical pilot-001 raw streams incomplete; protocol and corpus changed afterward. Legacy result is a dated record, not an exactly reproducible current run.



Next: Freeze neutral corpus/path names and preregister statistics/exclusions before rerunning. Report all-assigned and admitted sets, separating availability, actual search, evidence arrival and execution. Match lifecycle cost, repeat whole runs and add a distinct longitudinal write/update track.
<!-- EVIDENCE:limitations:END -->
