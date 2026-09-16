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

One casing system — **sentence case, on every surface.** Capitalize the first word and proper nouns; everything else is lowercase. There is no Title Case tier for buttons, headings, labels, or titles.

### What still gets a capital

- **First word** of the string: `“Try again”`, `“No projects”`.
- **Product, plan, and feature names:** `Framer`, `Pro`, `Free` (as a plan name), `CMS`, `API`, `Analytics` (the add-on). `“Upgrade to Pro”`, `“Copied API key”`, `“Connect to the CMS”`, `“You are currently on a Free plan.”`
- **Names the user typed:** project, workspace, and collection names appear exactly as entered: `“Archived My Portfolio.”`
- **Acronyms and units:** `SEO`, `URL`, `MB`, `GB`.

### Do / don’t, across surfaces

| Surface | Sentence case (do) | Title Case (don’t) |
|---------|--------------------|--------------------|
| Page (h1) title | “Account settings”, “General workspace” | “Account Settings” |
| Section heading | “Danger zone”, “Member details” | “Danger Zone” |
| Button | “Try again”, “View invoices”, “Update payment method” | “Try Again”, “Update Payment Method” |
| Field / control label | “First name”, “Aspect ratio”, “Time zone” | “First Name” |
| Form-group label | “Workspace invites”, “Default role for new workspace members” | “Workspace Invites” |
| Menu item | “Set variant”, “New page”, “View analytics” | “Set Variant” |
| Error / success / empty-state title | “Payment declined”, “Editor limit reached”, “No access”, “Add-on not available” | “Payment Declined”, “Add-On Not Available” |
| Tab label, table column header | “Pending invites” | “Pending Invites” |
| Button with a product name | “Upgrade to Pro”, “Back to plans” | “Upgrade To Pro” |

Bodies, secondary toast lines, tooltips, placeholders, and option/checkbox labels were already sentence case and don’t change: `“Your workspace has 8 editors, more than this plan allows.”`, `“Automatically hide toolbar”`, `“Who can join this workspace?”`

**Titles are fragments, not sentences.** When a title wants to be a sentence, rewrite it into a short fragment: `“You don’t have access”` → `“No access”`, `“Still activating your plan”` → `“Activation in progress”`. A fragment title takes no period; a rare full-sentence title (`“Thank you.”`) keeps its period.

**Codebase reality.** The vekter codebase is mid-migration and still carries Title Case in many places (`label="First Name"`, `title="Aspect Ratio"`, `title="Payment Declined"`, `<T>Danger Zone</T>`). Treat these as legacy, like straight quotes: write new copy sentence case, and in audits flag Title Case as a mechanics defect. Don’t “match the neighbours” by adding new Title Case strings to a file that has them — note the broader cleanup instead.

---

## Periods

- **Full sentences** get a period: `“Deleting a project will delete it for all collaborators and cannot be undone.”`
- **Buttons, labels, headlines, short fragments** do not: `“Try again”`, `“No projects”`, `“Payment declined”`.
- **Two-line toasts:** the secondary line usually completes a sentence and takes a period: `“Editor limit reached”` / `“Your workspace has 8 editors, more than this plan allows.”` The primary fragment doesn’t.

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

- **Never “we” / “us” / “our” in system messages.** It’s unclear who “we” is, and it turns a fact into an apology. `“Unable to load content”` or `“Couldn’t load summary”` — not `“We’re having trouble loading this content.”` This applies to all errors, toasts, tooltips, and settings copy.
- **Possessives sparingly.** Drop “my/your” when context already establishes ownership: `“Favorites”`, not `“Your Favorites”`; `“Account”`, not `“My Account”`. Keep the possessive when it does real work — `“Your workspace has 8 editors”` distinguishes *this* workspace from the plan’s limit.
- **Pick one perspective and hold it.** If a flow says “your site,” it doesn’t switch to “my site” elsewhere. Framer copy addresses the user as “you”; the product itself has no first person.
- **The sanctioned exception:** a rare, sincere human moment — e.g. the high-stakes cancellation line `“Please don’t hesitate to contact us if we can do anything to keep Framer in your workflow.”` That’s a person talking, on purpose. Everything routine stays impersonal.

---

## Numbers, units, dates & time

### Numbers & measured units

- **Numerals** for quantities and limits: `“8 editors”`, `“5 MB”`, `“(500/1000)”`. Not “eight editors.”
- **Space before measured units:** `“5 MB”`, `“105/100 GB”`. Compact relative timestamps are the exception; see below.
- **Money:** `“$20 / month”` — spaced slash matches the codebase.
- **Counts in errors:** show current/limit so the number explains itself: `“(5/50)”`.
- **Avoid vague quantities:** never “soon,” “a lot,” “some,” “large” when a real number is available.

### Relative time

Framer Studio has a deliberate compact style for dense metadata. Use the style that fits the surface; don’t mix compact and expanded forms within one list.

- **Dense lists and metadata:** `“Just now”`, `“28m ago”`, `“1h ago”`, `“2d ago”`, `“1w ago”`, `“3mo ago”`, `“1y ago”`. No space before the unit, no plural `s`, and no period.
- **Ultra-dense badges:** omit the suffix when the context already establishes recency: `“28m”`, `“1h”`.
- **Sentences and roomy secondary copy:** spell out the unit: `“Updated 2 hours ago.”`
- **Named relative dates:** `“Yesterday”` is allowed only when the surface uses a calendar-aware formatter. Don’t hand-author it from elapsed hours, and don’t swap it into a surface backed by a numeric formatter.
- **Implementation reality:** existing Studio UI should prefer the shared `RelativeTime` component or `formatDistanceToNowShort`. That formatter is compact but doesn’t currently guarantee named dates or week units at every threshold; adding `“Yesterday”` or `“1w ago”` may require formatter work.
- **Accessibility:** render timestamps with semantic `<time dateTime="…">` markup and expose the full localized date and time in a tooltip or accessible label.

### Calendar dates

- **New compact UI:** use `“Jan 14, 2024”` in tables, lists, and metadata.
- **Full or high-stakes copy:** use `“January 14, 2024”`, as in `“Expires June 30, 2026”`.
- **No ordinals in new copy:** use `“Jan 14”`, not `“Jan 14th”`. Existing billing and tooltip strings with ordinals are legacy, not patterns to copy.
- **No ambiguous numeric dates:** avoid `“06/30/26”` and `“30/06/26”` in non-localized copy.
- **Include the year** for historical records and any list that can span years. Omit it only when nearby context makes the year unambiguous.
- **Localization:** use the viewer’s locale when the surface supports localization; don’t assemble localized dates from string fragments.

### Clock time

- **Exact time:** use `“4:30 PM”` in English UI—no leading zero, with uppercase `AM` or `PM`.
- **Ranges:** use an en dash with no spaces: `“9:00–11:00 AM”`.
- **Time zones:** include the zone when people in different zones could interpret the time differently. A timestamp explicitly shown in the viewer’s local time doesn’t need one.
