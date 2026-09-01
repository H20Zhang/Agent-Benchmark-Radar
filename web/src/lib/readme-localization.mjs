import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";

import { loadRegistry } from "./registry.mjs";

const CHINESE_README_PATH = fileURLToPath(
  new URL("../../../README.md", import.meta.url),
);

/** @type {ReadonlyMap<string, string> | undefined} */
let summaryCache;

function cleanTableCell(value) {
  return value
    .replace(/\[([^\]]+)]\([^)]+\)/g, "$1")
    .replace(/[*_`]/g, "")
    .replace(/<[^>]+>/g, "")
    .replace(/\s+/g, " ")
    .trim();
}

/**
 * Extract the complete Chinese one-sentence descriptions already maintained
 * in the README's canonical registry tables.
 * @returns {ReadonlyMap<string, string>}
 */
export function loadChineseSummaries() {
  if (summaryCache) return summaryCache;

  const readme = readFileSync(CHINESE_README_PATH, "utf8");
  const summaries = new Map();
  const rowPattern =
    /^\|.*?<!-- benchmark-id:([a-z0-9-]+) -->.*\|\s*([^|]+?)\s*\|\s*$/gm;
  const areas = ["agent-memory", "rag", "data-agent"];

  for (const area of areas) {
    const startMarker = `<!-- TABLE-FIRST:AREA:${area}:START -->`;
    const endMarker = `<!-- TABLE-FIRST:AREA:${area}:END -->`;
    const block = readme.split(startMarker, 2)[1]?.split(endMarker, 1)[0];
    if (!block) throw new Error(`Missing Chinese registry table: ${area}`);

    for (const match of block.matchAll(rowPattern)) {
      const [, id, rawSummary] = match;
      if (summaries.has(id)) throw new Error(`Duplicate Chinese summary: ${id}`);
      const summary = cleanTableCell(rawSummary);
      if (!summary) throw new Error(`Empty Chinese summary: ${id}`);
      summaries.set(id, summary);
    }
  }

  const registryIds = new Set(loadRegistry().map((item) => item.id));
  const missing = [...registryIds].filter((id) => !summaries.has(id));
  const extra = [...summaries.keys()].filter((id) => !registryIds.has(id));
  if (missing.length || extra.length) {
    throw new Error(
      `Chinese summary coverage mismatch; missing=${missing.join(",")}; extra=${extra.join(",")}`,
    );
  }

  summaryCache = summaries;
  return summaryCache;
}
