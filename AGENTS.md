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

---

## Project Continuity Protocol

Before starting implementation work:

1. Read `docs/PROJECT_STATUS.md`.
2. Read `docs/PRODUCT.md`.
3. Read `docs/ARCHITECTURE.md`.
4. Read the relevant task file in `docs/tasks/`.
5. Read the relevant application-level `AGENTS.md`.
6. Check existing implementation before proposing changes.

### Scope Control

- Work only on the active milestone unless explicitly instructed.
- Do not implement future milestones prematurely.
- Do not introduce new infrastructure without justification.
- Do not replace accepted architectural decisions silently.
- Prefer small, independently verifiable changes.

### Completion Protocol

After completing a task:

1. Run relevant lint and type checks.
2. Run available tests.
3. Update API documentation if contracts changed.
4. Update architecture documentation if boundaries changed.
5. Update the active task status.
6. Update `docs/PROJECT_STATUS.md`.
7. Report completed work and remaining issues.

### Source of Truth

- `docs/PRODUCT.md`: Product requirements
- `docs/ARCHITECTURE.md`: System architecture
- `docs/DECISIONS.md`: Technical decisions
- `docs/API.md`: API contracts
- `docs/PROJECT_STATUS.md`: Current progress
- `docs/tasks/`: Task-specific requirements

If documents conflict, do not silently choose one.
Identify the conflict and request clarification.

### Verification Integrity

Never claim that a test, build, or command passed
unless it was actually executed successfully.

Do not mark incomplete work as completed.
