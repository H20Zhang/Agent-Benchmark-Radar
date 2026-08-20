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

## Preferred prose

- Explain benchmark purpose before protocol jargon.
- Name the predecessor before calling a benchmark important.
- Use concrete capability/environment/protocol nouns.
- State causal boundaries explicitly: `这是 system-level result` / `the protocol does not isolate retrieval policy`.
- Treat scale as novelty only when scale fixes a known validity problem.
- Use numbers only when they change interpretation.
- Keep the strongest confounder visible near the claim it weakens.

## AI-house-style patterns to avoid

Warn on repeated patterns across nearby entries:

- `真正重要的是…`, `关键不在于…而在于…`, `值得注意的是…` used as generic openers;
- `this matters because…`, `the key thing is…`, `the important point is not…` repeated across benchmarks;
- generic praise (`comprehensive`, `robust`, `groundbreaking`, `重要`, `全面`) without a predecessor/evidence cue;
- marketing language and emoji-heavy decoration;
- forced three-part symmetry;
- calling every recent benchmark `frontier` as a prestige label rather than a time-relative analytical role.

The target is pattern density and loss of specificity, not banned words.

## README fold contract

A 60–90 second fold should explain: predecessor limitation, capability × environment × protocol delta, what the score supports, strongest confounder, and why this changes the field map. Use 2–4 natural paragraphs rather than five mechanical mini-headings.

## Epistemic language

- paper/protocol fact: `论文报告…` / `the benchmark specifies…`;
- curator interpretation: `这说明 measurement object 正在…` / `this suggests the evaluation object is moving toward…`;
- open hypothesis: `下一代最需要补的 coordinate 是…` / `the next missing coordinate is…`.

Do not turn a leaderboard observation into component evidence without matched conditions.
