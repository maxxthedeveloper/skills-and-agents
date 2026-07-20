# AI giveaways in email copy

Framer's emails are drafted with AI assistance. The reader must never be able to tell. This file catalogs what makes short-form copy read as AI-written in 2026 — distilled for email from the deep catalogs in `blog-writer/references/ai-tells.md` and `humanize-ai-content` (use humanize's cross-skill diagnosis mode for a full cleanup pass; don't duplicate it here).

Why it matters commercially: readers punish *suspicion*, not authorship — 52% of consumers disengage the moment copy feels AI-written, and 18% have unsubscribed from a brand over it. There is no confirmed "AI detector" in spam filters; the deliverability penalty is engagement-mediated — AI-sounding copy gets fewer opens and clicks, and engagement is what inbox providers actually score.

The 2026 shape of the problem: the tells migrated from words (2024: "delve") to constructions (2025: contrast frames, participial tails) to absence (no specificity, no stance). Word lists go stale in 12–18 months; the constructions persist across model generations. So: constructions first, words second, and the positive requirements matter most.

`scripts/check-copy.sh` catches the mechanical patterns below deterministically. The judgment items stay manual.

## Banned constructions (the durable tells)

1. **Negation-pivot / contrast frame** — "It's not just an update — it's a new way to build." / "Not X. Not Y. Just Z." / "Not because X. Because Y." The single most-cited AI tell of 2025–2026: measured at 5× pre-ChatGPT frequency, and LinkedIn algorithmically demotes it since May 2026. In a subject line or lede it's one sentence carrying three tells (contrast frame + em dash + inflation). State the point directly instead.
2. **Participial benefit tail** — "…, ensuring a seamless experience", "…, empowering your team to do more", "…, highlighting the importance of". The strongest *measured* grammatical tell (~5× human rate) and the one that survived every model generation. Delete the tail; if the point matters, give it its own sentence with a concrete fact. (Concrete action participles are fine — "connecting pages, setting up styles" describes what the product does; "ensuring seamlessness" claims significance without content.)
3. **Equal-length triad** — "Fast. Simple. Effective." headlines, three perfectly parallel benefit bullets. One list of three concrete items is fine; a *pattern* of threes with identical-length limbs is templated. Break one limb's length, or use two or four items.
4. **Staccato stack** — short fragments, one per line, building to a payoff ("No setup. No code. Just publish."). The newest-generation tell: over-short uniform fragments replaced over-long uniform sentences. One fragment per email, load-bearing, maximum.
5. **Self-answering question** — "The result? More conversions." / "The best part? It's free." Radioactive in subject lines. Make the statement.
6. **False range & persona pair** — "From startups to enterprises", "Whether you're a designer or a founder". If you can't name the meaningful middle of the range, the range is fake. Name the actual audience or drop the frame.
7. **Copula dodge** — "boasts", "serves as", "offers a comprehensive suite of" where "is" or "has" belongs. "The API is fast" beats "The API boasts impressive speed."

## The word layer (dated — expect rotation)

Beyond the house banned list in `email-voice.md`:

- **Faded but still banned** (2023–24 era; readers' pattern-matchers were trained on them): delve, tapestry, testament, realm, elevate, supercharge, effortless, game-changer, cutting-edge, robust, harness, empower, streamline, transformative, revolutionize, "unlock your creativity"-style imperatives ("what unlocks on Pro" is house usage and stays).
- **Current-era survivors** (mid-2025+): emphasizing, enhance, highlighting, showcasing, underscoring — quieter significance verbs, usually riding a participial tail.
- **Performed casualness** (the 2025+ overshoot into fake informality): "Here's the kicker", "Let's be real", "no fluff", "wild ride", "chef's kiss", "at your fingertips", "think of it as", "it's like having a designer in your pocket", "Say goodbye to X. Say hello to Y."
- **Hollow significance**: "plays a crucial role", "stands as a testament", "marking a pivotal moment", "in today's fast-paced world".

## Em dashes — density, not presence

Framer's house style uses real em dashes and keeps them. The tell is density and placement: machine-typical is a dash where a comma belongs, roughly one per 150 words, and Claude models — which draft these emails — are the heaviest users. Rules: **max 2 per email, never 2 in one sentence, comma where a comma would do.** Never strip them all; dashless prose written in fear is its own tell.

## What makes 60 words read human (the positive kit)

These map onto the model-release formula — they're why it works:

1. **One product-specific observation** that fails the competitor-swap test: if the sentence works unchanged in a Cursor or Lovable email, it's slop. The "we've found…" hands-on line is this.
2. **One exact, real number.** A benchmark, a price, a credit multiple. Real — fake precision reads worse than none.
3. **One opinionated recommendation.** A ranking or trade-off: "save it for first generations; Sonnet 5 remains the pick for quick edits." AI avoids commitment; committing reads human.
4. **One short sentence** — under 8 words — against a longer one. Contrast is the rhythm signal in copy this size.

Hedge only in first person and only on genuinely uncertain particulars ("we're not sure why yet"). Never impersonal hedges ("can potentially", "designed to help").

## Judging (Audit mode)

Cluster before verdict: one tell is noise, two is a flag, three is a rewrite. Don't condemn a string over a single em dash or one common word — the constructions and the missing specificity are the evidence. For your own drafts, zero tolerance on everything above.
