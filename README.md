# Resume Builder

A lightweight command-line project that generates a polished Markdown resume from structured JSON input.

## Features
- Fill in basic profile details, skills, experience, and education.
- Generate a clean, readable `resume.md` file.
- Validate required fields and show helpful error messages.
- Keep your source data in version control as `resume.json`.

## Project structure
- `src/resume_builder.py` – main generator logic.
- `examples/resume.sample.json` – starter input data.
- `tests/test_resume_builder.py` – basic unit tests.
- `output/` – generated resumes.

## Quick start
1. Generate a resume from the sample data:
   ```bash
   python src/resume_builder.py examples/resume.sample.json output/resume.md
   ```
2. Open `output/resume.md`.

## Run tests
```bash
python -m unittest discover -s tests
```

## Input format
The input JSON must contain:
- `name`
- `title`
- `email`
- `location`
- `summary`
- `skills` (array)
- `experience` (array of roles)
- `education` (array of education items)

See `examples/resume.sample.json` for a complete example.
