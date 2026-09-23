# Historical release references

Every accepted benchmark has one compact bilingual reference immediately below its existing title. It records the original benchmark's reported result under an explicit protocol, as a historical difficulty reference—not a current leaderboard or an estimate of remaining headroom.

`data/release-references.json` is the authored source. `scripts/render-release-references.py` projects it into both notes. The normal `scripts/render-readme.mjs` command invokes this projection, including `--check`. No network or model call is required.

## Evidence and labels

- `release-best`: best within a named comparison in the initial paper or release. Record system, metric, score, decisive conditions, source location and version. A subgroup best is not automatically an overall winner.
- `release-reference`: selected original-paper configuration or baseline. One recorded result does not establish a best claim.
- `diagnostic`: original validity or safety evidence. Attack-success rates, constraint retention and evaluator correlation are not defender task accuracy.
- `later-version` and `paper-reference`: a known later paper version, or a historical source whose initial-version identity remains unverified. Neither is labeled a launch best.
- `unverified`: the initial score or comparison is not established. Link the original source without fabricating a number, inserting zero, or asserting that the authors published no result.

The `benchmarks` dictionary uses canonical IDs. Each record includes `status`, bilingual `period`, `scope` and `caveat`, explicit `results`, HTTPS `source`, `locator`, and `initial_release` (true, false or null). A `release-best` additionally declares `comparison_scope`. Each result names its system, metric and score, optionally a narrower scope and source. Numbers retain the original units and precision. Different tasks, splits, judges, budgets and versions are not synthesized into one score.

Previously curated paper snapshots retain `source_record`, `source_verified_at` and explicit track/entry provenance. Transcribing one does not imply a new primary-paper audit. An unavailable model name stays unverified even when an abstract explicitly reports a best score.

## Maintenance and validation

Update this editorial source only when evidence about the historical experiment changes. Do not choose a new maximum from `data/results/`, infer release time from a maintenance date, or replace historical anchors during citation refreshes. Corrections must retain version boundaries and expose source disagreements.

```bash
node scripts/render-readme.mjs
node scripts/render-readme.mjs --check
python -m unittest discover -s tests -v
python scripts/validate_reading.py
python scripts/validate_detail_pages.py
```

The standalone renderer supports `--check` and `--root`. Newly accepted IDs without authored references get an explicit unknown header, so every note remains readable without invented evidence. Orphan IDs, missing bilingual note pairs, invalid source records and duplicate markers abort publication. Projection validates all notes before writing. Header changes do not advance discovery, citation, result-verification or original acceptance timestamps.

These checks validate publication invariants. They neither certify factual paper claims nor reproduce benchmark experiments.
