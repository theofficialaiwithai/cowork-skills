# Path A — No-Code Build Steps (Zapier)

Step-by-step guide for building a Slack-native AI agent using Zapier + Claude API. No deployment required.

---

## Before You Start

Confirm the user has:
- A Slack workspace where they can install apps
- A Zapier account (free tier works for testing)
- An Anthropic API key

---

## Step 1: Create the Slack App

1. Go to https://api.slack.com/apps
2. Click **Create New App** → **From scratch**
3. Name the app (use the agent name)
4. Select the Slack workspace
5. Go to **OAuth & Permissions** → add these Bot Token Scopes:
   - `chat:write`
   - `channels:history`
   - `channels:read`
   - `app_mentions:read`
6. Click **Install to Workspace** → copy the **Bot User OAuth Token** (starts with `xoxb-`)
7. Go to **Basic Information** → copy the **Signing Secret**

**Prompt to give user:**
> "Go to api.slack.com/apps and create a new app from scratch. Name it [Agent Name]. Install it to your workspace and copy the Bot User OAuth Token and Signing Secret. Paste them somewhere safe — we'll need them in Step 3."

---

## Step 2: Invite the Bot to the Channel

1. Open Slack
2. Go to the channel where the agent will live (or create a new one)
3. Type `/invite @[agent-name]`
4. The bot is now a member of the channel

---

## Step 3: Create the Zap in Zapier

1. Go to zapier.com → **Create Zap**

**Trigger:**
- App: Slack
- Event: **New Message Posted to Channel**
- Account: Connect your Slack workspace
- Channel: Select the agent's channel
- Turn off "Trigger for Bot Messages" (prevents infinite loops)

**Action 1 — Call Claude API:**
- App: **Webhooks by Zapier**
- Event: **POST**
- URL: `https://api.anthropic.com/v1/messages`
- Headers:
  - `x-api-key`: [Your Anthropic API key]
  - `anthropic-version`: `2023-06-01`
  - `content-type`: `application/json`
- Body (raw JSON):
```json
{
  "model": "claude-sonnet-4-6",
  "max_tokens": 1024,
  "system": "[PASTE SYSTEM PROMPT HERE]",
  "messages": [
    {
      "role": "user",
      "content": "{{1. Text}}"
    }
  ]
}
```
(The `{{1. Text}}` pulls the Slack message text from the trigger step)

**Action 2 — Post Response to Slack:**
- App: Slack
- Event: **Send Channel Message**
- Channel: Same channel as trigger
- Message Text: Parse the Claude response — use Zapier's data mapper to extract `content[0].text` from the webhook response body
- Thread: Use `{{1. ts}}` to reply in the same thread as the original message

---

## Step 4: Write the System Prompt

This is the most important step. The system prompt defines the agent's entire personality and capability.

Template:
```
You are [Agent Name], a [one sentence description of the agent's role].

You live in the [#channel-name] Slack channel and respond to messages from [audience].

Your core job: [What the agent does in one sentence]

Your personality: [Tone — warm and direct / professional / etc.]

Guidelines:
- Keep responses concise and well-formatted for Slack (use bullet points, not walls of text)
- If you don't know something, say so — don't guess
- [Any domain-specific rules]

[Any additional context the agent needs about the user or their situation]
```

---

## Step 5: Test

1. Send a message in the Slack channel
2. Check Zapier's task history — did it trigger?
3. Did Claude respond?
4. Did the response appear in Slack?

Common issues:
- **Infinite loop:** The bot is responding to its own messages. Turn off "Trigger for Bot Messages" in the Zapier trigger.
- **No response:** Check the Anthropic API key header in the Webhooks step.
- **Wrong channel:** Make sure the Zap trigger channel matches where you're testing.

---

## Step 6: Add Memory (Optional)

If the agent needs to remember context across messages:

1. Add an Airtable base with a table: `Conversations`
   - Fields: `channel_id`, `thread_ts`, `history` (Long Text), `updated_at`

2. Before calling Claude (new Action 1):
   - App: Airtable
   - Event: **Find Record**
   - Search by `thread_ts` matching `{{1. Thread Timestamp}}`

3. Update the Claude API call to include history:
```json
{
  "model": "claude-sonnet-4-6",
  "max_tokens": 1024,
  "system": "[System prompt]",
  "messages": [AIRTABLE_HISTORY_FIELD, {"role": "user", "content": "{{1. Text}}"}]
}
```

4. After Claude responds (new final Action):
   - App: Airtable
   - Event: **Update Record** (or Create if not found)
   - Write updated conversation history back

Note: This gets complex fast. If memory is important, switch to Path B.
