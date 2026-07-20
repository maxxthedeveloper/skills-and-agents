# Email type playbooks

One section per email type. Each gives: the job, structure, word budget, subject pattern, CTA style, Loops mechanism + trigger, and DO/DON'T pairs from the cohort research (Cursor, Cognition, Linear, Loom, Superhuman, Raycast). Read only the section for the type you're writing.

Contents: model/agent release · feature announcement · welcome · activation nudge · first-success milestone · changelog/digest · trial & upgrade · dunning · usage recap · winback · transactional & required notices.

---

## Model/agent release

**Job**: a new model or agent capability is in Framer; get users to try it today.
**Budget**: 45–110 words. **Mechanism**: campaign, engaged segment (or all Agents users).
**Subject**: name the model, present tense, under 60 chars — “Fable 5 is now in Framer”, “Try Fable 5 in Framer”.
**Preview**: the positioning line — “Anthropic's most capable model, on the canvas.”

Structure (the formula):
1. "{Model} is now available in Framer." — line one, no wind-up. (House naming: never "Framer Agents" as a compound — the product is Framer, the feature is Agents.)
2. One credibility line: hands-on ("We've found it strongest at…") or one CanvasBench number with comparison ("clears 71% on CanvasBench, ahead of X at 58%").
3. One practical detail: credits/pricing, plan availability, how to select it.
4. One button into the product; optional inline links to the announcement post + CanvasBench.

- DO link the model-maker's announcement post if Framer is mentioned in it — third-party proof.
- DO give when-to-use guidance (Cognition: “Use this model when you need Devin to thoroughly investigate an issue”) when there's no clean benchmark story.
- DON'T stack two benchmark numbers, list every capability, or explain what an LLM is.
- DON'T use the model-maker's superlatives (“most intelligent model ever”, “most powerful”) — one factual apposition. Borrow Cursor's apposition shape, not its word “powerful” (banned).

## Feature announcement

**Job**: one shipped feature → one action.
**Budget**: under 150 words. **Mechanism**: campaign (segment who'd care) — or workflow if it's tied to behavior.
**Subject**: the feature, plainly — "Branching is here", "Introducing {Feature}" only for genuinely large launches.

Structure: problem sentence (optional, Linear-style) → what you can now do ("You can now…") → one image or GIF of the real feature → one button. One feature per email; a launch with four features is a launch email (see Framer 3.0 in the swipe file) — sectioned, each section = bold heading + 1–2 sentences + inline "Learn more" link.

- DO open changelog-style with the pain: "Important team context doesn't always belong in a specific issue" → the feature (Linear).
- DO show the actual product (screenshot/GIF), not an illustration.
- DON'T write "powerful", "seamless", "revolutionary" — the cohort never does.
- DON'T bundle a feature announcement with an upgrade pitch.

## Welcome (onboarding email 1)

**Job**: confirm the choice, set expectations, point at exactly one first action.
**Budget**: under 120 words. **Mechanism**: workflow, trigger Contact added, timer Immediately.
**Subject**: "Welcome to Framer".

Structure: one sentence of belief or orientation (Linear opens with "we believe software can feel magical" — Framer's equivalent: making the web more creative) → the one first action (start from a template / open the canvas) → one button → optionally 2–3 arrow-links (Guide →, Community →, Changelog →) Linear-style.

- DO the Linear anti-onboarding restraint: one email, a few links, zero tips-and-tricks.
- DO say what emails they'll get and how often, if a digest exists (Raycast: "Pure information and no spam").
- DON'T list features, DON'T multiple CTAs, DON'T "we're so excited you're here!".

## Activation nudge

**Job**: the user started but didn't reach the aha moment (site created, never published). Highest-ROI email in the sequence.
**Budget**: under 100 words. **Mechanism**: workflow — event trigger (or Contact added) + 2–3 day timer + audience filter `published equals false`. Behavior-gated, never sent to people who already did it.
**Subject**: name their situation — "Your site is one publish away".

Structure: name where they are (blamelessly — "Your site {EVENT_PROPERTY:siteName | Untitled} is ready to publish") → the single unblocking action → one button deep into their project.

- DO reference their actual object (their site, their draft) — behavioral personalization beats `{firstName}`.
- DON'T send generic tips, DON'T guilt ("you haven't…" → "your site is ready to…").

## First-success milestone

**Job**: they published — celebrate briefly, channel momentum into the next step.
**Budget**: under 90 words. **Mechanism**: workflow, event trigger `firstPublish`, immediately.
**Subject**: "Your site is live".

Structure: state the fact ("{siteName} is live") → one next action (share it, connect a domain, add CMS) → one button. This is the one email type where warmth peaks — still no exclamation marks; the checkmark energy, not the confetti.

- DO make the next action concrete and adjacent (custom domain after publish).
- DON'T stack three next steps, DON'T emoji (the cohort's consumer tools do; Framer doesn't).

## Changelog / digest

**Job**: recurring "what shipped" at a fixed cadence.
**Budget**: 2–3 sentences per item, 3–5 items, under ~180 words total including the TL;DR. **Mechanism**: campaign, fixed cadence (monthly like Raycast, or per-release), consistent subject prefix.
**Subject**: house prefix is “New in Framer: {headline feature}” (“Changelog: …” is Linear's pattern — calibration only). The prefix is the promise; keep it identical every send. Inline links may target the specific framer.com/updates post — the deeplink rule applies to buttons.

Structure: optional one-line TL;DR → items, each = bold heading + problem-or-capability sentences + inline "Learn more →" link (no buttons, or one at the very end) → optional community/human section if the brand allows.

- DO promise the contents and cadence at signup and never exceed them.
- DO lead each item with what the reader can now do.
- DON'T pad a thin month — skip the send instead ("the unsubscribe-proof strategy is not sending anything skippable").

## Trial / upgrade

**Job**: convert at the moment the value is proven.
**Budget**: under 110 words. **Mechanism**: workflow — trigger on hitting a real limit (event: page limit, bandwidth, CMS items, collaborators) or on trial-status change. Usage-triggered beats calendar-triggered, always.
**Subject**: the fact — "You've hit the page limit on Free".

Structure: the fact with the number (“Your site used 105 of 100 GB”) → what the next plan unlocks, priced plainly → one button. Day-before-expiry and renewal notices are transactional in **mechanism**, not just tone — they must reach unsubscribed contacts and state exactly what happens to their site. Only the upsell stays a marketing workflow; never combine the two in one send (transactional forbids marketing content).

- DO state price and what unlocks in the same breath — no “see plans” mystery.
- DON'T countdown-spam (“3 days left!!”), DON'T punish (“you exceeded”) — Framer's blameless rule applies to money most of all.

## Dunning

**Job**: recover a failed payment before the plan lapses.
**Budget**: under 80 words. **Mechanism**: workflow on payment-status → failed, 1–3 emails max; the final consequence notice is transactional.
**Subject**: the fact — “Your payment for Pro didn't go through”.

Structure: the fact, blamelessly (card declines are the card's fault) → the exact consequence and date (“your site unpublishes on {date}”) → one button to update the payment method.

- DO keep the register of the product's own billing copy: “Payment declined” energy, never alarm.
- DON'T stack urgency, DON'T send more than 3, DON'T bundle an upgrade pitch with a recovery email.

## Usage recap / milestone

**Job**: monthly mirror — turn usage into felt value (and quiet upgrade pressure).
**Budget**: short — the numbers are the copy. **Mechanism**: campaign to active segment, monthly.
**Subject**: "Your {Month} on Framer".

Structure: 3–4 stats (visitors, pages published, sites live) → one line of meaning → one button. Loom's model: usage converted into ROI language (“meetings avoided” → for Framer: “shipped without a developer”).

Stats must be synced to Loops as contact properties (e.g. `monthlyVisitors`, `sitesLive`) before this email can exist — there's no live lookup. Empty properties without fallbacks block the send per-contact; state the required properties in the spec rather than relying on them.

- DON'T send to users with empty stats — filter the segment; a zero recap is a churn letter.

## Winback

**Job**: lapsed users (30/60d inactive) — give a reason to return.
**Budget**: under 100 words. **Mechanism**: workflow on inactivity property/event, one email, maybe two.
**Subject**: what changed or what they own — "Your site is still live", "What's new in Framer since March".

Structure: lead with either (a) the best of what shipped since they left — a changelog excerpt, or (b) their own asset ("{siteName}.framer.website is still live") → one button back in.

- DO segment by lapse reason where known and answer the actual objection.
- DON'T "we miss you", DON'T discount as the opener, DON'T guilt.

## Transactional

**Job**: the app must tell them something. Magic links, publish confirmations, invites, renewals, comment notifications.
**Budget**: as short as truth allows. **Mechanism**: transactional API — no marketing content permitted, no unsubscribe footer, must be published before the API can send.
**Subject**: informative, front-loaded — "Your activation link for Framer", "Action needed: …" pattern for genuine action.

Structure: the fact → the constraint or consequence → the action. Framer's existing register is right: “Sign in to Framer using this link. It expires in one hour.” Data via `{DATA_VARIABLE:name}`.

- DO state expiries, dates, and consequences exactly (“renews on February 20, 2026”).
- DON'T smuggle in feature promotion — it's disallowed and it erodes the channel's deliverability.

### Required notices

Terms/policy updates, price changes, security incidents, and deprecations go **transactional** — they must reach unsubscribed contacts and contain zero promotion. Structure: what changes → exact effective date → what the user must do → link to the full text. Security incidents: what happened, what data, what Framer did, what the user should do — no reassurance adjectives. Deprecations: end date and migration path in line one.
