import assert from "node:assert/strict";
import { resolve } from "node:path";
import test from "node:test";

import {
  getArtifactKinds,
  getReleasedYear,
  loadRegistry,
} from "../src/lib/registry.mjs";
import { resolveRepositoryRoot } from "../src/lib/repository-path.mjs";
import { loadChineseSummaries } from "../src/lib/readme-localization.mjs";

test("registry and Chinese summaries cover the same stable ids", () => {
  const registry = loadRegistry();
  const summaries = loadChineseSummaries();

  assert.equal(registry.length, 126);
  assert.deepEqual(
    [...summaries.keys()].sort(),
    registry.map((item) => item.id).sort(),
  );
  assert.ok(
    registry.every(
      (item) => getArtifactKinds(item).includes("paper") || item.artifacts.code,
    ),
  );
});

test("registry normalization preserves release precision and useful artifacts", () => {
  const registry = loadRegistry();
  const locomo = registry.find((item) => item.id === "locomo");
  const injecmem = registry.find((item) => item.id === "injecmem");

  assert.equal(getReleasedYear(locomo.released), 2024);
  assert.equal(injecmem.released, "2026-08-24");
  assert.deepEqual(getArtifactKinds(locomo), ["paper", "code"]);
});

test("repository assets resolve from both root and Astro working directories", () => {
  const repositoryRoot = resolve(import.meta.dirname, "../..");

  assert.equal(resolveRepositoryRoot(repositoryRoot), repositoryRoot);
  assert.equal(
    resolveRepositoryRoot(resolve(repositoryRoot, "web")),
    repositoryRoot,
  );
});

test("Chinese summaries are clean sentences rather than Markdown table syntax", () => {
  const summaries = loadChineseSummaries();
  const summary = summaries.get("locomo");

  assert.match(summary, /超长多会话对话/);
  assert.doesNotMatch(summary, /benchmark-id|\|/);
});
