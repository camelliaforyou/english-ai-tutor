# ADR-0002: Push-to-talk first

Status: Accepted

## Context

Full-duplex audio requires interruption handling, streaming and more complicated latency controls.

## Decision

Build record -> stop -> process -> play first, with HTTP requests. Evaluate WebSocket and VAD later.

## Consequences

Simpler debugging and testability, less natural conversation in MVP.
