# Evaluation Frontier Web v2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn Agent Benchmark Radar into an Astro-based evaluation-frontier product that helps researchers discover benchmarks, assemble evaluation suites, inspect comparable results, identify evaluation opportunities, and track frontier movement.

**Architecture:** Keep `data/benchmarks.json` as the factual registry and add focused structured editorial/result sources under `data/`. A typed loader joins them at Astro build time; every route remains statically rendered, with small framework-free client scripts for filtering, comparison, and chart interaction. README and web pages project the same structured recipes, opportunities, genealogy, shifts, and results.

**Tech Stack:** Astro 7, JavaScript ES modules with JSDoc types, semantic HTML, CSS/SVG, Node test runner, Python `unittest`, GitHub Pages.

**Spec:** `docs/superpowers/specs/2026-09-01-evaluation-frontier-web-v2-design.md`

## Global Constraints

- Preserve the existing project URL, bilingual route symmetry, stable benchmark IDs, canonical URLs, and GitHub Pages deployment.
- Public copy uses Measurement strength, Suite completion, Fair comparison conditions, and Next validation.
- Raw result scores rank only inside an explicit comparable track.
- Quality and efficiency remain parallel dimensions; no composite frontier or efficiency score.
- Result facts require a primary source and verification date.
- Astro pre-renders essential facts and interpretation; JavaScript enhances interaction only.
- Existing URLs continue to resolve.
- Each completed task ends with relevant tests and a focused commit.

---

### Task 1: Shared Research Model and Validators

**Files:**
- Create: `data/taxonomy.json`
- Create: `data/recipes.json`
- Create: `data/genealogy.json`
- Create: `data/opportunities.json`
- Create: `data/frontier_shifts.json`
- Create: `data/editorial/benchmarks/*.json`
- Create: `web/src/lib/research-model.mjs`
- Create: `web/tests/research-model.test.mjs`
- Modify: `web/src/lib/registry.mjs`

**Interfaces:**
- Produces: `loadResearchModel(): ResearchModel`, `getBenchmarkResearch(id, lang): BenchmarkResearch`, `getStableFacets(items): FacetGroup[]`.
- `ResearchModel` contains `taxonomy`, `recipes`, `genealogy`, `opportunities`, and `frontierShifts`.

- [ ] **Step 1: Write failing loader and referential-integrity tests**

```js
test("research objects reference canonical benchmark ids", () => {
  const model = loadResearchModel();
  const ids = new Set(loadRegistry().map((item) => item.id));
  for (const recipe of model.recipes) {
    for (const id of [...recipe.core, ...recipe.complement]) assert.ok(ids.has(id));
  }
});

test("stable taxonomy stays below the interaction budget", () => {
  const facets = getStableFacets(loadRegistry());
  assert.ok(facets.every((facet) => facet.options.length <= 12));
});
```

- [ ] **Step 2: Run tests and confirm missing-module failure**

Run: `cd web && npm test`

Expected: FAIL because `research-model.mjs` and structured files do not exist.

- [ ] **Step 3: Add canonical structured sources from existing README judgments**

Encode the 15 claim-first recipes, three area genealogies, current frontier shifts, and curated next evaluation coordinates. Give every bilingual editorial field the shape `{ "zh": "…", "en": "…" }`. Map stable taxonomy dimensions through explicit token and area rules while retaining raw tags separately.

- [ ] **Step 4: Implement immutable loaders and validation**

```js
export function loadResearchModel() {
  return Object.freeze({
    taxonomy: readJson("data/taxonomy.json"),
    recipes: readJson("data/recipes.json"),
    genealogy: readJson("data/genealogy.json"),
    opportunities: readJson("data/opportunities.json"),
    frontierShifts: readJson("data/frontier_shifts.json"),
  });
}
```

Validate unique IDs, bilingual fields, benchmark references, allowed areas, bounded taxonomy option counts, and deterministic order at load time.

- [ ] **Step 5: Run the loader tests**

Run: `cd web && npm test`

Expected: PASS for research-model tests and existing registry tests.

- [ ] **Step 6: Commit**

```bash
git add data web/src/lib/registry.mjs web/src/lib/research-model.mjs web/tests/research-model.test.mjs
git commit -m "feat(data): add evaluation frontier research model"
```

### Task 2: Comparable Result Model

**Files:**
- Create: `data/results/*.json`
- Create: `web/src/lib/results.mjs`
- Create: `web/tests/results.test.mjs`
- Modify: `web/src/lib/research-model.mjs`

**Interfaces:**
- Produces: `loadResultSet(id): ResultSet | undefined`, `loadAllResultSets(): ReadonlyMap<string, ResultSet>`, `summarizeTrack(track): TrackSummary`, `getProgressPoint(item, resultSet, now): ProgressPoint`.
- A track identity is `benchmark_id + track_id`; the track stores task, split, protocol version, metric, entries, target provenance, and efficiency context.

- [ ] **Step 1: Write failing comparability, headroom, and progress tests**

```js
test("headroom is emitted only with a sourced bounded target", () => {
  assert.equal(summarizeTrack(trackWithoutTarget).headroom, undefined);
  assert.equal(summarizeTrack(trackWithTarget).headroom, 18.4);
});

test("best score respects metric direction", () => {
  assert.equal(summarizeTrack(higherIsBetter).best.score, 82.1);
  assert.equal(summarizeTrack(lowerIsBetter).best.score, 1.8);
});
```

- [ ] **Step 2: Run tests and confirm the missing result module**

Run: `cd web && node --test tests/results.test.mjs`

Expected: FAIL because `results.mjs` is absent.

- [ ] **Step 3: Add verified result files**

Create result files for benchmark notes that already contain attributable paper results, prioritizing current frontier benchmarks and historical anchors. Each file declares `tracking_status`, `verified_at`, and one or more explicit tracks. Preserve paper snapshots for historical anchors and live tracking for active sources.

- [ ] **Step 4: Implement result loading and derived values**

```js
export function summarizeTrack(track) {
  const ordered = [...track.entries].sort(scoreComparator(track.metric.direction));
  const best = ordered[0];
  const target = track.metric.reference_target;
  return { best, headroom: target ? normalizedHeadroom(best.score, track.metric, target) : undefined };
}
```

Reject duplicate entry IDs, out-of-range values, missing sources, invalid direction, unsourced targets, and result dates earlier than benchmark release.

- [ ] **Step 5: Run result and registry tests**

Run: `cd web && npm test`

Expected: PASS.

- [ ] **Step 6: Commit**

```bash
git add data/results web/src/lib/results.mjs web/src/lib/research-model.mjs web/tests/results.test.mjs
git commit -m "feat(results): add verified benchmark result tracks"
```

### Task 3: Intent-Led Shell and Navigation

**Files:**
- Modify: `web/src/lib/i18n.mjs`
- Modify: `web/src/components/Header.astro`
- Modify: `web/src/components/SiteFooter.astro`
- Modify: `web/src/pages/[lang]/index.astro`
- Modify: `web/src/styles/global.css`
- Modify: `web/package.json`
- Modify: `web/tests/generated-pages.test.mjs`

**Interfaces:**
- Consumes: `loadResearchModel`, `loadAllResultSets`, and current registry.
- Produces: three primary navigation destinations and the intent-led home page.

- [ ] **Step 1: Write failing source-contract tests**

```js
test("home leads with benchmark, opportunity, and frontier decisions", () => {
  const page = read("src/pages/[lang]/index.astro");
  for (const token of ["Benchmarks", "Opportunities", "Frontier", "loadResearchModel"])
    assert.ok(page.includes(token));
});
```

- [ ] **Step 2: Run generated page tests and confirm failure**

Run: `cd web && node --test tests/generated-pages.test.mjs`

Expected: FAIL on the new home contract.

- [ ] **Step 3: Rebuild the home information hierarchy**

Replace the filter-first hero with the evaluation-frontier thesis, three action entrances, latest verified releases, active result movement, curated opportunities, and domain Radar continuation. Keep the global search action and current registry statistics.

- [ ] **Step 4: Update header, footer, responsive navigation, and bilingual copy**

Use primary links for Benchmarks, Opportunities, and Frontier; expose Evaluate, Methodology, GitHub, and language switching as secondary actions. Preserve semantic landmarks, visible focus, reduced motion, and responsive behavior.

- [ ] **Step 5: Run tests and Astro check**

Run: `cd web && npm test && npm run check`

Expected: PASS.

- [ ] **Step 6: Commit**

```bash
git add web/src/lib/i18n.mjs web/src/components web/src/pages/[lang]/index.astro web/src/styles/global.css web/tests/generated-pages.test.mjs
git commit -m "feat(web): lead with evaluation frontier decisions"
```

### Task 4: Research-Grade Explorer

**Files:**
- Create: `web/src/pages/[lang]/benchmarks/index.astro`
- Modify: `web/src/components/Explorer.astro`
- Modify: `web/src/components/FilterPanel.astro`
- Modify: `web/src/components/BenchmarkCard.astro`
- Modify: `web/src/lib/filters.mjs`
- Modify: `web/src/scripts/explorer.mjs`
- Modify: `web/src/styles/global.css`
- Modify: `web/tests/filters.test.mjs`
- Modify: `web/tests/explorer.test.mjs`

**Interfaces:**
- Consumes: stable facets from Task 1 and result summaries from Task 2.
- Produces: shareable filters with OR-within/AND-across semantics and visible active chips.

- [ ] **Step 1: Add failing multi-select and result-filter tests**

```js
test("result-aware filters survive a canonical URL round trip", () => {
  const state = parseFilterState(new URLSearchParams("cap=memory-update&status=live&headroom=wide"));
  assert.equal(serializeFilterState(state), "cap=memory-update&status=live&headroom=wide");
});
```

- [ ] **Step 2: Run filter tests and confirm failure**

Run: `cd web && node --test tests/filters.test.mjs tests/explorer.test.mjs`

Expected: FAIL on stable taxonomy and result fields.

- [ ] **Step 3: Extend filter state and matching**

Add stable capability, environment, evaluation objective, evaluator type, lifecycle, result status, headroom, progress, benchmark age, and metric-family fields. Map v1 capability/environment/protocol query keys into the raw-tag escape hatch.

- [ ] **Step 4: Replace native giant selects with progressive controls**

Render search, area, release period, and sort in the compact bar. Render stable dimensions in a drawer/sheet and raw tags as a searchable on-demand control. Keep active chips outside the drawer and retain a no-JavaScript submit path.

- [ ] **Step 5: Add result signals to cards**

Show tracking state, current best with metric label, verification date, and next measurement coordinate only when the joined data supplies them. Keep cards concise and route full interpretation to the detail page.

- [ ] **Step 6: Run tests, check, and build**

Run: `cd web && npm test && npm run check && npm run build`

Expected: PASS with no giant raw-tag option list in the generated benchmark page.

- [ ] **Step 7: Commit**

```bash
git add web/src web/tests
git commit -m "feat(web): replace raw filters with research facets"
```

### Task 5: Benchmark Dossiers and Result Visuals

**Files:**
- Create: `web/src/components/ResultsPanel.astro`
- Create: `web/src/components/ScoreTimeline.astro`
- Create: `web/src/components/GenealogyTrail.astro`
- Create: `web/src/lib/deep-reads.mjs`
- Modify: `web/src/components/BenchmarkDetail.astro`
- Modify: `web/src/pages/[lang]/benchmarks/[id].astro`
- Modify: `web/src/styles/global.css`
- Modify: `web/tests/generated-pages.test.mjs`

**Interfaces:**
- Consumes: benchmark facts, localized editorial data, `ResultSet`, recipes, genealogy, and deep-read Markdown.
- Produces: a fully static dossier with optional result and deep-read sections.

- [ ] **Step 1: Write failing dossier contract tests**

```js
test("benchmark dossiers expose decision and result sections", () => {
  const detail = read("src/components/BenchmarkDetail.astro");
  for (const token of ["scoreSupports", "comparisonControls", "ResultsPanel", "GenealogyTrail"])
    assert.ok(detail.includes(token));
});
```

- [ ] **Step 2: Run generated page tests and confirm failure**

Run: `cd web && node --test tests/generated-pages.test.mjs`

Expected: FAIL on the dossier contract.

- [ ] **Step 3: Implement the selection summary and evaluation contract**

Correct the Chinese measurement duplication by using the canonical measurement-strength field. Render score support, suite role, next validation, fair comparison conditions, task, state, expected output, metrics, verifier, budget, and linked filter chips.

- [ ] **Step 4: Implement results and score timeline**

Render one table per explicit track with method, model, score, date, protocol/budget context, and source. Generate accessible SVG paths from dated comparable entries; provide the same values in the adjacent table.

- [ ] **Step 5: Add genealogy, recipes, related benchmarks, and deep reads**

Resolve explicit relations first, then use shared stable dimensions for labeled related items. Add `marked` and `sanitize-html` as explicit dependencies; render repository-owned bilingual notes with `marked.parse`, then allow only headings, paragraphs, links, lists, tables, code, blockquotes, and emphasis through `sanitizeHtml`. Preserve heading hierarchy and add `rel="noreferrer"` to external links.

- [ ] **Step 6: Run tests, check, and build**

Run: `cd web && npm test && npm run check && npm run build`

Expected: PASS; every benchmark route renders and result sections appear only with verified data.

- [ ] **Step 7: Commit**

```bash
git add web/src web/tests web/package.json
git commit -m "feat(web): turn benchmark pages into research dossiers"
```

### Task 6: Evaluate and Compare Workflows

**Files:**
- Create: `web/src/pages/[lang]/evaluate.astro`
- Create: `web/src/pages/[lang]/compare.astro`
- Create: `web/src/components/SuiteBuilder.astro`
- Create: `web/src/components/BenchmarkComparison.astro`
- Create: `web/src/scripts/suite-builder.mjs`
- Modify: `web/src/styles/global.css`
- Modify: `web/tests/generated-pages.test.mjs`

**Interfaces:**
- Consumes: recipes, benchmark dossiers, and result summaries.
- Produces: `?claim={recipe-id}` suite URLs and `?benchmarks={id},{id},{id}` comparison URLs.

- [ ] **Step 1: Write failing route and URL contract tests**

```js
test("evaluate and compare routes consume canonical research data", () => {
  assert.match(read("src/pages/[lang]/evaluate.astro"), /loadResearchModel/);
  assert.match(read("src/pages/[lang]/compare.astro"), /BenchmarkComparison/);
});
```

- [ ] **Step 2: Run generated page tests and confirm failure**

Run: `cd web && node --test tests/generated-pages.test.mjs`

Expected: FAIL because routes are absent.

- [ ] **Step 3: Build the claim-first suite experience**

Show Core, Complement, claim boundary, fair comparison conditions, next validation, and relevant result tracks. Add deterministic URL state and a copyable Markdown export generated entirely from visible canonical data.

- [ ] **Step 4: Build two-to-three benchmark comparison**

Align measurement target, environment, protocol, scale, artifacts, tracking state, score interpretation, suite role, and next validation. Keep non-comparable result tracks in separate panels.

- [ ] **Step 5: Run tests, check, and build**

Run: `cd web && npm test && npm run check && npm run build`

Expected: PASS.

- [ ] **Step 6: Commit**

```bash
git add web/src web/tests
git commit -m "feat(web): add evaluation suite and comparison tools"
```

### Task 7: Opportunity, Frontier, and Area Visualizations

**Files:**
- Create: `web/src/pages/[lang]/opportunities/index.astro`
- Create: `web/src/pages/[lang]/opportunities/[id].astro`
- Create: `web/src/pages/[lang]/frontier.astro`
- Create: `web/src/components/OpportunityMap.astro`
- Create: `web/src/components/BenchmarkProgressMap.astro`
- Create: `web/src/components/GenealogyMap.astro`
- Modify: `web/src/pages/[lang]/areas/[area].astro`
- Modify: `web/src/styles/global.css`
- Modify: `web/tests/generated-pages.test.mjs`

**Interfaces:**
- Consumes: opportunities, frontier shifts, genealogy, registry, and progress points.
- Produces: indexable opportunity/frontier pages and accessible SVG/table visualizations.

- [ ] **Step 1: Write failing static-route and visualization tests**

```js
test("opportunity and frontier routes are generated bilingually", () => {
  assert.match(read("src/pages/[lang]/opportunities/[id].astro"), /LOCALES\.flatMap/);
  assert.match(read("src/pages/[lang]/frontier.astro"), /BenchmarkProgressMap/);
});
```

- [ ] **Step 2: Run generated page tests and confirm failure**

Run: `cd web && node --test tests/generated-pages.test.mjs`

Expected: FAIL because routes and components are absent.

- [ ] **Step 3: Build Opportunity Map and pages**

Render capability × environment for one objective at a time. Use explicit cell states for established coverage, active expansion, and curated next coordinates. Provide evidence, feasibility, confidence, related benchmarks, and verification date on each opportunity page.

- [ ] **Step 4: Build Frontier and progress views**

Render 30-day shifts, six-month release/result timeline, progress points, and digest links. Separate defined-headroom points from current-best/activity-only benchmarks.

- [ ] **Step 5: Upgrade area pages**

Follow `area thesis → genealogy → current results → recipes → opportunities → recent shifts → library`. Use custom SVG/HTML genealogy with keyboard-accessible benchmark links and a textual stage summary.

- [ ] **Step 6: Run tests, check, and build**

Run: `cd web && npm test && npm run check && npm run build`

Expected: PASS for all bilingual routes, accessible alternatives, and metadata.

- [ ] **Step 7: Commit**

```bash
git add web/src web/tests
git commit -m "feat(web): visualize evaluation opportunities and frontier"
```

### Task 8: README Projection, SEO, and End-to-End Verification

**Files:**
- Create: `scripts/render_research_surfaces.py`
- Create: `tests/test_research_surface_projection.py`
- Modify: `README.md`
- Modify: `README.en.md`
- Modify: `web/src/pages/[lang]/methodology.astro`
- Modify: `web/src/layouts/BaseLayout.astro`
- Modify: `tests/test_web_contract.py`
- Modify: `.github/workflows/validate.yml`

**Interfaces:**
- Consumes: canonical recipes, opportunities, shifts, genealogy, results, and registry.
- Produces: deterministic README marked regions and validated web metadata.

- [ ] **Step 1: Write failing README projection tests**

```python
def test_projection_is_idempotent(self):
    first = subprocess.run([sys.executable, "scripts/render_research_surfaces.py", "--check"], cwd=ROOT)
    self.assertEqual(first.returncode, 0)
```

- [ ] **Step 2: Run Python tests and confirm the missing renderer failure**

Run: `python -m unittest tests.test_research_surface_projection -v`

Expected: FAIL because the renderer is absent.

- [ ] **Step 3: Implement generated README regions**

Generate the latest verified picks, evaluation recipes, opportunity snapshot, frontier shifts, and benchmark-map summaries between stable bilingual markers. Keep the README scannable and link each section into the richer website route.

- [ ] **Step 4: Complete methodology and metadata**

Document result source priority, comparable tracks, headroom provenance, active-set policy, and opportunity publication gates. Add route-specific canonical, `hreflang`, sitemap `lastmod`, JSON-LD, Open Graph, and social description coverage.

- [ ] **Step 5: Run complete verification**

Run: `python -m unittest discover -s tests -v`

Run: `python scripts/validate_reading.py`

Run: `cd web && npm install --no-audit --no-fund && npm test && npm run check && npm run build`

Expected: all Python and Node tests pass; Astro builds all bilingual benchmark, opportunity, area, evaluate, compare, frontier, and methodology routes.

- [ ] **Step 6: Inspect representative built pages**

Open the generated Chinese home, benchmark explorer, one benchmark with live results, one benchmark with a paper snapshot, one opportunity, and the Frontier page. Verify desktop and mobile layouts, source links, chart labels, active filter chips, language symmetry, and no console errors.

- [ ] **Step 7: Commit**

```bash
git add README.md README.en.md scripts tests web .github/workflows/validate.yml
git commit -m "feat: publish evaluation frontier radar v2"
```
