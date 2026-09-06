function escapeHtml(value = "") { return String(value).replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;").replaceAll('"', "&quot;"); }

function sameProtocolCell(items) {
  if (items.length < 2 || items.some((item) => !item.result)) return false;
  const first = items[0].result;
  return items.every((item) =>
    item.result.metricFamily === first.metricFamily &&
    item.result.direction === first.direction &&
    item.result.unit === first.unit &&
    item.result.protocolVersion === first.protocolVersion &&
    item.result.task === first.task &&
    item.result.split === first.split,
  );
}

function initCompare(root) {
  const lang = root.dataset.lang || "en";
  const data = JSON.parse(root.querySelector("#compare-data")?.textContent || "[]");
  const byId = new Map(data.map((item) => [item.id, item]));
  const controls = root.querySelector("[data-compare-controls]");
  const output = root.querySelector("[data-compare-table]");
  const requested = new URLSearchParams(window.location.search).getAll("benchmark").filter((id) => byId.has(id)).slice(0, 3);
  const selected = [...requested];
  while (selected.length < 3) selected.push("");

  const optionHtml = (active) => [`<option value="">${lang === "zh" ? "选择 Benchmark" : "Choose benchmark"}</option>`, ...data.map((item) => `<option value="${escapeHtml(item.id)}" ${item.id === active ? "selected" : ""}>${escapeHtml(item.name)} · ${escapeHtml(item.area)}</option>`)].join("");
  controls.innerHTML = selected.map((id, index) => `<label><span>0${index + 1}</span><select data-compare-select>${optionHtml(id)}</select></label>`).join("");

  const render = () => {
    const ids = [...controls.querySelectorAll("select")].map((select) => select.value).filter(Boolean);
    const items = ids.map((id) => byId.get(id));
    const params = new URLSearchParams();
    for (const id of ids) params.append("benchmark", id);
    history.replaceState({}, "", `${window.location.pathname}${params.size ? `?${params}` : ""}`);
    if (!items.length) { output.innerHTML = `<p>${lang === "zh" ? "选择 Benchmark 后开始比较。这里不会默认挑三个分数制造伪可比。" : "Choose benchmarks to begin. This workspace does not preselect scores and imply false comparability."}</p>`; return; }

    const comparable = sameProtocolCell(items);
    const comparability = comparable
      ? (lang === "zh" ? "这些成绩属于同一 protocol cell，可直接比较。" : "These result tracks share the same protocol cell and are directly comparable.")
      : (lang === "zh" ? "这些成绩不属于同一 protocol cell。下面的数值只作为各自来源内的 reported result 展示，不能据此排序系统优劣。" : "These results do not share one protocol cell. Scores below are source-local reported results, not a basis for ranking systems against each other.");

    const rows = [
      [lang === "zh" ? "定位" : "Position", (item) => `${item.area} · ${item.released}`],
      [lang === "zh" ? "测量对象" : "Measurement target", (item) => item.summary],
      [lang === "zh" ? "分数支持" : "Score supports", (item) => item.scoreSupports],
      [lang === "zh" ? "规模" : "Scale", (item) => item.scale],
      [lang === "zh" ? "能力" : "Capabilities", (item) => item.capabilities.join(" · ")],
      [lang === "zh" ? "环境" : "Environment", (item) => item.environment.join(" · ")],
      [lang === "zh" ? "协议" : "Protocol", (item) => item.protocol.join(" · ")],
      [lang === "zh" ? "公平比较" : "Fair comparison", (item) => item.comparison_controls.join(" ")],
      [lang === "zh" ? "结果轨道" : "Result track", (item) => item.result ? `${item.result.task} · ${item.result.split} · ${item.result.protocolVersion}` : (lang === "zh" ? "结果待结构化" : "Result awaiting structuring")],
      [comparable ? (lang === "zh" ? "可直接比较成绩" : "Directly comparable score") : (lang === "zh" ? "各自来源报告成绩" : "Source-local reported score"), (item) => item.result ? `${item.result.score}${item.result.unit} · ${item.result.method} · ${item.result.metric} · verified ${item.result.verifiedAt}` : (lang === "zh" ? "结果待结构化" : "Result awaiting structuring")],
    ];
    output.innerHTML = `<div class="compare-contract ${comparable ? "is-comparable" : "is-not-comparable"}"><strong>${lang === "zh" ? "可比性判断" : "Comparability judgment"}</strong><p>${escapeHtml(comparability)}</p></div><table><thead><tr><th>${lang === "zh" ? "比较维度" : "Dimension"}</th>${items.map((item) => `<th><a href="../benchmarks/${escapeHtml(item.id)}/">${escapeHtml(item.name)}</a></th>`).join("")}</tr></thead><tbody>${rows.map(([label, value]) => `<tr><th>${label}</th>${items.map((item) => `<td>${escapeHtml(value(item))}</td>`).join("")}</tr>`).join("")}</tbody></table>`;
  };
  controls.addEventListener("change", render);
  render();
}

export function initCompareWorkspaces() { for (const root of document.querySelectorAll("[data-compare-workspace]")) initCompare(root); }
