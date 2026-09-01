import { existsSync, readFileSync } from "node:fs";

import { fromRepositoryRoot } from "./repository-path.mjs";

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

export function loadDeepRead(id, lang) {
  const filename = `${id}${lang === "en" ? ".en" : ""}.md`;
  const path = fromRepositoryRoot("benchmarks", filename);
  if (!existsSync(path)) return undefined;
  const markdown = readFileSync(path, "utf8");
  const publicMarkdown = markdown
    .replaceAll("最强混淆", "公平比较条件")
    .replaceAll("最主要的混杂因素", "公平比较条件")
    .replaceAll("结论上限", "分数支持的判断")
    .replaceAll("还没有覆盖什么", "下一步评测坐标")
    .replaceAll("未覆盖", "下一步评测坐标")
    .replaceAll("Strongest confounder", "Fair comparison conditions")
    .replaceAll("Score ceiling", "What the score supports")
    .replaceAll("Remaining gap", "Next evaluation coordinate");
  return { id, lang, markdown, html: renderDeepReadMarkdown(publicMarkdown) };
}
