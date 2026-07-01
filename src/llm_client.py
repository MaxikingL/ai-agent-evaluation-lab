def get_agent_answer(test_case: dict, documentation: str) -> str:
    """
    Temporary mock LLM client.

    In the next step, this function will be replaced with a real LLM call.
    For now, it returns predefined answers so we can test the evaluation pipeline.
    """

    test_id = test_case["id"]

    mock_answers = {
        "TC001": (
            "No. The forecast endpoint requires latitude and longitude. "
            "Latitude and longitude must be provided as WGS84 geographical coordinates."
        ),
        "TC002": (
            "The default forecast length is 7 days. "
            "Seven days equals 168 hourly values."
        ),
        "TC003": (
            "No. You cannot request a 30-day forecast using forecast_days. "
            "The maximum forecast length is 16 days. "
            "The forecast_days parameter can be used to extend the forecast length."
        ),
        "TC004": (
            "No. The free API can be used for evaluation and prototyping. "
            "Commercial use requires a paid subscription. "
            "Paid commercial use uses a dedicated customer endpoint with an API key."
        ),
    }

    return mock_answers.get(
        test_id,
        "I do not have enough information to answer this question."
    )