import { escapeHtml } from "../lib/site.mjs";
import { writePageState } from "./page-state.mjs";
/** This is a benchmark-selection workspace, not a cross-dataset leaderboard. */
function initCompare(root) {
  const zh = root.dataset.lang === "zh";
  const data = JSON.parse(
    root.querySelector("#compare-data").textContent || "[]",
  );
  const byId = new Map(data.map((item) => [item.id, item]));
  const controls = root.querySelector("[data-compare-controls]");
  const output = root.querySelector("[data-compare-table]");
  let ids = [];
  const optionHtml = (active) =>
    `<option value="">${zh ? "添加基准" : "Add benchmark"}</option>` +
    data
      .filter((item) => item.id === active || !ids.includes(item.id))
      .map(
        (item) =>
          `<option value="${escapeHtml(item.id)}" ${item.id === active ? "selected" : ""}>${escapeHtml(item.name)}</option>`,
      )
      .join("");
  function render(mode = "replace") {
    controls.innerHTML = [...ids, ""]
      .map(
        (id, index) =>
          `<label><span>${zh ? "基准" : "Benchmark"} ${index + 1}</span><select data-compare-select data-slot="${index}" aria-label="${zh ? "选择基准" : "Choose benchmark"} ${index + 1}">${optionHtml(id)}</select></label>`,
      )
      .join("");
    const params = new URLSearchParams();
    for (const id of ids) params.append("benchmark", id);
    writePageState(params, mode);
    if (!ids.length) {
      output.innerHTML = `<p class="empty-state">${zh ? "添加基准，比较它们测什么、如何验证，以及需要控制哪些条件。" : "Add benchmarks to compare their measurement targets, protocols, and controls."}</p>`;
      return;
    }
    const items = ids.map((id) => byId.get(id));
    const rows = [
      [
        zh ? "领域 / 公开记录" : "Area / recorded date",
        (item) => `${item.area} · ${item.released}`,
      ],
      [zh ? "测量对象" : "Measurement target", (item) => item.summary],
      [zh ? "结论边界" : "Claim boundary", (item) => item.scoreSupports],
      [zh ? "规模（来源原文）" : "Scale", (item) => item.scale],
      [zh ? "能力" : "Capabilities", (item) => item.capabilities.join(" · ")],
      [zh ? "环境" : "Environment", (item) => item.environment.join(" · ")],
      [zh ? "协议" : "Protocol", (item) => item.protocol.join(" · ")],
      [
        zh ? "公平比较条件" : "Controls",
        (item) => item.comparison_controls.join(" "),
      ],
      [
        zh ? "各自设置的选录结果" : "Recorded result in its own setting",
        (item) =>
          item.result
            ? `${item.result.label}: ${item.result.score}${item.result.unit} · ${item.result.model} · ${item.result.method} · ${item.result.metric} · ${item.result.scope}`
            : zh
              ? "尚未收录结构化结果；见一手来源。"
              : "No structured result recorded; consult primary sources.",
      ],
      [zh ? "结果任务" : "Result task", item => item.result?.task],
      [zh ? "结果数据切分" : "Result split", item => item.result?.split],
      [zh ? "结果协议版本" : "Result protocol version", item => item.result?.protocolVersion],
      [zh ? "上下文条件（来源原文）" : "Context conditions", item => item.result?.context || (zh ? "未在本记录中报告" : "Not reported in this record")],
      [zh ? "资源预算（来源原文）" : "Resource budget", item => item.result?.budget || (zh ? "未在本记录中报告" : "Not reported in this record")],
      [zh ? "结果报告日期" : "Result reported", item => item.result?.reportedAt],
      [
        zh ? "结果核验日期" : "Result verified",
        (item) => item.result?.verifiedAt || "—",
      ],
    ];
    const resultLinks = items
      .map(
        (item) =>
          `<td>${item.result ? `<a href="${escapeHtml(item.result.source)}">${zh ? "结果原始来源" : "Original result source"}</a>` : "—"}</td>`,
      )
      .join("");
    output.innerHTML = `<p class="content-note">${zh ? `完整保留 ${ids.length} 个基准。不同基准的分数不可据此排列系统优劣；横向滚动查看全部列。` : `All ${ids.length} selected benchmarks are preserved. Scores from different benchmarks are not a basis for ranking systems. Scroll horizontally to see every column.`}</p><div class="table-scroll" role="region" tabindex="0" aria-label="${zh ? "全部基准对照表" : "All selected benchmarks"}"><table><caption>${zh ? "基准测量设计对照" : "Benchmark measurement design comparison"}</caption><thead><tr><th scope="col">${zh ? "比较维度" : "Dimension"}</th>${items.map((item) => `<th scope="col"><a href="../benchmarks/${escapeHtml(item.id)}/">${escapeHtml(item.name)}</a></th>`).join("")}</tr></thead><tbody>${rows.map(([label, value]) => `<tr><th scope="row">${label}</th>${items.map((item) => `<td>${escapeHtml(value(item) || "—")}</td>`).join("")}</tr>`).join("")}<tr><th scope="row">${zh ? "来源" : "Sources"}</th>${resultLinks}</tr></tbody></table></div>`;
  }
  function restore() {
    ids = [
      ...new Set(new URLSearchParams(location.search).getAll("benchmark")),
    ].filter((id) => byId.has(id));
    render();
  }
  controls.addEventListener("change", (event) => {
    const select = event.target.closest("[data-compare-select]");
    if (!select) return;
    const slot = Number(select.dataset.slot);
    const values = [...ids];
    values[slot] = select.value;
    ids = [...new Set(values.filter(Boolean))];
    render("push");
    controls.querySelector(`[data-slot="${Math.min(slot, ids.length)}"]`)?.focus();
  });
  window.addEventListener("popstate", restore);
  restore();
}
export function initCompareWorkspaces() {
  for (const root of document.querySelectorAll("[data-compare-workspace]"))
    initCompare(root);
}
