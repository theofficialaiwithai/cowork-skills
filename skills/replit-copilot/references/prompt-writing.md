# Writing Replit Agent Prompts

Use this when the PRD doesn't include Replit Agent prompts and you need to write them yourself. These principles are grounded in how Replit Agent actually behaves and what Replit's own docs recommend as of 2025–2026.

---

## How Replit Agent Works (What You're Prompting Into)

Replit Agent is not a chat assistant — it's an autonomous builder. When you send it a prompt, it:
1. Makes a plan (visible to you if Plan Mode is on)
2. Writes and edits code, installs packages, sets up databases and auth
3. Runs the app and tests it
4. Reports back what it did

Agent works best with **clear goals and constraints**, not exhaustive technical specs. It can make implementation decisions on its own — your job is to tell it what success looks like and what must stay the same.

Think of each Agent prompt as a direction memo: here's the goal, here's the acceptance test, here's what not to touch.

---

## The Five Things Every Prompt Must Include

**1. The specific task — scoped to this step only**
Name exactly what this step does. Not "build the app" — "add a reservation form to the booking page."

> "Add a form on the /booking page that lets users select a car, pick a date range, and submit a reservation request."

**2. What success looks like — the acceptance test**
Describe what the user should be able to do when this step is done. This is how Agent knows it finished.

> "When this is done, a logged-in user should be able to fill out the form and submit it. The reservation should appear in the database and show up in the user's 'My bookings' list."

**3. What not to change**
Tell Agent explicitly what to leave alone. This prevents Agent from touching things that are already working.

> "Keep the existing homepage, navbar, and all other pages exactly as they are. Only add the booking form and its server route."

**4. The tech stack — every time**
Agent can lose context across steps. Re-state the key choices in each prompt so it doesn't drift.

> "This is a Next.js app using Clerk Auth for user accounts and Neon (PostgreSQL) for the database."

**5. Where secrets come from — for any step using API keys**
Reference the Replit Secrets key name. Never hardcode values.

> "Read the Stripe key from Replit Secrets as `STRIPE_SECRET_KEY` via `process.env.STRIPE_SECRET_KEY`."

---

## Prompt Length and Scope

The sweet spot for Replit Agent prompts is **100–250 words per step**. Long enough to be specific, short enough to stay focused.

If a feature requires auth + database + UI all at once, split it into multiple steps. Agent does better with one clear goal per prompt.

Rule of thumb: if you find yourself writing "and also..." more than twice, that's a separate step.

---

## When to Use Plan Mode

Some steps are complex enough that you should suggest Plan Mode before the user pastes the prompt. Toggle **Plan** in the Agent chat before submitting.

Use Plan Mode when:
- The step involves auth (Clerk or Replit Auth setup)
- The step involves database migrations or schema changes
- The step touches payments or external API integrations
- You're worried Agent might change too many things at once

In Plan Mode, Agent produces a structured task plan and waits for approval before making any file changes. The user can review and ask Agent to revise the plan before approving.

---

## Example: Weak vs. Strong

**Weak:**
```
Add a dashboard.
```

**Strong:**
```
Build the main dashboard page at the route /dashboard.

This is a Next.js app using Clerk Auth and Neon (PostgreSQL).

The page should be protected — if a user isn't signed in, redirect them to the Clerk sign-in page.

The dashboard should show:
- A welcome message: "Welcome back, [user's first name from Clerk]"
- A grid of project cards. Each card shows: project name (bold), a short description (max 2 lines, truncated with ellipsis), and a "View" button linking to /projects/[id].
- An "Add Project" button in the top-right corner that links to /projects/new.

Fetch only the projects that belong to the currently signed-in user (match on the Clerk userId). Handle the loading state with skeleton placeholder cards.

Styling: use Tailwind CSS. Cards should be white with rounded corners and a subtle shadow. The Add Project button should be indigo.

Keep the existing navbar and footer exactly as they are.

Done looks like: a logged-in user can see their own projects on the dashboard, and a second test account sees only its own projects.
```

---

## Replit-Specific Prompt Patterns

**Clerk Auth — let Agent provision it:**
> "Add user authentication using Clerk Auth. Agent should provision Clerk automatically — do not ask me to create a Clerk account or add any keys. Set up separate Development and Production environments."

**Neon database — let Agent provision it:**
> "Add a PostgreSQL database using Neon. Agent should provision it automatically with separate Development and Production environments. Do not ask me to create a Neon account or add any keys."

**Replit Database (simpler alternative):**
> "Use Replit's built-in database for this. No external database signup needed."

**Secrets:**
> "Read the API key from Replit Secrets as `process.env.MY_API_KEY`. The key has already been added to Secrets."

**Publishing-ready step:**
> "Before finishing, confirm the app is ready to publish: no hardcoded secrets, all environment variables read from `process.env`, and the Production database and auth credentials are wired in."

**Scoping to current user:**
> "All database queries should be scoped to the currently signed-in user's Clerk userId. A user should never see another user's data."

---

## Inferring the Tech Stack

If the PRD doesn't specify the stack and the user hasn't told you, ask before writing any step prompts:

> "Before I write the prompts, I need to know your setup. Which of these are you using? (Or just tell me what's already in your project.)"
> - **Framework:** Next.js / React (Vite) / Express / Flask / Streamlit / Expo?
> - **Styling:** Tailwind CSS / plain CSS / other?
> - **Database:** Neon (PostgreSQL) / Replit Database / other?
> - **Auth:** Clerk Auth / Replit Auth / none yet?

Once confirmed, reference the same stack consistently across all step prompts. Repeat the key choices in each prompt — Agent can lose context between steps.

---

## Common Recommendations

Use these when the user asks you to choose:

- **Auth:** Clerk for production apps with public users. Replit Auth for internal tools or prototypes. Agent provisions both automatically.
- **Database:** Neon for real apps. Replit Database for quick prototypes where separate prod/dev environments don't matter.
- **Deployment type:** Autoscale for most web apps (scales to zero, cheaper). Reserved VM for apps with WebSockets, background jobs, or anything that must always be running.
- **Mobile:** Expo (React Native) — Agent can build and test mobile apps. Guides the user through opening in Expo Go on their phone.
