import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import test from "node:test";

import { copyFor, LOCALES } from "../src/lib/i18n.mjs";
import { absoluteUrl, sitePath } from "../src/lib/site.mjs";

const read = (path) =>
  readFileSync(new URL(`../${path}`, import.meta.url), "utf8");

test("sitePath prefixes the GitHub project base exactly once", () => {
  assert.equal(sitePath("/zh/"), "/Agent-Benchmark-Radar/zh/");
  assert.equal(
    sitePath("/Agent-Benchmark-Radar/en/"),
    "/Agent-Benchmark-Radar/en/",
  );
  assert.equal(
    absoluteUrl("/zh/"),
    "https://h20zhang.github.io/Agent-Benchmark-Radar/zh/",
  );
});

test("locales expose symmetric positive navigation copy", () => {
  assert.deepEqual(LOCALES, ["zh", "en"]);
  assert.equal(copyFor("zh").nav.benchmarks, "Benchmarks");
  assert.equal(copyFor("en").nav.benchmarks, "Benchmarks");
  assert.equal(copyFor("zh").nav.opportunities, "评测机会");
  assert.equal(copyFor("en").nav.opportunities, "Opportunities");
  assert.throws(() => copyFor("fr"), /Unsupported locale/);
});

test("Astro configuration locks the project Pages base and sitemap", () => {
  const config = read("astro.config.mjs");
  const pkg = JSON.parse(read("package.json"));

  assert.match(config, /site:\s*["']https:\/\/h20zhang\.github\.io["']/);
  assert.match(config, /base:\s*["']\/Agent-Benchmark-Radar["']/);
  assert.match(config, /sitemap\(/);
  assert.equal(pkg.dependencies.astro, "7.2.10");
  assert.equal(pkg.dependencies["@astrojs/sitemap"], "3.7.4");
});

test("base layout owns canonical, hreflang, social, and JSON-LD metadata", () => {
  const layout = read("src/layouts/BaseLayout.astro");

  for (const token of [
    'rel="canonical"',
    'hreflang="zh-CN"',
    'hreflang="en"',
    'hreflang="x-default"',
    'property="og:title"',
    'property="og:image"',
    'name="twitter:card"',
    "summary_large_image",
    'type="application/ld+json"',
  ]) {
    assert.ok(layout.includes(token), token);
  }
});

test("root entry is a visible noindex language handoff", () => {
  const page = read("src/pages/index.astro");

  assert.match(page, /robots="noindex,follow"/);
  assert.match(page, /http-equiv="refresh"/);
  assert.match(page, />中文</);
  assert.match(page, />English</);
});
