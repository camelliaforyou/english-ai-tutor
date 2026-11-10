# Product scope

## Audience

A Korean adult learning conversational English. Primary goal: natural speaking practice, later post-session grammar/vocabulary feedback.

## MVP user journey

Open local web app -> grant mic permission -> press record -> speak English -> stop -> see transcript -> hear short English response -> repeat.

## Success criteria

- All inference runs locally after initial model/package downloads.
- One complete speech -> transcript -> LLM reply -> speech cycle works.
- Text-only `/chat` smoke test works before audio integration.
- Clear error feedback and no implicit recording.

## Explicitly out of scope

Multi-user SaaS, cloud inference, payments, login, gamification, live interruptions, guaranteed pronunciation scoring.

## Product behavior

The tutor asks one follow-up question and responds in 1-3 natural English sentences. Detailed correction is post-session, not after every utterance.
