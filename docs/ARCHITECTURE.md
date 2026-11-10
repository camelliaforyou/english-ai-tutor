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
