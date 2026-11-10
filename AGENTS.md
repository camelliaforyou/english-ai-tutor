# Agent instructions — repository root

## Priority and scope

Follow user requests and repository instructions; this file applies repo-wide. Read the nearest nested `AGENTS.md` before editing an app. If instructions conflict, report the conflict and ask rather than silently changing the product scope.

## Mandatory context before edits

1. `README.md`
2. `docs/PRODUCT.md`
3. `docs/ARCHITECTURE.md`
4. `docs/DECISIONS.md`
5. Relevant `apps/*/README.md` and `apps/*/AGENTS.md`
6. Current task file in `docs/tasks/` when one exists

## Product guardrails

- Build a **local-first English speaking tutor**, not a general-purpose agent platform.
- Default stack: Next.js 16 / TypeScript / App Router, FastAPI / Python 3.11 / uv, Ollama `qwen3.5:9b`, local STT and TTS.
- MVP interaction is push-to-talk, request/response; do not introduce WebRTC, auth, billing, databases, queues or cloud AI without explicit approval.
- Keep model implementations behind interfaces so Whisper, Qwen, Kokoro can be replaced independently.
- Conversation model replies briefly in English; explanations and learner feedback are separate concerns.
- Never infer pronunciation quality from transcripts alone.
- Never send recorded audio or transcripts to third-party services without explicit approval.

## Change protocol

Before coding: state goal, affected files, assumptions and acceptance checks. Prefer smallest complete change. Do not add packages, services or infrastructure without justification. After coding: run applicable checks (or state why not), summarize changes, note risks and next step. Update docs if architecture or API contracts change. Do not invent test results.

## Security and hygiene

No secrets or raw personal audio in git. Validate upload type/size and limit recording duration before production use. Bind local services to loopback for development. Do not execute untrusted commands or remove user data without approval.

## Definition of done

Acceptance criteria met; lint/typecheck/tests relevant to change run or explicitly deferred; docs consistent; no unrelated refactors; clear handoff summary.
