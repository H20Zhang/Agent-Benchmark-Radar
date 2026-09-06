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

test("prose remains immutable; localization only labels structured tokens", () => {
  const input = "LoCoMo uses memory retrieval. 这些能力尚未覆盖。";
  assert.equal(localizeChineseProse(input, "zh"), input);
  const html = "<p>memory retrieval 尚未覆盖</p><code>memory</code>";
  assert.equal(localizeChineseHtml(html, "zh"), html);
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

test("authored Chinese next experiments are reused rather than masked as missing", async () => {
  const { getAuthoredBrief } = await import("../src/lib/deep-reads.mjs");
  const { loadRegistry } = await import("../src/lib/registry.mjs");
  for (const item of loadRegistry()) {
    assert.ok(getAuthoredBrief(item.id, "zh").next, `${item.id} next experiment`);
  }
});
