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
    "Research signals",
    'robots="index,follow"',
  ]) {
    assert.ok(page.includes(token), token);
  }
  for (const token of [
    "网站待完善",
    "Website under improvement",
    'robots="noindex,nofollow"',
    "wip-shell",
  ]) {
    assert.ok(!page.includes(token), token);
  }
});

test("primary navigation stays focused on the four repeat research actions", () => {
  const header = read("src/components/Header.astro");
  for (const token of ["benchmarks/", "#timeline", "evaluate/", "#results"]) {
    assert.ok(header.includes(token), token);
  }
  assert.ok(!header.includes('localePath(lang, "opportunities/")'));
  assert.ok(!header.includes('localePath(lang, "frontier/")'));
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

  for (const token of [
    "measurement_strength",
    "last_verified",
    "capabilities",
    "environment",
    "protocol",
    "artifacts",
    "citations",
  ]) {
    assert.ok(detail.includes(token), token);
  }
  assert.ok(!detail.includes("coverage_gap"));
  for (const token of ["scoreSupports", "comparisonControls", "nextValidation", "ResultsPanel", "deepRead", "benchmark-at-a-glance", "benchmark-setup-list", "summarizeTrack"]) {
    assert.ok(detail.includes(token), token);
  }
});

test("result panels bind visible scores to comparable tracks and primary sources", () => {
  const panel = read("src/components/ResultsPanel.astro");
  for (const token of ["summarizeTrack", "track.task", "track.split", "protocol_version", "entry.source", "metric.direction"]) {
    assert.ok(panel.includes(token), token);
  }
});

test("area pages provide six stable editorial landing pages", () => {
  const page = read("src/pages/[lang]/areas/[area].astro");

  assert.match(page, /LOCALES\.flatMap/);
  assert.match(page, /AREAS\.map/);
  assert.match(page, /CollectionPage/);
  assert.match(page, /BenchmarkCard/);
});

test("methodology pages explain the measurement model in both languages", () => {
  const page = read("src/pages/[lang]/methodology.astro");

  assert.match(page, /LOCALES\.map/);
  assert.match(page, /AboutPage/);
  assert.match(page, /measurement instrument/i);
  assert.match(page, /测量仪器/);
  assert.match(page, /Semantic Scholar/);
});

test("suite builder and comparison workspace expose reusable research decisions", () => {
  const evaluatePage = read("src/pages/[lang]/evaluate/index.astro");
  const evaluateScript = read("src/scripts/evaluate.mjs");
  const comparePage = read("src/pages/[lang]/compare/index.astro");

  for (const token of ["research.recipes", "claim_boundary", "next_validation", "data-suite-builder"]) assert.ok(evaluatePage.includes(token), token);
  for (const token of ["URLSearchParams", "recipe", "benchmark", "Markdown", "clipboard"]) assert.ok(evaluateScript.includes(token), token);
  for (const token of ["comparison_controls", "data-compare-workspace", "loadAllResultSets"]) assert.ok(comparePage.includes(token), token);
});

test("opportunity and frontier routes remain available as secondary research surfaces", () => {
  const opportunities = read("src/pages/[lang]/opportunities/index.astro");
  const opportunity = read("src/pages/[lang]/opportunities/[id].astro");
  const frontier = read("src/pages/[lang]/frontier/index.astro");

  for (const token of ["research.opportunities", "candidate_evaluation", "Opportunity map"]) assert.ok(opportunities.includes(token), token);
  for (const token of ["why_it_matters", "current_coverage", "next_coordinate", "candidate_evaluation"]) assert.ok(opportunity.includes(token), token);
  for (const token of ["frontierShifts", "recentItems", "freshness.discovery_scan_at", "genealogy", "Evaluation frontier"]) assert.ok(frontier.includes(token), token);
});

test("area pages inherit genealogy, results, opportunities, and frontier shifts", () => {
  const page = read("src/pages/[lang]/areas/[area].astro");
  for (const token of ["loadResearchModel", "loadAllResultSets", "genealogy", "opportunities", "frontierShifts"]) assert.ok(page.includes(token), token);
});
