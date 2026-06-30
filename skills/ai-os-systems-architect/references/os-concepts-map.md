# OS Concepts Map: Traditional OS → AI OS

Use this to introduce the AI OS analogy to users in Step D1 and D2.
The goal is to make systems-level thinking feel familiar, not foreign.

---

## The Core Analogy

A traditional operating system manages hardware resources so programs can run.
An AI OS manages intelligence resources so agents can act.

The layers map directly:

| Traditional OS | AI OS Equivalent | Plain Meaning |
|----------------|------------------|---------------|
| Kernel | Core Orchestrator (LLM + system prompt) | The brain that reads inputs, decides what to do, and coordinates everything else |
| RAM (working memory) | System prompt + CLAUDE.md | What the kernel always knows right now |
| Hard drive (storage) | Database (Supabase, Neon) | What the system remembers permanently |
| Processes | Agents + Tools | The individual jobs the OS runs |
| System calls | Tool calls / MCP calls | How agents ask the OS for resources |
| Interrupts | Webhooks / triggers | External events that tell the OS to wake up and act |
| Shell | User interface / API endpoint | How humans interact with the OS |
| Scheduler | Orchestration logic / cron | Who runs next, when, and in what order |
| File system | Document store / vector DB | Where the OS stores and retrieves structured information |
| Device drivers | MCP servers | Standardized connectors to external hardware (apps) |
| Bootloader | Initialization prompt / CLAUDE.md | The first thing that runs and sets up the system state |

---

## Memory Tiers (Detailed)

Traditional computers have a memory hierarchy. So do AI OS systems.

| Memory Type | Traditional | AI OS | Technology |
|-------------|-------------|-------|------------|
| Registers | Fastest, smallest | Token window (right now) | LLM context window |
| L1/L2 Cache | Very fast, small | Active system prompt | CLAUDE.md, pre-loaded context |
| RAM | Fast, medium | Session memory | Thread history, in-memory state |
| SSD/HDD | Slower, large | Persistent memory | Supabase, Neon, SQLite |
| Cold storage | Archival | Semantic search | pgvector, Pinecone, embeddings |

**Key insight:** The context window is like RAM — it's fast and powerful but limited. When a task requires more than fits in the window, you need to pull from "disk" (the database). Designing the memory tier means deciding what stays in RAM vs. what gets retrieved on demand.

---

## Process Types

In a traditional OS, processes are programs. In an AI OS, processes are agents and tools.

| Process Type | Traditional | AI OS | When to Use |
|--------------|-------------|-------|-------------|
| Foreground process | App the user is using | Main agent handling a request | Real-time user interaction |
| Background process | Daemon / service | Scheduled agent | Cron jobs, monitoring, daily digests |
| Child process | Spawned subprocess | Sub-agent | When the main agent delegates a specific task |
| System call | Kernel API request | Tool call | When an agent needs data or needs to take action |
| Driver | Hardware interface | MCP server | Standardized connection to an external app (Slack, Gmail, Supabase) |

---

## I/O System

| Traditional | AI OS | Example |
|-------------|-------|---------|
| Keyboard input | User message / form submit | User types a request |
| Hardware interrupt | Webhook | A new email arrives, a form is submitted |
| Timer interrupt | Cron job | Run every morning at 8am |
| Screen output | Chat response / UI update | Agent writes back |
| File write | Database write | Agent saves a result |
| Network packet | API call | Agent calls an external service |
| Printer | Email / Slack message | Agent sends a formatted output |

---

## Architecture Patterns (Quick Reference)

These are common AI OS shapes. Full details in `build-patterns.md`.

**Always-On Assistant** — Kernel waits for user input, responds, then waits again. Like a shell.
- Shape: Input → Kernel → Tools → Output → Wait

**Event-Driven Pipeline** — Kernel sleeps until triggered, then runs a workflow.
- Shape: Trigger → Kernel → Process A → Process B → Output

**Scheduled Worker** — Kernel wakes on a timer, does a job, goes back to sleep.
- Shape: Cron → Kernel → Tools → Output → Sleep

**Multi-Agent Council** — Multiple specialized agents, one orchestrator coordinates them.
- Shape: Input → Orchestrator → [Agent A, Agent B, Agent C in parallel] → Synthesizer → Output

---

## How to Introduce This to the User

In Step D1, after collecting their answers, say something like:

*"Before we design your system, here's a useful frame: your AI OS works exactly like a traditional operating system — just for intelligence instead of hardware. Let me show you how your system maps to it..."*

Then tailor the table to their specific use case. If they're building a research pipeline, show them the pipeline pattern. If it's an always-on assistant, show that pattern. Make it concrete to them, not abstract.
