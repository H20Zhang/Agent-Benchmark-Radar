import { existsSync, readFileSync } from "node:fs";

import { fromRepositoryRoot } from "./repository-path.mjs";
import { loadRegistry } from "./registry.mjs";

function escapeHtml(value) {
  return value
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

function inlineMarkdown(value) {
  return escapeHtml(value)
    .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
    .replace(/`([^`]+)`/g, "<code>$1</code>")
    .replace(/\[([^\]]+)\]\((https:\/\/[^\s)]+)\)/g, '<a href="$2" rel="noreferrer">$1</a>')
    .replace(/(^|\s)(https:\/\/[^\s<]+)/g, '$1<a href="$2" rel="noreferrer">$2</a>');
}

export function renderDeepReadMarkdown(markdown) {
  const lines = markdown.replaceAll("\r\n", "\n").split("\n");
  const output = [];
  let list = [];
  let paragraph = [];

  const flushList = () => {
    if (list.length) output.push(`<ul>${list.map((line) => `<li>${inlineMarkdown(line)}</li>`).join("")}</ul>`);
    list = [];
  };
  const flushParagraph = () => {
    if (paragraph.length) output.push(`<p>${inlineMarkdown(paragraph.join(" "))}</p>`);
    paragraph = [];
  };

  for (const line of lines) {
    const heading = /^(#{1,6})\s+(.+)$/.exec(line);
    const bullet = /^[-*]\s+(.+)$/.exec(line);
    if (heading) {
      flushList();
      flushParagraph();
      if (heading[1].length > 1) {
        const level = Math.min(4, heading[1].length);
        output.push(`<h${level}>${inlineMarkdown(heading[2])}</h${level}>`);
      }
    } else if (bullet) {
      flushParagraph();
      list.push(bullet[1]);
    } else if (!line.trim()) {
      flushList();
      flushParagraph();
    } else {
      flushList();
      paragraph.push(line.trim());
    }
  }
  flushList();
  flushParagraph();
  return output.join("\n");
}

const DEPTH_WITNESSES = [
  /测什么|测量对象|what it (?:actually )?measures|measurement object|measurement target/i,
  /相比|前身|前驱|compared|relative to|what changed|genealogy|谱系|演化/i,
  /评测|协议|protocol|evaluation setup|fair comparison|公平比较|comparison contract/i,
  /证据|结果|分数|evidence|result|score|leaderboard/i,
  /边界|混杂|混淆|限制|不能|局限|结论上限|confound|limitation|cannot|does not establish|score boundary|score ceiling|what (?:this|the) score supports/i,
  /下一步|没有覆盖|还没有测什么|未覆盖|缺口|next|unmeasured|coverage gap|remaining gap/i,
];

function semanticDepth(markdown) {
  return DEPTH_WITNESSES.reduce((score, witness) => score + Number(witness.test(markdown)), 0);
}

function humanize(value) {
  return String(value || "").replaceAll("-", " ");
}

function canonicalAppendix(item, lang) {
  const protocols = (item.protocol || []).map(humanize);
  const environments = (item.environment || []).map(humanize);
  const confounders = (item.confounders || []).map(humanize);
  const artifacts = Object.entries(item.artifacts || {}).filter(([, url]) => typeof url === "string" && url.startsWith("https://"));

  if (lang === "zh") {
    return [
      "## 规范评测契约",
      "",
      "这一节直接来自 Radar 的已核验 canonical record，用来补齐页面中最影响可比性、但原始 deep read 可能没有显式展开的条件。它不是对论文新增事实的推测。",
      "",
      "### 测量强度与适用边界",
      "",
      item.measurement_strength,
      "",
      `**规模 / 范围：** ${item.scale}`,
      "",
      `**当前仍未覆盖：** ${item.coverage_gap}`,
      "",
      "### Protocol cell",
      "",
      ...(protocols.length ? protocols.map((value) => `- 协议：${value}`) : ["- 协议：请以一手来源中的正式 evaluator contract 为准。"]),
      ...(environments.length ? environments.map((value) => `- 环境：${value}`) : []),
      "",
      "### 公平比较与主要混杂因素",
      "",
      "把两个结果放进同一比较单元前，至少应对齐模型/工具/harness、任务切分、环境版本、资源预算、停止与重试规则以及 evaluator。下面这些是该 benchmark 特别 load-bearing 的变量：",
      "",
      ...(confounders.length ? confounders.map((value) => `- ${value}`) : ["- 当前 canonical record 尚未标出额外的 benchmark-specific confounder。"]),
      "",
      "因此，协议单元不同的分数首先是 **system-level evidence**；除非有 matched intervention / ablation，不应把总分差异直接归因给某一个 memory、retrieval、planning 或 data-tool component。",
      "",
      "### 一手来源与核验",
      "",
      ...(artifacts.length ? artifacts.map(([key, url]) => `- ${humanize(key)}：${url}`) : ["- 一手来源见 canonical registry。"]),
      `- Radar 最后核验：${item.last_verified || "—"}`,
    ].join("\n");
  }

  return [
    "## Canonical evaluation contract",
    "",
    "This section is generated directly from Radar's verified canonical record. It fills comparison-critical conditions that a narrative deep read may not state explicitly; it does not invent additional facts about the benchmark.",
    "",
    "### Measurement strength and inference boundary",
    "",
    item.measurement_strength,
    "",
    `**Scale / scope:** ${item.scale}`,
    "",
    `**Still unmeasured:** ${item.coverage_gap}`,
    "",
    "### Protocol cell",
    "",
    ...(protocols.length ? protocols.map((value) => `- Protocol: ${value}`) : ["- Protocol: use the primary evaluator contract as authoritative."]),
    ...(environments.length ? environments.map((value) => `- Environment: ${value}`) : []),
    "",
    "### Fair comparison and main confounders",
    "",
    "Before placing two results in one comparison cell, align model/tools/harness, task split, environment version, resource budget, stopping/retry rules, and evaluator. These variables are especially load-bearing for this benchmark:",
    "",
    ...(confounders.length ? confounders.map((value) => `- ${value}`) : ["- The canonical record does not currently identify an additional benchmark-specific confounder."]),
    "",
    "Scores from different protocol cells are therefore **system-level evidence** first. Without a matched intervention or ablation, an aggregate score gap should not be attributed directly to one memory, retrieval, planning, or data-tool component.",
    "",
    "### Primary sources and verification",
    "",
    ...(artifacts.length ? artifacts.map(([key, url]) => `- ${humanize(key)}: ${url}`) : ["- See the canonical registry for primary sources."]),
    `- Radar last verified: ${item.last_verified || "—"}`,
  ].join("\n");
}

export function loadDeepRead(id, lang) {
  const filename = `${id}${lang === "en" ? ".en" : ""}.md`;
  const path = fromRepositoryRoot("benchmarks", filename);
  if (!existsSync(path)) return undefined;
  const markdown = readFileSync(path, "utf8");
  const item = loadRegistry().find((record) => record.id === id);
  const enrichedMarkdown = item && semanticDepth(markdown) < 6
    ? `${markdown.trim()}\n\n---\n\n${canonicalAppendix(item, lang)}\n`
    : markdown;
  const publicMarkdown = enrichedMarkdown
    .replaceAll("最强混淆", "公平比较条件")
    .replaceAll("最主要的混杂因素", "公平比较条件")
    .replaceAll("结论上限", "分数支持的判断")
    .replaceAll("还没有覆盖什么", "下一步评测坐标")
    .replaceAll("未覆盖", "下一步评测坐标")
    .replaceAll("Strongest confounder", "Fair comparison conditions")
    .replaceAll("Score ceiling", "What the score supports")
    .replaceAll("Remaining gap", "Next evaluation coordinate");
  return {
    id,
    lang,
    markdown,
    html: renderDeepReadMarkdown(publicMarkdown),
    canonicalAppendixAdded: enrichedMarkdown !== markdown,
  };
}
