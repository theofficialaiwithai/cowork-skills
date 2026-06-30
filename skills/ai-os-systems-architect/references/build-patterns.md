# AI OS Build Patterns

Use this during Step D1 to help the user identify which pattern fits their use case.
Each pattern has a different architecture shape, trigger type, and stack recommendation.

---

## Pattern 1: Always-On Assistant OS

**What it is:** A kernel that listens for user input, reasons about it, takes action, and responds. It's always available, like a shell prompt.

**Best for:**
- Personal AI assistants
- Customer-facing chatbots with tool use
- Internal team assistants (Slack bots, etc.)
- AI tutors and coaches

**Shape:**
```
User input → Kernel (LLM) → Selects tool → Tool executes → Kernel synthesizes → Response
                                    ↑
                            (loop back if multi-step)
```

**Key design decisions:**
- The kernel needs a strong system prompt that defines its personality and capabilities
- Memory is usually: system prompt (working) + conversation history (short-term) + user profile in DB (long-term)
- Tools are the "verbs" the assistant can perform (search, write, save, send)

**Stack:** Claude API + Supabase + Next.js frontend or Slack/Telegram interface via MCP
**Trigger:** User message
**Outputs:** Text responses, tool actions (saves, sends, creates)

---

## Pattern 2: Event-Driven Pipeline OS

**What it is:** The OS sleeps until an external event triggers it, then runs a multi-step workflow automatically.

**Best for:**
- Email processing pipelines
- Lead qualification systems
- Form-to-workflow automations
- "When X happens, do Y, Z, W" systems

**Shape:**
```
Webhook/trigger → Kernel reads event → Decides workflow path → Runs Process A → Runs Process B → Output
```

**Key design decisions:**
- The kernel's main job is to *classify* and *route* the incoming event
- Memory is usually minimal — the event itself carries most of the context
- Processes are usually tools (not sub-agents), because the work is well-defined

**Stack:** Claude API + Supabase + Vercel serverless function + webhook endpoint
**Trigger:** Webhook (external event), email arrival, form submission
**Outputs:** Database records, emails, Slack messages, API calls

---

## Pattern 3: Scheduled Worker OS

**What it is:** The OS wakes up on a timer, does a batch job, and goes back to sleep.

**Best for:**
- Daily briefings and digests
- Weekly report generators
- Monitoring and alerting systems
- Recurring research tasks (like App Flip Scout!)
- Cron-based automations

**Shape:**
```
Cron timer → Kernel wakes → Fetches data → Processes data → Generates output → Sends output → Sleeps
```

**Key design decisions:**
- No user input — the kernel must know its own task from the system prompt
- Long-term memory matters here — the OS often needs to compare today vs. last run
- The output delivery mechanism (email, Slack, file) is part of the I/O design

**Stack:** Claude API + Supabase + Vercel cron or Claude Code scheduled task
**Trigger:** Cron (daily, weekly, hourly, on the 1st and 15th, etc.)
**Outputs:** Emails, Slack messages, documents, database records

---

## Pattern 4: Multi-Agent Council OS

**What it is:** One orchestrator agent receives a complex task, breaks it into sub-tasks, dispatches specialized agents in parallel, then synthesizes their outputs.

**Best for:**
- Complex research and analysis tasks
- Systems where different domains need different expertise
- Tasks that are too big for one context window
- High-quality output that benefits from multiple perspectives (like the LLM Council skill!)

**Shape:**
```
Input → Orchestrator plans → Dispatches Agent A, Agent B, Agent C (parallel)
      ↓
Each agent uses its own tools
      ↓
Synthesizer agent reads all outputs → Final response
```

**Key design decisions:**
- The orchestrator's system prompt defines how to decompose tasks
- Each specialized agent has its own focused system prompt
- Memory shared across agents usually lives in the database, not individual context windows
- This pattern is more expensive (more LLM calls) — only use when complexity demands it

**Stack:** Claude API (multiple instances) + Supabase + task queue + Vercel
**Trigger:** User request or webhook
**Outputs:** Synthesized research reports, decisions, structured data

---

## Pattern 5: Hybrid OS (Most Common)

**What it is:** A combination of patterns — usually an always-on kernel with scheduled background workers and event-driven triggers.

**Example:** Adamma's AI business OS could be:
- Always-on assistant for ad-hoc queries
- Daily scheduled worker for morning briefing
- Event-driven pipeline that fires when a new student signs up
- Multi-agent council when doing deep research

**Shape:** Multiple patterns wired together through a shared database and kernel.

**Design principle:** Start with one pattern. Add patterns as the system grows. The shared database is the connective tissue — it's how the different patterns communicate.

---

## Choosing a Pattern — Quick Decision Tree

Ask the user these questions in order:

1. **Does a human trigger it each time?** → Always-On Assistant
2. **Does an external event trigger it?** → Event-Driven Pipeline
3. **Does time trigger it?** → Scheduled Worker
4. **Is the task too complex for one agent?** → Multi-Agent Council
5. **Is it some combination of the above?** → Hybrid OS

When in doubt, start with the simplest pattern that solves the problem. You can always add layers.

---

## Stack Reference by Pattern

| Pattern | Primary Language | Database | Deployment | Trigger |
|---------|-----------------|----------|------------|---------|
| Always-On Assistant | Python or TypeScript | Supabase/Neon | Vercel or Replit | HTTP API |
| Event-Driven Pipeline | Python or TypeScript | Supabase | Vercel serverless | Webhook |
| Scheduled Worker | Python | Supabase | Vercel cron / Claude Code scheduled task | Cron |
| Multi-Agent Council | Python | Supabase | Vercel | HTTP API or webhook |

All patterns use: Claude API (Anthropic SDK), MCP servers for integrations, CLAUDE.md for kernel memory.
