# Checklist & audit rubric

Use this every time. In **Audit** mode, score each string against it and report failures. In **Write** mode, run it on your own draft before delivering.

A string passes only if every applicable line passes. Any fail is a defect to fix, not a preference.

## Mechanics (always applies)

- [ ] **Curly quotes** — all apostrophes and quotes are `‘` `’` `“` `”`, never straight `'` or `"`. (Displayed text only; not code/translation keys.) Run `scripts/check-copy.sh` on drafted strings to catch these deterministically.
- [ ] **Dashes** — em `—` / en `–` where used, never `--`. Ellipsis is `…`, not `...`.
- [ ] **Casing split** — names and fragment titles get Title Case, full sentences get sentence case. Title Case: titles (page h1 + section headings), **error/success/empty-state titles that are fragments** (`“Payment Declined”`, `“Editor Limit Reached”`, `“No Access”`), buttons, **field/control labels**, form-group labels, menu items, property rows, tabs, column headers (`“Account Settings”`, `“Danger Zone”`, `“First Name”`, `“Set Variant”`) with small words lowercase (`“Upgrade to Pro”`, `“Payment in Progress”`). Sentence case: dialog/toast bodies, helper text, tooltips, placeholders, option labels, and any string that is a question or full sentence (`“Who can join this workspace?”`). Titles should be fragments — rewrite sentence titles (`“You don’t have access”` → `“No Access”`), don’t re-case them. Flag violations in either direction.
- [ ] **Periods** — present on full sentences, absent on buttons/labels/fragments.
- [ ] **No exclamation marks** (unless a truly exceptional, sincere case — default is none).
- [ ] **Oxford comma** in any list of three or more.
- [ ] **Multiline balance** — if it wraps (`\n` / pre-line), the lines are roughly equal width with no orphan word.
- [ ] **Numbers/dates** — numerals + spaced units; dates spelled (`June 30, 2026`); concrete, not vague.

## Voice (always applies)

- [ ] **Blameless & constructive** — no fault placed on the user (“you exceeded,” “invalid,” “illegal”). States the fact + the path out, and frames the fix as a positive instruction (“Choose a password with at least 8 characters,” not “Password too short”).
- [ ] **Outcome-first** — leads with what the user gets / what happened, not the system’s internal action.
- [ ] **No banned words** — easy, simple, just, simply, oops, uh-oh, awesome, amazing, leverage, utilize. No “Error:” prefix or error codes.
- [ ] **No AI-giveaway constructions** — no negation-pivot (“It's not just X — it's Y”), participial benefit tail (“…, ensuring your site stays fast”), equal-length triad (“Fast. Flexible. Free.”), self-answering question, or copula dodge (“boasts” for “has”). Never two em dashes in one string. Catalog in `ai-tells.md`; `check-copy.sh` catches the mechanical ones.
- [ ] **Impersonal system voice** — no “we”/“us”/“our” in errors or system messages (“Couldn’t load content,” not “We’re having trouble…”); possessives only where they disambiguate (“Favorites,” not “Your Favorites”). Sole exception: a deliberate, sincere human moment (see mechanics — pronouns).
- [ ] **Contractions** — uses them; reads human, not stiff.
- [ ] **Spare** — every word earns its place; no hedging (“might,” “could try to”), no padding.
- [ ] **Length** — within the surface’s budget (see the budget line per surface in `patterns.md`).
- [ ] **Could it join Bank B?** — sits comfortably next to the real strings in `framer-voice.md`.

## By surface

**Button / action**
- [ ] Starts with a verb; object named if the verb alone is ambiguous.
- [ ] No `-ing`. Not “OK,” “Submit,” “Yes.”
- [ ] Unambiguous read in isolation — makes sense without the title, and a pair never makes one label mean two things (“Keep downloading” / “Stop,” not “Cancel” / “OK”).
- [ ] Reflects the post-click result, not the current state.
- [ ] Destructive buttons name the destructive act (“Delete project,” not “Confirm”).

**Error / failure toast**
- [ ] Primary line = the fact, neutral, a Title Case fragment (`“Payment Declined”`). Secondary line = recovery or concrete detail, sentence case.
- [ ] Answers the three questions: what happened, why it happened, what to do now. The “why” isn’t silently dropped.
- [ ] Names the specific object when more than one referent is possible (“My Portfolio,” not “this project”).
- [ ] Recovery is specific when the fix is known (“Update Payment Method”), not generic.
- [ ] “Couldn’t” for failed attempts; “Can’t” for not-allowed.

**Success toast**
- [ ] States the result and stops. Past-tense verb + object for project actions.
- [ ] No exclamation mark; surfaces the next opportunity only if one genuinely exists.

**Empty state**
- [ ] Headline names the emptiness — Title Case fragment, no period (`“No Projects”`). Body guides forward or explains what appears here.
- [ ] At most one CTA, verb-first.

**Confirmation dialog (destructive)**
- [ ] States exactly what happens, future tense, including the irreversible part.
- [ ] Doesn’t hide or soften consequences. Confirm button = the verb.

**Tooltip / helper / placeholder**
- [ ] One job. Concrete fact (price, limit, date) over vague gesture.
- [ ] Placeholder shows expected input or a real example, not a restated label.

**Plan / billing**
- [ ] Neutral and precise; never punitive about money or limits.
- [ ] Explains *why* an action is unavailable in terms of the user’s setup.
- [ ] No fake/disabled CTA where there’s no action — say the informational thing plainly.

## Audit output format

For each failing string:

```
String:   "<original>"  (file:line if known)
Fails:    <which checklist items, one short clause each>
Rewrite:  "<fixed version>"
Why:      <one line>
```

Group by severity if there are many: mechanics defects (curly quotes, casing) first, then voice/blameless issues, then surface-specific.
