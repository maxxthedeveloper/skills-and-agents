# The Framer email voice

How Framer sounds in the inbox. The base is the product voice — if `framer-ux-writer` is installed, read its `references/framer-voice.md` for the full portrait and string bank; if not, the "What carries over unchanged" list below is the complete inherited rule set.

## What carries over unchanged

Everything mechanical and most of the temperament:

- **Curly quotes and real dashes** — `’` `“` `”`, em `—`, en `–`, ellipsis `…`. Never straight quotes or `--` in email copy.
- **Sentence case everywhere** — subjects, headings, buttons. Capitalize first word and proper nouns (Framer, Agents, CMS, Pro, CanvasBench, Fable 5). Stricter than the product here: framer-ux-writer accepts Title Case buttons in Studio; email buttons are always sentence case (“Try it in Framer”, never “Try It In Framer”). Intended divergence, not drift.
- **Confident, not boastful.** Capability stated as fact. Specificity does the convincing, not adjectives.
- **Outcome-first.** Lead with what the user gets. "Design entire pages with Fable 5" before any model detail.
- **Blameless.** Even a dunning or limit email states the fact and the path out, never fault.
- **Contractions.** "you'll", "we've", "doesn't". Human register.
- **Specific over vague.** Real numbers, dates, names: "71% on CanvasBench", "renews February 20, 2026" — not "top scores", "soon".
- **Banned words** (canonical list — the checklist fails on these): easy, simple, just, simply, oops, uh-oh, awesome, amazing, incredible, powerful, revolutionary, leverage, utilize, seamless-as-filler. Also banned in email: "we're excited/thrilled" and any excitement-opener, "exciting news", "don't miss out", "act now", any urgency theatre.
- **No exclamation marks.** The moment carries itself.

## What email adds

The inbox allows one register shift the product UI doesn't: the email is *from* someone (the team) *about* something that happened. So:

- **"We" is allowed and useful.** The strongest line in the cohort's model announcements is first-person and hands-on: "We've found it strongest at…". Framer's current emails never do this — the refresh adds it. One "we" observation per email, earned by actually having used the thing.
- **One concrete number is encouraged.** A benchmark, a price, a speed. Cursor states the model slug and price; Cognition states the benchmark score and quota. Framer states the CanvasBench score. One number — a second number starts a spec sheet.
- **One beat of narrative is allowed.** A changelog item may open with the problem before the capability (Linear: "Important team context doesn't always belong in a specific issue…" → the feature). Announcements may carry one sentence of why-this-matters. Never more than a beat.
- **Slightly longer sentences.** Product copy caps around 20 words; email body sentences can breathe to ~25 when carrying a real idea. Paragraphs stay 1–3 sentences.

## What email refuses

- **No greeting by default.** Framer's convention is to open with the heading, not "Hi there". A greeting is acceptable only when the email genuinely invites a reply (a survey, a beta invite asking for feedback) — and then it's "Hi there," never `{firstName}` theatre.
- **No sign-off.** Current Framer convention: the email ends on the CTA or last line, no "— The Framer Team". Add a sign-off only if the email asks for replies, and then it's "— The Framer team".
- **No first-name tokens as fake warmth.** Personalization is behavioral (what they built, what they hit, what changed for them), not mail-merge. Use `{firstName | there}` only where a human would actually use the name.
- **No marketing-page punch.** Homepage swagger belongs on framer.com — and its old "Not just vibes, a full platform" line is a negation-pivot, now a catalogued AI tell anyway (see `ai-tells.md`). Email is quieter: it informs someone who already chose Framer.

## Calibration bank A — Framer's own best email lines (keep this register)

- "Introducing Framer 3.0" / preview: "With Agents, Branching, Community, and an all-new design." — flat declarative subject, preview does the enumeration.
- "Agents bring AI to the canvas, and can design entire pages, iterate with you, make breakpoints, add effects, create components, write code, connect to the CMS…" — parallel verbs, capability as plain list.
- "Create a branch, experiment, review the changes, compare versions, and merge when the work is ready." — pure verb rhythm, no adjectives.
- "Join us on June 16 at 10 AM PDT as we unveil the future of designing." — specific date/time, one ambitious clause, stops.
- "Submit your site by January 30 and vote for your favorites." — instruction + date, no pleading.
- "Sign in to Framer using this link. It expires in one hour." — transactional register: fact, constraint, done.

## Calibration bank B — the target register (Cursor/Cognition moves Framer should adopt)

- "Cursor now supports Claude Fable 5, Anthropic's most powerful generally-available model." — line one names the thing, apposition does the positioning. (Borrow the apposition, not "powerful" — banned; Framer says "most capable".)
- "We've found it to be exceptional at long-running tasks, making it great for multi-step projects." — hands-on credibility, no benchmark needed. (Borrow the "We've found…" opener; cut the ", making it great for…" tail — that's a participial benefit tail, see `ai-tells.md`.)
- "On CursorBench, Opus 4.7 is a meaningful jump in capabilities, clearing 70% versus Opus 4.6 at 58%." — one comparative number, named benchmark.
- "Use this model when you need Devin to thoroughly investigate an issue, like a tricky bug or a new codebase." — when-to-use guidance instead of superlatives.
- "Through August 31, Sonnet 5 will use roughly 30% less quota than Sonnet 4.6." — the practical detail, dated and exact.
- Linear, changelog item shape: problem sentence → "You can now…" — capability framed as the reader's new ability, not the company's shipment.

## The test

Before delivering, hold the draft against both banks: **could this sit in Cursor's send queue without embarrassment, and in Framer's without sounding borrowed?** Louder than bank A = cut adjectives. Vaguer than bank B = add the number or the hands-on line. If it reads like a landing page, it fails; if it reads like a toast, it's underdressed — email is the register in between.
