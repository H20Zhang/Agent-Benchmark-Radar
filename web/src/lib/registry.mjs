import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";

const REGISTRY_PATH = fileURLToPath(
  new URL("../../../data/benchmarks.json", import.meta.url),
);

/** @typedef {{paper?: string, code?: string, data?: string, [key: string]: string | undefined}} Artifacts */
/**
 * @typedef {object} Benchmark
 * @property {string} id
 * @property {string} name
 * @property {"agent-memory" | "rag" | "data-agent"} area
 * @property {"precursor" | "foundation" | "transition" | "frontier"} evolution_role
 * @property {string} released
 * @property {number} importance
 * @property {string} status
 * @property {string} summary
 * @property {string[]} capabilities
 * @property {string[]} environment
 * @property {string[]} protocol
 * @property {string} scale
 * @property {string} measurement_strength
 * @property {string} coverage_gap
 * @property {string[]} confounders
 * @property {Artifacts} artifacts
 * @property {string} last_verified
 * @property {{count?: number, url?: string, status?: string}} [citations]
 */

/** @type {ReadonlyArray<Readonly<Benchmark>> | undefined} */
let registryCache;

function assertString(value, field, id) {
  if (typeof value !== "string" || value.length === 0) {
    throw new Error(`Benchmark ${id || "<unknown>"} has invalid ${field}`);
  }
}

/**
 * Load and minimally validate the canonical benchmark registry.
 * @returns {ReadonlyArray<Readonly<Benchmark>>}
 */
export function loadRegistry() {
  if (registryCache) return registryCache;

  const parsed = JSON.parse(readFileSync(REGISTRY_PATH, "utf8"));
  if (!Array.isArray(parsed)) {
    throw new Error("data/benchmarks.json must contain an array");
  }

  const ids = new Set();
  for (const item of parsed) {
    assertString(item.id, "id", item.id);
    assertString(item.name, "name", item.id);
    assertString(item.released, "released", item.id);
    assertString(item.summary, "summary", item.id);
    if (ids.has(item.id)) throw new Error(`Duplicate benchmark id: ${item.id}`);
    ids.add(item.id);
  }

  registryCache = Object.freeze(
    parsed
      .map((item) => Object.freeze(item))
      .sort(
        (left, right) =>
          right.released.localeCompare(left.released) ||
          left.name.localeCompare(right.name),
      ),
  );
  return registryCache;
}

/** @param {Benchmark} item */
export function getArtifactKinds(item) {
  return ["paper", "code", "data"].filter((kind) =>
    Boolean(item.artifacts?.[kind]),
  );
}

/** @param {string} released */
export function getReleasedYear(released) {
  const match = /^(\d{4})/.exec(released);
  if (!match) throw new Error(`Invalid released value: ${released}`);
  return Number(match[1]);
}
