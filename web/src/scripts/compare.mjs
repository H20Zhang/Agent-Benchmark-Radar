function escapeHtml(value = "") { return String(value).replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;").replaceAll('"', "&quot;"); }

function initCompare(root) {
  const lang = root.dataset.lang || "en";
  const data = JSON.parse(root.querySelector("#compare-data")?.textContent || "[]");
  const byId = new Map(data.map((item) => [item.id, item]));
  const controls = root.querySelector("[data-compare-controls]");
  const output = root.querySelector("[data-compare-table]");
  const requested = new URLSearchParams(window.location.search).getAll("benchmark").filter((id) => byId.has(id)).slice(0, 3);
  const selected = requested.length ? requested : data.filter((item) => item.result).slice(0, 3).map((item) => item.id);
  while (selected.length < 3) selected.push("");

  const optionHtml = (active) => [`<option value="">${lang === "zh" ? "选择 Benchmark" : "Choose benchmark"}</option>`, ...data.map((item) => `<option value="${escapeHtml(item.id)}" ${item.id === active ? "selected" : ""}>${escapeHtml(item.name)} · ${escapeHtml(item.area)}</option>`)].join("");
  controls.innerHTML = selected.map((id, index) => `<label><span>0${index + 1}</span><select data-compare-select>${optionHtml(id)}</select></label>`).join("");

  const render = () => {
    const ids = [...controls.querySelectorAll("select")].map((select) => select.value).filter(Boolean);
    const items = ids.map((id) => byId.get(id));
    const params = new URLSearchParams();
    for (const id of ids) params.append("benchmark", id);
    history.replaceState({}, "", `${window.location.pathname}${params.size ? `?${params}` : ""}`);
    if (!items.length) { output.innerHTML = `<p>${lang === "zh" ? "选择 Benchmark 后开始比较。" : "Choose benchmarks to begin."}</p>`; return; }
    const rows = [
      [lang === "zh" ? "定位" : "Position", (item) => `${item.area} · ${item.released}`],
      [lang === "zh" ? "测量对象" : "Measurement target", (item) => item.summary],
      [lang === "zh" ? "分数支持" : "Score supports", (item) => item.scoreSupports],
      [lang === "zh" ? "规模" : "Scale", (item) => item.scale],
      [lang === "zh" ? "能力" : "Capabilities", (item) => item.capabilities.join(" · ")],
      [lang === "zh" ? "环境" : "Environment", (item) => item.environment.join(" · ")],
      [lang === "zh" ? "协议" : "Protocol", (item) => item.protocol.join(" · ")],
      [lang === "zh" ? "公平比较" : "Fair comparison", (item) => item.comparison_controls.join(" ")],
      [lang === "zh" ? "已核验最佳" : "Verified best", (item) => item.result ? `${item.result.score}${item.result.unit} · ${item.result.method} · ${item.result.metric}` : (lang === "zh" ? "结果待结构化" : "Result awaiting structuring")],
    ];
    output.innerHTML = `<table><thead><tr><th>${lang === "zh" ? "比较维度" : "Dimension"}</th>${items.map((item) => `<th><a href="../benchmarks/${escapeHtml(item.id)}/">${escapeHtml(item.name)}</a></th>`).join("")}</tr></thead><tbody>${rows.map(([label, value]) => `<tr><th>${label}</th>${items.map((item) => `<td>${escapeHtml(value(item))}</td>`).join("")}</tr>`).join("")}</tbody></table>`;
  };
  controls.addEventListener("change", render);
  render();
}

export function initCompareWorkspaces() { for (const root of document.querySelectorAll("[data-compare-workspace]")) initCompare(root); }
