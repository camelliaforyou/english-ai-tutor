# ADR-0001: Local-first inference

Status: Accepted

## Context

The project is for learning and low-cost local English conversation on an M3 Pro MacBook with 36GB RAM.

## Decision

Use Ollama `qwen3.5:9b` for conversation and local Whisper-family STT plus Kokoro TTS. No paid APIs for MVP.

## Consequences

No per-request API fees and more privacy; local performance, model installation, RAM and license verification remain responsibilities.
