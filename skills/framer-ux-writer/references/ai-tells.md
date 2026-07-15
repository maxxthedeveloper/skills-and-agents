# AI giveaways in UX copy

Framer's interface copy is drafted with AI assistance; users must never be able to tell. Microcopy is short, so statistical tells (rhythm, word frequency) barely apply — what gives a string away is a handful of constructions and a register. This is the microcopy distillation of the deep catalogs in `blog-writer/references/ai-tells.md` and `humanize-ai-content` (use humanize's cross-skill diagnosis mode for long-form cleanup).

The 2026 rule of thumb: tells migrated from words ("delve") to constructions (contrast frames, participial tails) to absence (no specificity). Constructions first; word lists rotate and go stale.

`scripts/check-copy.sh` catches the mechanical patterns. Judgment items stay manual.

## Banned constructions

1. **Negation-pivot / contrast frame** — "It's not just a canvas — it's a design partner." The most-cited AI tell of 2025–2026. In UI it shows up in empty states, onboarding cards, and upsell moments. State what the thing does instead.
2. **Participial benefit tail** — "…, ensuring your site stays fast", "…, empowering your workflow". The strongest measured grammatical tell. Delete the tail or give the point its own concrete string. (Concrete action participles are fine: "Publishing your site…" as a progress label describes an action, not a significance claim.)
3. **Equal-length triad** — "Fast. Flexible. Free." Feature blurbs in three identical-length limbs read templated. Two items, or four, or one concrete fact.
4. **Self-answering question** — "The result? A faster site." Make the statement.
5. **Staccato stack** — "No code. No limits. Just design." Stacked fragment drama is the newest-generation tell (and "just" is already banned).
6. **Copula dodge** — "boasts", "offers", "features" where "is" or "has" belongs. "Additional editors are $20 / month" is house register: plain copula, real number.

## The word layer (dated — expect rotation)

Beyond the banned words in `framer-voice.md`:

- **Faded but still banned** (readers' pattern-matchers were trained on them): delve, tapestry, testament, realm, elevate, supercharge, effortless, game-changer, cutting-edge, robust, harness, empower, streamline, transformative, revolutionize.
- **Current-era survivors** (mid-2025+): emphasizing, enhance, highlighting, showcasing, underscoring.
- **Performed casualness** (fake informality, 2025+ overshoot): "Here's the kicker", "Let's be real", "no fluff", "at your fingertips", "think of it as", "it's like having a designer in your pocket". Framer's warmth is spare, not chummy.
- **Hollow significance**: "plays a crucial role", "stands as", "serves as", "in today's fast-paced world".

## Em dashes

House style uses real em dashes ("Periods to end thoughts; em-dashes to join them") and keeps them. In microcopy the rule is simply: never two in one string, and a comma where a comma would do. Don't strip them out of AI-panic — that reads worse.

## What makes a string read human

- **Specific over generic** — the existing non-negotiable is also the strongest anti-AI signal: "(8/100)", "of 5 MB", "Expires June 30, 2026". A string with a real number in it cannot read as slop.
- **Elegant variation is a tell** — call the thing by its name every time (the project, the plan, the domain). Never cycle synonyms ("your site" → "your creation" → "your masterpiece").
- **Plain verdicts** — "Payment declined" is human because it commits. Impersonal hedges ("This may potentially affect…") are the AI register; if something is uncertain, say what is known: "This can take a few minutes."

## Judging (Audit mode)

Cluster before verdict: one tell in one string is a flag, not a conviction — a lone em dash or a common word is noise. Constructions and missing specificity are the evidence. For your own drafts, zero tolerance.
