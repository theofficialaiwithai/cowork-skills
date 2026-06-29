# PRD Structure Reference

This file defines the required structure for every PRD the prd-assistant skill produces. Follow every section in order. Do not skip any. The Bordermath PRD (visa route planner for long-term travelers) is the gold-standard tonal and structural benchmark — specific, opinionated, build-ready.

---

## Section 1: What Is [App Name]?

One strong paragraph describing what the product is and what it does. Then 3 tagline options. Taglines must be:
- Punchy, specific, and honest
- NOT generic SaaS marketing language
- Reflective of the actual product, not an aspiration

Bad tagline: "Seamlessly manage your workflow."
Good tagline: "Know exactly how many days you have left before you have to leave."

---

## Section 2: The Problem

Write as narrative prose, not a bullet list. Describe the specific pain the target user experiences today. Use:
- Concrete examples and numbers where possible (e.g., "27 countries, 90 days, one rolling window")
- What the user does *instead* of using this app right now
- What's specifically missing — not just "there's no tool for this" but the exact gap between existing tools and what the user actually needs

This section should feel like a journalist wrote it — specific, concrete, a little urgent.

---

## Section 3: Target User

Three required sub-sections:

**Primary:** Who is the ideal first user? Give a behavioral profile, not just a demographic. What do they do every day? What problem are they actively trying to solve right now?

**Secondary:** Who else benefits but isn't the core focus? Why are they secondary, not primary?

**Not the target (for MVP):** Explicitly name who this product is NOT for. This is as important as who it is for — it keeps scope tight and prevents feature creep from edge cases.

---

## Section 4: Core Value Proposition

One sentence in a blockquote. This is the product's north star — every feature decision should pass through it.

Follow the blockquote with 2–3 bullets explaining the key dimensions of the value.

Example format:
> Bordermath tells you exactly when and where you need to leave — before you get a fine.

- **Precise:** Calculates to the day based on your actual entry/exit history
- **Proactive:** Shows you future options, not just current status
- **Simple:** Designed for travelers, not lawyers

---

## Section 5: MVP Feature Set

Numbered sub-sections (5.1, 5.2, etc.), one per feature. Limit to 5–7 features.

Each feature gets:
- A descriptive name (not just "Feature 1")
- What the user can do (written from the user's perspective)
- Any important implementation detail or constraint
- For calculation-heavy features: the exact logic in plain language or pseudocode

If a feature is "nice to have," it belongs in Section 15 (Phase 2), not here.

---

## Section 6: Out of Scope for MVP

A bullet list of things that will NOT be built in the first version. This section protects the founder from scope creep. Be direct and specific.

Include at least 6–8 items. Examples of good out-of-scope items:
- "No AI routing in MVP — users build itineraries manually"
- "No mobile app — web only"
- "No multi-user accounts — single user per login"
- "No real-time data sync — manual entry only"

---

## Section 7: Brand and Design Direction

Three required sub-sections:

**Tone:** How does the product speak? What is the emotional register? Give a reference point (e.g., "Khan Academy's encouragement meets Notion's restraint").

**Voice:** 3–4 bullet rules for how copy should be written. Include at least one bad/good line contrast if possible.

**Visual Direction:**
- Color system with hex values: background, surface, primary, accent, text, muted text, error state
- Typography choices (heading font, body font — recommend from Google Fonts)
- 2–3 visual principles (e.g., "No stock photography — this is a tool, not a magazine")

Match the color system to the design reference the user provided. If no reference was given, choose a system appropriate to the product's tone.

---

## Section 8: Tech Stack

A table with columns: **Layer | Tool | Why**

Cover at minimum: Framework, Styling, Auth, Database, Deployment. Add AI/API layers if relevant.

Choose the stack based on the build tool the user selected:
- **Claude Code**: Next.js 14 + Tailwind + shadcn/ui + Supabase + Vercel
- **Lovable**: React + Tailwind + Supabase (Lovable handles deployment)
- **Cursor**: Next.js or Vite + Tailwind + Supabase or PlanetScale + Vercel
- **v0**: Next.js + Tailwind + shadcn/ui + Supabase + Vercel
- **Bolt**: Vite + React + Tailwind + Firebase or Supabase

Include a note if a static JSON file is better than a live API for MVP (e.g., "Using a local countries.json instead of a live API — faster to build, no rate limits, MVP data is stable").

---

## Section 9: Data Schema

Write complete SQL for all tables if using a relational database (Supabase/Postgres). Requirements:
- Column names, types, and constraints
- Foreign key relationships
- A short comment on any non-obvious column
- This section should be pasteable directly into the Supabase SQL editor

If using NoSQL, write the document schema with field names, types, and example values instead.

---

## Section 10: App Routes

A table with columns: **Route | Page | Description**

List every URL the app will have in the MVP. Mark pages that require authentication with 🔒.

---

## Section 11: Core Algorithm or Logic (if applicable)

If the product has a calculation, matching engine, scoring system, or any non-trivial logic at its core, write it out here in pseudocode. This prevents the build tool from guessing.

Requirements:
- Specific enough to be testable
- Edge-case-aware (what happens at boundaries?)
- Written so a developer could implement it directly from this pseudocode

If the product has no non-trivial logic, write: "No core algorithm required for MVP — all logic is standard CRUD."

---

## Section 12: MVP Build Order

This is the most important section for a vibe coder. Number each step 1 through N (typically 8–12 steps). For each step, use this exact format:

```
### STEP [N] — [Step Name]

**What it does:** One sentence describing what this step builds.

**[Build tool] prompt:**
[A complete, self-contained, ready-to-paste prompt. Must include:
- What to build
- How to style it (with specific colors/fonts from Section 7)
- What data to use (reference Section 9 schema if needed)
- What behavior to implement
- What to verify afterward
Never assume the build tool remembers previous steps — each prompt must work standalone.]

**After this step, verify:**
- [Specific browser/terminal check]
- [Specific browser/terminal check]
- [What working looks like]
```

**Step ordering rules:**
- Auth before any protected page
- Data schema before any page that reads data
- Core algorithm implementation before any UI that displays its output
- Navigation/layout before individual pages
- Static data/seed data before dynamic features

---

## Section 13: Manual Onboarding Plan (First Users)

Where to find the first 20–30 users, what to offer them, and what to watch when they use the product.

This is the "launch before you're ready" section. The founder should be thinking about real humans before the product is finished. Include:
- Specific communities, subreddits, Slack groups, or Discord servers to post in
- What to offer (early access, lifetime deal, free tier)
- What to watch for in early sessions (what behavior signals the product is working?)

---

## Section 14: Success Metrics

A table: **Metric | Goal**

Include 5–7 metrics. At least one must be about the core trust mechanism — the thing that, if it fails, means the product has failed. For a calculation tool: accuracy. For a matching tool: match quality. For a social tool: repeat engagement.

---

## Section 15: Phase 2 Roadmap

A numbered list of 5–8 features that are out of scope for MVP but clearly belong in the product's future. This gives the founder a sense of trajectory without letting those ideas bloat the current build.

---

## Section 16: Build Tool Tips for Beginners

Include ONLY if the user said "complete beginner" or "some experience" in the discovery phase. Skip for confident/experienced users.

5–7 practical tips for working with their specific build tool. Must be specific to how that tool actually behaves — not generic advice.

**Claude Code tips (examples):**
- Describe what's wrong or what you want, not what code to write
- If something breaks, paste the full error message — don't summarize it
- Ask it to explain what it just built before moving to the next step
- Commit working code before asking for the next change

**Lovable tips (examples):**
- One change per prompt — never ask for multiple things at once
- Always say "do not rebuild from scratch" when making changes
- If a visual element looks wrong, screenshot it and describe what's off
- Use the preview mode frequently — don't just read the generated code

---

## Tone and Style Rules

Apply these throughout the entire PRD:

- **Clear, direct prose.** No generic SaaS buzzwords: no "leverage," "synergy," "seamless experience," "empower," "robust."
- **The problem section should feel urgent and specific** — like a journalist wrote it.
- **Taglines must be honest and specific**, not aspirational fluff.
- **Tech stack choices must be justified**, not just listed.
- **Build prompts must be complete enough to paste without modification.** If the user would need to fill something in, fill it in yourself based on what you know about the product.
- **Write as if you've built this type of product before** and know exactly where the hard parts are.
