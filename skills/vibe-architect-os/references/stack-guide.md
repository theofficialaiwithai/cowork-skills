# Stack Guide Reference

The canonical agentic vibe coding stack. Read this during Phase 3 to confirm tool choices for each agentic pattern.

---

## The Default Stack

Always start here. Only deviate when a specific project requirement demands it.

| Layer | Tool | Why it's the default |
|---|---|---|
| Build | Claude Code | Best AI coding tool for complex, multi-file projects |
| Frontend | Next.js | API routes + frontend in one repo; Vercel-native |
| Deploy | Vercel | Zero-config Next.js deploys, Cron Jobs, Edge Functions |
| Database | Supabase | Real-time, row-level security, visual dashboard, MCP server available |
| Auth | Clerk | Drop-in auth for Next.js; handles sessions, JWTs, user management |
| Automation | Make | Visual multi-step workflows, better data transformation than Zapier |
| Agent Protocol | MCP | Standard protocol for Claude ↔ external tool connections |
| AI Backbone | Claude API (claude-sonnet-4-6) | Best reasoning for agentic tasks; fast, affordable |

---

## When to Swap Each Layer

### Frontend: Next.js vs alternatives

**Keep Next.js when:**
- The app has any backend logic (API routes, auth, database)
- You're deploying to Vercel
- The app has multiple pages or dynamic content

**Swap to plain HTML/CSS when:**
- Pure static landing page or waitlist with no backend
- No user accounts, no database, no dynamic content

**Never use Create React App** — it's deprecated and not Vercel-optimized.

---

### Deploy: Vercel vs Cloudflare vs Netlify

**Use Vercel when:**
- Building with Next.js (it's built for this)
- You need Vercel Cron Jobs for scheduled tasks
- You need serverless API routes

**Use Cloudflare Pages when:**
- Performance and global edge distribution is the priority
- You're building with Cloudflare Workers for ultra-low latency
- The project is more infrastructure-heavy than app-heavy

**Use Netlify when:**
- Simple static site with no backend
- User wants the easiest possible drag-and-drop deploy
- No Vercel Cron or serverless functions needed

---

### Database: Supabase vs Neon

**Use Supabase when:**
- The agentic layer needs **real-time** triggers (Supabase has real-time webhooks)
- The user wants a visual dashboard to see/edit data
- Row-level security (RLS) is needed for user-specific data access
- You want an MCP server for the database (Supabase MCP exists)
- The project includes auth AND database (Supabase has both built in)

**Use Neon when:**
- The project already uses Vercel and wants tight integration (Vercel + Neon is a native pairing)
- Simpler Postgres setup with no real-time requirements
- The user is comfortable with SQL and doesn't need a visual dashboard
- Cost is a concern (Neon's free tier is generous)

**Rule of thumb:** Supabase for most agentic apps (real-time + RLS + MCP). Neon for simpler, Vercel-native projects.

---

### Auth: Clerk vs Supabase Auth vs None

**Use Clerk when:**
- The app has user accounts (almost always yes)
- You want pre-built sign-up/sign-in UI components
- You're using Next.js (Clerk has a Next.js SDK)
- You need social login (Google, GitHub, etc.) with minimal setup

**Use Supabase Auth when:**
- You're already using Supabase and want one less service
- The auth needs are basic (email/password only)
- You want tight integration between auth and RLS

**Skip auth entirely when:**
- Internal tool used only by the builder
- Pure public-facing static page (no accounts)
- Prototype/MVP where auth is premature

---

### Automation: Make vs Zapier

**Use Make when:**
- The workflow has 3+ steps
- Data needs to be transformed between steps (mapping, filtering, reformatting)
- The flow has conditional logic (if X then Y, else Z)
- The user wants to iterate quickly on the workflow visually
- Budget allows (Make is cheaper for high-volume automations)

**Use Zapier when:**
- Simple 2-step automation (trigger → action)
- The user is already a Zapier user
- Speed of setup matters more than complexity
- The app in question only has a Zapier integration, not Make

**Both tools can:**
- Connect to 1000+ apps
- Call webhooks (send and receive)
- Call Claude via HTTP request to the Anthropic API
- Run on a schedule

---

### Agent Protocol: MCP

Use MCP when Claude needs to **read from or write to** an external tool during a conversation or agentic task.

**Pre-built MCP servers available for:**
- Supabase (read/write database)
- Notion (create/update pages)
- GitHub (read repos, create issues, PRs)
- Slack (send messages, read channels)
- Google Calendar (read/write events)
- Google Drive (read/write files)
- Postgres (direct database queries)
- Filesystem (read/write local files)

**Build a custom MCP server when:**
- The external tool doesn't have a pre-built MCP server
- You need Claude to interact with your own app's API
- You're building a product where Claude is a core feature with tool access

**MCP is NOT needed when:**
- The automation is handled by Make/Zapier (they connect apps natively)
- The webhook handler does all the work server-side without Claude needing runtime tool access

---

### AI Backbone: Claude API

Always use `claude-sonnet-4-6` for agentic tasks unless:
- **Speed is critical + task is simple** → use `claude-haiku-4-5-20251001` (faster, cheaper, less capable)
- **The task requires maximum reasoning** → use `claude-opus-4-6` (slower, more expensive, most capable)

**How to call the Claude API in a Next.js API route:**
```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

const message = await client.messages.create({
  model: 'claude-sonnet-4-6',
  max_tokens: 1024,
  messages: [{ role: 'user', content: yourPrompt }],
});
```

Always store `ANTHROPIC_API_KEY` in Vercel environment variables, never in the codebase.

---

## Stack Combinations by Project Type

| Project Type | Recommended Stack |
|---|---|
| SaaS app with user accounts + database | Next.js + Vercel + Supabase + Clerk + Claude API |
| Internal tool or dashboard | Next.js + Vercel + Neon + Clerk (or no auth) |
| Automation-heavy app | Next.js + Vercel + Supabase + Make + Claude API |
| AI-native app (Claude is core) | Next.js + Vercel + Supabase + Clerk + MCP + Claude API |
| Simple landing page or waitlist | Plain HTML or Next.js + Vercel (no DB, no auth) |
| Notification/digest tool | Next.js + Vercel Cron + Supabase + Claude API + Resend |
| Multi-channel AI agent | Next.js + Vercel + Supabase + Openclaw + Claude API |

---

## Agentic Stack Essentials

For any app with a real agentic layer, these three things are non-negotiable:

1. **Environment variables** — All API keys go in Vercel environment variables. Never in code. Keys needed: `ANTHROPIC_API_KEY`, `SUPABASE_URL`, `SUPABASE_SERVICE_KEY`, `CLERK_SECRET_KEY`, and any third-party service keys.

2. **Webhook security** — All webhook endpoints must validate the incoming request (check the signature from Stripe, Typeform, etc.) before acting on it. Never trust an unvalidated webhook payload.

3. **Error handling in cron/webhooks** — Agentic processes run without a user watching. Always log errors to Supabase and handle failures gracefully (retry logic, fallback behavior, alerting).
