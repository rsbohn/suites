# suites

Static field scene with a single plant, backed by a tiny embedded SQLite database and a Vercel serverless function.

## Running locally

1. Install dependencies:
   ```bash
   npm install
   ```
2. Start the Vercel dev server:
   ```bash
   npx vercel dev
   ```
3. Open `http://localhost:3000` to view the page.

## Deployment (Vercel)

- Push this repo to Vercel; the default settings work. The `api/plant.js` function reads `data/field.db` (bundled via `vercel.json`).
- The SQLite file is read-only inside the serverless function runtime. Writes will not persist across invocations.

## Why no WSGI server?

Vercel serves static assets directly and runs Node-based serverless functions for dynamic bits. A WSGI server is unnecessary; the SQLite-backed API is implemented as an API route (`api/plant.js`) and the front-end is plain static HTML/CSS/JS.
