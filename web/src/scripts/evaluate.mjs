function json(value) { try { return JSON.parse(value || "[]"); } catch { return []; } }

function initBuilder(root) {
  const lang = root.dataset.lang || "en";
  const recipes = [...root.querySelectorAll("[data-recipe]")];
  const inputs = [...root.querySelectorAll('input[name="benchmark"]')];
  const selected = new Set();
  let activeRecipe;
  const params = new URLSearchParams(window.location.search);

  const render = () => {
    for (const input of inputs) input.checked = selected.has(input.value);
    const names = new Map(inputs.map((input) => [input.value, input.closest("label")?.querySelector("strong")?.textContent || input.value]));
    root.querySelector("[data-suite-count]").textContent = String(selected.size);
    const list = root.querySelector("[data-suite-selection]");
    list.replaceChildren(...[...selected].map((id) => {
      const item = document.createElement("li");
      const removeLabel = lang === "zh" ? `移除 ${names.get(id)}` : `Remove ${names.get(id)}`;
      item.innerHTML = `<span>${names.get(id)}</span><button type="button" data-remove="${id}" aria-label="${removeLabel}">×</button>`;
      return item;
    }));
    const query = new URLSearchParams();
    if (activeRecipe) query.set("recipe", activeRecipe.dataset.recipe);
    for (const id of selected) query.append("benchmark", id);
    history.replaceState({}, "", `${window.location.pathname}${query.size ? `?${query}` : ""}`);
    const compare = root.querySelector("[data-compare-suite]");
    const compareQuery = [...selected].slice(0, 3).map((id) => `benchmark=${encodeURIComponent(id)}`).join("&");
    compare.href = `${compare.getAttribute("href").split("?")[0]}${compareQuery ? `?${compareQuery}` : ""}`;
  };

  const chooseRecipe = (button) => {
    activeRecipe = button;
    for (const recipe of recipes) recipe.classList.toggle("is-active", recipe === button);
    selected.clear();
    for (const id of [...json(button.dataset.core), ...json(button.dataset.complement)]) selected.add(id);
    root.querySelector("[data-suite-title]").textContent = button.querySelector("strong")?.textContent || "";
    root.querySelector("[data-suite-boundary]").textContent = button.dataset.boundary || "";
    root.querySelector("[data-suite-next]").textContent = button.dataset.next || "";
    render();
  };

  for (const button of recipes) button.addEventListener("click", () => chooseRecipe(button));
  for (const input of inputs) input.addEventListener("change", () => { input.checked ? selected.add(input.value) : selected.delete(input.value); render(); });
  root.querySelector("[data-suite-selection]")?.addEventListener("click", (event) => { const button = event.target.closest("[data-remove]"); if (button) { selected.delete(button.dataset.remove); render(); } });
  root.querySelector("[data-suite-search]")?.addEventListener("input", (event) => { const query = event.target.value.trim().toLowerCase(); for (const item of root.querySelectorAll("[data-suite-item]")) item.hidden = query && !item.dataset.search.includes(query); });
  root.querySelector("[data-copy-suite]")?.addEventListener("click", async () => {
    const title = root.querySelector("[data-suite-title]").textContent;
    const boundary = root.querySelector("[data-suite-boundary]").textContent;
    const next = root.querySelector("[data-suite-next]").textContent;
    const names = [...root.querySelectorAll("[data-suite-selection] span")].map((node) => `- ${node.textContent}`).join("\n");
    const benchmarkHeading = lang === "zh" ? "基准" : "Benchmarks";
    const nextHeading = lang === "zh" ? "下一步验证" : "Next validation";
    const Markdown = `## ${title}\n\n${boundary}\n\n### ${benchmarkHeading}\n\n${names}\n\n### ${nextHeading}\n\n${next}`;
    await navigator.clipboard.writeText(Markdown);
    root.querySelector("[data-suite-feedback]").textContent = lang === "zh" ? "Markdown 已复制" : "Markdown copied";
  });

  const requestedRecipe = params.get("recipe");
  const requestedBenchmarks = params.getAll("benchmark");
  const preset = recipes.find((button) => button.dataset.recipe === requestedRecipe) || recipes[0];
  if (preset) chooseRecipe(preset);
  if (requestedBenchmarks.length) { selected.clear(); for (const id of requestedBenchmarks) if (inputs.some((input) => input.value === id)) selected.add(id); render(); }
}

export function initSuiteBuilders() { for (const root of document.querySelectorAll("[data-suite-builder]")) initBuilder(root); }
