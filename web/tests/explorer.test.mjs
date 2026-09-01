import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import test from "node:test";

const read = (path) =>
  readFileSync(new URL(`../${path}`, import.meta.url), "utf8");

test("benchmark explorer statically loads the complete canonical registry", () => {
  const page = read("src/pages/[lang]/benchmarks/index.astro");

  assert.match(page, /getStaticPaths/);
  assert.match(page, /LOCALES\.map/);
  assert.match(page, /loadRegistry\(\)/);
  assert.match(page, /loadChineseSummaries\(\)/);
  assert.match(page, /<Explorer/);
  assert.match(page, /CollectionPage/);
});

test("benchmark cards expose filter metadata and positive public fields", () => {
  const card = read("src/components/BenchmarkCard.astro");

  for (const attribute of [
    "data-benchmark-id",
    "data-area",
    "data-role",
    "data-year",
    "data-artifacts",
    "data-capabilities",
    "data-environments",
    "data-protocols",
    "data-stable-facets",
    "data-result-status",
    "data-headroom-band",
  ]) {
    assert.ok(card.includes(attribute), attribute);
  }
  assert.ok(card.includes("item.summary"));
  assert.ok(!card.includes("coverage_gap"));
});

test("filter panel keeps primary controls compact and groups stable research facets", () => {
  const panel = read("src/components/FilterPanel.astro");

  for (const name of [
    "q",
    "area",
    "role",
    "artifact",
    "year",
    "facet",
    "status",
    "headroom",
    "metric",
    "tag",
    "sort",
  ]) {
    assert.match(panel, new RegExp(`name=["']${name}["']`));
  }
  assert.match(panel, /stableFacets/);
  assert.match(panel, /facet-disclosure/);
  assert.doesNotMatch(panel, /<select name="capability"/);
});

test("client controller keeps filter state in the URL and updates visible results", () => {
  const controller = read("src/scripts/explorer.mjs");

  for (const token of [
    "parseFilterState",
    "filterBenchmarks",
    "serializeFilterState",
    "sortBenchmarks",
    "history.replaceState",
    ".hidden",
  ]) {
    assert.ok(controller.includes(token), token);
  }
  assert.match(controller, /querySelector\(["']\[data-result-count\]["']\)/);
  assert.doesNotMatch(controller, /querySelector\(["']\[aria-live=/);
});
