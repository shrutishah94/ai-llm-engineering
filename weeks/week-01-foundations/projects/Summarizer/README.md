# Summarizer

Week 1 summarization and extraction project with a simple modular layout.

## Structure

- `app/orchestration` agent flow and pipeline logic
- `app/models` model gateway and LLM clients
- `app/tools` callable utilities (summarization, extraction, scraping, etc.)
- `configs` project settings and configuration files
- `data` local files used by examples
- `examples` runnable demos
- `tests` test suite
- `notebooks` experiments

## Run examples

From repo root:

```bash
uv run python weeks/week-01-foundations/projects/Summarizer/examples/textSummary.py
uv run python weeks/week-01-foundations/projects/Summarizer/examples/resumeSummary.py
uv run python weeks/week-01-foundations/projects/Summarizer/examples/webSummary.py
```

## Run quality checks

```bash
uv run pytest weeks/week-01-foundations/projects/Summarizer/tests -q
uv run ruff check weeks/week-01-foundations/projects/Summarizer
```
