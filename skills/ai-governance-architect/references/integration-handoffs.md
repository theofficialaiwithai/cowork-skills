# Integration Handoffs

This skill never builds anything itself. Its whole output is: a confirmed list of governance options the user wants, handed to whichever skill actually builds (code-build-copilot for existing products, prd-assistant for new ones). Get the handoff format right and those skills do the rest.

## Audit Mode → code-build-copilot

code-build-copilot expects "a PRD or feature list" and then walks the user through it one step at a time, never advancing until they type "done." So the job here is to turn the selected governance options into something that reads exactly like a feature list entry - concrete enough that code-build-copilot can turn it into a single Claude Code prompt.

For each selected option, write:

- **What to build**: the mechanism itself (e.g. "confirmation modal before send_email fires, showing the rendered draft").
- **Where it plugs in**: the actual file, component, route, or function you identified in Step 2 - not a generic location. If you don't know the exact file because Step 2 was done at a conceptual level (no code yet, just a description), say so and note that code-build-copilot's first step on this item should be locating the right insertion point.
- **What "done" looks like**: a testable condition (e.g. "the send API is never called without a prior user click on Confirm; verify by checking the call site is gated behind the confirmation handler").

Compile these into a short list, ordered by the same priority you used when presenting the menu (highest-stakes / weakest-coverage first). Then either:

- Call the `code-build-copilot` skill directly with this list as the feature list input, or
- Tell the user plainly that you're handing off to code-build-copilot and proceed using its step-by-step pattern yourself (one prompt at a time, with a verification checklist, never advancing until they confirm) if the skill isn't separately invokable in this context.

Don't pad this list with options the user didn't select, and don't silently drop the HITL-Lead items into a different format than the HITL ones - a decision-rights matrix is still a concrete deliverable ("write decision_rights.md documenting X, Y, Z") even though it's a document rather than a UI element. code-build-copilot can walk someone through writing a doc just as well as wiring up a modal.

## Pipeline Mode → prd-assistant

prd-assistant follows a lean PRD template and writes the PRD after one clarifying question. Don't write the PRD - that's its job. Instead, produce a **governance addendum**: a short mapping of selected options to where they belong in the PRD and what specific language that section needs. This addendum is what prd-assistant should treat as additional input alongside the Agentic Architecture Brief, not as a separate section bolted onto the end.

Format, one entry per selected option:

- **PRD section it belongs in** (use the lean template's actual section names - Core Features, Non-Functional Requirements, Success Metrics, etc. - so it merges in cleanly rather than creating a new "Governance" section nobody reads).
- **Requirement language for that section**, written the way a PRD requirement reads, not the way a menu option reads. Example: menu option "Approval gate before auto-send" becomes PRD language "Core Features → Auto-send: the feature must render the drafted message and require explicit user confirmation before the send API is called; no message sends without this step."
- **Which feature/action point it constrains**, so prd-assistant places it next to the relevant feature description rather than in a generic list.

Hand this whole addendum over before prd-assistant starts writing. The reason to embed rather than append: a constraint sitting directly under the feature it limits gets respected during the build; a constraint in a separate "governance" section at the bottom gets skimmed and forgotten. If prd-assistant's one clarifying question would otherwise ask about something this addendum already answers (e.g. scope of the autonomous behavior), let the addendum answer it rather than asking the user twice.

## Common to both

Always show the user the final list/addendum before handing it off - a quick "here's what's getting built in, does this match what you picked" confirmation. The whole point of this skill is keeping a human in the lead of their own governance design; skipping a last confirmation before handoff would undercut that.
