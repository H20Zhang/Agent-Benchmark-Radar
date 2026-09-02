# Benchmark Detail Page Contract

This contract is additive to `docs/RADAR_AGENT_PROTOCOL.md` and `docs/DAILY_WORKFLOW.md`. It governs the GitHub Pages route `/{lang}/benchmarks/{id}/` and prevents accepted benchmark records from degrading into thin, generic landing pages.

## Reader goal

A benchmark detail page is a research decision surface, not a metadata card. A reader should be able to answer, without reopening the main paper first:

1. What controlled object does this benchmark measure?
2. Compared with the closest predecessor or prior evaluation object, what measurement coordinate changed?
3. What does a score under this protocol support, and what does it not identify causally?
4. Which model, harness, tool, budget, evaluator, or environment conditions must be aligned for a fair comparison?
5. What is the strongest verified result or evidence currently recorded?
6. What important coordinate remains unmeasured?
7. Where does this benchmark sit in the area genealogy, and what should be evaluated next?

The page should help a researcher decide whether the benchmark is useful for a claim and where the benchmark itself leaves research headroom.

## Baseline content invariant for every canonical record

Every canonical benchmark must provide enough structured state to render a substantive page even when no hand-written deep note exists. Required canonical fields are:

- `summary` and `measurement_strength` with benchmark-specific text;
- `scale`, non-empty `environment`, and non-empty `protocol`;
- a benchmark-specific inference boundary in `coverage_gap`;
- at least one concrete `confounders` entry;
- at least one primary artifact URL.

The web research model must turn those fields into benchmark-specific claim support, comparison controls, next validation, and a fallback evidence brief. Generic area-level prose is not a valid replacement.

If a normalized comparable result set is absent, the page must say so explicitly rather than fabricate a leaderboard or silently leave the result layer empty.

## Deep-note publication gate

Activation time: `2026-09-02T13:31:45Z`.

For a benchmark first accepted by Radar at or after the activation time, publication requires a paired `benchmarks/<id>.md` and `benchmarks/<id>.en.md` note. Each note must be grounded in full text or equivalent primary protocol evidence and cover the measurement object, closest predecessor, decisive evidence, score/claim ceiling, strongest confounder, remaining gap, and genealogy consequence. Quantitative values are included only when verified from a primary source.

Pre-activation canonical records remain valid while their notes are backfilled. The Daily Agent treats missing or thin historical notes as an explicit backlog, not as evidence that the benchmark should disappear from the public registry.

## Backfill priority

After genuinely new material is processed, use remaining run budget to improve multiple existing pages in this order:

1. canonical records with no paired note;
2. existing notes that are materially thin or generic;
3. frontier and transition benchmarks;
4. foundations and precursors.

A historical backfill is a material content update and may be published even when no new benchmark is discovered.

## Bilingual and evidence rules

Chinese and English are projections of one research judgment. Identity, quantitative evidence, claim boundary, comparison controls, and primary links must agree. Natural phrasing may differ.

Do not infer a component-level causal gain from a packaged system result. Do not invent missing SOTA scores, model results, or protocol details. When primary evidence is insufficient, state the evidence gap explicitly and keep the page useful through the measurement contract, known confounders, and next coordinate.

## Validation

Run:

```bash
python scripts/validate_detail_pages.py
python -m unittest discover -s tests -v
python scripts/validate_reading.py
```

`validate_detail_pages.py` hard-fails missing canonical baseline fields, unpaired existing notes, underspecified notes below the safety floor, and post-activation accepted records without paired deep notes. It also reports the historical note backlog so the Daily Agent can continue reducing it over time.
