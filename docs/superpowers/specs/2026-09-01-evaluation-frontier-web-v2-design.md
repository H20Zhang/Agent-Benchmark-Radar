# Agent Benchmark Radar: Evaluation Frontier Web v2 Design

**Date:** 2026-09-01

**Status:** Design approved in conversation; pending written-spec review

**Project site:** `https://h20zhang.github.io/Agent-Benchmark-Radar/`

**Supersedes:** Product and information-architecture decisions in [`2026-09-01-benchmark-radar-web-design.md`](./2026-09-01-benchmark-radar-web-design.md). The Astro, static-generation, bilingual, accessibility, SEO, and GitHub Pages decisions from v1 remain in force.

## 1. Product Thesis

Agent Benchmark Radar maps the evaluation frontier:

> what agents can be measured on today, what the next useful measurement coordinates are, and where research is moving.

A benchmark does more than provide a dataset. It makes a capability observable, gives researchers a shared optimization target, and defines what evidence can support a research claim. Result trajectories then show how quickly the community is improving against that target. The boundary of the benchmark reveals the next useful evaluation coordinate.

The product therefore follows one research loop:

`Benchmark → Results → Headroom → Opportunity → Frontier shift`

The site is an interactive research-decision system. The README is its concise, durable GitHub snapshot.

## 2. Problem Statement

The v1 site successfully turns the registry into an indexable, bilingual explorer. Its primary interaction remains a filterable catalog, while the README carries much of the project's research judgment: evaluation recipes, benchmark genealogy, recent shifts, timelines, reading paths, and next evaluation directions.

Three limitations now constrain user value:

1. Discovery emphasizes metadata over the decision “is this benchmark useful for my claim today?”
2. Benchmark pages explain the artifact but do not show the methods, models, result history, or remaining performance space.
3. Raw capability, environment, and protocol tags behave like a keyword index rather than a stable comparison taxonomy.

V2 connects the catalog to the evaluation and research workflows. It preserves complete benchmark coverage while adding layered editorial depth, living results for the active set, explicit evaluation opportunities, and visual frontier tracking.

## 3. Scope and Delivery Boundary

V2 covers five connected capabilities:

- discover current, verified benchmark repositories and artifacts;
- assemble a benchmark suite for a research claim;
- inspect comparable methods, models, scores, budgets, and progress over time;
- identify evidence-backed next evaluation coordinates;
- track how benchmark design and results move the research frontier.

V2 keeps the following boundaries:

- The project curates benchmark evidence; it does not run submissions or host a universal evaluation harness.
- Raw scores remain local to a comparable track. Cross-benchmark research views use age, headroom, activity, and progress dimensions rather than a universal score ranking.
- Result ingestion prioritizes public, attributable sources and curator verification. Community submission workflows can follow after the data contract and review process are stable.
- The Benchmark Radar routes method surveys to the related domain radars. It explains evaluation consequences without duplicating full method landscapes.

## 4. Users and Core Decisions

| User intent | Question | Product response |
|---|---|---|
| Pick | What can I use today? | Latest verified benchmarks, Repo/data readiness, benchmark maturity, supported claims, and comparison tools |
| Evaluate | Which benchmark combination supports my claim? | Claim-first recipes with Core, Complement, comparison controls, and next validation |
| Build | What evaluation is worth creating next? | Evidence-backed opportunities derived from current coverage and measurement boundaries |
| Track | What changed, and does it alter my research decision? | Frontier shifts, result trajectories, genealogy, and time-aware synthesis |

The user-facing navigation compresses these decisions into three primary destinations: **Benchmarks**, **Opportunities**, and **Frontier**. Evaluation recipes and comparison are action tools within Benchmarks.

## 5. Information Architecture

| Route family | Role |
|---|---|
| `/{lang}/` | Intent-led home: pick a benchmark, design an evaluation, or track the frontier |
| `/{lang}/benchmarks/` | Latest releases, full library, stable research filters, active result signals |
| `/{lang}/benchmarks/{id}/` | Benchmark research dossier with evaluation contract, results, interpretation, genealogy, and deep read |
| `/{lang}/evaluate/` | Claim-first suite builder using the canonical evaluation recipes |
| `/{lang}/compare/` | Side-by-side comparison of two or three benchmarks under explicit dimensions |
| `/{lang}/opportunities/` | Evaluation Opportunity Map and curated opportunity index |
| `/{lang}/opportunities/{id}/` | Evidence, current coverage, proposed evaluation coordinate, feasibility, and confidence |
| `/{lang}/frontier/` | Recent shifts, six-month timeline, result activity, and digest archive |
| `/{lang}/areas/{area}/` | Area thesis, interactive genealogy, recipes, opportunities, recent shifts, and complete benchmark subset |
| `/{lang}/methodology/` | Inclusion, comparability, result verification, opportunity inference, citation, and update policies |

The root language redirect, sitemap, canonical links, and bilingual route symmetry remain unchanged from v1.

## 6. Homepage

The home page starts with the product thesis and three task entrances:

1. **Pick a Benchmark** — recent verified releases with code and data readiness.
2. **Design an Evaluation** — claim-first suite creation and evaluation opportunities.
3. **Track the Frontier** — the most consequential recent benchmark and result shifts.

Below the entrances, the page presents a compact “current state” layer:

- recent benchmark releases that introduce a meaningful measurement coordinate;
- active benchmarks with notable verified result movement;
- current evaluation opportunities with the strongest evidence;
- direct continuation into the three domain Radar repositories.

The full filter interface lives on `/benchmarks/`. The home page keeps a global search box and high-value entry points without placing a large control panel ahead of the research story.

## 7. Benchmark Discovery and Filtering

### 7.1 Stable research taxonomy

The explorer uses a two-level taxonomy:

- low-cardinality research dimensions drive visible filters;
- the existing normalized tags remain available through one searchable “all tags” control.

The stable dimensions cover capability, environment, evaluation objective, evaluator type, lifecycle stage, artifact readiness, release period, and result status. Area-specific capability vocabularies preserve domain meaning; for example, Memory can expose recall, update, lifecycle, personalization, action, safety, and multimodal evidence.

Raw tags retain retrieval value without rendering hundreds of single-item options in the initial DOM.

### 7.2 Interaction contract

Desktop uses a compact top bar for search, area, release period, and sort. A “Refine N” control opens a side drawer for stable research dimensions and result signals. Mobile uses a sticky filter/sort action and a full-screen sheet. Selected filters remain visible as removable chips on every viewport.

Within one facet, selected values use OR semantics. Across facets, selections use AND semantics. Query parameters serialize deterministically and preserve multiple values. Existing v1 parameters continue to resolve through a compatibility mapping.

### 7.3 Result-aware filters

Result filters include:

- metric family and comparable track;
- best reported result range when the selected metric defines a compatible numeric scale;
- remaining headroom when a credible reference target exists;
- recent improvement and result activity;
- benchmark age and last result verification date.

A raw best score never creates a global cross-metric ranking. The explorer first fixes a compatible metric family and track. Research-opportunity views prioritize remaining headroom, progress, age, activity, and evaluation importance as separate dimensions.

## 8. Benchmark Detail as a Research Dossier

Every benchmark page provides a useful selection and interpretation layer. Key benchmarks additionally receive full protocol, result, and genealogy analysis.

### 8.1 Selection summary

The first screen answers:

- what the benchmark makes measurable;
- which research claims its score can support;
- where it belongs in an evaluation suite;
- its release, verification, paper, code, data, and project status;
- the conditions that make comparisons fair.

The page presents positive, actionable labels such as **Measurement strength**, **Suite completion**, **Fair comparison conditions**, and **Next validation**.

### 8.2 Evaluation contract

The contract describes capability, environment, accessible state, task, expected output or action, protocol, scale, metrics, verifier or judge, retry/stopping behavior, and relevant resource budget. A reader can determine whether two reported results share the same comparison conditions.

### 8.3 Results

Benchmarks with verified results expose:

- current best result and original-paper reference result;
- a comparable leaderboard of methods and models;
- score-over-time history;
- metric, split, and track selection;
- available quality, cost, latency, token, step, and tool-call context;
- result sources and verification dates.

Quality and efficiency remain parallel dimensions. The interface does not collapse them into a universal efficiency score.

### 8.4 Interpretation and landscape position

The page explains what the score supports at system level, which comparison controls carry the conclusion, and which next evaluation coordinate follows. It links the nearest predecessor, continuation, same-branch benchmarks, recipe membership, complementary benchmarks, and related opportunities.

Existing bilingual benchmark notes render as the deep-read layer. All 125 pages use structured facts; editorial depth grows first for recipe Core benchmarks, historical anchors, branch turning points, and active frontier benchmarks.

## 9. Result Tracking

### 9.1 Coverage policy

Result maintenance follows a hybrid policy:

- benchmarks released within the rolling six-month window receive live result tracking;
- older benchmarks remain live when an official leaderboard or recent comparable result demonstrates continuing activity;
- other historical benchmarks preserve the original-paper snapshot and the latest explicitly verified snapshot available to the project.

Public status labels are **Live tracking**, **Paper snapshot**, and **Verified snapshot**, each accompanied by an `as of` date.

### 9.2 Source priority

Result evidence uses this order:

1. official benchmark leaderboard or repository;
2. benchmark paper and supplement;
3. method paper and official method repository;
4. reputable aggregators as discovery leads that route back to a primary source.

Every public value links to its source. A result becomes verified only after its track, metric, split, protocol, model, and score are sufficiently identified for interpretation.

### 9.3 Comparability unit

The smallest ranking unit is a benchmark result track, defined by:

`benchmark × task/subset × split × protocol version × metric × direction`

Meaningful protocol variants, such as tool budget, accessible state, hints, retries, judge version, or model restrictions, create separate tracks or explicit configuration columns. The site does not merge values that carry materially different score semantics.

### 9.4 Headroom and progress

Headroom appears only when the metric has a bounded scale and a credible target such as a benchmark-defined ceiling, verified human reference, or explicit task target. The record stores the target type and source. When no target is defensible, the site reports the current best and progress history without fabricating a percentage of completion.

Progress is represented through separate observable values:

- benchmark age;
- time since latest verified result;
- improvement over a fixed recent window when comparable observations exist;
- number of comparable methods and recent result events;
- remaining headroom when defined.

V2 does not publish a composite “frontier score.” Keeping the dimensions visible preserves the distinction between a hard problem, an underexplored problem, a saturated task, and a weakly discriminating benchmark.

## 10. Benchmark Progress Map

The site introduces a result-aware frontier visualization:

- horizontal axis: time since benchmark release;
- vertical axis: normalized remaining headroom where defined;
- color: recent comparable improvement;
- point size: comparable result activity.

The visual supports four interpretations without turning them into automatic verdicts:

| Pattern | Research reading |
|---|---|
| Recent release, substantial headroom | Emerging optimization target |
| Recent release, limited headroom | Rapid maturation; inspect task discrimination and reference target |
| Established benchmark, limited headroom | Mature evaluation target |
| Established benchmark, substantial headroom | Persistent challenge or limited adoption; use activity and importance evidence to distinguish them |

Points with undefined headroom appear in a separate current-best/activity view rather than receiving an invented position.

## 11. Evaluation Recipes and Comparison

The suite builder starts from a research claim. Each recipe returns:

- Core benchmark;
- complementary coverage;
- supported claim boundary;
- fair comparison controls;
- next validation;
- relevant result tracks when available.

Users can share the suite URL and export a concise Markdown evaluation plan. The export cites benchmark sources and carries the selected claim and comparison conditions.

Comparison accepts two or three benchmarks. It aligns measurement target, environment, protocol, scale, metrics, artifacts, result status, score interpretation, suite role, and next validation. Result tables remain separate when tracks are not directly comparable.

## 12. Evaluation Opportunities

An opportunity is a curated research object, not an empty taxonomy cell. It must connect an important capability to current benchmark evidence and an executable next measurement coordinate.

Each opportunity contains:

- research claim and why the measurement matters;
- current benchmark coverage and supporting evidence;
- next measurement coordinate across capability, environment, protocol, lifecycle, or validity;
- candidate task, artifact, verifier, or comparison design;
- related benchmarks, result signals, confidence, curator, and verification date.

Publication requires three gates:

1. the capability or deployment property can change a meaningful research or system decision;
2. current benchmarks provide limited evidence for the claim under review;
3. a credible task, protocol, verifier, or artifact can make progress observable.

The Opportunity Map displays capability against environment for one selected protocol/evaluation objective at a time. Cell state distinguishes established coverage, active expansion, and curated next coordinates. The interface never interprets an unpopulated cell as an opportunity without editorial evidence.

## 13. Frontier Tracking and Area Pages

The Frontier page combines:

- concise 30-day shifts with explicit “compared with what” interpretation;
- a six-month release and result timeline;
- movement in benchmark design, result headroom, and opportunity status;
- bilingual weekly and monthly digests.

Area pages become complete research narratives:

`area thesis → interactive genealogy → current results → evaluation recipes → opportunities → recent shifts → complete benchmark library`

The genealogy uses custom SVG and HTML rather than Mermaid on the website. It supports stage and branch focus, hover summaries, keyboard selection, and links into benchmark dossiers. README keeps accessible Mermaid maps because GitHub renders them reliably.

## 14. Canonical Content Architecture

Structured sources become the shared research model for both public surfaces:

| Source | Responsibility |
|---|---|
| `data/benchmarks.json` | Stable identity, release, factual metadata, artifacts, citations, and current normalized tags |
| `data/editorial/benchmarks/{id}.json` | Bilingual selection judgment, evaluation contract, score support, suite completion, comparison controls |
| `data/results/{id}.json` | Result tracks, entries, protocol context, efficiency context, sources, and verification |
| `data/taxonomy.json` | Stable research dimensions and mapping from raw normalized tags |
| `data/recipes.json` | Claim-first benchmark suites |
| `data/genealogy.json` | Branches, predecessors, continuations, and relation reasons |
| `data/opportunities.json` | Evidence-backed next evaluation coordinates |
| `data/frontier_shifts.json` | Time-bounded benchmark and result changes with editorial interpretation |
| `benchmarks/*.md` and `*.en.md` | Long-form bilingual deep reads |
| `digests/*` | Weekly and monthly synthesis |

README sections and website pages are projections of these sources. Generated README regions use stable markers and repository validation. Editorial prose outside generated regions remains intentionally concise.

The build never relies on scraping evolving README prose for benchmark judgment. Chinese and English content share identifiers and validation contracts.

## 15. Result Data Contract

Each result file contains benchmark-level tracking metadata and one or more tracks. A track records:

- stable `track_id`, localized display name, task/subset, split, protocol version, and source;
- metric identifier, metric family, unit, direction, numeric range, and optional reference target with provenance;
- entries with method, model, score, result date, source URL, source type, and verification state;
- protocol context including accessible state, tools, harness or prompt version, retries, stopping rule, and judge version where relevant;
- efficiency context including cost, latency, token use, steps, and tool calls when reported.

Build validation enforces unique identities, valid metric direction, numeric range consistency, source presence, deterministic ordering, and explicit separation of materially different protocols. Conflicting verified values fail validation until the source or track distinction resolves the conflict.

## 16. Public Language Contract

Reader-facing prose uses direct, constructive labels:

| Internal analytical concept | Public label |
|---|---|
| coverage gap | Suite completion / Next validation |
| confounder | Fair comparison condition |
| missing dimension | Next measurement coordinate |
| stale result | Verified snapshot as of `{date}` |
| unavailable efficiency fields | Source reports score dimensions shown |

Positive wording preserves causal boundaries. It describes what current evidence supports and what additional validation would strengthen the claim. It does not convert uncertainty into promotional certainty.

## 17. Visual and Interaction System

V2 retains the editorial research-instrument aesthetic and adds three precise visualization types:

- genealogy maps for how measurement targets evolved;
- score timelines for how methods improved within one result track;
- progress and opportunity maps for age, headroom, activity, and measurement coverage.

Every chart includes a textual summary, accessible labels, keyboard navigation, source context, and a tabular alternative. Tooltips supplement visible axes and legends rather than carrying essential information alone. Mobile layouts use staged cards or scrollable plots with preserved labels instead of shrinking desktop diagrams.

Astro continues to pre-render all research content. Client scripts provide filtering, comparison state, chart interaction, and shareable URLs. Core facts, current-best values, and editorial interpretation remain available without client execution.

## 18. SEO and Discovery

Every benchmark page gains unique, indexable content around measurement target, supported claim, result state, genealogy, and next validation. Opportunity pages target concrete evaluation questions rather than generic “future work” phrases. Frontier pages retain dated change history so search engines and readers can distinguish current synthesis from permanent benchmark facts.

Canonical, `hreflang`, sitemap, Open Graph, Twitter, and JSON-LD behavior from v1 continues. Sitemap `lastmod` reflects material content or result verification changes. Benchmark pages use `CreativeWork` or `Dataset` according to the artifact; collection and leaderboard sections use semantic HTML and `ItemList` only when the listed entities and order are explicit.

Faceted URLs remain non-canonical views. Stable area, benchmark, opportunity, methodology, and dated frontier pages are the primary indexable surfaces.

## 19. Degraded States and Error Handling

The public interface handles incomplete evidence explicitly:

- a benchmark without a comparable result track shows its paper and artifact context without an empty leaderboard;
- a live benchmark with no later verified result presents the original-paper snapshot and its verification date;
- a metric without a credible reference target omits headroom and remains available in current-best/activity views;
- results under different protocols render as separate tracks;
- an opportunity awaiting sufficient evidence stays in editorial review and remains outside the public opportunity index.

At build time, invalid IDs, broken references, bilingual drift, missing result sources, track collisions, and unresolved value conflicts stop publication. External link availability remains a verification signal with a timestamp rather than a permanent build dependency.

## 20. Maintenance Workflow

The research workflow separates discovery, verification, and publication:

1. Detect benchmark releases, repository changes, official leaderboard updates, and new method results.
2. Resolve the benchmark identity and comparable result track.
3. Extract factual fields and record primary sources.
4. Add or revise editorial judgment: supported claim, comparison controls, next validation, opportunity, and frontier consequence.
5. Validate bilingual semantics, schemas, links, generated README regions, and Astro output before publication.

Automation can collect candidates and draft structured records. Curator verification remains required for track comparability, headroom targets, opportunity publication, and causal interpretation.

## 21. Delivery Sequence

Implementation proceeds as four dependency-ordered workstreams:

1. **Research model foundation** — schemas, typed loaders, taxonomy, recipe/genealogy migration, result contracts, validators, and generated README regions.
2. **Decision surfaces** — intent-led home, streamlined explorer, benchmark dossiers, area narratives, compare, and suite builder using existing content.
3. **Opportunity and frontier surfaces** — opportunity records, custom genealogy, Opportunity Map, Frontier page, and digest inheritance.
4. **Living results** — active-set result ingestion, leaderboards, score timelines, result filters, progress map, and maintenance checks.

Each workstream receives its own implementation plan and review checkpoint. It leaves the site deployable and preserves existing URLs. Result UI ships with verified data; the interface does not publish invented examples or unverified rankings.

## 22. Validation and Acceptance

The release is accepted when:

- README and website consume the shared structured recipes, genealogy, opportunities, and frontier shifts without duplicated manual tables;
- all 125 benchmark pages expose the selection summary, evaluation contract fields available in canonical data, fair comparison conditions, artifacts, and related research navigation;
- existing bilingual deep reads appear on their benchmark pages with semantic parity;
- the explorer uses stable low-cardinality facets, searchable raw tags, persistent multi-select URLs, visible active chips, and responsive filter surfaces;
- suite URLs and comparison URLs restore deterministically;
- every live-tracked benchmark has a source-backed paper result track and publishes subsequent results only when comparability is verified;
- score tables, timelines, headroom, and result filters respect track boundaries and target provenance;
- opportunity publication passes importance, evidence, and feasibility gates;
- genealogy, progress, and opportunity visualizations provide keyboard, text, and tabular alternatives;
- all bilingual, schema, registry, link, unit, Astro build, sitemap, metadata, accessibility, and existing repository tests pass.

## 23. Principal Risks and Controls

### Benchmark availability can distort research importance

The site keeps next measurement coordinates and important poorly measured properties visible beside mature benchmark coverage. Editorial importance is independent of benchmark count.

### Leaderboard values can create false comparability

Track identity, protocol context, budget dimensions, and source provenance gate every ranking. Quality and efficiency remain parallel, and cross-benchmark views use interpretable dimensions.

### Result freshness can exceed curator capacity

Live tracking follows the rolling active set; historical benchmarks use verified snapshots. Candidate automation reduces discovery effort while public verification remains bounded.

### Generated surfaces can flatten research judgment

Structured data carries identifiers, evidence, and shared semantics. Human-authored deep reads and frontier interpretations remain first-class sources, while generators handle repeatable presentation and validation.
