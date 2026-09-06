# Daily Benchmark Adapter


This file adapts [Radar Agent Protocol v2](RADAR_AGENT_PROTOCOL.md) to Agent Benchmark Radar. The shared protocol governs roles, private candidate states, timestamps, atomic publication, bilingual projection, and retries. This adapter governs what counts as a reusable evaluation object and where Benchmark Radar writes it.

## Repository role

Agent Benchmark Radar is the Research Radar family's default entry and horizontal evaluation layer. It explains how measurement targets change across Agent Memory, Agentic RAG, and Data Agents, then routes readers to each domain repository's `#field-map`. It does not duplicate their method and system surveys.

The public README is intentionally **timeline-first and table-first**: lead with the recent release chronology and complete per-area tables; keep interpretation in linked reading guides without requiring card-by-card opening. Agent-maintenance provenance and deep audit metadata support that surface; they do not dictate its visual form.

## Source lanes

Freeze and report each lane separately:

- primary paper sources and proceedings for benchmark, dataset, evaluation, diagnostic, challenge, or evaluator releases;
- official benchmark repositories, datasets, executable environments, leaderboards, and protocol/version releases;
- contamination, saturation, label-correction, reproducibility, and independent validity evidence;
- bounded historical backfill for predecessors repeatedly cited by accepted frontier work or missing from a genealogy;
- family-domain signals from Agent Memory, Agentic RAG, and Data Agent Radars that introduce a reusable evaluation object.

Search naming drift around long-term/procedural/multimodal memory; RAG, agentic retrieval, search, and deep research; data, analytics, database, and data-science agents. Prefer primary sources. Vendor or product claims may identify a lead or protocol but cannot alone support benchmark metadata or importance.

## Measurement-object acceptance test

A work is in scope only when its benchmark/evaluation contribution is reusable by other systems: task, environment, dataset, protocol, challenge, diagnostic, evaluator, or validity correction. A paper does not qualify merely because it evaluates a Memory, RAG, or Data Agent method.

Before acceptance answer, from full text or equivalent primary protocol evidence:

1. What controlled object and success contract become measurable?
2. What is the closest predecessor, and what changes in capability × environment × protocol?
3. What does the decisive result support under the stated controls?
4. What is the strongest protocol confounder or alternative explanation?
5. What important coordinate remains unmeasured?
6. Is it a verifiable, reusable, in-scope evaluation object, and what importance/role should it receive separately?

The minimal evaluation loop is `task/environment → harness → trajectory → evaluator`. Acceptance requires that the claimed result can be located within that loop and that the evaluation object, not merely the evaluated model, is the contribution.

The orchestrator may delegate discovery, identity resolution, full-text reading, protocol audit, genealogy, and skeptical review, but it remains the only writer. Discovery optimizes recall; the benchmark judge decides scope and reusability; the editor decides explanation depth after acceptance. Do not defer an in-scope recent benchmark merely because a nearby record measures a similar coordinate.

## Protocol and confounder audit

The Full-Text Reader and Skeptical Reviewer record model/backbone, accessible state/context, tools and interface, harness/controller, prompts and hints, trials/retries, stopping rule, evaluator/judge, executable validation, contamination controls, latency/token/tool budgets, and environment version/drift.

If any load-bearing condition differs, a leaderboard gap is system-level evidence. Do not attribute it to memory, retrieval, planning, routing, or data tooling unless the relevant comparison holds those conditions sufficiently constant. Negative results and harness sensitivity are first-class validity evidence.

## Canonical locations and update order

1. Update `data/benchmarks.json` first, preserving canonical identity, aliases/version lineage, source release precision, area, role, capabilities, environment, protocol, scale, measurement strength, coverage gap, confounders, artifacts, citation metadata, verification time, and v2 provenance. Citation counts use Semantic Scholar and may be refreshed mechanically without changing editorial role/importance.
2. Add or update `benchmarks/<id>.md` and `benchmarks/<id>.en.md` when a row is insufficient for controls, decisive evidence, caveats, or genealogy.
3. Update `library/README.md` and `library/README.en.md` so every accepted identity remains in the complete release chronology and exactly one area table; then update genealogy and measurement-coordinate routes when they change.
4. Derive the **public timeline-first README pair** from canonical state: regenerate the rolling six-month timeline and all three complete area tables. Update linked editorial guides separately when their evidence changes.
5. Update the gated Field Map only when durable evaluation coordinates or defining chains change. Do not add per-item deep-read or rolling 7-day/30-day synthesis sections to the public README; audit detail belongs in canonical records, benchmark notes, and digests.
6. Write an immutable closed-period digest when the shared protocol's boundary gate fires.
7. Publish canonical data, both README languages, due digest, and gated map together in one atomic Git commit; never create a public operational or daily-run file.

Legacy records keep honest `released` precision. New v2 records use strict UTC `published_at`, `first_seen_at`, and `radar_published_at` ordered by event time with `time_provenance=native_v2` and a valid map delta. A later merge, verification date, or scheduler run is not evidence of the original Radar acceptance timestamp. These provenance fields do not change the source release date shown to readers.

## Notes and genealogy

A deep note adds decision value only when it records the predecessor/implicit critique, evaluated object, decisive result, score ceiling, strongest confounder, remaining gap, and genealogy consequence. Preserve quantitative facts only when they change interpretation and cite the primary source.

Genealogy expresses changes in the evaluation coordinate system, not prestige. Use `precursor`, `foundation`, `transition`, and `frontier` as defined in `SCHEMA.md`. A historical backfill may change a chain without being framed as newly published research. Never remove a durable foundation merely because it is outside the recent-release window.

## Evaluation-specific `map_delta`

Assign every accepted event one status from `SCHEMA.md`:

- `none`: accepted evidence does not change the evaluation map;
- `early_signal`: one credible work makes a coordinate worth watching;
- `reinforces`: independent accepted evidence supports the same capability/environment/protocol direction;
- `revises`: evidence weakens or materially qualifies an existing measurement claim;
- `splits`: one node must separate because protocols measure causally different objects;
- `retires`: a coordinate is no longer defensible because of saturation, invalidity, or replacement evidence.

For `reinforces`, name at least two independent accepted identities. For `revises`, `splits`, or `retires`, record the previous claim, new evidence, confounder audit, and smallest reversible map edit. Shared terminology or several releases in one month is not sufficient.

## Reader projection

[README-first publication](README_PUBLICATION.md) is the active reader contract.
The website is retired. The root README contains the rolling six-month timeline,
month jumps, and every accepted benchmark in three complete area tables, newest
first. One concise measurement description accompanies each entry. Names link to
the authored language-matched note; original papers, code and datasets are directly
accessible. Citation counts remain context, not a ranking or stage assignment.

Recipes, source-record indexes and editorial maps belong in linked Markdown guides
after the complete tables. No score leaderboard, trend claim, or maintenance report
may displace the main lists. Preserve compatibility anchors at meaningful sections.
The date selector uses typed public/publication/data events with evidence, then
explicitly marked legacy dates. Never substitute a scan, verification or commit
time for the benchmark date. Preserve exact day/month precision.

## Publication validation

Run from the repository root:

```bash
node scripts/render-readme.mjs
node scripts/render-readme.mjs --check
python -m unittest discover -s tests -v
python scripts/validate_reading.py
python scripts/validate_detail_pages.py
```

The renderer does not require an Astro install or build. Commit both languages and
the generated recipe/source indexes atomically with their inputs. Tests check exact
membership, chronology, summaries, date types, direct sources and citation values;
Library validation retains the complete canonical identity/area/source checks.
An editorial rewrite must not advance factual verification or discovery timestamps.

## No public operational run logs

Do not write under `runs/daily/` or any other public operational path. `runs/README.md` is static policy only. Scout, candidate, lane, retry, and validation traces stay in ignored `.radar-private/runs/<run_id>.json` or ephemeral Agent memory. Canonical data, the bilingual public projection, a due digest, and one atomic Git commit are the public provenance. If nothing material changes, validate and exit without a content commit or notification.
