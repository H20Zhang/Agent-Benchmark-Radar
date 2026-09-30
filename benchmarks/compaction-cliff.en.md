# The Compaction Cliff: preservation scores, behavior and budget boundaries

<!-- RELEASE-REFERENCE:START -->
> **Release diagnostic (historical reference)** · 2026-08-24 · paper v1 snapshot<br>
> **TypeCompact — Constraint recall after five compaction rounds: 96%** (Constraint recall after five compaction rounds)<br>
> Five-round constraint-retention diagnostic for the deterministic TypeCompact operator. Claude Sonnet is a separate comparator, not its answer model. The public artifact covers 20 configurations and five nominal 50%-target rounds; 96% is the rounded paper value. [Original source](https://arxiv.org/html/2608.22752v1)<br>
> The released implementation carries untruncated typed state but truncated LLM text. This diagnostic does not establish equal-feasible-budget superiority or a general safety guarantee. Experiments were not rerun.
<!-- RELEASE-REFERENCE:END -->

[中文](compaction-cliff.md) | **English**

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Reviewed the stated paper version, method, experimental setup, key results and limitations; no independent reproduction.

Read all six main sections, all ten tables, algorithms and limitations; this version has no appendix. Read pinned README, complete operators.py, preservation.py, safety_margin.py and multiturn_stability.py, plus its frozen JSON. No independent execution or full behavioral-run audit.

[arXiv 2608.22752v1 (2026-08-24)](https://arxiv.org/html/2608.22752v1)

[Auxiliary material (checked 2026-09-30)](https://github.com/searchsim-org/cikm26-knowledge-triage/blob/a6ceb01a3368cee25ef7ebcf05ebdab8c9be24a4/README.md)

[Auxiliary material (checked 2026-09-30)](https://github.com/searchsim-org/cikm26-knowledge-triage/blob/a6ceb01a3368cee25ef7ebcf05ebdab8c9be24a4/knowledge_triage/operators.py)

[Auxiliary material (checked 2026-09-30)](https://github.com/searchsim-org/cikm26-knowledge-triage/blob/a6ceb01a3368cee25ef7ebcf05ebdab8c9be24a4/knowledge_triage/preservation.py)

[Auxiliary material (checked 2026-09-30)](https://github.com/searchsim-org/cikm26-knowledge-triage/blob/a6ceb01a3368cee25ef7ebcf05ebdab8c9be24a4/knowledge_triage/safety_margin.py)

[Auxiliary material (checked 2026-09-30)](https://github.com/searchsim-org/cikm26-knowledge-triage/blob/a6ceb01a3368cee25ef7ebcf05ebdab8c9be24a4/experiments/multiturn_stability.py)

[Auxiliary material (checked 2026-09-30)](https://github.com/searchsim-org/cikm26-knowledge-triage/blob/a6ceb01a3368cee25ef7ebcf05ebdab8c9be24a4/results/multiturn_stability.json)

The frozen release reference is preserved; newer paper results do not replace initial-release scores.
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## How tasks create memory demands

The paper proposes Knowledge Triage alongside compaction, partitioning, retrieval and behavioral tests. It classifies each line as constraint, procedure, belief, preference or episode. TypeCompact pins constraints/procedures; TypeDecompose replicates constraints into applicable partitions; TypeRetrieve prioritizes in-scope constraints. SafetyMargin asks a model whether removing an item could make an action unsafe: this is a model estimate, not a real action intervention. An allergy fact, for example, can require hard retention without containing a prohibition word.

Genealogy: The paper’s closest methodological comparison is MaRS typed memory with a single utility objective; the changed coordinate is type-specific fidelity. MaRS-FL is the authors’ reimplementation, not an official MaRS run. Relative to LLMLingua-2 compression, constraint preservation takes priority. The work constructs AAC while reusing retail, airline and retrieval tasks; their distinct protocols do not form one safety score.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental settings and scoring targets

AAC contains 396934 configuration artifacts from 54628 public repositories, not that many evaluation instances per experiment. Typology uses 2000 annotations; structural compaction uses 50 configurations, LLM/multiround comparisons 20; decomposition uses 200. Retrieval mixes 1000 scifact distractors with 33 retail-policy chunks and 50 handwritten queries. Its gold set is the in-scope subset of 22 classifier-flagged constraints, averaging twelve per query, not an independent human inventory of all real constraints. Automated preservation checks at most five key substrings anywhere in the output and can miss weakened meaning. Claimed operator guarantees require correct typing/scope and feasible budgets; they do not guarantee compliant actions.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Table 6 and Figure 3, selected constraint-preservation results

Constraint-preservation proportions, averaged by configuration. The first three columns are single-round targets; the last is a separate five-round test at 50% each round. LLM outputs are truncated before scoring. Zero inference tokens for the deterministic operator exclude indexing-time classification.

20 configurations in the LLM and multiround comparison; blank means no reported five-round MaRS-FL row.

| Method | Single round 50% budget | Single round 25% budget | Single round 10% budget | Fifth round |
|---|---|---|---|---|
| TypeCompact | 1 | 0.95 | 0.8 | 0.96 |
| MaRS-FL | 0.99 | 0.75 | 0.43 | — |
| Sonnet 4.6 | 0.53 | 0.39 | 0.24 | 0.1 |

Locator: Table 6 and Figure 3, selected constraint-preservation results · [Source](https://arxiv.org/html/2608.22752v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Table 7, selected decomposition results

Keep the two reported violation aggregates separate. Section-header topic markers provide shared scope information. Replication overhead has median zero and maximum 219%; implementation budget boundaries are discussed below.

200 AAC configurations; 25%-of-total partition budget.

| Method | Mean violation % | Configurations with violation % | Mean extra tokens % |
|---|---|---|---|
| chunk_by_tokens | 32 | 93 | 0 |
| chunk_by_topic | 13 | 40 | 0 |
| TypeDecompose | 0 | 0 | 14.5 |

Locator: Table 7, selected decomposition results · [Source](https://arxiv.org/html/2608.22752v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## Table 8, selected retrieval controls

Recall covers only classifier-flagged, topic-matched constraints. Sonnet selects/ranks from dense top-100 candidates; TypeRetrieve directly pins the in-scope set. Perfect recall requires enough slots and does not extend to k=5.

50 queries over 1033 items; query-specific gold denominators average twelve.

| Retriever | Recall@5 % | Recall@20 % | Recall@50 % |
|---|---|---|---|
| Dense (octen) | 34 | 67 | 91 |
| Sonnet 4.6 | 34 | 61 | 73 |
| TypeRetrieve | 40 | 96 | 100 |

Locator: Table 8, selected retrieval controls · [Source](https://arxiv.org/html/2608.22752v1)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:result-4:START -->
## Section 4.5 and Table 10, selected behavioral results

The hierarchical baseline keeps the head; it is not general LLM summarization. Retail has 115 tasks times three models, with 329 of 345 possible model-task pairs complete; airline has 117 complete pairs from 50 tasks times three models. SafetyMed separately reports Sonnet compaction at 92.5% pass/81% preservation versus TypeCompact at 97%/95.5%.

SafetyMed 200 scenarios. Retail/airline exclude incomplete matched cells. Retail retains 1338/669/1136 tokens for full/head/TypeCompact; airline head/TypeCompact uses 718/647.

| Setting | Full-policy pass % | Head-truncated pass % | TypeCompact pass % | Complete matched pairs |
|---|---|---|---|---|
| SafetyMed | 96.5 | 98 | 97 | 200 |
| Retail | 28.6 | 29.2 | 37.7 | 329 |
| Airline | 34.2 | 15.4 | 26.5 | 117 |

Locator: Section 4.5 and Table 10, selected behavioral results · [Source](https://arxiv.org/html/2608.22752v1)
<!-- EVIDENCE:result-4:END -->

<!-- EVIDENCE:result-5:START -->
## Sections 4.4–4.5, selected classifier and scoring diagnostics

The first two rows concern declarative rewrites of fifty known constraints. The last two concern preservation audits; kappa and agreement are different statistics. Classifier labels separately have human kappa 0.45 for five classes and 0.79 for constraint versus other.

Phrasing experiment has 50 base rules times four forms; preservation audit has 100 cells, eighty double-labeled.

| Check | Value | Denominator |
|---|---|---|
| Grammatical declarative recall | 0.62 | 50 |
| SafetyMargin declarative recall | 0.9 | 50 |
| Human-human binary kappa | 0.92 | 80 |
| Automatic-human agreement | 0.79 | 100 |

Locator: Sections 4.4–4.5, selected classifier and scoring diagnostics · [Source](https://arxiv.org/html/2608.22752v1)
<!-- EVIDENCE:result-5:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and next validation

Preservation is not behavioral correctness, and full policy is not a universal ceiling: TypeCompact exceeds it on retail and falls below it on airline without a significant difference. Nonsignificance is not equivalence. Extra retail tokens confound attribution; the reversed airline budget does not supply a token-matched control on the same tasks. Human audits show that key-token scoring can credit rules missing qualifiers; human-human kappa 0.92 does not validate automated scoring at that level.

The pinned implementation also materially differs from the paper algorithm. TypeCompact in operators.py lacks the described restoration verifier; TypeDecompose does not rebalance after replication. The multiround script ignores COMPACTION_UNSAFE, truncates scored text at four characters per token, but carries the untruncated object forward; the LLM carries truncated text forward. Treat 96% as that reported diagnostic, not certification of a safe budget invariant. Scope/classification errors and insufficient capacity require separate tests.

Table 6 gives LLMLingua-2 recall 0.21/0.08/0.01, whereas ablation prose gives 0.55/0.18/0.02 without reconciling settings. The limitations’ 19–42% single-round range also differs from main Table 6; keep explicit table values. README calls 73% a dense-retrieval baseline, but paper Table 8 assigns it to Sonnet; dense is 91%. README table numbering is stale. The checked code’s locality helper counts constraints with any uncovered partition, not directly the prose’s fraction of offending partitions; frozen reported Table 7 values are not independently recomputed. The full AAC distribution requires a data-use agreement according to README; no gated access was attempted. No full retail/airline trace audit was performed.



Next: Pair with GateMem behavior gating and MemoryAgentBench revision tasks. First test consistent budget accounting, Unsafe handling and cross-round state. Under matched retained tokens, vary labels, pinning and verifier separately. Report classifier recall, semantic preservation, scope coverage, compliance and legitimate task success, including uncertain rules and hard constraints exceeding capacity.
<!-- EVIDENCE:limitations:END -->
