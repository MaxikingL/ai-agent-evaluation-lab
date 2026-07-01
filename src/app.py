from pathlib import Path

import yaml

from src.llm_client import get_agent_answer
from src.evaluator import evaluate_answer
from src.report_generator import generate_markdown_report


PROJECT_ROOT = Path(__file__).resolve().parents[1]

DOCUMENTATION_PATH = PROJECT_ROOT / "data" / "company_faq.md"
TEST_CASES_PATH = PROJECT_ROOT / "data" / "test_cases.yaml"
REPORT_PATH = PROJECT_ROOT / "reports" / "evaluation_report.md"


def load_documentation() -> str:
    return DOCUMENTATION_PATH.read_text(encoding="utf-8")


def load_test_cases() -> list[dict]:
    with TEST_CASES_PATH.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def main() -> None:
    documentation = load_documentation()
    test_cases = load_test_cases()

    results = []

    for test_case in test_cases:
        answer = get_agent_answer(test_case, documentation)
        evaluation = evaluate_answer(test_case, answer)
        results.append(evaluation)

    generate_markdown_report(results, str(REPORT_PATH))

    print(f"Evaluation finished. Report saved to: {REPORT_PATH}")


if __name__ == "__main__":
    main()