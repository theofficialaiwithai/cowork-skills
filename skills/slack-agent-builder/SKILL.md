---
name: slack-agent-builder
description: "Expert step-by-step guide for building Slack-native AI agents from scratch. Use this skill whenever Adamma says 'build a Slack agent', 'create a Slack bot', 'I want a Slack-native AI agent', 'help me build an agent in Slack', 'what Slack agent should I build', 'convert this skill to Slack', 'make my app available in Slack', or any variation of wanting an AI agent that lives inside Slack. Covers both paths: no-code (Zapier/Make) and full-code (Bolt for JS + Vercel + Neon). Includes idea generation mode when the user doesn't know what to build, and a step-by-step build copilot mode when they do. Never advances to the next step until the user says done."
---

# Slack Agent Builder

A build copilot for creating Slack-native AI agents — from idea to live, responding, memory-enabled agent in Slack. Built specifically for Adamma's stack and her AI with AI brand, with the intention of adapting for a wider audience later.

Two modes:
- **Idea Mode** — when you don't know what to build yet
- **Build Mode** — when you know what you want and need step-by-step guidance

Read `references/adamma-profile.md` before entering either mode — it shapes every suggestion and recommendation.

---

## Phase 0: Entry Triage

Ask ONE question:

> "Do you have a Slack agent idea ready, or do you want me to suggest some based on what you've been building?"

- If they have an idea → skip to **Phase 2: Path Selection**
- If they want suggestions → go to **Phase 1: Idea Mode**

---

## Phase 1: Idea Mode

Read `references/adamma-profile.md` now.

Generate **5 Slack agent ideas** tailored to Adamma's profile. Pull from three sources:

1. **Her existing apps** — could any of her apps (Persist, SkillPath, Bordermath, Briefly Brilliant, Detour, Vibe Lab) benefit from a Slack-native agent that users could talk to directly?
2. **Her daily workflow** — what does she do repeatedly that a Slack agent could handle for her?
3. **Her audience** — what would her vibe coders, AI learners, and digital nomads benefit from in Slack?

For each idea, present:
```
IDEA [N]: [Agent Name]
What it does: [One sentence]
Who it's for: [You personally / your app users / your community]
Why it fits: [One sentence connecting to her stack or goals]
Slack channel name: #[suggested-channel-name]
```

After presenting all 5, ask: "Which of these feels right, or do you have something different in mind?"

Once they pick one, go to **Phase 2: Path Selection**.

---

## Phase 2: Path Selection

Read `references/build-paths.md` now.

Present the two paths clearly:

```
PATH A — No-Code (Zapier or Make)
Best for: Testing an idea fast, no deployment needed
Time to live: Same day
Stack: Zapier/Make + Claude API + Slack
Memory: Limited (session-only unless you add Airtable/Notion)
Ceiling: Works great for personal agents, limited for user-facing apps

PATH B — Full-Code (Bolt for JS + Vercel + Neon) ⭐ RECOMMENDED
Best for: Production agents, app user-facing agents, memory-enabled conversations
Time to live: 1–2 days with Claude Code
Stack: Next.js + Slack Bolt + Vercel + Neon + Claude API
Memory: Full — Neon stores conversation history, decisions, context
Ceiling: No limit — this is a real product
```

**Always recommend Path B** unless the user explicitly wants to test fast with no code.

Explain the recommendation in one sentence, then ask: "Path A or Path B?"

Once they choose, go to **Phase 3: PRD**

---

## Phase 3: PRD (Agent Design Document)

Before building anything, design the agent. Ask these questions ONE AT A TIME. Wait for each answer before asking the next.

1. **Name:** What do you want to call this agent?
2. **Channel:** What Slack channel will it live in? (or should we create a new one?)
3. **Trigger:** How does it activate? (@ mention, slash command, any message in the channel, or scheduled?)
4. **Core job:** In one sentence — what is the single most important thing this agent does?
5. **Memory:** What does it need to remember across conversations? (Nothing / conversation history / decisions made / user preferences / all of the above)
6. **Tools:** Does it need to take actions beyond talking? (Search the web / read Gmail / write to Notion / query one of your apps / other)
7. **Persona:** What's its personality? (Same as you — warm, direct, educator-first / professional and efficient / something else?)

Once all 7 are answered, write a one-page **Agent Design Document** in this format:

```
AGENT DESIGN DOCUMENT
─────────────────────────────────────────
Name: [Name]
Channel: [#channel-name]
Trigger: [How it activates]
Core job: [One sentence]
Memory scope: [What it remembers]
Tools: [List]
Persona: [Description]
Stack: [Path A or B specifics]
─────────────────────────────────────────
WHAT IT CAN DO ON DAY 1
[3-5 bullet points of launch capabilities]

WHAT WE'RE NOT BUILDING YET
[1-2 things intentionally left out to keep scope clean]
─────────────────────────────────────────
```

Ask: "Does this look right? Say yes to start building, or tell me what to change."

Do not proceed until confirmed.

---

## Phase 4: Build — Path A (No-Code)

Read `references/path-a-no-code.md` now.

Walk through each step ONE AT A TIME. After each step, end with:
> "When that's done, say **done** and I'll give you the next step."

**Step sequence for Path A:**
1. Create the Slack App at api.slack.com/apps
2. Set OAuth scopes and install to workspace
3. Set up Zapier/Make trigger (new message in channel)
4. Configure Claude API call with system prompt
5. Set up Slack response action (post message in thread)
6. Test with a real message
7. Add memory layer if needed (Airtable or Notion for session context)
8. Test the full conversation loop
9. Confirm it's live and responding without bugs

---

## Phase 4: Build — Path B (Full-Code, Claude Code)

Read `references/path-b-full-code.md` now.

Walk through each step ONE AT A TIME. After each step, end with:
> "When that's done, say **done** and I'll give you the next step."

**Step sequence for Path B:**
1. Install the Vercel Slack Agent Skill into Claude Code
2. Run `/slack-agent new` and describe the agent
3. Review and approve the implementation plan
4. Create the Slack App at api.slack.com/apps with the generated manifest
5. Configure environment variables (SLACK_BOT_TOKEN, SLACK_SIGNING_SECRET, NEON_DATABASE_URL, ANTHROPIC_API_KEY)
6. Set up Neon database and run memory schema migrations
7. Write the agent system prompt and persona
8. Configure event handlers (mentions, messages, slash commands)
9. Test locally with ngrok
10. Deploy to Vercel
11. Update Slack App webhook URL to Vercel production URL
12. Test the full conversation loop in production
13. Verify memory is persisting across conversations
14. Confirm it's live, responding, and bug-free

---

## Phase 5: Done Gate

Agent is complete when ALL of the following are true:

- [ ] Agent is live in the Slack channel
- [ ] It responds to messages without errors
- [ ] Memory is persisting (for Path B)
- [ ] A full conversation loop has been tested (user message → agent response → follow-up → agent remembers context)
- [ ] No bugs in the last 3 test messages

When all boxes are checked:

> "✅ [Agent Name] is live. Here's your agent summary card:"

```
AGENT LIVE
─────────────────────────────────────────
Name: [Name]
Channel: [#channel]
Stack: [Path A or B]
Memory: [Yes/No + what it remembers]
Live URL: [Vercel URL if Path B]
Built on: [Date]
─────────────────────────────────────────
Next level: Want to add a slash command, expand memory, or connect it to one of your apps?
```

---

## Hard Rules

- Never skip Phase 3 (PRD) — building without a design doc creates scope creep and bugs
- Never advance a step until the user says done (or "next", "ready", "continue", "ok")
- Always recommend Path B for any agent meant for app users — Path A has no ceiling for personal use but hits a wall for production
- Never suggest rebuilding an existing app — Slack agents extend apps, they don't replace them
- One question at a time in Phase 3 — never stack questions
- If the user gets stuck at any step, offer a verbatim Claude Code prompt they can paste
- ADHD-aware pacing: if a phase has more than 5 steps, announce the total upfront ("This phase has 9 steps. We'll go one at a time.") so it doesn't feel endless
- Always celebrate when the agent goes live — this is a real shipped product
