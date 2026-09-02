# MedMemoryBench：个性化医疗中的 streaming memory accumulation

**中文** | [English](medmemorybench.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2605.11814) · [代码](https://github.com/AQ-MedAI/MedMemoryBench)

## 它到底测什么

MedMemoryBench 评估 **streaming clinical accumulation**：患者历史持续增长，关键医疗状态必须保持精确，而且信息越来越多时，retrieval/reasoning 可能主动变差。它把 memory saturation 变成显式可测的 failure mode。

## 相比此前评测多测了什么

开放域 conversation memory 往往只把历史变长当 scale problem；医疗场景的错误成本和 state 结构不同：旧信息可能持续相关、被新诊断覆盖，或与新症状发生复杂交互。MedMemoryBench 用 evaluate-while-constructing protocol，在 memory 逐步构建过程中持续测量。

## 决定性证据

数据约有 2,000 个 session、16,000 个 interaction turn，基于 clinically grounded synthetic patient archetype 并经过专家验证；公开框架包含 14 类 memory-method baseline。实验暴露了 complex medical reasoning、noise resilience 与 history 增长后的 memory saturation 等明显瓶颈。

## 这个分数能证明什么

它能支持 synthetic but clinically structured history 下的 memory robustness 判断，但绝不等价于临床有效性或可直接用于 patient care 的安全证明；downstream medical model 与 synthetic trajectory assumption 都是重要 confounder。

## 公平比较契约

应固定 patient trajectory、clinical backbone、streaming checkpoint、retrieval budget 与 evaluator，并报告 performance 随 accumulated memory size 的曲线，而不是只有一个最终平均分。stale/superseded state 和 irrelevant noise 也应拆开，因为对应不同机制。

## 还没有测什么

真实 EHR 有 missing record、coding artifact、provider disagreement、法规约束和 distribution shift；prospective clinical outcome 与真实 harm 也不是 synthetic benchmark 能回答的。

## 下一步最有判别力的验证

分别对 write compression、retrieval、reasoning 画 stage-level saturation curve，并在每个 checkpoint 加 oracle retrieval，定位长临床 memory 主要是“写丢了、找不到、还是找到了不会用”。

## 演化位置

`long conversation memory → streaming clinical state → saturation-aware high-stakes memory`

它把“memory 越长越容易退化”从工程现象提升成生产级评测问题。