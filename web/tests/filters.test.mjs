import assert from "node:assert/strict";
import test from "node:test";

import {
  buildFacetOptions,
  filterBenchmarks,
  parseFilterState,
  serializeFilterState,
  sortBenchmarks,
} from "../src/lib/filters.mjs";

const fixtures = [
  {
    id: "locomo",
    name: "LoCoMo",
    summary: "Long-horizon temporal conversational memory.",
    measurement_strength: "Established long-term memory evaluation.",
    area: "agent-memory",
    evolution_role: "foundation",
    released: "2024-08",
    capabilities: ["temporal-reasoning", "long-range-recall"],
    environment: ["multi-session-conversation"],
    protocol: ["question-answering"],
    artifacts: { paper: "paper", code: "code" },
    citations: { count: 780 },
  },
  {
    id: "livebrowsecomp",
    name: "LiveBrowseComp",
    summary: "Live-web agentic search.",
    measurement_strength: "Measures fresh evidence retrieval.",
    area: "rag",
    evolution_role: "frontier",
    released: "2026-05-28",
    capabilities: ["fresh-information-retrieval"],
    environment: ["live-web"],
    protocol: ["agentic-web-search"],
    artifacts: { paper: "paper" },
    citations: { count: 4 },
  },
  {
    id: "spider",
    name: "Spider",
    summary: "Cross-domain text-to-SQL.",
    measurement_strength: "Established schema generalization.",
    area: "data-agent",
    evolution_role: "foundation",
    released: "2018-09",
    capabilities: ["text-to-sql"],
    environment: ["relational-databases"],
    protocol: ["execution-accuracy"],
    artifacts: { paper: "paper", code: "code", data: "data" },
    citations: { count: 2600 },
  },
];

test("filter state round-trips in canonical order", () => {
  const state = parseFilterState(
    new URLSearchParams(
      "sort=citations&role=frontier&area=rag&artifact=code&area=agent-memory&q=memory",
    ),
  );

  assert.equal(
    serializeFilterState(state),
    "q=memory&area=agent-memory&area=rag&role=frontier&artifact=code&sort=citations",
  );
});

test("unknown primary values are dropped while controlled tags remain stable", () => {
  const state = parseFilterState(
    new URLSearchParams(
      "area=unknown&role=foundation&artifact=weights&capability=text-to-sql&year=2026&sort=random",
    ),
  );

  assert.deepEqual(state.areas, []);
  assert.deepEqual(state.roles, ["foundation"]);
  assert.deepEqual(state.artifacts, []);
  assert.deepEqual(state.capabilities, ["text-to-sql"]);
  assert.deepEqual(state.years, [2026]);
  assert.equal(state.sort, "newest");
});

test("text and facets combine with AND semantics", () => {
  const result = filterBenchmarks(fixtures, {
    query: "temporal",
    areas: ["agent-memory"],
    roles: ["foundation"],
    artifacts: ["code"],
    capabilities: [],
    environments: [],
    protocols: [],
    years: [],
    sort: "newest",
  });

  assert.deepEqual(result.map((item) => item.id), ["locomo"]);
});

test("multiple values use OR within a facet", () => {
  const state = parseFilterState(
    new URLSearchParams("area=rag&area=data-agent&artifact=data"),
  );
  const result = filterBenchmarks(fixtures, state);

  assert.deepEqual(result.map((item) => item.id), ["spider"]);
});

test("sorts are deterministic", () => {
  assert.deepEqual(
    sortBenchmarks(fixtures, "newest").map((item) => item.id),
    ["livebrowsecomp", "locomo", "spider"],
  );
  assert.deepEqual(
    sortBenchmarks(fixtures, "citations").map((item) => item.id),
    ["spider", "locomo", "livebrowsecomp"],
  );
  assert.deepEqual(
    sortBenchmarks(fixtures, "name").map((item) => item.id),
    ["livebrowsecomp", "locomo", "spider"],
  );
});

test("facet options expose useful counts", () => {
  assert.deepEqual(buildFacetOptions(fixtures, "capabilities"), [
    { value: "fresh-information-retrieval", count: 1 },
    { value: "long-range-recall", count: 1 },
    { value: "temporal-reasoning", count: 1 },
    { value: "text-to-sql", count: 1 },
  ]);
});
