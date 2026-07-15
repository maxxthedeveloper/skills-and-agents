# The Framer voice

A portrait of how Framer writes, plus a bank of real strings to pattern-match against. When you draft, your copy should feel like it could sit next to these without anyone noticing it was added.

## Personality

- **Confident, not boastful.** States capability as fact. No “we think,” “maybe,” “try to.” Doesn’t oversell either — specificity does the convincing, not adjectives.
- **Designerly.** Talks to people who build for the web and respect craft. Comfortable with the right technical word (canvas, breakpoint, component, CMS) but never jargon for its own sake.
- **Outcome-first.** Leads with what the user gets. “Manage more. Publish faster.” before any feature description.
- **In control.** A recurring theme — the user (or the designer) stays in command. “Agents that work alongside you, not instead of you.” “Under your control.”
- **Warm but spare.** Human, uses contractions, occasionally says “please” where it’s genuine — but never chatty, never padded.
- **Unsentimental.** No hype words, no exclamation theatre, no “oops.” Calm even when something broke.

## Sentence rhythm

- Short. Headlines are 3–7 words, often fragments. Bodies rarely top ~20 words.
- Parallel structure for lists: “Design freely, manage CMS content, optimize SEO, collaborate, and publish fast.”
- Periods to end thoughts; em-dashes to join them. Two casing systems: names get Title Case (titles, buttons, field labels, menu items), statements get sentence case (toasts, bodies, placeholders, helper text) — see mechanics.md.

## House words (reach for these)

ship · build · publish · design · create · manage · control · canvas · responsive · professional · workspace · in sync

## Words to avoid

easy · simple · just · simply · oops · uh-oh · awesome · amazing · incredible · powerful · revolutionary · leverage · utilize · seamless (when used as filler) · “we’re excited/thrilled” (and any excitement-opener) · “Error:” prefixes · error codes in user-facing text

---

## Bank A — marketing voice (framer.com)

For calibration only. **Do not** write in-product copy this punchy; product copy is plainer. But the underlying confidence and outcome-first instinct carries over.

- “Framer is your AI website builder for professional sites” — possessive “your,” clear what + for whom.
- “Agents that work alongside you, not instead of you” — control philosophy in one line.
- “A professional design agent, native to the canvas. It works directly on your site to generate and refine in place, with every change visible, editable, and under your control.” — technical specificity + empowerment.
- “Manage more. Publish faster.” — outcome-first, parallel, velocity implied.
- “Not just vibes, a full platform” — confident dismissal, no hype needed. (Legacy line: the “not just X” contrast frame has since become a catalogued AI tell — keep the confidence, don’t reuse the construction; see `ai-tells.md`.)
- “Design freely, manage CMS content, optimize SEO, collaborate, and publish fast” — parallel verbs, freedom + speed.
- “Make the web more creative” — the mission; ambitious, domain-specific.
- “Built on a community that isn’t going anywhere” — reassurance, human, no superlative.

What makes these “Framer”: they assume a sophisticated reader, lead with the verb or the outcome, follow the casing split (Title Case for names, sentence case for statements), and never raise their voice.

---

## Bank B — in-product voice (real strings from the codebase)

These are the closest reference for what you write. Grouped by surface. All are good examples of the house style.

### Error / failure toasts
- “Couldn’t load prices”
- “Couldn’t load your summary” / “Check your connection and try again, or contact support.”
- “Couldn’t start your checkout”
- “Couldn’t reactivate your plan”
- “Couldn’t update your plan”
- “Payment declined”
- “Payment already in progress” / “Complete it in your other tab, or close it to start over.”
- “You don’t have access” / “Only editors in this workspace can open this page.”
- “Editor limit reached” / “Your workspace has 8 editors, more than this plan allows.”
- “Promotion code didn’t work” / “This code is invalid or expired.”
- “Exceeded max file size” / “of 5 MB.”
- “Page limit exceeded” / “(5/50).”
- “CMS items limit exceeded” / “(500/1000).”
- “Bandwidth limit exceeded” / “(105/100 GB).”
- “Failed to load” / “code editor.”
- “Try again, or contact support if this keeps happening.”

Pattern: name the fact neutrally (“Payment declined,” “Editor limit reached”), then give the recovery or the number. Never “you failed,” never an error code.

### Success / confirmation toasts
- “Thank you.”
- “Updated to Pro” / “Your site subscription has been updated to a Pro plan.”
- “The invoice has been sent to your inbox.”
- “You are now eligible to claim a free domain.”
- “Archived My Portfolio.”
- “Deleted My Portfolio.”
- “Unarchived My Portfolio.”
- “Copied API key”
- “Purchased add-on”

Pattern: state the result plainly. Past-tense verb + object for project actions. No exclamation marks; the moment carries itself.

### Empty states
- “No projects” / “Create a project from scratch or use a template to get started.”
- “No archived projects” / “All archived projects will be listed here.”
- “No templates” / “Create a new template or mark existing projects as templates to use them as starting points for your team.”
- “No projects found” / “Try adjusting your search or browse workspaces.”
- “This project does not contain any code components.” / “Browse all code components and code overrides here.”

Pattern: short headline naming the emptiness, then one line that either guides the user forward or explains what will appear here.

### Buttons & actions
- “Subscribe” · “Upgrade to Pro” · “Downgrade to Pro” · “Switch to Yearly” · “Reactivate”
- “Try Again” · “Back to Plans” · “Update Payment Method” · “Update Billing Address” · “Manage Editors”
- “Republish” · “Add Domain” · “Dismiss” · “Learn More” · “Contact Us”
- “Cancel Plan” · “Leave Project” · “Archive Project” · “Delete Project” · “Confirm & Pay”

Pattern: verb-first, Title Case (small words lowercase: “Upgrade to Pro”), object when needed, no `-ing`.

### Confirmation dialogs (destructive)
- Leave: “You will leave this project, and it will no longer be visible on your dashboard.”
- Archive: “This will move the project to the workspace archive for all members and unpublish its sites.”
- Delete: “Deleting a project will delete it for all collaborators and cannot be undone.”
- Cancel plan (consequences list): “Your custom domain will be disconnected” · “A Framer banner will be shown on your site” · “All CMS limits will be reapplied” · “You’ll lose access to paid features”

Pattern: say exactly what happens, in future tense, including the irreversible part. No softening.

### Tooltips / helper text
- “Additional editors are $20 / month.”
- “Compare all plans and features”
- “Select an annual plan and get a free domain for your first year.”
- “Expires June 30, 2026”
- “You are currently on a Free plan.”
- “Read-only editor.” / “You cannot edit files.”

### Warnings
- “Adding large files” / “can impact performance.”
- “Workspace used over 80%” / “of its credits.”
- “Your plan expires soon.” / “Upgrade now.”

---

## Quick calibration test

Before delivering, ask: *Could this line drop into Bank B unnoticed?* If it’s louder, longer, blamier, or more title-cased than those strings, bring it back in line.
