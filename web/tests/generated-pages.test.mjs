import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import test from "node:test";
import { loadRegistry } from "../src/lib/registry.mjs";
import { loadChineseSummaries } from "../src/lib/readme-localization.mjs";
import { loadDeepRead, getAuthoredBrief } from "../src/lib/deep-reads.mjs";
import { loadAllResultSets, presentResult } from "../src/lib/results.mjs";
const read = (path) =>
  readFileSync(new URL(`../src/${path}`, import.meta.url), "utf8");

test("home and dedicated timeline share the same factual projection", () => {
  for (const path of [
    "pages/[lang]/index.astro",
    "pages/[lang]/timeline/index.astro",
  ])
    assert.match(read(path), /<Timeline\s/);
  const component = read("components/Timeline.astro");
  assert.match(component, /isPublishedRecord/);
  assert.match(component, /publicationWindow/);
  assert.doesNotMatch(
    component,
    /evolution_role|loadAllResultSets|frontierShifts/,
  );
});
test("all registry records have matched authored notes, localized targets, and usable navigation", () => {
  const zh = loadChineseSummaries();
  for (const item of loadRegistry())
    for (const lang of ["zh", "en"]) {
      const note = loadDeepRead(item.id, lang);
      assert.ok(note.html, item.id);
      assert.ok(zh.get(item.id));
      assert.doesNotMatch(
        note.html,
        /RESEARCH-DECISION:|\]\([^)]*\.md(?:#.*?)?\)/,
        `${lang}/${item.id}`,
      );
      assert.ok(note.headings.length > 0);
      assert.equal(
        note.headings.length,
        new Set(note.headings.map((h) => h.id)).size,
      );
      assert.ok(
        getAuthoredBrief(item.id, lang).next,
        `${lang}/${item.id}: authored next experiment`,
      );
    }
});
test("all result summaries bind record scope, method, source and distinct dates", () => {
  for (const rs of loadAllResultSets().values())
    for (const track of rs.tracks) {
      const value = presentResult(rs, "en", track);
      assert.ok(value.source.startsWith("https://"));
      assert.equal(value.verifiedAt, rs.verified_at);
      assert.ok(value.reportedAt);
      assert.ok(value.scope.includes("SOTA"));
      assert.doesNotMatch(value.label, /Current best|SOTA|headroom/);
    }
});
test("shared shell owns indexability and one typography sheet", () => {
  const layout = read("layouts/BaseLayout.astro");
  assert.match(layout, /robots = "index,follow"/);
  assert.match(layout, /styles\/site.css/);
  assert.doesNotMatch(
    layout,
    /styles\/(global|research-tool|core-tool-ui)\.css/,
  );
  const css = read("styles/site.css");
  assert.match(css, /\[hidden\]\s*\{\s*display:\s*none\s*!important;?\s*\}/);
  assert.doesNotMatch(css, /site-nav[^{}]*nth-child/);
});
test("area registry precedes optional interpretation and has scoped timeline entry", () => {
  const page = read("pages/[lang]/areas/[area].astro");
  assert.ok(
    page.indexOf("<BenchmarkCard") < page.indexOf("genealogy&&<details"),
  );
  assert.match(page, /timeline\/\?area=/);
});
test("result panels do not claim a controlled protocol cell or draw false progress bars", () => {
  const panel = read("components/ResultsPanel.astro");
  assert.match(panel, /presentResult/);
  assert.match(panel, /entry.source/);
  assert.match(panel, /metric.direction/);
  assert.doesNotMatch(panel, /score-bars|Current best|当前最好|当前最佳/);
});
