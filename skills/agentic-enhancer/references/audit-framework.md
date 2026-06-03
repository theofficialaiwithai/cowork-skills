# Audit Framework — 5-Dimension Agentic Gap Analysis

Use this framework during Phase 2 to systematically scan an existing app for agentic gaps. Work through each dimension in order. For each one, identify: what the app currently does, what it's missing, and what the gap costs the user.

---

## Dimension 1: Event Response

**The question:** When something important happens in or around this app, does it react automatically?

**What to look for:**
- Does a user action (form submit, payment, sign-up, upload) trigger anything downstream — or does the user have to manually check or act?
- Does the app receive events from external services (Stripe, Typeform, Calendly, GitHub, etc.) and handle them — or ignore them?
- When data changes in the database, does anything happen automatically?

**Signs of a gap:**
- "I have to manually check" anything — a form, an inbox, a database table
- External events (payments, bookings, submissions) arrive but nothing reacts to them
- Users complete actions in the app and have to wait for a human to respond

**Common enhancements:**
- Add a webhook receiver (`/api/webhooks/[service]`) to react to external events
- Add a Supabase database trigger or webhook to react to data changes
- Add an automatic response/confirmation when users submit something

---

## Dimension 2: Scheduled Automation

**The question:** Does the app do anything on a timer, without anyone initiating it?

**What to look for:**
- Are there tasks the user does manually on a regular schedule? (checking data, sending reports, syncing, reviewing)
- Should the app be doing anything nightly, daily, weekly, or monthly?
- Is there data that goes stale or accumulates without periodic processing?

**Signs of a gap:**
- User mentions checking, reviewing, or updating something "every day/week"
- Reports or digests are compiled manually
- No Vercel Cron Jobs or equivalent scheduled tasks exist
- Data builds up in the database with no automated processing

**Common enhancements:**
- Add Vercel Cron Job for daily/weekly digests or reports
- Add scheduled data sync (pull from external API → update database)
- Add scheduled cleanup (archive old records, expire sessions, purge stale data)
- Add deadline/reminder system (check for upcoming due dates → notify)

---

## Dimension 3: External Connectivity

**The question:** Is the app connected to all the tools and services it should be talking to?

**What to look for:**
- Are there tools the user uses alongside this app that could be integrated? (Slack, Notion, Google Calendar, HubSpot, Airtable, etc.)
- Does the user copy/paste data between this app and another tool?
- Could Claude (or another AI layer) be given access to external data to answer questions or perform tasks?
- Are there outbound integrations missing (the app should be writing to somewhere it isn't)?

**Signs of a gap:**
- User manually copies data from one tool to another
- The app is an island — it doesn't read from or write to any external service
- The user "checks" an external tool to get information that the app should surface
- No MCP servers connected to the AI layer (if the app has one)

**Common enhancements:**
- Add MCP server connection for key external tools (Supabase, Notion, GitHub, Slack)
- Add outbound integration (write to Notion, post to Slack, update Airtable) when events occur
- Add inbound data pull (sync from external API into the app's database)
- Add Make or Zapier workflow to bridge the app with the user's other tools

---

## Dimension 4: AI Reasoning

**The question:** Is AI being applied at the right moments — or is the app just storing and displaying data without intelligence?

**What to look for:**
- Are there places where data is collected but never analyzed, summarized, or acted on intelligently?
- Does the user have to read raw data and manually draw conclusions?
- Could Claude generate something useful (a summary, a draft, a classification, a recommendation) at a trigger point?
- If the app has an AI feature, is it only responding to direct user queries — or could it proactively offer insights?

**Signs of a gap:**
- Raw data sits in a database with no AI layer on top
- Users have to manually interpret submissions, reports, or logs
- The app has no AI at all — it's pure CRUD
- AI exists in the app but only as a chatbot, not as a proactive reasoning layer

**Common enhancements:**
- Add Claude API call at a trigger point (classify, summarize, draft, decide)
- Add AI-powered digest/report generation in a cron job
- Add AI triage for incoming submissions (auto-categorize, auto-respond)
- Add proactive AI insights surfaced in the dashboard (not just in chat)

---

## Dimension 5: Notification & Alerting

**The question:** Does the app proactively tell the right people what they need to know, at the right time?

**What to look for:**
- When something important happens, who needs to know — and are they being told automatically?
- Are there conditions that should trigger an alert but currently don't? (threshold crossed, deadline approaching, anomaly detected)
- Does the user have to actively check the app to stay informed — instead of being notified?
- Are notifications going to the right channel? (email, Slack, SMS, push)

**Signs of a gap:**
- No email or Slack notifications exist anywhere in the app
- The user checks the app to see if anything happened (pull), instead of being notified (push)
- Alerts exist but go to the wrong channel or contain too little context
- High-importance events (payment failed, deadline missed, threshold crossed) trigger nothing

**Common enhancements:**
- Add email notifications via Resend for key events
- Add Slack notifications via webhook for team-relevant events
- Add threshold alerting (if X > Y → send alert)
- Add daily/weekly digest emails using Claude API for natural-language summaries
- Add in-app notification system (Supabase real-time → frontend toast/badge)

---

## How to Use This Framework

For each dimension, assign one of three statuses:

| Status | Meaning |
|---|---|
| ✅ Covered | The app handles this well already |
| 🟡 Partial | Something exists but it's incomplete or weak |
| 🔴 Missing | This dimension is completely unaddressed |

A `🔴 Missing` on Dimensions 1 or 5 is almost always high-impact and relatively low-effort to fix — these are your first recommendations.

A `🔴 Missing` on Dimension 4 (AI Reasoning) often has the highest transformational impact — turning a passive data store into an intelligent system.

A `🔴 Missing` on Dimension 2 (Scheduled Automation) is the "set it and forget it" win — tasks that should just happen, without anyone remembering to do them.
