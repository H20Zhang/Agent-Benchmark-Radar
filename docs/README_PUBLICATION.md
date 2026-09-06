# README-first publication

The Chinese and English README files are the primary user reading surfaces. The
standalone website is retired. `web/` is retained as dormant source; Pages serves
only a retirement handoff to GitHub, never the Astro app. Ordinary README/data
updates do not redeploy Pages. Do not re-enable the website without a new decision.

## Reader path

Chronology comes first, followed immediately by every benchmark in three complete
area tables. Month and area anchors let readers jump without opening a separate
site or expanding cards. Benchmark names link to the matching language's authored
note. Paper, repository, dataset and leaderboard links remain directly accessible.
Citations are context, not rank. Unknown citation counts stay distinct from zero.

Optional selection guidance and research interpretation live in
`library/evaluation-recipes*.md`, `library/results*.md` and
`docs/reading-guide*.md`. They do not interrupt the main lists. All 131 current
notes remain available; the number is not a fixed inclusion limit.

## Update sources, then generate both languages

1. Update `data/benchmarks.json` and `data/locales/zh/benchmarks.json`, preserving
   source identity, date type/precision and verification dates.
2. Update paired `benchmarks/<id>.md` and `<id>.en.md` when substantive evidence
   changes. Change recipes in `data/recipes.json`; maintain editorial commentary
   in the paired `docs/reading-guide*.md`, not the generated README.
3. Run `node scripts/render-readme.mjs`, then
   `node scripts/render-readme.mjs --check` and
   `python -m unittest discover -s tests -v`.
4. Commit the inputs and every generated projection together. No Astro install,
   build or deployment is required for normal content maintenance.

The compatibility command `node web/scripts/sync-publication.mjs` delegates to
the same renderer. Citation refresh regenerates the same projections; it must not
reinstate old table layouts. Discovery scan, citation refresh and result
verification dates remain independent. An editorial rewrite does not advance any
of those factual timestamps.

## Acceptance

The reader contract checks the exact canonical membership and chronology of every
table, direct note and source links, one-sentence summary parity, truthful date
labels, citation values and bilingual ID/order equivalence. Source integrity tests
and the complete legacy Library validation remain. The retired website can still
be checked explicitly, but its visual assumptions do not govern the README.
