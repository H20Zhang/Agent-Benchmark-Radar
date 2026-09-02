import { existsSync, readFileSync, readdirSync } from "node:fs";
import { join } from "node:path";

import { loadChineseSummaries } from "./readme-localization.mjs";
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
  return JSON.parse(readFileSync(fromRepositoryRoot("data", ...segments), "utf8"));
}

function assertLocalized(value, field) {
  if (!value || typeof value.zh !== "string" || typeof value.en !== "string") {
    throw new Error(`${field} must contain zh and en strings`);
  }
  if (!value.zh.trim() || !value.en.trim()) throw new Error(`${field} cannot be empty`);
}

function assertUnique(items, label) {
  const ids = new Set();
  for (const item of items) {
    if (!item.id || ids.has(item.id)) throw new Error(`${label} has invalid or duplicate id: ${item.id}`);
    ids.add(item.id);
  }
}

function humanizeToken(value) {
  return String(value || "").replaceAll("-", " ");
}

function defaultEditorial(item, chineseSummary) {
  const areaValidation = {
    "agent-memory": {
      zh: "建议结合行动、长期用户状态与生命周期评测，形成覆盖完整的 Memory 证据链。",
      en: "Pair with action, long-term user-state, and lifecycle evaluation to complete the memory evidence chain.",
    },
    rag: {
      zh: "建议结合实时证据、搜索轨迹与语料变化评测，形成覆盖完整的 Retrieval 证据链。",
      en: "Pair with live evidence, search-trajectory, and corpus-change evaluation to complete the retrieval evidence chain.",
    },
    "data-agent": {
      zh: "建议结合完整工作流、业务语义与执行质量评测，形成覆盖完整的 Data Agent 证据链。",
      en: "Pair with complete-workflow, business-semantic, and execution-quality evaluation to complete the data-agent evidence chain.",
    },
  }[item.area];
  const role = {
    precursor: { zh: "历史参照", en: "Historical reference" },
    foundation: { zh: "基础能力锚点", en: "Foundation anchor" },
    transition: { zh: "演进转折点", en: "Transition benchmark" },
    frontier: { zh: "前沿测量坐标", en: "Frontier measurement coordinate" },
  }[item.evolution_role];

  const measurement = item.measurement_strength || item.summary;
  const inferenceBoundary = item.coverage_gap || areaValidation.en;
  const confounders = (item.confounders || []).map(humanizeToken).filter(Boolean);
  const confounderText = confounders.join(", ");
  const confounderTextZh = confounders.join("、");
  const benchmarkSpecificControl = confounders.length
    ? {
        zh: `这项评测尤其需要固定或完整报告这些 load-bearing 条件：${confounderTextZh}。否则分数差异只能视为 system-level evidence。`,
        en: `This benchmark is especially sensitive to these load-bearing conditions: ${confounderText}. If they differ, score gaps are system-level evidence rather than component attribution.`,
      }
    : {
        zh: "完整报告模型、工具、harness、预算与 evaluator；存在差异时只做系统级比较。",
        en: "Report model, tools, harness, budget, and evaluator completely; treat mismatches as system-level comparisons only.",
      };

  return {
    id: item.id,
    score_supports: {
      zh: `这个分数首先支持对该测量对象的判断：${measurement} 只有在模型、工具、资源预算和协议充分对齐后，才适合比较系统差异；分数本身不能识别收益来自哪个内部组件。`,
      en: `The score first supports a claim about this measurement object: ${measurement} Under sufficiently matched model, tools, resource budget, and protocol, it can compare systems; by itself it does not identify which internal component caused a gain.`,
    },
    suite_role: role,
    next_validation: {
      zh: item.coverage_gap
        ? `当前最有判别力的下一评测坐标是：${item.coverage_gap}`
        : areaValidation.zh,
      en: item.coverage_gap
        ? `The next discriminating evaluation coordinate is: ${item.coverage_gap}`
        : areaValidation.en,
    },
    evidence_brief: {
      zh: `这项 benchmark 的核心测量增量是：${measurement} 当前推断边界是：${inferenceBoundary}${confounders.length ? ` 公平比较最敏感的条件包括 ${confounderTextZh}。` : ""}`,
      en: `The benchmark's core measurement advance is: ${measurement} Its current inference boundary is: ${inferenceBoundary}${confounders.length ? ` Fair comparison is especially sensitive to ${confounderText}.` : ""}`,
    },
    comparison_controls: [
      {
        zh: "对齐模型版本、可访问状态、工具接口、提示方式、重试/停止规则与资源预算。",
        en: "Align model version, accessible state, tool interface, prompting, retry/stopping rules, and resource budget.",
      },
      benchmarkSpecificControl,
      {
        zh: "使用相同任务切分、评测协议、指标定义、evaluator 与环境版本；若任一项变化，单独报告。",
        en: "Use the same task split, evaluation protocol, metric definition, evaluator, and environment version; report any mismatch separately.",
      },
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
    evaluation_contract: { ...base.evaluation_contract, ...(overlay.evaluation_contract || {}) },
    comparison_controls: overlay.comparison_controls || base.comparison_controls,
  };
}

function loadEditorial(registry) {
  const chinese = loadChineseSummaries();
  const directory = fromRepositoryRoot("data", "editorial", "benchmarks");
  const overlays = new Map();
  if (existsSync(directory)) {
    for (const filename of readdirSync(directory).filter((name) => name.endsWith(".json")).sort()) {
      const record = JSON.parse(readFileSync(join(directory, filename), "utf8"));
      overlays.set(record.id, record);
    }
  }

  return new Map(
    registry.map((item) => {
      const base = defaultEditorial(item, chinese.get(item.id) || item.summary);
      const editorial = mergeEditorial(base, overlays.get(item.id) || {});
      for (const field of ["score_supports", "suite_role", "next_validation", "evidence_brief"]) {
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
    if (!benchmarkIds.has(id)) throw new Error(`${owner} references unknown benchmark ${id}`);
  };

  assertUnique(model.taxonomy.facets, "taxonomy facets");
  assertUnique(model.recipes, "recipes");
  assertUnique(model.opportunities, "opportunities");
  assertUnique(model.frontierShifts, "frontier shifts");

  for (const recipe of model.recipes) {
    if (!AREAS.has(recipe.area)) throw new Error(`${recipe.id} has invalid area`);
    for (const field of ["claim", "claim_boundary", "next_validation"]) assertLocalized(recipe[field], `${recipe.id}.${field}`);
    for (const id of [...recipe.core, ...recipe.complement]) check(id, recipe.id);
  }
  for (const opportunity of model.opportunities) {
    if (!AREAS.has(opportunity.area)) throw new Error(`${opportunity.id} has invalid area`);
    for (const field of ["title", "why_it_matters", "current_coverage", "next_coordinate", "candidate_evaluation"]) {
      assertLocalized(opportunity[field], `${opportunity.id}.${field}`);
    }
    for (const id of opportunity.benchmarks) check(id, opportunity.id);
  }
  for (const shift of model.frontierShifts) {
    if (!AREAS.has(shift.area)) throw new Error(`${shift.id} has invalid area`);
    for (const field of ["title", "delta", "consequence"]) assertLocalized(shift[field], `${shift.id}.${field}`);
    for (const id of shift.benchmarks) check(id, shift.id);
  }
  for (const area of model.genealogy.areas) {
    if (!AREAS.has(area.id)) throw new Error(`genealogy has invalid area ${area.id}`);
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
  const raw = Object.fromEntries(Object.entries(DATA_FILES).map(([key, filename]) => [key, readJson(filename)]));
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
    comparisonControls: editorial.comparison_controls.map((item) => localize(item, lang)),
  };
}

function searchableText(item) {
  return [
    item.name,
    item.summary,
    item.measurement_strength,
    item.scale,
    ...(item.capabilities || []),
    ...(item.environment || []),
    ...(item.protocol || []),
  ].join(" ").toLocaleLowerCase();
}

export function getStableFacets(items) {
  const taxonomy = loadResearchModel().taxonomy;
  return taxonomy.facets.map((facet) => ({
    ...facet,
    options: facet.options
      .map((option) => ({
        ...option,
        count: items.filter((item) => {
          if (facet.area && item.area !== facet.area) return false;
          const text = searchableText(item);
          return option.match.some((token) => text.includes(token.toLocaleLowerCase()));
        }).length,
      }))
      .filter((option) => option.count > 0),
  }));
}

export function getStableFacetValues(item) {
  const text = searchableText(item);
  return loadResearchModel().taxonomy.facets.flatMap((facet) => {
    if (facet.area && facet.area !== item.area) return [];
    return facet.options
      .filter((option) => option.match.some((token) => text.includes(token.toLocaleLowerCase())))
      .map((option) => option.id);
  });
}
