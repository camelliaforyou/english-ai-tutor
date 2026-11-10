# Architecture decisions log

- ADR-0001: Local-first MVP; no paid cloud APIs. See `adr/0001-local-first.md`.
- ADR-0002: Push-to-talk before real-time streaming. See `adr/0002-push-to-talk.md`.

For new decisions: add `docs/adr/NNNN-short-name.md` with context, decision, consequences and alternatives. Link it here.

# Architecture Decisions

This document summarizes important technical decisions.

Detailed decisions may be recorded separately under `docs/adr/`.

## ADR-002: Use Ollama with Qwen3.5 9B

- Date: 2026-11-10
- Status: Accepted
- Milestone: M1

### Context

The project requires a local LLM capable of natural English
conversation without paid cloud APIs.

The development machine is an Apple Silicon MacBook M3 Pro
with 36 GB unified memory.

### Decision

Use Ollama with `qwen3.5:9b` as the default conversation model.

### Rationale

Local benchmark results with the model kept in memory:

- Average response latency: approximately 1.82 seconds
- Average generation speed: approximately 18 tokens/second
- Model loading overhead after warm-up: negligible

These measurements were obtained from three short,
non-streaming text responses.

They are not end-to-end voice latency measurements.

### Consequences

- No paid LLM API is required.
- The application can operate locally.
- Model quality and latency depend on local hardware.
- The service layer must allow future model replacement.
- Keep-alive increases memory residency.

### Constraints

- Do not hardcode model names in API routers.
- Read the model name from configuration.
- Do not introduce cloud LLM providers without approval.

## ADR-003: Separate API and LLM Service Layers

- Date: 2026-11-10
- Status: Accepted
- Milestone: M1

### Decision

Use separate FastAPI routers, Pydantic schemas,
configuration, and LLM service modules.

### Rationale

This separation supports:

- Testability
- Model replacement
- Clear responsibilities
- Future STT/TTS integration
- Easier maintenance

### Constraints

- Routers handle HTTP concerns.
- Services handle external model communication.
- Schemas define request and response contracts.
- Configuration manages environment-dependent settings.

## ADR-004: Stateless Conversation API

- Date: 2026-11-10
- Status: Accepted
- Milestone: M1

### Decision

Clients send conversation history with each `/chat` request.

The backend does not persist conversation history.

### Rationale

- Reduces initial implementation complexity.
- Avoids premature database introduction.
- Supports rapid MVP development.

### Consequences

- Clients are responsible for conversation history.
- Request payloads grow with conversation length.
- Long conversations will eventually require
  history truncation or summarization.

### Future Considerations

Session persistence and conversation summarization
may be introduced in later milestones.

Do not add a database during M1.
