# MemEvoBench：memory safety failure 会随着 repeated writeback 累积

**中文** | [English](memevobench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2604.15774) · [代码](https://github.com/xiewwee11/MemEvoBench)

## 它在测什么

MemEvoBench 含 108 个 QA risk cases（7 domains、36 risk types）与 83 个 workflow cases，模拟 misleading memories、noisy tool outputs 与 biased feedback 被多轮写回 memory 后造成的 behavioral drift，并评价 attack success 与 correction quality。

## 相比什么前进了

普通 safety benchmark 每次只看独立 prompt；普通 memory benchmark 又假设写入信息可信。MemEvoBench 让 unsafe evidence 通过 repeated writeback 积累，因此可以观察小错误如何在 memory lifecycle 中放大。

## 分数边界

attack/correction metrics 支持给定 memory-pool scaffold、base safety policy 与 simulated feedback 下的 drift resistance。它不证明真实工具后果或 shared-memory authorization，也不能把 package 的安全差异归因给单一 write filter。

## 公平比较条件

锁定 memory scaffold、base model safety policy、judge、attack schedule 与 simulated tool feedback。单轮与多轮结果必须分开。

## 下一步评测坐标

下一步需要逐条追踪 poisoned write 到真实 external consequence，并验证 selective repair 而非粗暴清空 memory。
