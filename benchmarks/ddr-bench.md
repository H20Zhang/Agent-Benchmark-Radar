# DDR-Bench：开放数据研究里，最重要的能力可能是自己决定“什么值得分析”

**中文** | [English](ddr-bench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

## 它在测什么

DDR-Bench 覆盖 291 个 entities：MIMIC 100、GLOBEM 91、10-K 100，底层超过 203M records、40 tables、6,372 fields，并用 2,058 个 checklist items 评价 agent 在 minimal prompt 下自主 goal setting、exploration 与 insight generation。

## 相比什么前进了

多数 benchmark 明确告诉 agent 要回答哪个 query。DDR-Bench 把 research objective 留得更开放，检查 agent 是否能在大型数据库中选择有价值的分析方向，而不是只执行已有 specification。

## 分数边界

checklist/insight score 支持在三类 dataset 与 benchmark-defined research criteria 下的 autonomous exploration；它仍不能等同真实科研/业务价值，因为 checklist 构造决定“什么算值得发现”。

## 公平比较条件

锁定 dataset snapshot、minimal prompt、tool access、exploration budget、checklist/judge 与 entity split，并报告 domain slices。

## 下一步评测坐标

下一步需要更强的 novelty/decision-value evaluation，以及 agent 对“没有足够证据形成 insight”的校准与停止能力。
