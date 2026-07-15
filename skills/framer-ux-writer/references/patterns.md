# Patterns by surface

Per-surface playbooks. Each is a short rule plus DO / DON’T pairs grounded in real Framer copy. Read the section for the surface you’re writing.

---

## Error & failure toasts

**Rule.** Name the fact neutrally, then give the recovery. Two lines: primary (what happened) + secondary (detail or next step). Blameless always. No error codes, no “Error:” prefix, no “Oops.”

**Budget.** Primary 2–5 words, no period; secondary one sentence.

| DO | DON’T |
|----|-------|
| “Couldn’t load prices” | “Error: failed to fetch pricing data” |
| “Payment declined” / “Update your payment method and try again.” | “Your payment was rejected” |
| “Editor limit reached” / “Your workspace has 8 editors, more than this plan allows.” | “You’ve exceeded the editor limit!” |
| “Promotion code didn’t work” / “This code is invalid or expired.” | “Invalid promo code” |
| “Couldn’t start your checkout” / “Try again, or contact support if this keeps happening.” | “Checkout initialization error” |

**Limit / capacity errors.** State the limit + the live count: `“Page limit exceeded”` / `“(5/50).”`, `“Bandwidth limit exceeded”` / `“(105/100 GB).”`. The number does the explaining.

**Notes.**
- “Couldn’t” for things the system tried and failed at; “Can’t” for things that aren’t allowed right now.
- Offer the action that fixes it, not generic “try again,” when you know the fix (e.g. an “Update Payment Method” button).
- Keep both lines balanced in width (see mechanics — multiline balance).

---

## Success / confirmation toasts

**Rule.** State the result plainly and stop. The accomplishment carries the emotion; you don’t need an exclamation mark.

**Budget.** Primary 2–5 words; optional secondary one sentence.

| DO | DON’T |
|----|-------|
| “Archived My Portfolio.” | “Successfully archived your project!” |
| “Updated to Pro” / “Your site subscription has been updated to a Pro plan.” | “Awesome! You’re now on Pro 🎉” |
| “Copied API key” | “API key copied to clipboard!” |
| “The invoice has been sent to your inbox.” | “Check your email for the invoice!” |

**Notes.**
- Project actions: past-tense verb + object — “Archived,” “Deleted,” “Unarchived,” “Left,” “Removed from [Workspace].”
- A genuine “Thank you.” is in-voice for moments like a completed upgrade. One period, no more.
- Surface the next opportunity when there is one: “You are now eligible to claim a free domain.” with an “Add Domain” action.

---

## Empty states

**Rule.** Headline names the emptiness (sentence case, no period). One line of body either guides the user to the first action or explains what will appear here. Optional single CTA, verb-first.

**Budget.** Headline 2–4 words; body one sentence.

| DO | DON’T |
|----|-------|
| “No projects” / “Create a project from scratch or use a template to get started.” | “Nothing here yet!” |
| “No archived projects” / “All archived projects will be listed here.” | “You have no archived projects at this time.” |
| “This project does not contain any code components.” / “Browse all code components and code overrides here.” | “No data” |

**Three flavors:**
- *First-run / actionable* — guide forward with a CTA (“Create a project…”).
- *Will-appear-here* — reassure nothing’s broken (“All archived projects will be listed here.”).
- *No-permission / no-results* — state the reason plainly (“You don’t have permission to create projects.” / “Try adjusting your search or browse workspaces.”).

---

## Buttons & actions

**Rule.** Verb first. Name the object when the verb alone is ambiguous. Title Case (small words lowercase — see mechanics). No `-ing`. Reflect what happens *after* the click, not the current state.

**Budget.** 1–4 words.

| DO | DON’T |
|----|-------|
| “Subscribe” · “Upgrade to Pro” · “Cancel Plan” | “OK” · “Submit” · “Yes” |
| “Try Again” | “Retry?” |
| “Update Payment Method” | “Payment” |
| “Add Domain” | “Domains” |
| “Confirm & Pay” | “Continue” |
| “Delete Project” | “Deleting…” (as a label) |

**Notes.**
- Destructive primary buttons name the destructive act: “Delete Project,” “Cancel Plan,” “Leave Project” — not “Confirm.”
- Pair the verb consistently with its object across the product. If it’s “Archive Project” in one place, it’s not “Move to Archive” in another.
- Use “…” only when the action needs more input before it executes (opens a dialog/flow). See mechanics.

---

## Confirmation dialogs (destructive actions)

**Rule.** Tell the user exactly what will happen, in future tense, including the irreversible part. Don’t soften, don’t hide consequences. The confirm button restates the action.

**Budget.** Body one to two sentences, or a short consequence list.

| DO | DON’T |
|----|-------|
| “Deleting a project will delete it for all collaborators and cannot be undone.” | “Are you sure you want to do this?” |
| “This will move the project to the workspace archive for all members and unpublish its sites.” | “This may affect your project.” |
| Consequence list: “Your custom domain will be disconnected,” “A Framer banner will be shown on your site,” “All CMS limits will be reapplied” | “You’ll lose some features.” |

**When NOT to confirm.** Reserve the dialog for uncommon, irreversible actions. Don’t interrupt with a confirmation for something the user can undo — deleting a draft that goes to a recoverable archive, removing an item with an undo toast. A confirm dialog on an undoable action just trains people to click through. If there’s an undo, ship the undo, not the dialog.

**Notes.**
- Confirm button = the verb (“Delete Project,” “Cancel Plan”). Cancel/secondary = “Dismiss” or a plain “Cancel” that means “don’t do it.”
- For high-stakes cancellation, a genuine line is in-voice: “Please don’t hesitate to contact us if we can do anything to keep Framer in your workflow.” Use sparingly and only where sincere — this is the *sole* sanctioned use of “we/us” (see mechanics — pronouns); routine copy stays impersonal.

---

## Tooltips & helper text

**Rule.** One job, concise, no period if it’s a fragment/label. Give the concrete fact (price, limit, date), not a vague gesture.

**Budget.** One fragment or sentence, ≤10 words unless stating a price/date.

| DO | DON’T |
|----|-------|
| “Additional editors are $20 / month.” | “Extra editors may incur charges” |
| “Expires June 30, 2026” | “Expires soon” |
| “Compare all plans and features” | “More info” |
| “Select an annual plan and get a free domain for your first year.” | “Annual plans have perks” |

---

## Placeholders

**Rule.** Show the expected input or a real example. Sentence case. Use “…” to signal an open field where the user continues typing.

**Budget.** A realistic example value — a few words at most.

| DO | DON’T |
|----|-------|
| “My collection” (example value) | “Enter a name here” |
| “Reason for cancellation…” | “Type something” |
| “you@studio.com” | “Email” (that’s a label, not a placeholder) |

---

## Plan / billing messaging

**Rule.** Neutral, precise, never punitive. Money and limits are sensitive — be factual and give the path. This is where the recent Plans cleanup set the bar.

**Budget.** Same as toasts: fact 2–6 words, path-out one sentence.

| DO | DON’T |
|----|-------|
| “You are currently on a Free plan.” | “You haven’t upgraded yet” |
| “Couldn’t load your summary” / “Check your connection and try again, or contact support.” | “Failed to create your order” |
| “Payment already in progress” / “Complete it in your other tab, or close it to start over.” | “A checkout’s already open” |
| “Cancel your add-on to downgrade” / “The Analytics add-on isn’t available on this plan.” | “You can’t downgrade with this add-on” |
| Informational dead-end (no fake CTA): “Plans live in workspaces” | A disabled button that goes nowhere |

**Notes.**
- When an action is impossible, explain the *why* in terms of the user’s setup (“more than this plan allows,” “isn’t available on this plan”), not a refusal.
- Reserve the accent/primary button color for the genuinely positive action (e.g. “Republish” after upgrade). Recovery buttons stay neutral.
- Don’t invent a CTA where there’s no action to take — say the informational thing and let it be.
