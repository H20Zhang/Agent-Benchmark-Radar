# Beyond Goldfish Memory: multisession training, summary memory and dialogue quality

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2022-05<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://aclanthology.org/2022.acl-long.356/)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](beyond-goldfish-memory.md) | **English**

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Reviewed the stated paper version, method, experimental setup, key results and limitations; no independent reproduction.

Read the final 18-page ACL paper, Sections 1–7 and Appendices A–D, all fifteen tables, and rendered image-only summary/conversation/opening examples plus collection/evaluation interfaces on pages 14–18. No implementation audit or independent model training/evaluation.

[ACL 2022 final (2022-05)](https://aclanthology.org/2022.acl-long.356.pdf)

[Auxiliary material (checked 2026-09-30)](https://aclanthology.org/2022.acl-long.356/)

The frozen release reference is preserved; newer paper results do not replace initial-release scores.
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## How tasks create memory demands

Beyond Goldfish Memory introduces Multi-Session Chat (MSC), where two roles resume conversation after simulated hours or days, testing how previous interaction supplies personal knowledge. Crowdworkers can change between sessions while roles remain fixed; this is not a months-long relationship between the same real users. Session one directly inherits PersonaChat, followed by new human dialogue and turn-level salient-information summaries, establishing actual data genealogy.

Compared with a fixed PersonaChat profile, MSC expands personal knowledge through interaction and reserves a fifth session beyond training-session length. SumMem trains a supervised summarizer to write new personal information or no-summary, then retrieves summary memories to generate replies. RAG, FiD and FiD-RAG distinguish retriever training and decoder fusion. This is an early foundation for later long-conversation memory evaluation, without testing tool actions, authority revocation or physical deletion.
Illustrative continuation: after discussing a pet in an earlier session, a later opening asks how the pet is doing. Summary memory should support continuity, while more references to old topics do not automatically establish detail-level correctness.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental settings and scoring targets

Training contains 4000 three-session series and 1001 four-session series; validation/test session five contain 500/501 episodes. Summing per-session rows does not count independent personas. Sessions typically have six or seven turns per speaker; five-session test histories average about 66 utterances and 1614 BlenderBot BPE tokens. The 1155 role profiles are separated between training and validation/test. Models initialize from BlenderBot BST 2.7B and fine-tune on MSC, with 128/512/1024 encoder truncation. DPR retrieves whole-session or summary documents; N is selected from 3/5/6 on validation. Training uses up to eight 32GB V100s, 4000 updates and batch size 128, typically eight hours for standard models and sixteen for retrieval models. Automatic metrics use ParlAI defaults: lower perplexity is better, while lexical F1/BLEU are not memory-fact accuracy.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Table 7, selected test perplexity comparisons

Test set; lower perplexity is better. BST-to-MSC changes training data as well. Differences from MSC-1024 better represent incremental memory architecture, although retrieval computation differs.

Test session 2: 501 episodes/5939 utterances; session 5: 501/5945. Perplexity aggregates token likelihood, not a count of correct episodes; opening rows use opening responses.

| Model | Session 2 perplexity | Session 5 perplexity | Session-opening perplexity |
|---|---|---|---|
| BST 2.7B | 9.98 | 10.5 | 12.92 |
| MSC 2.7B (truncate 1024) | 8.76 | 9.16 | 8.09 |
| MSC 2.7B (FiD-RAG) | 8.75 | 9.11 | 8.03 |
| SumMem-MSC 2.7B (FiD-RAG) | 8.7 | 9.07 | 7.87 |

Locator: Table 7, selected test perplexity comparisons · [Source](https://aclanthology.org/2022.acl-long.356.pdf)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Table 4, selected validation context controls

Same BST 2.7B-1024 initialization with MSC training. Human gold summaries are diagnostic context, not a deployable writer. Openings depend more on old information and show larger gaps than the full session.

Validation session 5: 500 episodes, 5964 utterances; opening perplexity uses only opening responses.

| Context | Session 5 perplexity | Session 5 opening perplexity |
|---|---|---|
| No session history | 9.3 | 10.46 |
| Dialogue history | 9.08 | 7.94 |
| Gold summary | 8.96 | 7.77 |
| Predicted summary | 9.0 | 7.81 |

Locator: Table 4, selected validation context controls · [Source](https://aclanthology.org/2022.acl-long.356.pdf)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## Table 8, selected human conversation evaluations

Fifth-session conversations with validation personas; workers receive summaries of four prior sessions. Each new conversation has seven human and eight bot messages. Percentages use annotated replies, final ratings whole conversations; reply counts are not independent conversation counts. RAG and FiD-RAG lead different metrics.

Response counts shown per row. Exact independent conversation/worker counts are not printed. Reported t-tests compare with BST, not every pair among memory models.

| Model | Partner-topic reference % | Engaging responses % | Final rating / 5 | Annotated responses |
|---|---|---|---|---|
| BST 2.7B | 14.5 | 53.0 | 3.14 | 668 |
| MSC 2.7B (truncate 1024) | 22.5 | 54.2 | 3.47 | 653 |
| SumMem-MSC 2.7B (RAG) | 33.8 | 62.1 | 3.65 | 668 |
| SumMem-MSC 2.7B (FiD-RAG) | 26.4 | 59.3 | 3.68 | 649 |

Locator: Table 8, selected human conversation evaluations · [Source](https://aclanthology.org/2022.acl-long.356.pdf)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:result-4:START -->
## Appendix A Tables 13–14, selected test lexical metrics

Original reported scales; lexical overlap against reference replies. Open dialogue can have multiple good answers, so these are not task-success percentages.

Same test-session pool as Table 7; opening responses are a separate subset.

| Model | Session 5 F1 | Opening F1 | Session 5 BLEU-4 | Opening BLEU-4 |
|---|---|---|---|---|
| BST 2.7B | 19.4 | 13.7 | 0.57 | 0.107 |
| MSC 2.7B (truncate 1024) | 20.0 | 14.1 | 0.631 | 0.139 |
| SumMem-MSC 2.7B (FiD-RAG) | 20.2 | 14.5 | 0.678 | 0.222 |

Locator: Appendix A Tables 13–14, selected test lexical metrics · [Source](https://aclanthology.org/2022.acl-long.356.pdf)
<!-- EVIDENCE:result-4:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and next validation

The clearest evidence is that multisession training and access to history help; automatic gains from summary retrieval beyond the stronger 1024-token baseline are modest. All improvement cannot be attributed to retrieval, and more topic references do not establish factual correctness. Three-to-five-session experiments do not validate indefinite memory; persistent storage cannot guarantee perfect retrieval/generation. Role-play and instructions to continue earlier topics shape both collection and human evaluation. No persona/conversation-clustered intervals are provided. The ethics section says memory stays private to the individual conversation, but leakage and privacy guarantees are not separately tested.

Table 9 prints Unique counts larger than Total, inconsistent with its near-100% uniqueness percentages; do not use those columns to certify exact deduplication counts. The prose says keeping the self summary is slightly more important, while Table 4’s partner-only row has lower perplexity than self-only; report rows rather than that interpretation. Table 5 sparsity caption says how often a summary is generated, but the prose identifies the gold 42% as no-summary frequency; that convention is ambiguous, so it is not used as a memory-size result.



Next: Pair with LoCoMo, first comparing raw versus predicted-summary memory with the same backbone/training data and matched retrieval tokens/candidates. Separately evaluate factual correctness, contradictions and engagement at openings versus mid-session. Extend session length and add profile changes, reporting persona-series intervals rather than relying only on lexical similarity.
<!-- EVIDENCE:limitations:END -->
