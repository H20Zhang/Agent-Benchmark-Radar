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

test("deep read renderer escapes active markup and only links https sources", () => {
  const html = renderDeepReadMarkdown("# title\n\n<script>alert(1)</script>\n\nPrimary: https://example.com/paper");

  assert.doesNotMatch(html, /<script>/);
  assert.match(html, /&lt;script&gt;/);
  assert.match(html, /href="https:\/\/example.com\/paper"/);
});
