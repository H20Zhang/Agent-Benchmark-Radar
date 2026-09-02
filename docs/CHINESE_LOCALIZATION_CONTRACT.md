# Chinese Localization Contract

The Chinese GitHub Pages surface is a Chinese research tool, not a mixed-language mirror of the English site.

## Keep canonical English only when it is the identifier

Keep benchmark names, model names, method/system names, dataset names, metric identifiers, acronyms, API/tool names, paper titles, and code/protocol identifiers in their canonical form when translation would make them harder to recognize. Examples: `LoCoMo`, `GPT-5`, `BM25`, `MRR@10`, `Recall@5`, `Spider 2.0`, `OpenHands`.

## Translate ordinary technical prose

Ordinary concepts in Chinese prose should normally be Chinese, even when the English term is common in papers. Prefer:

- memory → 记忆
- query → 查询
- retrieval → 检索
- write representation / write-side representation → 写入表征 / 写入侧表征
- enrichment → 增强
- embedder / embedding model → 嵌入模型
- reranker → 重排模型
- downstream → 下游
- utility → 效用
- benchmark / leaderboard / protocol / split / task → 基准 / 排行榜 / 评测协议 / 数据切分 / 任务 when used as prose, while canonical names remain unchanged
- full context → 完整上下文
- oracle → Oracle when it is a named protocol setting; otherwise use “理想信息/Oracle 设置” on first mention

Do not create dense phrases such as “write enrichment 的 downstream utility” when natural Chinese can say “写入增强能否改善下游任务效用”.

## UI language

On `/zh/`, all navigation, section titles, eyebrow labels, buttons, status labels, explanatory labels, empty states, helper copy, and table headers must be Chinese. Canonical entities inside the value may stay English.

Good: `当前最佳 · Hindsight (Gemini-3)`.
Bad: `Current best · Hindsight (Gemini-3)`.

## Bilingual terminology

Use `中文（English）` only when the English term is genuinely useful for disambiguation or search. Do not repeat English after every common technical concept.

## Result data

`data/results/*.json` must localize human-facing track labels with `label.zh`. Method/model identities remain canonical. Task/split/protocol values are provenance fields and may remain canonical English internally; the renderer must label those fields in Chinese and should prefer localized display text when a localized value is available.

## Detail notes

Chinese benchmark notes should read as native Chinese prose. Code identifiers, benchmark names, metrics, model/method names and concise math notation are exempt. Avoid full English clauses and avoid unnecessary English common nouns embedded in Chinese sentences.

## Validation

Validators should reject known English UI labels on Chinese pages and flag Chinese benchmark notes with suspiciously dense English common-noun usage for manual cleanup. The detector is a guardrail, not a reason to translate canonical names mechanically.
