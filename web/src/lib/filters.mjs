const ALLOWED_AREAS = new Set(["agent-memory", "rag", "data-agent"]);
const ALLOWED_ROLES = new Set([
  "precursor",
  "foundation",
  "transition",
  "frontier",
]);
const ALLOWED_ARTIFACTS = new Set(["paper", "code", "data"]);
const ALLOWED_SORTS = new Set(["newest", "oldest", "citations", "name"]);
const ALLOWED_RESULT_STATUSES = new Set(["tracked", "untracked"]);
const ALLOWED_SOURCE_TYPES = new Set(["live", "paper-snapshot", "verified-snapshot"]);
const ALLOWED_HEADROOM_BANDS = new Set([
  "wide",
  "moderate",
  "limited",
  "unknown",
]);
const TAG_PATTERN = /^[\p{L}\p{N}][\p{L}\p{N}+:._-]{0,139}$/u;

function uniqueSorted(values) {
  return [...new Set(values)].sort((left, right) =>
    String(left).localeCompare(String(right)),
  );
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
    stableFacets: tagValues(params, "facet"),
    resultStatuses: allowedValues(params, "status", ALLOWED_RESULT_STATUSES),
    sourceTypes: uniqueSorted([...allowedValues(params, "source", ALLOWED_SOURCE_TYPES), ...allowedValues(params, "status", ALLOWED_SOURCE_TYPES)]),
    headroomBands: [], // Retired: target distance is not a research-opportunity filter.
    metricFamilies: tagValues(params, "metric"),
    rawTags: tagValues(params, "tag"),
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
    ["facet", state.stableFacets],
    ["status", state.resultStatuses],
    ["source", state.sourceTypes],
    ["metric", state.metricFamilies],
    ["tag", state.rawTags],
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
  return (
    selected.length === 0 || selected.some((value) => actual.includes(value))
  );
}

function artifactKinds(item) {
  return ["paper", "code", "data"].filter((key) =>
    Boolean(item.artifacts?.[key]),
  );
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

export function matchesFacetGroups(actual = [], selected = []) {
  const groups = new Map();
  for (const key of selected) {
    const separator = key.indexOf(":");
    // Legacy URL keys remain matchable only within their one explicit legacy group.
    const group = separator < 0 ? "legacy" : key.slice(0, separator);
    if (!groups.has(group)) groups.set(group, []);
    groups.get(group).push(key);
  }
  return [...groups.values()].every((options) =>
    options.some((value) => actual.includes(value)),
  );
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
      matchesFacetGroups(item.stableFacets, state.stableFacets) &&
      includesAny([item.resultStatus], state.resultStatuses) &&
      includesAny([item.resultTrackingStatus], state.sourceTypes || []) &&
      includesAny(
        item.metricFamilies || [item.metricFamily],
        state.metricFamilies,
      ) &&
      includesAny(
        [
          ...(item.capabilities || []),
          ...(item.environment || []),
          ...(item.protocol || []),
        ],
        state.rawTags,
      ) &&
      includesAny([year], state.years)
    );
  });
}

/**
 * @template {{released: string, name: string, citations?: {count?: number}}} T
 * @param {ReadonlyArray<T>} items
 * @param {string} sort
 * @returns {T[]}
 */
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

/** Migrate only unambiguous historical aliases. An unresolved alias remains restrictive. */
export function migrateFacetParams(params, knownKeys) {
  const out = new URLSearchParams(params);
  const keys = [...new Set(knownKeys)];
  const selected = out.getAll("facet");
  out.delete("facet");
  for (const value of selected) {
    const matches = keys.filter((key) => key.endsWith(`:${value}`));
    out.append("facet", !value.includes(":") && matches.length === 1 ? matches[0] : value);
  }
  return out;
}
export function replaceFilterDimension(params, key, values) {
  const out = new URLSearchParams(params);
  out.delete(key);
  for (const value of values) if (String(value).trim()) out.append(key, String(value));
  return out;
}
