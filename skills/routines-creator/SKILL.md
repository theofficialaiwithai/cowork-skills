---
name: routines-creator
description: "Designs and builds Routines for Claude Code — automated, repeatable workflows that run on a schedule, on a trigger, or on demand. Use this skill whenever the user says 'create a routine', 'build a routine', 'I want to automate this', 'help me set up a recurring workflow', 'I do this every week/day and want Claude to handle it', 'set up a scheduled task', 'automate my morning/weekly/monthly process', or describes any task they want to happen automatically or consistently. Also trigger when the user says 'I keep doing X manually' or 'can Claude do Y for me automatically' or 'recommend me a routine' or 'what routine should I build' or 'help me figure out what to automate'. This skill covers the full lifecycle: recommending routines via questionnaire, interviewing the user, designing the routine architecture, identifying the right tools and integrations, and building the routine one step at a time."
---

# Routines Creator

A Routine is a named, repeatable workflow that Claude executes automatically or on demand. This skill helps the user go from "I want to automate X" — or even just "I don't know what to automate" — all the way to a working routine.

**Two ways to start:**

- **"I know what I want to build"** → Go straight to Phase 1: Discover
- **"I'm not sure what to build"** → Start with Recommend Mode

Everything in this skill happens **one step at a time**. Claude asks one question, waits for the answer, then moves forward. Claude never presents a wall of information — only what the user needs right now. When building, each action gets its own step. The user says **"done"** (or "next" or "ready") to advance.

This approach exists because building routines involves a lot of decisions and actions — presenting them all at once creates overwhelm and makes it easy to miss things. One step at a time keeps things clear and manageable.

---

## Recommend Mode

Use this when the user isn't sure what to build, asks for suggestions, or says something like "what routine would help me?" or "recommend me something to automate."

Read `references/routine-recommender.md` for the full questionnaire and recommendation logic.

The questionnaire has **5 questions, one at a time**. After each answer, acknowledge it briefly before asking the next — don't just fire questions back-to-back. Once all 5 are answered, present **2–3 recommended routines**, each with:

- A name and one-sentence description
- Why it fits based on what the user shared
- The trigger type and estimated setup complexity (Simple / Moderate / Advanced)

Then ask: "Which of these feels most useful to start with?"

Once the user picks one, flow directly into Phase 1: Discover for that routine.

---

## Phase 1: Discover

**One question at a time.** Ask only what you need, and wait for the answer before moving on. Never stack multiple questions in one message.

Start with the most important question — what the user actually wants to happen — then follow up based on what they say.

**The questions to work through (in roughly this order):**

1. What do you want this routine to do? (If vague: "Walk me through it — what would happen first, then second, then last?")
2. How should it start — on a schedule, when something happens, or when you call it yourself?
3. What apps or info does it need to touch? (Gmail, Notion, Calendar, local files, etc.)
4. What should the output look like? (Chat summary, a file, an email draft, a calendar event?)
5. Is this just for you, or does it need to work for a team?

When you have enough to move forward, write a **one-sentence summary** of what the routine does and ask the user to confirm:

> "So — a routine that [does X], runs [when], and produces [output]. Does that sound right?"

Wait for confirmation before moving to Phase 2. If they want to adjust something, make the change and confirm again.

---

## Phase 2: Design

Read `references/routine-types.md` to categorize the routine and determine its trigger. Read `references/tool-integrations.md` to identify the right tools for each step.

Present the plan in this format — keep it scannable, not a wall of text:

```
## Routine: [Name]

**What it does:** [One sentence]
**Trigger:** [Specific time/event/call — be exact, e.g. "8:00 AM every weekday"]
**Output:** [What the user gets]

### Steps
1. [Step name] — [What happens, what tool is used]
2. [Step name] — [What happens, what tool is used]
3. [Step name] — [What happens, what tool is used]

### Tools needed
- [Tool]: [Why it's needed]

### Before this runs
[Required setup — connected apps, MCP IDs, anything the user needs to do first]
```

After presenting the plan, explain your key choices briefly. If there's a tradeoff worth mentioning ("I could use Zapier here, but the direct MCP is simpler"), mention it in one sentence and state your recommendation.

Then ask: **"Does this plan look right, or would you like to change anything?"**

If they want changes, update the plan and confirm again before building. Don't start building until the user explicitly approves.

---

## Phase 3: Build

Once the plan is approved, build the routine **one step at a time**. Each step gets its own message. After delivering a step, end with:

> "When you're ready, say **done** and I'll give you the next step."

Wait. Do not advance until the user says done (or "next", "ready", "continue", "ok", "yeah", "yep" — anything that signals they're ready to move forward).

**Structure each build step like this:**

```
**Step [N] of [total]: [Step name]**

[What to do — short, clear, specific. One action.]

[If there's something to check or confirm, note it here in one line.]
```

Keep each step to 3–5 lines max. If a step involves multiple sub-actions, break it into separate steps rather than combining them.

### Build paths by routine type

**Scheduled routines:**
- Step 1: Confirm the cron schedule and show it in plain language ("every Monday at 8am = `0 8 * * 1`")
- Step 2: Write the self-contained task prompt
- Step 3: Register the scheduled task via `mcp__scheduled-tasks__create_scheduled_task`
- Step 4: Confirm it's registered and show the task ID

**On-demand routines:**
- Step 1: Confirm the skill name and where it will live
- Step 2: Write the SKILL.md content
- Step 3: Save the file to the Skills Creator workspace
- Step 4: Confirm how to invoke it

**Event-triggered routines:**
- Step 1: Confirm the trigger event and source app
- Step 2: Set up the connector (Zapier, Make, or direct MCP)
- Step 3: Write the Claude prompt that runs when triggered
- Step 4: Test the trigger with a sample event

### After the last step

Once all steps are done, send a short confirmation message:

> "✅ [Routine Name] is ready. Here's how to use it: [one sentence]. Let me know if you'd like to test it now or adjust anything."

---

## How to communicate throughout

The user may be working through a lot of decisions and actions. These guidelines apply at every phase:

- **One thing at a time.** One question. One step. One action. Never combine.
- **Short messages.** If you're about to write more than 6–8 lines, find a way to split it.
- **Be explicit about what comes next.** End every message with a clear signal: a question, a "say done to continue", or a confirmation prompt. Never leave the user guessing.
- **Acknowledge before moving forward.** When the user answers a question or completes a step, say something brief like "Got it" or "Perfect" before moving to the next thing. It signals you heard them.
- **No jargon without explanation.** If you use a technical term (cron, MCP, webhook), explain it in parentheses the first time: "a cron schedule (the format computers use to define repeating times)".
- **Celebrate small wins.** When a step is done, say so. When the routine is built, make it feel like an accomplishment — because it is.

---

## Key Principles

**Start narrow.** A routine that does three things reliably beats one that tries ten and breaks. If the user's idea is big, suggest starting with the core and expanding once it's working.

**Match the trigger to real behavior.** "Every day" often means "every weekday." Ask. People default to "daily" when they mean Mon–Fri.

**Surface setup requirements early.** If a routine needs Gmail connected, Notion authorized, or a specific plugin installed, say so in Phase 2 — not mid-build when it's frustrating to discover.

**Don't duplicate what exists.** Before building a new routine, check if something similar is already set up. Build on what's there.

---

## Reference Files

- `references/routine-types.md` — Scheduled, triggered, and on-demand routine types with trigger mechanics and implementation guidance. Read during Phase 2.
- `references/tool-integrations.md` — Available MCPs and tools, what they do, and when to use each. Read during Phase 2 when mapping steps to tools.
- `references/routine-recommender.md` — Questionnaire questions and recommendation logic for Recommend Mode. Read at the start of Recommend Mode.
