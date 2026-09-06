import { suiteState, suiteParams } from "../lib/suite-state.mjs";
import { writePageState } from "./page-state.mjs";
function parse(value) {
  try {
    return JSON.parse(value || "[]");
  } catch {
    return [];
  }
}
function initBuilder(root) {
  const lang = root.dataset.lang || "en";
  const zh = lang === "zh";
  const buttons = [...root.querySelectorAll("[data-recipe]")];
  const inputs = [...root.querySelectorAll('input[name="benchmark"]')];
  const names = new Map(
    inputs.map((input) => [
      input.value,
      input.closest("label").querySelector("strong").textContent,
    ]),
  );
  const recipes = new Map(
    buttons.map((button) => [
      button.dataset.recipe,
      {
        id: button.dataset.recipe,
        core: parse(button.dataset.core),
        complement: parse(button.dataset.complement),
        title: button.querySelector("strong").textContent,
        boundary: button.dataset.boundary,
        next: button.dataset.next,
        area: button.closest("[data-area]").dataset.area,
      },
    ]),
  );
  const selected = new Set();
  let recipe, area;
  const title = root.querySelector("[data-suite-title]");
  const boundary = root.querySelector("[data-suite-boundary]");
  const next = root.querySelector("[data-suite-next]");
  const copy = root.querySelector("[data-copy-suite]");
  const compare = root.querySelector("[data-compare-suite]");
  const compareBase = compare.getAttribute("href").split("?")[0];
  const feedback = root.querySelector("[data-suite-feedback]");
  let state;
  function render(mode = "replace", updateUrl = true) {
    state = suiteState(selected, recipe);
    for (const input of inputs) input.checked = selected.has(input.value);
    for (const button of buttons) {
      const active = state.matches && button.dataset.recipe === recipe?.id;
      button.classList.toggle("is-active", active);
      button.setAttribute("aria-pressed", String(active));
    }
    title.textContent = state.matches
      ? recipe.title
      : zh
        ? state.empty
          ? "尚未选择基准"
          : "自定义评测草稿"
        : state.empty
          ? "No benchmarks selected"
          : "Custom evaluation draft";
    boundary.textContent = state.matches
      ? recipe.boundary
      : zh
        ? "当前集合不再对应预设组合，原研究主张不适用。请逐项确认测量对象和证据边界。"
        : "This selection does not match a preset. Its original claim no longer applies; validate the scope of each selected benchmark.";
    next.textContent = state.matches
      ? recipe.next
      : zh
        ? "确认核心评测、补充维度、模型与资源约束后，再形成研究主张。"
        : "Define core measurements, complementary evidence, model and resource controls before asserting a research claim.";
    root.querySelector("[data-suite-count]").textContent = String(
      state.ids.length,
    );
    root.querySelector("[data-suite-selection]").replaceChildren(
      ...state.ids.map((id) => {
        const li = document.createElement("li");
        const link = document.createElement("a");
        link.href = `../benchmarks/${id}/`;
        link.textContent = names.get(id);
        const remove = document.createElement("button");
        remove.type = "button";
        remove.dataset.remove = id;
        remove.textContent = "×";
        remove.setAttribute(
          "aria-label",
          `${zh ? "移除" : "Remove"} ${names.get(id)}`,
        );
        li.append(link, remove);
        return li;
      }),
    );
    copy.disabled = state.empty;
    compare.setAttribute("aria-disabled", String(state.empty));
    if (state.empty) {
      compare.removeAttribute("href");
      compare.tabIndex = -1;
    } else {
      const query = new URLSearchParams();
      for (const id of state.ids) query.append("benchmark", id);
      compare.href = `${compareBase}?${query}`;
      compare.tabIndex = 0;
    }
    feedback.textContent = "";
    root.querySelector("[data-copy-fallback]")?.remove();
    if (updateUrl) writePageState(suiteParams(state, recipe?.id, area), mode);
  }
  function restore() {
    const params = new URLSearchParams(location.search);
    area = params.get("area");
    recipe = recipes.get(params.get("recipe"));
    const requested = params.getAll("benchmark");
    selected.clear();
    if (requested.length || params.has("custom")) {
      for (const id of requested) if (names.has(id)) selected.add(id);
    } else {
      recipe ||=
        [...recipes.values()].find((r) => r.area === area) ||
        [...recipes.values()][0];
      if (recipe)
        for (const id of [...recipe.core, ...recipe.complement])
          selected.add(id);
    }
    render("replace");
  }
  for (const button of buttons)
    button.addEventListener("click", () => {
      recipe = recipes.get(button.dataset.recipe);
      area = recipe.area;
      selected.clear();
      for (const id of [...recipe.core, ...recipe.complement]) selected.add(id);
      render("push");
    });
  for (const input of inputs)
    input.addEventListener("change", () => {
      input.checked ? selected.add(input.value) : selected.delete(input.value);
      render("push");
    });
  root
    .querySelector("[data-suite-selection]")
    .addEventListener("click", (event) => {
      const button = event.target.closest("[data-remove]");
      if (button) {
        selected.delete(button.dataset.remove);
        render("push");
      }
    });
  root
    .querySelector("[data-suite-search]")
    .addEventListener("input", (event) => {
      const query = event.target.value.trim().toLocaleLowerCase();
      for (const item of root.querySelectorAll("[data-suite-item]"))
        item.hidden = Boolean(query && !item.dataset.search.includes(query));
    });
  copy.addEventListener("click", async () => {
    if (state.empty) return;
    const list = state.ids
      .map(
        (id) =>
          `- [${names.get(id)}](${new URL(`../benchmarks/${id}/`, location.href).href})`,
      )
      .join("\n");
    const Markdown = `## ${title.textContent}\n\n${boundary.textContent}\n\n${list}\n\n### ${zh ? "下一步验证" : "Next validation"}\n\n${next.textContent}\n\n${location.href}`;
    try {
      await navigator.clipboard.writeText(Markdown);
      feedback.textContent = zh ? "Markdown 已复制。" : "Markdown copied.";
    } catch {
      feedback.textContent = zh
        ? "无法访问剪贴板，请从下方文本框复制。"
        : "Clipboard unavailable. Copy from the text field below.";
      let field = root.querySelector("[data-copy-fallback]");
      if (!field) {
        field = document.createElement("textarea");
        field.dataset.copyFallback = "";
        field.readOnly = true;
        field.setAttribute(
          "aria-label",
          zh ? "评测组合 Markdown" : "Suite Markdown",
        );
        feedback.after(field);
      }
      field.value = Markdown;
      field.focus();
      field.select();
    }
  });
  window.addEventListener("popstate", restore);
  restore();
}
export function initSuiteBuilders() {
  for (const root of document.querySelectorAll("[data-suite-builder]"))
    initBuilder(root);
}
