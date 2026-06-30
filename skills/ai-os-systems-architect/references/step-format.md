# Step Delivery Format

Use this template for every build step in Phase 2. Read this before delivering the first build step.

---

## The Template

```
---

## Step [N] — [Layer Name]

**What this is:** [2 sentences max — what this layer does and why it comes now in the build order]

**Your prompt for Claude Code:**

\```
[Complete, copy-pasteable prompt. Nothing abbreviated. No "add your X here" placeholders — be specific based on the user's Architecture Brief.]
\```

**Verification checklist:**
- [ ] [Specific thing to confirm is working]
- [ ] [Another specific check]
- [ ] [One more if needed]

**💡 Tip:** [One common gotcha at this specific layer and how to handle it]

Type `done` when this step is verified and working. ✅

---
```

---

## Worked Example — Step: Kernel Core

```
---

## Step 2 — Kernel Core

**What this is:** The kernel is the brain of your AI OS. It reads inputs, decides what to do, and coordinates your tools and agents. This step wires up the main agent loop — the thing that runs every time your OS is triggered.

**Your prompt for Claude Code:**

\```
Build the core orchestration system for my AI research assistant. 

Create a main agent function called `run_kernel` that:
1. Accepts a user input string
2. Loads context from CLAUDE.md (the system memory)
3. Calls Claude claude-sonnet-4-6 with the system prompt + user input
4. Parses the response to determine which tool to call next
5. Returns a structured response: { action, reasoning, output }

Use the Anthropic Python SDK. Store the system prompt in a `system_prompt.txt` file that the kernel loads on each run.

Also create a CLAUDE.md file with this initial content:
- Project: [their project name]
- Purpose: [their OS purpose from the Architecture Brief]  
- Memory: [note their memory sources]
- Available tools: [list from their Process Registry]
\```

**Verification checklist:**
- [ ] `run_kernel("test input")` runs without errors
- [ ] Response includes `action`, `reasoning`, and `output` fields
- [ ] CLAUDE.md exists and loads correctly
- [ ] Logs show the full kernel response in the console

**💡 Tip:** If the kernel returns unstructured text instead of JSON, add "Respond ONLY in valid JSON format" to the system prompt and specify the exact shape you want back.

Type `done` when this step is verified and working. ✅

---
```

---

## Notes on Writing Good Prompts

When generating the Claude Code prompt for each step, follow these principles:

**Be specific to their system.** Use the actual names, models, and technologies from their Architecture Brief. Never write generic placeholders — pull in their real details.

**One step does one thing.** Each prompt builds exactly one layer. Don't bundle the database schema AND the kernel loop into one step. The user needs to verify each piece before moving on.

**Name the files.** Always specify what files to create and what to name them. Vague instructions ("create a utility file") lead to inconsistent structure.

**Include the verification targets.** Think ahead to what the user will check — write the prompt so those things are definitely produced and testable.

**Layer order matters.** Always scaffold before kernel, kernel before memory, memory before processes, processes before orchestration. A sub-agent cannot call a tool that hasn't been built yet.

---

## Adjusting for Replit vs. Claude Code

The prompt format is the same. The only difference is the framing line at the top:

- **Claude Code:** "Your prompt for Claude Code:"
- **Replit:** "Your prompt for Replit Agent:"

Everything else stays identical.
