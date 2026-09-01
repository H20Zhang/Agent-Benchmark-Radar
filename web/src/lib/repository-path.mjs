import { existsSync } from "node:fs";
import { resolve } from "node:path";

/**
 * Resolve the repository root from either the repository itself or Astro's
 * `web/` working directory. This remains stable after Astro bundles modules
 * into `dist/.prerender`.
 * @param {string} [startDirectory]
 */
export function resolveRepositoryRoot(startDirectory = process.cwd()) {
  if (existsSync(resolve(startDirectory, "data", "benchmarks.json"))) {
    return resolve(startDirectory);
  }

  const parent = resolve(startDirectory, "..");
  if (existsSync(resolve(parent, "data", "benchmarks.json"))) {
    return parent;
  }

  throw new Error(`Unable to resolve repository root from ${startDirectory}`);
}

/** @param {...string} segments */
export function fromRepositoryRoot(...segments) {
  return resolve(resolveRepositoryRoot(), ...segments);
}
