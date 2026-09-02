# InMind: retrieving personal facts whose relevance requires a world-knowledge bridge

[中文](inmind.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2607.24368) · [Code](https://github.com/imlrz/InMind)

## What it measures

InMind contains 125 expert-verified tasks across 10 life domains. Each has direct and indirect queries; the indirect query requires world knowledge to understand why a personal fact is relevant before retrieval can succeed, so embedding similarity alone is insufficient.

## Compared with what

Typical memory retrieval assumes semantic proximity between query and stored fact. InMind uses paired controls to separate storage failure, missing backbone knowledge, retrieval-routing failure, and final application failure, isolating implicit-association retrieval.

## Score boundary

The direct/indirect gap supports whether a system can retrieve target memory after a world-knowledge bridge. It does not measure updating, forgetting, or action. Base-model knowledge is itself load-bearing, so cross-backbone score changes cannot be attributed solely to the memory retriever.

## Fair comparison conditions

Align base model, embedding/retrieval budget, synthetic personal facts, background trace, and judge, and report direct and indirect conditions separately.

## Next evaluation coordinate

A stronger test introduces competing dynamic memories and checks whether implicit associations improve later actions rather than only one QA response.
