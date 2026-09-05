import assert from "node:assert/strict";
import test from "node:test";

import { loadDeepRead, renderDeepReadMarkdown } from "../src/lib/deep-reads.mjs";

test("deep reads load authored bilingual benchmark notes", () => {
  const zh = loadDeepRead("mpbench", "zh");
  const en = loadDeepRead("mpbench", "en");
  assert.match(zh.markdown, /研究决策卡/);
  assert.match(en.markdown, /Research decision card/);
  assert.match(zh.html, /最有判别力的实验/);
  assert.match(en.html, /Most discriminating experiment/);
});

test("all canonical detail pages are source-authored rather than runtime padded", () => {
  for (const id of ["scale-qa", "wikisql", "dataspace", "bright", "locomo"]) {
    const zh = loadDeepRead(id, "zh");
    const en = loadDeepRead(id, "en");
    assert.match(zh.markdown, /研究决策卡/);
    assert.match(en.markdown, /Research decision card/);
    assert.doesNotMatch(zh.html, /规范评测契约/);
    assert.doesNotMatch(en.html, /Canonical evaluation contract/);
  }
});

test("deep read renderer escapes active markup and only links https sources", () => {
  const html = renderDeepReadMarkdown("# title\n\n<script>alert(1)</script>\n\nPrimary: https://example.com/paper");
  assert.doesNotMatch(html, /<script>/);
  assert.match(html, /&lt;script&gt;/);
  assert.match(html, /href=\"https:\/\/example.com\/paper\"/);
});
