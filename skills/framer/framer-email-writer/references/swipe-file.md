# Swipe file — verbatim reference emails

Real product emails mined from Max's inbox (July 2026) plus the cohort research. Bodies are verbatim (tracking URLs stripped). Use as the offline fallback when the Gmail subagent is unavailable, and as the calibration bank in Audit mode. Quotes keep their original straight quotes — they're evidence, not Framer copy.

Contents: Framer baseline · Cursor · Cognition/Devin · OpenAI · Linear · Lovable · Vercel · Anthropic · cross-company patterns · the gap analysis.

---

## Framer — the current baseline (being refreshed)

Sent via Loops from `team@framer.com`, sender name "Framer". House pattern: small logo top-left → short bold heading (~16px) → 1–3 sentences of 14px body → one small blue (#0099ff) pill button → optional rounded full-width image → grey footer. No greeting, no sign-off, no `{firstName}`. Tersest of the entire cohort.

### "Introducing Framer 3.0" (2026-06-17, launch)
Preview: "With Agents, Branching, Community, and an all-new design."

> **Introducing Framer 3.0**
> With Agents, Branching, Community, and an all-new design. Read about everything we launched below or watch the launch video, and the full event to see everything that's new.
>
> **Agents**
> Agents bring AI to the canvas, and can design entire pages, iterate with you, make breakpoints, add effects, create components, write code, connect to the CMS, share site analytics, organize styles, and so much more. Learn more about Agents.
>
> **Branching**
> Create a branch, experiment, review the changes, compare versions, and merge when the work is ready. Teams can keep AI edits and production work separate. Learn more about Branching.
>
> **External Agents**
> Connect Claude Code, Cursor, Codex, or any AI to your Framer projects. Use your AI workflow while Framer stays the canvas, CMS, and publishing layer. Learn more about External Agents.
>
> **The New Framer Community**
> We've brought Marketplace, Gallery, Feed, Members, and Contests into one place. Discover work, share your own, meet other creators, and join contests from the new Framer Community. Join the new Community.

~200 words, sectioned, inline text links (no buttons per section). *Steal: the parallel-verb capability lists. Fix: no credibility lines, no numbers.*

### "Framer 3.0 is almost here" (2026-06-03, event teaser)
> **A peek into the future**
> Join us on June 16 at 10 AM PDT as we unveil the future of designing, followed by a 24 hour hackathon. Watch it live on framer.com or our YouTube channel.
>
> [Add to your calendar] ← blue pill button

~40 words, one CTA. *Steal: the whole shape — this is the house length.* (Note: YouTube link in email is a deliverability risk — link the page instead.)

### "Join the Framer Awards and win $10k" (2025-12-17, campaign)
Preview: "The Framer Awards are back with $100,000 in prizes"
> **The Framer Awards are back with $100,000 in prizes**
> Submit your site by January 30 and vote for your favorites. Winners take home $10k with a trophy, a Creator Micro 2 keyboard, and exclusive Framer merch.
>
> [Join the Awards]

### Transactional register (keep this exactly)
- Magic link: "Sign in to Framer using this link. It expires in one hour."
- Renewal: "This is a reminder that your Framer subscription will automatically renew on February 20, 2026. You can view, update, or cancel your subscription by clicking the button below."
- Comment: "Tito left a new comment in Dashboard Settings Redesign. '…' [View comment]"

---

## Cursor — the model-announcement masters

Two senders: "Cursor Team" (`team@mail.cursor.com`) and "Michael" (`michael@mail.cursor.com`, signs "Best, Michael & Cursor Team"). Plain-text look, one dark pill button (often a `cursor://` deeplink), orange inline links.

### "Try Claude Fable 5" (2026-06-09) ⭐ the exact genre
Preview: "Use Anthropic's most powerful model"
> Hi there,
>
> Cursor now supports Claude Fable 5, Anthropic's most powerful generally-available model.
>
> Fable 5 costs $10 / MTok input and $50 / MTok output. See how it stacks up against other models in our [evals].
>
> [Open Cursor]
>
> Fable 5 comes with new data privacy considerations, which you can read more about in our [docs].
>
> Best,
> Cursor Team

~60 words. *Steal: line-one apposition, price as the concrete detail, evals link.*

### "Opus 4.7 is out in Cursor with 50% off" (2026-04-16)
Preview: "A more autonomous and creative coding model."
> Hi there,
>
> Claude Opus 4.7 is now available in Cursor with 50% off for a limited time.
>
> We've found it to impressively autonomous and more creative in its reasoning. On CursorBench, Opus 4.7 is a meaningful jump in capabilities, clearing 70% versus Opus 4.6 at 58%.
>
> It comes with a new X-High effort level and the same per-token pricing as Opus 4.6. The default slug for this model is **claude-opus-4-7-thinking-high**.
>
> You can try it in Cursor now, or learn more in our [docs].
>
> [Try Opus 4.7 in Cursor]
>
> Best,
> Cursor Team

~90 words. *Steal: "We've found it…" + one benchmark comparison — the credibility one-two. (Shipped with a typo: "found it to impressively autonomous" — even the best ship typos; still, don't.)*

### "GPT-5.2 Codex is out in Cursor" (2026-01-14, minimal version)
Preview: "Run it for days to weeks on your most ambitious tasks."
> Hi there,
>
> GPT-5.2 Codex is now available in Cursor.
>
> We've found it to be exceptional at long-running tasks, making it great for multi-step projects that require sustained context and reasoning.
>
> You can try it with Agent in Cursor now.
>
> [Try in Cursor]
>
> Best,
> Michael & Cursor Team

~45 words — the floor of the genre. *Steal: hands-on line carries the whole email, no benchmark needed.*

### "Introducing Cursor 2.0 and Composer" (2025-10-30, big launch, ~260 words)
Preview: "Our first coding model and a new interface, both purpose-built for working with agents."
Sectioned: bold headings + screenshots. Openers worth keeping:
> Today, we're releasing our first agentic coding model and a new interface for working with many agents in parallel.
> Composer is a frontier model that is 4x faster than similarly intelligent models… completes most turns in under 30 seconds.
> We've even found that having multiple models attempt the same problem and picking the best result significantly improves the final output.
Ends with a bullet list of smaller items, download/changelog links, "- Cursor Team".

### Monthly changelog: "New in Cursor: Plan Mode, Slash Commands, and more" (2025-10-14)
"Hello, / It's been a busy month…" then 4 sections (bold heading + 1–2 short paragraphs + screenshot). Recurring voice move: "We've found that this allows agents to run for significantly longer." / "We've been using them for running linters, fixing compile errors, and creating PRs…". No buttons — inline links only. Ends "Let us know any feedback you have! / - Cursor Team".

**Cursor's model-announcement formula**: greeting → "X is now available in Cursor" → one hands-on eval sentence → one concrete spec (price / benchmark / slug) → deeplink CTA → sign-off. 45–90 words.

---

## Cognition / Devin

Sender: `theo@cognition.ai` (personal-name sender — Framer won't copy this). Black primary button + outlined secondary, stacked.

### "Claude Sonnet 5 is now available" (2026-06-30)
Preview: "Now available in Devin Desktop and CLI". No greeting, no sign-off.
> Claude Sonnet 5 is now available in Devin Desktop and Devin CLI.
>
> Sonnet 5 pairs frontier-level coding performance with a more affordable price point, making advanced coding models practical for everyday engineering work. On FrontierCode (Extended), our benchmark for real-world engineering tasks that grades mergeability and quality, Sonnet 5 scores 53.8% and has a 57.6% pass rate (higher than Opus 4.8).
>
> Through August 31, Sonnet 5 will use roughly 30% less quota than Sonnet 4.6. After that, it will use the same quota as Sonnet 4.6.
>
> We can't wait to see what you build!
>
> [Download Devin Desktop]
> [Try Devin Cloud]

~110 words — the ceiling of the genre. *Steal: benchmark named and explained in a clause; the dated quota detail.*

### "Fable 5 is back in Devin." (2026-07-02)
Preview: "Experience Claude Fable 5 with Devin today"
> Claude Fable 5 is back on Devin Cloud, Desktop, and CLI. You can access it from any of these platforms.
>
> Use this model when you need Devin to thoroughly investigate an issue, like a tricky bug, a new codebase he's not familiar with, or a complex workflow that requires significant computer work, such as integrating with MCP systems.
>
> In Devin Cloud, Fable 5 operates using the Ultra agent.
>
> [Try Fable 5 in Devin]
> [Download Devin Desktop]

~80 words. *Steal: when-to-use guidance instead of benchmarks — the alternative credibility move.*

### "Introducing Devin Fusion" (2026-06-29, agent-feature announcement, ~230 words)
Preview: "Frontier-level performance at 35% lower cost."
> Hi there,
>
> Today we're introducing Devin Fusion, a new hybrid-model harness for agentic coding.
>
> Fusion is designed to make Devin more efficient without sacrificing the quality needed for real engineering work. In testing, Fusion reduced the cost of frontier intelligence by 35% while maintaining performance.
>
> [chart image]
>
> The motivation is simple: not every step of an engineering task requires the most expensive model. …
>
> [Try Devin Fusion]
> …
> We'd love for you to put Fusion to work on real tasks and tell us where it breaks.
>
> The Cognition Team

*Steal: "the motivation is simple" problem-first paragraph; "tell us where it breaks" as the feedback ask.*

---

## OpenAI — "Introducing GPT-5.5" (2026-04-24, ~300 words)

Preview: "A new class of intelligence for real work". Designed: hero image, one centered black button "Read the Blog", bold-led capability sections ("Agentic coding:", "Knowledge work:", "Scientific and technical research:"), "—The OpenAI Team". Opens:
> We're excited to **introduce GPT-5.5**, our smartest and most intuitive to use model yet… GPT-5.5 is now available in the API, Codex, and ChatGPT.
> **It also uses significantly fewer tokens to complete the same tasks**, making it more efficient as well as more capable.

*Counter-example for Framer: "We're excited to" opener and 300-word length are what the formula exists to avoid. Steal only: bolding the one economic fact.*

---

## Linear

### "Welcome to Linear" (`notifications@linear.app`, 2026-06-23) ⭐ onboarding calibration
White card, arrow-suffixed links, one indigo button.
> **Welcome to Linear**
>
> At Linear, we believe software can feel magical. Well-designed tools and practices encourage momentum and level up execution in our teams.
>
> We're excited to welcome you to the Linear community. And we're committed to pushing our own limits so that we can help you reach yours.
>
> **Linear Method →** Why we built Linear and what we aim to do with the software.
> **Linear Guide →** Our documentation and tips on how to use the product better.
> **Linear Changelog →** We believe software should always improve. We share our new improvements and updates in our weekly changelog.
>
> Thanks for signing up. We're here to help you and your team. If you have any questions, contact us at hello@linear.app or on X.
>
> [Open Linear]

~150 words. The famous anti-onboarding: one email, three links, zero tips. *Steal: belief-first opener, arrow-link trio, philosophy sent after experience.*

### "Welcome to Linear Diffs Beta" (`changelog@updates.linear.app`, 2026-04-29)
Dated like a changelog entry, screenshot mid-body, no button, inline links. Opens:
> We're excited to invite your workspace to beta access of Linear Diffs.
> With Linear Diffs, you'll be able to read, review, and merge code end-to-end directly within Linear — without needing to switch tools.
Ends: "We'd love to hear how this is working for your team! Please share your feedback to support@linear.app."

Linear changelog subjects (real): "Changelog: Coding sessions in Linear", "Changelog: Team documents", "Changelog: Linear Diffs", "Changelog: Introducing Linear Agent" — label + colon + noun phrase, zero selling. Changelog items open with the problem: "Agents generate large volumes of code, but individuals are still accountable for the changes that merge." (→ Diffs).

---

## Lovable — changelog with embedded model announcement

"Lovable Update: Opus 4.6, a smarter agent & test environments" (`noreply@lovable.dev`, 2026-02-06, ~350 words). "Hey there, here's what's new in Lovable:", sections + "TRY THIS" callout box with a copyable prompt, one black button "Start building" at end. Model item:
> **Now powered by Claude Opus 4.6**
> Claude Opus 4.6 is now a core model in Lovable. It scores 21% higher on our app building benchmark, runs twice as long on complex tasks, and is noticeably stronger on design-heavy work like landing pages and marketing sites. Read more

Subject-line style, benefit-first and "your"-led: "Your builds just got a lot faster", "Your app can take payments now", "The Lovable mobile app is here". *Steal: the TRY THIS box — a copyable prompt is a great CTA for an agent product.*

---

## Vercel — "Persistent sandboxes and Docker support" (`ship@info.vercel.com`, 2026-06-05)

Monthly product update, ~400 words: TL;DR paragraph up top → sections ending "Read the changelog →" / "Join the waitlist →" → "Other reading" list → events block. Representative:
> Sandboxes now save and restore filesystem state between sessions, so long-running, durable sandboxes resume where you left off. This means teams no longer need to re-run setup steps or rebuild from scratch each time.

*Steal: TL;DR-first digest structure; capability sentence → "this means" consequence sentence.*

---

## Anthropic — notice tone (subjects/previews)

- "[No Action Required]: Higher rate limits on the Claude API" / preview: "Your rate limits are increasing, and usage tiers are getting simpler. No action required."
- "Your Claude API prompt cache hit rate is low" — proactive, personalized savings framing.

*Steal: stating "no action required" in the subject — respect for attention as a feature.*

---

## Cross-company patterns (the distillation)

1. **Model announcements are the shortest genre (45–110 words)**: "X is now available in [product]" → one credibility line (hands-on eval or one benchmark) → one practical detail (price/quota/slug/agent) → single deeplink CTA. Devin adds when-to-use guidance; Cursor adds a docs/evals link.
2. **Preview text = one crisp benefit sentence, always distinct from the subject.**
3. **Subjects plain, present-tense, no emoji, no exclamation**: "Try Claude Fable 5", "Claude Sonnet 5 is now available", "Introducing Framer 3.0".
4. **Sign-offs vary; Framer currently has none** — keep none.
5. **One primary CTA max**; changelogs use zero buttons and inline links.
6. **No adjectives**: "powerful", "seamless", "revolutionary" never appear in Cursor/Linear sends. Version numbers and plain nouns as headlines.
7. **Restraint is positioning**: Linear's one-email onboarding; Cognition barely emails at all. Low frequency, high signal — never send anything skippable.

## The gap analysis — Framer baseline vs the target

Framer is already the tersest sender in the cohort. The refresh is not about length — it's about adding four moves the baseline lacks:

| Missing from Framer today | The move | Source |
|---|---|---|
| Credibility line | One first-person, hands-on sentence: "We've found it…" | Cursor |
| Concrete number | One benchmark/price/spec per email (CanvasBench for models) | Cursor, Cognition |
| Deeplink CTA | Button opens the relevant place in Framer, not the homepage | Cursor's `cursor://` |
| Preview text discipline | Written deliberately, continues the subject | whole cohort |

Keep from the baseline: the no-greeting/no-sign-off shape, the ~40-word floor, the parallel-verb lists, the single blue button, the blameless transactional register.
