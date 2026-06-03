# Agentic Patterns Reference

Five core patterns for building apps that act on their own. Read this during Phase 2 to identify which patterns apply to the project.

---

## 1. Webhook — React to External Events

**What it is:** Your app receives a signal from an external service when something happens, then acts on it immediately.

**When it applies:** The user mentions anything that "happens" in an external system — a payment, a form submission, a new record, a message, a sign-up, a status change.

**Real examples:**
- Stripe sends a webhook when a payment succeeds → your app unlocks a feature for that user
- Typeform sends a webhook when a form is submitted → your app saves the response + sends a confirmation email
- GitHub sends a webhook when a PR is merged → your app posts a Slack message to the team
- Calendly sends a webhook when a meeting is booked → your app creates a prep doc in Notion

**How it's built:** Next.js API route (`/api/webhooks/[service]`) that receives a POST request, validates the payload, and triggers the appropriate action.

**Decision signal:** User says anything like "when X happens", "as soon as", "every time someone", "triggered by", "responds to".

---

## 2. Cron — Run on a Schedule

**What it is:** Your app runs a task automatically at a set time interval, without any user action.

**When it applies:** The user mentions anything that should happen "every day", "every week", "each morning", "nightly", "on Mondays", or "automatically over time".

**Real examples:**
- Every Monday at 8am → query the database → generate a Claude summary → email a digest to the user
- Every night at midnight → check for overdue tasks → send a reminder notification
- Every hour → pull new data from an API → update a dashboard in Supabase
- Every day at 9am → scrape competitor prices → compare to last week → alert if significant change

**How it's built:** Vercel Cron Jobs (defined in `vercel.json`) call a Next.js API route on a schedule. That route runs the logic and writes to Supabase/Neon.

**Decision signal:** User mentions a time interval, recurring task, digest, report, sync, or anything that should "just happen" without them initiating it.

---

## 3. MCP — Connect Claude to External Tools

**What it is:** Claude can read from and write to external services during a conversation or agentic task, using the Model Context Protocol.

**When it applies:** The user wants Claude (or their app's AI layer) to interact with an external tool — read from a database, create a Notion page, send a Slack message, query a calendar, update a spreadsheet.

**Real examples:**
- Claude reads from a Supabase database to answer questions about user data
- Claude creates a Notion page when a project milestone is reached
- Claude reads a user's Google Calendar to schedule a follow-up
- A custom MCP server lets Claude write to a proprietary internal tool

**How it's built:** Pre-built MCP servers exist for Supabase, Notion, Slack, GitHub, Google Calendar, and more. Custom MCP servers can be built in Python or TypeScript for any API. Point Claude at the server via `claude_desktop_config.json` or programmatically via the Claude API.

**Decision signal:** The user wants Claude (or their AI feature) to "read from", "write to", "check", "update", or "interact with" an external tool or service — especially Notion, Supabase, GitHub, Slack, Google Workspace.

---

## 4. Automation — Multi-Step Workflows Across Apps

**What it is:** A visual workflow tool (Make or Zapier) orchestrates a series of steps across multiple apps, triggered by an event, schedule, or webhook.

**When it applies:** The user describes a process that touches multiple apps in sequence — "when X happens in app A, do Y in app B, then do Z in app C."

**Real examples:**
- New lead in Typeform → Create contact in HubSpot → Send welcome email via Mailchimp → Add row to Google Sheets
- New row in Airtable → Generate content with Claude API → Post to LinkedIn → Log to Notion
- Stripe payment → Update Supabase → Send Slack notification → Create Notion invoice page
- Weekly: Pull data from Supabase → Format with Claude → Send email digest → Archive old records

**Make vs Zapier decision:**
- **Make**: Multi-step flows, conditional logic, data transformation, loops, error handling — use for anything complex
- **Zapier**: Simple 2–3 step automations, fast setup, widely supported apps — use when speed matters more than complexity

**How it's built:** In Make or Zapier, connect the trigger app, add modules/actions for each step, authenticate each service. Your app exposes a webhook endpoint or uses a native connector.

**Decision signal:** User describes a chain of things that need to happen across multiple apps. Or they say "every time X, then Y, then Z." Or they're doing something manually that involves copying data between tools.

---

## 5. Claude API — AI Reasoning at a Trigger Point

**What it is:** Your app calls the Claude API at a specific moment — inside a webhook handler, a cron job, or a user action — to apply AI reasoning to data, generate content, or make a decision.

**When it applies:** The user wants the app to "summarize", "analyze", "generate", "classify", "suggest", "draft", or "decide" something automatically — especially when triggered by an event or schedule.

**Real examples:**
- New support ticket submitted → Claude API categorizes it and drafts a reply → saved to Supabase
- Weekly cron fires → Claude API reads last 7 days of data → generates an executive summary → emails the user
- New client brief submitted → Claude API extracts key requirements → creates a structured project spec in Notion
- User uploads a document → Claude API extracts action items → adds them to a task list

**How it's built:** Call `anthropic.messages.create()` inside any server-side handler (API route, cron, webhook). Pass the relevant data as context in the user message. Use the response to trigger the next action.

**Decision signal:** User wants something "analyzed", "summarized", "generated", "written", "classified", or "decided" at a moment that isn't directly user-initiated. Or they want the app to be "smart" about something.

---

## Pattern Combinations

The most powerful agentic apps combine multiple patterns:

| Combination | Example |
|---|---|
| Webhook + Claude API | Incoming form → Claude extracts structured data → saves to DB |
| Cron + Claude API + Automation | Daily: query DB → Claude summary → Zapier sends email |
| MCP + Claude API | Claude reads Notion + Supabase to answer complex questions |
| Webhook + Automation | Stripe payment → Make workflow → 5 downstream actions |
| Cron + Webhook + Claude API | Scheduled monitor → detect change → fire webhook → Claude alert |

When you identify multiple patterns in Phase 2, look for opportunities to combine them into a single coherent agentic flow rather than treating them as isolated features.
