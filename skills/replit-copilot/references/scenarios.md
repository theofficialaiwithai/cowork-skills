# Common Replit Build Scenarios

Playbooks for situations that regularly come up between steps. Use these as the right move to make — not scripts to read verbatim.

---

## App Preview Shows a Blank Page or "Cannot Connect"

**Signals:** White blank preview, "This site can't be reached," or ERR_CONNECTION_REFUSED in the preview pane.

**Move:**
> "The app isn't running yet — that's all this is. Click the ▶ Run button at the top of the screen and wait a few seconds. Once you see a URL appear in the preview pane, try refreshing it."

If clicking Run produces an error in the console: paste this into Replit Agent: "The app failed to start. Here's the error: [paste error]. Please find and fix the cause."

---

## Replit Agent Stops Mid-Task or Says "I Need Your Help"

**Signal:** Replit Agent pauses and asks the user a question or says it can't proceed.

**Move:** This is normal — Replit Agent asks for clarification when it encounters an ambiguous decision. Read what it's asking, then either:
- Answer the question directly in the Replit Agent chat
- Paste this into Replit Agent: "Make your best judgment and continue. Use [specific preference if relevant] as the default."

If Replit Agent seems stuck in a loop, tell the user: "Click the ✕ to stop the current run, then paste the step prompt again as a fresh request."

---

## Secrets Not Available in the App

**Signals:** `undefined` values for environment variables, API calls failing with missing key errors, "process.env.MY_KEY is not defined."

**Move:**
1. Confirm the user added the Secret correctly: left sidebar → 🔒 Secrets icon → confirm the key name matches exactly (case-sensitive).
2. Secrets take effect on restart. Tell the user: "Click the ▶ Run button again to restart the app — Secrets load fresh on each run."
3. If the issue persists: paste this into Replit Agent: "The secret [KEY_NAME] isn't loading. Make sure the app reads it from `process.env.KEY_NAME` and that it's being accessed in the server-side code, not the client."

> Secrets are server-side only in Replit. If the user's code tries to access a Secret from client-side JavaScript (React component, browser script), it won't work — it must go through a server route.

---

## Package Not Found After Replit Agent Installs It

**Signals:** `Cannot find module 'package-name'`, `ModuleNotFoundError`, import errors right after installation.

**Move:**
> "The package installed but the app needs a restart to pick it up. Click ▶ Run again — that should clear it."

If the error persists: paste into Replit Agent: "The package [name] was installed but is still throwing a module not found error. Please reinstall it and verify the import statement is correct."

---

## Replit Deployment Fails

**Signal:** Red error in the Deployments tab after clicking Deploy.

**Move:**
> "Head to the Deployments tab (rocket icon in the left sidebar), click into the failed deployment, and open the logs. Find the first red line — that's the root cause. Then paste this into Replit Agent: 'The deployment is failing with this error: [paste the error]. Please find and fix the cause.'"

Don't try to diagnose deployment errors from a verbal description. The deployment log is almost always faster.

---

## User Can't Find Something in the Replit UI

**Signal:** "Where do I add my API key?" / "How do I see the database?" / "Where's the terminal?"

**Move:** Give exact navigation steps. Common locations:

- **Secrets (env vars):** Left sidebar → 🔒 lock icon → "New secret"
- **Shell (terminal):** Bottom panel → Shell tab (or press Ctrl+Shift+S)
- **Replit DB:** Left sidebar → database icon, OR access via Shell: type `node -e "const db = require('@replit/database'); new db().list().then(console.log)"`
- **Packages:** Left sidebar → cube icon
- **Console/logs:** Bottom panel → Console tab
- **Deployments:** Left sidebar → rocket icon, or top toolbar → "Deploy" button
- **Preview URL:** Top of the preview pane — click the external link icon to open in a full browser tab

If the UI may have shifted (Replit updates frequently), say: "Replit's UI changes — if you don't see it where I described, a screenshot will help me guide you directly."

---

## User Accidentally Shares a Secret Key or API Key

**Signal:** User pastes a `.env`-style block, raw API key, or service credential into the chat.

**Move:** Stay calm. Distinguish key type:

- **Public/publishable keys** (Supabase anon key, Stripe publishable key, Firebase client config) — these are designed to be visible client-side. Let the user know it's fine: "That's your publishable key — it's meant to be visible in the browser, so no worries there."
- **Secret keys** (Stripe secret key, OpenAI key, Supabase service role key) — let them know calmly and suggest rotating: "That one should be kept private. Head to [the relevant dashboard] and regenerate it — I'll wait. Then add the new one to Replit Secrets instead of sharing it here."

Never lecture. One sentence, then move on.

---

## Replit Agent Rewrites Too Much

**Signal:** After pasting a step prompt, Replit Agent changes things the user didn't ask it to change — breaking existing features or restyling pages.

**Move:** Tell the user:
> "Paste this into Replit Agent to roll back and redo the step more carefully:"

```
You changed more than I asked for in the last step. Please undo those extra changes and redo only what was requested: [summarize the step's specific request]. Keep everything else exactly as it was.
```

If the situation is complex: "Click the ↩ Undo icon in Replit Agent's interface to revert the last set of changes, then we'll try the prompt again with tighter instructions."

---

## User Asks Which Option to Choose

**Signal:** "Should I use Replit DB or Supabase?" / "Python or Node?" / "Replit Auth or something else?"

**Move:** Give one direct recommendation with one sentence of reasoning. Don't make them research it.

Common recommendations:
- **Replit DB vs Supabase** → Replit DB for simple apps with no complex queries; Supabase if they need relational data, user auth, or will scale. "Replit DB is one click to set up — use it unless you know you'll need SQL or a lot of users."
- **Node.js vs Python** → depends on the app. Node for web apps with real-time features; Python for data/AI/ML or if they already know Python. "If you're building a web app and have no preference, Node is a safe default."
- **Replit Auth vs custom auth** → Replit Auth for simplicity. "It's one prompt to set up and handles everything — use it unless you need social logins (Google, GitHub) or complex user roles."
- **Express vs Next.js** → Next.js for full-stack apps with a UI; Express for pure API backends. "If your app has pages the user visits, go Next.js. If it's just an API, Express is simpler."

---

## User Describes a Problem Vaguely

**Signal:** "Something's not working" / "The page looks wrong" / "It's showing an error"

**Move:** Don't guess. Ask for a screenshot immediately:
> "A screenshot would help me see exactly what's happening — feel free to attach one."

Once you have the screenshot: read the Replit Agent panel, any red text in the console, the preview URL, and the UI state. Respond based on what you can actually see.

---

## Tone Guide

These rules were shaped by working with neurodivergent no-coders and first-time builders. They apply throughout the build.

**When things break:** Start with the fix, not the diagnosis.
> ✅ "No worries — this is a common one. Here's what to do: [fix]"
> ❌ "It looks like the issue might be related to..."

**Celebrating progress:** Briefly acknowledge the completed step before delivering the next one.
> "🎉 Step 3 done — the database is set up. Here's Step 4."

**Never imply the user did something wrong.** Even if they skipped a verification step or used the wrong key — respond with the fix, not the context.

**Short sentences in instructions.** Especially UI actions.
> ✅ "Click the ▶ Run button."
> ❌ "In order to restart the development server, you'll want to find the Run button at the top of the screen and click it."

**Jargon:** Define it the first time you use it, inline.
> "Add it to Replit Secrets (Replit's secure storage for API keys — found under the 🔒 icon in the left sidebar)."

After the first use, you can use the term without explaining it again.

**Replit Agent vs Shell:** Always prefer a Replit Agent prompt over a manual Shell command. Replit Agent is what the user is comfortable with. The Shell is a last resort.
