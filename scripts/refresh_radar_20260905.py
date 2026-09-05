#!/usr/bin/env python3
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "data" / "benchmarks.json"
TODAY = "2026-09-05"

NEW = [
  {
    "id": "authmem-bench",
    "name": "AuthMem-Bench",
    "area": "agent-memory",
    "released": "2026-08-03",
    "importance": 4,
    "status": "verified",
    "evolution_role": "frontier",
    "summary": "Paired evaluation of whether persistent-memory consolidation preserves source authority rather than laundering low-authority content into reusable instructions or user facts.",
    "capabilities": ["memory consolidation", "authority preservation", "authorization", "memory safety", "provenance"],
    "environment": ["persistent memory", "paired source-authority conditions", "action-grounded downstream tasks"],
    "protocol": ["paired focal-claim controls", "write-time collapse audit", "downstream unauthorized-action evaluation", "authority-label intervention"],
    "scale": "7 memory consolidators × 7 LLM backbones, with paired source-authority and action-grounded evaluations",
    "measurement_strength": "Makes source authority a first-class memory invariant by holding remembered content fixed while varying the authority under which it may later be reused.",
    "coverage_gap": "Does not yet establish governance robustness under real multi-principal identity systems, adversarial provenance spoofing, or long-lived production stores.",
    "confounders": ["consolidator", "LLM backbone", "authority metadata policy", "memory write policy", "downstream action harness"],
    "artifacts": {"paper": "https://arxiv.org/abs/2608.01679"},
    "last_verified": TODAY,
    "citations": {"count": None, "source": "semantic-scholar", "updated_at": TODAY, "status": "unmatched"}
  },
  {
    "id": "agent-retrieval-bench",
    "name": "Agent Retrieval Bench",
    "area": "rag",
    "released": "2026-07-27",
    "importance": 4,
    "status": "verified",
    "evolution_role": "frontier",
    "summary": "File-level context-acquisition benchmark for coding agents, where relevance is defined by the repository context an agent needs next rather than direct query–file semantic similarity.",
    "capabilities": ["agentic retrieval", "code retrieval", "context acquisition", "selective retrieval", "abstention"],
    "environment": ["25 software repositories", "frozen base-commit snapshots", "coding-workflow signals"],
    "protocol": ["four positive retrieval tracks", "natural no-gold cases", "counterfactual wrong-repository controls", "token-budgeted context yield"],
    "scale": "427 samples across 25 repositories; 392K files and 7.9M chunks in the released corpus inventory",
    "measurement_strength": "Separates the upstream context-acquisition problem of coding agents from patch generation and evaluates whether retrieved files are useful for the next workflow need.",
    "coverage_gap": "File-level hits do not establish function/span localization or end-to-end test-passing repair, and the current seed intervention is not a full repair benchmark.",
    "confounders": ["repository snapshot", "candidate filtering", "token packing", "retriever", "selective threshold", "context budget"],
    "artifacts": {"paper": "https://arxiv.org/abs/2607.24882", "code": "https://github.com/eyuansu62/agent-retrieval-bench"},
    "last_verified": TODAY,
    "citations": {"count": None, "source": "semantic-scholar", "updated_at": TODAY, "status": "unmatched"}
  },
  {
    "id": "pm-bench",
    "name": "PM-Bench",
    "area": "agent-memory",
    "released": "2026-07-14",
    "importance": 4,
    "status": "verified",
    "evolution_role": "frontier",
    "summary": "Prospective-memory benchmark testing whether agents maintain delayed user intentions and execute them at the correct future cue while continuing ongoing activities.",
    "capabilities": ["prospective memory", "delayed intentions", "cue monitoring", "temporal memory", "ongoing-task coordination"],
    "environment": ["text-based Virtual Week", "simulated seven-day schedule", "latent environment changes"],
    "protocol": ["ongoing activity plus delayed intentions", "future cue monitoring", "eight agent configurations", "F1 evaluation"],
    "scale": "Simulated seven-day Virtual Week; 8 LLMs evaluated under 8 agent configurations",
    "measurement_strength": "Turns remembering to act later—not merely recalling a past fact—into a controlled agent-memory evaluation object.",
    "coverage_gap": "Does not yet cover long real-world time horizons, noisy external calendars/tools, or the cost and safety of triggering deferred actions in production.",
    "confounders": ["agent configuration", "LLM backbone", "cue visibility", "time representation", "ongoing-task policy"],
    "artifacts": {"paper": "https://arxiv.org/abs/2607.12385"},
    "last_verified": TODAY,
    "citations": {"count": None, "source": "semantic-scholar", "updated_at": TODAY, "status": "unmatched"}
  }
]

ZH = {
  "authmem-bench": {
    "summary": "固定记忆内容、只改变来源权威，测持久记忆 consolidation 是否把低权限内容洗成可复用的用户事实或指令。",
    "delta": "把 memory safety 从内容是否被保存推进到‘内容以什么权威被保存并再次使用’。",
  },
  "agent-retrieval-bench": {
    "summary": "在真实代码仓库的冻结 commit 上，测 coding agent 能否找到下一步真正需要阅读的文件，或在无本地证据时正确弃答。",
    "delta": "把 coding-agent 检索从语义相似搜索改成 workflow-next-need context acquisition，并加入自然与反事实 no-gold 控制。",
  },
  "pm-bench": {
    "summary": "在持续进行其他活动时，测智能体能否保留延迟意图，并在未来正确 cue 或状态出现时执行。",
    "delta": "把 Agent Memory 从‘记住过去’扩展到‘记得未来要做什么’，直接测 prospective memory。",
  },
}
EN_DELTA = {
  "authmem-bench": "Moves memory safety from whether content is retained to the authority under which it is retained and later reused.",
  "agent-retrieval-bench": "Redefines coding-agent retrieval around next-workflow context need and adds natural and counterfactual no-gold controls.",
  "pm-bench": "Extends agent memory from remembering the past to remembering what must be done later, directly measuring prospective memory.",
}

DETAILS = {
"authmem-bench": {
"zh": """# AuthMem-Bench：记住内容还不够，还要记住它有没有权威\n\n**中文** | [English](authmem-bench.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)\n\n[论文](https://arxiv.org/abs/2608.01679)\n\n## 它到底测什么\n\nAuthMem-Bench 测 persistent-memory consolidation 是否保留 **source authority**。它用配对设计固定要记住的 claim 与下游任务，只改变来源的权威条件，从而检查同一内容在被整理进长期记忆后，会不会失去“谁有资格让系统把它当成事实或指令”的边界。\n\n## 相比此前评测多测了什么\n\nGateMem 等工作已经把共享记忆的 access control 变成评测对象；AuthMem-Bench 更进一步把风险定位到 **consolidation boundary**：即使最终记忆文本本身没有明显恶意内容，来源约束也可能在摘要、抽取或归一化时被洗掉。\n\n## 决定性证据\n\n论文报告，在 7 种 consolidator × 7 个 LLM backbone 的 49 个配置中，48 个观察到 authority collapse；在受控 action-grounded 条件下，缺少 authority metadata 的 collapsed memory 平均 unauthorized-action rate 为 50.3%。端到端实验中，自动预测并持久保存 authority label 后，观察到的 unauthorized-action rate 从 16.9% 降到 0.0%，同时 benign task success 基本不变。\n\n## 这个分数能证明什么\n\n它支持“某个 memory pipeline 是否在写入/整理过程中保持来源权威边界”的判断。它不能单独证明完整权限系统安全，因为身份认证、真实 ACL、跨租户隔离、provenance spoofing 与物理删除不在同一个受控对象里。\n\n## 公平比较契约\n\n固定 consolidator 输入、LLM backbone、authority-label policy、memory write/read policy 与 downstream action harness；尤其不能把人工提供 authority metadata 的系统与需要自行恢复 authority 的系统直接归因为同一组件能力。\n\n## 还没有测什么\n\n真实多主体身份系统、恶意 provenance 伪造、长期多次 consolidation 后的 authority drift，以及生产 memory store 中的治理代价。\n\n## 下一步最有判别力的验证\n\n做 `same claim × same downstream task × different source authority × repeated consolidation depth` 的 factorial control，并在正确 authority metadata 直接给定条件下建立 oracle ceiling，区分 authority extraction、persistence 与 action policy 三层失败。\n\n<!-- RESEARCH-DECISION:START -->\n## 研究决策卡\n### 什么时候值得用\n如果你的 claim 是 memory consolidation、summary、experience extraction 或 self-evolving memory 不应把来源约束洗掉，AuthMem-Bench 是比一般 recall benchmark 更直接的安全坐标。\n### 一个具体任务长什么样\n示意任务：相同一句陈述分别来自有权设定规则的用户与低权限外部来源；经过 consolidation 后，后续 action request 看起来完全相同。正确系统必须只在授权来源条件下把记忆当成可执行约束。\n### 最有判别力的实验\n固定 claim 与 action，只改变 authority 和 consolidation depth；同时给出 oracle authority metadata，测收益究竟来自正确识别来源还是下游 policy。\n### 建议搭配\n[GateMem](gatemem.md) · [InjecMEM](injecmem.md) · [Utility Under Attack](utility-under-attack.md)\n> **读分数的原则：** authority preservation 是 memory lifecycle 的一层，不等价于完整部署权限安全。\n<!-- RESEARCH-DECISION:END -->\n\n## 演化位置\n`recall → shared-memory governance → provenance / authority-preserving consolidation`\n""",
"en": """# AuthMem-Bench: Memory must preserve authority, not only content\n\n[中文](authmem-bench.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)\n\n[Paper](https://arxiv.org/abs/2608.01679)\n\n## What it measures\n\nAuthMem-Bench tests whether persistent-memory consolidation preserves **source authority**. Its paired design holds the focal claim and downstream task fixed while changing only source authority, exposing whether consolidation launders low-authority content into reusable facts or instructions.\n\n## What changed relative to prior evaluation\n\nBenchmarks such as GateMem made access control in shared memory measurable. AuthMem-Bench moves the failure boundary earlier, into consolidation itself: summaries, extraction, or normalization can preserve a proposition while deleting the conditions under which it was authorized for reuse.\n\n## Decisive evidence\n\nThe paper reports authority collapse in 48 of 49 configurations spanning seven consolidators and seven LLM backbones. In a controlled action-grounded evaluation, collapsed memories without authority metadata produce a mean unauthorized-action rate of 50.3%. In the end-to-end setting, automatically predicted and persisted authority labels reduce the observed unauthorized-action rate from 16.9% to 0.0% while benign task success remains essentially unchanged.\n\n## What the score supports\n\nThe benchmark supports claims about preservation of authority boundaries through a memory pipeline. It does not establish complete authorization-system security: identity, production ACLs, cross-tenant isolation, provenance spoofing, and physical erasure are separate layers.\n\n## Fair comparison contract\n\nMatch consolidator input, backbone, authority-label policy, memory write/read policy, and downstream action harness. A system supplied with human authority metadata is not the same causal treatment as one that must infer it.\n\n## What remains unmeasured\n\nReal multi-principal identity systems, adversarial provenance spoofing, authority drift across repeated consolidation, and governance cost in long-lived production memory stores.\n\n## Next discriminating validation\n\nRun a `same claim × same downstream task × source authority × consolidation depth` factorial experiment and add supplied-correct-authority metadata as an oracle condition to separate extraction, persistence, and action-policy failures.\n\n<!-- RESEARCH-DECISION:START -->\n## Research decision card\n### When to use it\nUse AuthMem-Bench when the claim concerns consolidation, summarization, experience extraction, or self-evolving memory preserving source constraints; it is more direct than a recall benchmark for that question.\n### What a concrete task looks like\nIllustrative task: the same statement comes from an authorized user or a low-authority external source. After consolidation, an identical later action request should be governed by the memory only in the authorized condition.\n### Most discriminating experiment\nHold claim and action fixed, vary authority and consolidation depth, and add oracle authority metadata to separate source recognition from downstream policy.\n### Pair with\n[GateMem](gatemem.en.md) · [InjecMEM](injecmem.en.md) · [Utility Under Attack](utility-under-attack.en.md)\n> **Score-reading rule:** authority preservation is one memory-lifecycle layer, not proof of complete deployment authorization security.\n<!-- RESEARCH-DECISION:END -->\n\n## Evolution position\n`recall → shared-memory governance → provenance / authority-preserving consolidation`\n"""},
"pm-bench": {
"zh": """# PM-Bench：Agent Memory 不只是记住过去，也要记得未来要做什么\n\n**中文** | [English](pm-bench.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)\n\n[论文](https://arxiv.org/abs/2607.12385)\n\n## 它到底测什么\n\nPM-Bench 测 **prospective memory**：智能体在继续执行其他活动时，能否保留用户的延迟意图，并在正确未来时间、cue 或环境状态出现时执行，而不是等用户再次提醒。任务受到认知科学 Virtual Week 范式启发，运行在模拟七天的文本环境中。\n\n## 相比此前评测多测了什么\n\nLoCoMo、LongMemEval 等长期记忆基准主要问“过去发生了什么 / 当前状态是什么”；PM-Bench 把时间方向翻转成“未来条件满足时要记得做什么”，从 retrospective recall 推到 intention maintenance + cue monitoring + timely execution。\n\n## 决定性证据\n\n论文比较 8 个 LLM、8 种 agent configuration；最好的 GPT-5.4 agent 也只有 65.1% F1，而且没有一种改善 prospective memory 的策略跨模型稳定占优。\n\n## 这个分数能证明什么\n\n它支持受控模拟环境中的 delayed-intention maintenance 与 cue-triggered execution。它不证明现实日历、异步通知、工具失败或高风险动作下的长期可靠性。\n\n## 公平比较契约\n\n固定 backbone、agent configuration、时间表示、cue 可见性、ongoing-task policy 与评分规则；如果一方拥有显式 scheduler/notification tool 而另一方只能靠上下文记忆，必须分轨道报告。\n\n## 还没有测什么\n\n真实数天/月时长、外部工具与通知系统、多个相互冲突或撤销的未来意图，以及执行错误的安全代价。\n\n## 下一步最有判别力的验证\n\n将同一 intention 分别设置为 time-based、event-based、更新、取消与冲突条件；配对比较纯上下文、外部持久记忆、显式 scheduler，并按首次正确触发、漏触发与误触发分开评分。\n\n<!-- RESEARCH-DECISION:START -->\n## 研究决策卡\n### 什么时候值得用\n当你的 memory claim 是“未来需要的时候会主动做对事”，而不是“现在问它能不能复述旧事实”时，PM-Bench 是直接坐标。\n### 一个具体任务长什么样\n示意任务：用户周一提出“周四出现某个环境 cue 时完成 X”，智能体随后持续处理无关活动；到 cue 真正出现时必须首次正确触发，同时不应提前执行。\n### 最有判别力的实验\n对相同 intention 配对 time cue、event cue、更新、取消与冲突，并比较 context-only、persistent memory 与 scheduler。\n### 建议搭配\n[LongMemEval](longmemeval.md) · [MemoryArena](memoryarena.md) · [Mem2ActBench](mem2actbench.md)\n> **读分数的原则：** prospective-memory F1 不等于现实自动化的端到端安全可靠性。\n<!-- RESEARCH-DECISION:END -->\n\n## 演化位置\n`past-event recall → current-state tracking → future-intention execution`\n""",
"en": """# PM-Bench: Agent memory must remember what to do later, not only what happened before\n\n[中文](pm-bench.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)\n\n[Paper](https://arxiv.org/abs/2607.12385)\n\n## What it measures\n\nPM-Bench measures **prospective memory**: maintaining a delayed user intention while continuing other activities, then executing it when the correct future time, cue, or environment state occurs without another reminder. It uses a text-based simulated seven-day Virtual Week inspired by cognitive-science paradigms.\n\n## What changed relative to prior evaluation\n\nBenchmarks such as LoCoMo and LongMemEval primarily ask what happened in the past or what state is current. PM-Bench reverses the temporal direction: maintain an intention, monitor for its trigger, and act at the right future moment.\n\n## Decisive evidence\n\nThe paper evaluates eight LLMs under eight agent configurations. The best reported GPT-5.4 agent reaches only 65.1% F1, and no prospective-memory strategy dominates consistently across models.\n\n## What the score supports\n\nIt supports claims about delayed-intention maintenance and cue-triggered execution in the controlled simulation. It does not establish long-horizon reliability with real calendars, asynchronous notifications, tool failures, or safety-critical actions.\n\n## Fair comparison contract\n\nMatch backbone, agent configuration, time representation, cue visibility, ongoing-task policy, and scoring. Explicit scheduler/notification tools should be reported as a separate condition from context-only memory.\n\n## What remains unmeasured\n\nReal days-to-months horizons, external notification systems, conflicts and cancellations among future intentions, and the safety cost of erroneous execution.\n\n## Next discriminating validation\n\nPair time-based, event-based, updated, cancelled, and conflicting variants of the same intention. Compare context-only, persistent memory, and explicit scheduling while separating correct first trigger, misses, and false triggers.\n\n<!-- RESEARCH-DECISION:START -->\n## Research decision card\n### When to use it\nUse PM-Bench when the memory claim is that an agent will do the right thing later when needed, rather than merely restate an old fact on demand.\n### What a concrete task looks like\nIllustrative task: on Monday a user asks for X when a particular cue appears on Thursday. The agent handles unrelated activity until then, must trigger on the first correct cue, and must not act early.\n### Most discriminating experiment\nPair time cues, event cues, updates, cancellations, and conflicts for the same intention, comparing context-only, persistent-memory, and scheduler conditions.\n### Pair with\n[LongMemEval](longmemeval.en.md) · [MemoryArena](memoryarena.en.md) · [Mem2ActBench](mem2actbench.en.md)\n> **Score-reading rule:** prospective-memory F1 is not end-to-end safety reliability for real automation.\n<!-- RESEARCH-DECISION:END -->\n\n## Evolution position\n`past-event recall → current-state tracking → future-intention execution`\n"""},
"agent-retrieval-bench": {
"zh": """# Agent Retrieval Bench：coding agent 在写 patch 之前，先得找到真正该读的代码\n\n**中文** | [English](agent-retrieval-bench.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)\n\n[论文](https://arxiv.org/abs/2607.24882) · [代码与数据](https://github.com/eyuansu62/agent-retrieval-bench)\n\n## 它到底测什么\n\nAgent Retrieval Bench（ARB）隔离 coding agent 的 **context-acquisition layer**：给定真实 workflow signal 与冻结 base commit，检索器要找到智能体下一步真正需要阅读的文件，或者在仓库不存在有用本地上下文时正确弃答。相关性由 workflow need 定义，不等于 query 与文件文字相似。\n\n## 相比此前评测多测了什么\n\n传统 code retrieval 常以 query-file 相似性或已知修改文件定义 gold；ARB 使用 code2test、comment2context、trace2code、edit2ripple 四类真实工作流关系，并加入 natural no-gold 与 wrong-repository counterfactual，直接测 selective retrieval。\n\n## 决定性证据\n\n当前发布包含 427 个样本、25 个仓库；正例 345 个，另有 50 个 natural no-gold 与 32 个 counterfactual control。论文报告没有一种 retrieval family 在所有任务和指标上占优；logged agent trajectories 在 27–35% 样本上一个 gold file 都没找到。\n\n## 这个分数能证明什么\n\n它支持 file-level upstream context acquisition 的判断，不支持“更高 Recall 一定带来更高 patch success”。官方范围也明确：file hit 不等于 function/span localization，当前 seed intervention 测的是 context-selection behavior，不是完整 repair success。\n\n## 公平比较契约\n\n固定 repository/base commit、candidate filter、token packing、top-k/context budget、selective threshold 与 metric version。不同 release bundle 的 corpus inventory 和 evaluated snapshots 也要明确，不能混用 legacy packing 指标与 canonical BCY。\n\n## 还没有测什么\n\n函数/行级定位、编辑生成、测试通过率、跨多轮工具探索，以及检索成本对完整修复时延的影响。\n\n## 下一步最有判别力的验证\n\n在同一 repair agent 下做 `random seed context / retrieved context / oracle gold context` 干预，并固定后续探索预算；最终用测试通过率和新增探索量同时检验 file retrieval 是否真正改善修复。\n\n<!-- RESEARCH-DECISION:START -->\n## 研究决策卡\n### 什么时候值得用\n如果你的 claim 是 context engine、repo retrieval 或 agent search 帮 coding agent 找到下一步所需上下文，ARB 比直接跑 patch benchmark 更容易做因果归因。\n### 一个具体任务长什么样\n示意任务：失败 trace 暴露的是测试文件，但真正需要阅读的是另一个模块里的 root-cause implementation；检索器必须跨表面词汇定位下一步工作所需文件。\n### 最有判别力的实验\n固定 repair agent 和 post-seed exploration budget，只替换初始上下文为 random、retrieved 与 oracle gold，再看 file F1 与最终 tests。\n### 建议搭配\n[BEIR](beir.md) · [The Recall Trap](recall-trap.md) · [BrowseComp-Plus_CM](browsecomp-plus-cm.md)\n> **读分数的原则：** file-level retrieval 是上游坐标，不应直接包装为 end-to-end coding-agent success。\n<!-- RESEARCH-DECISION:END -->\n\n## 演化位置\n`semantic code retrieval → workflow-conditioned context acquisition → selective retrieval / downstream intervention`\n""",
"en": """# Agent Retrieval Bench: Coding agents must find the right context before writing the patch\n\n[中文](agent-retrieval-bench.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)\n\n[Paper](https://arxiv.org/abs/2607.24882) · [Code and data](https://github.com/eyuansu62/agent-retrieval-bench)\n\n## What it measures\n\nAgent Retrieval Bench (ARB) isolates the **context-acquisition layer** of coding agents. Given a real workflow signal and a frozen base commit, a retriever must find files the agent needs to read next or abstain when the repository contains no useful local context. Relevance is defined by workflow need rather than query–file textual similarity.\n\n## What changed relative to prior evaluation\n\nConventional code retrieval often defines gold context through semantic similarity or known edited files. ARB covers code2test, comment2context, trace2code, and edit2ripple workflow relations and adds natural no-gold and wrong-repository counterfactual controls for selective retrieval.\n\n## Decisive evidence\n\nThe current release contains 427 samples across 25 repositories: 345 positive examples, 50 natural no-gold examples, and 32 counterfactual controls. The paper reports no single retrieval family dominating across tasks and metrics; logged agent trajectories miss every gold file on 27–35% of samples.\n\n## What the score supports\n\nIt supports file-level upstream context-acquisition claims, not the claim that higher recall necessarily improves patch success. The official scope explicitly notes that file hits do not establish function/span localization and the current seed intervention studies context selection rather than full repair success.\n\n## Fair comparison contract\n\nPin repository/base commits, candidate filtering, token packing, top-k/context budget, selective threshold, and metric version. Disclose release bundles and corpus inventory; legacy packing fields are not canonical BCY.\n\n## What remains unmeasured\n\nFunction/line localization, edit generation, test-passing repair, multi-round tool exploration, and the impact of retrieval cost on complete repair latency.\n\n## Next discriminating validation\n\nUnder one repair agent, intervene on initial context with random non-gold, retrieved, and oracle-gold seeds while fixing post-seed exploration budget. Measure both file/context quality and final test-passing repair.\n\n<!-- RESEARCH-DECISION:START -->\n## Research decision card\n### When to use it\nUse ARB when the claim concerns a context engine, repository retriever, or agent search policy finding the next useful coding context. It enables cleaner attribution than jumping directly to patch benchmarks.\n### What a concrete task looks like\nIllustrative task: a failure trace exposes a test file while the needed next read is a root-cause implementation in another module. Retrieval must bridge the workflow relation rather than match surface vocabulary.\n### Most discriminating experiment\nFix the repair agent and post-seed exploration budget; replace only initial context with random, retrieved, and oracle-gold seeds, then measure context quality and final tests.\n### Pair with\n[BEIR](beir.en.md) · [The Recall Trap](recall-trap.en.md) · [BrowseComp-Plus_CM](browsecomp-plus-cm.en.md)\n> **Score-reading rule:** file-level retrieval is an upstream coordinate, not end-to-end coding-agent success.\n<!-- RESEARCH-DECISION:END -->\n\n## Evolution position\n`semantic code retrieval → workflow-conditioned context acquisition → selective retrieval / downstream intervention`\n"""}
}

AREA_LABEL = {"agent-memory": ("Agent Memory", "Agent Memory"), "rag": ("RAG", "RAG / Agentic Retrieval"), "data-agent": ("Data Agent", "Data Agents")}
ROLE = {"zh": {"precursor":"🌱 前身","foundation":"🧱 基石","transition":"↗ 过渡","frontier":"🔭 前沿"}, "en": {"precursor":"🌱 Precursor","foundation":"🧱 Foundation","transition":"↗ Transition","frontier":"🔭 Frontier"}}


def primary(r):
    for k in ("paper","project","code","data"):
        if r.get("artifacts",{}).get(k): return r["artifacts"][k]
    raise ValueError(r["id"])

def citation_cell(r):
    c=r.get("citations") or {}
    if c.get("status")=="ok" and c.get("url") and c.get("count") is not None:
        return f"[{c['count']}]({c['url']})"
    return "—"

def replace_block(text, label, lines):
    a=f"<!-- {label}:START -->"; b=f"<!-- {label}:END -->"
    s=text.index(a)+len(a); e=text.index(b,s)
    return text[:s]+"\n\n\n"+"\n".join(lines)+"\n"+text[e:]

def existing_rows(text,label):
    a=f"<!-- {label}:START -->"; b=f"<!-- {label}:END -->"
    body=text[text.index(a)+len(a):text.index(b,text.index(a)+len(a))]
    out={}
    for line in body.splitlines():
        m=re.search(r"<!-- benchmark-id:([^ ]+) -->",line)
        if m: out[m.group(1)]=line
    return out

def render_recent(r, lang):
    if lang=="zh":
        area=AREA_LABEL[r["area"]][0]; summary=ZH.get(r["id"],{}).get("summary",r["summary"])
        return f"| {r['released']} | {area} | [{r['name']}]({primary(r)}) <!-- benchmark-id:{r['id']} --> | {summary} |"
    area={"agent-memory":"Agent Memory","rag":"RAG / Agentic Retrieval","data-agent":"Data Agent"}[r["area"]]
    return f"| {r['released']} | {area} | [{r['name']}]({primary(r)}) <!-- benchmark-id:{r['id']} --> | {r['summary']} |"

def render_area(r, lang):
    summary=ZH.get(r["id"],{}).get("summary",r["summary"]) if lang=="zh" else r["summary"]
    return f"| {ROLE[lang][r['evolution_role']]} | [{r['name']}]({primary(r)}) <!-- benchmark-id:{r['id']} --> | {citation_cell(r)} | {r['released']} | {summary} |"

def render_library_timeline(r, lang):
    if lang=="zh":
        area={"agent-memory":"Agent Memory","rag":"RAG / Agentic Retrieval","data-agent":"Data Agents"}[r["area"]]
        delta=ZH.get(r["id"],{}).get("delta",r["measurement_strength"])
    else:
        area={"agent-memory":"Agent Memory","rag":"RAG / Agentic Retrieval","data-agent":"Data Agents"}[r["area"]]
        delta=EN_DELTA.get(r["id"],r["measurement_strength"])
    return f"| {r['released']} | [{r['name']}]({primary(r)}) <!-- benchmark-id:{r['id']} --> | {area} | {ROLE[lang][r['evolution_role']]} | {delta} |"

def render_library_map(r, lang):
    if lang=="zh":
        area={"agent-memory":"Agent Memory","rag":"RAG / Agentic Retrieval","data-agent":"Data Agents"}[r["area"]]
        desc=ZH.get(r["id"],{}).get("summary",r["summary"])
    else:
        area={"agent-memory":"Agent Memory","rag":"RAG / Agentic Retrieval","data-agent":"Data Agents"}[r["area"]]
        desc=r["summary"]
    # map tables validate release at column index 2: Benchmark | Role | Time | Description
    return f"| [{r['name']}]({primary(r)}) <!-- benchmark-id:{r['id']} --> | {ROLE[lang][r['evolution_role']]} | {r['released']} | {desc} |"

records=json.loads(REG.read_text())
byid={r["id"]:r for r in records}
for r in NEW:
    byid[r["id"]]=r
records=list(byid.values())
REG.write_text(json.dumps(records,ensure_ascii=False,indent=2)+"\n")

# Deep reads are explicit reviewed source pages, not runtime filler.
for bid, langs in DETAILS.items():
    (ROOT/"benchmarks"/f"{bid}.md").write_text(langs["zh"])
    (ROOT/"benchmarks"/f"{bid}.en.md").write_text(langs["en"])

# README complete surfaces.
for filename,lang in (("README.md","zh"),("README.en.md","en")):
    p=ROOT/filename; text=p.read_text()
    if lang=="zh":
        text=text.replace('<p><strong>中文</strong> · <a href="README.en.md">English</a></p>', '<p><strong>中文</strong> · <a href="README.en.md">English</a> · <a href="https://h20zhang.github.io/Agent-Benchmark-Radar/zh/">Website</a></p>',1)
        text=text.replace('<p><strong>网站待完善；当前内容以本 README 为准。</strong></p>\n','')
        text=text.replace('以下是 registry 中的全部 126 个基准。','以下是 registry 中的全部 129 个基准。')
    else:
        text=text.replace('<p><a href="README.md">中文</a> · <strong>English</strong></p>', '<p><a href="README.md">中文</a> · <strong>English</strong> · <a href="https://h20zhang.github.io/Agent-Benchmark-Radar/en/">Website</a></p>',1)
        text=text.replace('<p><strong>Website under improvement; this README is the source of truth for now.</strong></p>\n','')
        text=text.replace('all 126 benchmarks','all 129 benchmarks')
    recent_rows=existing_rows(text,"TABLE-FIRST:RECENT")
    for r in NEW: recent_rows[r["id"]]=render_recent(r,lang)
    recent_ids=[r["id"] for r in sorted(records,key=lambda x:(x["released"],x["name"].casefold()),reverse=True) if r["released"] >= "2026-02"]
    header="| 时间 | 方向 | Benchmark | 考察内容 |\n|---|---|---|---|" if lang=="zh" else "| Time | Area | Benchmark | What it measures |\n|---|---|---|---|"
    text=replace_block(text,"TABLE-FIRST:RECENT",[header]+[recent_rows[i] for i in recent_ids])
    for area in ("agent-memory","rag","data-agent"):
        label=f"TABLE-FIRST:AREA:{area}"
        rows=existing_rows(text,label)
        for r in NEW:
            if r["area"]==area: rows[r["id"]]=render_area(r,lang)
        ids=[r["id"] for r in sorted((x for x in records if x["area"]==area),key=lambda x:(x["released"],x["name"].casefold(),x["id"]))]
        header="| 阶段 | Benchmark | 引用数 (S2) | 时间 | 考察内容 |\n|---|---|---:|---:|---|" if lang=="zh" else "| Stage | Benchmark | Citations (S2) | Time | What it measures |\n|---|---|---:|---:|---|"
        text=replace_block(text,label,[header]+[rows[i] for i in ids])
    p.write_text(text)

# Complete alternate Library surfaces.
for filename,lang in (("library/README.md","zh"),("library/README.en.md","en")):
    p=ROOT/filename; text=p.read_text()
    tl=existing_rows(text,"COMPLETE-TIMELINE")
    for r in NEW: tl[r["id"]]=render_library_timeline(r,lang)
    ids=[r["id"] for r in sorted(sorted(records,key=lambda x:(x["name"].casefold(),x["id"])),key=lambda x:x["released"],reverse=True)]
    header="| 时间 | Benchmark | 领域 | 角色 | 这次改变了什么 |\n|---:|---|---|---|---|" if lang=="zh" else "| Time | Benchmark | Area | Role | What changed |\n|---:|---|---|---|---|"
    text=replace_block(text,"COMPLETE-TIMELINE",[header]+[tl[i] for i in ids])
    for area in ("agent-memory","rag","data-agent"):
        label=f"COMPLETE-MAP:{area}"; rows=existing_rows(text,label)
        for r in NEW:
            if r["area"]==area: rows[r["id"]]=render_library_map(r,lang)
        aids=[r["id"] for r in sorted((x for x in records if x["area"]==area),key=lambda x:(x["released"],x["name"].casefold(),x["id"]))]
        header="| Benchmark | 角色 | 时间 | 这次改变了什么 |\n|---|---|---:|---|" if lang=="zh" else "| Benchmark | Role | Time | What changed |\n|---|---|---:|---|"
        text=replace_block(text,label,[header]+[rows[i] for i in aids])
    p.write_text(text)

# Record the freshness pass as a compact weekly synthesis, without pretending method papers are benchmarks.
report_zh=ROOT/"reports/weekly/2026-W36.md"; report_en=ROOT/"reports/weekly/2026-W36.en.md"
report_zh.write_text("""# 2026-W36｜Freshness backfill：不是凑 9 月数量，而是补三个漏掉的评测坐标\n\n本周重新扫描 Agent Memory、Agentic Retrieval 与 Data Agents 的近期 primary sources。9 月 1–5 日检索到的方法论文与跨域 agent benchmark 中，没有在证据核验后强行扩张三条 canonical area；更实质的 content debt 是 7–8 月三项可复用 benchmark 漏收。\n\n- **AuthMem-Bench（2026-08-03）**：把 memory consolidation 中的 source authority preservation 变成配对可测对象。\n- **Agent Retrieval Bench（2026-07-27）**：把 coding-agent context acquisition 与 patch generation 拆开，并加入 no-gold / counterfactual selective retrieval。\n- **PM-Bench（2026-07-14）**：把 prospective memory——未来 cue 到来时记得执行延迟意图——从 retrospective recall 中独立出来。\n\n## So what\n\nMemory 前沿继续从“存了什么”转向“什么时候、以什么权限、为了什么未来行动使用”；Retrieval 则继续从 query-document similarity 转向 workflow-conditioned context utility。相比再增加一批相似 QA，这两类变化更可能改变实验设计。\n""")
report_en.write_text("""# 2026-W36 | Freshness backfill: three missing evaluation coordinates matter more than forcing September volume\n\nThis week's primary-source scan revisited recent Agent Memory, Agentic Retrieval, and Data Agent work. Rather than stretching the three canonical areas to absorb method papers or cross-domain agent benchmarks from September 1–5, the more consequential content debt was three reusable benchmarks missed in July–August.\n\n- **AuthMem-Bench (2026-08-03):** makes preservation of source authority through memory consolidation a paired measurable object.\n- **Agent Retrieval Bench (2026-07-27):** isolates coding-agent context acquisition from patch generation and adds no-gold / counterfactual selective retrieval.\n- **PM-Bench (2026-07-14):** isolates prospective memory—executing a delayed intention when a future cue arrives—from retrospective recall.\n\n## So what\n\nThe memory frontier is moving from what is stored toward when, under whose authority, and for which future action memory is used. Retrieval is moving from query–document similarity toward workflow-conditioned context utility. Those shifts change experimental design more than another similar QA set would.\n""")

print(f"registry: {len(records)} benchmarks; backfilled {[r['id'] for r in NEW]}")
