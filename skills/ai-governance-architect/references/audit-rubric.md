# Audit Rubric - Scoring Action Points and Presenting the Menu

This is how to go from the action-point list (SKILL.md Step 2) to a concrete, dual-track menu (Step 3) without it turning into a generic checklist.

## Scoring each action point

For every action point, answer four questions. The answers are what turn into plain-language gap descriptions in the menu - don't show the user a score, show them what the score means.

1. **Does a human see this before it has real-world effect?** No → HITL gap (likely: approval gate or notification-and-veto window).
2. **Does anything route uncertain or unusual cases to a human, or does everything run the same way regardless of confidence?** Uniform handling → HITL gap (likely: confidence-threshold escalation, or sampling review if volume is too high for full escalation).
3. **If this goes wrong, is there a record of what happened and why?** No → HITL gap (likely: audit/decision log).
4. **Is there a written boundary on what this is allowed to do, set by a human in advance - or is the scope just whatever it currently happens to do?** Implicit/undocumented → HITL-Lead gap (likely: decision-rights matrix or operating boundaries).

Then zoom out from individual action points to the product level and ask two more:

5. **Is there anywhere a human wrote down what this AI feature is *for* and what it must never do?** No → HITL-Lead gap (strategic intent document).
6. **Does anyone revisit, on a schedule, whether this is still doing what it was meant to do - or is launch the last time anyone checked?** No → HITL-Lead gap (governance review cadence).

A product can score "fine" on 1-4 (good execution-time checkpoints) and still fail 5-6 completely. That's the most common shape of a one-sided product, and exactly the gap this skill exists to catch. Don't let strong HITL coverage talk you out of proposing HITL-Lead options.

## Severity, not just presence

When an action point has *no* coverage at all (e.g. an irreversible action with zero gate, zero log, zero documented boundary), say so plainly rather than softening it - that's the kind of gap that matters most to surface clearly. When something has partial coverage (e.g. a log exists but nothing escalates on low confidence), name specifically what's missing rather than re-describing what's already there.

## Presenting the menu

Use `AskUserQuestion` with `multiSelect: true`. Structure options so the two tracks are visually separable - either two separate questions ("Human-in-the-loop options" / "Human-in-the-lead options") or one question with option labels prefixed by track. Don't interleave them silently; the user should be able to tell at a glance which kind of control each option adds.

Each option's description should name the actual action point, not just the pattern: "Approval gate before the auto-send email feature fires" reads as real; "Add an approval gate" reads as boilerplate. Pull the wording straight from what you found in Step 2.

If the product has many action points, don't try to cover all of them in one menu - prioritize the two or three with the weakest current coverage (per the scoring above) and the highest stakes (irreversible, financial, reputational, or affecting other people without their knowledge). Mention there are more candidates if the user wants a second pass later.
