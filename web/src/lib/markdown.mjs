import { markdownToMdast } from "satteri";
import { toHast } from "mdast-util-to-hast";
import { toHtml } from "hast-util-to-html";
import GithubSlugger from "github-slugger";
import { posix } from "node:path";
import { sitePath, localePath, REPOSITORY_URL } from "./site.mjs";

export const textOf = (node) =>
  node.value ?? node.children?.map(textOf).join(["root", "list", "listItem", "blockquote", "table", "tableRow"].includes(node.type) ? "\n" : "") ?? "";
export const parseMarkdown = (source) =>
  markdownToMdast(source, {
    features: { gfm: true, frontmatter: false, smartPunctuation: false },
  });
/** Relative links resolve from the actual authored note, never from the browser route. */
export function resolveNoteLink(url, { id = "", lang = "en" } = {}) {
  if (/^https:\/\//i.test(url)) return url;
  if (url.startsWith("#")) return `#note-${url.slice(1)}`;
  if (/^[a-z][a-z0-9+.-]*:/i.test(url) || url.startsWith("//"))
    return undefined;
  const [path, fragment = ""] = url.split("#");
  const resolved = posix.normalize(
    posix.join("benchmarks", decodeURIComponent(path)),
  );
  const note = /^benchmarks\/([a-z0-9-]+)(\.en)?\.md$/.exec(resolved);
  if (note)
    return sitePath(
      localePath(
        note[2] ? "en" : "zh",
        `benchmarks/${note[1]}/${fragment ? `#note-${fragment}` : ""}`,
      ),
    );
  if (/^README(?:\.en)?\.md$/.test(resolved)) {
    const locale = resolved.includes(".en") ? "en" : "zh";
    const routes = {
      "release-timeline": "timeline/",
      timeline: "timeline/",
      latest: "timeline/",
      "frontier-signals": "frontier/",
      "evaluation-recipes": "evaluate/",
      "all-benchmarks": "benchmarks/",
      library: "benchmarks/",
      "benchmark-memory": "areas/agent-memory/",
      "benchmark-rag": "areas/rag/",
      "benchmark-data": "areas/data-agent/",
      "registry-memory": "benchmarks/?area=agent-memory",
      "registry-rag": "benchmarks/?area=rag",
      "registry-data": "benchmarks/?area=data-agent",
      "recipe-memory": "evaluate/?area=agent-memory",
      "recipe-rag": "evaluate/?area=rag",
      "recipe-data": "evaluate/?area=data-agent",
      "evaluation-frontiers": "opportunities/",
    };
    return sitePath(
      localePath(locale, routes[fragment] || (fragment ? `#${fragment}` : "")),
    );
  }
  if (/^library\/README(?:\.en)?\.md$/.test(resolved))
    return sitePath(
      localePath(resolved.includes(".en") ? "en" : "zh", "benchmarks/"),
    );
  // Repository documentation remains available as documentation, with a stable explicit target.
  if (resolved.startsWith("../") || resolved.startsWith("/")) return undefined;
  return `${REPOSITORY_URL}/blob/main/${resolved}${fragment ? `#${fragment}` : ""}`;
}
function cleanAst(node, options, headings, slugger) {
  if (node.type === "html") {
    // Comments are maintenance data. Other raw HTML is escaped as text, not executed.
    if (/^\s*<!--[\s\S]*-->\s*$/.test(node.value)) return null;
    return { type: "text", value: node.value };
  }
  if (node.type === "heading") {
    if (node.depth === 1) return null; // The route supplies the article h1.
    const id = `note-${slugger.slug(textOf(node))}`;
    node.data = { ...node.data, hProperties: { id } };
    headings.push({ id, depth: node.depth, text: textOf(node) });
  }
  if (node.type === "link" || node.type === "definition") {
    const target = resolveNoteLink(node.url, options);
    if (target) node.url = target;
    else if (node.type === "link") return { type: "text", value: textOf(node) };
    else return null;
  }
  if (node.type === "image" && !/^https:\/\//i.test(node.url))
    return { type: "text", value: node.alt || "" };
  if (node.children)
    node.children = node.children
      .map((child) => cleanAst(child, options, headings, slugger))
      .filter(Boolean);
  return node;
}
export function renderMarkdown(source, options = {}) {
  const headings = [];
  const tree = cleanAst(
    parseMarkdown(source),
    options,
    headings,
    new GithubSlugger(),
  );
  return { html: toHtml(toHast(tree)), headings };
}
/** Select complete authored sections; never invent or translate the missing prose. */
export function authoredSections(source) {
  const tree = parseMarkdown(source);
  const sections = new Map();
  let title,
    parts = [];
  const flush = () => {
    if (title && parts.length) sections.set(title, parts.join("\n\n"));
    parts = [];
  };
  for (const node of tree.children) {
    if (node.type === "heading") {
      flush();
      title = textOf(node);
    } else if (node.type !== "html") {
      const value = textOf(node).trim();
      if (value) parts.push(value);
      if (node.type === "list")
        for (const child of node.children) {
          const match = /^([^：:]+)[：:]\s*([\s\S]+)$/.exec(textOf(child));
          if (match) sections.set(match[1].trim(), match[2].trim());
        }
    }
  }
  flush();
  return sections;
}
