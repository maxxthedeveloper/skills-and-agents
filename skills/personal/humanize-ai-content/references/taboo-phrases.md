# Taboo Phrases — Zero Tolerance

These phrases are markers of AI-generated text. **Every single one** must be eliminated during the Reconstruction Pass. No exceptions.

Scan is case-insensitive. Partial matches count (e.g., "delve" matches "delving into").

---

## 1. Hedging / Qualification (~15)

- It's important to note that
- It's worth noting that
- It should be noted that
- It depends on your specific needs
- It's crucial to understand that
- It bears mentioning that
- One could argue that
- It goes without saying
- There are several factors to consider
- This is particularly important because
- It's essential to recognize that
- While there's no one-size-fits-all
- The answer isn't straightforward
- That said, it's important to
- Results may vary depending on

## 2. Filler Transitions (~18)

- Moreover
- Furthermore
- Additionally
- In addition to this
- Let's dive in
- Let's dive deeper
- Let's unpack this
- Let's explore
- Without further ado
- With that being said
- That being said
- Having said that
- It's also worth mentioning
- On the other hand
- By the same token
- In light of this
- In the same vein
- Moving forward

## 3. Corporate Buzzwords (~30)

- leverage
- robust
- seamless
- seamlessly
- empower
- scalable
- cutting-edge
- game-changer
- game-changing
- best-in-class
- world-class
- synergy
- paradigm shift
- holistic
- ecosystem
- innovative
- revolutionize
- streamline
- streamlined
- optimize
- optimized
- elevate
- transform
- transformative
- harness
- unlock
- drive growth
- actionable insights
- thought leader
- thought leadership
- disruptive

## 4. AI-Typical Openers (~12)

- In today's rapidly evolving
- In today's fast-paced
- In today's digital age
- In today's world
- In an era of
- In the ever-changing landscape
- Imagine a world where
- Picture this:
- Have you ever wondered
- Are you tired of
- When it comes to
- In the realm of

## 5. AI-Typical Closers (~14)

- In conclusion
- To sum up
- To summarize
- In summary
- All in all
- At the end of the day
- Embrace the power of
- The future is now
- The possibilities are endless
- Start your journey today
- Take the first step
- Ready to transform
- Don't miss out
- The ball is in your court

## 6. AI Sentence Starters (~12)

- Essentially,
- Interestingly,
- Firstly,
- Secondly,
- Thirdly,
- Importantly,
- Notably,
- Significantly,
- Fundamentally,
- Ultimately,
- Consequently,
- Accordingly,

## 7. Empty Emphasis (~18)

- very
- incredibly
- extremely
- highly
- truly
- really
- absolutely
- utterly
- comprehensive
- myriad
- plethora
- multifaceted
- unparalleled
- unmatched
- unprecedented
- groundbreaking
- a wide range of
- a variety of

## 8. Delve & Family (~15)

- delve
- delving
- deep dive
- dive deep
- navigate challenges
- navigate the complexities
- navigate this landscape
- landscape (when describing a field/industry)
- tapestry
- rich tapestry
- intricate tapestry
- at the forefront
- realm
- the intricacies of
- foster

---

## Scan Rules

1. **Case-insensitive** matching
2. **Partial match** — "delving into the topic" triggers "delve"
3. **Word-boundary aware** — "moreover" in "moreover" triggers, but "more over" does not
4. **Context-exempt** — even inside quotations, these must be flagged (the writer can decide to keep a direct quote, but it must be flagged)
5. **Zero tolerance** — a single remaining taboo phrase fails the validation
