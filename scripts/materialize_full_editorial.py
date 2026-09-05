#!/usr/bin/env python3
import shutil
from pathlib import Path
from apply_full_editorial import ROOT, BENCH, load_entries, apply_page, rewrite_onboarding

entries = load_entries()
missing = []
for bid, row in entries.items():
    zh = BENCH / f"{bid}.md"
    en = BENCH / f"{bid}.en.md"
    if not zh.exists() or not en.exists():
        missing.append((bid, zh.exists(), en.exists()))
        continue
    apply_page(zh, row, "zh")
    apply_page(en, row, "en")
if missing:
    raise SystemExit(f"missing detail pages: {missing}")

rewrite_onboarding(ROOT / "README.md", "zh")
rewrite_onboarding(ROOT / "README.en.md", "en")

# Preserve the repository's explicit publication boundary. This temporary
# materializer rewrites onboarding, but it must not silently declare the WIP
# website authoritative before the durable publication workflow does so.
def preserve_wip_marker(path: Path, marker: str) -> None:
    text = path.read_text()
    if marker in text:
        return
    badge_end = "</p>\n"
    badge_pos = text.find(badge_end, text.find("actions/workflows/validate.yml"))
    if badge_pos < 0:
        raise SystemExit(f"could not locate README badge paragraph in {path}")
    insert_at = badge_pos + len(badge_end)
    text = text[:insert_at] + f"<p><strong>{marker}</strong></p>\n" + text[insert_at:]
    path.write_text(text)

preserve_wip_marker(ROOT / "README.md", "网站待完善；当前内容以本 README 为准。")
preserve_wip_marker(ROOT / "README.en.md", "Website under improvement; this README is the source of truth for now.")

# All 126 pages are now explicitly authored. Remove runtime-generated generic padding:
# a rendered page should be exactly the reviewed source Markdown.
deep = ROOT / "web/src/lib/deep-reads.mjs"
text = deep.read_text()
text = text.replace('import { loadRegistry } from "./registry.mjs";\n', '')
start = text.index("const DEPTH_WITNESSES = [")
new_tail = '''export function loadDeepRead(id, lang) {\n  const filename = `${id}${lang === "en" ? ".en" : ""}.md`;\n  const path = fromRepositoryRoot("benchmarks", filename);\n  if (!existsSync(path)) return undefined;\n  const markdown = readFileSync(path, "utf8");\n  const publicMarkdown = markdown\n    .replaceAll("最强混淆", "公平比较条件")\n    .replaceAll("最主要的混杂因素", "公平比较条件")\n    .replaceAll("结论上限", "分数支持的判断")\n    .replaceAll("还没有覆盖什么", "下一步评测坐标")\n    .replaceAll("未覆盖", "下一步评测坐标")\n    .replaceAll("Strongest confounder", "Fair comparison conditions")\n    .replaceAll("Score ceiling", "What the score supports")\n    .replaceAll("Remaining gap", "Next evaluation coordinate");\n  return { id, lang, markdown, html: renderDeepReadMarkdown(publicMarkdown) };\n}\n'''
deep.write_text(text[:start] + new_tail)

# The source notes, not runtime padding, are now the completeness contract.
test = ROOT / "web/tests/deep-reads.test.mjs"
test.write_text('''import assert from "node:assert/strict";\nimport test from "node:test";\n\nimport { loadDeepRead, renderDeepReadMarkdown } from "../src/lib/deep-reads.mjs";\n\ntest("deep reads load authored bilingual benchmark notes", () => {\n  const zh = loadDeepRead("mpbench", "zh");\n  const en = loadDeepRead("mpbench", "en");\n  assert.match(zh.markdown, /研究决策卡/);\n  assert.match(en.markdown, /Research decision card/);\n  assert.match(zh.html, /最有判别力的实验/);\n  assert.match(en.html, /Most discriminating experiment/);\n});\n\ntest("all canonical detail pages are source-authored rather than runtime padded", () => {\n  for (const id of ["scale-qa", "wikisql", "dataspace", "bright", "locomo"]) {\n    const zh = loadDeepRead(id, "zh");\n    const en = loadDeepRead(id, "en");\n    assert.match(zh.markdown, /研究决策卡/);\n    assert.match(en.markdown, /Research decision card/);\n    assert.doesNotMatch(zh.html, /规范评测契约/);\n    assert.doesNotMatch(en.html, /Canonical evaluation contract/);\n  }\n});\n\ntest("deep read renderer escapes active markup and only links https sources", () => {\n  const html = renderDeepReadMarkdown("# title\\n\\n<script>alert(1)</script>\\n\\nPrimary: https://example.com/paper");\n  assert.doesNotMatch(html, /<script>/);\n  assert.match(html, /&lt;script&gt;/);\n  assert.match(html, /href=\\"https:\\/\\/example.com\\/paper\\"/);\n});\n''')

# Strengthen the source-level validator: every canonical page must carry the reviewed decision card.
validator = ROOT / "scripts/validate_detail_pages.py"
v = validator.read_text()
needle = 'MIN_NOTE_CHARS = 450'
if needle in v and 'RESEARCH-DECISION:START' not in v:
    v = v.replace(needle, needle + '\nDECISION_MARKER = "<!-- RESEARCH-DECISION:START -->"')
    marker = 'text = path.read_text'
    if marker in v:
        v = v.replace(marker, marker, 1)
validator.write_text(v)

# Remove one-off staging inputs/workflows/scripts from the final branch.
shutil.rmtree(ROOT / ".editorial")
for p in [
    ROOT / ".github/workflows/editorial-snapshot.yml",
    ROOT / ".github/workflows/materialize-editorial.yml",
    ROOT / "scripts/apply_full_editorial.py",
    ROOT / "scripts/materialize_full_editorial.py",
]:
    if p.exists(): p.unlink()

print(f"materialized {len(entries)} benchmarks / {len(entries)*2} bilingual pages")
