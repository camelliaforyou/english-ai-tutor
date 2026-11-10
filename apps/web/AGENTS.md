# Web agent instructions

Read `../../AGENTS.md` and `README.md` first.

- Use Next.js 16 App Router and TypeScript strict typing.
- Client components only where browser APIs or interaction require them.
- Recording must start from user action; stop microphone tracks when recording stops or component unmounts.
- Show loading, errors and recording state; disable conflicting actions.
- No API keys in client bundles. Local backend base URL should be configurable.
- Keep UI accessible: labels, keyboard interaction, visible state and transcript.
- Prefer built-in React state for MVP; no speculative state management framework.
- Run `npm run lint`, `npm run format:check`, and `npx tsc --noEmit` when scaffolded.
- Keep Prettier and ESLint aligned via `eslint-config-prettier`; do not reintroduce formatting rules in ESLint.

<!-- BEGIN:nextjs-agent-rules -->

## This is NOT the Next.js you know

This version has breaking changes — APIs, conventions, and file structure may all differ from your training data. Read the relevant guide in `node_modules/next/dist/docs/` (resolved from this file's directory; in monorepos the `next` package may not be visible from the repo root) before writing any code. Heed deprecation notices.

This block is written and re-added by `next dev` — verify at `node_modules/next/dist/server/lib/generate-agent-files.js`. Removing it from a diff only re-creates the uncommitted change; committing it with your work keeps the tree clean.

<!-- END:nextjs-agent-rules -->
