import assert from "node:assert/strict";
import test from "node:test";

import { loadRegistry } from "../src/lib/registry.mjs";
import {
  getStableFacetValues,
  getStableFacets,
  loadResearchModel,
  localize,
} from "../src/lib/research-model.mjs";

test("research objects reference canonical benchmark ids", () => {
  const model = loadResearchModel();
  const ids = new Set(loadRegistry().map((item) => item.id));

  for (const recipe of model.recipes) {
    for (const id of [...recipe.core, ...recipe.complement]) {
      assert.ok(ids.has(id), `${recipe.id} references ${id}`);
    }
  }
  for (const opportunity of model.opportunities) {
    for (const id of opportunity.benchmarks) {
      assert.ok(ids.has(id), `${opportunity.id} references ${id}`);
    }
  }
  for (const area of model.genealogy.areas) {
    for (const stage of area.stages) {
      for (const id of stage.benchmarks) assert.ok(ids.has(id), `${area.id} references ${id}`);
    }
  }
});

test("stable facet values map registry records to low-cardinality research controls", () => {
  const item = loadRegistry().find((entry) => entry.id === "locomo");
  const values = getStableFacetValues(item);

  assert.ok(values.includes("memory-recall"));
  assert.ok(values.includes("conversation"));
  assert.equal(values.length, new Set(values).size);
});

test("research model has symmetric bilingual fields", () => {
  const model = loadResearchModel();
  const localized = [
    ...model.recipes.flatMap((item) => [item.claim, item.claim_boundary, item.next_validation]),
    ...model.opportunities.flatMap((item) => [item.title, item.why_it_matters, item.next_coordinate]),
    ...model.frontierShifts.flatMap((item) => [item.title, item.delta, item.consequence]),
  ];

  for (const value of localized) {
    assert.equal(typeof localize(value, "zh"), "string");
    assert.equal(typeof localize(value, "en"), "string");
    assert.ok(value.zh.length > 3);
    assert.ok(value.en.length > 3);
  }
});

test("stable taxonomy stays within the interaction budget", () => {
  const facets = getStableFacets(loadRegistry());
  assert.ok(facets.length >= 4);
  assert.ok(facets.every((facet) => facet.options.length <= 12));
  assert.ok(facets.every((facet) => facet.options.every((option) => option.count > 0)));
});

test("canonical editorial records enrich every benchmark", () => {
  const model = loadResearchModel();
  const registry = loadRegistry();
  assert.equal(model.benchmarkEditorial.size, registry.length);

  for (const item of registry) {
    const editorial = model.benchmarkEditorial.get(item.id);
    assert.ok(editorial, item.id);
    assert.ok(localize(editorial.score_supports, "zh").length > 8);
    assert.ok(localize(editorial.next_validation, "en").length > 8);
    assert.ok(editorial.comparison_controls.length > 0);
  }
});
