# Agent Retrieval Bench: Coding agents must find the right context before writing the patch

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-07-27<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2607.24882)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](agent-retrieval-bench.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

Reviewed the stated primary paper in full for methods, experimental setup, results and limitations; no independent reproduction.

Read Sections 1–13, all retrieval, budget, selective, trajectory and seed-intervention analyses; appendices inspected: A–E, repository counts, every sample example, checkpoint revisions/tokenizer caveat and closed-tool results. Not performed: No repository/artifact rerun or independent semantic label audit

[arXiv v1, 2026-07-27](https://arxiv.org/pdf/2607.24882v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## What changes relative to nearby evaluations

The following is an editorial protocol comparison, not an assertion of direct inheritance unless stated.

Compared with RepoBench’s context-conditioned completion and SWE-bench’s final repair, this isolates workflow-signal-to-next-file retrieval with budgets and natural no-gold abstention. It distinguishes file discovery, useful-line localization and repair; file scores do not replace test success.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

This isolates which repository files a coding agent should read next before editing. The 427 samples span twenty-five repositories: 106 implementation-to-test, eighty review-to-additional-context, 101 failure-trace-to-root-cause and fifty-eight anchored-edit-to-ripple cases, plus fifty naturally externally resolved no-gold cases and thirty-two wrong-repository controls. Positives freeze pre-resolution base commits; given files are excluded from additional targets and exact gold paths, final patches and fix hashes are sanitized. Samples use 271 snapshots, while the reusable manifest has 308 across twenty-nine repositories, about 392,000 files and 7.92 million chunks. Each query searches its own snapshot, not all repositories. Workflow evidence supports labels without exhausting useful files.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Conditions needed to interpret the results

SentenceTransformers embeddings use no recommended query instruction, L2 normalization and cosine retrieval; file scores are maximum chunk scores and all files remain candidates. Qwen4B/8B cap at 40,960 tokens and Jina/Nomic/pplx at 32,768. The pplx run omits the recommended fix_mistral_regex option and is provisional. BCY greedily packs ranked files using a regex code tokenizer, charging path headers and prefix-truncating the boundary; one gold content token earns file exposure, not comprehension or model-token coverage. Main static results cover 345 positives; trajectories/fusion/spans use 287. Abstention uses repository-grouped five-fold calibration maximizing balanced accuracy. The forty-five-query seed pilot fixes Codex GPT-5.5 with sixteen calls, twenty turns, eight thousand post-seed read tokens, twelve hundred per file and three final files. Each sample–arm has one trajectory, with no recorded temperature or seed.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Rankings change with budget and repository weighting

345 positives across twenty-five repositories, all values zero-to-one. Recall covers gold files, MRR uses first-gold rank and BCY counts file exposure within eight thousand regex tokens. Repository macro first averages within repositories, then weights them equally.

| Retriever | Weighted Recall@20 | Weighted MRR | BCY@8k | Repository macro Recall@20 |
|---|---|---|---|---|
| Qwen3-Embedding-4B | 0.6306 | 0.2379 | 0.3409 | 0.6344 |
| Qwen3-Embedding-8B | 0.7029 | 0.2336 | 0.3732 | 0.6193 |
| RepoMap | 0.6333 | 0.2158 | 0.3788 | 0.4619 |

Source: Tables 4–5 · [Paper](https://arxiv.org/pdf/2607.24882v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Negative abstention result on natural no-gold cases

345 positives plus fifty natural no-gold cases, rebuilding five folds after excluding thirty-two wrong-repository controls. Zero-to-one rates; success means correct no-gold abstention or an accepted positive with any gold in top twenty, not gold-file recall.

| Ranker | Positive pass rate | No-gold abstention | Selective success@20 | Always-retrieve success |
|---|---|---|---|---|
| Lexical | 0.423 | 0.58 | 0.294 | 0.499 |
| Jina-0.5B | 0.377 | 0.94 | 0.334 | 0.489 |
| BM25 | 0.188 | 0.98 | 0.22 | 0.463 |

Source: Table 19, natural-only rows · [Paper](https://arxiv.org/pdf/2607.24882v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## Context-seed pilot with fixed tools

Forty-five queries, fifteen per task, one Codex GPT-5.5 trajectory per query/arm. F1 is zero-to-one; other values are query means. Post-seed tokens exclude preload and are not total tokens. The agent submits three files without editing or testing.

| Seed arm | Final File F1 | Tool calls | Post-seed tokens | Seed tokens |
|---|---|---|---|---|
| No seed | 0.3222 | 3.71 | 2137.3 | 0 |
| Random non-gold | 0.3437 | 8.49 | 3681.7 | 2427.8 |
| RRF | 0.3967 | 5.42 | 1856.7 | 3298.8 |
| Oracle gold | 0.6337 | 4.18 | 1736.4 | 1781.3 |

Source: Table 16 · [Paper](https://arxiv.org/pdf/2607.24882v1)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:interpretation:START -->
## What the comparisons establish

Qwen8B leads sample-weighted Recall@20 at 0.7029, but equal weighting of twenty-five repositories favors Qwen4B at 0.6344 over 0.6193. Rankings depend on task/repository composition. Recalibration on natural no-gold cases alone makes every tested threshold policy worse than always returning files, so easy wrong-repository controls must not mask calibration failure. RRF seeds improve File F1 and reduce post-seed reading versus random context, but total reading must include preloaded seeds. One trajectory per arm cannot resolve small differences statistically or establish improved repair success.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source discrepancies and next test

Repositories are purposively sampled and Gin contributes 25.5 percent of positives. Zero violations in specified hygiene checks do not prove freedom from training contamination or exhaustive semantic gold. Results lack repeated-seed intervals and model-specific instruction optimization. File hits may remain far from useful lines, whose median evidence occupies only 4.7 percent of the file. PES is a potential first-hit-delay proxy, not causal tool savings; a post-hoc trajectory prefix is not a smaller-budget rerun. Next intervene on executable repair tasks with fixed model/tools/total tokens/sampling and random, retrieval and oracle seeds, jointly measuring tests and file/span localization.

Appendix B’s comment2context example lists tokio/src/sync/mpsc/chan.rs both as required gold and as a negative distractor. Official all-files gold scoring is clear, but this auxiliary label conflict needs artifact verification. General sanitization prose says raw diffs are removed, while edit2ripple intentionally retains the anchor diff; this permitted anchor is distinct from revealing the target ripple patch. Canonical BCY counts regex tokens; Table 12’s span diagnostic instead uses legacy 8,000-character packing and must not be merged into the same-budget leaderboard. No selected main-table numeric inconsistency found; pplx remains explicitly provisional, and high-budget BCY points may be lower bounds.
<!-- EVIDENCE:limitations:END -->

Related benchmarks: [BEIR](beir.en.md) · [The Recall Trap](recall-trap.en.md) · [BrowseComp-Plus_CM](browsecomp-plus-cm.en.md)
