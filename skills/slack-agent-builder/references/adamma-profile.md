# Adamma's Profile — Slack Agent Builder Reference

This file shapes every idea, recommendation, and suggestion in the Slack Agent Builder skill. Read it before generating ideas or making build path recommendations.

---

## Who She Is

Adamma Ihemeson is a Human-Centered AI Systems & Literacy Architect. She builds agentic AI apps using Claude Code, teaches AI literacy through her AI with AI brand, and is positioning herself as an authority at the intersection of AI systems, learning science, and human-centered design.

**She is the first user of this skill.** Everything built here will eventually be productized and taught to others.

---

## Her Stack

| Tool | Role |
|---|---|
| Claude Code | Primary build tool — vibe coder, not a traditional developer |
| Vercel | Deployment for all apps |
| Clerk | Authentication |
| Neon | Primary database (serverless Postgres) |
| Supabase | Secondary database (some apps) |
| Make | Complex automations |
| Zapier | Simple automations |
| Slack | Communication + agent interface |
| Claude API | AI backbone for all agents |

**Important:** She uses Neon as her primary database — NOT Redis or Upstash. When memory is needed for a Slack agent, the recommendation is always Neon Postgres, not Redis. Neon is agent-ready, serverless, and already in her stack.

---

## Her Apps (Potential Slack Agent Sources)

| App | What It Does | Slack Agent Potential |
|---|---|---|
| Persist | AI student retention for course creators | Agent for course creators: "How are my students doing this week?" |
| SkillPath | Curated learning paths with IRL events | Agent for learners: "What should I learn next?" |
| Bordermath | Visa compliance for digital nomads | Agent for nomads: "Am I compliant with my current itinerary?" |
| Briefly Brilliant | LSAT prep with score-matched resources | Agent for LSAT students: "Quiz me on logical reasoning" |
| Detour | Financial planning for non-linear careers | Agent for users: "Can I afford to take 3 months off?" |
| Vibe Lab | Skills assessment for vibe coders | Agent for vibe coders: "What should I learn to level up?" |

---

## Her Workflow (Personal Agent Opportunities)

Things she does repeatedly that a Slack agent could handle:
- App Flip Scout (already built — could live in Slack natively)
- Weekly planning and priority setting
- Research questions about her apps, their markets, or competitors
- Social media content brainstorming
- AI literacy curriculum development
- Community event planning for AI with AI

---

## Her Audience (Who Her Agents Would Serve)

1. **Vibe coders** — non-traditional developers building with AI tools, ADHD-aware, need step-by-step guidance
2. **AI learners** — people new to AI who want accessible, non-intimidating guidance
3. **Digital nomads** — long-term travelers managing visa and finance complexity
4. **Course creators** — solo educators trying to retain students and build community
5. **LSAT students** — high-stakes learners who need personalized, accountable support

---

## Her Build Style

- Vibe coder: she builds through AI tools, not by writing code directly
- Screenshots are her primary debugging method
- She needs verbatim prompts she can paste into Claude Code — not explanations of what to type
- One step at a time — never a wall of information
- ADHD-aware pacing is non-negotiable
- She likes to understand the "why" behind architecture decisions, not just follow instructions blindly
- She's building for herself first, then teaching others — so every build should be documented clearly enough to turn into a lesson

---

## Build Path Guidance for Her

**Path A (No-Code/Zapier):** Good for personal workflow agents she wants to test same-day. Not suitable for anything she'd put in front of app users.

**Path B (Bolt + Vercel + Neon):** Her real path. She already uses Vercel and Neon. Bolt for JavaScript + Next.js is compatible with her Claude Code workflow. The Vercel Slack Agent Skill (`npx skills add vercel-labs/slack-agent-skill`) runs directly in Claude Code and guides the entire scaffold. This is the path to recommend for anything production or user-facing.

**Memory:** Always use Neon for memory. Neon has a published guide for Slack + Neon + Vercel AI SDK. The schema is simple: `conversations` table with channel_id, thread_ts, role, content, created_at. That's the foundation for any agent memory in her stack.
