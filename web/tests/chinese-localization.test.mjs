import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { join } from "node:path";
import test from "node:test";

import { localizeChineseHtml, localizeChineseProse, localizeTechnicalToken } from "../src/lib/chinese-localization.mjs";
import { copyFor } from "../src/lib/i18n.mjs";
import { displayToken } from "../src/lib/site.mjs";

const root = new URL("..", import.meta.url).pathname;

function source(path) {
  return readFileSync(join(root, path), "utf8");
}

test("Chinese prose localizer translates ordinary lowercase technical nouns but preserves canonical identifiers", () => {
  const input = "LoCoMo uses memory retrieval for each query with BM25 and MRR@10, then measures downstream utility.";
  const output = localizeChineseProse(input, "zh");
  assert.match(output, /LoCoMo/);
  assert.match(output, /BM25/);
  assert.match(output, /MRR@10/);
  assert.match(output, /记忆/);
  assert.match(output, /检索/);
  assert.match(output, /查询/);
  assert.match(output, /下游/);
  assert.match(output, /效用/);
  assert.doesNotMatch(output, /\bmemory\b|\bretrieval\b|\bquery\b|\bdownstream\b|\butility\b/);
});

test("Chinese HTML localizer leaves code spans untouched", () => {
  const output = localizeChineseHtml("<p>memory retrieval</p><code>memory retrieval</code>", "zh");
  assert.equal(output, "<p>记忆 检索</p><code>memory retrieval</code>");
});

test("common taxonomy tokens have Chinese display labels", () => {
  assert.equal(localizeTechnicalToken("temporal-reasoning", "zh", displayToken), "时间推理");
  assert.equal(localizeTechnicalToken("text-to-sql", "zh", displayToken), "Text-to-SQL");
  assert.equal(localizeTechnicalToken("temporal-reasoning", "en", displayToken), "temporal reasoning");
});

test("Chinese locale does not expose known English UI labels", () => {
  const zh = copyFor("zh");
  const values = [
    zh.nav.benchmarks,
    zh.hero.eyebrow,
    zh.hero.registry,
    zh.home.missionEyebrow,
    zh.home.latestEyebrow,
    zh.home.resultEyebrow,
    zh.home.opportunityEyebrow,
    zh.home.shiftEyebrow,
    zh.footer.data,
  ].join("\n");
  for (const forbidden of ["Benchmarks", "Evaluation frontier observatory", "Complete registry", "Three research decisions", "Latest verified releases", "Measured progress", "Next measurement coordinates", "Frontier shifts", "Machine-readable data"]) {
    assert.ok(!values.includes(forbidden), `Chinese locale contains English UI label: ${forbidden}`);
  }
});

test("core Chinese pages use explicit localized labels on the public content site", () => {
  const detail = source("src/components/BenchmarkDetail.astro");
  const results = source("src/components/ResultsPanel.astro");
  const home = source("src/pages/[lang]/index.astro");
  const explorer = source("src/pages/[lang]/benchmarks/index.astro");
  const suites = source("src/pages/[lang]/evaluate/index.astro");
  assert.match(detail, /supportEyebrow: "结论边界"/);
  assert.match(detail, /evidenceEyebrow: "证据摘要"/);
  assert.match(results, /eyebrow: "成绩进展"/);
  assert.match(home, /lang === "zh" \? "最新发布" : "Latest releases"/);
  assert.match(home, /lang === "zh" \? "研究信号" : "Research signals"/);
  assert.doesNotMatch(home, /网站待完善|Website under improvement/);
  assert.match(explorer, /lang === "zh" \? "基准筛选" : "Benchmark explorer"/);
  assert.match(suites, /lang === "zh" \? "评测组合" : "Evaluation suites"/);
});
