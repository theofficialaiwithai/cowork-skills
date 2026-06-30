---
name: ai-governance-architect
description: >-
  Audits a product or in-progress build for AI governance gaps, then walks the user
  through adding what's missing. Covers two tracks - human-in-the-loop (reactive: approval
  gates, confidence escalation, audit logs, kill switches) and human-in-the-lead (upstream:
  strategic intent docs, decision-rights matrices, AI boundaries set by humans before AI
  acts). ALWAYS surfaces both tracks, never just one, and lets the user pick. Use whenever
  the user wants to add human oversight, approval steps, or governance to an AI feature;
  says 'human in the loop', 'human in the lead', 'add an approval step', 'AI governance',
  'who is accountable here', 'add oversight', or seems worried about an AI feature acting
  unsupervised. Also trigger in the build pipeline - runs after vibe-architect-os (once an
  Agentic Architecture Brief exists) and before prd-assistant. After the user picks
  options, hand off to code-build-copilot for an existing product, or fold picks into the
  brief feeding prd-assistant for a new build.
---

# AI Governance Architect

Most AI products default to one kind of human oversight - a human reviewing what the AI already did. That's human-in-the-loop (HITL), and it's necessary but not sufficient: it only catches problems after the AI has acted, and it puts the human in a reactive, supervisory role.

The complementary idea is human-in-the-lead (HITL-Lead): humans define the goals, boundaries, and decision-rights *before* the AI acts, so the AI is amplifying a human-set direction rather than making the call itself. Loop is supervision. Lead is direction. A well-governed product usually needs both - one keeps execution safe, the other keeps strategy and ethics in human hands.

This skill's job is to make sure every product it touches gets offered options from *both* tracks, never just the reactive one, and to turn whatever the user picks into either a build-ready feature list (existing product) or PRD-embedded requirements (new product, via prd-assistant).

## Step 1: Work out which mode you're in

**Pipeline Mode** - you're mid-build-pipeline. Signal: the conversation already has a vibe-architect-os Agentic Architecture Brief, or the user is clearly about to move into prd-assistant for a new product. In this mode you're designing governance into something that doesn't exist as code yet.

**Audit Mode** - the user has something real: a live app, an in-progress codebase, or a finished PRD, and wants to know where human control is missing. In this mode you're inspecting something that already exists.

If you can't tell from context, ask one direct question: "Are we adding governance to something you've already built (or are building), or designing it in before we write the PRD?" Don't guess - the two modes read context completely differently (Step 2) and guessing wrong wastes the whole pass.

## Step 2: Gather context - find where AI currently acts unsupervised

You can't propose governance for actions you haven't found. Look for every point where AI produces an output that triggers a real-world effect or a decision a human would otherwise make.

**Audit Mode**: Read the actual product. If there's a codebase, search for the action points - API calls that send/post/delete/charge/publish, automated recommendations surfaced to end users, anything that fires on a schedule or webhook without a human touching it. If there's only a PRD or feature list (no code yet), read it the same way: find every feature description where "the AI will..." appears and note what it does next.

**Pipeline Mode**: Read the Agentic Architecture Brief vibe-architect-os produced. It already documents the agentic layer - webhooks, cron jobs, MCP calls, autonomous decision points. Each one is a candidate.

Make a short list of these action points before moving on. This list is what Step 3 turns into governance options - skipping this step leads to generic, copy-paste recommendations instead of ones tied to what this specific product actually does.

## Step 3: Build the menu - always both tracks, every time

Read `references/hitl-patterns.md` and `references/hitl-lead-patterns.md` together. For every action point on your Step 2 list, propose at least one pattern from each file - even when one track looks obviously more relevant than the other. This isn't about padding the list; it's the actual point of the skill. A product that already has a confirmation modal (HITL) can still be missing a documented decision-rights boundary (HITL-Lead) for what the AI may do without asking, and vice versa. Read `references/audit-rubric.md` for how to score each action point's current exposure and turn that into plain language ("no approval step before this fires" / "no documented boundary on what this agent can decide alone").

Present the menu with `AskUserQuestion`, `multiSelect: true`. Group the options so HITL and HITL-Lead are visually distinct (e.g. two separate questions, or clearly labeled option sets) - the user needs to know which kind of control they're picking, not just that it's "more oversight." Keep each option's description concrete: name the specific action point it applies to, not a generic pattern name.

Hard rule: never silently drop a track because the other one seems more obviously needed. If you find yourself about to present only HITL options because "this product doesn't really have strategy decisions," that's the moment to push past the assumption - re-read `references/hitl-lead-patterns.md` and find the upstream-governance angle anyway (even small products benefit from a one-paragraph strategic-intent note). The user decides what's overkill, not you.

## Step 4: Hand off based on mode

Read `references/integration-handoffs.md` for the full mechanics. Short version:

**Audit Mode → code-build-copilot.** Turn the user's selections into a feature list (one entry per selected option, written the way code-build-copilot expects a feature spec: what to build, where it plugs into the existing product, what "done" looks like). Then either invoke the `code-build-copilot` skill directly with that list, or tell the user you're handing off to it and proceed with its step-by-step build flow - one prompt at a time, never advancing until they confirm.

**Pipeline Mode → prd-assistant.** Don't write the PRD yourself. Instead, produce a short governance addendum: for each selected option, which PRD section it belongs in (Core Features, Non-Functional Requirements, Success Metrics, etc.) and the specific requirement language that section needs (e.g. "Core Features: the auto-send action must render a confirmation step showing the draft and may not call the send API until the user confirms"). Hand this addendum to prd-assistant so it gets woven into the PRD as it's written, not appended afterward - governance requirements read very differently when they're sitting next to the feature they constrain versus listed in a separate section nobody reads.

## Rules

- Always surface both tracks. One-sided output (all HITL or all HITL-Lead) is the single biggest failure mode for this skill - if you catch yourself doing it, stop and re-read Step 3.
- Tie every option to a real action point from Step 2. Don't recite a generic governance checklist - that's what makes recommendations feel bolted-on instead of designed-in.
- Don't pick options for the user. Present the menu, wait for their selections, then proceed. This skill exists to put humans in the lead of their own product's governance design - skipping the selection step would be a little ironic.
- In Audit Mode, actually read the product before proposing anything. A governance audit based on assumptions about what the codebase probably does is worse than no audit - it gives false confidence.
- Keep the handoff lightweight. This skill's output is a short, scoped list of selections and where they plug in - the heavy lifting (writing the PRD, writing the code) belongs to prd-assistant and code-build-copilot respectively.
