# Mechanics — typography & grammar

The rules below are mechanical and enforceable. When a punctuation or casing call is in doubt, this file decides it.

---

## Curly quotes & apostrophes

Use typographic (curly) characters in all user-facing copy. Never straight quotes.

| Use | Not | Example |
|-----|-----|---------|
| `’` apostrophe (U+2019) | `'` straight | `won’t`, `you’ll`, `couldn’t` |
| `‘` `’` single quotes (U+2018 / U+2019) | `'` `'` | `‘draft’` |
| `“` `”` double quotes (U+201C / U+201D) | `"` `"` | `“Pro”` plan |
| `…` ellipsis (U+2026) | `...` three dots | `Reason for cancellation…` |
| `—` em dash (U+2014) | `--` or hyphen | thoughts joined — like this |
| `–` en dash (U+2013) | hyphen | `9:00–11:00`, `5–10 items` |

The apostrophe is the one that bites most often: it’s the same character as a right single quote (`’`), so `won’t` is correct, `won't` is wrong.

### The important caveat — displayed text only

Curly characters belong in the **words the user reads**, not in code. Do **not** put curly characters in:
- Code identifiers, variable names, object keys.
- JSX attribute values that are props/config (`type="primary"`), URLs, or class names.
- **Translation keys** — the lookup string. If copy goes through a `<T>` / translatable system, the *key* often must stay ASCII; the curly character belongs in the *translated value*. Check how the surrounding strings are stored before changing one.

### Codebase reality

The Framer codebase is mid-migration: a lot of existing copy still uses straight quotes (and some uses `&rsquo;` / `&lsquo;` HTML entities). That’s legacy. Write **new** copy curly. When auditing, flag straight quotes as a fix — but if a single string sits in a file where changing it would mix encodings inconsistently, note the broader cleanup rather than leaving a lone mismatch. There is no lint rule enforcing this yet, so it’s on you.

### Producing the characters

Type the literal Unicode glyph directly in the string (`‘` `’` `“` `”` `—` `…`). In JSX text you can also use entities (`&rsquo;` `&ldquo;` `&rdquo;` `&mdash;` `&hellip;`) — match whatever the surrounding file already does.

---

## Balanced multiline copy

When a string wraps to multiple lines on purpose — Framer toasts and error/success cards split on `\n` and render with `white-space: pre-line` — make the lines **roughly equal width**. A long line stacked over a short orphan looks broken. Rebreak the sentence at a natural clause boundary so the block reads as a tidy shape.

Worked example — `“Only editors in this workspace can open this page.”`

```
Bad break (orphan):
  Only editors in this workspace can
  open this page.

Good break (balanced):
  Only editors in this workspace
  can open this page.
```

Technique:
1. Write the full sentence.
2. Find the midpoint by character count.
3. Move the `\n` to the nearest clause/preposition boundary so both halves are close in length.
4. If one option still orphans a word, reword slightly (“of 5 MB.” not “of 5MB max.”) to even it out — copy and layout are tuned together.

This applies to two-line toasts (primary/secondary are each one line, but a wrapping secondary should still balance) and to any hard-wrapped card body.

---

## Capitalization

Two casing systems, split by one rule — **names get Title Case, statements get sentence case.** This is Apple’s macOS logic (HIG, “Capitalization of Interface Element Labels and Text”) and it matches the vekter codebase (`label="First Name"`, `title="Aspect Ratio"`, menu `label: "Set Variant"`, `<T>Danger Zone</T>`).

### Title Case — anything that names something

| Surface | Verified codebase examples |
|---------|---------------------------|
| Page (h1) title | “General Workspace”, “Account Settings” |
| Section heading | “Danger Zone”, “Passkeys”, “Member Details” |
| Button | “View Invoices”, “Add Passkey”, “Sign Out”, “Manage Seats” |
| Field / control label | “First Name”, “Last Name”, “Language Name” |
| Form-group label | “Workspace Invites”, “Move Projects”, “Default Role for New Workspace Members” |
| Property-panel row | “Aspect Ratio”, “Offset Y”, “Time Zone” |
| Menu item | “Set Variant”, “New Page”, “Select All”, “View Analytics” |
| Tab label, table column header | “Pending Invites” |

Title Case rules: capitalize principal words; short prepositions, articles, and conjunctions (to, and, of, a, an, the, for, or) stay lowercase — `“Upgrade to Pro”`, `“Back to Plans”`, `“Switch to Yearly”`, never `“Upgrade To Pro”`.

| Title Case (do) | (don’t) |
|-----------------|---------|
| “Try Again” | “Try again” |
| “First Name” (field label) | “First name” |
| “Update Payment Method” | “Update payment method” |
| “Danger Zone” (section heading) | “Danger zone” |

### Sentence case — anything that says something

| Surface | Examples |
|---------|----------|
| Toast / message | “Payment already in progress” |
| Dialog body, helper/description text | “Deleting a project will delete it for all collaborators…” |
| Explanatory tooltip | “Additional editors are $20 / month.” |
| Empty state | “No projects” / “Create a project from scratch…” |
| Placeholder | “Enter a path…”, “My workspace”, “First name” (as example input) |
| Label that is a question or full sentence | “Who can join this workspace?” |

Note product names keep their caps inside a sentence-case string: `“Connect to the CMS”`, `“You are currently on a Free plan.”`

**The tiebreak test:** could the string be the *name* of the field, command, or place? Title Case. Is it *telling the user* something — describing, asking, reporting? Sentence case. A placeholder saying “First name” is sentence case (it’s example input), while the label above it is “First Name” (it names the field). In audits, flag violations in either direction; treat old sentence-case labels as legacy, like straight quotes.

---

## Periods

- **Full sentences** get a period: `“Deleting a project will delete it for all collaborators and cannot be undone.”`
- **Buttons, labels, headlines, short fragments** do not: `“Try Again”`, `“No projects”`, `“Copied API key”`.
- **Two-line toasts:** the secondary line usually completes a sentence and takes a period: `“Exceeded max file size”` / `“of 5 MB.”` The primary fragment doesn’t.

---

## Other punctuation

- **Exclamation marks:** essentially never. Success is conveyed by the result and the checkmark, not the `!`. (If you’re reaching for one, the copy is doing too much.)
- **Oxford comma:** always. `“Edit, delete, or archive.”`
- **Ellipsis `…`:** signals “this needs more input” on an action (`“Save as…”`, opening a dialog) or an in-progress state (`“Exporting…”`). Don’t use it for trailing-off tone.
- **Question marks:** fine in genuine questions (“Cancel download?”), but most dialog bodies are statements, not questions.
- **Ampersand `&`:** acceptable in tight button labels where it reads naturally: `“Confirm & pay”`.

---

## Pronouns

Aligned with Apple’s HIG (“Writing”): the interface is an instrument, not a speaker.

- **Never “we” / “us” / “our” in system messages.** It’s unclear who “we” is, and it turns a fact into an apology. `“Unable to load content”` or `“Couldn’t load your summary”` — not `“We’re having trouble loading this content.”` This applies to all errors, toasts, tooltips, and settings copy.
- **Possessives sparingly.** Drop “my/your” when context already establishes ownership: `“Favorites”`, not `“Your Favorites”`; `“Account”`, not `“My Account”`. Keep the possessive when it does real work — `“Your workspace has 8 editors”` distinguishes *this* workspace from the plan’s limit.
- **Pick one perspective and hold it.** If a flow says “your site,” it doesn’t switch to “my site” elsewhere. Framer copy addresses the user as “you”; the product itself has no first person.
- **The sanctioned exception:** a rare, sincere human moment — e.g. the high-stakes cancellation line `“Please don’t hesitate to contact us if we can do anything to keep Framer in your workflow.”` That’s a person talking, on purpose. Everything routine stays impersonal.

---

## Numbers, units, dates

- **Numerals** for quantities and limits: `“8 editors”`, `“5 MB”`, `“(500/1000)”`. Not “eight editors.”
- **Space before unit:** `“5 MB”`, `“105/100 GB”`.
- **Money:** `“$20 / month”` — spaced slash matches the codebase.
- **Dates spelled, not numeric:** `“Expires June 30, 2026”`. Avoid `“06/30/26”` (ambiguous, less human).
- **Counts in errors:** show current/limit so the number explains itself: `“(5/50)”`.
- **Avoid vague quantities:** never “soon,” “a lot,” “some,” “large” when a real number is available.
