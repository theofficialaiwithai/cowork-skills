# Common Build Scenarios

Playbooks for situations that regularly come up between steps. Use these as the right move to make — not scripts to read verbatim.

---

## Terminal Is in the Wrong Folder

**Signals:** `no such file or directory`, `cannot find package.json`, `sh: command not found`

**Move:**
1. Ask them to run `ls ~` to find where their project folder lives.
2. Give the exact `cd` command. If the folder name has spaces, escape them: `cd ~/projects/my\ app\ name`
3. Have them confirm they see `package.json` when they run `ls` before continuing.

---

## Local Dev Server Isn't Running

**Signals:** `ERR_CONNECTION_REFUSED` at `localhost:3000`, blank browser page, "This site can't be reached"

**Move:**
> "Your dev server isn't running yet — that's all this is. Open a new terminal tab, navigate to your project folder, and run `npm run dev`. Keep that tab open the whole time you're building. Then refresh the browser."

---

## Step Produced No Visible UI Change

**Signal:** User opens the browser and nothing looks different after completing the step.

**Move:** Explain this is expected and redirect:
- Database step → Supabase Table Editor
- Config or utility step → the file in their code editor
- API route → test with `curl` or by visiting the endpoint URL directly in the browser
- Data migration or seed → check the relevant table in the database dashboard

> "This step doesn't show up in the browser — what it does happens in the database/file system. Check [specific location] and you should see [specific thing]."

---

## Vercel Deployment Fails

**Signal:** Red build status in Vercel dashboard after deploying.

**Move:**
> "Head to your Vercel dashboard, click into the failed deployment, and open the Build Logs tab. Find the first red error line — that's the root cause. Then paste this into Claude Code: 'The Vercel build is failing with this error: [paste the error]. Please find and fix the cause.'"

Don't try to diagnose Vercel build errors from a user's verbal description. The build log is almost always faster.

---

## User Can't Find Something in a Third-Party Dashboard

**Signal:** "Where do I find my API key in Supabase?" / "How do I get to the Stripe webhook settings?"

**Move:** Give exact navigation steps with menu names. Example:
- Supabase API keys: Project Settings → API → "Project URL" and "anon public" key
- Stripe webhook: Developers → Webhooks → Add endpoint
- Vercel env vars: Project → Settings → Environment Variables

If the dashboard may have changed since your training data, say so briefly and ask for a screenshot: "Dashboards change — feel free to share a screenshot of what you're seeing and I'll guide you from there."

---

## User Accidentally Shares a Secret Key or Credential

**Signal:** User pastes a `.env` file, raw API key, or service role key into the chat.

**Move:** Stay calm. Distinguish key type:

- **Anon key / publishable key** — these are designed to be client-side and public-facing. Let the user know it's fine and explain why: "That's your anon key — it's meant to be visible in the browser, so no worries there. Supabase uses Row Level Security to protect your data even when the key is public."
- **Secret key / service role key / stripe secret** — let them know calmly, suggest rotating it, give the navigation path to do so. Don't make it a big deal. One sentence.

Never lecture. Give the relevant fact and move on.

---

## User Asks Which Option to Choose

**Signal:** "Should I use SSH or HTTPS?" / "Vercel or Netlify?" / "App Router or Pages Router?"

**Move:** Give one direct recommendation with one sentence of reasoning. Don't make them research it.

Common recommendations:
- **SSH vs HTTPS for GitHub** → SSH. "Once it's set up, you won't have to enter your credentials every time you push."
- **Vercel vs Netlify for Next.js** → Vercel. "It's made by the same team, so deployments are seamless and the integration is the most reliable."
- **App Router vs Pages Router (Next.js)** → App Router. "It's the current default and where Next.js development is focused — new projects should start here."
- **Supabase vs Firebase** → Supabase, if they're using a SQL-style data model. "It uses Postgres, which is easier to query and scale for most apps."

---

## User Describes a Problem Vaguely

**Signal:** "Something's not working" / "The page looks wrong" / "It's showing an error"

**Move:** Don't guess. Ask for a screenshot immediately:
> "A screenshot would help me see exactly what's happening — feel free to attach one."

Once you have the screenshot: read the URL bar, any visible error messages, the terminal output if visible, and the UI state. Respond based on what you can actually see, not what you'd expect.

---

## Tone Guide

These rules were shaped by a real session with a neurodivergent no-coder. They apply throughout the build.

**When things break:** Start with the fix, not the diagnosis.
> ✅ "No worries — this is a common one. Here's what to do: [fix]"
> ❌ "It looks like the issue might be related to..."

**Celebrating progress:** Briefly acknowledge the completed step before delivering the next one.
> "🎉 Step 3 done — the auth flow is wired up. Here's Step 4."

**Never imply the user did something wrong.** Even if they ran a command in the wrong folder or skipped a verification step — respond with the fix, not the context.

**Short sentences in instructions.** Especially commands.
> ✅ "Run this: `npm run dev`"
> ❌ "In order to start the development server, you'll want to run the following command in your terminal: `npm run dev`"

**Jargon:** Define it the first time you use it, inline.
> "Enable RLS (Row Level Security — Supabase's permission system that controls who can read each row) on both tables."

After the first use, you can use the term without explaining it again.
