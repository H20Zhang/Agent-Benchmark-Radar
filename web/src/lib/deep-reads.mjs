import { existsSync, readFileSync } from "node:fs";
import { fromRepositoryRoot } from "./repository-path.mjs";
import { renderMarkdown, authoredSections } from "./markdown.mjs";
const cache = new Map();
export function renderDeepReadMarkdown(markdown, options = {}) {
  return renderMarkdown(markdown, options).html;
}
export function loadDeepRead(id, lang) {
  const key = `${id}:${lang}`;
  if (cache.has(key)) return cache.get(key);
  const filename = `${id}${lang === "en" ? ".en" : ""}.md`;
  const path = fromRepositoryRoot("benchmarks", filename);
  if (!existsSync(path)) return undefined;
  const markdown = readFileSync(path, "utf8");
  const rendered = renderMarkdown(markdown, { id, lang });
  const result = {
    id,
    lang,
    markdown,
    ...rendered,
    sections: authoredSections(markdown),
  };
  cache.set(key, result);
  return result;
}
export function getAuthoredBrief(id, lang) {
  const sections = loadDeepRead(id, lang)?.sections || new Map();
  const choose = (names) =>
    names.map((n) => sections.get(n)).find(Boolean) || "";
  return lang === "zh"
    ? {
        why: choose([
          "什么时候值得用",
          "相比此前评测多测了什么",
          "测量对象",
          "它到底测什么",
        ]),
        example: choose(["一个具体任务长什么样"]),
        supports: choose([
          "这个分数能证明什么",
          "结论上限",
          "分数支持的判断",
          "结论边界",
        ]),
        controls: choose(["公平比较契约", "公平比较条件", "最强混淆"]),
        next: choose([
          "最有判别力的实验",
          "下一步最有判别力的验证",
          "下一步验证",
          "剩余缺口与下一步",
        ]),
      }
    : {
        why: choose([
          "When to use it",
          "What it measures",
          "Measurement target",
          "What it adds",
        ]),
        example: choose([
          "What a concrete task looks like",
          "A concrete task example",
        ]),
        supports: choose([
          "What the score establishes",
          "What the score supports",
          "Score ceiling",
          "Score boundary",
        ]),
        controls: choose([
          "Fair-comparison contract",
          "Fair comparison contract",
          "Strongest confounder",
          "Fair comparison conditions",
        ]),
        next: choose([
          "Most discriminating experiment",
          "Next discriminating evaluation",
          "Next discriminating validation",
          "Remaining gap and next validation",
        ]),
      };
}
