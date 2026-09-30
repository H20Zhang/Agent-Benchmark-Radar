# EAL-Bench: authorization errors form in memory and propagate to action

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-09-01<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2609.01836)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](eal-bench.md) | **English**

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Reviewed the stated paper version, method, experimental setup, key results and limitations; no independent reproduction.

Read main Sections 1–5 and Appendices A–D: domain rules, writer templates and schemas, full seed/memory matrices, capacity/pressure experiments, mitigation protocols and exact treatment text. PDF checked for table/count consistency; plotted effect coordinates not digitized. No implementation audit or independent reproduction.

[arXiv 2609.01836v1 (2026-09-01)](https://arxiv.org/html/2609.01836v1)

The frozen release reference is preserved; newer paper results do not replace initial-release scores.
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## How tasks create memory demands

EAL-Bench studies how ordinary memory updates preserve narrowed or revoked permissions as valid authority without an external attacker. A hidden deterministic ledger replays authorization events; a writer turns history into persistent memory, and a fresh executor sees only that memory and the current request. Paired authorized/unauthorized requests differ in one authorization-relevant field. Typed memory supports a deterministic false-authority indicator F before execution; issuing the requested action G is measured separately. Free-text memory has no equivalent deterministic F label and is evaluated through behavior and memory replacement instead.

Editorial placement: AuthMem-Bench fixes claims and swaps source authority; EAL-Bench changes authorization history through grants, narrowing, revocation and replacement. It adds incremental state maintenance and formation-to-propagation diagnosis. Both include action-side tests; AuthMem-Bench is not write-only. This is an evaluation-coordinate comparison, not a claim of direct dataset inheritance.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental settings and scoring targets

Procurement has 12 cases/36 request pairs, 65–84 turns and 5–6 blocks per case; cybersecurity has 16/64, 120 turns and 10 blocks; finance has 8/32 and 18 blocks. LangMem 0.0.30 maintains one profile in a text/typed × one-shot/incremental design. Incremental writers see only previous memory plus the new block. Capacity is twice the largest faithful calibration payload; each update permits one attempt and one repair, retaining the old profile if both fail. Writers are Nemotron 3 Ultra, Kimi K2.6, GLM 5.2, Grok 4.3 and Qwen-Plus 2025-07-28; executors are GPT-OSS-120B and DeepSeek V4 Pro. Three writer seeds, temperature 1 and 4096 output tokens are used; the same frozen memory is replayed behind both executors. Deterministic rules score exact calls without an LLM judge. Tools are simulated scored functions, not live purchases, system changes or trades.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Tables 2, 6 and 12, selected three-seed representation comparison

US is unauthorized submission, AU authorized use and F false authority represented in memory. Behavior pools five writers, three seeds and two executors; F is measured from writer artifacts, not doubled as independent writes for executor replays.

Behavior per side/condition: Procurement 1080, Cybersecurity 1920, Finance 960; formation denominators are respectively 540, 960, 480.

| Domain | Typed one-shot US (%) | Typed incremental US (%) | Typed incremental AU (%) | Typed incremental F (%) |
|---|---|---|---|---|
| Procurement | 1.6 | 28.9 | 96.8 | 28.3 |
| Cybersecurity | 0.8 | 10.4 | 88.8 | 10.4 |
| Finance | 0.4 | 51.0 | 98.3 | 50.2 |

Locator: Tables 2, 6 and 12, selected three-seed representation comparison · [Source](https://arxiv.org/html/2609.01836v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Table 3, targeted exact-state replacement

Only naturally generated F=1 memories are selected; request and executor are held fixed while memory is replaced. Pooled 205/208=98.6% becomes 0/208: conditional propagation, not all-request failure. Exact state comes from the benchmark oracle, not a deployable automatic repairer.

68/60/80 selected trials per domain, 208 total; these are a targeted intervention population, separate from the three-seed full matrix.

| Domain | Unauthorized calls with erroneous memory | Unauthorized calls after exact repair | Trials per arm |
|---|---|---|---|
| Procurement | 66 | 0 | 68 |
| Cybersecurity | 60 | 0 | 60 |
| Finance | 79 | 0 | 80 |

Locator: Table 3, targeted exact-state replacement · [Source](https://arxiv.org/html/2609.01836v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## Section 4.4 and Tables 21, 24, aligned mitigation comparison

Paired on the same three-seed typed-incremental population. Source gating checks visible citations and authorization-capable issuers, not semantic support. Event sourcing combines model-extracted changes, an external immutable log and deterministic state reduction; it is a package intervention.

3960 authorized and 3960 unauthorized behavior trials per arm. Paired bootstrap resamples writer–case trajectories 10,000 times.

| Mechanism | US (%) | AU (%) |
|---|---|---|
| Typed incremental | 25.3 | 93.3 |
| Gold source-authority gate | 7.3 | 53.8 |
| Bounded event sourcing | 9.0 | 64.7 |

Locator: Section 4.4 and Tables 21, 24, aligned mitigation comparison · [Source](https://arxiv.org/html/2609.01836v1)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:result-4:START -->
## Table 24, event-sourcing domain effects

Same writer/case/request/executor population. Safety improvement must be read beside legitimate-action loss; finance’s low US accompanies extensive rejection of authorized requests, not near-perfect authorization.

Procurement 1080 and Finance 960 trials per side/arm, pooled across three seeds.

| Domain | Baseline US (%) | Event US (%) | Baseline AU (%) | Event AU (%) |
|---|---|---|---|---|
| Procurement | 28.9 | 10.7 | 96.8 | 89.5 |
| Finance | 51.0 | 6.9 | 98.3 | 13.3 |

Locator: Table 24, event-sourcing domain effects · [Source](https://arxiv.org/html/2609.01836v1)
<!-- EVIDENCE:result-4:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and next validation

Faithful-memory controls select executors reaching 100% AU and zero US on these fixed requests, so high propagation characterizes two calibrated executors, not arbitrary agents. Whole-memory replacement is a strong local intervention but does not prove that execution-side constraints can never help. Executors receive the complete bounded memory, with no retrieval/access-control test or source dereferencing. Claude Opus 4.8 assisted scenario generation and authors reviewed cases; authorization events are unusually explicit, and domains share a closed-world ledger structure. Domain differences are not industry prevalence estimates.

The main text reports pooled formation 24.9%, supported by Appendix A.5’s 494/1980, whereas Tables 21/25 print 25.0%; preserve this minor reporting discrepancy rather than silently reconciling it. Table 4 and pressure comparisons use one fixed seed, unlike the three-seed main matrix. Procurement’s scaling experiment reports zero self-repair, but the broader three-domain incremental analysis reports 207/5550 (3.7%); these scopes must remain separate. The capacity ablation changes a visible budget/enforcement, not retrieval or full-history access, and larger budgets were barely used. Oracle-exact selection is a diagnostic pool ceiling, not a universal achievable performance bound.



Next: Extend the existing 2×2, cross-executor and exact-repair controls with source-retrieving executors, hard permission checks, missing/conflicting history, concurrent writers and real tool failures. Ablate gating/event-sourcing components under matched information and call budgets; report unauthorized calls, legitimate use, missed events and recovery costs together.
<!-- EVIDENCE:limitations:END -->
