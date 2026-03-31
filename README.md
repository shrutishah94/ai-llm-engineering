# ai-llm-engineering

Playground for learning and showcasing AI skills.

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
uv run python src/main.py
```

## Alternative setup (pip)

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install numpy pandas
python src/main.py
```
