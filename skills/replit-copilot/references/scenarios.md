# Common Replit Build Scenarios

Playbooks for situations that regularly come up between steps. Use these as the right move to make — not scripts to read verbatim.

---

## Preview Shows a Blank Page or "Cannot Connect"

**Signals:** White blank Preview pane, "This site can't be reached," or a loading spinner that never resolves.

**Move:**
> "The app isn't running yet — that's all this is. Paste this into Replit Agent: 'The app isn't loading in Preview. Please start the app and make sure it's running on the correct port.' Wait a moment, then refresh the Preview."

If that doesn't work: open the **Console tab** in the bottom panel and look for red error text. Paste the exact error into Agent.

---

## Agent Stops and Asks a Question Mid-Task

**Signal:** Replit Agent pauses and shows a question or asks the user to make a choice before continuing.

**Move:** This is normal — Agent asks for clarification when it encounters a genuine decision. Read what it's asking and either:
- Answer directly in the Agent chat
- Or paste: "Make your best judgment and continue. Default to the simpler approach."

If Agent seems stuck in a loop, tell the user:
> "In the Agent chat, click the ✕ or stop button to cancel the current task. Then paste the step prompt again as a fresh message."

---

## Something Broke — Use a Checkpoint

**Signal:** Agent just made changes and now the app is broken, showing errors, or behaves worse than before.

**Move:** Don't try to fix forward. Roll back first.
> "Open the **History** panel — click the clock icon in the left sidebar (or look for 'History' in the Agent panel). You'll see a list of checkpoints. Find the one just before this step and click **Rollback here**. Agent will show you exactly what will be restored before applying it. Once you're back to the working version, come back here and we'll try again."

After rolling back: rewrite the step prompt more narrowly (one thing at a time, explicit constraints) before retrying.

---

## Agent Changed Too Much

**Signal:** User asked for a small change and Agent rewrote unrelated pages, changed the design, or removed existing features.

**Move:** Roll back first (see above), then retry with a tighter prompt. Add to the prompt:
> "Keep all existing pages, styles, and functionality exactly as they are. Only change [the specific thing]. Do not modify anything else."

If the user doesn't want to roll back: paste this into Agent:
> "You changed more than I asked for. Please undo the extra changes and restore everything to how it was before, except for [the specific requested change]."

---

## Sign-In Works in Preview But Not on the Public URL

**Signal:** After publishing, clicking "Sign in" shows an error, redirects to a broken page, or Clerk/Replit Auth doesn't recognize the user.

**Move:**
> "Paste this into Replit Agent: 'Sign-in works in Preview but not on the published URL. Please confirm the Production Clerk/Replit Auth credentials are wired into the published deployment and re-publish if needed.'"

Context for you: Clerk has separate Development and Production environments. Agent provisions both, but the Production credentials need to be applied before publishing. If Agent didn't do this automatically, a re-publish usually fixes it.

---

## Data Doesn't Persist After Refresh or Publish

**Signal:** Data the user saved disappears when they refresh the page or republish. Or data shows in Preview but not on the public URL.

**Move:**
> "Paste this into Replit Agent: 'Data isn't persisting after refresh [or: after publishing]. Please confirm the app is reading and writing to the Neon database (not in-memory storage), and that the Production Neon database is connected to the published deployment.'"

Context: Neon has separate Development and Production databases. Agent wires the Production database into the published deployment automatically, but sometimes it needs a re-publish to take effect. If the user is using Replit Database instead of Neon, the same logic applies.

---

## Secrets Not Available in the App

**Signals:** `undefined` values for environment variables, API calls failing with missing key errors, `process.env.MY_KEY` returning undefined.

**Move:**
1. Confirm the user added the Secret correctly: 🔒 Secrets icon in the left sidebar → confirm the key name matches exactly (case-sensitive, no extra spaces).
2. Secrets don't update in a running app — they load fresh when Agent restarts the app. Tell the user: "Paste this into Agent: 'Please restart the app so it picks up the new Secrets.'"
3. If the issue persists: paste into Agent: "The secret [KEY_NAME] isn't loading. Make sure it's being accessed via `process.env.KEY_NAME` in server-side code only — Secrets can't be read from client-side JavaScript."

> Secrets are server-side only. If the user's code tries to read a Secret from a React component or other client-side code, it won't work. It must go through a server route or API endpoint.

---

## Publishing Fails

**Signal:** The publish attempt shows an error, or the app is broken on the public URL after publishing.

**Move:**
> "In the Publishing panel (Tools & Files → Publishing), click into the failed deployment and open the logs. Find the first red error line — that's the root cause. Then paste into Agent: 'The deployment failed with this error: [paste the error]. Please find and fix the cause.'"

Don't diagnose publishing errors from verbal descriptions — the deployment logs are always faster.

---

## User Can't Find Something in the Replit UI

**Signal:** "Where do I add my API key?" / "Where's the terminal?" / "How do I see the database?"

**Move:** Give exact navigation steps. Current UI locations:

- **Secrets (API keys):** Left sidebar → 🔒 lock icon → click "New secret"
- **Shell (terminal):** Bottom panel → Shell tab
- **Console (app logs):** Bottom panel → Console tab
- **History / Checkpoints:** Left sidebar → clock icon, OR look for "History" in the Agent chat panel
- **Publishing:** Left sidebar or Tools & Files panel → Publishing tile; or look for the inline Publish card that appears in the Agent chat after a build
- **Preview URL (public):** After publishing — top of the Preview pane shows the public URL, or check the Publishing panel

If the UI has changed (Replit updates frequently), say: "Replit's interface updates regularly — if you don't see it where I described, a screenshot will help me guide you directly."

---

## User Accidentally Shares a Secret Key or Credential

**Signal:** User pastes a `.env` block, raw API key, or credential into the chat.

**Move:** Stay calm. Distinguish key type:

- **Public/publishable keys** (Stripe publishable key, Firebase client config, Supabase anon key) — these are designed to be visible in the browser. "That's your publishable key — it's designed to be visible, so no worries."
- **Secret keys** (OpenAI key, Stripe secret key, Supabase service role key) — let them know calmly: "That one should be kept private. Go to [the relevant dashboard] and rotate it — generate a new one and add it to Replit Secrets instead. I'll wait."

Never lecture. One sentence of context, then move on.

---

## User Asks Which Option to Choose

**Signal:** "Should I use Replit Auth or Clerk?" / "Should I use Neon or Replit Database?" / "Next.js or Express?"

**Move:** Give one direct recommendation with one sentence of reasoning.

Common recommendations:
- **Replit Auth vs Clerk** → Clerk for production apps with public users who don't have Replit accounts. Replit Auth for internal tools, quick prototypes, or apps where users already have Replit accounts. "Clerk gives your app its own branded sign-in and Agent sets it up automatically — use it if this is a real app with real users."
- **Neon vs Replit Database** → Neon for anything that needs to persist reliably in production, or has user-specific data. Replit Database for simple prototypes. "If real users will use this app, use Neon — it separates your dev and production data automatically."
- **Next.js vs Express** → Next.js for full-stack apps with pages the user visits. Express for pure API backends. "If your app has screens people navigate to, use Next.js."
- **Autoscale vs Reserved VM deployment** → Autoscale for most web apps (scales to zero when idle, lower cost). Reserved VM for apps that need to always be on, like WebSocket-based apps or background job processors.

---

## Plan Mode: When to Suggest It

**Signal:** The user is about to attempt a complex step — major database migration, adding auth, payment integration, or anything that touches many files.

**Move:** Proactively suggest Plan Mode before the user pastes the prompt:
> "This is a bigger step. Before pasting the prompt, toggle **Plan** on in the Agent chat (the checkbox next to the send button). That way Agent will show you its full plan before making any changes — you can review and approve it, or ask Agent to adjust the plan first."

Plan Mode is especially useful when:
- The step touches authentication, database schema, or payments
- A mistake would require significant rollback effort
- The user wants to understand what Agent intends before it starts

---

## User Describes a Problem Vaguely

**Signal:** "Something's not working" / "The page looks weird" / "It's showing an error"

**Move:** Don't guess. Ask for a screenshot immediately:
> "A screenshot would help me see exactly what's happening — feel free to attach one."

Once you have it: read the Agent chat panel, any red text in the Console tab, the Preview URL, and the visible UI. Respond based on what you can see.

---

## Tone Guide

These rules apply throughout every build.

**When things break:** Start with the fix, not the diagnosis.
> ✅ "No worries — this is a common one. Here's what to do: [fix]"
> ❌ "It looks like the issue might be related to..."

**Celebrating progress:** Briefly acknowledge the completed step before delivering the next one.
> "🎉 Step 3 done — the database is connected. Here's Step 4."

**Never imply the user did something wrong.** Even if they skipped a verification step or pasted a prompt into the wrong place — respond with the fix, not the judgment.

**Short sentences in instructions.** Especially UI actions.
> ✅ "Open the History panel."
> ❌ "In order to access your version history, you'll want to find the clock icon in the left sidebar and click it to open the History panel."

**Jargon:** Define it the first time, inline.
> "Add it to Secrets (Replit's secure storage for API keys — the 🔒 icon in the left sidebar)."

After the first use, you can use the term without explaining it again.

**Agent vs Shell:** Always prefer a Replit Agent prompt over a manual Shell command. Shell is a last resort. Most things Agent can handle directly through its own tools.
