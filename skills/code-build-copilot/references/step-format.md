# Step Format

Every step you deliver must follow this exact structure. Read the template, then the annotated example below it.

---

## Template

```
## ✅ Step [N] — [Step Title]

[Optional: One sentence of context — what this step does and why it matters now.]

Paste this into Claude Code:

\```
[The complete Claude Code prompt. Nothing omitted. No paraphrasing. Copy-pasteable as-is.]
\```

**What to verify before moving on:**
- [Specific URL to visit and exactly what to look for]
- [Specific action to take and the expected result]
- [Specific place to check in a third-party tool — name the dashboard, tab, and button]
- [Any command to run in the terminal and what passing output looks like]

> 💡 **Tip:** [One specific gotcha for this step. Skip this block entirely if nothing notable.]

Once everything looks good, type **`done`** and I'll give you Step [N+1].
```

---

## Annotated Example

```
## ✅ Step 2 — Database Setup

This step creates the tables your app needs to store users and posts. We're doing it now so every later step can build on a working schema.

Paste this into Claude Code:

\```
Set up the Supabase database schema for a blog app. Use the Supabase SQL editor to create the following tables:

1. A `posts` table with these columns:
   - id: uuid, primary key, default gen_random_uuid()
   - title: text, not null
   - body: text
   - author_id: uuid, references auth.users(id)
   - created_at: timestamptz, default now()
   - published: boolean, default false

2. A `profiles` table with these columns:
   - id: uuid, primary key, references auth.users(id)
   - display_name: text
   - avatar_url: text
   - created_at: timestamptz, default now()

After creating the tables:
- Enable Row Level Security (RLS) on both tables
- On `posts`: add a policy allowing any authenticated user to SELECT rows where published = true
- On `profiles`: add a policy allowing users to SELECT and UPDATE their own row (where id = auth.uid())

Use the Supabase client already initialized in lib/supabaseClient.ts.
\```

**What to verify before moving on:**
- In your Supabase dashboard, go to Table Editor. You should see two new tables: `posts` and `profiles`.
- Click into each table and confirm the column names match exactly.
- Go to Authentication → Policies. Confirm RLS is enabled on both tables and both policies are listed.

> 💡 **Tip:** RLS stands for Row Level Security — it's Supabase's permission system that controls who can read or write each row. If you see "RLS disabled" on either table, click the toggle to enable it before moving on, otherwise your data will be publicly readable.

Once everything looks good, type **`done`** and I'll give you Step 3.
```

---

## When the Step Has No Visible UI Output

Some steps — config files, utility functions, database schemas, data seeds — produce nothing visible in the browser. When this happens, tell the user explicitly:

> "This step doesn't change anything you'll see in the browser — that's expected. Check [specific location] to confirm it worked."

Then redirect them to the right verification spot:
- Database step → Supabase Table Editor
- Config step → the file in their code editor
- API route → test with a `curl` command or the browser's address bar
- Utility function → terminal output from a test run

---

## Tip Block Usage

Only include the `> 💡 **Tip:**` block if there is a genuine gotcha at this step. Common reasons to include one:

- A setting that is easy to forget but hard to debug later (e.g., enabling RLS, adding a redirect URI)
- A terminal command that needs to be run in a specific folder
- A third-party dashboard that has changed recently and the location may differ from the prompt
- A required environment variable that is easy to miss

If there is no notable gotcha, omit the tip block entirely. Don't write tips for their own sake.
