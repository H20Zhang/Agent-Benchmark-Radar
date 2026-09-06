import { existsSync, readFileSync } from "node:fs";
import { fromRepositoryRoot } from "./repository-path.mjs";
import { renderMarkdown, authoredSections } from "./markdown.mjs";
import { sectionIdentity, pairedHeadingMap } from "./section-identity.mjs";
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
  const alternatePath = fromRepositoryRoot("benchmarks", `${id}${lang === "zh" ? ".en" : ""}.md`);
  const alternate = existsSync(alternatePath) ? renderMarkdown(readFileSync(alternatePath, "utf8"), {id, lang: lang === "zh" ? "en" : "zh"}).headings : [];
  const result = {
    id,
    lang,
    markdown,
    ...rendered,
    sections: authoredSections(markdown),
    languageFragments: pairedHeadingMap(rendered.headings, alternate),
  };
  cache.set(key, result);
  return result;
}
export function getAuthoredBrief(id, lang) {
  const sections = loadDeepRead(id, lang)?.sections || new Map();
  const choose = (keys) => {
    for (const key of keys) for (const [heading, prose] of sections)
      if (sectionIdentity(heading) === key && prose) return prose;
    return "";
  };
  return {
    why: choose(["use", "measurement", "contribution"]), example: choose(["example"]),
    supports: choose(["boundary"]), controls: choose(["controls"]), next: choose(["next"]),
  };
}
