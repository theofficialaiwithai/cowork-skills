# Cowork Skills

A collection of Claude skills for vibe coders, non-technical builders, and anyone using Claude to build, automate, and ship things — without needing to be a developer.

These skills are designed to be opinionated, structured, and neurodivergent-friendly. Every skill works one step at a time, asks one question at a time, and never leaves you guessing what to do next.

---

## Skills

### 🤖 [automation-architect](./skills/automation-architect)
**Full Agent Builder OS** — takes you from a vague idea to a production-ready automation system in six structured phases. Covers idea clarification, system design, tool selection (Zapier, Make, n8n, Gumloop, Lindy, Claude API, Openclaw), workflow mapping, step-by-step implementation, and optimization. Generates a formatted `.docx` spec at the end.

Best for: "I want to automate something but don't know where to start."

---

### 🏗️ [code-build-copilot](./skills/code-build-copilot)
**Step-by-step Claude Code co-pilot** — reads your PRD or feature list and walks you through the build one step at a time. Each step includes the exact prompt to paste into Claude Code, a verification checklist, and calm, knowledgeable support when things break. Never advances until you type `done`.

Best for: "I have a PRD — now help me actually build it."

---

### 📋 [prd-assistant](./skills/prd-assistant)
**PRD generator + build coach** — turns a raw app idea into a complete, opinionated, build-ready Product Requirements Document, then coaches you through the build step by step. Covers discovery, problem framing, tech stack, data schema, app routes, build order with pasteable prompts, and launch plan.

Best for: "I have an idea for an app. Help me plan it and build it."

---

### 🔁 [routines-creator](./skills/routines-creator)
**Build automated routines** — helps you go from "I want to automate X" (or even "I don't know what to automate") to a working routine. Covers scheduled routines, event-triggered routines, and on-demand routines. Includes a 5-question recommender if you're not sure where to start.

Best for: "I keep doing this manually every week. Can Claude just handle it?"

---

### 🔌 [mcp-assistant](./skills/mcp-assistant)
**MCP integration guide** — expert, step-by-step guidance for connecting Claude to external tools and data using the Model Context Protocol. Covers connecting to pre-built servers (GitHub, Notion, Supabase, Google Drive, etc.), building custom MCP servers in Python or TypeScript, auth, and debugging.

Best for: "I want my AI app to access [external service]. How do I connect it?"

---

### 🌐 [openclaw-assistant](./skills/openclaw-assistant)
**Openclaw gateway guide** — expert guidance for adding multi-channel messaging and automation to your AI app using Openclaw. Covers installation, channel setup (Telegram, Discord, Slack, WhatsApp), cron jobs, hooks, multi-agent routing, and integration with Vercel/Clerk/Neon stacks.

Best for: "I want users to be able to message my AI from Telegram/Slack/WhatsApp."

---

## How to Use These Skills

### Option 1: Claude Cowork (Recommended)
If you're using Claude in Cowork mode, you can install these as a plugin. Skills activate automatically when you describe what you want — no slash commands needed.

### Option 2: Claude Code
Clone this repo and add the skills directory to your Claude Code setup:

```bash
git clone https://github.com/YOUR_USERNAME/cowork-skills.git
```

Then reference skill files directly in your Claude Code sessions, or add them to your `.claude/skills/` directory.

### Option 3: Copy & Paste
Each `SKILL.md` file is a self-contained prompt. You can copy the content of any `SKILL.md` and paste it as a system prompt in any Claude interface.

---

## Skill Structure

Each skill follows this folder structure:

```
skills/
  skill-name/
    SKILL.md              # The main skill prompt — start here
    references/           # Supporting reference docs the skill reads at runtime
      *.md
    scripts/              # Optional helper scripts
      *.py
```

The `SKILL.md` file contains the skill's description (used for auto-triggering) and its full instructions. Reference files are loaded by the skill when needed — they contain matrices, templates, playbooks, and other structured content that would bloat the main prompt if included inline.

---

## Design Principles

**One thing at a time.** Every skill asks one question, delivers one step, and waits. This is intentional — it reduces cognitive load and prevents overwhelm.

**No jargon without explanation.** Every technical term is defined the first time it appears.

**Calm when things break.** Skills are written to start with the fix, not the diagnosis. "No worries — this is common. Here's what to do."

**Structured outputs.** Every phase ends with a locked summary so you always know where you are and what's been decided.

**Built for vibe coders.** These skills assume you're capable and motivated, not that you're a developer. They give you the exact words to use, the exact commands to run, and the exact things to look for — without requiring you to understand the underlying infrastructure.

---

## Contributing

Found a bug, have an improvement, or want to add a skill? PRs are welcome.

For new skills, follow the structure above: a `SKILL.md` with a YAML frontmatter `description` block, and reference files in a `references/` subdirectory if needed.

---

## License

MIT — free to use, fork, and build on.
