# KBGym / Training a Knowledge Base

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-08-22<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2608.21829)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](kbgym.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

Reviewed the stated primary paper in full for methods, experimental setup, results and limitations; no independent reproduction.

Read Complete Sections I–VIII, Figures 1–4, Tables I–V, implementation and limitations; appendices inspected: No separate appendices in the reviewed PDF. Not performed: No code/data rerun, causal edge ablation or cross-model reader test

[arXiv v1, 2026-08-22](https://arxiv.org/pdf/2608.21829v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## What changes relative to nearby evaluations

The following is an editorial protocol comparison, not an assertion of direct inheritance unless stated.

Compared with frozen-store RAG and offline graph indexing, KBGym lets supervised questions update store structure before frozen-reader exams. It separates transferable structure from repeated-instance benefits rather than treating training-question efficiency as general persistent memory.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

The knowledge base is the trainable object. A fixed reader searches, reads and submits one answer before gold and F1 are revealed; a separate consolidation phase may add, delete, edit and link documents. Exams freeze the store and hide gold and write tools. KBGym generates a fictional 500-person relational world with 5,864 atomic sentences, initially unlinked, over ten question classes and twenty-six templates; official PhantomWiki provides an external-generator check. Index documents name a key and link to members; one read returns their full one-hop target texts. Evaluation jointly measures answer F1, action cost and provenance-based structural coverage/link quality.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Conditions needed to interpret the results

The nominal 330-question split is 150 train, 100 unseen instances, 50 held-out templates and 30 evaluation questions, but the main run repeats only one hundred training questions for two epochs. Trainer and reader are gpt-5-mini-2025-08-07 at temperature 0.3, low effort and 12,000 completion tokens per turn. Forward/exam budgets are fifteen actions, consolidation thirty, and FIFO memory thirty pairs. Chroma’s default ONNX MiniLM returns five documents per search page, costing one action; linking up to forty edges also costs one action. These tool prices condition the result. The main gradient uses four thirty-query groups from six two-slot templates: trained instances, both keys seen, one key seen and neither seen. Scoring is SQuAD-normalized token F1 without an answer LLM judge; writes have a separate LLM deduplication guard. B2/B3 adapt GraphRAG/HippoRAG-style structures, with no PageRank in B3, rather than reproduce full original systems.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Separate accuracy and action transfer

Thirty tasks per group, same reader and fifteen-action cap. F1 is zero-to-one; action ratio is trained/flat, lower better. Trained-instance 95% bootstrap interval is [0.52,0.84]; both-key/one-key intervals include one. Neither-key 0.904 is significant on KBGym but does not replicate on PhantomWiki.

| Probe group | Flat F1 | Trained F1 | Trained action ratio |
|---|---|---|---|
| Trained question | 0.7 | 0.8 | 0.686 |
| Both keys seen | 0.6 | 0.767 | 0.935 |
| One key seen | 0.767 | 0.867 | 1.032 |
| Neither key seen | 0.833 | 0.833 | 0.904 |

Source: Table IV; Section VII-B · [Paper](https://arxiv.org/pdf/2608.21829v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Absolute performance and structural coverage

All 120 gradient probes, zero-to-one F1 and mean actions per question. Coverage is the fraction of 5,864 source sentences directly linked from at least one authored index. B3 is a lexical entity-hub adaptation, not the complete original HippoRAG-2 algorithm.

| Store | Corpus coverage percent | Actions per query | F1 |
|---|---|---|---|
| Flat store | 0 | 9.8 | 0.725 |
| HippoRAG2-style B3 | 100 | 7.3 | 0.908 |
| Supervised store | 27.6 | 8.7 | 0.817 |

Source: Table III; Section VII-B · [Paper](https://arxiv.org/pdf/2608.21829v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:interpretation:START -->
## What the comparisons establish

On trained instances, the action ratio is 0.686 and F1 rises from 0.700 to 0.800. Accuracy transfers with key coverage, but both-key/one-key action ratios of 0.935/1.032 do not establish general efficiency transfer. Across all 120 probes, B3 is absolutely stronger at F1 0.908 and 7.3 actions versus the trained store’s 0.817 and 8.7. The claimed 1.6×/1.8× benefits normalize gains by corpus coverage; they are not absolute superiority to B3. Excluding trained instances reverses the normalized action advantage to 0.6×. Roughly 3,400-query break-even concerns repeat traffic in the trained population, while full coverage after four hundred new questions is an extrapolation of the early slope.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source discrepancies and next test

Single-seed, same-family trainer/readers and thirty queries per gradient group limit inference; synthetic atomic text differs from real documents. Official PhantomWiki lacks offline baselines and support diagnostics. A single read can expand much text, so action savings need not translate proportionally to tokens, latency or dollars. Full entity indexing covers all documents versus 27.6% supervised coverage; normalization does not control which material is covered or edge-construction cost, nor prove gains persist at full coverage. Continuous online deployment, concurrent maintenance and factual updates are not measured. Next fix visible-token and latency budgets, use multiple seeds and cross-model readers, intervene by deleting index edges, and actually train more unseen keys to test coverage extrapolation.

Nominal train split and Figure 1 say 150 questions; the actual main run uses 100 distinct questions twice. Figure 2 discussion gives trained-group starting F1 0.633, whereas Table IV gives flat-store trained F1 0.700; the exact run/probe alignment is not resolved. Authored-document totals differ: prose classifies 287, whereas Figures 3–4 label 284 indexes and define index documents as surviving authored documents. The figure category includes stubs, unlike the 242 genuine-index classification. Table V lists 220 scored indexes but the five displayed category counts sum to 217; omitted-category accounting is not specified. Only the trained-group action saving replicates significantly on both benchmarks; KBGym neither-key ratio 0.904 is also significant, so no saving anywhere untrained is too absolute.
<!-- EVIDENCE:limitations:END -->

Related benchmarks: [structmemeval](structmemeval.en.md) · [snapshot-compatibility-audit](snapshot-compatibility-audit.en.md)
