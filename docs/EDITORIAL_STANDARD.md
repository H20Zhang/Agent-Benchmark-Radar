# Research Radar Editorial Standard

This is the prose contract for reader-facing Agent Benchmark Radar content.

## Benchmark reasoning before prose

For a high-value benchmark or protocol change, settle these questions before drafting:

1. **Measurement delta** — what newly becomes measurable?
2. **Predecessor / implicit critique** — what was the closest earlier benchmark, and what was too easy, narrow, static, synthetic, opaque, or weakly diagnosed?
3. **What it actually measures** — capability, environment, accessible state, task, and target behavior.
4. **Protocol** — tools/interfaces, model/harness assumptions, hints, retries/trials, stopping rule, metrics/judge, executable validation, and relevant resource budgets.
5. **What a score supports** — system-level claim versus any justified component-level attribution.
6. **Strongest confounder / validity risk** — contamination, saturation, judge dependence, environment drift, hidden hints, harness sensitivity, synthetic shortcuts, or lifecycle cost.
7. **What remains unmeasured** — the next missing coordinate made visible by this benchmark.
8. **Genealogy consequence** — precursor / foundation / transition / frontier, plus the nearest continuation.

## Chinese-first bilingual rule

`README.md` is Simplified Chinese by default. `README.en.md` is the complete English counterpart. Reader-facing library/note/synthesis surfaces should preserve the same semantic benchmark judgment across languages.

Keep benchmark names, paper titles, dataset/model/metric/protocol/tool names, and standard acronyms in canonical English form when that improves precision and literature search.

Chinese sentences should still have a Chinese grammatical spine: use Chinese verbs, connectives, and descriptive phrases. Keep English for proper names, standard acronyms such as RAG/QA/SQL/API, and terms whose canonical form materially improves search. When a less familiar English term is necessary, introduce it once as `中文（English）` rather than using English noun phrases as substitutes for Chinese predicates.

## Preferred prose

- Explain benchmark purpose before protocol jargon.
- Name the predecessor before calling a benchmark important.
- Use concrete capability/environment/protocol nouns.
- State causal boundaries explicitly: `这是 system-level result` / `the protocol does not isolate retrieval policy`.
- Treat scale as novelty only when scale fixes a known validity problem.
- Use numbers only when they change interpretation.
- Keep the strongest confounder visible near the claim it weakens.
- Treat README as a data-rich awesome list: put complete tables and direct links ahead of framing prose.
- Layer-level attention navigation (`30 sec → 3 min → 5 min → 15 min → browse all`) is a stable reader contract; it names the depth of a route, not the value of an individual item.
- Keep the same information contract across table rows, but vary the syntax. Repeating `相比 X，把 A 推进到 B` in every row is not a style guide.
- Emoji are allowed when they carry a stable meaning, such as evolution roles; do not use them as decoration.

## AI-house-style patterns to avoid

Warn on repeated patterns across nearby entries:

- `真正重要的是…`, `关键不在于…而在于…`, `值得注意的是…` used as generic openers;
- `this matters because…`, `the key thing is…`, `the important point is not…` repeated across benchmarks;
- generic praise (`comprehensive`, `robust`, `groundbreaking`, `重要`, `全面`) without a predecessor/evidence cue;
- marketing language and emoji-heavy decoration;
- forced three-part symmetry;
- Chinese sentences assembled from English noun phrases joined by Chinese particles;
- per-entry reading-time promises and generic meta headings such as “what this tells us”;
- a summary chain immediately followed by a table that already contains the same chronology;
- identical `frontier signal / biggest gap` wrappers repeated for every area whether or not the prose needs them;
- calling every recent benchmark `frontier` as a prestige label rather than a time-relative analytical role.

The target is pattern density and loss of specificity, not banned words.

## README disclosure contract

Every Timeline item keeps the five predictable same-level fields `Question / Evidence / Caveat / Map / Links` (and their Chinese counterparts) so a reader can expand one row and orient immediately. Write natural, concise sentences inside those fields; do not turn the labels themselves into five repetitive slogans or copy the full deep note into the README.

## Epistemic language

- paper/protocol fact: `论文报告…` / `the benchmark specifies…`;
- curator interpretation: `这说明 measurement object 正在…` / `this suggests the evaluation object is moving toward…`;
- open hypothesis: `下一代最需要补的 coordinate 是…` / `the next missing coordinate is…`.

Do not turn a leaderboard observation into component evidence without matched conditions.
