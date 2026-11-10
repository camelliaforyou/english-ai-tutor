# API agent instructions

Read `../../AGENTS.md` and `README.md` first.

- Use type hints and Pydantic schemas for API boundaries.
- Separate `routers/`, `services/`, and model adapters when functionality is added; avoid speculative abstraction.
- Never load STT/TTS model weights inside a request handler.
- Keep audio files temporary and delete in `finally`; never log raw audio or full transcripts by default.
- Preserve conversation history per session only when explicitly implemented; don't claim persistent memory.
- Use explicit request timeouts, error handling and upload limits.
- Keep model IDs and endpoint URLs configurable via environment with safe local defaults.
- Tests should mock model providers; tests must not require downloading model weights.
- Run `uv run pytest` when tests exist; otherwise report that tests are not yet configured.
- Run `uv run ruff check` and `uv run ruff format --check` when Python files change.
