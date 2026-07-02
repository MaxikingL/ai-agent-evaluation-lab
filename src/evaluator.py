import json

from openai import OpenAI

from src.config import get_settings


def evaluate_answer(test_case: dict, answer: str) -> dict:
    settings = get_settings()

    if settings.evaluator_provider == "rule":
        return evaluate_answer_rule_based(test_case, answer)

    if settings.evaluator_provider == "openai":
        return evaluate_answer_with_openai(test_case, answer)

    raise ValueError(f"Unsupported EVALUATOR_PROVIDER: {settings.evaluator_provider}")


def evaluate_answer_rule_based(test_case: dict, answer: str) -> dict:
    """
    Simple rule-based evaluator.

    It checks whether all expected facts are present as exact text fragments.
    This is useful as a baseline, but it can fail when the answer is correct
    but phrased differently.
    """

    expected_facts = test_case.get("expected_facts", [])
    answer_lower = answer.lower()

    missing_facts = []

    for fact in expected_facts:
        if fact.lower() not in answer_lower:
            missing_facts.append(fact)

    total_facts = len(expected_facts)
    found_facts = total_facts - len(missing_facts)

    if total_facts == 0:
        score = 0.0
    else:
        score = round((found_facts / total_facts) * 5, 2)

    passed = score >= 4 and len(missing_facts) == 0

    return {
        "test_id": test_case["id"],
        "title": test_case.get("title", ""),
        "question": test_case["question"],
        "risk": test_case.get("risk", ""),
        "answer": answer,
        "score": score,
        "passed": passed,
        "grounded": len(missing_facts) == 0,
        "hallucination_detected": False,
        "missing_facts": missing_facts,
        "evaluation_method": "rule_based_exact_match",
    }


def evaluate_answer_with_openai(test_case: dict, answer: str) -> dict:
    settings = get_settings()

    if not settings.openai_api_key:
        raise ValueError(
            "OPENAI_API_KEY is missing. Add it to your .env file or use EVALUATOR_PROVIDER=rule."
        )

    client = OpenAI(api_key=settings.openai_api_key)

    prompt = build_evaluation_prompt(test_case, answer)

    response = client.responses.create(
        model=settings.openai_evaluator_model,
        input=prompt,
    )

    raw_output = response.output_text.strip()

    try:
        evaluation = json.loads(raw_output)
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"Evaluator returned invalid JSON:\n{raw_output}"
        ) from exc

    missing_facts = evaluation.get("missing_facts", [])
    hallucination_detected = bool(evaluation.get("hallucination_detected", False))
    score = float(evaluation.get("score", 0.0))

    passed = score >= 4.0 and not hallucination_detected

    return {
        "test_id": test_case["id"],
        "title": test_case.get("title", ""),
        "question": test_case["question"],
        "risk": test_case.get("risk", ""),
        "answer": answer,
        "score": score,
        "passed": passed,
        "grounded": len(missing_facts) == 0 and not hallucination_detected,
        "hallucination_detected": hallucination_detected,
        "missing_facts": missing_facts,
        "comment": evaluation.get("comment", ""),
        "evaluation_method": "openai_semantic_judge",
    }


def build_evaluation_prompt(test_case: dict, answer: str) -> str:
    expected_facts = test_case.get("expected_facts", [])

    return f"""
You are an AI QA evaluator.

Your task is to evaluate whether the agent answer correctly addresses the user question using the expected facts.

Important:
- Evaluate semantic meaning, not exact wording.
- Do not require identical phrasing.
- Mark a fact as missing only if the meaning is absent.
- Detect hallucinations if the answer includes unsupported or contradictory information.
- Return only valid JSON. Do not include markdown.

Test case ID:
{test_case["id"]}

Question:
{test_case["question"]}

Expected facts:
{json.dumps(expected_facts, indent=2)}

Agent answer:
{answer}

Return JSON with this exact structure:
{{
  "score": 0,
  "missing_facts": [],
  "hallucination_detected": false,
  "comment": "short explanation"
}}

Scoring:
5 = all expected facts are present and no hallucination
4 = mostly correct, minor omission
3 = partially correct
2 = major omissions or unclear answer
1 = mostly incorrect
0 = incorrect or unrelated
""".strip()