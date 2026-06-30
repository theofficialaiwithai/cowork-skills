# Build Paths — Slack Agent Technical Reference

Two paths for building Slack-native AI agents. This file contains the technical details for making the right recommendation and guiding the build.

---

## Path A — No-Code (Zapier or Make)

### When to use
- Personal workflow agents only
- Testing a concept before committing to a full build
- No memory needed beyond a single session
- Target: Adamma herself, not her app users

### How it works
1. A message is sent in a Slack channel
2. Zapier/Make detects it via a Slack trigger
3. The automation calls the Claude API with the message + a system prompt
4. Claude's response is posted back to Slack via a Slack action

### Zapier Setup (simpler)
- Trigger: "New Message Posted to Channel" (Slack app)
- Action 1: "Send Message" to Claude API via Webhooks by Zapier (POST to `https://api.anthropic.com/v1/messages`)
- Action 2: "Send Channel Message" (Slack app) — post Claude's response to the thread

### Make Setup (more control)
- Trigger: Slack "Watch Messages" module
- Module 2: HTTP "Make a Request" → Claude API
- Module 3: Slack "Create a Message" → post response

### Key limitation
Slack sends events to a webhook URL. Zapier and Make both provide webhook URLs, but they are not true persistent connections — each message is treated as a new, stateless event. Memory requires manually storing and retrieving context from an external source (Airtable, Notion, or Google Sheets) on every call.

### Memory for Path A (if needed)
- Store conversation history in Airtable (channel_id + thread_ts as keys)
- On each new message: retrieve history from Airtable, append new message, send full history to Claude, store Claude's response back to Airtable
- This works but adds latency and complexity — if memory matters, switch to Path B

---

## Path B — Full-Code (Bolt for JS + Vercel + Neon) ⭐ RECOMMENDED

### When to use
- Any agent meant for app users
- Any agent that needs real memory across conversations
- Anything that will be productized or taught to others
- Any agent that needs to take actions (query a database, call an API, read Gmail)

### The Stack
| Component | Tool | Why |
|---|---|---|
| Framework | Slack Bolt for JavaScript | Official Slack SDK, supports streaming, tool calling, all event types |
| Deployment | Vercel | Already in her stack, handles Slack's 3-second response requirement via Fluid Compute |
| Language | TypeScript / Next.js | Her Claude Code workflow, compatible with Vercel |
| AI | Claude API via Anthropic SDK | Her primary AI |
| Memory | Neon (serverless Postgres) | Her primary database, agent-ready, published Neon + Slack guide |
| Local testing | ngrok | Tunnels localhost to a public URL for Slack webhook verification |

### The Vercel Slack Agent Skill
This is the fastest path into a full-code build. Install it directly in Claude Code:

```bash
npx skills add vercel-labs/slack-agent-skill
```

Then in Claude Code:
```
/slack-agent new
```

The wizard guides through:
1. Framework selection (choose Bolt for JavaScript)
2. Implementation plan generation — describe the agent, review the plan
3. Project scaffolding — all files created automatically
4. Slack app creation with manifest
5. Environment variable setup
6. Local testing with ngrok
7. Production deployment to Vercel

### Slack App Manifest (base template)
```json
{
  "display_information": {
    "name": "[Agent Name]",
    "description": "[One sentence description]"
  },
  "features": {
    "bot_user": {
      "display_name": "[Agent Name]",
      "always_online": true
    }
  },
  "oauth_config": {
    "scopes": {
      "bot": [
        "app_mentions:read",
        "channels:history",
        "channels:read",
        "chat:write",
        "im:history",
        "im:read",
        "im:write"
      ]
    }
  },
  "settings": {
    "event_subscriptions": {
      "request_url": "https://your-domain.vercel.app/api/slack/events",
      "bot_events": [
        "app_mention",
        "message.channels",
        "message.im"
      ]
    },
    "socket_mode_enabled": false,
    "token_rotation_enabled": false
  }
}
```

### Required Environment Variables
```
SLACK_BOT_TOKEN=xoxb-...         # From Slack App > OAuth & Permissions
SLACK_SIGNING_SECRET=...          # From Slack App > Basic Information
ANTHROPIC_API_KEY=sk-ant-...      # From Anthropic Console
NEON_DATABASE_URL=postgresql://...  # From Neon dashboard
```

### Neon Memory Schema
Run this migration to set up conversation memory:

```sql
CREATE TABLE IF NOT EXISTS slack_conversations (
  id SERIAL PRIMARY KEY,
  channel_id TEXT NOT NULL,
  thread_ts TEXT NOT NULL,
  role TEXT NOT NULL CHECK (role IN ('user', 'assistant')),
  content TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_slack_conversations_thread
  ON slack_conversations(channel_id, thread_ts);

-- Optional: for agent-specific data
CREATE TABLE IF NOT EXISTS slack_agent_context (
  id SERIAL PRIMARY KEY,
  channel_id TEXT NOT NULL,
  key TEXT NOT NULL,
  value JSONB NOT NULL,
  updated_at TIMESTAMPTZ DEFAULT NOW(),
  UNIQUE(channel_id, key)
);
```

### Core Bot Logic Pattern (lib/bot.ts)
```typescript
import Anthropic from "@anthropic-ai/sdk";
import { neon } from "@neondatabase/serverless";

const anthropic = new Anthropic();
const sql = neon(process.env.NEON_DATABASE_URL!);

export async function handleMessage(
  channelId: string,
  threadTs: string,
  userMessage: string,
  systemPrompt: string
) {
  // 1. Load conversation history from Neon
  const history = await sql`
    SELECT role, content FROM slack_conversations
    WHERE channel_id = ${channelId} AND thread_ts = ${threadTs}
    ORDER BY created_at ASC
  `;

  // 2. Build messages array
  const messages = [
    ...history.map(row => ({
      role: row.role as "user" | "assistant",
      content: row.content
    })),
    { role: "user" as const, content: userMessage }
  ];

  // 3. Call Claude
  const response = await anthropic.messages.create({
    model: "claude-sonnet-4-6",
    max_tokens: 1024,
    system: systemPrompt,
    messages
  });

  const assistantMessage =
    response.content[0].type === "text"
      ? response.content[0].text
      : "";

  // 4. Save both messages to Neon
  await sql`
    INSERT INTO slack_conversations (channel_id, thread_ts, role, content)
    VALUES
      (${channelId}, ${threadTs}, 'user', ${userMessage}),
      (${channelId}, ${threadTs}, 'assistant', ${assistantMessage})
  `;

  return assistantMessage;
}
```

### Vercel Configuration (vercel.json)
```json
{
  "functions": {
    "api/slack/events.ts": {
      "maxDuration": 30
    }
  }
}
```

The `maxDuration: 30` gives Slack agents time to think and respond without Vercel's default 10-second function timeout cutting them off.

### Critical Slack Gotcha: The 3-Second Rule
Slack requires a 200 OK response within 3 seconds or it retries the event. For agents that take longer to respond, the pattern is:
1. Immediately acknowledge the event with 200 OK
2. Use Vercel's `waitUntil` to process and respond in the background

The Vercel Slack Bolt adapter handles this automatically — don't try to build this yourself.

### Local Testing with ngrok
```bash
# Install ngrok
brew install ngrok

# Start your dev server
npm run dev

# In another terminal, tunnel to Slack
ngrok http 3000

# Copy the https://xxx.ngrok.io URL
# Paste into Slack App > Event Subscriptions > Request URL
# (append /api/slack/events)
```

---

## Comparison Table

| | Path A (No-Code) | Path B (Full-Code) |
|---|---|---|
| Time to live | Same day | 1–2 days |
| Memory | Manual/limited | Full Neon Postgres |
| Suitable for users | No | Yes |
| Teachable/productizable | Limited | Yes — full lesson |
| Scales | No | Yes |
| Claude Code compatible | Yes (for config) | Yes (primary tool) |
| Adamma's real stack | Partial | Full match |
