import assert from "node:assert/strict";
import test from "node:test";

import { loadDeepRead, renderDeepReadMarkdown } from "../src/lib/deep-reads.mjs";

test("deep reads load the matching bilingual benchmark note", () => {
  const zh = loadDeepRead("mpbench", "zh");
  const en = loadDeepRead("mpbench", "en");

  assert.match(zh.markdown, /测量对象/);
  assert.match(en.markdown, /Measurement object/);
  assert.doesNotMatch(zh.html, /<h1/);
  assert.match(zh.html, /<ul>/);
});

test("thin deep reads are completed from the canonical registry without mutating source markdown", () => {
  const zh = loadDeepRead("vakra", "zh");
  const en = loadDeepRead("vakra", "en");

  assert.equal(zh.canonicalAppendixAdded, true);
  assert.equal(en.canonicalAppendixAdded, true);
  assert.doesNotMatch(zh.markdown, /规范评测契约/);
  assert.match(zh.html, /规范评测契约/);
  assert.match(zh.html, /Protocol cell/);
  assert.match(en.html, /Canonical evaluation contract/);
  assert.match(en.html, /Fair comparison and main confounders/);
});

test("mature deep reads are preserved rather than padded with duplicate boilerplate", () => {
  const zh = loadDeepRead("lifeside", "zh");
  const en = loadDeepRead("lifeside", "en");

  assert.equal(zh.canonicalAppendixAdded, false);
  assert.equal(en.canonicalAppendixAdded, false);
  assert.doesNotMatch(zh.html, /规范评测契约/);
  assert.doesNotMatch(en.html, /Canonical evaluation contract/);
});

test("deep read renderer escapes active markup and only links https sources", () => {
  const html = renderDeepReadMarkdown("# title\n\n<script>alert(1)</script>\n\nPrimary: https://example.com/paper");

  assert.doesNotMatch(html, /<script>/);
  assert.match(html, /&lt;script&gt;/);
  assert.match(html, /href="https:\/\/example.com\/paper"/);
});
