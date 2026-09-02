# BrowseComp: persistent search for hard-to-find web evidence

[中文](browsecomp.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[OpenAI release](https://openai.com/index/browsecomp/) · [Paper](https://arxiv.org/abs/2504.12516) · [Eval code](https://github.com/openai/simple-evals)

## What it actually measures

BrowseComp contains 1,266 hard fact-seeking questions whose answers require persistent, creative web browsing across multiple sources. Answers are deliberately short and verifiable, keeping grading simple while making **evidence discovery** difficult.

## What changed relative to prior evaluation

Simple factual QA and shallow web search saturate once a browsing model can issue a few searches. BrowseComp shifts difficulty into search persistence, query reformulation, source chaining, and finding obscure evidence rather than long-form answer generation.

## Decisive evidence

The benchmark was constructed around single, stable, indisputable short answers, often requiring tens or potentially hundreds of pages to locate. Its continued usefulness comes from separating hard search from subjective report judging: failure is usually inability to find the answer rather than disagreement over prose quality.

## What the score supports

A score supports end-to-end browsing-agent ability under a particular search provider, browsing interface, time, and model. It does not cleanly measure retrieval algorithm quality because web navigation, query generation, model priors, and tool implementation are inseparable.

## Fair comparison contract

Record model/version, search provider, tool interface, date, call/token budget, and whether page fetching is available. Web drift makes historical scores only approximately comparable. Equal answer grading does not imply equal information access.

## What remains unmeasured

OpenAI explicitly notes the short-answer distribution may correlate poorly with open-ended user research. BrowseComp does not evaluate citation quality, synthesis, ambiguity clarification, artifact generation, or user-facing completeness.

## Next discriminating validation

Pair BrowseComp questions with evidence-set scoring and controlled search budgets. This would distinguish “found the answer by luck/priors” from efficient discovery of sufficient supporting evidence.

## Genealogy

`factual QA → persistent web search → evidence-aware research agents`

BrowseComp is a clean benchmark of search hardness, not a complete benchmark of research usefulness.