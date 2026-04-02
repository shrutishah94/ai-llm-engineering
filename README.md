# ai-llm-engineering

Web Intelligence Pipeline: scrape website content, then summarize and extract structured entities with an LLM.
More Projects to be added. 

## Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

## Setup (uv)

```bash
uv sync
```

This creates/updates `.venv` and installs dependencies from `pyproject.toml` and `uv.lock`.

## Run

```bash
uv run python examples/demo.py
```

If your machine/proxy causes SSL certificate issues during scraping, pass `verify_ssl=False` when calling `analyze_website(...)` for local testing.

## Project structure

- `app/scraper.py` website scraping and cleaning utilities
- `app/llm_client.py` shared OpenAI client + `generate_response()`
- `app/summarizer.py` text and resume summarization utility
- `app/extractor.py` JSON entity extraction utility
- `app/pipeline.py` glue layer for website analyzer (`analyze_website`)
- `app/classifier.py` category classifier utility
- `app/rewriter.py` tone rewriter utility
- `examples/textSummary.py` text-only utility demo
- `examples/webSummary.py` URL -> scrape -> summarize -> extract
- `examples/resumeSummary.py` URL -> summarize -> extract


## Alternative setup (pip)

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install numpy pandas
python src/main.py
```
