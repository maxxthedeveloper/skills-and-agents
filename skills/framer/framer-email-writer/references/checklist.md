# Checklist & audit rubric

Use this every time. In **Audit** mode, score each email against it and report failures. In **Write** mode, run it on your own draft before delivering. An email passes only if every applicable line passes — any fail is a defect to fix, not a preference.

## Mechanics (always applies)

Run `scripts/check-copy.sh` on the draft first — it catches the character-level items deterministically; fix every hit. The judgment items stay manual.

- [ ] **Curly quotes & dashes** — `‘` `’` `“` `”`, em `—` / en `–`, ellipsis `…`. Never straight `'` or `"`, never `--`.
- [ ] **Sentence case** — subject, headings, and buttons: first word + proper nouns only (Framer, Agents, CMS, Pro, CanvasBench, Fable 5).
- [ ] **Periods** on full sentences; none on buttons, subjects, or fragments.
- [ ] **No exclamation marks.** No emoji anywhere (subject or body).
- [ ] **Oxford comma** in lists of three or more.
- [ ] **Numbers and dates concrete** — "renews February 20, 2026", "71% on CanvasBench", "(105/100 GB)". Never "soon", "big improvement".

## Email mechanics (always applies)

- [ ] **Subject under 60 characters, key noun in the first ~35** (mobile truncation), present tense, no personalization tokens, no clickbait. Information scent: the reader knows what's inside before opening.
- [ ] **Preview text present, 35–90 characters, front-loaded** and distinct — continues the subject, never repeats it, never left to default to the first body line by accident.
- [ ] **One primary CTA.** Announcements/lifecycle: exactly one button. Changelogs/digests: inline `→` links, at most one button at the end. No two buttons competing (a stacked secondary is allowed only with explicit reason).
- [ ] **CTA is a deeplink** — buttons land in the relevant place in Framer (the project, the Agents panel, the plan page), not the homepage. Changelog/digest inline links may target the specific framer.com/updates post.
- [ ] **Every variable has a fallback** — `{firstName | there}`, `{EVENT_PROPERTY:siteName | your site}`. A marketing email with an unfilled, fallback-less variable silently doesn't send.
- [ ] **Send mechanism stated** — campaign (+ audience/segment), workflow (+ trigger, timers, filters), or transactional. Transactional contains zero marketing content.
- [ ] **No hand-written footer** — Loops appends address + unsubscribe on marketing email.
- [ ] **No shortened youtu.be links** (deliverability) — full URL, untracked, or the framer.com page that embeds the video.
- [ ] **Every image has alt text**, and no essential copy lives only inside an image.
- [ ] **Word budget met** — model release 45–110; feature <150; onboarding <120; trial/upgrade <110; nudge/winback <100; milestone <90; dunning <80; changelog <180 total. Exact numbers live in `email-types.md`. Over budget = the email is saying two things.

## Voice (always applies)

- [ ] **No banned words** — canonical list in `email-voice.md` § What carries over (easy, simple, just, powerful, revolutionary, "we're excited", urgency theatre, …). `check-copy.sh` catches these.
- [ ] **No AI-giveaway constructions** — no negation-pivot ("It's not just X — it's Y"), participial benefit tail ("…, ensuring a seamless experience"), equal-length triad, staccato stack, self-answering question ("The result? …"), false range ("From startups to enterprises"), or copula dodge ("boasts", "serves as"). Max 2 em dashes per email, never 2 in one sentence. Full catalog in `ai-tells.md`; `check-copy.sh` catches the mechanical ones.
- [ ] **Passes the competitor-swap test** — at least one product-specific observation that would be false or meaningless in a competitor's email. If every sentence could ship under another logo, it's slop.
- [ ] **Outcome-first** — leads with what the reader gets or can now do, not what the company shipped.
- [ ] **One credibility element** where the type calls for it (release/feature): a hands-on "we've found…" line or one concrete number. Not two numbers, not zero.
- [ ] **Blameless** — limits and billing framed as facts + path out ("You've hit the page limit" → what unlocks), never fault ("you exceeded").
- [ ] **Contractions** — reads human, not stiff.
- [ ] **Spare** — no greeting or sign-off unless the email invites replies; no padding, no hedging.
- [ ] **The calibration test** — could it sit in Cursor's send queue without embarrassment, and in Framer's without sounding borrowed? (Compare against both banks in `email-voice.md`.)

## By type (check the one that applies)

**Model/agent release** — line one names the model in Framer (never “Framer Agents” as a compound name); one credibility line (CanvasBench or hands-on); one practical detail; announcement post linked if Framer is mentioned in it.
**Feature announcement** — one feature; problem-or-capability opener; real product image; no bundled upgrade pitch.
**Welcome** — one first action; Linear-grade restraint (no feature lists, no tips); cadence expectations set if a digest exists.
**Activation nudge** — behavior-gated (filter excludes people who already did it); references their actual object; positive framing.
**Milestone** — states their fact; exactly one adjacent next step.
**Changelog** — consistent subject prefix; items lead with what the reader can now do; thin months skipped, not padded.
**Trial/upgrade** — triggered by a real limit or status change, not the calendar; price + what unlocks stated together; expiry/renewal notices sent transactional, not as marketing workflow.
**Dunning** — blameless fact + exact consequence date + one payment button; max 3 sends; no bundled upsell.
**Winback** — leads with what changed or what they own; no "we miss you", no guilt, no discount-as-opener.
**Transactional** — fact, constraint, action; exact dates/expiries; zero promotion. Required notices (terms, price changes, security, deprecations) are transactional so they reach unsubscribed contacts.

## Audit output format

For each failing email or line:

```
Email:    "<subject>" (type, mechanism)
String:   "<original line>"
Fails:    <checklist items, one short clause each>
Rewrite:  "<fixed version>"
Why:      <one line>
```

Group by severity: mechanics defects first, then email mechanics (subject/preview/CTA/variables), then voice, then type-specific. End with the sends-correctly check: would every email in the set actually deliver (fallbacks, mechanism, published transactional templates)?
