from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def update_library(path: Path, lang: str):
    text = path.read_text(encoding="utf-8")
    if lang == "zh":
        timeline = (
            "| 2026-09-01 | [EAL-Bench](https://arxiv.org/abs/2609.01836) <!-- benchmark-id:eal-bench --> | Agent Memory | 🔭 前沿 | 把持久记忆中的授权错误拆成“虚假权限形成”与“错误权限向真实行动传播”两阶段。 |\n"
            "| 2026-09-01 | [The Memory Trust Gap](https://arxiv.org/abs/2609.01852) <!-- benchmark-id:memory-trust-gap --> | Agent Memory | 🔭 前沿 | 把过期记忆与当前权威证据冲突做成受控实验，并显式测量失败如何随模型能力变化。 |\n"
        )
        amap = (
            "| 🔭 前沿 | [EAL-Bench](https://arxiv.org/abs/2609.01836) <!-- benchmark-id:eal-bench --> | 2026-09-01 | 持久记忆中的授权状态保持、虚假权限形成与越权行动传播。 | 把记忆安全从“内容是否正确”推进到“权限是否被忠实保持并影响行动”。 |\n"
            "| 🔭 前沿 | [The Memory Trust Gap](https://arxiv.org/abs/2609.01852) <!-- benchmark-id:memory-trust-gap --> | 2026-09-01 | 过期记忆与当前权威证据冲突时的过度信任，以及模型规模效应。 | 把记忆冲突失败从单一模型现象推进到能力依赖的受控比较。 |\n"
        )
    else:
        timeline = (
            "| 2026-09-01 | [EAL-Bench](https://arxiv.org/abs/2609.01836) <!-- benchmark-id:eal-bench --> | Agent Memory | 🔭 Frontier | Separates false-authority formation in persistent memory from propagation into unauthorized downstream actions. |\n"
            "| 2026-09-01 | [The Memory Trust Gap](https://arxiv.org/abs/2609.01852) <!-- benchmark-id:memory-trust-gap --> | Agent Memory | 🔭 Frontier | Turns stale-memory conflict with current authoritative evidence into a controlled capability-dependent evaluation. |\n"
        )
        amap = (
            "| 🔭 Frontier | [EAL-Bench](https://arxiv.org/abs/2609.01836) <!-- benchmark-id:eal-bench --> | 2026-09-01 | Preservation of evolving authorization state, false-authority formation, and propagation into unauthorized action. | Moves memory safety from content correctness to whether authority is faithfully preserved and operationalized. |\n"
            "| 🔭 Frontier | [The Memory Trust Gap](https://arxiv.org/abs/2609.01852) <!-- benchmark-id:memory-trust-gap --> | 2026-09-01 | Over-trust of stale memory against current authoritative evidence, including model-scale effects. | Turns memory conflict from a single-model failure into a capability-dependent controlled comparison. |\n"
        )
    if "benchmark-id:eal-bench" not in text:
        text = text.replace("| 2026-08-26 | [SCALE-QA]", timeline + "| 2026-08-26 | [SCALE-QA]", 1)
        marker = "<!-- COMPLETE-MAP:agent-memory:END -->"
        text = text.replace(marker, amap + marker, 1)
    path.write_text(text, encoding="utf-8")


def update_signal(path: Path, lang: str):
    text = path.read_text(encoding="utf-8")
    start = text.index("<!-- FRONTIER-SIGNALS:START -->")
    end = text.index("<!-- FRONTIER-SIGNALS:END -->", start)
    block = text[start:end]
    if lang == "zh":
        row = "| **Agent Memory** | 最新信号从“记忆内容是否安全”继续推进到**记忆是否保留授权与来源权威，以及错误记忆是否真正改变行动**。EAL-Bench 把虚假权限形成与越权传播拆开；The Memory Trust Gap 则把过期记忆与当前权威证据冲突做成能力规模受控实验。 | [EAL-Bench](https://arxiv.org/abs/2609.01836) · [The Memory Trust Gap](https://arxiv.org/abs/2609.01852) · [AuthMem-Bench](https://arxiv.org/abs/2608.01679) |"
    else:
        row = "| **Agent Memory** | The newest signal moves beyond whether memory content is safe to **whether memory preserves authorization/source authority and whether bad memory changes actions**. EAL-Bench separates false-authority formation from unauthorized-action propagation; The Memory Trust Gap makes stale-memory conflict with current authoritative evidence a capability-controlled experiment. | [EAL-Bench](https://arxiv.org/abs/2609.01836) · [The Memory Trust Gap](https://arxiv.org/abs/2609.01852) · [AuthMem-Bench](https://arxiv.org/abs/2608.01679) |"
    block = re.sub(r"^\| \*\*Agent Memory\*\* \|.*$", row, block, count=1, flags=re.MULTILINE)
    text = text[:start] + block + text[end:]
    path.write_text(text, encoding="utf-8")


def update_web_contract():
    path = ROOT / "web/tests/generated-pages.test.mjs"
    text = path.read_text(encoding="utf-8")
    old = 'for (const token of ["frontierShifts", "getProgressPoint", "genealogy", "Evaluation frontier"]) assert.ok(frontier.includes(token), token);'
    new = 'for (const token of ["frontierShifts", "recentItems", "freshness.discovery_scan_at", "genealogy", "Evaluation frontier"]) assert.ok(frontier.includes(token), token);'
    if old not in text:
        raise RuntimeError("frontier web contract shape changed unexpectedly")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


update_library(ROOT / "library/README.md", "zh")
update_library(ROOT / "library/README.en.md", "en")
update_signal(ROOT / "README.md", "zh")
update_signal(ROOT / "README.en.md", "en")
update_web_contract()
