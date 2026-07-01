def evaluate_answer(test_case: dict, answer: str) -> dict:
    """
    Simple rule-based evaluator.

    It checks whether all expected facts are present in the answer.
    This is not a perfect evaluator yet, but it gives us a working baseline.
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
        score = 0
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
    }