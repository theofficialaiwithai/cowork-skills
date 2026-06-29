# Claude Code Implementation Guide

This file contains the technical details for building routines in Claude Code. Reference it during Phase 2 (when designing for Claude Code) and Phase 3 (when building).

---

## The Four Mechanisms

Claude Code has four ways to implement a routine. Choose based on how the routine starts and how complex it is.

---

## 1. Skills — On-Demand Structured Workflows

**Use when:** The routine is multi-step, needs to be invoked by name, or should auto-trigger when the user describes what they want.

**File locations:**
- User-level (works in any Claude Code session): `~/.claude/skills/<skill-name>/SKILL.md`
- Project-level (only in a specific project): `.claude/skills/<skill-name>/SKILL.md`

**When to use user-level vs. project-level:**
- User-level: routines that the person will use across multiple projects (morning briefing, meeting prep, weekly review)
- Project-level: routines specific to one codebase or workflow (run tests, deploy to staging, generate release notes)

**File format — SKILL.md:**
```yaml
---
name: Brief name of what this skill does
description: "When Claude should use this. Include trigger keywords the user would say — this is how Claude knows to auto-invoke it. Example: 'Use when the user says morning briefing, daily digest, or wants a summary of their emails and calendar.'"
---

# Skill Name

[Instructions Claude follows when this skill is active. Write in clear steps.]

## Step 1: [First action]
[What to do, what tool to use]

## Step 2: [Second action]
[What to do, what tool to use]
```

**YAML frontmatter fields:**
- `name` — Short label, shown in the skill list
- `description` — The primary triggering mechanism. Be specific about when to use it. Include keywords.
- `disable-model-invocation: true` — Optional. Set this if you only want `/skill-name` to trigger it (prevents auto-invocation)
- `allowed-tools` — Optional. Restrict which tools Claude can use (e.g., `["Bash", "Read"]`)
- `context: "fork"` — Optional. Run the skill in a subagent with isolated state (good for long or complex routines)

**Invocation:**
- Auto: Claude detects the trigger keywords in the user's prompt and invokes automatically
- Manual: User types `/skill-name` in Claude Code

**Example — morning briefing skill:**
```yaml
---
name: Morning Briefing
description: "Pulls unread emails and today's calendar events and delivers a morning summary. Use when the user says 'morning briefing', 'daily digest', 'what do I have today', or wants a morning summary."
---

# Morning Briefing

Pull unread emails using the Gmail MCP and today's calendar events using the Google Calendar MCP, then format a clean summary.

## Step 1: Pull unread emails
Use Gmail MCP search_threads with query "is:unread". Get up to 10 threads. For each: sender, subject, one-line snippet.

## Step 2: Pull today's calendar
Use Google Calendar MCP list_events for today's date range. Get title, start time, end time, and any meeting link.

## Step 3: Format and deliver
Output a two-section summary: **Unread Emails** and **Today's Schedule**. Keep it scannable.
```

---

## 2. Slash Commands — Simple One-Shot Prompts

**Use when:** The routine is a single prompt the user wants to run quickly, with no complex workflow needed.

**File locations:**
- User-level: `~/.claude/commands/<command-name>.md`
- Project-level: `.claude/commands/<command-name>.md`

**File format:**
Just a markdown file. The content is the prompt Claude runs when the command is invoked. No YAML frontmatter required (though it can be included).

```markdown
Review the last 5 git commits and summarize what changed and why. 
Flag anything that looks risky or incomplete.
```

**Invocation:** User types `/<command-name>` in Claude Code.

**When to use Skills vs Slash Commands:**
- Slash command: user wants a quick prompt shortcut, one-liner, no workflow
- Skill: routine has multiple steps, should auto-trigger based on description, or needs supporting reference files

---

## 3. Scheduled Tasks — Automated Time-Based Routines

**Use when:** The routine should run automatically on a schedule, without the user having to do anything.

**How to set it up:**
Run this command in the terminal from the project directory (or any directory for user-level tasks):

```bash
claude trigger create --interval "CRON_EXPRESSION" --prompt "PROMPT_TEXT"
```

**Common cron expressions:**
```
"0 8 * * 1-5"    Every weekday at 8:00 AM
"0 9 * * 1"      Every Monday at 9:00 AM
"0 17 * * 5"     Every Friday at 5:00 PM
"0 8 * * *"      Every day at 8:00 AM
"0 9 1 * *"      First of every month at 9:00 AM
"0 */4 * * *"    Every 4 hours
```

**The prompt must be self-contained.** It runs without any conversation context, so it needs to include all instructions inline:

```bash
claude trigger create \
  --interval "0 9 * * 1" \
  --prompt "Run my Weekly Priorities routine:
1. Use the Notion MCP to fetch all open tasks from my task database (filter: status is not done).
2. Select the top 3 priorities based on: due date urgency, business impact, and whether the task unblocks other work. Write one sentence of rationale for each.
3. Use the docx skill to create a Word doc titled 'Weekly Priorities — [today's date]' with the top 3 priorities and the full task list.
4. Save to /Users/[username]/Documents/Weekly Priorities/
5. Confirm completion in chat with the 3 priority names and total task count."
```

**Desktop vs Cloud tasks:**
- Desktop tasks run on the user's machine — their computer must be on at the scheduled time
- Cloud tasks run on Anthropic infrastructure — always-on, no machine required
Both use the same `claude trigger create` command. Cloud tasks are the default when Claude Code is connected to Anthropic's cloud.

**Verifying a scheduled task:**
```bash
claude trigger list    # shows all active triggers
claude trigger delete <id>   # removes a trigger
```

**Providing instructions when Claude can't run the command directly:**
If the skill can't run terminal commands in the user's environment, show the command in a code block with a clear explanation:

```
Run this in your terminal:

claude trigger create --interval "0 9 * * 1" --prompt "..."

This schedules your routine every Monday at 9:00 AM.
After running it, type `claude trigger list` to confirm it was registered.
```

---

## 4. Hooks — Event-Triggered Routines

**Use when:** The routine should fire automatically when something specific happens — a tool runs, a session starts, the user submits a prompt.

**File location:**
- User-level: `~/.claude/settings.json`
- Project-level: `.claude/settings.json`

**Hook event types:**

| Event | When it fires |
|---|---|
| `SessionStart` | At the beginning of every Claude Code session |
| `SessionEnd` | When the session ends |
| `UserPromptSubmit` | Every time the user submits a message |
| `PreToolUse` | Before Claude runs any tool (can block it) |
| `PostToolUse` | After a tool completes successfully |
| `Stop` | When the user stops the session |

**Settings.json format:**
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matchers": ["Write", "Edit"],
        "handlers": [
          {
            "type": "shell",
            "command": "echo 'File saved' >> ~/claude-activity.log"
          }
        ]
      }
    ],
    "SessionStart": [
      {
        "matchers": [],
        "handlers": [
          {
            "type": "shell",
            "command": "/Users/username/.claude/hooks/session-start.sh"
          }
        ]
      }
    ]
  }
}
```

**Matchers:** A string using `|` to match tool names. Empty array `[]` means "apply to all events of this type."

**Handler types:**

Shell command:
```json
{
  "type": "shell",
  "command": "/path/to/script.sh",
  "timeout": 30
}
```

HTTP POST (sends event data to an API or webhook):
```json
{
  "type": "http",
  "url": "https://your-webhook-url.com",
  "timeout": 30,
  "headers": {
    "Authorization": "Bearer your-token"
  }
}
```

**Blocking a tool (PreToolUse only):**
A shell handler can block Claude from running a tool by exiting with code 1 and printing a reason:
```bash
#!/bin/bash
# Read the event JSON from stdin
input=$(cat)
echo "This tool is blocked in this project" >&2
exit 1
```

**Adding a hook to settings.json — if file access is available:**
Read the current `.claude/settings.json`, add the hooks entry, and write it back. If the file doesn't exist, create it.

**If file access is not available:**
Show the user the exact JSON snippet to add, with instructions:
```
Add this to your `.claude/settings.json` file 
(create the file if it doesn't exist):

{
  "hooks": {
    ...
  }
}
```

---

## Choosing the Right Mechanism — Quick Guide

**The routine should run automatically on a schedule**
→ Scheduled Task (`claude trigger create`)

**The routine runs when the user asks for it or types a command**
→ Skill (multi-step) or Slash Command (simple one-liner)

**The routine fires when Claude takes a specific action (like writing a file)**
→ Hook (`PostToolUse` or `PreToolUse`)

**The routine fires at the start of every session**
→ Hook (`SessionStart`)

**The routine needs access to external tools like Gmail or Notion**
→ All mechanisms support MCP tools — but the user needs those MCPs configured in their Claude Code project first

---

## Important Notes

**MCPs in Claude Code:** MCP connections in Claude Code are configured separately from Cowork. The user may need to set up their MCPs in Claude Code before the routine can use them. If a routine requires Gmail, Notion, or another MCP, remind the user to check that their MCP is configured in Claude Code.

**Skills hot-reload:** Changes to skill files take effect immediately in the current session — no restart needed.

**Cron times are in UTC by default** for cloud tasks. For desktop tasks, they follow the machine's local time. When specifying a schedule, ask the user their timezone and convert accordingly.
