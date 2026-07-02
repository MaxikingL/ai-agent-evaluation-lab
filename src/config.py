import os
from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()


@dataclass(frozen=True)
class Settings:
    llm_provider: str
    evaluator_provider: str
    openai_api_key: str | None
    openai_model: str
    openai_evaluator_model: str


def get_settings() -> Settings:
    return Settings(
        llm_provider=os.getenv("LLM_PROVIDER", "mock").lower(),
        evaluator_provider=os.getenv("EVALUATOR_PROVIDER", "rule").lower(),
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        openai_model=os.getenv("OPENAI_MODEL", "gpt-5.5"),
        openai_evaluator_model=os.getenv("OPENAI_EVALUATOR_MODEL", "gpt-5.5"),
    )