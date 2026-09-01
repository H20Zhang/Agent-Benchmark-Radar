const ALLOWED_AREAS = new Set(["agent-memory", "rag", "data-agent"]);
const ALLOWED_ROLES = new Set([
  "precursor",
  "foundation",
  "transition",
  "frontier",
]);
const ALLOWED_ARTIFACTS = new Set(["paper", "code", "data"]);
const ALLOWED_SORTS = new Set(["newest", "oldest", "citations", "name"]);
const TAG_PATTERN = /^[\p{L}\p{N}][\p{L}\p{N}+._-]{0,99}$/u;

function uniqueSorted(values) {
  return [...new Set(values)].sort((left, right) => left.localeCompare(right));
}

function allowedValues(params, key, allowed) {
  return uniqueSorted(
    params
      .getAll(key)
      .map((value) => value.trim())
      .filter((value) => allowed.has(value)),
  );
}

function tagValues(params, key) {
  return uniqueSorted(
    params
      .getAll(key)
      .map((value) => value.trim())
      .filter((value) => TAG_PATTERN.test(value)),
  );
}

/** @param {URLSearchParams} params */
export function parseFilterState(params) {
  const requestedSort = params.get("sort") || "newest";
  const years = uniqueSorted(
    params
      .getAll("year")
      .filter((value) => /^\d{4}$/.test(value))
      .map(Number),
  );

  return {
    query: (params.get("q") || "").trim().slice(0, 120),
    areas: allowedValues(params, "area", ALLOWED_AREAS),
    roles: allowedValues(params, "role", ALLOWED_ROLES),
    artifacts: allowedValues(params, "artifact", ALLOWED_ARTIFACTS),
    capabilities: tagValues(params, "capability"),
    environments: tagValues(params, "environment"),
    protocols: tagValues(params, "protocol"),
    years,
    sort: ALLOWED_SORTS.has(requestedSort) ? requestedSort : "newest",
  };
}

/** @param {ReturnType<typeof parseFilterState>} state */
export function serializeFilterState(state) {
  const params = new URLSearchParams();
  if (state.query) params.set("q", state.query.trim().slice(0, 120));

  const groups = [
    ["area", state.areas],
    ["role", state.roles],
    ["artifact", state.artifacts],
    ["capability", state.capabilities],
    ["environment", state.environments],
    ["protocol", state.protocols],
    ["year", state.years],
  ];
  for (const [key, values] of groups) {
    for (const value of uniqueSorted(values || [])) {
      params.append(key, String(value));
    }
  }
  if (state.sort && state.sort !== "newest") params.set("sort", state.sort);
  return params.toString();
}

function includesAny(actual = [], selected = []) {
  return selected.length === 0 || selected.some((value) => actual.includes(value));
}

function artifactKinds(item) {
  return ["paper", "code", "data"].filter((key) => Boolean(item.artifacts?.[key]));
}

function searchableText(item) {
  return [
    item.name,
    item.summary,
    item.measurement_strength,
    item.scale,
    ...(item.capabilities || []),
    ...(item.environment || []),
    ...(item.protocol || []),
  ]
    .filter(Boolean)
    .join(" ")
    .toLocaleLowerCase();
}

/**
 * Apply OR within each facet and AND across facets.
 * @param {Array<object>} items
 * @param {ReturnType<typeof parseFilterState>} state
 */
export function filterBenchmarks(items, state) {
  const query = state.query.trim().toLocaleLowerCase();
  return items.filter((item) => {
    const year = Number(item.released.slice(0, 4));
    return (
      (!query || searchableText(item).includes(query)) &&
      includesAny([item.area], state.areas) &&
      includesAny([item.evolution_role], state.roles) &&
      includesAny(artifactKinds(item), state.artifacts) &&
      includesAny(item.capabilities, state.capabilities) &&
      includesAny(item.environment, state.environments) &&
      includesAny(item.protocol, state.protocols) &&
      includesAny([year], state.years)
    );
  });
}

/** @param {Array<object>} items @param {string} sort */
export function sortBenchmarks(items, sort = "newest") {
  const result = [...items];
  if (sort === "oldest") {
    return result.sort(
      (left, right) =>
        left.released.localeCompare(right.released) ||
        left.name.localeCompare(right.name),
    );
  }
  if (sort === "citations") {
    return result.sort(
      (left, right) =>
        (right.citations?.count ?? -1) - (left.citations?.count ?? -1) ||
        left.name.localeCompare(right.name),
    );
  }
  if (sort === "name") {
    return result.sort((left, right) => left.name.localeCompare(right.name));
  }
  return result.sort(
    (left, right) =>
      right.released.localeCompare(left.released) ||
      left.name.localeCompare(right.name),
  );
}

/** @param {Array<object>} items @param {string} key */
export function buildFacetOptions(items, key) {
  const counts = new Map();
  for (const item of items) {
    for (const value of item[key] || []) {
      counts.set(value, (counts.get(value) || 0) + 1);
    }
  }
  return [...counts]
    .map(([value, count]) => ({ value, count }))
    .sort((left, right) => left.value.localeCompare(right.value));
}
