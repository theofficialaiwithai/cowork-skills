# Enhancement Patterns — Upgrading Existing Apps

Five agentic patterns, each framed as an upgrade path for an app that's already live. Use this during Phase 3 to design specific enhancements for confirmed gaps.

---

## Pattern 1: Webhook — Add Event Response

**What it fixes:** An app that collects data or receives submissions but doesn't react automatically.

**The upgrade:** Add an API route that receives a POST request when something happens, validates it, and triggers downstream actions.

**How to add it to an existing Next.js app:**
```
/app/api/webhooks/[service]/route.ts
```
1. Register the webhook URL in the external service (Stripe, Typeform, Calendly, etc.)
2. Validate the incoming request signature (every major service provides this)
3. Parse the payload and trigger the action (database write, email, Claude API call, etc.)
4. Return `200 OK` immediately — do async work after responding

**Supabase database triggers (no external service needed):**
- Enable Supabase webhooks on any table
- Fires automatically on INSERT, UPDATE, or DELETE
- Calls your API route with the changed row data
- Perfect for: "when a new row is added, do X"

**Common impact:** High — turns a passive data collector into a responsive system.
**Common effort:** Low to Medium — a single API route + external service config.

**Architecture template:**
```
[External event] → POST /api/webhooks/[service] → Validate → Parse → Action
```

---

## Pattern 2: Cron — Add Scheduled Automation

**What it fixes:** Tasks the user does manually on a recurring schedule — checking data, sending reports, syncing, reviewing.

**The upgrade:** Add Vercel Cron Jobs that call API routes on a schedule, doing the recurring work automatically.

**How to add it to an existing Next.js + Vercel app:**

1. Add cron config to `vercel.json`:
```json
{
  "crons": [
    {
      "path": "/api/cron/daily-digest",
      "schedule": "0 8 * * *"
    }
  ]
}
```

2. Create the API route:
```
/app/api/cron/daily-digest/route.ts
```

3. Protect the route from unauthorized calls:
```typescript
if (request.headers.get('authorization') !== `Bearer ${process.env.CRON_SECRET}`) {
  return new Response('Unauthorized', { status: 401 });
}
```

**Common cron schedules:**
| Schedule | Cron Expression |
|---|---|
| Daily at 8am | `0 8 * * *` |
| Weekly Monday 8am | `0 8 * * 1` |
| Every hour | `0 * * * *` |
| Nightly midnight | `0 0 * * *` |
| Every 15 minutes | `*/15 * * * *` |

**Common impact:** High — eliminates entire categories of manual work.
**Common effort:** Low — mostly config + a single API route.

**Architecture template:**
```
Schedule fires → GET/POST /api/cron/[job-name] → Query DB → Process → Output
```

---

## Pattern 3: MCP — Add External Connectivity

**What it fixes:** An app that's an island — doesn't read from or write to the tools the user actually works in.

**The upgrade:** Connect Claude (or the app's AI layer) to external tools via MCP servers, or add direct API integrations for data sync.

**Two approaches:**

**A. Pre-built MCP servers (fastest):**
Available for: Supabase, Notion, GitHub, Slack, Google Calendar, Google Drive, Postgres, Filesystem

Add to `claude_desktop_config.json` or wire into the app's Claude API calls via the MCP client SDK.

**B. Direct API integration (for non-MCP services):**
Call the external service's API directly from your webhook or cron handler. Store credentials in Vercel environment variables.

**Common integrations to add:**
| Gap | Integration |
|---|---|
| No Slack notifications | Slack Incoming Webhooks (free, instant) |
| No email delivery | Resend API (simple, developer-friendly) |
| Data not in Notion | Notion API → create/update pages |
| No CRM sync | HubSpot / Airtable API |
| No calendar awareness | Google Calendar API |

**Common impact:** Medium to High — depends on how central the external tool is to the user's workflow.
**Common effort:** Low (MCP) to Medium (custom API integration).

**Architecture template:**
```
Trigger → MCP call / API call → External tool read/write → Response → Next action
```

---

## Pattern 4: Automation — Add Multi-Step Workflows

**What it fixes:** A chain of manual steps across multiple apps that the user does repeatedly after something happens in their app.

**The upgrade:** Use Make or Zapier to orchestrate the workflow visually, triggered by a webhook from the existing app.

**How to add it to an existing app:**

1. Add a webhook trigger step in Make or Zapier
2. In your existing app, add a `fetch()` call to POST to that webhook URL when the trigger event occurs
3. Build the downstream steps in Make/Zapier visually

**Make vs Zapier for upgrades:**
- **Make**: Use when the workflow has 3+ steps, conditional logic, or data transformation
- **Zapier**: Use when it's a simple 2-step (trigger → action) and speed of setup matters

**What your app sends to Make/Zapier:**
```typescript
await fetch(process.env.MAKE_WEBHOOK_URL, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ event: 'new_submission', data: payload }),
});
```

**Common impact:** Medium to High — eliminates manual multi-app workflows.
**Common effort:** Low to Medium — your app just fires a webhook; Make/Zapier handles the rest.

**Architecture template:**
```
App event → fetch(MAKE_WEBHOOK_URL) → Make/Zapier workflow → Step 1 → Step 2 → Step N
```

---

## Pattern 5: Claude API — Add AI Reasoning

**What it fixes:** An app that collects or displays data without intelligence — raw data that nobody interprets automatically.

**The upgrade:** Insert a Claude API call at the right trigger point — in a webhook handler, cron job, or user action — to classify, summarize, draft, or decide.

**How to add it to an existing Next.js app:**

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

const response = await client.messages.create({
  model: 'claude-sonnet-4-6',
  max_tokens: 1024,
  messages: [{
    role: 'user',
    content: `Here is the data: ${JSON.stringify(data)}. ${yourTask}`
  }]
});

const result = response.content[0].text;
```

**Common AI reasoning upgrades:**
| What the app does today | What to add |
|---|---|
| Receives form submissions | Claude classifies + drafts a response |
| Stores records in a table | Claude generates a weekly natural-language summary |
| Has a dashboard of metrics | Claude surfaces the most important insight daily |
| Logs events | Claude detects anomalies and sends an alert |
| Shows raw data | Claude adds a "What this means" plain-language layer |

**Model choice:**
- `claude-haiku-4-5-20251001` — Fast, cheap; use for classification, short summaries, simple drafts
- `claude-sonnet-4-6` — Balanced; use for most agentic reasoning tasks (default)
- `claude-opus-4-6` — Strongest reasoning; use only when quality is critical and latency/cost is acceptable

**Common impact:** Very High — the difference between a passive tool and an intelligent system.
**Common effort:** Low to Medium — a single API call added to an existing handler.

**Architecture template:**
```
Trigger → Gather context → Claude API call → Parse response → Store/Send/Display result
```

---

## Impact × Effort Matrix

Use this to rank enhancements quickly:

| Enhancement Type | Typical Impact | Typical Effort |
|---|---|---|
| Add webhook for existing event | High | Low |
| Add email/Slack notification | High | Low |
| Add Claude API to existing handler | Very High | Low |
| Add Vercel Cron for recurring task | High | Low |
| Add Make/Zapier automation | Medium-High | Low-Medium |
| Add MCP connection | Medium-High | Low (pre-built) / Medium (custom) |
| Add full scheduled digest | High | Medium |
| Add real-time data sync | Medium | Medium-High |

**Prioritization rule:** Lead with High Impact / Low Effort. These are the wins that make the user feel the app transformed overnight. Save High Effort items for after the quick wins are shipped and the user has momentum.
