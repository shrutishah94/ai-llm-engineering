# Week 01 - Foundations

## Goal
Build strong Python + LLM basics and establish reusable project conventions.

## Projects
- `projects/Summarizer`

## Outcomes
- One-project-per-week structure to reduce context switching and folder duplication.
- Established production-like layout: `app`, `configs`, `data`, `examples`, `tests`, `README`.

## Architecture Notes
- Decisions: keep model interactions in `app/models` and domain utilities in `app/tools`.
- Trade-offs: prioritized clear structure and fast iteration over deeper abstractions.
- What I would improve next: add typed schemas, stronger error handling, and richer tests.
