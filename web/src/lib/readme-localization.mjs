import { readFileSync } from "node:fs";
import { loadRegistry } from "./registry.mjs";
import { fromRepositoryRoot } from "./repository-path.mjs";
let cache;
/** Compatibility name: canonical Chinese prose is no longer parsed from README. */
export function loadChineseSummaries() {
  if (cache) return cache;
  const records = JSON.parse(
    readFileSync(
      fromRepositoryRoot("data", "locales", "zh", "benchmarks.json"),
      "utf8",
    ),
  );
  const ids = new Set(loadRegistry().map((item) => item.id));
  if (Object.keys(records).some((id) => !ids.has(id)))
    throw new Error("Unknown Chinese locale identity");
  cache = new Map(
    [...ids].map((id) => {
      const text = records[id]?.summary;
      if (typeof text !== "string" || !text.trim())
        throw new Error(`Missing canonical Chinese summary: ${id}`);
      return [id, text];
    }),
  );
  return cache;
}
