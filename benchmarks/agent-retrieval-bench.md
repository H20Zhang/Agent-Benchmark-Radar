# Agent Retrieval Bench：coding agent 在写 patch 之前，先得找到真正该读的代码

**中文** | [English](agent-retrieval-bench.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2607.24882) · [代码与数据](https://github.com/eyuansu62/agent-retrieval-bench)

## 它到底测什么

Agent Retrieval Bench（ARB）隔离 coding agent 的 **context-acquisition layer**：给定真实 workflow signal 与冻结 base commit，检索器要找到智能体下一步真正需要阅读的文件，或者在仓库不存在有用本地上下文时正确弃答。相关性由 workflow need 定义，不等于 query 与文件文字相似。

## 相比此前评测多测了什么

传统 code retrieval 常以 query-file 相似性或已知修改文件定义 gold；ARB 使用 code2test、comment2context、trace2code、edit2ripple 四类真实工作流关系，并加入 natural no-gold 与 wrong-repository counterfactual，直接测 selective retrieval。

## 决定性证据

当前发布包含 427 个样本、25 个仓库；正例 345 个，另有 50 个 natural no-gold 与 32 个 counterfactual control。论文报告没有一种 retrieval family 在所有任务和指标上占优；logged agent trajectories 在 27–35% 样本上一个 gold file 都没找到。

## 这个分数能证明什么

它支持 file-level upstream context acquisition 的判断，不支持“更高 Recall 一定带来更高 patch success”。官方范围也明确：file hit 不等于 function/span localization，当前 seed intervention 测的是 context-selection behavior，不是完整 repair success。

## 公平比较契约

固定 repository/base commit、candidate filter、token packing、top-k/context budget、selective threshold 与 metric version。不同 release bundle 的 corpus inventory 和 evaluated snapshots 也要明确，不能混用 legacy packing 指标与 canonical BCY。

## 还没有测什么

函数/行级定位、编辑生成、测试通过率、跨多轮工具探索，以及检索成本对完整修复时延的影响。

## 下一步最有判别力的验证

在同一 repair agent 下做 `random seed context / retrieved context / oracle gold context` 干预，并固定后续探索预算；最终用测试通过率和新增探索量同时检验 file retrieval 是否真正改善修复。

<!-- RESEARCH-DECISION:START -->
## 研究决策卡
### 什么时候值得用
如果你的 claim 是 context engine、repo retrieval 或 agent search 帮 coding agent 找到下一步所需上下文，ARB 比直接跑 patch benchmark 更容易做因果归因。
### 一个具体任务长什么样
示意任务：失败 trace 暴露的是测试文件，但真正需要阅读的是另一个模块里的 root-cause implementation；检索器必须跨表面词汇定位下一步工作所需文件。
### 最有判别力的实验
固定 repair agent 和 post-seed exploration budget，只替换初始上下文为 random、retrieved 与 oracle gold，再看 file F1 与最终 tests。
### 建议搭配
[BEIR](beir.md) · [The Recall Trap](recall-trap.md) · [BrowseComp-Plus_CM](browsecomp-plus-cm.md)
> **读分数的原则：** file-level retrieval 是上游坐标，不应直接包装为 end-to-end coding-agent success。
<!-- RESEARCH-DECISION:END -->

## 演化位置
`semantic code retrieval → workflow-conditioned context acquisition → selective retrieval / downstream intervention`
