import { existsSync, readFileSync, readdirSync } from "node:fs";
import { join } from "node:path";

import { loadChineseSummaries } from "./readme-localization.mjs";
import { getAuthoredBrief } from "./deep-reads.mjs";
import { loadRegistry } from "./registry.mjs";
import { fromRepositoryRoot } from "./repository-path.mjs";

const AREAS = new Set(["agent-memory", "rag", "data-agent"]);
const DATA_FILES = {
  taxonomy: "taxonomy.json",
  recipes: "recipes.json",
  genealogy: "genealogy.json",
  opportunities: "opportunities.json",
  frontierShifts: "frontier_shifts.json",
};

let researchCache;

function readJson(...segments) {
  return JSON.parse(
    readFileSync(fromRepositoryRoot("data", ...segments), "utf8"),
  );
}

function assertLocalized(value, field) {
  if (!value || typeof value.zh !== "string" || typeof value.en !== "string") {
    throw new Error(`${field} must contain zh and en strings`);
  }
  if (!value.zh.trim() || !value.en.trim())
    throw new Error(`${field} cannot be empty`);
}

function assertUnique(items, label) {
  const ids = new Set();
  for (const item of items) {
    if (!item.id || ids.has(item.id))
      throw new Error(`${label} has invalid or duplicate id: ${item.id}`);
    ids.add(item.id);
  }
}

function humanizeToken(value) {
  return String(value || "").replaceAll("-", " ");
}

function defaultEditorial(item, chineseSummary) {
  const zh = getAuthoredBrief(item.id, "zh");
  const en = getAuthoredBrief(item.id, "en");
  // Authored notes own interpretation. The registry still owns measurement_strength,
  // item.coverage_gap and item.confounders; missing translations are not manufactured.
  const genericZh =
    "这是系统级评测证据；组件归因仍需要固定模型、工具、预算和评判器后进行消融。";
  const genericEn =
    "This is system-level evidence; component attribution requires controlled ablations with matched models, tools, budgets, and evaluators.";
  return {
    id: item.id,
    score_supports: {
      zh: zh.supports || genericZh,
      en: en.supports || genericEn,
    },
    suite_role: { zh: "按测量对象选择", en: "Select by measurement target" },
    next_validation: {
      zh: zh.next || "具体实验建议见下方研究解读。",
      en:
        en.next ||
        "See the authored research interpretation for the next experiment.",
    },
    evidence_brief: {
      zh: zh.why || chineseSummary,
      en: en.why || item.summary,
    },
    example: { zh: zh.example, en: en.example },
    comparison_controls: [
      { zh: zh.controls || genericZh, en: en.controls || genericEn },
    ],
    evaluation_contract: {
      target: { zh: chineseSummary, en: item.summary },
      environment: item.environment || [],
      protocol: item.protocol || [],
      scale: item.scale,
    },
  };
}

function mergeEditorial(base, overlay) {
  return {
    ...base,
    ...overlay,
    evaluation_contract: {
      ...base.evaluation_contract,
      ...(overlay.evaluation_contract || {}),
    },
    comparison_controls:
      overlay.comparison_controls || base.comparison_controls,
  };
}

function loadEditorial(registry) {
  const chinese = loadChineseSummaries();
  const directory = fromRepositoryRoot("data", "editorial", "benchmarks");
  const overlays = new Map();
  if (existsSync(directory)) {
    for (const filename of readdirSync(directory)
      .filter((name) => name.endsWith(".json"))
      .sort()) {
      const record = JSON.parse(
        readFileSync(join(directory, filename), "utf8"),
      );
      overlays.set(record.id, record);
    }
  }

  return new Map(
    registry.map((item) => {
      const base = defaultEditorial(item, chinese.get(item.id) || item.summary);
      const editorial = mergeEditorial(base, overlays.get(item.id) || {});
      for (const field of [
        "score_supports",
        "suite_role",
        "next_validation",
        "evidence_brief",
      ]) {
        assertLocalized(editorial[field], `${item.id}.${field}`);
      }
      for (const [index, control] of editorial.comparison_controls.entries()) {
        assertLocalized(control, `${item.id}.comparison_controls[${index}]`);
      }
      return [item.id, Object.freeze(editorial)];
    }),
  );
}

function validateReferences(model, registry) {
  const benchmarkIds = new Set(registry.map((item) => item.id));
  const check = (id, owner) => {
    if (!benchmarkIds.has(id))
      throw new Error(`${owner} references unknown benchmark ${id}`);
  };

  assertUnique(model.taxonomy.facets, "taxonomy facets");
  const facetIds = new Map(
    model.taxonomy.facets.map((f) => [
      f.id,
      new Set(f.options.map((o) => o.id)),
    ]),
  );
  for (const facet of model.taxonomy.facets)
    assertUnique(facet.options, `${facet.id} options`);
  for (const item of registry)
    for (const [facet, options] of Object.entries(
      item.facet_assignments || {},
    )) {
      if (
        !facetIds.has(facet) ||
        options.some((option) => !facetIds.get(facet).has(option))
      )
        throw new Error(`Invalid facet assignment: ${item.id}/${facet}`);
    }
  assertUnique(model.recipes, "recipes");
  assertUnique(model.opportunities, "opportunities");
  assertUnique(model.frontierShifts, "frontier shifts");

  for (const recipe of model.recipes) {
    if (!AREAS.has(recipe.area))
      throw new Error(`${recipe.id} has invalid area`);
    for (const field of ["claim", "claim_boundary", "next_validation"])
      assertLocalized(recipe[field], `${recipe.id}.${field}`);
    for (const id of [...recipe.core, ...recipe.complement])
      check(id, recipe.id);
  }
  for (const opportunity of model.opportunities) {
    if (!AREAS.has(opportunity.area))
      throw new Error(`${opportunity.id} has invalid area`);
    for (const field of [
      "title",
      "why_it_matters",
      "current_coverage",
      "next_coordinate",
      "candidate_evaluation",
    ]) {
      assertLocalized(opportunity[field], `${opportunity.id}.${field}`);
    }
    for (const id of opportunity.benchmarks) check(id, opportunity.id);
  }
  for (const shift of model.frontierShifts) {
    if (!AREAS.has(shift.area)) throw new Error(`${shift.id} has invalid area`);
    for (const field of ["title", "delta", "consequence"])
      assertLocalized(shift[field], `${shift.id}.${field}`);
    for (const id of shift.benchmarks) check(id, shift.id);
  }
  for (const area of model.genealogy.areas) {
    if (!AREAS.has(area.id))
      throw new Error(`genealogy has invalid area ${area.id}`);
    assertLocalized(area.thesis, `${area.id}.thesis`);
    assertUnique(area.stages, `${area.id} stages`);
    for (const stage of area.stages) {
      assertLocalized(stage.label, `${stage.id}.label`);
      for (const id of stage.benchmarks) check(id, stage.id);
    }
  }
}

export function localize(value, lang) {
  if (typeof value === "string") return value;
  return value?.[lang] || value?.en || "";
}

export function loadResearchModel() {
  if (researchCache) return researchCache;
  const registry = loadRegistry();
  const raw = Object.fromEntries(
    Object.entries(DATA_FILES).map(([key, filename]) => [
      key,
      readJson(filename),
    ]),
  );
  const model = {
    ...raw,
    benchmarkEditorial: loadEditorial(registry),
  };
  validateReferences(model, registry);
  researchCache = Object.freeze(model);
  return researchCache;
}

export function getBenchmarkResearch(id, lang = "en") {
  const editorial = loadResearchModel().benchmarkEditorial.get(id);
  if (!editorial) return undefined;
  return {
    ...editorial,
    scoreSupports: localize(editorial.score_supports, lang),
    suiteRole: localize(editorial.suite_role, lang),
    nextValidation: localize(editorial.next_validation, lang),
    evidenceBrief: localize(editorial.evidence_brief, lang),
    comparisonControls: editorial.comparison_controls.map((item) =>
      localize(item, lang),
    ),
  };
}

/** Explicit facet membership: prose edits must not silently change classifications. */
export function getStableFacets(items) {
  const taxonomy = loadResearchModel().taxonomy;
  return taxonomy.facets.map((facet) => ({
    ...facet,
    options: facet.options
      .map((option) => ({
        ...option,
        key: `${facet.id}:${option.id}`,
        count: items.filter((item) =>
          item.facet_assignments?.[facet.id]?.includes(option.id),
        ).length,
      }))
      .filter((option) => option.count > 0),
  }));
}
export function getStableFacetValues(item) {
  return Object.entries(item.facet_assignments || {}).flatMap(
    ([facet, options]) => options.map((option) => `${facet}:${option}`),
  );
}
