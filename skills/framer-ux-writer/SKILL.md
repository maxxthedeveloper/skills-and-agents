---
name: framer-ux-writer
description: Write and audit in-product UX copy for Framer Studio in Framer's house voice — button labels, error and success toasts, empty states, confirmation dialogs, tooltips, placeholders, and plan/billing messaging. Use when writing or reviewing any user-facing interface text in the Framer (vekter) codebase, or when the user mentions UX copy, microcopy, error messages, button text, empty states, or toast copy. For marketing pages (homepage, pricing, landing) use the copywriter skill instead. For emails Framer sends (announcements, onboarding, lifecycle, transactional) use framer-email-writer.
metadata:
  related_skills: framer-email-writer, copywriter, web-typography, humanize-ai-content
---

# Framer UX Writer

You write and audit the words inside Framer Studio. Not marketing — the interface itself: the toast when a publish fails, the button that cancels a plan, the empty state before the first project. This copy is part of the product’s craft. Treat every word as designed.

Assume you already know general UX-writing. This skill exists to make copy sound like **Framer specifically**, and to enforce a few mechanical rules the team cares about.

## Two modes

**Write** — generate new copy.
1. Get just enough context: What surface (toast, button, modal, empty state)? What just happened? What can the user do next? What’s the emotional moment (routine, blocked, relieved, about to lose something)?
2. **Always** spawn the reference subagent (see “Learn from design-forward companies” below) to pull how design-forward products word this same surface. Do this early — kick it off right after step 1 so it runs while you gather context.
3. Draft 2–3 options. Keep them tight. Let the references inform *structure and microcopy patterns*, but Framer’s own voice (`references/framer-voice.md`) always wins — never copy another brand’s tone.
4. Recommend one and say why in a line. Show the multiline break (`\n`) explicitly if the surface wraps.

**Audit** — review existing copy.
1. Score each string against `references/checklist.md`.
2. List what fails and why (cite the rule).
3. Rewrite the failures. Show before → after.

In **Audit** mode, the reference subagent is optional — spawn it when a string feels weak and you want to see how strong products handle the same moment, or when the user asks for references. In **Write** mode it is mandatory.

If the request is marketing copy (homepage, pricing, landing, feature pages), stop and hand off to the `copywriter` skill — different voice, different rules. If it's an email Framer sends, hand off to `framer-email-writer`.

## Learn from design-forward companies (always)

Before drafting, study how the best products word this exact surface. Spawn a subagent (Agent tool, `general-purpose`) that uses the **Mobbin MCP** to find and read real references, so your copy is calibrated against the current bar — not written in a vacuum.

Give the subagent this brief:

> You are gathering UX-copy references for a Framer Studio interface string. Surface: **{toast / button / empty state / confirmation dialog / tooltip / placeholder / plan-billing}**. Situation: **{what just happened + what the user can do next + the emotional moment}**.
>
> Load the tools first with ToolSearch: `select:mcp__mobbin__search_screens,mcp__mobbin__search_flows` — they may be deferred and error until loaded. Use `mcp__mobbin__search_screens`, and `mcp__mobbin__search_flows` for multi-step moments like onboarding/checkout/cancellation. Search `platform: "web"` first; add an `ios` pass if the surface is common on mobile. Inspect at least 6–8 screens across your queries before distilling. Run 2–3 focused queries describing the *screen and its situation* (e.g. “empty state before first project with a create button”, “subscription cancellation confirmation dialog”, “file upload error toast”). Favor design-forward products — Linear, Vercel, Stripe, Notion, Raycast, Arc, Figma, Superhuman, Height, Framer itself, and similar craft-led tools; you can name an app in the query to filter to it.
>
> **Examine the returned images and read the actual on-screen words** — do not infer copy from metadata. Extract the *verbatim microcopy* for the matching surface (primary line, secondary line, button labels).
>
> Return a compact digest, nothing else: 5–10 reference strings, each as `App — “verbatim copy”` with a one-clause note on why it works (structure, verb choice, how it frames the fix), and the screen’s `mobbin_url` as a markdown link. Group by primary line / secondary line / buttons if useful. No preamble, no restating the task.

When it returns: mine the references for *patterns* — how they structure the two-line toast, which verb they put on the button, how they frame a blocked moment blamelessly. Then write in **Framer’s** voice and enforce every non-negotiable. If the references clash with Framer’s rules (Title-case everything, marketing hype, straight quotes), Framer wins. Cite a couple of the strongest references to the user alongside your draft so they see the calibration.

If Mobbin returns nothing useful or the MCP is unavailable, say so in one line and proceed from `references/framer-voice.md` — don’t block the copy on it.

## The Framer voice, in one breath

Confident, designerly, outcome-first, warm but spare. You’re talking to practitioners who build for the web and value **control** and **speed**. Lead with what the user gets, not what the system did. State things as fact — no hedging, no hype, no apology theatre. Never “easy,” “simple,” “just,” “oops,” or “awesome.” When in doubt, cut a word.

Read `references/framer-voice.md` for the full portrait and a bank of real Framer strings to pattern-match against.

## Non-negotiables

These are always in force, in both modes. Violating one is a defect.

1. **Curly quotes & dashes.** Use `‘` `’` `“` `”` — never straight `'` or `"`. Use real em (`—`) and en (`–`) dashes, never `--`. So: `won’t`, `you’re`, `“Pro”`. The codebase is mid-migration and still has straight quotes in many places — new copy is curly. Be careful: this applies to *displayed text*, not code identifiers, JSX attributes, or translation **keys**. See `references/mechanics.md`.

2. **Balanced multiline copy.** When copy wraps to multiple lines (toasts and error cards use `\n` with `white-space: pre-line`), tweak the wording so the lines are roughly equal width. Never leave a long line stacked over a one-word orphan. Rebreak the sentence, don’t just let it flow.
   - Bad: `“Only editors in this workspace can\nopen this page.”`
   - Good: `“Only editors in this workspace\ncan open this page.”`

3. **Casing split: names get Title Case, statements get sentence case.** A string that *names* something is Title Case; a string that *says* something is sentence case (Apple’s macOS logic, and verified against the vekter codebase).
   - **Title Case:** page (h1) titles (`“Account Settings”`), section headings (`“Danger Zone”`, `“Passkeys”`), buttons (`“View Invoices”`, `“Add Passkey”`, `“Try Again”`), **field and control labels** (`“First Name”`, `“Aspect Ratio”`, `“Workspace Invites”`), menu items (`“Set Variant”`, `“New Page”`), tab labels, table column headers. Small words (to, and, of, a, the) stay lowercase: `“Upgrade to Pro”`, `“Back to Plans”`.
   - **Sentence case:** anything phrased as a statement or question — toasts (`“Payment already in progress”`), dialog bodies, helper/description text, tooltips that explain, empty states (`“No projects”`), placeholders (`“Enter a path…”`, `“My workspace”`), and labels that are full sentences or questions (`“Who can join this workspace?”`, `“Automatically hide toolbar”`).
   - The test: could it be the *name* of the thing? Title Case. Is it *telling you* something? Sentence case. Flag violations in either direction in audits.

4. **Blameless and constructive.** Never put fault on the user. State the fact, then the path out — and frame the fix as a positive instruction (what *to* do), not what went wrong.
   - Not `“You exceeded the editor limit”` → `“Editor limit reached”`.
   - Not `“Invalid code”` → `“Promotion code didn’t work”`.
   - Not `“That password is too short”` → `“Choose a password with at least 8 characters”`.

5. **Action-verb buttons.** Start with the verb, name the object when it isn’t obvious: `“Subscribe”`, `“Upgrade to Pro”`, `“Cancel Plan”`, `“Try Again”`. Never `“OK”`, `“Submit”`, `“Yes”`. No `-ing` forms (`“Cancel”`, not `“Cancelling”`). A button must make sense read on its own, without the title — and in a pair, never let one label mean two things (a “Cancel download?” dialog gets `“Keep downloading”` / `“Stop”`, not `“Cancel”` / `“OK”`).

6. **Restrained punctuation.** Full sentences get periods; labels and buttons don’t. Exclamation marks: essentially never (lean on the checkmark, not the `!`). Oxford comma always.

7. **Contractions, yes.** `“don’t”`, `“couldn’t”`, `“you’ll”`. Human register, never stiff.

8. **Specific over vague.** Real names, numbers, dates: `“Expires June 30, 2026”`, `“of 5 MB”`, `“(8/100)”`. Not `“soon”`, `“large”`, `“some”`.

9. **Impersonal system voice — no “we,” pronouns sparingly.** The product states facts; it doesn’t speak as a company. Never “we”/“us”/“our” in errors or system messages — `“Couldn’t load content”`, not `“We’re having trouble loading this content”`. Use possessives only when needed to disambiguate: `“Favorites”` over `“Your Favorites”`, but `“Your workspace has 8 editors”` is fine because the possessive does real work. One sanctioned exception: a sincere human moment like high-stakes cancellation (`“…contact us if we can do anything…”`) — deliberate, rare, and only where a human is genuinely behind it.

10. **No AI-giveaway constructions.** No negation-pivot (`“It's not just X — it's Y”`), no participial benefit tail (`“…, ensuring your site stays fast”`), no equal-length triads (`“Fast. Flexible. Free.”`), no self-answering questions, no copula dodges (`“boasts”` for `“has”`). Never two em dashes in one string. Catalog and rationale in `references/ai-tells.md`; `scripts/check-copy.sh` catches the mechanical ones.

## The two-line toast pattern

Framer’s toasts and error/success cards are usually two lines: **primary** (what happened) + **secondary** (the detail or the next step). Both lines balanced (rule 2). Examples from the product:

- `“Exceeded max file size”` / `“of 5 MB.”`
- `“Couldn’t load your summary”` / `“Check your connection and try again, or contact support.”`
- `“Payment already in progress”` / `“Complete it in your other tab, or close it to start over.”`
- `“Editor limit reached”` / `“Your workspace has 8 editors, more than this plan allows.”`

Single-line is fine for simple successes: `“Archived My Portfolio.”`, `“Copied API key”`.

## References — load when relevant

- `references/framer-voice.md` — tone profile + bank of verbatim Framer strings (marketing and in-product). Read before any Write task to calibrate.
- `references/patterns.md` — per-category playbooks (errors, success, empty states, buttons, confirmations, tooltips, placeholders, plan/billing) with real DO/DON’T pairs. Read for the surface you’re writing.
- `references/mechanics.md` — quotes, dashes, capitalization, the multiline-balance technique, periods, numbers, dates. Read when a typography/grammar call is in question.
- `references/ai-tells.md` — the AI-giveaway catalog for microcopy: banned constructions (negation-pivot, participial tails, triads), the dated word layer, and what makes a string read human. Skim before Write tasks; cite it when auditing.
- `references/checklist.md` — the pass/fail rubric. Read every time in Audit mode; skim before delivering in Write mode.
- `scripts/check-copy.sh` — deterministic mechanics check (straight quotes, `--`, `!`, banned words, emoji). Run it on drafted strings; fix every hit.

## Before you deliver

Self-check against the non-negotiables. Re-read your own copy as if it were the codebase you’re about to fail in review: curly quotes? balanced lines? casing split (Title Case for names — titles, buttons, labels, menu items; sentence case for statements)? blameless? verb-first buttons? If any answer is no, fix it before showing the user.
