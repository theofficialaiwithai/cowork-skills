# Writing Claude Code Prompts

Use this when the PRD doesn't include Claude Code prompts and you need to write them yourself. These principles are based on what makes Claude Code produce accurate, on-spec results.

---

## Core Principle: Be Exhaustive, Not Brief

Claude Code does better with more context, not less. A vague prompt produces a vague result. A specific prompt — with file paths, exact column names, colors, and behavior — produces something that actually matches what the user wants.

Think of each Claude Code prompt as a full project brief: include everything Claude Code needs to know so it doesn't have to infer anything.

---

## What Every Prompt Must Include

**1. The tech stack — explicitly**
Name the framework, styling library, state manager, and database client. Don't assume Claude Code will infer them from the project.

> "This app uses Next.js 14 with the App Router, Tailwind CSS, Supabase (configured in `lib/supabaseClient.ts`), and Zustand for state management."

**2. The file path or component name**
Tell Claude Code exactly where to create or modify the file.

> "Create this component at `app/dashboard/page.tsx`."
> "Edit the existing file `components/NavBar.tsx`."

**3. The visual spec — for any step with UI**
Name the colors (Tailwind class or hex), describe the layout, and specify interaction behavior including hover states, loading states, and error messages.

> "The button should be `bg-indigo-600` with white text. Show a loading spinner (use the existing `<Spinner />` component) while the form is submitting. Show a green toast notification on success."

**4. The data spec — for any step with persistence**
Name the database table, exact column names, and when data is saved (on submit, on change, on blur, debounced).

> "Save to the `projects` table in Supabase. Columns: `name` (text, not null), `description` (text), `owner_id` (uuid, set to the current session user's id). Insert on form submit. Show a success toast and close the modal on completion."

**5. What to preserve — for steps that modify existing files**
If the step edits existing code, tell Claude Code what to keep.

> "Keep the existing header and footer layout. Only add the new content section between them."

---

## Prompt Length

There is no upper limit on a useful Claude Code prompt. A three-paragraph, fully specific prompt is better than a three-sentence vague one. The user will paste it directly — they don't need to understand every word.

If you find yourself writing a short prompt, ask: what would Claude Code need to know to get this exactly right? Then add it.

---

## Example: Weak vs. Strong

**Weak:**
```
Build the dashboard page.
```

**Strong:**
```
Build the main dashboard page at `app/dashboard/page.tsx`. This is a protected route — check for a Supabase session on load and redirect to `/login` if none exists.

The page should display:
- A greeting at the top: "Welcome back, [user's display_name from the `profiles` table]"
- A 2-column grid of project cards (1 column on mobile). Each card shows: project name, a short description (max 2 lines, truncated with ellipsis), and a "View" button linking to `/projects/[id]`.
- An "Add Project" button in the top-right corner that opens a modal. The modal contains a form with: name (text input, required), description (textarea, optional). On submit, insert a new row into the `projects` table in Supabase with `owner_id` set to the current user's id. Close the modal and refresh the project list on success.

Styling: use Tailwind CSS throughout. Cards should be `bg-white shadow-sm rounded-lg p-4`. The Add Project button should be `bg-indigo-600 text-white`. The modal should use a semi-transparent overlay.

Fetch projects using the Supabase client from `lib/supabaseClient.ts`. Filter by `owner_id = current user's id`. Handle the loading state with skeleton cards.
```

---

## Inferring the Tech Stack

If the PRD doesn't specify the tech stack and the user hasn't told you yet, ask before writing any step prompts:

> "Before I write the step prompts, I need to know your tech stack. Which of these are you using? (Or tell me what you've already set up.)"
> - Framework: Next.js / Vite + React / SvelteKit / other?
> - Styling: Tailwind / CSS Modules / styled-components?
> - Database: Supabase / Firebase / PlanetScale / other?
> - Auth: Supabase Auth / NextAuth / Clerk / other?

Once confirmed, reference the same stack consistently across all step prompts.
