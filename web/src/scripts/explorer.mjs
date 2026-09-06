import { writePageState } from "./page-state.mjs";
import { filterBenchmarks, parseFilterState, serializeFilterState, sortBenchmarks,
  migrateFacetParams, replaceFilterDimension } from "../lib/filters.mjs";

function parseArray(value) { try { return JSON.parse(value || "[]"); } catch { return []; } }
function modelFromCard(element) {
  return {
    id: element.dataset.benchmarkId,
    name: element.querySelector("h3")?.textContent?.trim() || "",
    summary: element.dataset.search || "", area: element.dataset.area,
    evolution_role: element.dataset.role, released: element.dataset.released,
    capabilities: parseArray(element.dataset.capabilities),
    environment: parseArray(element.dataset.environments), protocol: parseArray(element.dataset.protocols),
    stableFacets: parseArray(element.dataset.stableFacets),
    resultStatus: element.dataset.resultStatus || "untracked",
    resultTrackingStatus: element.dataset.resultTrackingStatus || "",
    metricFamilies: parseArray(element.dataset.metricFamilies),
    artifacts: Object.fromEntries(parseArray(element.dataset.artifacts).map(kind => [kind, true])),
    citations: {count: Number(element.dataset.citations ?? -1)}, element,
  };
}
function syncForm(form, params) {
  for (const control of form.elements) {
    if (!(control instanceof HTMLInputElement || control instanceof HTMLSelectElement)) continue;
    const values = params.getAll(control.name);
    if (control.type === "checkbox") control.checked = values.includes(control.value);
    else control.value = values[0] || (control.name === "sort" ? "newest" : "");
    if (control.checked) {
      let parent = control.parentElement;
      while (parent && parent !== form) { if (parent instanceof HTMLDetailsElement) parent.open = true; parent = parent.parentElement; }
    }
  }
}
function initExplorer(root) {
  const form = root.querySelector("[data-filter-form]"), grid = root.querySelector("[data-result-grid]");
  const count = root.querySelector("[data-result-count]"), empty = root.querySelector("[data-empty-state]");
  const active = root.querySelector("[data-active-filters]");
  if (!(form instanceof HTMLFormElement) || !grid || !count || !empty) return;
  const zh = root.dataset.lang === "zh";
  const models = [...grid.querySelectorAll("[data-benchmark-id]")].map(modelFromCard);
  const knownKeys = [...form.querySelectorAll('[name="facet"]')].map(el => el.value);
  const labels = zh ? {q:"搜索", area:"领域", year:"年份", facet:"维度", status:"成绩收录", source:"来源类型", capability:"能力", environment:"环境", protocol:"协议", metric:"指标", tag:"标签", role:"编辑角色", artifact:"资源"}
    : {q:"Search", area:"Area", year:"Year", facet:"Facet", status:"Availability", source:"Source type", capability:"Capability", environment:"Environment", protocol:"Protocol", metric:"Metric", tag:"Tag", role:"Role", artifact:"Resource"};
  const notice = document.createElement("p"); notice.className = "content-note"; notice.setAttribute("role", "status");
  form.append(notice);
  let params = new URLSearchParams();
  function labelFor(key, value) {
    const control = [...form.elements].find(el => el.name === key && el.value === value && el.type === "checkbox");
    if (!control) return value;
    const span = control.closest("label")?.querySelector("span")?.cloneNode(true);
    span?.querySelectorAll("small").forEach(el => el.remove());
    const dimension = control.dataset.facetId && control.closest("details")?.querySelector("summary > span")?.textContent;
    return `${dimension ? `${dimension} / ` : ""}${span?.textContent?.trim() || value}`;
  }
  function apply(mode = "replace") {
    const state = parseFilterState(params);
    const matches = new Set(filterBenchmarks(models, state).map(item => item.id));
    for (const model of sortBenchmarks(models, state.sort)) { model.element.hidden = !matches.has(model.id); grid.append(model.element); }
    for (const facet of form.querySelectorAll("[data-facet-area]")) {
      facet.hidden = Boolean(facet.dataset.facetArea && state.areas.length && !state.areas.includes(facet.dataset.facetArea) && !facet.querySelector("input:checked"));
    }
    count.textContent = String(matches.size); empty.hidden = matches.size !== 0;
    const canonical = new URLSearchParams(serializeFilterState(state));
    if (active) active.replaceChildren(...[...canonical].filter(([key]) => key !== "sort").map(([key,value]) => {
      const chip = document.createElement("button"); chip.type = "button"; chip.className = "active-filter";
      chip.textContent = `${labels[key] || key}: ${labelFor(key,value)} ×`;
      chip.setAttribute("aria-label", `${zh ? "移除" : "Remove"} ${chip.textContent.slice(0,-2)}`);
      chip.addEventListener("click", () => {
        params = replaceFilterDimension(params, key, params.getAll(key).filter(v => v !== value));
        syncForm(form, params); apply("push"); form.querySelector('[name="q"]').focus();
      }); return chip;
    }));
    const unresolved = state.stableFacets.filter(key => !knownKeys.includes(key));
    notice.textContent = unresolved.length ? (zh ? `链接包含未识别或有歧义的筛选项：${unresolved.join("、")}。这些条件未被忽略；请移除或重新选择。` : `Unrecognized or ambiguous facets: ${unresolved.join(", ")}. They remain restrictive; remove or reselect them.`) : "";
    notice.hidden = !notice.textContent;
    params = canonical; writePageState(params, mode);
  }
  function restore() {
    const original = new URLSearchParams(location.search);
    params = new URLSearchParams(serializeFilterState(parseFilterState(migrateFacetParams(original, knownKeys))));
    syncForm(form,params); apply();
  }
  function update(control, mode) {
    if (!control.name) return;
    let values;
    if (control.type === "checkbox") {
      const group = [...form.elements].filter(el => el.name === control.name && el.type === "checkbox");
      // Preserve legacy values that have no rendered control until explicitly removed.
      values = [...group.filter(el => el.checked).map(el => el.value), ...params.getAll(control.name).filter(v => !group.some(el => el.value === v))];
    } else values = control.value ? [control.value] : [];
    params = replaceFilterDimension(params, control.name, values); apply(mode);
  }
  let frame;
  form.addEventListener("input", event => {
    if (event.target.type !== "search") return;
    cancelAnimationFrame(frame); frame = requestAnimationFrame(() => update(event.target, "replace"));
  });
  form.addEventListener("change", event => { cancelAnimationFrame(frame); update(event.target,"push"); });
  form.addEventListener("submit", event => {event.preventDefault(); apply();});
  for (const reset of root.querySelectorAll("[data-reset-filters]")) reset.addEventListener("click", event => {
    event.preventDefault(); cancelAnimationFrame(frame); params = new URLSearchParams(); form.reset(); syncForm(form,params); apply("push");
  });
  window.addEventListener("popstate",restore); restore();
}
export function initExplorers() { for (const root of document.querySelectorAll("[data-explorer]")) initExplorer(root); }
