import {
  filterBenchmarks,
  parseFilterState,
  serializeFilterState,
  sortBenchmarks,
} from "../lib/filters.mjs";

function parseArray(value) {
  try {
    return JSON.parse(value || "[]");
  } catch {
    return [];
  }
}

function modelFromCard(element) {
  return {
    id: element.dataset.benchmarkId,
    name: element.querySelector("h3")?.textContent?.trim() || "",
    summary: element.dataset.search || "",
    measurement_strength: "",
    scale: "",
    area: element.dataset.area,
    evolution_role: element.dataset.role,
    released: element.dataset.released,
    capabilities: parseArray(element.dataset.capabilities),
    environment: parseArray(element.dataset.environments),
    protocol: parseArray(element.dataset.protocols),
    artifacts: Object.fromEntries(
      parseArray(element.dataset.artifacts).map((kind) => [kind, true]),
    ),
    citations: { count: Number(element.dataset.citations || -1) },
    element,
  };
}

function paramsFromForm(form) {
  const params = new URLSearchParams();
  const data = new FormData(form);
  for (const [key, value] of data.entries()) {
    if (String(value).trim()) params.append(key, String(value));
  }
  return params;
}

function syncForm(form, params) {
  for (const control of form.elements) {
    if (!(control instanceof HTMLInputElement || control instanceof HTMLSelectElement)) {
      continue;
    }
    const selected = params.getAll(control.name);
    if (control instanceof HTMLInputElement && control.type === "checkbox") {
      control.checked = selected.includes(control.value);
    } else if (control.name === "sort") {
      control.value = selected[0] || "newest";
    } else {
      control.value = selected[0] || "";
    }
  }
}

function initExplorer(root) {
  const form = root.querySelector("[data-filter-form]");
  const grid = root.querySelector("[data-result-grid]");
  const count = root.querySelector('[aria-live="polite"]');
  const empty = root.querySelector("[data-empty-state]");
  if (!(form instanceof HTMLFormElement) || !grid || !count || !empty) return;

  const models = [...grid.querySelectorAll("[data-benchmark-id]")].map(modelFromCard);
  syncForm(form, new URLSearchParams(window.location.search));

  const apply = () => {
    const state = parseFilterState(paramsFromForm(form));
    const matches = new Set(filterBenchmarks(models, state).map((item) => item.id));
    const ordered = sortBenchmarks(models, state.sort);

    for (const model of ordered) {
      model.element.hidden = !matches.has(model.id);
      grid.append(model.element);
    }

    count.textContent = String(matches.size);
    empty.hidden = matches.size !== 0;
    const query = serializeFilterState(state);
    const next = `${window.location.pathname}${query ? `?${query}` : ""}${window.location.hash}`;
    history.replaceState({}, "", next);
  };

  let frame;
  const schedule = () => {
    cancelAnimationFrame(frame);
    frame = requestAnimationFrame(apply);
  };

  form.addEventListener("input", schedule);
  form.addEventListener("change", apply);
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    apply();
  });
  for (const reset of root.querySelectorAll("[data-reset-filters]")) {
    reset.addEventListener("click", () => {
      form.reset();
      syncForm(form, new URLSearchParams());
      apply();
    });
  }
  apply();
}

export function initExplorers() {
  for (const root of document.querySelectorAll("[data-explorer]")) {
    initExplorer(root);
  }
}
