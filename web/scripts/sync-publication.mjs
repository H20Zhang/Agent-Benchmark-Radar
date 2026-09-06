/** Rebuild publication projections from canonical data. Run with --check in CI. */
import { readFileSync, writeFileSync } from "node:fs";
import { loadRegistry } from "../src/lib/registry.mjs";
import { loadChineseSummaries } from "../src/lib/readme-localization.mjs";
import { publicationWindow } from "../src/lib/publication.mjs";
import {
  chronological,
  releaseDate,
  releaseLabel,
  inReleaseWindow,
  isoDay,
} from "../src/lib/release-time.mjs";
import { loadAllResultSets, presentResult } from "../src/lib/results.mjs";
import { fromRepositoryRoot } from "../src/lib/repository-path.mjs";
const records = [...loadRegistry()],
  byId = new Map(records.map((item) => [item.id, item]));
const chinese = loadChineseSummaries(),
  period = publicationWindow(),
  results = loadAllResultSets();
const recipes = JSON.parse(
  readFileSync(fromRepositoryRoot("data", "recipes.json"), "utf8"),
);
const areas = {
  "agent-memory": "Agent Memory",
  rag: "RAG / Agentic Retrieval",
  "data-agent": "Data Agents",
};
const roles = {
  zh: {
    precursor: "🌱 前身",
    foundation: "🧱 基石",
    transition: "↗ 过渡",
    frontier: "🔭 前沿",
  },
  en: {
    precursor: "🌱 Precursor",
    foundation: "🧱 Foundation",
    transition: "↗ Transition",
    frontier: "🔭 Frontier",
  },
};
const suffix = { "agent-memory": "memory", rag: "rag", "data-agent": "data" };
const clean = (text) =>
  String(text ?? "")
    .replaceAll("|", "&#124;")
    .replace(/\n+/g, " ");
const summary = (item, lang) =>
  lang === "zh" ? chinese.get(item.id) : item.summary;
const primary = (item) =>
  item.artifacts.paper ||
  item.artifacts.project ||
  item.artifacts.code ||
  item.artifacts.data;
const link = (id, marker = false) => {
  const item = byId.get(id);
  return `[${item.name}](${primary(item)})${marker ? ` <!-- benchmark-id:${id} -->` : ""}`;
};
const block = (label, text) =>
  `<!-- ${label}:START -->\n\n${text.trim()}\n\n<!-- ${label}:END -->`;
const replaceBlock = (source, label, text) => {
  const start = `<!-- ${label}:START -->`,
    end = `<!-- ${label}:END -->`;
  const a = source.indexOf(start),
    b = source.indexOf(end, a);
  if (a < 0 || b < 0) throw new Error(`Missing projection markers ${label}`);
  return source.slice(0, a) + block(label, text) + source.slice(b + end.length);
};
const nameCmp = (a, b) =>
  a.name.toLowerCase() < b.name.toLowerCase()
    ? -1
    : a.name.toLowerCase() > b.name.toLowerCase()
      ? 1
      : a.id.localeCompare(b.id);
const oldest = (items) =>
  [...items].sort(
    (a, b) => a.released.localeCompare(b.released) || nameCmp(a, b),
  );
const newest = (items) =>
  [...items].sort(
    (a, b) => b.released.localeCompare(a.released) || nameCmp(a, b),
  );
function intro(lang) {
  const zh = lang === "zh";
  return `<div align="center">\n\n<h1>Agent Benchmark Radar</h1>\n\n<p><strong>${zh ? "先看最新基准，再读评测设计与结果证据。" : "Start with benchmark chronology, then inspect evaluation design and result evidence."}</strong></p>\n<p>${zh ? `按时间与领域组织 ${records.length} 个 Benchmark` : `${records.length} benchmarks organized by time and area`}：<b>Agent Memory</b> · <b>RAG / Agentic Retrieval</b> · <b>Data Agents</b></p>\n<p>${zh ? "中文 · [English](README.en.md)" : "[中文](README.md) · English"} · <a href="https://h20zhang.github.io/Agent-Benchmark-Radar/${lang}/">Website</a></p>\n\n</div>\n\n${zh ? "[最近六个月](#release-timeline) · [全部基准](#all-benchmarks) · [评测组合](#evaluation-recipes) · [研究观察](#frontier-signals)" : "[Last six months](#release-timeline) · [All benchmarks](#all-benchmarks) · [Evaluation suites](#evaluation-recipes) · [Research observations](#frontier-signals)"}\n\n| ${zh ? "领域 | 能力地图 | 评测组合 | 完整列表" : "Area | Capability map | Evaluation suite | Full registry"} |\n|---|---|---|---|\n${Object.entries(
    areas,
  )
    .map(
      ([id, name]) =>
        `| ${name} | [${zh ? "地图" : "Map"}](#benchmark-${suffix[id]}) | [${zh ? "组合" : "Recipes"}](#recipe-${suffix[id]}) | [${zh ? "全部" : "Registry"}](#registry-${suffix[id]}) |`,
    )
    .join(
      "\n",
    )}\n\n> ${zh ? "时间记录与日期来源分开核验；月份精度不补造日期。领域阶段、评测组合和研究机会属于编辑解读，不是客观排名。结果只代表所收录来源，不宣称当前 SOTA。" : "Date events and sources are tracked separately; month precision does not imply an invented day. Stages, suites, and opportunities are editorial interpretations, not objective rankings. Results describe recorded sources, not current SOTA."}\n\n${zh ? "[收录规则](CURATION.md) · [日期与证据规范](SCHEMA.md)" : "[Curation policy](CURATION.md) · [Date and evidence schema](SCHEMA.md)"}`;
}
function recent(lang) {
  const zh = lang === "zh",
    items = chronological(records).filter((item) =>
      inReleaseWindow(item, period.recent),
    );
  return `<a id="release-timeline"></a>\n## ${zh ? "最近六个月 Benchmark 时间线" : "Benchmark Timeline: Last Six Months"}\n\n${zh ? "发现扫描窗口" : "Discovery window"}：**${isoDay(period.recent.start)} — ${period.asOf}** · ${items.length} ${zh ? "个记录" : "records"}\n\n${zh ? "日期下的类型说明区分最早公开、正式发表与事件类型待复核的历史记录；月份精度按区间重叠纳入。这个表不会因会议发表而把已公开基准重新包装成首发。" : "Date annotations distinguish earliest public versions, publications, and historical dates whose event type remains unclassified. Month-precision intervals are included when they overlap the window; conference publication does not relaunch an already public benchmark."}\n\n${block(
    "TABLE-FIRST:RECENT",
    `| ${zh ? "时间 | 方向 | Benchmark | 考察内容" : "Time | Area | Benchmark | What it measures"} |\n|---|---|---|---|\n${items
      .map((item) => {
        const release = releaseDate(item);
        return `| ${release.date}<br><sub>${releaseLabel(release, lang)} · [${zh ? "来源" : "source"}](${release.source || primary(item)})</sub> | ${areas[item.area]} | ${link(item.id, true)} | ${clean(summary(item, lang))} |`;
      })
      .join("\n")}`,
  )}\n\n`;
}
function recipeProjection(lang) {
  const zh = lang === "zh";
  return `<a id="evaluation-recipes"></a>\n## ${zh ? "Evaluation Recipes：按研究主张配评测" : "Evaluation Recipes: Build the Suite from Your Claim"}\n\n${zh ? "以下是编辑建议，不是自动成立的实验结论。核心评测、补充评测与完整协议共同限定支持范围。修改组合后，必须重新核验原主张。" : "These editorial suggestions are not automatic experimental conclusions. Core and complementary measurements only support a claim under the complete protocol. Changing the selection requires revalidating its claim."}\n\n${Object.entries(
    areas,
  )
    .map(
      ([area, name]) =>
        `<a id="recipe-${suffix[area]}"></a>\n### ${name}\n\n| ${zh ? "你想证明 | Core | Complement | 下一步验证" : "Claim you want to support | Core | Complement | Next validation"} |\n|---|---|---|---|\n${recipes
          .filter((r) => r.area === area)
          .map(
            (r) =>
              `| **${clean(r.claim[lang])}** | ${r.core.map((id) => link(id)).join(" · ")} | ${r.complement.map((id) => link(id)).join(" · ")} | ${clean(r.next_validation[lang])} |`,
          )
          .join("\n")}`,
    )
    .join("\n\n")}\n\n`;
}
function resultProjection(lang) {
  const zh = lang === "zh";
  const rows = [...results]
    .map(([id, rs]) => ({ item: byId.get(id), rs }))
    .sort(
      (a, b) =>
        b.rs.verified_at.localeCompare(a.rs.verified_at) ||
        nameCmp(a.item, b.item),
    )
    .slice(0, 6);
  return `<a id="result-snapshots"></a>\n### ${zh ? "已收录的结果快照" : "Recorded Result Snapshots"}\n\n${zh ? `已为 **${results.size} 个基准**整理结构化结果；下表仅展示最近核验的 ${rows.length} 项，不是排行榜。` : `Structured result records cover **${results.size} benchmarks**. The table shows the ${rows.length} most recently verified records, not a leaderboard.`} ${zh ? "单条基线不称当前最好；距满分的差值不作为研究空间。" : "A single recorded baseline is not a current best; distance to a ceiling is not research headroom."}\n\n| Benchmark | ${zh ? "记录范围 | 结果 | 结果核验 | 来源" : "Record scope | Result | Result verified | Source"} |\n|---|---|---:|---|---|\n${rows
    .map(({ item, rs }) => {
      const view = presentResult(rs, lang);
      return `| [${item.name}](https://h20zhang.github.io/Agent-Benchmark-Radar/${lang}/benchmarks/${item.id}/#results) | ${view.label} · ${view.status} · ${clean(view.trackLabel)} | ${view.score}${view.unit} | ${view.verifiedAt} | [${zh ? "原始记录" : "Source"}](${view.source}) |`;
    })
    .join("\n")}\n\n`;
}
let changed = [];
for (const lang of ["zh", "en"]) {
  const filename = lang === "zh" ? "README.md" : "README.en.md";
  let source = readFileSync(fromRepositoryRoot(filename), "utf8");
  const tail = source.slice(source.indexOf('<a id="timeline"></a>'));
  let signal = source.slice(
    source.indexOf('<a id="frontier-signals"></a>'),
    source.indexOf(
      lang === "zh" ? "### 当前成绩追踪" : "### Current Result Tracking",
    ),
  );
  // Subsequent runs use explicit generated result marker.
  if (!signal.includes("FRONTIER-SIGNALS:END"))
    signal = source.slice(
      source.indexOf('<a id="frontier-signals"></a>'),
      source.indexOf('<a id="result-snapshots"></a>'),
    );
  signal =
    signal.trim() +
    `\n\n> ${lang === "zh" ? "以上为编辑观察；代表条目是证据锚点，不代表窗口内全部新基准。完整记录见上方时间线。" : "These are editorial observations. Representative benchmarks are evidence anchors, not a complete window listing; use the timeline above for the complete projection."}\n\n`;
  // Avoid duplicating generated note on repeated invocation.
  const endMarker = "<!-- FRONTIER-SIGNALS:END -->";
  signal =
    signal.slice(0, signal.indexOf(endMarker) + endMarker.length) +
    `\n\n${lang === "zh" ? "观察核验截至" : "Observations verified through"}：${period.asOf}\n\n> ${lang === "zh" ? "编辑观察，不代表窗口内全部新基准；完整记录见时间线。" : "Editorial observations, not a complete window listing; use the timeline for the complete projection."}\n\n`;
  let next =
    block("ONBOARDING", intro(lang)) +
    "\n\n" +
    recent(lang) +
    block("EVALUATION-RECIPES", recipeProjection(lang)) +
    "\n\n" +
    signal +
    block("RESULT-SNAPSHOTS", resultProjection(lang)) +
    "\n\n" +
    tail;
  for (const [area] of Object.entries(areas)) {
    const rows = oldest(records.filter((item) => item.area === area));
    next = replaceBlock(
      next,
      `TABLE-FIRST:AREA:${area}`,
      `| ${lang === "zh" ? "阶段（编辑） | Benchmark | 引用数 (S2) | 时间 | 考察内容" : "Stage (editorial) | Benchmark | Citations (S2) | Time | What it measures"} |\n|---|---|---:|---|---|\n${rows.map((item) => `| ${roles[lang][item.evolution_role]} | ${link(item.id, true)} | ${item.citations.status === "ok" ? `[${item.citations.count.toLocaleString("en-US")}](${item.citations.url})` : "—"} | ${releaseDate(item).date} | ${clean(summary(item, lang))} |`).join("\n")}`,
    );
  }
  next = next
    .replace(/全部 \d+ 个基准/g, `全部 ${records.length} 个基准`)
    .replace(/all \d+ benchmarks/g, `all ${records.length} benchmarks`);
  next = next.replace(/\n{4,}/g, "\n\n\n").trim() + "\n";
  if (next !== source) {
    changed.push(filename);
    if (!process.argv.includes("--check"))
      writeFileSync(fromRepositoryRoot(filename), next);
  }
  // Preserve authored measurement-advance prose, only synchronize dates and order in the legacy full Library.
  const library = `library/${filename}`;
  let old = readFileSync(fromRepositoryRoot(library), "utf8"),
    updated = old;
  for (const label of [
    "COMPLETE-TIMELINE",
    ...Object.keys(areas).map((area) => `COMPLETE-MAP:${area}`),
  ]) {
    const start = `<!-- ${label}:START -->`,
      end = `<!-- ${label}:END -->`;
    if (!updated.includes(start)) continue;
    const body = updated.split(start)[1].split(end)[0];
    const lines = body.trim().split("\n");
    const rowById = new Map(
      lines
        .filter((line) => line.includes("benchmark-id:"))
        .map((line) => [line.match(/benchmark-id:([a-z0-9-]+)/)[1], line]),
    );
    const order =
      label === "COMPLETE-TIMELINE"
        ? newest(records)
        : oldest(records.filter((item) => item.area === label.split(":")[1]));
    const rows = order.map((item) => {
      let row = rowById.get(item.id);
      if (!row)
        throw new Error(`Missing authored library row ${library}/${item.id}`);
      return row.replace(/\b\d{4}-\d{2}(?:-\d{2})?\b/g, (match) =>
        match === item.release_date_evidence?.legacy_recorded_at?.date
          ? item.released
          : match,
      );
    });
    updated = replaceBlock(
      updated,
      label,
      [
        ...lines.filter((line) => !line.includes("benchmark-id:")),
        ...rows,
      ].join("\n"),
    );
  }
  if (updated !== old) {
    changed.push(library);
    if (!process.argv.includes("--check"))
      writeFileSync(fromRepositoryRoot(library), updated);
  }
}
if (process.argv.includes("--check") && changed.length) {
  console.error("Stale publication projections: " + changed.join(", "));
  process.exitCode = 1;
} else
  console.log(
    `Publication projection ${process.argv.includes("--check") ? "verified" : "synchronized"}: ${records.length} benchmarks, ${results.size} result sets, window ${isoDay(period.recent.start)}—${period.asOf}.`,
  );
