# Build Scenarios & Error Playbooks

Read the relevant section when an error or question comes in between build steps.
Organized by the layer where it typically occurs.

---

## Layer 1: Scaffold

**Problem: Claude Code generates a messy folder structure with random file names**
Fix: Re-run with a more explicit prompt. Add: "Use this exact folder structure: [paste structure]. Do not add any files not listed."

**Problem: Environment variables not loading**
Fix: Check that `.env.local` (not `.env`) exists and the variable names match exactly what the code reads. In Next.js, client-side vars need `NEXT_PUBLIC_` prefix. Server-side vars do not.

**Problem: "Module not found" errors immediately after scaffold**
Fix: Run `npm install` (or `pip install -r requirements.txt` for Python) from the project root. Claude Code sometimes generates the code before installing the deps.

---

## Layer 2: Kernel Core

**Problem: Kernel returns raw text instead of structured JSON**
Fix: Add to the system prompt: `"You must respond ONLY with valid JSON. No markdown, no explanation, no code blocks. Just the raw JSON object."` Then specify the exact schema you expect.

**Problem: Kernel "hallucinates" tool calls — calls tools that don't exist yet**
Fix: In the system prompt, list ONLY the tools that have been built so far. Add: `"You may only call tools from this list: [list]. Do not reference any other tools."`

**Problem: Kernel loop runs forever / hits token limits**
Fix: Add a max_turns or max_iterations counter. After N steps without resolution, the kernel should return a "stuck" state rather than looping. Add this to the kernel logic explicitly.

**Problem: CLAUDE.md not loading or kernel ignoring it**
Fix: Confirm the file path is correct and the read happens at startup, before the first LLM call. Log the loaded content to the console to verify it's being read.

---

## Layer 3: Memory / Database

**Problem: Supabase/Neon connection fails**
Fix: Check the `.env` file for the correct connection string. For Supabase, use the pooler URL (port 6543) for serverless/edge functions, the direct URL (port 5432) for persistent servers. Log the error message exactly — it usually says which env var is missing.

**Problem: Database schema migration fails**
Fix: Run migrations one at a time. If using Supabase CLI: `supabase db push`. If using raw SQL, run each statement separately and look for the first error.

**Problem: Vector similarity search returns garbage results**
Fix: Check that embeddings were generated with the same model used for queries (they must match). Also check the similarity threshold — start with 0.7 and adjust. Log the similarity scores to see what's actually coming back.

**Problem: Agent "forgets" things it was told earlier**
Fix: This is a context window issue, not a memory bug. The conversation history is being trimmed. Implement explicit memory: after each turn, save key facts to the database and retrieve relevant ones at the start of the next turn.

---

## Layer 4: Process Layer (Agents and Tools)

**Problem: Tool call fails silently — kernel thinks it succeeded but nothing happened**
Fix: Add explicit error handling to every tool. Return `{ success: false, error: "..." }` on failure. Teach the kernel to check `success` before continuing.

**Problem: Sub-agent produces low-quality output**
Fix: The sub-agent's system prompt is probably too vague. Add: specific output format, examples of good output, explicit constraints ("do not include X", "always include Y"). Quality comes from specificity.

**Problem: Parallel agents produce conflicting outputs**
Fix: This is normal — that's the point of the multi-agent council pattern. The synthesizer agent's job is to resolve conflicts. Give it an explicit instruction: "When agents disagree, use the reasoning that is most supported by evidence."

**Problem: MCP server not connecting**
Fix: Check that the MCP server is listed correctly in `claude_desktop_config.json` or the project's MCP config. Restart Claude Code after changing MCP config. Check the MCP server logs for auth errors.

---

## Layer 5: I/O System

**Problem: Webhook not firing**
Fix: Use a tool like ngrok (for local dev) or check the Vercel function logs. Confirm the receiving URL is correct and publicly accessible. Log every incoming request so you can see if events are arriving at all.

**Problem: Cron job not running**
Fix: Check the cron expression format (it varies by platform). Test by temporarily changing it to "every minute" (`* * * * *`) to confirm the wiring works, then change back.

**Problem: Scheduled task runs but does nothing**
Fix: The kernel probably lacks context — it woke up but doesn't know what to do. Add a "task intent" to the cron trigger: the cron should pass a task description when it wakes the kernel.

**Problem: Output (email/Slack message) sends but with wrong formatting**
Fix: Check what format the sending API expects. Slack uses Markdown-ish Block Kit. Email usually wants HTML or plain text. Log the raw payload you're sending before the API call to see exactly what's going out.

---

## Layer 6: Orchestration (Wiring It All Together)

**Problem: Kernel routes to wrong tool/agent**
Fix: Add logging at the routing step. Log what the kernel decided and why. Usually the issue is that the tool descriptions are too similar — make each tool's description more distinct.

**Problem: System works for simple inputs but fails on complex ones**
Fix: Add a planning step before execution. Teach the kernel to first output a plan (`{ steps: [...] }`) and then execute each step. This prevents the kernel from trying to do too much in one LLM call.

**Problem: The system is slow**
Fix: Identify which layer is the bottleneck by logging timestamps at each step. Usually it's LLM calls (use Haiku instead of Sonnet where reasoning isn't needed) or database queries (add indexes).

---

## Deployment

**Problem: Works locally, fails on Vercel**
Fix: Check environment variables are set in Vercel's project settings (not just `.env.local`). Check if the error is a timeout — Vercel serverless functions timeout at 10s (free) or 60s (pro). If it's a long-running task, move it to a background queue.

**Problem: Vercel deployment succeeds but the app crashes on load**
Fix: Check the Vercel function logs (not build logs — *runtime* logs). The error is usually a missing env var or a module that works in Node but not in the Edge Runtime.

**Problem: Claude Code deploys but the API key isn't working in production**
Fix: Make sure you're using the *production* Anthropic API key, not a test key. Also confirm the key has the right permissions/model access for what you're calling.

---

## Tone Guidance

When things break between steps, stay calm and specific:

✅ "No worries — this is a common one at the memory layer. Here's what to do: [fix]"
✅ "Can you paste the exact error message? That'll tell us exactly where it's stuck."
✅ "This usually means [X]. Try [fix] and let me know what you see."

❌ Don't diagnose before you have the error message
❌ Don't suggest multiple fixes at once — give one, wait, then give another if needed
❌ Don't say "I'm not sure" without offering a next step — always give a direction
