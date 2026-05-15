import argparse
import json
from pathlib import Path
from typing import Any

REQUIRED_FIELDS = [
    "name",
    "title",
    "email",
    "location",
    "summary",
    "skills",
    "experience",
    "education",
]


def bullet_list(items: list[str]) -> str:
    if not items:
        return "- N/A"
    return "\n".join(f"- {item}" for item in items)


def render_experience(experience: list[dict[str, Any]]) -> str:
    if not experience:
        return "_No experience entries provided._"

    blocks = []
    for role in experience:
        header = (
            f"### {role.get('role', 'Role')} — {role.get('company', 'Company')} "
            f"({role.get('start', 'Start')} to {role.get('end', 'End')})"
        )
        bullets = bullet_list(role.get("highlights", []))
        blocks.append(f"{header}\n{bullets}")
    return "\n\n".join(blocks)


def render_education(education: list[dict[str, Any]]) -> str:
    if not education:
        return "- N/A"

    rows = []
    for entry in education:
        rows.append(
            f"- **{entry.get('degree', 'Degree')}**, "
            f"{entry.get('school', 'School')} ({entry.get('year', 'Year')})"
        )
    return "\n".join(rows)


def validate_input(data: dict[str, Any]) -> None:
    missing = [field for field in REQUIRED_FIELDS if field not in data]
    if missing:
        missing_fields = ", ".join(missing)
        raise ValueError(f"Missing required fields: {missing_fields}")

    if not isinstance(data["skills"], list):
        raise ValueError("'skills' must be an array")
    if not isinstance(data["experience"], list):
        raise ValueError("'experience' must be an array")
    if not isinstance(data["education"], list):
        raise ValueError("'education' must be an array")


def build_resume(data: dict[str, Any]) -> str:
    validate_input(data)

    return f"""# {data['name']}

**{data['title']}**  
{data['location']} | {data['email']}

## Summary
{data['summary']}

## Skills
{bullet_list(data.get('skills', []))}

## Experience
{render_experience(data.get('experience', []))}

## Education
{render_education(data.get('education', []))}
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a Markdown resume from JSON input."
    )
    parser.add_argument("input", help="Path to input JSON resume data")
    parser.add_argument("output", help="Path to output Markdown file")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        print(f"Error: input file not found: {input_path}")
        return 1

    try:
        data = json.loads(input_path.read_text(encoding="utf-8"))
        resume = build_resume(data)
    except json.JSONDecodeError as exc:
        print(f"Error: invalid JSON in {input_path}: {exc}")
        return 1
    except ValueError as exc:
        print(f"Error: {exc}")
        return 1

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(resume, encoding="utf-8")

    print(f"Resume generated at {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
