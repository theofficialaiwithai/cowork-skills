# Human-in-the-Loop (HITL) Patterns

HITL is reactive: the AI produces an output or is about to take an action, and a human reviews, approves, corrects, or stops it. These patterns live at execution time, right at the action point. Use the action-point list from SKILL.md Step 2 to pick which of these actually apply - don't propose all of them everywhere.

For each pattern below: what it is, when it earns its keep, and a concrete phrasing to use when presenting it as a menu option (swap in the real action point you found).

## Approval gate
The AI prepares an action but a human must explicitly confirm before it executes. The AI does the work; the human keeps the "go" button.

Best for: anything irreversible or hard to undo - sending a message on someone's behalf, charging a card, publishing content, deleting data, executing a trade.

Menu phrasing: "Add an approval gate before [action] - the AI drafts/prepares it, but it doesn't fire until you confirm."

## Confidence-threshold escalation
The AI acts autonomously when it's confident, and routes to a human only when its own confidence score (or a proxy for it) drops below a set bar. This avoids making every single action a chokepoint while still catching the cases most likely to be wrong.

Best for: high-volume classification or triage tasks where reviewing every item isn't feasible, but the AI can reasonably flag its own uncertainty.

Menu phrasing: "Auto-handle [action] when the AI is confident, but escalate to a human when confidence is low or the case is unusual."

## Override / correction mechanism
After the AI acts (or proposes), the human can edit, correct, or reverse the outcome - and that correction ideally feeds back into improving the system. Different from an approval gate because the action already happened or was already shown as final; this is about the ability to fix it.

Best for: recommendations, generated content, or categorizations where being wrong sometimes is acceptable as long as it's easy to catch and fix.

Menu phrasing: "Let users override/correct [output] after the fact, and log corrections so the pattern of mistakes is visible."

## Audit / decision log
Every autonomous action the AI takes gets recorded - what it did, why (its stated reasoning or the inputs it used), and when. Nobody has to review it in real time, but the record exists for after-the-fact accountability.

Best for: any autonomous action, especially ones that are individually low-stakes but could be high-stakes in aggregate, or where "who decided this and why" will eventually be a question someone asks.

Menu phrasing: "Log every time [action] happens autonomously - what was decided, what inputs drove it, and when - so it's reviewable later even without real-time approval."

## Kill switch / pause control
A human can halt the AI's autonomous behavior entirely, immediately, without needing to understand or unwind individual actions first. This is the emergency brake, distinct from per-action approval.

Best for: any system that runs unattended for stretches of time (cron jobs, agents that chain multiple actions, anything that could misbehave in a loop).

Menu phrasing: "Add a kill switch so [agent/automation] can be paused instantly if something looks wrong, without having to debug it live."

## Sampling review
Instead of reviewing every action, a human reviews a random or risk-weighted sample after the fact. Cheaper than full review, catches systemic problems before they compound.

Best for: high-volume, low-individual-stakes actions where 100% human review isn't realistic but zero review is too risky.

Menu phrasing: "Periodically sample and review a percentage of [action] outcomes to catch drift or systemic errors."

## Notification-and-veto window
The AI announces an intended action and waits a short window before executing, giving a human the chance to step in and stop it - but doesn't require active approval to proceed (silence = go-ahead).

Best for: medium-stakes, time-sensitive actions where a full approval gate would be too slow but zero warning is too risky.

Menu phrasing: "Announce [action] before it happens with a short window to veto, rather than requiring active sign-off every time."
