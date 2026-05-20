# Routine Recommender

This file guides the Recommend Mode questionnaire. The goal is to understand the user's work patterns and pain points well enough to suggest 2–3 routines that would genuinely help them — not generic suggestions, but ones that fit what they actually do.

Ask one question at a time. After each answer, acknowledge it briefly before moving to the next question.

---

## The 5 Questions

**Q1 — Work style**
> "To start — what does your typical workday look like? Are you in a lot of meetings, mostly heads-down on tasks, doing client work, or something else?"

*What you're learning:* Whether their bottlenecks are communication-heavy (email, calendar, Slack), task-management heavy (Notion, Asana), or output-heavy (documents, reports, research).

---

**Q2 — The most repetitive thing they do**
> "What's one thing you find yourself doing over and over that feels like it should just... happen automatically?"

*What you're learning:* The highest-friction manual task. This is usually the strongest routine candidate. Common answers: morning inbox review, weekly task review, meeting prep, pulling metrics, writing follow-up emails.

*If they say "I don't know" or "nothing comes to mind":* Ask "What's the first thing you do when you sit down to work each day?" — that's almost always something automatable.

---

**Q3 — What tools they live in**
> "What are the main apps you use every day? For example — Gmail, Notion, Google Calendar, Slack, a project management tool?"

*What you're learning:* Which MCPs and integrations are actually relevant to them. Don't recommend routines that require tools they don't use.

---

**Q4 — Timing and energy**
> "Are there parts of your day or week that feel chaotic or hard to get started? Like — Monday mornings, end of day, before client calls?"

*What you're learning:* When a routine would be most valuable. A person who struggles on Monday mornings needs a weekly kickoff routine. Someone who loses track before meetings needs a meeting-prep routine. Someone who feels scattered at end of day needs a wrap-up routine.

---

**Q5 — What they want more of**
> "If you could get 30 minutes back each week by having something handled automatically, what would you use that time for?"

*What you're learning:* What they actually value. This helps frame recommendations in terms of what matters to them, not just what's technically automatable.

---

## How to Map Answers to Recommendations

After all 5 answers, identify the 2–3 strongest matches from the patterns below. Pick based on what they said — don't recommend all of them.

### Pattern: Inbox overwhelm + email-heavy work
**Recommend:** Daily Email Triage Routine
- Trigger: Scheduled, weekday mornings
- What it does: Scans unread Gmail, categorizes by urgency, creates a short action list
- Tools: Gmail MCP
- Complexity: Simple
- Why it helps: Replaces the "open inbox and get lost" start to the day with a structured brief

---

### Pattern: Lots of meetings + struggles with prep
**Recommend:** Meeting Prep Routine
- Trigger: On-demand (called before each meeting)
- What it does: Pulls attendees from calendar, researches them, produces talking points and agenda
- Tools: Google Calendar MCP + Web Search
- Complexity: Simple
- Why it helps: Removes the scramble of "who is this person again?" right before a call

---

### Pattern: Monday chaos / weekly planning struggles
**Recommend:** Weekly Kickoff Routine
- Trigger: Scheduled, Monday mornings
- What it does: Pulls open tasks, reviews the week's calendar, identifies top 3 priorities, produces a Word doc briefing
- Tools: Notion MCP (or task tool they use) + Google Calendar MCP + docx skill
- Complexity: Moderate
- Why it helps: Replaces the fuzzy "what am I doing this week?" feeling with a clear starting point

---

### Pattern: Loses track of tasks / projects drift
**Recommend:** End-of-Day Wrap-Up Routine
- Trigger: Scheduled, weekday evenings (e.g. 5pm)
- What it does: Reviews what was completed vs. still open, flags anything overdue, drafts a quick summary note
- Tools: Notion MCP (or task tool) + Gmail MCP (optional, to draft a status update)
- Complexity: Simple
- Why it helps: Creates a clean close to the day and prevents things from falling through the cracks overnight

---

### Pattern: Does client work / lots of outreach
**Recommend:** Client Follow-Up Routine
- Trigger: On-demand (called after a meeting or conversation)
- What it does: Takes meeting notes or context, drafts a follow-up email with next steps, optionally creates a task in Notion
- Tools: Gmail MCP (draft) + Notion MCP (task creation, optional)
- Complexity: Simple
- Why it helps: Eliminates the "I'll write that follow-up later" loop that leads to dropped balls

---

### Pattern: Works with data / needs regular reports
**Recommend:** Weekly Metrics Digest
- Trigger: Scheduled (e.g. Friday afternoons)
- What it does: Pulls key data from a connected source, computes a summary, saves as a spreadsheet or doc
- Tools: Supabase MCP or Google Drive MCP + xlsx skill
- Complexity: Moderate to Advanced
- Why it helps: Replaces manual data pulls with an automatic snapshot ready every Friday

---

### Pattern: Content creator / active on social or email
**Recommend:** Content Ideas Routine
- Trigger: Scheduled (weekly) or on-demand
- What it does: Reviews recent work, notes, or saved links, generates 5 content ideas with angles, saves to a doc
- Tools: Google Drive MCP or Notion MCP + Web Search
- Complexity: Simple
- Why it helps: Keeps the ideas pipeline full without requiring dedicated brainstorming blocks

---

## Presenting Recommendations

After identifying the best 2–3 matches, present them like this (one per section, not a bullet dump):

---

**Option 1: [Routine Name]**
*[One sentence on what it does]*

Based on what you said about [reference their specific answer], this routine would [specific benefit]. It runs [trigger description] and takes about [X minutes] to set up. Complexity: **[Simple / Moderate / Advanced]**.

---

**Option 2: [Routine Name]**
[Same format]

---

**Option 3: [Routine Name]** *(if applicable)*
[Same format]

---

Then ask: **"Which of these feels most useful to start with?"**

Once they pick one, acknowledge the choice and move straight into Phase 1: Discover for that routine — you already have a lot of context from the questionnaire, so Phase 1 will be shorter.
