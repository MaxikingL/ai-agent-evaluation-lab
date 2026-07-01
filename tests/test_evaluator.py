from src.evaluator import evaluate_answer


def test_evaluate_answer_passes_when_all_expected_facts_are_present():
    test_case = {
        "id": "TC_TEST_001",
        "title": "Required facts present",
        "question": "How long is the default forecast?",
        "expected_facts": [
            "The default forecast length is 7 days.",
            "Seven days equals 168 hourly values.",
        ],
        "risk": "incorrect_forecast_length",
    }

    answer = (
        "The default forecast length is 7 days. "
        "Seven days equals 168 hourly values."
    )

    result = evaluate_answer(test_case, answer)

    assert result["test_id"] == "TC_TEST_001"
    assert result["score"] == 5.0
    assert result["passed"] is True
    assert result["grounded"] is True
    assert result["missing_facts"] == []


def test_evaluate_answer_fails_when_expected_facts_are_missing():
    test_case = {
        "id": "TC_TEST_002",
        "title": "Missing expected facts",
        "question": "How long is the default forecast?",
        "expected_facts": [
            "The default forecast length is 7 days.",
            "Seven days equals 168 hourly values.",
        ],
        "risk": "incorrect_forecast_length",
    }

    answer = "The default forecast length is 10 days."

    result = evaluate_answer(test_case, answer)

    assert result["test_id"] == "TC_TEST_002"
    assert result["score"] == 0.0
    assert result["passed"] is False
    assert result["grounded"] is False
    assert result["missing_facts"] == [
        "The default forecast length is 7 days.",
        "Seven days equals 168 hourly values.",
    ]


def test_evaluate_answer_gives_partial_score_when_some_facts_are_present():
    test_case = {
        "id": "TC_TEST_003",
        "title": "Partial answer",
        "question": "What is included in the Premium Plan?",
        "expected_facts": [
            "Priority support",
            "Advanced analytics",
            "API access",
        ],
        "risk": "plan_features",
    }

    answer = "The Premium Plan includes Priority support and API access."

    result = evaluate_answer(test_case, answer)

    assert result["test_id"] == "TC_TEST_003"
    assert result["score"] == 3.33
    assert result["passed"] is False
    assert result["grounded"] is False
    assert result["missing_facts"] == [
        "Advanced analytics",
    ]





