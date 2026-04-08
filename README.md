# ai-llm-engineering

8-week AI/LLM learning portfolio with production-style project structure, quality checks, and architecture notes.

## Setup

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) recommended

```bash
uv sync --group dev
```

## Portfolio Index

| Week | Theme | Project(s) | Outcome |
|---|---|---|---|
| 01 | Foundations | `Summarizer` | Baseline NLP/LLM workflow + modular architecture |

## Quality Signals

- Linting with `ruff`
- Tests with `pytest`
- CI on push/pull request via GitHub Actions

## Add New Project (No Refactor Needed)

1. Pick the week folder: `weeks/week-0X-topic/projects/`
2. Create a new project folder: `my-project-name`
3. Copy structure from `weeks/_templates/project-template/README.md`
4. Add project-level folders: `app` or `src`, `tests`, `configs`, `README.md`
5. Update that week's `README.md` with outcomes + architecture notes
