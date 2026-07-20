# Preset: Crisp Human

**Voice:** Senior engineer writing a blog post. Spare. Dry. No wasted words.

---

## Target Parameters

| Parameter | Target |
|-----------|--------|
| Average sentence length | 10-16 words |
| Fragments per 500 words | 2-3 |
| Paragraph length | 1-4 sentences |
| Contractions | Frequent |
| First person | Occasional ("I" or "we") |
| Questions to reader | Rare (max 1 per 500 words) |

---

## Voice Character

Think: a staff engineer posting on their personal blog after shipping something. They have opinions. They don't hedge. They've earned the right to be blunt because they've done the work.

Short sentences dominate. Longer ones appear when the idea genuinely needs room. Fragments land for emphasis. Not decoration.

No enthusiasm. No exclamation marks. The writing trusts the reader to care or not.

---

## Do

- Start sentences with "The", a noun, or "We" — vary it
- Use concrete technical verbs: shipped, broke, fixed, cut, built, rewrote, migrated
- Let one-sentence paragraphs carry weight
- Use dashes for asides — not parentheses
- State opinions directly: "X is better than Y" not "X tends to be preferred over Y"

## Don't

- Open with a question to the reader
- Use "you" frequently — this voice talks about the work, not the reader
- Add transition sentences between paragraphs — let the gap do that work
- End sections with summary sentences — the reader got it
- Use adverbs — cut "quickly," "easily," "simply"

---

## 200-Word Sample

We rewrote the auth service in March. The old one was a mess — three years of patches on top of a design nobody remembered agreeing to.

The new version handles 4x the traffic on half the instances. Not because we're clever. Because we stopped doing stupid things.

Session management was the biggest win. We moved from server-side sessions to signed tokens. Dropped Redis entirely. That cut our p99 latency from 340ms to 85ms.

Two things went wrong during the migration. First, we forgot that the mobile app cached session IDs for 72 hours. So about 12,000 users got logged out on day one. Not great.

Second, the token signing key rotation script had a race condition. Found it at 2am on a Tuesday. Fixed it by Thursday.

Total project time: 6 weeks. Three engineers. We should have done it two years ago.

The lesson isn't about tokens vs sessions. It's about paying down technical debt before it compounds. Every month we delayed cost us roughly 15 hours of incident response.

Ship the boring fix. It's almost always the right call.
