# Step Format

Every step you deliver must follow this exact structure. Read the template, then the annotated example below it.

---

## Template

```
## ✅ Step [N] — [Step Title]

[Optional: One sentence of context — what this step does and why it matters now.]

Paste this into Replit Agent:

\```
[The complete Replit Agent prompt. Nothing omitted. No paraphrasing. Copy-pasteable as-is.]
\```

**What to verify before moving on:**
- [Specific place in the Replit UI to check and exactly what to look for]
- [Specific action to take and the expected result]
- [If there's a preview — what URL to open, what to click, what should appear]
- [Any console or Shell output to confirm — and what passing output looks like]

> 💡 **Tip:** [One specific Replit gotcha for this step. Skip this block entirely if nothing notable.]

Once everything looks good, type **`done`** and I'll give you Step [N+1].
```

---

## Annotated Example

```
## ✅ Step 3 — User Authentication

This step adds login and sign-up so only registered users can access the app. We're doing it now so every page we build from here can check who's logged in.

Paste this into Replit Agent:

\```
Add user authentication to this app using Replit Auth.

Set up Replit Auth so that:
- Any page under /dashboard requires the user to be logged in. If they're not logged in, redirect them to /login.
- The /login page shows a "Sign in with Replit" button that triggers the Replit Auth flow.
- After a successful login, the user is redirected to /dashboard.
- The navbar shows the logged-in user's display name and a "Sign out" button. Clicking Sign out ends the session and redirects to /.

Use the existing Express server in server.js. Store session data in Replit DB (key: `session:[userId]`).

Keep all existing routes and UI — only add the auth layer on top.
\```

**What to verify before moving on:**
- Click the Run button (▶) and wait for the preview to load.
- In the preview, navigate to `/dashboard` in the URL bar. You should be redirected to `/login`.
- Click "Sign in with Replit." You should be taken through the Replit Auth flow and then land on `/dashboard`.
- Confirm your display name appears in the navbar, along with a Sign out button.
- Click Sign out. You should be redirected to the home page and `/dashboard` should redirect you to `/login` again.

> 💡 **Tip:** Replit Auth only works when the app is running — it won't work in a local preview outside of Replit. If the "Sign in with Replit" button doesn't appear, check the Console tab in the bottom panel for any server errors and paste them into Replit Agent to fix.

Once everything looks good, type **`done`** and I'll give you Step 4.
```

---

## When the Step Has No Visible UI Output

Some steps — config, utility functions, database schema setup, Secrets — produce nothing visible in the preview. When this happens, tell the user explicitly:

> "This step doesn't change anything you'll see in the preview — that's expected. Check [specific location] to confirm it worked."

Then redirect them to the right verification spot:
- Database step → check Replit DB in the left sidebar, or open the Shell and query it
- Secrets step → open the 🔒 Secrets panel and confirm the key appears
- Package install step → check the Packages tab or look for a green success message in the Replit Agent panel
- Config file step → open the file in the Files pane and confirm the content

---

## Tip Block Usage

Only include the `> 💡 **Tip:**` block if there is a genuine Replit-specific gotcha at this step. Common reasons to include one:

- Replit Auth only works in a running Repl, not a static preview
- Secrets won't be available until the Repl is restarted after adding them
- Replit DB is only accessible server-side — client code can't reach it directly
- The Run button needs to be clicked after Replit Agent finishes making changes
- A package installed by Replit Agent may need the Repl to restart before it loads

If there is no notable gotcha, omit the tip block entirely. Don't write tips for their own sake.
