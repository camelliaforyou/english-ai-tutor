# Task 0002 — Text Conversation MVP

- Status: In Progress
- Milestone: M1
- Priority: High
- Created: 2026-11-10

## 1. Objective

Implement a text-based English conversation API using FastAPI and
Ollama (qwen3.5:9b).

This milestone establishes the LLM integration layer before
introducing speech recognition (STT) and text-to-speech (TTS).

## 2. Scope

### In Scope

- FastAPI `/chat` endpoint
- Ollama integration using HTTP
- Conversation history support
- Pydantic request/response validation
- Environment-based LLM configuration
- English tutor system prompt
- Basic error handling
- API tests
- API documentation

### Out of Scope

- Speech-to-Text (STT)
- Text-to-Speech (TTS)
- Streaming responses
- WebSocket communication
- Authentication
- Database persistence
- Cloud LLM providers
- Pronunciation scoring
- Frontend chat interface

## 3. Architecture

```text
Client
  |
  | POST /chat
  v
FastAPI Router
  |
  v
LLMService
  |
  | HTTP POST /api/chat
  v
Ollama (qwen3.5:9b)
  |
  v
LLMService
  |
  v
FastAPI Response
```

## 4. Implementation Requirements

### API Layer

- Define `/chat` using FastAPI APIRouter.
- Validate requests using Pydantic.
- Return structured JSON responses.
- Map Ollama connection errors to HTTP 503.
- Do not expose internal error details.

### Service Layer

- Keep Ollama HTTP communication in `services/llm.py`.
- Do not place LLM business logic inside API routers.
- Use `httpx.AsyncClient`.
- Keep model name and base URL configurable.
- Disable thinking mode for short conversational responses.
- Keep the model loaded using `keep_alive: -1`.

### Conversation

- Accept a list of messages.
- Support `user` and `assistant` roles.
- Inject the system prompt on the server.
- Keep responses short and conversational.
- Ask one relevant follow-up question.
- Provide Korean explanations when explicitly requested.

### Configuration

- Use `pydantic-settings`.
- Store local settings in `.env`.
- Commit `.env.example`, never `.env`.

## 5. API Contract

Endpoint:

`POST /chat`

Request:

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Hello! I want to practice English."
    }
  ]
}
```

Response:

```json
{
  "reply": "Hi! How was your day?",
  "model": "qwen3.5:9b"
}
```

## 6. Acceptance Criteria

- [ ] FastAPI starts successfully.
- [ ] `GET /health` returns HTTP 200.
- [ ] `POST /chat` returns an English response.
- [ ] Multiple messages preserve conversational context.
- [ ] Empty messages return HTTP 422.
- [ ] Ollama connection failures return HTTP 503.
- [ ] API tests pass.
- [ ] Ruff checks pass.
- [ ] `docs/API.md` is updated.

## 7. Verification

Run from `apps/api`:

```bash
uv run pytest
uv run ruff check .
uv run ruff format --check .
```

Manual API test:

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {
        "role": "user",
        "content": "Hello!"
      }
    ]
  }'
```

## 8. Definition of Done

This task is complete when:

1. All acceptance criteria are satisfied.
2. Automated tests pass.
3. API documentation matches implementation.
4. No unrelated functionality is introduced.
5. Task status is changed to `Done`.

## 9. Future Work

- M2: Frontend text conversation UI
- M3: Local Whisper STT integration
- M4: Local Kokoro TTS integration
- M5: Voice conversation orchestration
- M6: Streaming and latency optimization

---

- Status : Done
- Milestone : M1
- Priority : High
- Created : 2026-11-10
- Completed : 2026-11-10
