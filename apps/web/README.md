# Web — Next.js 16

App Router + TypeScript + Tailwind. Provides microphone recording, transcript display, playback and learning feedback.

## Development (after app scaffolding)

```bash
cd apps/web
npm install
npm run dev
```

Lint / format:

```bash
npm run lint
npm run format
```

Repo-root `pre-commit` also runs ESLint and Prettier on commit. See `docs/SETUP.md`.

## MVP UX

Push to start/stop recording; show recording/processing/playback states, transcript and AI reply. Explicit mic permissions and useful error states. Do not silently record in the background.

## Rules

See `AGENTS.md`. Keep browser-only APIs in client components. Prefer accessible native controls. Avoid adding global state libraries until needed.
