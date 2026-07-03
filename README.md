# AI Agent Evaluation Lab

![Python tests](https://github.com/MaxikingL/ai-agent-evaluation-lab/actions/workflows/tests.yml/badge.svg)

## Overview

AI Agent Evaluation Lab is a Python-based evaluation framework for testing the quality of AI agent answers against source documentation.

The project simulates a realistic business scenario:

1. A company has technical documentation.
2. A user asks a question.
3. An AI agent answers using the documentation.
4. An evaluator checks whether the answer is correct, complete, grounded and free from hallucinations.
5. A Markdown report is generated with pass/fail status, scores, missing facts and evaluator comments.

This project focuses on practical AI QA, LLM evaluation and agentic testing patterns.

---

## Problem

LLM-powered agents can generate fluent and confident answers, but those answers are not always correct.

Common risks include:

- missing important facts,
- hallucinated information,
- incorrect limits or parameters,
- unsupported commercial or legal claims,
- regressions after changing the prompt, model or documentation,
- answers that sound correct but are incomplete.

In production AI systems, it is not enough to check whether an agent produces an answer. We need a repeatable way to evaluate whether the answer is reliable.

---

## Solution

This project provides a lightweight evaluation pipeline:

```text
source documentation
        ↓
test cases
        ↓
AI agent answer
        ↓
rule-based or semantic evaluator
        ↓
Markdown evaluation report