#!/usr/bin/env python3
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BENCH = ROOT / "benchmarks"
EDITORIAL = ROOT / ".editorial"
START = "<!-- RESEARCH-DECISION:START -->"
END = "<!-- RESEARCH-DECISION:END -->"


def load_entries():
    rows = []
    for path in sorted(EDITORIAL.glob("*.json")):
        rows.extend(json.loads(path.read_text()))
    by_id = {row["id"]: row for row in rows}
    if len(rows) != 126 or len(by_id) != 126:
        raise SystemExit(f"expected 126 unique editorial entries, got {len(rows)} rows / {len(by_id)} ids")
    return by_id


def decision_block(row, lang):
    if lang == "zh":
        related = " · ".join(f"[{x}]({x}.md)" for x in row["related"])
        return f'''{START}\n\n## 研究决策卡\n\n### 什么时候值得用\n\n{row["judgment"]["zh"]}\n\n### 一个具体任务长什么样\n\n{row["example"]["zh"]}\n\n### 最有判别力的实验\n\n{row["experiment"]["zh"]}\n\n### 建议搭配\n\n{related}\n\n> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。\n\n{END}'''
    related = " · ".join(f"[{x}]({x}.en.md)" for x in row["related"])
    return f'''{START}\n\n## Research decision card\n\n### When to use it\n\n{row["judgment"]["en"]}\n\n### What a concrete task looks like\n\n{row["example"]["en"]}\n\n### Most discriminating experiment\n\n{row["experiment"]["en"]}\n\n### Pair with\n\n{related}\n\n> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.\n\n{END}'''


def apply_page(path, row, lang):
    text = path.read_text()
    block = decision_block(row, lang)
    if START in text:
        text = re.sub(re.escape(START) + r".*?" + re.escape(END), block, text, flags=re.S)
    else:
        # Put the decision card before genealogy/evolution when possible; otherwise append.
        candidates = ["\n## 演化位置", "\n## Evolution position", "\n## Genealogy"]
        pos = next((text.find(h) for h in candidates if text.find(h) >= 0), -1)
        if pos >= 0:
            text = text[:pos].rstrip() + "\n\n" + block + "\n" + text[pos:]
        else:
            text = text.rstrip() + "\n\n" + block + "\n"
    path.write_text(text)


def rewrite_onboarding(path, lang):
    text = path.read_text()
    if lang == "zh":
        body = '''<!-- ONBOARDING:START -->\n<div align="center">\n\n<h1>Agent Benchmark Radar</h1>\n\n<p><strong>不是 Benchmark 清单，而是一张 Agent Evaluation 的研究地图。</strong></p>\n\n<p>覆盖 <b>Agent Memory</b> · <b>RAG / Agentic Retrieval</b> · <b>Data Agents</b><br/>\n从 <b>测什么 → 怎么公平比较 → 分数能证明什么 → 下一步还该测什么</b> 组织 126 个 Benchmark。</p>\n\n<p><strong>中文</strong> · <a href="README.en.md">English</a></p>\n\n<p><a href="https://github.com/H20Zhang/Agent-Benchmark-Radar/actions/workflows/validate.yml"><img alt="Validation" src="https://github.com/H20Zhang/Agent-Benchmark-Radar/actions/workflows/validate.yml/badge.svg"></a> <a href="https://github.com/H20Zhang/Agent-Benchmark-Radar/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/H20Zhang/Agent-Benchmark-Radar?style=flat"></a> <img alt="Last commit" src="https://img.shields.io/github/last-commit/H20Zhang/Agent-Benchmark-Radar?style=flat"></p>\n</div>\n\n## 先做研究判断，再选 Benchmark\n\n| 你现在要回答的问题 | 入口 | 你应该带走什么 |\n|---|---|---|\n| **最近评测范式变了什么？** | [近 30 天信号](#frontier-signals) | 哪些变化会改变实验设计，而不是只多了一个数据集。 |\n| **我的 claim 应该用什么测？** | [Evaluation Recipes](#evaluation-recipes) | Core + Complement + 下一项判别实验。 |\n| **某个 Benchmark 的分数到底说明什么？** | [完整 Benchmark Library](#all-benchmarks) | 进入详情页看 protocol、claim boundary、混杂因素和研究决策卡。 |\n| **哪里还有真正的评测空白？** | [下一阶段关键评测方向](#evaluation-frontiers) | 从已有证据走向尚未被测量的坐标。 |\n\n### 三条主线\n\n| 方向 | 现在真正难的是什么 | 能力地图 | 评测组合 | 完整列表 |\n|---|---|---|---|---|\n| **Agent Memory** | 从“能召回”走向状态更新、经验迁移、多模态与安全生命周期。 | [Memory Map](#benchmark-memory) | [Memory Recipes](#recipe-memory) | [Memory Benchmarks](#registry-memory) |\n| **RAG / Agentic Retrieval** | 从静态相关性走向长程搜索、动态语料、轨迹诊断与可验证研究交付。 | [Retrieval Map](#benchmark-rag) | [Retrieval Recipes](#recipe-rag) | [Retrieval Benchmarks](#registry-rag) |\n| **Data Agents** | 从 SQL/code 正确走向数据发现、业务语义、完整工作流与可执行交付。 | [Data Agent Map](#benchmark-data) | [Data Agent Recipes](#recipe-data) | [Data Agent Benchmarks](#registry-data) |\n\n> **本 Radar 的默认证据纪律：** “论文报告过的最好结果”不等于“当前 SOTA”；“距满分还有多少”不等于“可实现 headroom”；不同 protocol cell 的分数不直接比较。详情页优先告诉你 **compared to what、so what、what could fool us**。\n\n_Registry 以可复用 benchmark / evaluation contribution 为收录单元；完整规则见 [Curation](CURATION.md)。_\n\n---\n<!-- ONBOARDING:END -->'''
    else:
        body = '''<!-- ONBOARDING:START -->\n<div align="center">\n\n<h1>Agent Benchmark Radar</h1>\n\n<p><strong>Not a benchmark list: a research map of agent evaluation.</strong></p>\n\n<p>Covering <b>Agent Memory</b> · <b>RAG / Agentic Retrieval</b> · <b>Data Agents</b><br/>\n126 benchmarks organized by <b>what is measured → what a fair comparison requires → what a score supports → what remains unmeasured</b>.</p>\n\n<p><a href="README.md">中文</a> · <strong>English</strong></p>\n\n<p><a href="https://github.com/H20Zhang/Agent-Benchmark-Radar/actions/workflows/validate.yml"><img alt="Validation" src="https://github.com/H20Zhang/Agent-Benchmark-Radar/actions/workflows/validate.yml/badge.svg"></a> <a href="https://github.com/H20Zhang/Agent-Benchmark-Radar/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/H20Zhang/Agent-Benchmark-Radar?style=flat"></a> <img alt="Last commit" src="https://img.shields.io/github/last-commit/H20Zhang/Agent-Benchmark-Radar?style=flat"></p>\n</div>\n\n## Make the research decision before picking a benchmark\n\n| Question you need to answer | Start here | What you should take away |\n|---|---|---|\n| **What changed in evaluation recently?** | [30-day signals](#frontier-signals) | Changes that alter experimental design, not merely another dataset. |\n| **What should measure my claim?** | [Evaluation Recipes](#evaluation-recipes) | Core + Complement + the next discriminating experiment. |\n| **What does a benchmark score actually establish?** | [Complete Benchmark Library](#all-benchmarks) | Open a detail page for protocol, claim boundary, confounders, and its research decision card. |\n| **Where is the real evaluation gap?** | [Evaluation frontiers](#evaluation-frontiers) | Move from current evidence to a genuinely unmeasured coordinate. |\n\n### Three research lines\n\n| Area | What is hard now | Capability map | Evaluation suite | Full registry |\n|---|---|---|---|---|\n| **Agent Memory** | From recall to state updates, experience transfer, multimodality, and lifecycle safety. | [Memory Map](#benchmark-memory) | [Memory Recipes](#recipe-memory) | [Memory Benchmarks](#registry-memory) |\n| **RAG / Agentic Retrieval** | From static relevance to long-horizon search, dynamic corpora, trace diagnosis, and verifiable research deliverables. | [Retrieval Map](#benchmark-rag) | [Retrieval Recipes](#recipe-rag) | [Retrieval Benchmarks](#registry-rag) |\n| **Data Agents** | From SQL/code correctness to discovery, business semantics, complete workflows, and executable deliverables. | [Data Agent Map](#benchmark-data) | [Data Agent Recipes](#recipe-data) | [Data Agent Benchmarks](#registry-data) |\n\n> **Default evidence discipline:** “best result reported in a paper” is not “current SOTA”; distance to 100% is not realizable research headroom; scores from different protocol cells are not directly comparable. Detail pages prioritize **compared to what, so what, and what could fool us**.\n\n_The Registry tracks reusable benchmark / evaluation contributions. See [Curation](CURATION.md) for the full policy._\n\n---\n<!-- ONBOARDING:END -->'''
    text = re.sub(r"<!-- ONBOARDING:START -->.*?<!-- ONBOARDING:END -->", body, text, flags=re.S)
    # Tighten result-table claims without changing source-backed values.
    if lang == "zh":
        text = text.replace("| Benchmark | 当前已核验坐标 | 当前最佳 | 研究判断 |", "| Benchmark | 已核验 protocol cell | 已收录结果 | 如何读这个结果 |")
        text = text.replace("当前已为 12 个 Benchmark 建立来源核验的结构化结果轨道；每项成绩都绑定 task、split、protocol、metric、方向、日期与原始来源。", "当前为 12 个 Benchmark 建立来源核验的结构化结果轨道。这里展示的是 **已收录、可追溯的 protocol cell**，不是在没有完整排行榜核验时宣称 current SOTA；每项结果绑定 task、split、protocol、metric、方向、日期与原始来源。")
    else:
        text = text.replace("| Benchmark | Current verified coordinate | Current best | Research judgment |", "| Benchmark | Verified protocol cell | Collected result | How to read it |")
        text = text.replace("We currently maintain source-verified structured result tracks for 12 benchmarks; every score is bound to task, split, protocol, metric, direction, date, and primary source.", "We currently maintain source-verified structured result tracks for 12 benchmarks. These are **collected, traceable protocol cells**, not claims of current SOTA without exhaustive leaderboard verification; every result is bound to task, split, protocol, metric, direction, date, and primary source.")
    path.write_text(text)


def remove_runtime_padding():
    path = ROOT / "web/src/lib/deep-reads.mjs"
    text = path.read_text()
    text = text.replace('import { loadRegistry } from "./registry.mjs";\n', '')
    start = text.index("const DEPTH_WITNESSES = [")
    end = text.index("export function loadDeepRead", start)
    text = text[:start] + text[end:]
    pattern = re.compile(r'''export function loadDeepRead\(id, lang\) \{.*?\n\}''', re.S)
    replacement = '''export function loadDeepRead(id, lang) {\n  const filename = `${id}${lang === "en" ? ".en" : ""}.md`;\n  const path = fromRepositoryRoot("benchmarks", filename);\n  if (!existsSync(path)) return undefined;\n  const markdown = readFileSync(path, "utf8");\n  const publicMarkdown = markdown\n    .replaceAll("最强混淆", "公平比较条件")\n    .replaceAll("最主要的混杂因素", "公平比较条件")\n    .replaceAll("结论上限", "分数支持的判断")\n    .replaceAll("还没有覆盖什么", "下一步评测坐标")\n    .replaceAll("未覆盖", "下一步评测坐标")\n    .replaceAll("Strongest confounder", "Fair comparison conditions")\n    .replaceAll("Score ceiling", "What the score supports")\n    .replaceAll("Remaining gap", "Next evaluation coordinate");\n  return { id, lang, markdown, html: renderDeepReadMarkdown(publicMarkdown) };\n}'''