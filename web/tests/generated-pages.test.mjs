import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import test from "node:test";

const read = (path) =>
  readFileSync(new URL(`../${path}`, import.meta.url), "utf8");

test("benchmark route generates every locale and stable registry id", () => {
  const page = read("src/pages/[lang]/benchmarks/[id].astro");

  assert.match(page, /LOCALES\.flatMap/);
  assert.match(page, /loadRegistry\(\)\.map/);
  assert.match(page, /params:\s*\{\s*lang,\s*id:\s*item\.id\s*\}/);
  assert.match(page, /<BenchmarkDetail/);
  assert.match(page, /Dataset/);
  assert.match(page, /CreativeWork/);
});

test("benchmark details expose auditable positive evidence without raw gap copy", () => {
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
