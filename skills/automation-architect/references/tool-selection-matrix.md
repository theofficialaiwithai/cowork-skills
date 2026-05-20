# Tool Selection Matrix

Reference for Phase 3 and Phase 5. Contains full selection logic, use-case profiles, and
documentation links for every supported automation tool.

---

## Quick-Reference Matrix

| Tool | Best For | Complexity | AI-Native | Self-Hosted | Free Tier |
|------|----------|-----------|-----------|------------|-----------|
| Zapier | Simple app-to-app automations | Low | No | No | Yes (limited) |
| Make | Multi-step workflows with branching | Medium | No | No | Yes |
| n8n | Developer-grade, full control | High | Partial | Yes | Yes (self-host) |
| Gumloop | AI-first pipelines with LLM nodes | Medium | Yes | No | Yes |
| Lindy | Conversational AI agents | Low-Medium | Yes | No | Yes |
| Claude API | Reasoning, orchestration, tool use | High | Yes | No | No |
| Openclaw | Multi-agent coordination at scale | High | Yes | No | No |

---

## Tool Profiles

### Zapier
**Use when**: Simple trigger → action logic. The user needs to connect common apps (Gmail,
Slack, Sheets, Notion, HubSpot, etc.) without writing code. Volume is low-to-medium.

**Don't use when**: Multi-step branching logic, heavy AI integration, cost-sensitivity at
scale, or self-hosting is required.

**Strengths**: 6,000+ app integrations, easiest onboarding, reliable for simple flows.
**Weaknesses**: Expensive at volume, limited logic, not AI-native.

**Documentation**:
- Integration directory: https://docs.zapier.com/integrations
- Help center: https://help.zapier.com/hc/en-us

**Setup starting point**: zapier.com → New Zap → Choose trigger app → Choose action app

---

### Make (formerly Integromat)
**Use when**: The workflow has multiple steps, parallel branches, data transformation, or
loops. The user wants visual workflow design with more power than Zapier but no code.

**Don't use when**: AI-heavy tasks, self-hosting required, or the user needs simplicity above
all else.

**Strengths**: Visual flow builder, powerful data mapping, routers/iterators/aggregators,
competitive pricing.
**Weaknesses**: Steeper learning curve, limited native AI, not designed for agent-style tasks.

**Documentation**:
- App directory: https://apps.make.com/
- Developer docs: https://developers.make.com/

**Setup starting point**: make.com → Create a new scenario → Add modules

---

### n8n
**Use when**: The user wants developer-grade control, self-hosting, custom code nodes, or
complex conditional logic. Good for technical users who want to avoid vendor lock-in.

**Don't use when**: The user is non-technical, wants managed hosting, or needs simplicity.

**Strengths**: Open source, self-hostable, JavaScript/Python code nodes, 400+ integrations,
free on self-host.
**Weaknesses**: Requires more setup, smaller app library than Zapier, steeper learning curve.

**Documentation**:
- Full docs: https://docs.n8n.io/

**Setup starting point**: n8n.io → Start free (cloud) or self-host via Docker

---

### Gumloop
**Use when**: The workflow is AI-native — multiple LLM steps, prompt chaining, scraping +
AI analysis, document processing, or output generation. Non-technical users who want
AI-first pipelines without API keys.

**Don't use when**: No AI involved, needs enterprise integrations, or high-volume production.

**Strengths**: Visual AI workflow builder, built-in LLM nodes, scraping, document AI,
no-code friendly.
**Weaknesses**: Smaller app ecosystem, newer platform, best for AI-centric tasks.

**Documentation**:
- Full docs: https://docs.gumloop.com/

**Setup starting point**: gumloop.com → New flow → Add AI nodes

---

### Lindy
**Use when**: The system needs a conversational AI agent that talks to users, handles emails
or messages, has memory, or can be given a persona and instructions.

**Don't use when**: No conversation required, needs complex data pipelines, or the task is
purely trigger → action.

**Strengths**: Purpose-built for AI agents, natural language configuration, memory, handles
email/calendar natively.
**Weaknesses**: Less flexible for complex backend automation, limited integrations vs. Zapier.

**Documentation**:
- Full docs: https://docs.lindy.ai/

**Setup starting point**: lindy.ai → Create a Lindy → Define role + instructions

---

### Claude API
**Use when**: The system requires complex reasoning, planning, tool use orchestration,
long-context processing, or functions as the "brain" of a multi-step agent.

**Don't use when**: A no-code solution is required or the task can be handled by a simpler
automation tool.

**Strengths**: Best reasoning, 200K context window, tool use, vision, native in Cowork/Code.
**Weaknesses**: Requires API access and some coding, cost per token at scale.

**Documentation**:
- Platform docs: https://platform.claude.com/docs/en/home

**Setup starting point**: console.anthropic.com → API keys → Use claude-sonnet-4-6 or claude-opus-4-6

---

### Openclaw
**Use when**: The system requires multiple AI agents working together — orchestrator + specialist
agents, parallel task execution, shared memory, or complex agent-to-agent communication.

**Don't use when**: Single-agent or simple workflow — overkill, adds unnecessary complexity.

**Strengths**: Multi-agent architecture, agent orchestration, memory systems, production-grade.
**Weaknesses**: Highest complexity, steepest learning curve, newer ecosystem.

**Documentation**:
- Full docs: https://docs.openclaw.ai/

**Setup starting point**: openclaw.ai → Create workspace → Define agents + orchestration logic

---

## Decision Tree

Use this when the rule-based filter gives unclear results:

```
Is AI reasoning or generation a core part of the workflow?
├── No → Does it need 3+ steps with branching?
│         ├── No → ZAPIER
│         └── Yes → MAKE or N8N (n8n if self-host needed)
└── Yes → Is this a conversational agent (talks to users)?
          ├── Yes → LINDY (simple) or CLAUDE API (complex)
          └── No → Is it multiple LLM steps in sequence?
                   ├── Yes → GUMLOOP (no-code) or CLAUDE API (code)
                   └── Is it multiple agents coordinating?
                            ├── Yes → OPENCLAW
                            └── No → CLAUDE API
```

---

## Integration Overlap Guide

When a user's tool choice is constrained by which apps they use:

**Zapier wins** for: Gmail, Google Sheets, HubSpot, Salesforce, Typeform, Airtable, Slack,
Notion, Calendly — any mainstream SaaS tool.

**Make wins** for: Same as Zapier but with more complex data transformation between steps.

**n8n wins** for: Any tool with a REST API (everything), plus custom webhook logic.

**Gumloop wins** for: Workflows where the data flow passes through multiple AI models.

**Lindy wins** for: Email inboxes, calendars, and customer-facing conversation workflows.

---

## Cost Guidance (as of 2025)

| Tool | Entry Price | Scale Price |
|------|------------|-------------|
| Zapier | Free (limited), $20/mo starter | $100+/mo at volume |
| Make | Free (1,000 ops), $10/mo | $50+/mo |
| n8n | Free self-host, $20/mo cloud | $50/mo cloud |
| Gumloop | Free tier available | Credits-based |
| Lindy | Free tier, ~$49/mo pro | Usage-based |
| Claude API | Pay-per-token | ~$3–$15 per M tokens |
| Openclaw | Contact sales | Enterprise |
