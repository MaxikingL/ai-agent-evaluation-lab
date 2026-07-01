from pathlib import Path


def generate_markdown_report(results: list[dict], output_path: str) -> None:
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    total = len(results)
    passed = sum(1 for result in results if result["passed"])
    failed = total - passed

    average_score = 0
    if total > 0:
        average_score = round(
            sum(result["score"] for result in results) / total,
            2
        )

    lines = []

    lines.append("# AI Agent Evaluation Report")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"Total test cases: {total}")
    lines.append(f"Passed: {passed}")
    lines.append(f"Failed: {failed}")
    lines.append(f"Average score: {average_score}/5")
    lines.append("")

    lines.append("## Results")
    lines.append("")

    for result in results:
        status = "PASSED" if result["passed"] else "FAILED"

        lines.append(f"### {result['test_id']} — {result['title']}")
        lines.append("")
        lines.append(f"Status: **{status}**")
        lines.append(f"Score: **{result['score']}/5**")
        lines.append(f"Risk: `{result['risk']}`")
        lines.append("")
        lines.append("**Question:**")
        lines.append("")
        lines.append(result["question"])
        lines.append("")
        lines.append("**Agent answer:**")
        lines.append("")
        lines.append(result["answer"])
        lines.append("")
        lines.append("**Missing facts:**")
        lines.append("")

        if result["missing_facts"]:
            for fact in result["missing_facts"]:
                lines.append(f"- {fact}")
        else:
            lines.append("- None")

        lines.append("")
        lines.append("---")
        lines.append("")

    output_file.write_text("\n".join(lines), encoding="utf-8")