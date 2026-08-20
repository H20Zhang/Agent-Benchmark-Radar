# Daily Benchmark Adapter

This file adapts [Radar Agent Protocol v2](RADAR_AGENT_PROTOCOL.md) to Agent Benchmark Radar. The shared protocol governs roles, private candidate states, timestamps, atomic publication, bilingual projection, period boundaries, and retries. This adapter governs what counts as a reusable evaluation object and where Benchmark Radar writes it.

## Repository role

Agent Benchmark Radar is the Research Radar family's default entry and horizontal evaluation layer. It explains how measurement targets change across Agent Memory, Agentic RAG, and Data Agents, then routes readers to each domain repository's `#field-map`. It does not duplicate their method and system surveys.

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

1. Update `data/benchmarks.json` first, preserving canonical identity, aliases/version lineage, dates, area, role, capabilities, environment, protocol, scale, measurement strength, coverage gap, confounders, artifacts, and verification time.
2. Add or update `benchmarks/<id>.md` and `benchmarks/<id>.en.md` when the Timeline fold is insufficient for controls, decisive evidence, caveats, or genealogy.
3. Update `library/README.md` and `library/README.en.md` so every accepted identity remains in the complete release chronology and exactly one area table; then update genealogy and measurement-coordinate routes when they change.
4. Derive `README.md` and `README.en.md` Timeline, rolling periods, and Field Map from accepted canonical state.
5. Write an immutable closed-period digest when the shared protocol's boundary gate fires.
6. Publish canonical data, Timeline, any due digest, and gated map together in one atomic Git commit; never create a public operational or daily-run file.

Legacy records keep honest `released` precision. Untouched legacy records remain field-absent compatible and belong to the complete Library, not the acceptance-time Timeline. The fixed Timeline compatibility migration uses `published_at=released`, null discovery/Radar times, `time_provenance=legacy_unknown`, and `map_delta=early_signal`; it never infers an unknown day. New v2 records use strict UTC `published_at`, `first_seen_at`, and `radar_published_at` ordered by event time with `time_provenance=native_v2` and a valid map delta. A later merge, verification date, or scheduler run is not evidence of the original Radar acceptance timestamp.

## Notes and genealogy

A deep note adds decision value only when it records the predecessor/implicit critique, evaluated object, decisive result, score ceiling, strongest confounder, remaining gap, and genealogy consequence. Preserve quantitative facts only when they change interpretation and cite the primary source.

Genealogy expresses changes in the evaluation coordinate system, not prestige. Use `precursor`, `foundation`, `transition`, and `frontier` as defined in `SCHEMA.md`. A historical backfill may change a chain without being framed as newly published research. Never remove a durable foundation merely because it is outside Timeline.

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

The public order is `Latest Timeline → 7-day / 30-day synthesis → Field Map → Reading Paths → Library`. Preserve the paired top attention routes `30 秒 / 3 分钟 / 5 分钟 / 15 分钟 / 浏览全部` and `30 sec / 3 min / 5 min / 15 min / Browse all`; those budgets describe navigation depth, not paper importance. Timeline contains every native-v2 record whose `radar_published_at` is in the current 30-day window and no later than the exact shared public synthesis cutoff, sorted by full timestamp, followed by the fixed explicit-legacy compatibility projection; it has no fixed item cap. Each Timeline item keeps a scannable summary and same-level `<details>` expansion with Question, Evidence, Caveat, Map, and Links. The rolling periods synthesize changes in the evaluation object from in-window native records accepted no later than that same cutoff rather than counting releases. Legacy records may provide context but never Benchmark period support; the shared protocol's separately labeled legacy publication-date adapter is not active on this native Radar-acceptance surface.

Each visible direction list item owns exactly one `timefirst:direction` metadata comment and exactly one visible state, supports, confidence, timing-basis, exact UTC synthesis, implication, and prior-map field. A block includes natural continuation lines and attached prose until the next visible direction or period boundary; comments and URL destinations cannot supply visible claims. Chinese and English metadata must pair exactly. Every native-v2 record cited as support under direction key `K` must include that exact stable token in its non-empty unique `direction_keys` list. `reinforced` needs two distinct in-window native supports bound to the block's exact key plus visible prior Field Map evidence; `revised`, `splits`, and `retires` need bound canonical support plus prior Field Map evidence; `no_material_change` needs zero support and `prior=none`. Fewer than two native supports cannot carry a trend or durable-result claim. The three Benchmark areas route directly to the sibling repository's `#field-map` anchor. `What Is Still Poorly Measured` remains first-class.

Chinese is the default surface and English is its full counterpart. Identity, dates/order, decisive evidence, caveat, map status, period windows, and links are one judgment projected twice. Chinese prose keeps Chinese verbs, connectives, and descriptive phrases while retaining canonical English names and search terms where useful. Complete Library tables lead with direct links and a consistent row contract, without reading-time labels or repetitive manifesto prose.

## Publication validation

Run from the repository root:

```bash
python -m unittest discover -s tests -v
python scripts/validate_reading.py
```

Both commands must succeed without warnings or errors before publication. Also inspect the diff for canonical/README drift, predecessor logic, unpaired links, public candidate state, fixed Timeline caps, fabricated time precision, and component claims that outrun matched controls.

Validation must also prove that both Library languages contain the exact canonical release chronology and each record exactly once in its canonical area table, with visible canonical title, release precision, and primary link. A hidden identity comment cannot substitute for a visible row.

## No public operational run logs

Do not write under `runs/daily/` or any other public operational path. `runs/README.md` is static policy only. Scout, candidate, lane, retry, and validation traces stay in ignored `.radar-private/runs/<run_id>.json` or ephemeral Agent memory. Canonical data, the complete bilingual Timeline, a due digest, and one atomic Git commit are the public provenance. If nothing material changes, validate and exit without a content commit or notification.
