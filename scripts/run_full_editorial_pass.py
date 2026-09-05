#!/usr/bin/env python3
"""Finish the one-shot editorial migration and write regression tests."""
from __future__ import annotations

import json
import re
from pathlib import Path

from apply_full_editorial_pass import main as apply_pass

ROOT = Path(__file__).resolve().parents[1]

RENDERER = r'''import { existsSync, readFileSync } from "node:fs";
import { fromRepositoryRoot } from "./repository-path.mjs";
import { loadRegistry } from "./registry.mjs";
import { localePath, sitePath } from "./site.mjs";

function escapeHtml(value) {
  return String(value).replaceAll("&", "&amp;").replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;").replaceAll('"', "&quot;").replaceAll("'", "&#39;");
}

function safeHref(value) {
  const href = value.trim();
  if (/^https:\/\//i.test(href)) {
    try { const parsed = new URL(href); return parsed.protocol === "https:" ? parsed.href : undefined; }
    catch { return undefined; }
  }
  if (/^#[\p{L}\p{N}_-]+$/u.test(href)) return href;
  const note = /^([a-z0-9][a-z0-9-]*)(\.en)?\.md(#[\p{L}\p{N}_-]+)?$/u.exec(href);
  if (note && loadRegistry().some((item) => item.id === note[1])) {
    return sitePath(localePath(note[2] ? "en" : "zh", `benchmarks/${note[1]}/`)) + (note[3] || "");
  }
  const readme = /^\.\.\/README(\.en)?\.md(#[a-z0-9-]+)?$/.exec(href);
  if (readme) return `https://github.com/H20Zhang/Agent-Benchmark-Radar/blob/main/README${readme[1] || ""}.md${readme[2] || ""}`;
  if (/^\.\.\/(?:library\/README(?:\.en)?\.md|CURATION\.md|SCHEMA\.md)(#[a-z0-9-]+)?$/.test(href)) {
    return "https://github.com/H20Zhang/Agent-Benchmark-Radar/blob/main/" + href.slice(3);
  }
  return undefined;
}

function inlineMarkdown(text) {
  // Parse supported tokens before escaping text; never link or format inside code.
  const pattern = /`([^`\n]+)`|\[([^\]\n]+)\]\(([^\s)]+)\)|\*\*([^*\n]+)\*\*|https:\/\/[^\s<>"'`]+/g;
  let output = "", previous = 0;
  for (const match of text.matchAll(pattern)) {
    output += escapeHtml(text.slice(previous, match.index));
    if (match[1] !== undefined) output += `<code>${escapeHtml(match[1])}</code>`;
    else if (match[2] !== undefined) {
      const href = safeHref(match[3]);
      const label = escapeHtml(match[2]);
      output += href ? `<a href="${escapeHtml(href)}" rel="noreferrer">${label}</a>` : label;
    } else if (match[4] !== undefined) output += `<strong>${escapeHtml(match[4])}</strong>`;
    else {
      const url = match[0].replace(/[.,;，。；]+$/, "");
      const punctuation = match[0].slice(url.length);
      const href = safeHref(url);
      output += (href ? `<a href="${escapeHtml(href)}" rel="noreferrer">${escapeHtml(url)}</a>` : escapeHtml(url)) + escapeHtml(punctuation);
    }
    previous = match.index + match[0].length;
  }
  return output + escapeHtml(text.slice(previous));
}

function cells(line) {
  return line.trim().replace(/^\|/, "").replace(/\|$/, "").split(/(?<!\\)\|/).map((part) => part.trim().replaceAll("\\|", "|"));
}

export function renderDeepReadMarkdown(markdown) {
  const lines = String(markdown).replaceAll("\r\n", "\n").replace(/<!--[\s\S]*?-->/g, "").split("\n");
  const output = [];
  const ids = new Map();
  let paragraph = [], list = [], listType = "ul", code = [], fence;
  const flushParagraph = () => {
    if (paragraph.length) output.push(`<p>${inlineMarkdown(paragraph.join(" "))}</p>`);
    paragraph = [];
  };
  const flushList = () => {
    if (list.length) output.push(`<${listType}>${list.map((line) => `<li>${inlineMarkdown(line)}</li>`).join("")}</${listType}>`);
    list = [];
  };
  const flush = () => { flushParagraph(); flushList(); };
  for (let index = 0; index < lines.length; index++) {
    const line = lines[index];
    if (fence) {
      if (line.trim().startsWith(fence)) {
        output.push(`<pre><code>${escapeHtml(code.join("\n"))}</code></pre>`); code = []; fence = undefined;
      } else code.push(line);
      continue;
    }
    const fenced = /^\s*(`{3,}|~{3,})/.exec(line);
    if (fenced) { flush(); fence = fenced[1]; continue; }
    const heading = /^(#{1,6})\s+(.+)$/.exec(line);
    const bullet = /^\s*(?:([-*])|\d+\.)\s+(.+)$/.exec(line);
    if (heading) {
      flush();
      if (heading[1].length === 1) continue;
      const level = Math.min(heading[1].length, 4);
      const slug = heading[2].toLowerCase().replace(/[^\p{L}\p{N}\s_-]/gu, "").trim().replace(/\s+/g, "-") || "section";
      const count = ids.get(slug) || 0; ids.set(slug, count + 1);
      output.push(`<h${level} id="${escapeHtml(slug + (count ? `-${count}` : ""))}">${inlineMarkdown(heading[2])}</h${level}>`);
    } else if (line.includes("|") && index + 1 < lines.length && /^\s*\|?\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)+\|?\s*$/.test(lines[index + 1])) {
      flush(); const headers = cells(line); const rows = []; index++;
      while (index + 1 < lines.length && lines[index + 1].trim().startsWith("|")) rows.push(cells(lines[++index]));
      output.push(`<div class="deep-read-table"><table><thead><tr>${headers.map((cell) => `<th scope="col">${inlineMarkdown(cell)}</th>`).join("")}</tr></thead><tbody>${rows.map((row) => `<tr>${headers.map((_, column) => `<td>${inlineMarkdown(row[column] || "")}</td>`).join("")}</tr>`).join("")}</tbody></table></div>`);
    } else if (/^\s*(?:-{3,}|\*{3,}|_{3,})\s*$/.test(line)) { flush(); output.push("<hr>"); }
    else if (/^>\s?/.test(line)) { flush(); output.push(`<blockquote><p>${inlineMarkdown(line.replace(/^>\s?/, ""))}</p></blockquote>`); }
    else if (bullet) {
      flushParagraph(); const type = bullet[1] ? "ul" : "ol";
      if (list.length && type !== listType) flushList();
      listType = type; list.push(bullet[2]);
    } else if (!line.trim()) flush();
    else { flushList(); paragraph.push(line.trim()); }
  }
  flush();
  if (fence) output.push(`<pre><code>${escapeHtml(code.join("\n"))}</code></pre>`);
  return output.join("\n");
}

export function loadDeepRead(id, lang) {
  if (!/^[a-z0-9][a-z0-9-]*$/.test(id) || !["zh", "en"].includes(lang)) return undefined;
  const filename = `${id}${lang === "en" ? ".en" : ""}.md`;
  const path = fromRepositoryRoot("benchmarks", filename);
  if (!existsSync(path)) return undefined;
  const markdown = readFileSync(path, "utf8");
  return { id, lang, markdown, html: renderDeepReadMarkdown(markdown), canonicalAppendixAdded: false };
}
'''

TESTS = r'''import assert from "node:assert/strict";
import test from "node:test";
import { readFileSync } from "node:fs";
import { loadDeepRead, renderDeepReadMarkdown } from "../src/lib/deep-reads.mjs";
import { loadRegistry } from "../src/lib/registry.mjs";
import { fromRepositoryRoot } from "../src/lib/repository-path.mjs";

test("every canonical note contains the authored judgment, illustration and experiment exactly once", () => {
  const guides = new Map(JSON.parse(readFileSync(fromRepositoryRoot("data", "editorial", "reading_guides.json"), "utf8")).map((item) => [item.id, item]));
  assert.equal(guides.size, loadRegistry().length);
  for (const item of loadRegistry()) for (const lang of ["zh", "en"]) {
    const note = loadDeepRead(item.id, lang);
    assert.ok(note, `${item.id}/${lang}`);
    assert.equal(note.canonicalAppendixAdded, false);
    for (const field of ["judgment", "example", "experiment"]) {
      const value = guides.get(item.id)[field][lang];
      assert.equal(note.markdown.split(value).length - 1, 1, `${item.id}/${lang}/${field}`);
    }
    assert.doesNotMatch(note.html, /Canonical evaluation contract|规范评测契约|EDITORIAL-GUIDE|<h1/);
    assert.match(note.html, /<h2/);
  }
});

test("unsafe source markup and URL schemes cannot become active content", () => {
  const html = renderDeepReadMarkdown('# title\n\n<script>alert(1)</script>\n\n[bad](javascript:alert) [bad2](data:text/html,evil) [safe](https://example.com/paper)');
  assert.doesNotMatch(html, /<script>|href="javascript:|href="data:/);
  assert.match(html, /&lt;script&gt;/);
  assert.match(html, /href="https:\/\/example.com\/paper"/);
});

test("related benchmark links resolve to locale-specific Pages routes", () => {
  const html = renderDeepReadMarkdown('[中文](beir.md) [English](beir.en.md)');
  assert.match(html, /\/zh\/benchmarks\/beir\//);
  assert.match(html, /\/en\/benchmarks\/beir\//);
  assert.doesNotMatch(html, /href="beir/);
});

test("tables, fenced code and comments are rendered without leaking Markdown chrome", () => {
  const html = renderDeepReadMarkdown('<!-- private editorial marker -->\n\n| A | B |\n|---|---|\n| x | y |\n\n```\n<script>literal</script>\n```');
  assert.match(html, /<table>/);
  assert.match(html, /<th scope="col">A<\/th>/);
  assert.match(html, /<pre><code>&lt;script&gt;literal/);
  assert.doesNotMatch(html, /private editorial marker|<script>/);
});

test("prose scope is not changed by global replacements", () => {
  const html = renderDeepReadMarkdown('当前仍未覆盖真实部署；结论上限需要根据证据判断。');
  assert.match(html, /仍未覆盖真实部署/);
  assert.match(html, /结论上限/);
});
'''


def main() -> None:
    apply_pass()
    (ROOT / "web/src/lib/deep-reads.mjs").write_text(RENDERER, encoding="utf-8")
    (ROOT / "web/tests/deep-reads.test.mjs").write_text(TESTS, encoding="utf-8")
    registry = json.loads((ROOT / "data/benchmarks.json").read_text(encoding="utf-8"))
    for item in registry:
        for lang, suffix in (("zh", ".md"), ("en", ".en.md")):
            path = ROOT / "benchmarks" / (item["id"] + suffix)
            text = path.read_text(encoding="utf-8")
            # The new experiment replaces the prior forward-looking advice; source
            # evidence, measurement and limitations remain in the note.
            text = re.sub(r"^## (?:下一步最有判别力的验证|下一步评测坐标|下一步最值得验证|Next discriminating validation|Next evaluation coordinate|Most useful next validation)\s*\n.*?(?=^## |\Z)", "", text, flags=re.M | re.S)
            if lang == "zh":
                text = re.sub(r"^编辑整理：2026-09-05。元数据最近核验：.*$", f"编辑：2026-09-05 · 元数据核验：{item.get('last_verified', '—')}。编辑日期不等于成绩重新核验；数值应按原始设置、轨道与版本阅读。", text, flags=re.M)
            else:
                text = re.sub(r"^Editorial revision: 2026-09-05\. Last recorded metadata verification:.*$", f"Edited: 2026-09-05 · Metadata last verified: {item.get('last_verified', '—')}. Editing is not a fresh score verification; read numerical evidence within its original configuration, track and release.", text, flags=re.M)
            path.write_text(text, encoding="utf-8")
    # A dated record is not a claim to know the live leaderboard.
    component = ROOT / "web/src/components/BenchmarkDetail.astro"
    text = component.read_text(encoding="utf-8")
    text = text.replace('currentBest: "当前最好成绩"', 'currentBest: "已收录最佳成绩"').replace('currentBest: "Current best"', 'currentBest: "Best recorded result"')
    component.write_text(text, encoding="utf-8")
    print("Removed runtime padding and global prose substitutions; installed safe relative links, tables, code blocks, and full-registry rendering tests.")


if __name__ == "__main__":
    main()
