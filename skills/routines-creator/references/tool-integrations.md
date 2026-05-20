# Tool Integrations for Routines

This file maps available tools and MCPs to the types of tasks they're best suited for in a routine context. Use it during Phase 2 (Design) to figure out which tools to include in each step of the routine.

---

## Communication & Messaging

### Gmail
**Best for:** Reading, searching, drafting, and labeling emails.

Routine use cases:
- Pull unread emails from a specific sender or label for a morning digest
- Search for emails matching a topic for research or triage routines
- Create draft replies based on email content
- Label and organize emails as part of an inbox management routine

Key capabilities: `search_threads`, `get_thread`, `create_draft`, `list_labels`, `label_thread`

**Limitation:** Cannot send emails directly — only create drafts. If sending is needed, route through Zapier.

---

### Google Calendar
**Best for:** Reading upcoming events, creating events, checking availability.

Routine use cases:
- Pull today's or this week's events for a briefing routine
- Create calendar blocks automatically (focus time, recurring check-ins)
- Check availability before suggesting meeting times
- Get event details to prep talking points or agendas

Key capabilities: `list_events`, `get_event`, `create_event`, `list_calendars`

---

### Calendly
**Best for:** Checking scheduled meetings, availability, and booking links.

Routine use cases:
- Pull upcoming booked meetings for weekly prep
- Check availability schedule for a scheduling routine
- Generate single-use scheduling links

---

## Productivity & Project Management

### Notion
**Best for:** Reading and writing to Notion databases, pages, and docs.

Routine use cases:
- Pull open tasks from a Notion database for a weekly review routine
- Create new pages or database entries (meeting notes, research docs)
- Update task statuses as part of a task management routine
- Fetch project context before preparing a client-facing deliverable

Key capabilities: `notion-search`, `notion-fetch`, `notion-create-pages`, `notion-update-page`

---

## Automation Connectors

### Zapier
**Best for:** Bridging Claude with apps that don't have direct MCPs, and building event-triggered routines.

Routine use cases:
- Trigger a routine when a new form submission arrives
- Send a message to Slack or Teams when a routine completes
- Write a row to a Google Sheet as routine output
- Connect to 6,000+ apps via pre-built Zaps

Key capabilities: `execute_zapier_write_action`, `execute_zapier_read_action`, `list_enabled_zapier_actions`

**When to use Zapier vs. a direct MCP:** Use a direct MCP when available — it's faster and simpler. Use Zapier when: (a) the app doesn't have a direct MCP, (b) you need two-way sync with an app, or (c) you need to trigger Claude from an external event.

---

### Make / Integromat
**Best for:** Complex multi-step automation scenarios with conditional logic.

Routine use cases:
- Build event-triggered routines with complex filtering
- Chain multiple apps together with branching logic
- Handle webhooks from external services
- Schedule scenarios with precise timing control

Use Make when the automation logic is complex enough that Zapier's linear flow isn't sufficient — e.g., "if the email is from a VIP sender AND the subject contains 'urgent', do X; otherwise do Y."

---

## File & Document Tools

### Google Drive
**Best for:** Reading and writing files in Google Drive.

Routine use cases:
- Save routine outputs (reports, summaries) as Google Docs
- Read a source file at the start of a routine (e.g., a brief, a template)
- Search for recent files to include in a digest

Key capabilities: `read_file_content`, `create_file`, `search_files`, `list_recent_files`

---

### Local File System (Read/Write/Edit tools)
**Best for:** Creating and editing files in the user's workspace folder.

Routine use cases:
- Save routine outputs as .md, .docx, .xlsx, or .txt files locally
- Read a local config or template file at the start of a routine
- Append to a running log file

---

### Word Documents (docx skill)
**Best for:** Producing formatted Word documents as routine output.

Routine use cases:
- Weekly briefing document
- Meeting prep sheet
- Status report

Invoke the `docx` skill when the routine's output should be a formatted .docx file rather than plain text.

---

### Excel Spreadsheets (xlsx skill)
**Best for:** Producing or updating spreadsheet files as routine output.

Routine use cases:
- Weekly metrics tracker
- Task list with status columns
- Data aggregation from multiple sources

Invoke the `xlsx` skill when the routine's output is a structured table or spreadsheet.

---

## Design & Visual Tools

### Canva
**Best for:** Creating or updating design assets automatically.

Routine use cases:
- Generate a social media post graphic as part of a content routine
- Update a presentation template with new data
- Create weekly announcement visuals

---

### Figma
**Best for:** Reading design context or generating design assets.

Routine use cases:
- Pull design specs to feed into a documentation routine
- Generate diagrams or wireframes as part of a planning workflow

---

## Development & Infrastructure

### Supabase
**Best for:** Running SQL queries, reading/writing database records.

Routine use cases:
- Pull metrics from a database for a reporting routine
- Insert records as part of a data processing workflow
- Run scheduled data cleanup queries

---

### Vercel
**Best for:** Monitoring deployments and project status.

Routine use cases:
- Daily deployment health check
- Alert on failed builds as part of a monitoring routine

---

## Web Research

### Web Search / WebFetch
**Best for:** Pulling live information from the web.

Routine use cases:
- Morning news digest for a specific topic or industry
- Competitive intelligence routine (check competitor sites, product pages)
- Research step before a meeting or client call
- Price monitoring or content monitoring

---

### Apify
**Best for:** Web scraping and structured data extraction at scale.

Routine use cases:
- Scrape a job board or listing site on a schedule
- Extract structured data from websites that don't have APIs
- Monitor web content for changes

---

## Tool Selection Quick Reference

| Task | Recommended Tool |
|---|---|
| Read today's emails | Gmail MCP |
| Create a calendar event | Google Calendar MCP |
| Pull open Notion tasks | Notion MCP |
| Save output as a Word doc | docx skill |
| Save output as a spreadsheet | xlsx skill |
| Send a Slack message | Zapier (Slack action) |
| Connect to an app without an MCP | Zapier or Make |
| Complex conditional automation | Make MCP |
| Run a database query | Supabase MCP |
| Pull live web data | WebSearch / WebFetch |
| Save a file locally | Local file tools (Read/Write/Edit) |
| Save to Google Drive | Google Drive MCP |
| Create a design asset | Canva MCP |
