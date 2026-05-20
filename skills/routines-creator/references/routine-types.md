# Routine Types

Routines fall into three categories based on how they start. Choosing the right type is the most important architectural decision — it determines what tools are needed and how the routine gets built.

---

## Type 1: Scheduled Routines

A scheduled routine runs automatically at a fixed time or interval — no human action required to kick it off.

**Best for:**
- Daily briefings (morning standup, daily digest, end-of-day summary)
- Weekly reviews (weekly kickoff, team sync prep, weekly report)
- Recurring maintenance tasks (inbox triage, task grooming, file cleanup)
- Periodic reports (monthly metrics, quarterly reviews)

**Trigger mechanism:**
Use the `schedule` skill or `mcp__scheduled-tasks` directly to register the routine with a cron-style schedule.

Common schedule patterns:
- Every weekday morning: `0 8 * * 1-5`
- Every Monday at 9am: `0 9 * * 1`
- Every day at 7am: `0 7 * * *`
- First of every month: `0 9 1 * *`
- Every hour during business hours: `0 9-17 * * 1-5`

**Implementation:**
1. Define the routine's full prompt — everything Claude needs to know to run the workflow from scratch (tools to call, how to format output, where to save results)
2. Register it as a scheduled task with the schedule skill
3. The prompt should be self-contained because no conversational context will be available at runtime

**Example prompt structure for a scheduled task:**
```
Run my [Routine Name] routine:
1. [Step 1 with specific tool/action]
2. [Step 2 with specific tool/action]
3. [Output: save to X / send to Y / show in chat]
```

**What to watch for:**
- Scheduled tasks run without a human in the loop — errors happen silently. Build in clear output confirmation so the user can see at a glance whether it ran successfully.
- If the routine depends on live data (e.g., "today's calendar events"), the prompt needs to reference dynamic variables like today's date rather than hardcoded values.

---

## Type 2: Triggered Routines

A triggered routine runs in response to an external event — something that happens in a connected app.

**Best for:**
- Responding to new emails matching certain criteria
- Processing form submissions
- Acting on new Slack messages or mentions
- Reacting to new tasks being assigned in a project tool
- Handling new calendar invites

**Trigger mechanism:**
Triggered routines require a connector between the external event source and Claude. The main options:

**Option A — Zapier MCP**
Use the Zapier integration to create a "Zap" that watches for the event and fires a Claude prompt. Best when the user already uses Zapier or the event source is one of Zapier's 6,000+ supported apps.

**Option B — Make (Integromat) MCP**
Similar to Zapier but more powerful for complex multi-step triggers. Better for advanced logic (conditionals, loops, data transformation).

**Option C — Direct MCP polling**
Some MCPs (Gmail, Google Calendar, Notion) support watching for new items. Claude can be scheduled to poll frequently and act only when new items match criteria. This is less true "event-driven" but works without Zapier/Make setup.

**Implementation:**
1. Identify the trigger event and source app
2. Choose the connector approach (Zapier, Make, or polling)
3. Define the filter criteria (e.g., "only emails from senders not in my contacts" or "only tasks assigned to me")
4. Write the Claude prompt that runs when the trigger fires
5. Walk the user through connecting the source app if they haven't already

**What to watch for:**
- Triggered routines can run frequently — build in rate limiting or deduplication logic if needed
- Make sure the trigger filter is specific enough that it doesn't fire on every event in a busy system

---

## Type 3: On-Demand Routines

An on-demand routine runs when the user explicitly calls it — but it's structured and consistent every time, so the user doesn't have to think about the steps.

**Best for:**
- Processes that need human judgment at the start (e.g., "research this company before my call")
- Tasks that vary in timing but not in structure (e.g., "prep for any meeting")
- Workflows that need user input to personalize (e.g., "write a follow-up email for [person]")
- Complex multi-step tasks the user wants to invoke with a short command

**Trigger mechanism:**
On-demand routines are built as **skills** — a SKILL.md file the user invokes with a `/skill-name` command or by describing what they want.

**Implementation:**
1. Create a skill file in the user's Skills Creator workspace using the DBS framework
2. The SKILL.md should contain the full workflow — Discover, execute, output
3. Include any user-input prompts at the top (e.g., "What's the person's name and company?")
4. Reference any tool integrations needed

**What to watch for:**
- On-demand routines need clear triggering descriptions so Claude knows when to use them
- If the routine needs context from the user (a name, a URL, a date), make sure Phase 1 of the routine captures that before proceeding

---

## Choosing the Right Type

| If the user says... | Routine type |
|---|---|
| "Every morning I want Claude to..." | Scheduled |
| "Every Monday, automatically..." | Scheduled |
| "When I get a new email from X..." | Triggered |
| "Whenever a task is assigned to me..." | Triggered |
| "I want to be able to call this anytime..." | On-demand |
| "I keep doing this manually, help me automate it" | On-demand or Scheduled (ask about frequency) |
| "I want this to just happen without me doing anything" | Scheduled or Triggered |

When in doubt, ask: "Should this run automatically without you doing anything, or do you want to kick it off yourself?"
