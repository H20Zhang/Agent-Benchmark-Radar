# SearchAuditBench：只看 final answer 无法知道 deep-search agent 为什么失败

**中文** | [English](searchauditbench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2608.05212) · [代码](https://github.com/lzzzx666/SearchAuditor)

## 它在测什么

SearchAuditBench 收集 1,243 条 failed trajectories，来自 8 个 open-weight models 与 5 个 deep-search benchmarks，平均 73.1 messages、65.1K tokens。expert annotations 标出 critical step、六类 root cause 与可执行 repair，并评价 strict/loose localization、cause accuracy、diagnosis 与 repair pass rate。

## 相比什么前进了

大多数 benchmark 把失败压成 0 分。SearchAuditBench 把 post-hoc auditor 设为 evaluation object：能否找到最早关键错误、解释原因并给出足以让 trajectory 恢复的 repair。

## 分数边界

高 diagnosis/repair score 支持 auditor 在 failures-only mixture 上定位和修复错误；它不说明原始 search agent 更强，也不覆盖 proactive prevention。source-model、harness 与 benchmark mixture 会塑造 failure distribution。

## 公平比较条件

锁定 trajectory corpus、failure sampling、cause taxonomy、repair execution/judge 与 tolerance span。不能把不同 failure mixtures 的 auditor scores 直接排名。

## 下一步评测坐标

下一步应将 auditor 在线接入 agent，测提前干预是否真正减少最终失败，而不是只在事后解释。
