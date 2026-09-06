import assert from "node:assert/strict";
import test from "node:test";
import { readFileSync } from "node:fs";
import {
  dateInterval,
  calendarWindow,
  dayWindow,
  isoDay,
  releaseDate,
  inReleaseWindow,
  isPublishedRecord,
} from "../src/lib/release-time.mjs";
import { loadRegistry } from "../src/lib/registry.mjs";
import {
  getStableFacetValues,
  getStableFacets,
} from "../src/lib/research-model.mjs";
import {
  parseFilterState,
  serializeFilterState,
  filterBenchmarks,
  matchesFacetGroups,
} from "../src/lib/filters.mjs";
import { suiteState, suiteParams } from "../src/lib/suite-state.mjs";
import { renderMarkdown, resolveNoteLink } from "../src/lib/markdown.mjs";
import { loadAllResultSets, presentResult } from "../src/lib/results.mjs";
const registry = loadRegistry();

test("known first-public corrections retain separate conference publication dates", () => {
  for (const [id, date, pub] of [
    ["locomo", "2024-02-27", "2024-08"],
    ["mem-gallery", "2026-01-07", "2026-07"],
    ["locomo-plus", "2026-02-11", "2026-07"],
  ]) {
    const item = registry.find((x) => x.id === id);
    assert.equal(releaseDate(item).date, date);
    assert.equal(item.publication_at, pub);
    assert.equal(item.release_date_evidence.first_public_at.precision, "day");
    assert.match(
      item.release_date_evidence.first_public_at.source,
      /arxiv.org/,
    );
  }
});
test("unknown historical event types are not promoted to first-public facts", () => {
  for (const item of registry.filter(
    (x) => !x.first_public_at && !x.publication_at && !x.data_release_at,
  )) {
    assert.equal(releaseDate(item).field, "legacy_recorded_at");
    assert.equal(
      item.release_date_evidence.legacy_recorded_at.status,
      "event-type-unclassified",
    );
  }
});
test("six calendar months and inclusive day windows do not drift", () => {
  const w = calendarWindow("2026-09-05");
  assert.equal(isoDay(w.start), "2026-03-05");
  assert.equal(isoDay(w.end), "2026-09-05");
  assert.equal(isoDay(calendarWindow("2024-08-31").start), "2024-02-29");
  const d = dayWindow("2026-09-05");
  assert.equal((d.end - d.start) / 86400000 + 1, 30);
  assert.equal(inReleaseWindow({ released: "2026-02" }, w), false);
  assert.equal(inReleaseWindow({ released: "2026-03" }, w), true);
  assert.equal(inReleaseWindow({ released: "2026-09-06" }, w), false);
});
test("source precision and impossible dates are validated", () => {
  assert.equal(
    dateInterval("2024-02").end - dateInterval("2024-02").start,
    28 * 86400000,
  );
  for (const value of ["2026-02-29", "2026-13", "2026-00-01", "2026-09-00"])
    assert.throws(() => dateInterval(value));
});
test("verified entries remain discoverable rather than excluded by active-only filtering", () => {
  assert.ok(registry.filter((x) => x.status === "verified").length > 0);
  assert.equal(registry.filter(isPublishedRecord).length, registry.length);
});
test("facet keys preserve group identity and prose edits cannot alter membership", () => {
  const options = getStableFacets(registry).flatMap((f) =>
    f.options.map((o) => o.key),
  );
  assert.equal(new Set(options).size, options.length);
  for (const item of registry)
    assert.deepEqual(
      getStableFacetValues({
        ...item,
        summary: "changed unrelated prose",
        measurement_strength: "modified",
      }),
      getStableFacetValues(item),
    );
  assert.equal(matchesFacetGroups(["a:shared"], ["b:shared"]), false);
});
test("OR within each facet, AND between groups: real audit fixture is 16, not 85", () => {
  const facets = getStableFacets(registry);
  const choose = (id) =>
    facets.flatMap((f) => f.options).find((o) => o.id === id)?.key;
  const items = registry.map((x) => ({
    ...x,
    stableFacets: getStableFacetValues(x),
  }));
  const a = facets
    .flatMap((f) => f.options)
    .find((o) => o.label.en.toLowerCase().includes("conversation"))?.key;
  const b = choose("answer-quality");
  assert.ok(a && b, JSON.stringify(facets));
  const filter = (keys) =>
    filterBenchmarks(
      items,
      parseFilterState(new URLSearchParams(keys.map((key) => ["facet", key]))),
    );
  const left = filter([a]),
    right = filter([b]);
  const common = left.filter((x) => right.some((y) => y.id === x.id));
  assert.equal(common.length, 16);
  assert.deepEqual(
    filter([a, b]).map((x) => x.id),
    common.map((x) => x.id),
  );
});
test("zero-result model and all metric families remain filterable", () => {
  const rs = loadAllResultSets();
  const items = registry.map((x) => ({
    ...x,
    metricFamilies: rs.get(x.id)?.tracks.map((t) => t.metric.family) || [],
  }));
  assert.equal(
    filterBenchmarks(
      items,
      parseFilterState(new URLSearchParams("q=zzzz_no_match_09876")),
    ).length,
    0,
  );
  assert.ok(
    filterBenchmarks(
      items,
      parseFilterState(new URLSearchParams("metric=rmse")),
    ).some((x) => x.id === "ragbench"),
  );
});
test("namespaced facets and all source statuses round-trip; headroom is retired", () => {
  const state = parseFilterState(
    new URLSearchParams(
      "facet=a:one&facet=b:one&status=paper-snapshot&headroom=wide",
    ),
  );
  assert.deepEqual(
    parseFilterState(new URLSearchParams(serializeFilterState(state))),
    state,
  );
  assert.deepEqual(state.headroomBands, []);
  assert.equal(state.sourceTypes[0], "paper-snapshot");
  assert.deepEqual(state.resultStatuses, []);
});
test("editing a suite invalidates its preset claim and keeps all benchmark identities", () => {
  const r = { id: "safety", core: ["a"], complement: ["b", "c", "d"] };
  assert.equal(suiteState(["a", "b", "c", "d"], r).matches, true);
  assert.equal(suiteState(["b", "c", "d"], r).matches, false);
  const empty = suiteState([], r);
  assert.equal(empty.empty, true);
  assert.equal(empty.matches, false);
  assert.equal(suiteParams(empty, r.id).get("custom"), "1");
  assert.equal(suiteParams(empty, r.id).has("recipe"), false);
  assert.equal(
    suiteParams(suiteState(["a", "b", "c", "d"], r), r.id).getAll("benchmark")
      .length,
    4,
  );
});
test("Markdown preserves negation, paragraphs, nested lists, tables, and code", () => {
  const md =
    '## Limits\n\n这些能力尚未覆盖。\n\nSecond paragraph.\n\n- Parent\n  - Child\n\n| A | B |\n|---|---|\n| 1 | 2 |\n\n```js\nconst text="未覆盖";\n```';
  const { html, headings } = renderMarkdown(md, {
    id: "structmemeval",
    lang: "zh",
  });
  assert.match(html, /这些能力尚未覆盖。/);
  assert.match(html, /<table>/);
  assert.match(html, /<pre><code/);
  assert.match(html, /<ul>[\s\S]*<ul>/);
  assert.equal(headings[0].id, "note-limits");
  assert.doesNotMatch(html, /下一步评测坐标/);
});
test("maintenance comments are removed and relative publication links become real routes", () => {
  const { html } = renderMarkdown(
    "<!-- RESEARCH-DECISION:START -->\n\n[English](structmemeval.en.md) · [返回 Radar](../README.md)\n\n<!-- RESEARCH-DECISION:END -->",
    { lang: "zh", id: "structmemeval" },
  );
  assert.doesNotMatch(html, /RESEARCH-DECISION/);
  assert.match(
    html,
    /href="\/Agent-Benchmark-Radar\/en\/benchmarks\/structmemeval\/"/,
  );
  assert.match(html, /href="\/Agent-Benchmark-Radar\/zh\/"/);
  for (const url of [
    "javascript:alert(1)",
    "data:text/html,test",
    "//evil.test",
    "../../../../etc/passwd",
  ])
    assert.equal(resolveNoteLink(url), undefined);
});
test("a single SCALE-QA baseline is scoped consistently, never advertised as current best", () => {
  const rs = loadAllResultSets().get("scale-qa");
  assert.equal(rs.tracking_status, "paper-snapshot");
  for (const lang of ["zh", "en"]) {
    const view = presentResult(rs, lang);
    assert.equal(view.score, 29.8);
    assert.ok(view.model);
    assert.match(view.label, /基线|baseline/i);
    assert.doesNotMatch(view.label, /当前|best/);
  }
});
