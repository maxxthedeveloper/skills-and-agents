# Loops, distilled for a copywriter

What you must know about Loops (loops.so) to write copy that ships correctly. Framer sends its email through Loops. This is the copy-relevant distillation — full docs at loops.so/docs (machine-readable index: loops.so/docs/llms.txt).

Contents: send mechanisms · workflow triggers · personalization variables · editor blocks & components · LMX · the Loops CLI (read-only) · lifecycle framework · deliverability notes.

## The three send mechanisms

Every deliverable must name one of these. They have different rules.

| Mechanism | What it is | Use for | Copy constraints |
|---|---|---|---|
| **Campaign** | Human-initiated broadcast to the audience, a segment, a mailing list, or an ad-hoc filter. Schedulable. | Announcements, changelogs, launches, events | Marketing email: Loops appends the footer (address + unsubscribe) automatically — never write your own. Only reaches `subscribed` contacts. |
| **Workflow** | Behavior-triggered sequence: trigger → timers → emails → branches. A/B experiments supported per-node. | Onboarding, activation nudges, upgrade/lifecycle, winback | Marketing email, same footer rule. Can use event properties in copy. Active workflows can't be edited — pause first. |
| **Transactional** | API-triggered 1-to-1 must-deliver mail. Ignores subscribe status. No open/click tracking. | Magic links, publish confirmations, invites, billing, renewal notices | **No marketing content allowed.** No unsubscribe footer. Template must be published before the API can send it. |

Rule of thumb: a human decides to send it → campaign; the user's behavior decides → workflow; the app must deliver it → transactional.

## Workflow triggers (Sequence mode vocabulary)

Exactly four trigger types — use these names when mapping a sequence:

1. **Contact added** — fires when a contact enters the audience via API/form/integration (not CSV upload). The welcome-series trigger.
2. **Contact updated** — fires on a property change; can match specific from→to transitions (e.g. `subscriptionStatus` free→paid). The billing/lifecycle trigger.
3. **Contact added to list** — fires on mailing-list join; leaving the list pulls the contact out of the workflow at the next node.
4. **Event received** — fires on a named event from the app (e.g. `firstPublish`, `hitPageLimit`). The activation/behavior trigger — prefer this over timers whenever the product can emit the event.

Plus: **timers** (fixed delays, placeable anywhere), **audience filters** (gate all following nodes or next node only), **branches** (conditional splits), **experiments** (A/B/n with % allocation — the built-in way to test subject lines). Trigger frequency is "one time" vs "every time" — say which, for re-triggerable moments like limit hits.

## Personalization variables — exact syntax

- **Contact properties** (campaigns + workflows): `{firstName}` — camelCase API name. Typing `{` in the editor opens the menu.
- **Event properties** (workflows on an event trigger only): `{EVENT_PROPERTY:propertyName}` — data carried on the triggering event, e.g. the name of the site they published.
- **Data variables** (transactional only): `{DATA_VARIABLE:variableName}` — passed in the API call. Placeable in body, subject, headers, button links, image URLs.

**Fallbacks are mandatory in marketing email.** A contact/event variable with no value and no fallback means Loops silently doesn't send that email to that contact. Write fallbacks into every deliverable — notation in specs: `{firstName | there}`. The pipe is spec shorthand only — in the editor, set the fallback in the variable menu when inserting it; LMX has no inline fallback syntax at all. Variable names are case-sensitive.

There is **no Liquid/Handlebars templating and no conditional logic** inside templates. If two segments need different copy, that's two emails behind a branch or filter — not one clever template.

## Editor blocks & Components

The Loops editor is Notion-like. Block vocabulary for specs: **Heading, Paragraph, Button, Image, Video, Link, Divider, Section, Columns, CodeBlock, List, Quote**, plus **array blocks** (repeatable, bound to array data variables — line items etc.).

Two reuse mechanisms — this is how "own the components" happens in practice:

- **Themes** — styling presets (typography, colors, button shape) shared across emails. The visual refresh lives here.
- **Components** — reusable *content* blocks shared across emails. Name recurring structures in your specs (release-header, benchmark-line, changelog-item) so they get built once as Components and every future email inherits the style.

Marketing emails get an automatic footer (company address + unsubscribe) — required by Loops, never hand-written. Transactional emails don't get one.

## LMX — the escape hatch

Loops Markup Language: strict-XML email format (`<Section>`, `<H1>`, `<Paragraph>`, `<Button>`, `<Image>`, inline `<Strong>` `<Link>`) editable via the API, for version-controlled or programmatically generated emails. Variables are prefixed there: `{contact.firstName}`, `{data.resetLink}`. Custom HTML/MJML upload also exists. Default to editor-block specs; reach for LMX only when the user wants emails in git or generated from data. Operating Loops directly is the `loops-cli` skill's job — this skill only reads, see the next section.

## The Loops CLI — read-only grounding

The official CLI (`loops`) talks to the live Framer team when authenticated. Within this skill it is strictly a research instrument — read, never write.

Availability: `command -v loops && loops auth status`. Missing or unauthenticated → note it in one line and work without it.

| To ground… | Run (add `-o json` when parsing) |
|---|---|
| Personalization variable names (case-sensitive) | `loops contact-properties list` |
| Segment names for the `Send as:` audience | `loops audience-segments list` |
| Existing campaigns / a baseline email's content | `loops campaigns list`, `loops email-messages get <id>` |
| Existing transactional templates | `loops transactional list`, `loops transactional get <id>` |
| Existing workflows before proposing a sequence | `loops workflows list`, `loops workflows get <id>` |
| Mailing lists | `loops lists list` |
| Existing Themes / Components (the reuse system) | `loops themes list`, `loops components list`, `loops components get <id>` |

**NEVER run mutating commands.** Banned verbs anywhere in a `loops` invocation: `create`, `update`, `delete`, `send`, `publish`, `draft`, `upload`, `suppression`, `nodes`, plus the bare `loops send`. Three traps that don't look mutating: `email-messages preview` SENDS a real email to real addresses, `events send` fires live workflow triggers for real contacts, and `auth get` prints a secret API key to the transcript. If the user wants changes made in Loops, that's the separate `loops-cli` skill, invoked by them explicitly — not this skill's job.

## Loops' own lifecycle framework (for Sequence mode)

Their recommended shape, adapted to Framer:

- **Onboarding**: 1–5 emails over ~30 days while the user is on Free — welcome immediately on Contact added, then event-gated nudges (started a site but didn't publish → nudge; published → milestone email). Front-load week one, go sparse after.
- **New-paying**: 1–3 emails on `subscriptionStatus` → paid, within 3 days — the features their plan unlocked.
- **Dunning**: 1–3 recovery emails on payment-failed status. Transactional in tone.
- **Churn**: one goodbye/feedback email on cancellation. Never a sequence.
- Canonical nudge pattern from their docs: event trigger + 3-day timer + audience filter `converted equals false` → one email.

## Deliverability notes that affect copy

- Send from a subdomain (Framer already does — keeps root-domain reputation safe).
- **Avoid shortened youtu.be links** — Gmail flags click-tracked short links as phishing (Loops' Guardian warns on these). Use the full youtube.com URL or disable tracking on that link; safest is linking the framer.com page that embeds the video.
- Big sends go to engaged segments first (active last 30/90 days), then expand — so "audience" in a spec should usually be a segment, not "everyone".
- Loops' own stance: open rates are vanity; clicks and conversions (Goals) are the metric. Write for the click.
- Test recipients: addresses `@example.com` / `@test.com` return API success without sending — useful for transactional QA.
