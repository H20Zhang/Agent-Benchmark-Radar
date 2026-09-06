# Site publication and regression contract

The home page and Timeline share one chronology component; all public surfaces use
one typography and layout sheet. Timeline records precede editorial interpretation.
Source records remain separate from comparison hypotheses and partial result sets.

## Release-blocking invariants

| Failure mode | Permanent contract | Regression gate |
|---|---|---|
| First-public and publication dates conflated | Typed date events with source and precision; retain unclassified legacy provenance | Known three-date fixtures, invalid-date and interval tests |
| Zero count with visible cards | HTML `hidden` wins over every display rule | Browser zero query: zero visible cards |
| Cross-facet union | Namespaced facet/option identities; OR within, AND across groups | Real conversation × answer-quality fixture: 16 records |
| Mobile navigation loses tools | All primary routes and language toggle remain reachable at every breakpoint | 390 / 768 / 1440 rendered navigation checks |
| Author's negation rewritten | Markdown AST, no global prose substitution | Negation, paragraphs, nested lists, tables and code fixtures |
| Relative links/comments leak | Resolve source paths to routes; omit maintenance comments | All generated hrefs/fragments plus all 262 notes |
| Edited/empty suite retains preset claim | Recompute exact set match; custom is unvalidated; empty export disabled | Browser removal, reload and preset-state tests |
| Comparison silently drops selections | Preserve all unique selected ids; scroll complete comparison table | Four-item governance suite → four comparison columns |
| Narrative becomes a grid | Normal document flow with bounded line length and section anchors | Computed prose display, rendered narrow-layout checks |
| One baseline becomes “current best” | Shared scope-bounded presentation with source and dates | SCALE-QA baseline fixture and every result-track presentation |

## Publication quality invariants

Both READMEs preserve complete area tables and derive their date window, summaries,
recipes and result coverage from canonical data. A six-calendar-month window and an
inclusive 30-day window are separate operations; no month is promoted to a day.
All 131 records, including entries marked `verified`, remain available in the
published registry. Historical classification gaps and imported heuristic facet
assignments stay explicit rather than masquerading as newly verified facts.

Run from the repository root:

```sh
node web/scripts/sync-publication.mjs
python -m unittest discover -s tests -v
python scripts/validate_reading.py
python scripts/validate_detail_pages.py
cd web
npm test
npm run check:publication
npm run check
npm run build
python scripts/verify-site.py --output /tmp/radar-verification
```

The rendered gate requires Python `playwright` and `beautifulsoup4`, plus Chromium.
CI installs the pinned versions used by the local audit and exercises a real HTTP
origin. It checks all generated HTML, renders every content route at phone width,
and checks the core routes in both languages at three widths. It also verifies
reload, language-switch, and history round-trips for the workflows above.

`--offline` is available for environments that prohibit browser networking. It
renders the exact built CSS and JavaScript from local bytes; history calls are
captured instead of navigated. This mode is **not** a substitute for the real-origin
CI gate. Screenshots and metrics are ephemeral CI artifacts, not public run logs.
