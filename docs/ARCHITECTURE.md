# Architecture (target MVP)

```text
Browser (Next.js 16)
  | recorded audio / JSON over localhost HTTP
  v
FastAPI (session/orchestration)
  +--> local STT adapter (Whisper family)
  +--> Ollama http://127.0.0.1:11434 (qwen3.5:9b)
  +--> local TTS adapter (Kokoro)
  |
  v
JSON transcript + response + audio -> Browser
```

## Design principles

- Local-first: no third-party inference calls.
- Adapter boundaries: STT, LLM and TTS replaceable independently.
- Sequential push-to-talk pipeline for MVP. WebSocket/VAD later only if justified by measured latency.
- Model warm-up and keep-alive for latency; never assume all models fit memory concurrently.
- Store no recordings by default. Persistence requires explicit design decision.

## Latency measurement

Track model load, STT, LLM first-token/total, TTS and end-to-end separately. The observed Ollama warm 9B response (~1.82 s average for a short prompt) is an informal baseline, not an end-to-end SLA.

## API contracts

Document exact schemas in `docs/API.md` before wiring web and API. Do not invent implemented routes.

---

## Milestone 1: Text Conversation Architecture

### Runtime Flow

```text
HTTP Client
    |
    | POST /chat
    v
FastAPI
    |
    v
Chat Router
    |
    v
Pydantic Validation
    |
    v
LLMService
    |
    v
Ollama HTTP API
    |
    v
Qwen3.5 9B
    |
    v
JSON Response
```

### Backend Structure

```text
apps/api/
├── main.py
├── app/
│   ├── api/
│   │   └── routes/
│   │       ├── health.py
│   │       └── chat.py
│   ├── core/
│   │   └── config.py
│   ├── schemas/
│   │   └── chat.py
│   └── services/
│       └── llm.py
└── tests/
```

### Dependency Rules

1. API routers may depend on schemas and services.
2. Services may depend on schemas and configuration.
3. Services must not import API routers.
4. Schemas must not depend on service implementations.
5. Ollama HTTP calls must remain inside the LLM service.
6. Frontend code must not communicate directly with Ollama.

### Future Voice Architecture

```text
Next.js
   |
   v
FastAPI
   |
   +-- STT Service (Whisper)
   |
   +-- LLM Service (Ollama)
   |
   +-- TTS Service (Kokoro)
   |
   v
Audio Response
```

STT, LLM, and TTS must remain independently replaceable.

### Current Limitations

- No streaming
- No persistent conversation sessions
- No audio input or output
- No pronunciation assessment
- No authentication
- No database

These limitations are intentional for M1.
