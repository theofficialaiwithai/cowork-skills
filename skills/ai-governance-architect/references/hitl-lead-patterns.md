# Human-in-the-Lead (HITL-Lead) Patterns

Source concept: Kategos, "Human in the Lead, Not Human in the Loop: Rethinking AI Governance" (kategos.ai). The core reframe: HITL is supervision (humans react to what AI did); HITL-Lead is leadership (humans set the goals, boundaries, and ethics *before* AI acts, and AI amplifies that direction rather than substituting for it). These patterns live upstream of execution - in planning, scoping, and recurring governance, not at the moment an action fires.

A product can have excellent HITL checkpoints and still have no HITL-Lead at all - nobody ever wrote down what the AI is *for*, what it's *not allowed* to decide, or who's accountable for its strategic direction. That gap is just as real as a missing approval gate, even though it's less visible in the code. Surface it anyway.

For each pattern: what it is, when it earns its keep, and menu phrasing to use (swap in specifics about the actual product).

## Strategic intent document
A short, explicit statement of what the AI is *for* in this product - the goals it serves, the boundaries it must never cross, and who owns that definition. This is the artifact that everything else gets checked against; without it, "is the AI doing the right thing" has no answer to compare to.

Best for: any product where the AI's scope could quietly expand over time (an assistant that started doing X and is now doing X, Y, and Z without anyone deciding that was okay).

Menu phrasing: "Write a short strategic-intent doc for [agent/feature]: what it's for, what it must never do, who owns that definition."

## Decision-rights matrix
An explicit map of which decisions the AI may make fully autonomously, which require human sign-off, and which are human-only and the AI may only inform. Different from an approval gate (which is an enforcement mechanism) - this is the upstream policy that an approval gate, if added, would be enforcing.

Best for: products where it's currently implicit or assumed which decisions the AI "should" be trusted with, rather than written down and agreed on.

Menu phrasing: "Define which decisions in [feature] the AI can make alone, which need sign-off, and which stay human-only - write it down rather than leaving it implicit."

## AI operating boundaries / guardrails defined by humans
Concrete limits on what the AI may act on or affect, set by a human up front rather than inferred by the AI from data or instructions at runtime. E.g. spend caps, audience size limits, categories of users it can't act on, topics it can't generate content about.

Best for: any agent with real-world reach (spending money, contacting people, publishing) where the boundary should be a hard constraint, not a hope that the AI infers it correctly.

Menu phrasing: "Set explicit, human-defined limits on [agent] - e.g. spend cap, audience size, excluded categories - rather than relying on it inferring reasonable boundaries."

## Governance review cadence
A recurring (not one-time) human review of whether the AI's behavior still matches the strategic intent - not a review of individual outputs, but of the pattern and direction. Catches drift that no single approval gate would catch, because each individual action can look fine while the aggregate trend quietly moves away from what was intended.

Best for: any product that's been live a while, or that learns/adapts over time, where "is this still doing what we meant it to do" needs a standing answer rather than a one-time check at launch.

Menu phrasing: "Set a recurring review (monthly/quarterly) of whether [agent]'s behavior still matches its original intent, separate from day-to-day output review."

## Capability-building over automation-dependence
A deliberate choice to keep the humans who oversee the AI sharp enough to actually direct it - documentation, training, or workflow design that prevents the "skill atrophy" the source article calls out, where humans defer to AI because they've lost the context to evaluate it. This is a design and team practice, not a feature, but it can show up in-product as surfaced reasoning, explainability, or "why" context rather than just an answer.

Best for: products where the humans nominally "in the lead" are at risk of rubber-stamping because they no longer have the standing knowledge to second-guess the AI.

Menu phrasing: "Make sure [feature]'s output includes enough of its reasoning/context that the human reviewing it can actually evaluate it, not just approve it on faith."

## AI-as-amplifier framing in the UX
A product-level choice to present AI output as an input to a human decision (a suggestion, a draft, a ranked option set) rather than as the decision itself - even in places where no formal approval gate exists. This is about framing and UI, not just mechanics: it shapes whether users *feel* like they're leading or being led.

Best for: any feature where the AI's output reads as a final answer when it should read as a recommendation - even if there's technically a way to change it.

Menu phrasing: "Reframe [feature]'s output as a recommendation the user acts on, not a finished decision - same underlying mechanics, different framing."
