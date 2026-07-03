from openai import OpenAI

from src.config import get_settings


def get_agent_answer(test_case: dict, documentation: str) -> str:
    settings = get_settings()

    if settings.llm_provider == "mock":
        return get_mock_answer(test_case)

    if settings.llm_provider == "openai":
        return get_openai_answer(test_case, documentation)

    raise ValueError(f"Unsupported LLM_PROVIDER: {settings.llm_provider}")


def get_mock_answer(test_case: dict) -> str:
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
        "TC005": (
            "The documentation does not contain information about earthquake forecasts."
        ),
    }

    return mock_answers.get(
        test_id,
        "I do not have enough information to answer this question."
    )


def get_openai_answer(test_case: dict, documentation: str) -> str:
    settings = get_settings()

    if not settings.openai_api_key:
        raise ValueError(
            "OPENAI_API_KEY is missing. Add it to your .env file or use LLM_PROVIDER=mock."
        )

    client = OpenAI(api_key=settings.openai_api_key)

    prompt = build_prompt(test_case, documentation)

    response = client.responses.create(
        model=settings.openai_model,
        input=prompt,
    )

    return response.output_text


def build_prompt(test_case: dict, documentation: str) -> str:
    return f"""
You are a technical support AI assistant.

Answer the user's question using only the documentation below.

Rules:
- Use only facts from the documentation.
- If the documentation does not contain the answer, say: "I do not have enough information in the documentation."
- Do not invent parameters, limits, pricing, or usage rules.
- Keep the answer concise and factual.

Documentation:
\"\"\"
{documentation}
\"\"\"

User question:
{test_case["question"]}
""".strip()