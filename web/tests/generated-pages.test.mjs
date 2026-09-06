import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import test from "node:test";

const read = (path) =>
  readFileSync(new URL(`../${path}`, import.meta.url), "utf8");

test("home is a public content-first research index", () => {
  const page = read("src/pages/[lang]/index.astro");
  for (const token of [
    "loadRegistry",
    "loadResearchModel",
    "content-home__table",
    "Latest releases",
    "Canonical timeline first",
    'robots="index,follow"',
  ]) assert.ok(page.includes(token), token);
  for (const token of ["网站待完善", "Website under improvement", 'robots="noindex,nofollow"', "wip-shell"]) assert.ok(!page.includes(token), token);
});

test("primary navigation starts from the canonical timeline and exposes stable research surfaces", () => {
  const header = read("src/components/Header.astro");
  for (const token of ["timeline/", "benchmarks/", "evaluate/", "opportunities/", "methodology/"]) assert.ok(header.includes(token), token);
  for (const deadAnchor of ["#timeline", "#results"]) assert.ok(!header.includes(deadAnchor), deadAnchor);
});

test("canonical timeline is a factual release ledger rather than a frontier ranking", () => {
  const page = read("src/pages/[lang]/timeline/index.astro");
  for (const token of ["loadRegistry", "released", "last_verified", "Canonical release timeline", "Strictly by released"]) assert.ok(page.includes(token), token);
  assert.ok(page.includes("SOTA, importance, frontier, or opportunity judgments"));
  assert.ok(!page.includes("loadAllResultSets"));
  assert.ok(!page.includes("frontierShifts"));
  assert.ok(!page.includes("research.opportunities"));
});

test("public layout is indexable unless a route explicitly opts out", () => {
  const layout = read("src/layouts/BaseLayout.astro");
  assert.ok(layout.includes('robots = "index,follow"'));
  assert.ok(!layout.includes('robots = "noindex,nofollow"'));
});

test("benchmark route generates every locale and stable registry id", () => {
  const page = read("src/pages/[lang]/benchmarks/[id].astro");
  assert.match(page, /LOCALES\.flatMap/);
  assert.match(page, /loadRegistry\(\)\.map/);
  assert.match(page, /params:\s*\{\s*lang,\s*id:\s*item\.id\s*\}/);
  assert.match(page, /<BenchmarkDetail/);
  assert.match(page, /Dataset/);
  assert.match(page, /CreativeWork/);
});

test("benchmark details expose a fast research judgment before deep reading", () => {
  const detail = read("src/components/BenchmarkDetail.astro");
  for (const token of ["measurement_strength", "last_verified", "capabilities", "environment", "protocol", "artifacts", "citations"]) assert.ok(detail.includes(token), token);
  assert.ok(!detail.includes("coverage_gap"));
  for (const token of ["scoreSupports", "comparisonControls", "nextValidation", "ResultsPanel", "deepRead", "benchmark-at-a-glance", "benchmark-setup-list", "summarizeTrack"]) assert.ok(detail.includes(token), token);
});

test("default Chinese editorial never silently substitutes English measurement prose", () => {
  const model = read("src/lib/research-model.mjs");
  assert.ok(model.includes("measurementZh = chineseSummary"));
  assert.ok(model.includes("coverage gap 尚未提供规范中文版本"));
  assert.ok(!model.includes("const inferenceBoundary = item.coverage_gap || areaValidation.en"));
});

test("result panels bind visible scores to protocol cells and primary sources", () => {
  const panel = read("src/components/ResultsPanel.astro");
  for (const token of ["summarizeTrack", "track.task", "track.split", "protocol_version", "entry.source", "metric.direction", "not automatically comparable"]) assert.ok(panel.includes(token), token);
  assert.ok(panel.includes("Reported best on this track"));
});

test("area pages explicitly separate factual chronology from interpretation", () => {
  const page = read("src/pages/[lang]/areas/[area].astro");
  assert.match(page, /LOCALES\.flatMap/);
  assert.match(page, /AREAS\.map/);
  assert.match(page, /CollectionPage/);
  assert.match(page, /BenchmarkCard/);
  assert.ok(page.includes("timeline/"));
  assert.ok(page.includes("Interpretive layer"));
  assert.ok(page.includes("not a cross-benchmark ranking"));
  assert.ok(page.includes("verified_at.localeCompare"));
});

test("methodology documents the evidence hierarchy and current structuring boundary", () => {
  const page = read("src/pages/[lang]/methodology.astro");
  assert.match(page, /LOCALES\.map/);
  assert.match(page, /AboutPage/);
  assert.match(page, /Separate facts, result evidence, and research interpretation/i);
  assert.match(page, /事实、结果证据和研究解释/);
  assert.ok(page.includes("Current structuring boundary"));
  assert.ok(page.includes("timeline/"));
});

test("suite builder and comparison workspace expose reusable research decisions", () => {
  const evaluatePage = read("src/pages/[lang]/evaluate/index.astro");
  const evaluateScript = read("src/scripts/evaluate.mjs");
  const comparePage = read("src/pages/[lang]/compare/index.astro");
  const compareScript = read("src/scripts/compare.mjs");
  for (const token of ["research.recipes", "claim_boundary", "next_validation", "data-suite-builder"]) assert.ok(evaluatePage.includes(token), token);
  for (const token of ["URLSearchParams", "recipe", "benchmark", "Markdown", "clipboard", "requestedArea"]) assert.ok(evaluateScript.includes(token), token);
  for (const token of ["comparison_controls", "data-compare-workspace", "loadAllResultSets", "protocolVersion"]) assert.ok(comparePage.includes(token), token);
  for (const token of ["sameProtocolCell", "metricFamily", "protocolVersion", "task", "split", "not a basis for ranking"]) assert.ok(compareScript.includes(token), token);
  assert.ok(!compareScript.includes("data.filter((item) => item.result).slice(0, 3)"));
});

test("frontier and opportunity pages explicitly label interpretation over factual anchors", () => {
  const opportunities = read("src/pages/[lang]/opportunities/index.astro");
  const opportunity = read("src/pages/[lang]/opportunities/[id].astro");
  const frontier = read("src/pages/[lang]/frontier/index.astro");
  for (const token of ["research.opportunities", "candidate_evaluation", "interpretive layer", "timeline/"]) assert.ok(opportunities.includes(token), token);
  for (const token of ["why_it_matters", "current_coverage", "next_coordinate", "candidate_evaluation", "interpretive layer", "timeline/", "loadChineseSummaries"]) assert.ok(opportunity.includes(token), token);
  for (const token of ["frontierShifts", "recentItems", "freshness.discovery_scan_at", "genealogy", "Factual window", "Interpretive layer", "timeline/"]) assert.ok(frontier.includes(token), token);
});

test("filter URL status contract only admits states actually rendered by benchmark cards", () => {
  const filters = read("src/lib/filters.mjs");
  assert.ok(filters.includes('new Set(["tracked", "untracked"])'));
  assert.ok(!filters.includes('"live", "snapshot"'));
});

test("area pages inherit genealogy, results, opportunities, and frontier shifts", () => {
  const page = read("src/pages/[lang]/areas/[area].astro");
  for (const token of ["loadResearchModel", "loadAllResultSets", "genealogy", "opportunities", "frontierShifts"]) assert.ok(page.includes(token), token);
});
