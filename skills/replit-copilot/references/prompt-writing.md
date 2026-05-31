# Writing Replit Agent Prompts

Use this when the PRD doesn't include Replit Agent prompts and you need to write them yourself. These principles are based on what makes Replit Agent produce accurate, on-spec results.

---

## Core Principle: Be Specific, Stay Scoped

Replit Agent does better with focused, specific prompts than broad ones. Unlike Claude Code — which is great at long, exhaustive briefs — Replit Agent can go off-track with too many things in a single prompt. The sweet spot is: one clear goal per step, with all the detail needed to get it exactly right.

Think of each prompt as a precise task card: here's what to build, here's what it should look like, here's what to leave alone.

---

## What Every Prompt Must Include

**1. The specific task — not the whole feature**
Name exactly what this step does. Not "build the dashboard" — "build the project card grid on the dashboard page."

> "Add a 2-column grid of project cards to the dashboard page at `/dashboard`."

**2. The tech stack — explicitly, every time**
Replit Agent doesn't always remember previous steps. Re-state the key stack details in each prompt.

> "This app uses Node.js with Express, EJS templates, and Replit DB for storage."

**3. The visual spec — for any step with UI**
Describe the layout, colors (use Tailwind class names or hex codes), and interaction behavior including hover states and loading states.

> "Each card should have a white background, rounded corners, a subtle shadow, the project name in bold, and a 'View' button in indigo. On hover, the card should lift slightly (use a CSS transform or shadow increase)."

**4. The data spec — for any step with persistence**
Name the exact Replit DB keys, Supabase table names, or data structure being used. Specify when data is saved and what happens on success or failure.

> "Save the project to Replit DB under the key `project:[userId]:[projectId]`. After saving, redirect to `/dashboard` and show a green success banner at the top of the page."

**5. What to preserve — for steps that modify existing features**
If the step edits existing code, explicitly tell Replit Agent what not to change.

> "Keep the existing navbar, footer, and homepage layout exactly as they are. Only add the new project cards section between the header and footer."

**6. Where secrets come from — for any step using API keys**
Reference the Replit Secrets key name. Never hardcode values.

> "Use the API key stored in Replit Secrets as `OPENAI_API_KEY`. Access it via `process.env.OPENAI_API_KEY` in the server route."

---

## Prompt Length and Scope

Replit Agent handles medium-length prompts well — around 100–300 words per step. Shorter than a Claude Code prompt, but never vague.

If a step is complex (like setting up auth + session handling + UI at once), break it into two separate steps. This keeps Replit Agent focused and reduces the chance of it going off-script.

Rule of thumb: if you find yourself writing "and also..." more than twice, that's a separate step.

---

## Example: Weak vs. Strong

**Weak:**
```
Build the dashboard.
```

**Strong:**
```
Build the main dashboard page at the route `/dashboard`.

This is a protected route. If the user is not logged in (no session), redirect them to `/login`.

The page should show:
- A welcome message at the top: "Welcome back, [user's display name]."
- A 2-column grid of project cards. Each card shows: project name (bold), a short description (max 2 lines, truncate with ellipsis if longer), and a "View" button linking to `/projects/[id]`.
- An "Add Project" button in the top-right corner that links to `/projects/new`.

Fetch projects from Replit DB using the key pattern `project:[userId]:*`. Filter to only show projects that belong to the logged-in user.

Styling: use Tailwind CSS. Cards should be `bg-white rounded-lg shadow p-4`. The "Add Project" button should be `bg-indigo-600 text-white rounded px-4 py-2`.

Keep the existing navbar and footer exactly as they are.
```

---

## Inferring the Tech Stack

If the PRD doesn't specify the stack and the user hasn't told you, ask before writing any step prompts:

> "Before I write the step prompts, I need to know your setup. Which of these are you using? (Or just tell me what's already in your Repl.)"
> - Language: Node.js / Python / other?
> - Framework: Express / Next.js / Flask / Streamlit / other?
> - Styling: Tailwind CSS / plain CSS / Bootstrap?
> - Database: Replit DB / Supabase / Firebase / other?
> - Auth: Replit Auth / custom / none yet?

Once confirmed, reference the same stack consistently across all step prompts. Replit Agent can lose context across steps — repeating the stack in each prompt is a small redundancy that prevents big mistakes.

---

## Replit-Specific Prompt Patterns

**Adding a Secret:** Always tell Replit Agent to read from `process.env`, not to hardcode the value.
> "Read the API key from `process.env.MY_API_KEY`. The user has already added it to Replit Secrets."

**Using Replit DB:** Be explicit about key structure. Replit DB is a flat key-value store — there are no tables.
> "Store each item under the key `item:[userId]:[itemId]`. Use `await db.set(key, value)` to write and `await db.get(key)` to read. Use `await db.list('item:[userId]:')` to get all items for a user."

**Installing a package:** Let Replit Agent handle it rather than instructing the user to use the Packages tab.
> "Install the `stripe` package and use it to [task]. Do not ask the user to install anything manually."

**Replit Auth:** Use the phrase "Replit Auth" explicitly — Replit Agent knows how to implement it.
> "Add Replit Auth to protect the `/dashboard` route. Use the `@replit/replit-auth` package."

**Deployment readiness:** For the final step, ask Replit Agent to verify the app is production-ready.
> "Make sure the app is ready to deploy: confirm there are no hardcoded secrets, the start command works correctly, and all environment variables are read from `process.env`."
