import {
  calendarWindow,
  inReleaseWindow,
  isoDay,
} from "../lib/release-time.mjs";
import { writePageState } from "./page-state.mjs";
export function initTimelines() {
  for (const root of document.querySelectorAll("[data-timeline]")) {
    const form = root.querySelector("[data-timeline-form]");
    const records = [...root.querySelectorAll("[data-timeline-record]")];
    const months = [...root.querySelectorAll("[data-timeline-month]")];
    const window = calendarWindow(root.dataset.asOf);
    const controls = Object.fromEntries(
      [...form.elements].filter((el) => el.name).map((el) => [el.name, el]),
    );
    function render(mode = "replace") {
      const query = controls.q.value.trim().toLocaleLowerCase();
      const area = controls.area.value,
        month = controls.month.value,
        all = controls.window.value === "all";
      let count = 0;
      for (const row of records) {
        const matches =
          (!query || row.dataset.search.includes(query)) &&
          (!area || row.dataset.area === area) &&
          (!month || row.dataset.released.startsWith(month)) &&
          (all || inReleaseWindow({ released: row.dataset.released }, window));
        row.hidden = !matches;
        if (matches) count++;
      }
      for (const group of months)
        group.hidden = !group.querySelector(
          "[data-timeline-record]:not([hidden])",
        );
      root.querySelector("[data-timeline-count]").textContent = String(count);
      root.querySelector("[data-timeline-empty]").hidden = count !== 0;
      root.querySelector("[data-timeline-range]").textContent =
        month ||
        (all
          ? root.dataset.lang === "zh"
            ? "全部历史"
            : "All history"
          : `${isoDay(window.start)} — ${root.dataset.asOf}`);
      const params = new URLSearchParams();
      if (query) params.set("q", controls.q.value.trim());
      if (area) params.set("area", area);
      if (all) params.set("window", "all");
      if (month) params.set("month", month);
      writePageState(params, mode);
    }
    function restore() {
      const params = new URLSearchParams(location.search);
      for (const [name, control] of Object.entries(controls))
        control.value = params.get(name) || (name === "window" ? "recent" : "");
      if (!controls.window.value) controls.window.value = "recent";
      render();
    }
    form.addEventListener("input", (event) => {
      if (event.target.name === "q") render();
    });
    form.addEventListener("change", (event) => {
      if (event.target.name === "month" && controls.month.value)
        controls.window.value = "all";
      if (event.target.name === "window") controls.month.value = "";
      render("push");
    });
    form.addEventListener("submit", (event) => {
      event.preventDefault();
      render();
    });
    form.addEventListener("reset", () => {
      queueMicrotask(() => render("push"));
    });
    globalThis.addEventListener("popstate", restore);
    restore();
  }
}
