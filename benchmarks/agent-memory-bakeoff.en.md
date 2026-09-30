# Agent Memory Bakeoff: write enrichment under query vocabulary shifts

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-08-21<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://github.com/JaysonRawlins/agent-memory-bakeoff)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](agent-memory-bakeoff.md) | **English**

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Reviewed the pinned official protocol, settings, result artifacts and limitations; no independent reproduction.

Read pinned README and complete corpus/query generation, topic universe, retrieval runner and scorer. Parsed checked-in corpus/query counts and inspected a source scenario with its sibling documents. No independent retrieval run; the tree contains no committed raw retrieval-result matrix.

[57585be8bcf735ef783fc0b8134e809b943d9695](https://github.com/JaysonRawlins/agent-memory-bakeoff/blob/57585be8bcf735ef783fc0b8134e809b943d9695/README.md)

[Auxiliary material (checked 2026-09-30)](https://github.com/JaysonRawlins/agent-memory-bakeoff/blob/57585be8bcf735ef783fc0b8134e809b943d9695/gen/generate_corpus.py)

[Auxiliary material (checked 2026-09-30)](https://github.com/JaysonRawlins/agent-memory-bakeoff/blob/57585be8bcf735ef783fc0b8134e809b943d9695/gen/generate_queries.py)

[Auxiliary material (checked 2026-09-30)](https://github.com/JaysonRawlins/agent-memory-bakeoff/blob/57585be8bcf735ef783fc0b8134e809b943d9695/runners/retrieve.py)

[Auxiliary material (checked 2026-09-30)](https://github.com/JaysonRawlins/agent-memory-bakeoff/blob/57585be8bcf735ef783fc0b8134e809b943d9695/eval/score.py)

[Auxiliary material (checked 2026-09-30)](https://github.com/JaysonRawlins/agent-memory-bakeoff/blob/57585be8bcf735ef783fc0b8134e809b943d9695/data/queries/queries.jsonl)

The frozen release reference is preserved; newer paper results do not replace initial-release scores.
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## How tasks create memory demands

Agent Memory Bakeoff is a retrieval-component experiment. A fictional operations scenario yields one to three sibling memories; plain and enriched indexes differ only by two or three future-search phrases and a symptom description. BM25, vector and fused retrieval use the same documents and queries. It directly varies write representation without an answer model, measuring accessibility rather than answer or action quality.

Genealogy: This is a synthetic public check motivated by the author’s private memory system, not data derived from LoCoMo or LongMemEval. Relative to those downstream QA benchmarks, the changed coordinate is the stopping point: retrieving any sibling from the right scenario is sufficient. Claims about private blind evaluation and latency lack public traces here and are not verified public-benchmark results.
Illustrative query shift: a document records a fault under an internal cache-module name, while a later query only describes seeing stale values after an update. Enrichment adds symptom language at writing time; scoring checks retrieval of a same-scenario document, not repair success.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental settings and scoring targets

The pinned data contain 225 scenarios, 497 documents and 390 queries from 130 scenarios, with one identifier, conceptual and symptom query each. claude-haiku-4-5 generates documents, enrichment and queries. Queries see hidden scenarios but not document text/search phrases, reducing direct copying without eliminating shared-model or scenario dependence. BM25 uses bm25s defaults and English stopwords; local nomic-embed-text supplies cosine vectors. Hybrid scores use per-query min-max normalization, then α times BM25 plus 1−α times vector. α is swept from 0.1 to 0.9 without a separate tuning set. MRR uses the first sibling hit within ten; Recall@1/@5 is query-level any-gold-hit rate, not coverage of every relevant document.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## README Results, selected matched write-representation comparisons

Same underlying documents, queries and gold sets; enrichment adds indexed text without matching storage or write-time compute. MRR is 0–1; other columns are percentages.

390 total queries, 130 per bucket; shared scenario clusters mean queries are correlated.

| System | MRR@10 | Recall@1 % | Recall@5 % | Symptom Recall@5 % |
|---|---|---|---|---|
| bm25-plain | 0.678 | 58.7 | 79.7 | 60 |
| bm25-enriched | 0.783 | 70.3 | 89.7 | 83.8 |
| vector-plain | 0.565 | 46.7 | 69.7 | 39.2 |
| vector-enriched | 0.625 | 52.1 | 76.7 | 63.1 |

Locator: README Results, selected matched write-representation comparisons · [Source](https://github.com/JaysonRawlins/agent-memory-bakeoff/blob/57585be8bcf735ef783fc0b8134e809b943d9695/README.md)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## README Results, selected enrichment-versus-fusion contrasts

The best α is selected on the same query set. MRR rises by 0.023, but Recall@5 does not improve and conceptual-bucket recall falls. The selected optimum is not a held-out generalization gain.

390 queries; identifier/conceptual each 130. No repeated-run or cluster-bootstrap intervals are reported.

| System | MRR@10 | Recall@5 % | Identifier Recall@5 % | Conceptual Recall@5 % |
|---|---|---|---|---|
| bm25-enriched | 0.783 | 89.7 | 99.2 | 86.2 |
| hybrid α=0.5 enriched | 0.801 | 90.5 | 99.2 | 86.9 |
| hybrid α=0.6 enriched | 0.806 | 89.7 | 99.2 | 84.6 |

Locator: README Results, selected enrichment-versus-fusion contrasts · [Source](https://github.com/JaysonRawlins/agent-memory-bakeoff/blob/57585be8bcf735ef783fc0b8134e809b943d9695/README.md)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and next validation

This supports write-enrichment gains for BM25 on this synthetic corpus, not universal redundancy of embeddings. Enrichment and queries deliberately use symptom vocabulary, and all scenario siblings are gold without human verification that each answers every query. The released data are fixed; regeneration is not deterministic. No stable embedding digest, raw full retrieval matrix, uncertainty intervals or public latency table are supplied, so private-system cost claims cannot become quantitative conclusions here.

README says the entire gain is concentrated in symptoms, but conceptual Recall@5 also rises from 79.2% to 86.2%, while identifier recall falls from 100% to 99.2%. Queries are blind to document text, not statistically independent: each three-query cluster shares one scenario and the generation model. The retrieval cache is keyed by file name and row count rather than corpus content hash; unchanged row counts after edits can reuse stale vectors unless caches are cleared.



Next: Pair with LongMemEval or InMind using natural, scenario-held-out queries. Compare write expansion, query expansion and reranking under matched extra-token budgets, then measure answer utility and erroneous enrichment. Bootstrap scenarios rather than individual queries, tune α separately, and retain model digests plus full rankings.
<!-- EVIDENCE:limitations:END -->
