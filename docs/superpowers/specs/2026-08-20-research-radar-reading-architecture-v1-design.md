# Research Radar Reading Architecture v1

Date: 2026-08-20

## Problem statement

Agent Benchmark Radar already has a strong conceptual spine: new benchmarks reveal what the field has started to care about, while historical benchmarks explain how today’s evaluation target emerged. The main remaining problem is navigation depth. New & Notable scans well, but long per-area tables will keep growing; benchmark genealogy, current frontier, measurement gaps, and protocol caveats compete for the same README space. The repository also lacks a stable note/editorial standard comparable to the paper radars.

This design turns the repository into a layered benchmark reading system **and the front door of the Radar family**. A reader should be able to enter through evaluation—what the field measures, how the target changed, and what is still missing—then descend into the corresponding method/system radar for Agent Memory, Agentic RAG, or Data Agents.

Scope: root README, benchmark-note contract, benchmark genealogy/library navigation, compactions, editorial standard, validation, bilingual reader surfaces, Radar-family routing, and the recurring workflow that derives public surfaces.

Non-goals: GitHub Pages/frontend work; maximizing benchmark count; replacing official benchmark documentation; treating leaderboard rank as component evidence; forcing every benchmark into an equally detailed note; duplicating machine-readable or maintenance state solely for localization; duplicating domain-radar method surveys inside Benchmark Radar.

## Design principles

1. **Benchmark Radar is the entry point.** It provides the fastest map of what Agent Memory, Agentic RAG, and Data Agents currently consider progress, then routes deeper method/system questions to the relevant sibling radar.
2. **Scan the frontier; expand the reason.** New benchmarks should be easy to scan, while important ones expose a 60–90 second explanation of what newly became measurable.
3. **Genealogy is causal, not chronological decoration.** Historical benchmarks remain only when they explain a durable shift in capability, environment, protocol, validity, or cost.
4. **One record, several views.** README, benchmark notes, research library, and compactions provide different projections of the same canonical benchmark record.
5. **Measurement claims need confounders.** Every important benchmark interpretation names what a score supports and what the harness/protocol prevents us from attributing.
6. **Chinese by default, one research judgment underneath.** Chinese is the default public reading surface; English mirrors the same research interpretation rather than becoming a separately curated fork.
7. **Structure is stable; prose is not templated.** Use a consistent reasoning contract without repetitive AI sentence skeletons.

## Radar family role

The Radar family has three vertical research radars plus one horizontal evaluation entry point:

```text
                         Agent Benchmark Radar
                         entry + evaluation layer
                    /             |              \
                   /              |               \
        Agent Memory Radar   Agentic RAG Radar   Data Agent Radar
        memory systems       information access   end-to-end data work
```

The division of responsibility is deliberate:

- **Agent Benchmark Radar** asks: *What does the field measure? How did the evaluation target evolve? What does a score actually support? What remains poorly measured?*
- **Agent-Memory-Radar** asks: *How should agents write, organize, retrieve, reconstruct, update, forget, and govern memory?*
- **Agentic-RAG-Radar** asks: *How should agents plan information needs, access evidence, control retrieval, materialize context, preserve state, and decide when to stop?*
- **Data-Agent-Radar** asks: *How should agents discover/ground data, plan analytic work, query/code/transform, inspect/verify, recover, and deliver data artifacts?*

Benchmark Radar should therefore **route rather than duplicate**. Each area field map includes one prominent domain-radar continuation link. The sibling radars link back from their evaluation/field-map surfaces to the corresponding Benchmark Radar section or genealogy.

The expected reader flow is:

`What does the field care about? → How is that measured? → Which research line addresses it? → Inspect methods/systems in the domain radar → Return to benchmark genealogy to check whether progress is actually measured.`

## External writing basis

The design follows Google Technical Writing guidance on key points first, audience fit, progressive disclosure, and organizing large information collections into navigable views; Microsoft’s “scanning first, reading second” principle; and NeurIPS checklist/reviewer guidance that claims, scope, assumptions, evidence, reproducibility, and limitations should align.

Third-party plain-writing and research-writing skills are design references only. The repository-local editor and validator are authoritative so the daily workflow does not depend on an external skill being installed.

## Reading architecture

```text
canonical benchmark registry
  ├─ 30 sec: README New & Notable row
  ├─ 60–90 sec: README fold for high-value benchmark changes
  ├─ 5–10 min: benchmark note / protocol audit
  ├─ topic view: Benchmark Library + genealogy
  ├─ domain continuation: Memory / Agentic RAG / Data Agent Radar
  └─ time view: weekly → monthly → yearly evaluation compaction
```

Every reader-facing projection has a Chinese-default and English form, but both derive from the same benchmark identity, protocol facts, comparison judgment, confounder analysis, and genealogy assignment.

## Bilingual reader contract

The repository is bilingual for **reader-facing narrative surfaces**, not for canonical or operational state.

### Default language and file layout

- `README.md` — default **Simplified Chinese** landing page.
- `README.en.md` — complete English counterpart.
- Both pages expose a compact language switch at the top: `中文 | [English](README.en.md)` and `[中文](README.md) | English`.
- Benchmark names, paper titles, dataset names, metric names, model names, protocol/tool names, repository names, and standard acronyms remain in their original form unless a Chinese gloss materially helps comprehension.
- Chinese prose should use established technical terms where natural, but should not translate terminology so aggressively that literature search becomes harder.

### Which surfaces are bilingual

Maintain both languages for public narrative that readers may reasonably traverse from the root README:

- root README;
- Benchmark Library / genealogy navigation;
- high-value benchmark notes / protocol audits;
- weekly, monthly, and yearly research compactions when they are linked as reader-facing synthesis;
- public explanatory pages that define the benchmark taxonomy or how to read the radar.

Do **not** duplicate language variants for:

- `data/benchmarks.json` and other canonical machine-readable records;
- scheduler prompts, validation output, schemas, and maintenance-only docs;
- `runs/README.md`, which is static policy only.

### No public operational run logs

The Daily Agent never commits a file under `runs/daily/` or another public operational path. Private scout, candidate, lane, retry, and validation traces live only in ignored `.radar-private/` state or ephemeral Agent memory. Canonical data, the complete bilingual Timeline, any due digest, and one atomic Git commit are the public provenance.

### Source-of-truth and drift control

Bilingual does not mean two independent editorial pipelines.

For every accepted benchmark, first settle one semantic research record: measurement delta, predecessor, capability/environment/protocol, what the score supports, confounder, coverage gap, genealogy role, and primary evidence. Only after this judgment is stable should the workflow render Chinese and English reader prose.

Chinese is the **default editorial surface**, but neither language may introduce a factual or causal claim absent from the shared semantic judgment. English should be rewritten naturally rather than translated word-for-word; Chinese should likewise avoid calques from English. The two versions must preserve the same:

- importance / evolution role;
- predecessor and implicit critique;
- decisive protocol facts and quantitative evidence;
- attribution boundary;
- strongest confounder;
- open measurement gap;
- links to primary sources;
- sibling-radar routing target for each area.

If one language receives a material interpretation correction, the paired surface must be updated in the same maintenance transaction.

### Translation/editorial quality

Treat localization as technical editing, not literal translation.

Chinese default prose should:

- explain the benchmark purpose before protocol jargon;
- prefer short, direct sentences and natural Chinese information order;
- preserve English search terms where they are the field’s canonical vocabulary;
- avoid unnecessary English-Chinese duplication such as `检索（retrieval）` on every occurrence after the term is established;
- avoid machine-translation syntax, stacked nominal phrases, and generic transitions such as “值得注意的是”“此外”“总的来说” when they add no reasoning value.

English prose follows the same Research Radar Editor standard: concrete language, comparison before praise, explicit attribution limits, and no recurring AI-house-style sentence templates.

Validation should compare semantic invariants rather than expect sentence-level translation equivalence.

## README contract

The root README is the **family landing page**, not only a benchmark archive. Its first screen should make all four repos legible without turning into a promotional directory.

Near the title, expose:

- Chinese/English language switch;
- depth navigation;
- one compact `Research Radars` line linking to Agent Memory, Agentic RAG, and Data Agent Radar.

Use this top-level order in both languages:

```text
New & Notable
What Benchmark Evolution Says About the Field
Field Maps: Memory / RAG / Data Agents
Reading Paths
Benchmark Library / Browse All
What Is Still Poorly Measured
Research Compactions
About / Contributing
```

The Chinese default uses natural Chinese section names rather than literal translations, while preserving one-to-one conceptual sections and stable anchors where practical.

Expose depth navigation near the title:

Chinese default: `30 秒：前沿 · 5 分钟：领域演化 · 15 分钟：阅读路径 · 浏览全部`

English: `30 sec: Frontier · 5 min: Field Evolution · 15 min: Reading Paths · Browse All`

Keep the current core idea: a useful new benchmark is often an implicit critique of what the previous generation failed to measure. Keep the comparison rule that higher leaderboard score is system-level evidence unless model, accessible state, tools, prompts/hints, retries, stopping rule, evaluator, and relevant budgets are sufficiently matched.

### New & Notable

Keep roughly 6–10 recent benchmark changes that materially alter the evaluation object. Include benchmark releases, major protocol/evaluator revisions, contamination/saturation findings, and newly recovered historical foundations when they change current interpretation.

Each row answers:

- what is newly measurable;
- what previous limitation it exposes;
- what field signal follows.

Importance >= 4/5, or a benchmark/protocol change that alters a current genealogy, receives an inline `<details>` explainer. The fold should cover these information points naturally in 3–5 short paragraphs:

- previous benchmark/control it implicitly criticizes;
- capability × environment × protocol delta;
- what a score does and does not support;
- strongest validity/confounder issue;
- why this changes the field map.

Do not repeat a future benchmark note verbatim.

### Field evolution

Keep one compact area-level evolution arrow for Agent Memory, RAG / Agentic Retrieval, and Data Agents. The arrow should tell a causal story: what target became too narrow or easy, and which new coordinate replaced it.

Each area ends with a clear continuation:

- `继续看 Agent Memory 的方法与系统 → Agent-Memory-Radar`
- `继续看 Agentic RAG / Search 的方法与系统 → Agentic-RAG-Radar`
- `继续看 Data Agent 的方法与系统 → Data-Agent-Radar`

English uses the corresponding natural labels. These are semantic continuation links, not repeated promotional banners.

### Area field maps

Do not render the full historical registry as one permanently expanded table. Each area defaults to:

- one-line evolution chain;
- 4–6 defining benchmarks covering precursor/foundation/transition/frontier;
- current frontier signal;
- biggest current measurement gap;
- sibling domain-radar continuation link.

Place the full genealogy in `<details>` or link to the Benchmark Library. This keeps foundations visible without making the first read exhaustive.

### Reading Paths

Use three or four paths maximum, framed as questions such as `How did long-term memory move from recall to action?`, `How did retrieval evaluation become a stateful control problem?`, or `How did data-agent evaluation move from SQL/code to real workspaces?`.

A path may end in a sibling radar when the next useful question is about methods rather than measurement. Do not reproduce a sibling radar’s method reading path inside Benchmark Radar.

## Benchmark Explainer Standard

High-visibility benchmark notes follow this reasoning contract:

1. **Measurement delta** — the smallest change that makes the benchmark worth knowing.
2. **Predecessor / implicit critique** — closest prior benchmark and what was missing, too easy, too static, too synthetic, or too weakly diagnosed.
3. **What it actually measures** — capability, environment, accessible state, task, and target behavior.
4. **Protocol** — tools/interfaces, model/harness assumptions, hints, retries/trials, stopping rule, metrics/judge, executable validation, and relevant cost budgets.
5. **What a score supports** — system-level claim versus any justified component-level attribution.
6. **Strongest confounder / validity risk** — contamination, saturation, judge dependence, environment drift, hidden hints, harness sensitivity, synthetic shortcuts, or lifecycle cost.
7. **What remains unmeasured** — the next missing coordinate made visible by this benchmark.
8. **Genealogy consequence** — precursor/foundation/transition/frontier role and nearest continuation.
9. **Research continuation** — when useful, one link to the relevant sibling radar research line; omit it when the benchmark is only weakly tied to a domain-method question.

Use a note only when it adds decision value. A large registry does not imply a large collection of prose files.

For bilingual notes, keep identical semantic sections and evidence scope in Chinese and English, but allow paragraph order and sentence construction to differ when that improves natural readability.

## Editorial standard

Create a repository-local Research Radar Editor contract shared in spirit with the paper radars.

Preferred prose:

- concrete nouns for capability, environment, protocol, evaluator, and artifacts;
- comparisons before adjectives;
- one research claim per paragraph;
- explicit causal boundaries (`this is a system-level result`, `the protocol does not isolate retrieval policy`);
- numbers only when they change interpretation;
- simple language for benchmark purpose before protocol detail.

Avoid:

- repetitive openers such as `the important thing is not...` or `this matters because...` across every entry;
- generic praise without comparison/evidence;
- describing benchmark scale as novelty when the evaluation object is unchanged;
- marketing language, emoji-heavy decoration, and inflated labels such as `groundbreaking` or `comprehensive` without support;
- treating `frontier` as a prestige label rather than a time-relative analytical role;
- turning sibling-radar links into repeated calls to action that interrupt research reading.

A deterministic editorial linter should warn on repeated sentence skeletons, generic judgments without nearby comparison/evidence, duplicated prose across surfaces, and structural drift. It should not ban words mechanically.

For Chinese, add warnings for repeated empty discourse markers, machine-translated English syntax, excessive parenthetical English, and repeated evaluative templates such as `真正重要的是……` or `关键不在于……而在于……` across many entries.

## Benchmark Library

Time-based digests are not the historical index. Maintain three discovery routes:

- **Browse by Area** — Agent Memory; RAG / Agentic Retrieval; Data Agents. Each area routes to its sibling domain radar for method/system continuation.
- **Browse by Genealogy** — `precursor → foundation → transition → frontier`, with nearest-predecessor relationships and the limitation each successor exposed.
- **Browse by Measurement Coordinate** — capability, environment, protocol, validity/reproducibility, cost, action/decision impact, multimodality, persistent state, and other controlled coordinates.

A compact **Browse by Year** view remains available for chronology and provenance.

Every important historical benchmark must remain reachable through at least one non-temporal route. Weekly/monthly/yearly synthesis explains changes; it does not own discoverability.

Both Chinese and English library entry surfaces must route to the same benchmark set, genealogy relationships, and sibling-radar destinations. Translation must never create separate inclusion/exclusion decisions.

## Layer responsibilities

- `data/benchmarks.json`: canonical benchmark identity, area, evolution role, capability/environment/protocol, measurement strength, coverage gap, confounders, artifacts, verification.
- benchmark notes when present: protocol/evidence audit layer, bilingual for reader-facing notes.
- Benchmark Library/genealogy: historical retrieval and evolution layer, bilingual navigation.
- `digests/*`: temporal synthesis of evaluation-object shifts, bilingual when public-facing.
- `README.md`: default Chinese **Radar-family entry + benchmark judgment/router** layer.
- `README.en.md`: English counterpart.
- sibling domain radars: method/system argument and evidence layers; Benchmark Radar links into them rather than duplicating their coverage.
- `runs/README.md`: static no-public-run policy only; operational provenance stays in ignored `.radar-private/` state or ephemeral Agent memory.

Do not duplicate the same paragraph across layers or maintain separate research judgments by language.

## Maintenance workflow

Move detailed recurring behavior into a repository-owned `docs/DAILY_WORKFLOW.md`. The scheduler should become a thin entry point.

Each transaction follows:

`preflight → recent discovery + bounded historical backfill → independent benchmark judgment → protocol audit → canonical registry update → note/genealogy update when useful → derive Chinese + English reader projections → verify sibling-radar routing → bilingual editorial review → validate semantic parity → atomic commit → notify only if material`

A new benchmark does not automatically become a defining benchmark in the default area view. Default genealogy changes only when the new work shifts a durable evaluation coordinate.

A sibling-radar link should change only when a research continuation becomes materially better; do not rewrite cross-links because a new paper happened to arrive.

Chinese and English public updates for the same semantic change should land atomically in one transaction. Do not publish one language and leave the paired high-visibility surface stale; any blocker remains private in ignored `.radar-private/` state or ephemeral Agent memory.

## Validation

Add deterministic checks for:

- `README.md` exists as the Chinese default and `README.en.md` exists as the English counterpart;
- both expose language-switch links, the same conceptual top-level sections, and the same three sibling-radar destinations;
- both include the same New & Notable benchmark identities, importance values, evolution roles, and primary links;
- material interpretation fields remain semantically aligned across languages;
- README top-level section order and New & Notable bounds;
- fold eligibility and required semantic coverage;
- every README benchmark exists in the canonical registry;
- every default genealogy entry has a valid evolution role and a meaningful predecessor/delta explanation;
- each of the three area maps has exactly one canonical sibling-radar continuation target;
- every high-importance historical benchmark is reachable through the Benchmark Library in both languages;
- no maintenance/scheduler/schema internals leak to public surfaces;
- repeated house-style lead-in warnings and high-similarity paragraph warnings, with Chinese- and English-specific patterns;
- registry/README synchronization, dates, links, role validity, measurement-strength versus coverage-gap separation, and component-attribution discipline continue to pass.

Editorial lint is advisory unless a deterministic public/canonical contract is violated. Semantic bilingual drift or incorrect sibling-radar routing for high-visibility surfaces is a correctness failure, not an editorial warning.

## Migration

1. Rebuild `README.md` as the Chinese-default **Radar-family entry** and progressive-depth benchmark surface while retaining the current useful New & Notable and core comparison rule.
2. Create `README.en.md` from the same semantic judgment, rewritten as natural English rather than literal translation.
3. Add one compact first-screen navigation line to Agent-Memory-Radar, Agentic-RAG-Radar, and Data-Agent-Radar; add one domain continuation link per area field map.
4. Collapse long per-area history into defining benchmarks + current frontier + measurement gap; preserve full genealogy behind disclosure/library navigation in both languages.
5. Add a bilingual Benchmark Library with area, genealogy, measurement-coordinate, and year routes.
6. Add the local Research Radar Editor standard and bilingual editorial linter.
7. Add `docs/DAILY_WORKFLOW.md` and move stable recurring behavior out of the scheduler prompt, including atomic Chinese/English projection updates and sibling-routing validation.
8. Add/upgrade benchmark notes selectively for frontier works and foundations whose protocol/genealogy is otherwise easy to misunderstand; high-value public notes receive both Chinese and English versions.
9. Migrate public compactions to bilingual form as they are touched or regenerated; keep operational traces only in ignored `.radar-private/` state or ephemeral Agent memory.
10. Preserve old benchmarks in canonical data; do not delete history merely to shorten README.

## Success criteria

A reader should be able to:

- open Agent Benchmark Radar as the natural entry point for the entire Radar family;
- understand within one screen that the family covers Agent Memory, Agentic RAG, and Data Agents, and move to the correct sibling radar without guessing repository names;
- land on a complete Chinese default experience and switch to English without losing information depth;
- identify the newest meaningful evaluation shifts within 30 seconds;
- understand why a high-value new benchmark exists in 60–90 seconds without leaving README;
- trace a current frontier benchmark back to the predecessor limitation it addresses;
- continue from an evaluation question into the corresponding method/system research line without duplicated surveys;
- find historical benchmarks by area, genealogy, or measurement coordinate rather than publication week;
- tell what a score supports and what the protocol confounds;
- read repeated benchmark explanations in either language without a templated AI house style.

The maintainer should be able to change reader/editorial contracts in repository files while the recurring automation prompt stays short and stable, and should never need to curate separate Chinese and English benchmark judgments.
