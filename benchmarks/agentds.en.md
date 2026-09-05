# AgentDS: data-agent evaluation should compare human-only, AI-only, and human-AI collaboration

[中文](agentds.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2603.19005) · **Area: Data Agent**

AgentDS is useful not because it adds another agent leaderboard, but because it places **AI-only, human-only, and human-AI collaboration** inside the same evaluation question: how much work can AI replace, where does human judgment remain load-bearing, and when does collaboration outperform AI alone?

## What it actually measures

AgentDS uses **17 data-science challenges across six industries with 29 teams / 80 participants**, synthetic enterprise-pattern data, and hidden leaderboard evaluation of complete analysis or modeling outcomes.

The object is therefore broader than isolated SQL, code generation, or statistics questions. More importantly, the **mode of work** is itself part of the comparison: the same class of challenge may be attempted by AI alone or by a human working with AI.

## Compared with what

Benchmarks such as MLE-bench, DSAgentBench, and DataSpace mainly ask whether an agent can complete an end-to-end task. AgentDS asks an additional adoption-oriented question:

- Is AI-only already useful?
- Does human-AI collaboration reliably beat AI-only?
- Does AI improve outcome quality or mainly reduce execution effort?
- Which bottlenecks still require problem framing, result judgment, or domain expertise rather than code execution?

That makes AgentDS more informative for **augmentation / substitution** claims than for pure model ranking.

## How the evaluation works

An interpretable AgentDS result must align the challenge release, data version, hidden evaluator, AI tools and models, time budget, participant selection, and collaboration rules.

AI-only, human-only, and human-AI should be treated as separate tracks. In the human-AI condition, whether the AI can act autonomously, whether humans must approve each step, and whether participants can freely choose tools can all materially change the result.

The protocol therefore matters almost as much as the headline score.

## What a score supports

A challenge score supports a claim about task outcome quality under the current participant pool, data, tools, time budget, and hidden tests.

It does **not** directly support a claim such as “AI replaces data scientists.” Substitution also depends on human time, review burden, error severity, problem selection, communication, and long-term maintenance cost.

Likewise, human-AI beating AI-only does not automatically prove that human expertise caused the gain. Extra time, more retries, stronger prompting, or humans handling evaluator-sensitive final steps may explain part of the difference.

## Main confounders

**Human variance is the major additional source of uncertainty relative to pure-agent benchmarks.** Participants differ in data-science experience, tool familiarity, and collaboration strategy.

A second limitation is synthetic enterprise-pattern data. It enables controlled and verifiable tasks, but real enterprise analytics also contains dirty schemas, permissions, inherited metric definitions, organizational knowledge, and business-value judgments that are hard to encode in an evaluator.

Cross-paper comparisons therefore need much more than model name and final score.

## Fair comparison contract

At minimum, align:

- challenge and hidden-test version;
- participant selection and experience distribution;
- AI model, tool access, and agent harness;
- time and retry budgets for every track;
- the human-AI collaboration contract;
- evaluator and any feedback visible during the run.

When these differ, report separate protocol cells rather than one merged leaderboard.

## What is still missing

AgentDS brings the question “do humans still matter?” into benchmark design, but it does not yet fully measure:

- whether productivity gains persist with long-term use;
- whether review and correction effort cancels automation savings;
- low-frequency but high-severity errors;
- whether better benchmark outcomes improve real business decisions;
- how persistent AI use changes human verification behavior and skill.

## Most discriminating next test

The highest-value extension is not simply more static challenges, but a **longitudinal controlled deployment**. Run human-only, AI-only, and human-AI modes over the same teams and task distribution while jointly tracking output quality, human minutes, rework, severe errors, and downstream decision impact.

That would separate “agents score better on benchmarks” from “agents actually reduce data-team workload.”

## Evolution position

`isolated data task → end-to-end data-science agent → human–AI team effectiveness`

AgentDS occupies the last step: it moves the research question from “can the agent do the task?” to “**what incremental value appears when the agent enters a real work organization?**”
