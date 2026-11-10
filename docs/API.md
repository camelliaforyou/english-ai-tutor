# API Specification

## Overview

English AI Tutor provides a local REST API powered by FastAPI.

- Base URL: `http://localhost:8000`
- Framework: FastAPI
- API Version: 0.1.0
- LLM Provider: Ollama
- Default Model: `qwen3.5:9b`
- Response Format: JSON

## 1. Health Check

### GET /health

Checks whether the FastAPI application is running.

Response: `200 OK`

```json
{
  "status": "ok"
}
```

Note: This endpoint does not verify Ollama availability.

## 2. Text Conversation

### POST /chat

Generates an English conversation response using the local LLM.

### Request

Content-Type: `application/json`

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

### Request Schema

| Field              | Type      | Required | Description           |
| ------------------ | --------- | -------- | --------------------- |
| messages           | Message[] | Yes      | Conversation history  |
| messages[].role    | string    | Yes      | `user` or `assistant` |
| messages[].content | string    | Yes      | Message text          |

Constraints:

- Minimum 1 message
- Maximum 30 messages
- Content length: 1–4000 characters
- System messages are managed by the server

### Response

Status: `200 OK`

```json
{
  "reply": "Hi! I'd love to help. How was your day?",
  "model": "qwen3.5:9b"
}
```

### Response Schema

| Field | Type   | Description                  |
| ----- | ------ | ---------------------------- |
| reply | string | Generated assistant response |
| model | string | Ollama model identifier      |

## 3. Conversation History

The API is stateless.

Clients must send the relevant conversation history
with every request.

Example:

```json
{
  "messages": [
    {
      "role": "user",
      "content": "I went swimming yesterday."
    },
    {
      "role": "assistant",
      "content": "That sounds fun! How was it?"
    },
    {
      "role": "user",
      "content": "It was difficult but enjoyable."
    }
  ]
}
```

The server adds the tutor system prompt automatically.

Conversation history is not persisted in this milestone.

## 4. Error Responses

### 422 — Validation Error

Returned when request data violates the Pydantic schema.

### 503 — LLM Unavailable

Returned when an Ollama HTTP or connection error occurs.

```json
{
  "detail": "LLM service is unavailable"
}
```

Note: Unexpected response formats from Ollama may currently
produce HTTP 500. Additional upstream response validation
will be implemented in a future milestone.

## 5. LLM Configuration

Environment variables:

```dotenv
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=qwen3.5:9b
OLLAMA_TIMEOUT=120
```

Default generation options:

| Option      | Value |
| ----------- | ----- |
| stream      | false |
| think       | false |
| keep_alive  | -1    |
| temperature | 0.7   |
| num_predict | 120   |

## 6. Interactive Documentation

FastAPI automatically exposes:

- Swagger UI: `http://localhost:8000/docs`
- OpenAPI JSON: `http://localhost:8000/openapi.json`

## 7. Planned Endpoints

The following endpoints are not implemented yet.

| Endpoint                 | Purpose            | Milestone |
| ------------------------ | ------------------ | --------- |
| POST /voice/transcribe   | Speech-to-Text     | M3        |
| POST /voice/synthesize   | Text-to-Speech     | M4        |
| POST /voice/conversation | Voice conversation | M5        |

Do not implement planned endpoints until their milestone begins.
