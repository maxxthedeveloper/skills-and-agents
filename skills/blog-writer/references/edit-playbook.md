# Edit Playbook -- 12 Transformations

Each transformation: the pattern to spot, why it's a problem, the fix, and a before/after example. Apply during Phase 3 (Reconstruction).

---

## 1. Lead with the Point, Not the Setup

**Pattern**: The first 1-3 sentences are warmup before the actual point arrives. The writer is clearing their throat in front of the reader.

**Fix**: Delete everything before the first interesting sentence. Start with the claim, the fact, or the story.

| Before | After |
|--------|-------|
| There's been a lot of discussion lately about whether remote work actually improves productivity. Many studies have been conducted, and the results are surprisingly mixed. But what most people miss is that productivity isn't even the right metric. | Productivity isn't the right metric for remote work. Retention is. Companies with flexible policies kept 34% more senior engineers in 2024 than those with strict return-to-office mandates. |

---

## 2. Convert Abstractions to Evidence

**Pattern**: Claims that float in the abstract. "Companies are adopting," "many teams have found," "research shows." No names, no numbers, no proof.

**Fix**: Name the company. Cite the number. Tell the specific story. If you can't find evidence, the claim might not be worth making.

| Before | After |
|--------|-------|
| Many companies are finding that microservices introduce more complexity than they solve. The industry is starting to reconsider. | Amazon's Prime Video team moved from microservices back to a monolith in 2023. Monitoring costs dropped 90%. They weren't alone -- Segment, Istio, and Basecamp all made similar moves. |

---

## 3. Kill the Transition

**Pattern**: Sentences that exist only to bridge paragraphs. "With that in mind," "Building on this idea," "Another important consideration is."

**Fix**: Delete the transition entirely. Start the next paragraph with its content. If the flow breaks, the paragraphs are in the wrong order.

| Before | After |
|--------|-------|
| TypeScript catches type errors at compile time. **Building on this idea,** generics allow you to write flexible yet type-safe code. | TypeScript catches type errors at compile time. Generics take this further -- write the function once, and the type system adapts it to whatever data structure you pass. |

---

## 4. Sharpen the Verb

**Pattern**: Weak verbs propped up by adverbs, or abstract verbs that could mean anything: "utilize," "implement," "address," "facilitate."

**Fix**: Replace verb+adverb with a single precise verb. Choose verbs that create images.

| Before | After |
|--------|-------|
| We utilized a comprehensive monitoring solution to effectively address performance issues. | We added Datadog. It flagged the three slowest queries in a week. We rewrote them. p99 dropped from 1.2s to 180ms. |

---

## 5. Kill the Adverb, Distrust the Adjective

**Pattern**: Verbs propped up by adverbs when a single vivid verb would do. Adjective clusters stacked in front of nouns where a concrete fact would be more persuasive.

**Fix**: Replace verb+adverb with one precise verb. Replace adjective stacks with evidence.

| Before | After |
|--------|-------|
| She walked slowly through the empty office. | She shuffled through the empty office. |
| He spoke loudly and angrily at the meeting. | He shouted at the meeting. |
| A powerful, flexible, intuitive platform for modern teams. | A platform that handles 10K users on a $50/month plan. |
| They worked extremely hard to quickly deliver an incredibly comprehensive solution. | They shipped in three weeks. |

Stephen King: "The road to hell is paved with adverbs." Hemingway learned to "distrust adjectives as I would later learn to distrust certain people." If the verb needs an adverb, the verb is wrong. If the noun needs three adjectives, the noun is too vague.

---

## 6. One-Sentence Paragraph for Emphasis

**Pattern**: An important point is buried in the middle of a paragraph, surrounded by context and caveats.

**Fix**: Pull the key sentence out. Give it its own paragraph. Let whitespace do the work.

| Before | After |
|--------|-------|
| We spent three months debating the architecture, running benchmarks, and evaluating alternatives. In the end, we realized that the simplest option -- a single PostgreSQL instance -- would have handled our load for the next two years. We over-engineered significantly. | We spent three months debating the architecture. Running benchmarks. Evaluating six different databases. A single PostgreSQL instance would have handled our load for two years. We didn't figure that out until month four. |

---

## 7. Replace Listicle with Narrative

**Pattern**: A numbered list of tips, each independent. No through-line, no argument. Could be shuffled into any order.

**Fix**: Find the one idea that unifies the items. Order them so each builds on the previous. Turn a list into an argument.

| Before | After |
|--------|-------|
| **5 Tips for Better Code Reviews** 1. Keep PRs small 2. Review within 24 hours 3. Focus on logic, not style 4. Ask questions instead of demands 5. Approve when good enough | The best code review practice is the one nobody talks about: speed. Review within hours, not days. When reviews are fast, engineers submit smaller PRs -- because they know feedback comes quickly. Smaller PRs are easier to review, which keeps reviews fast. It's a virtuous cycle. The opposite is also true. Slow reviews breed large PRs. Large PRs get superficial reviews. Nobody learns anything. |

---

## 8. Cut the Qualifier, Keep the Claim

**Pattern**: Every opinion comes with an escape hatch. "In my experience," "This might not work for everyone," "Your mileage may vary."

**Fix**: State the claim. If it needs a caveat, give a specific one. "This breaks down at scale" is useful. "Your mileage may vary" is not.

| Before | After |
|--------|-------|
| I think that, in most cases, it's probably better to start with a monolith rather than microservices, at least initially, though there are certainly exceptions depending on your team size and requirements. | Start with a monolith. Split services out when you can name exactly which service needs to scale independently and why. Until then, a monolith is faster to build, easier to debug, and cheaper to run. |

---

## 9. Compress the Anecdote

**Pattern**: A story that takes 150 words when 50 would do. The setup is too long. The details don't serve the point. The lesson is stated explicitly after the story already made it.

**Fix**: Cut to the essential beats. Trust the reader to get the point.

| Before | After |
|--------|-------|
| Last year, our team was working on a critical feature for a major client. We had been going back and forth for weeks about the best approach. There were lots of meetings and discussions. One day, a junior developer suggested we just build a prototype over the weekend instead of continuing to debate. So that's exactly what we did. And you know what? The prototype worked so well that it became the actual product. The lesson here is that sometimes you just need to stop talking and start building. | We spent three weeks debating a feature architecture. A junior dev built a prototype over the weekend. It shipped. That was the final product. |

---

## 10. Earn Every Sentence

**Pattern**: Sentences that take up space without revealing anything new or advancing the argument. Setup paragraphs that repeat what the reader already knows. Conclusions that restate the introduction.

**Fix**: Apply Vonnegut's Rule 4 — every sentence must reveal something or advance the argument. Test: cover the sentence, read what comes before and after. If nothing is lost, delete it.

| Before | After |
|--------|-------|
| Remote work has been a topic of much discussion in recent years. Many companies have experimented with different approaches. Some have found success, while others have struggled. The key insight that most people miss is that productivity depends on trust, not surveillance. | Productivity depends on trust, not surveillance. |

Four sentences of scaffolding, one sentence that does the actual work. The first three told the reader nothing they didn't already know. Cut them.

---

## 11. Kill the Negation-Pivot

**Pattern**: "It's not X. It's Y." / "What matters isn't X -- it's Y." The theatrical reveal where the writer negates one framing and offers another as if it's an insight.

**Why it's dangerous**: This is the hardest AI pattern to catch because it feels like good writing. It mimics the structure of an insight without requiring actual thought. You can generate these for any topic by filling in a template.

**Fix**: State the positive claim directly. If you find yourself writing "It's not about X," ask: what IS it about? Say that. Skip the theatrical setup.

| Before | After |
|--------|-------|
| It's not about writing more code. It's about writing the right code. | Write less. But write the parts that matter. |
| The problem isn't that teams don't communicate. The problem is that they communicate about the wrong things. | Most team communication is about coordination, not collaboration. Standups report status. What's missing is the conversation about direction. |
| What they're missing isn't discipline. It's choosing what to work on. | Most people work hard enough. They just aim badly. |

---

## 12. Deflate the Vocabulary

**Pattern**: Latinate, academic, or "impressive" words used where simpler synonyms would work. "Facilitate" instead of "help." "Methodology" instead of "method." "Paradigm" instead of "approach."

**Why it matters**: Paul Graham: "Fancy writing doesn't just conceal ideas. It can also conceal the lack of them." The vocabulary should be invisible. If the reader notices a word, it failed.

**Fix**: Apply the "would I say this out loud?" test to every word. Nobody says "utilize" to a friend. Nobody says "endeavor" or "facilitate" in conversation. Use the word you'd actually use.

| Before | After |
|--------|-------|
| The team endeavored to implement a comprehensive solution that would facilitate cross-functional collaboration and mitigate systemic inefficiencies. | The team tried to build something that would help people work together and stop wasting time. |
| This paradigm necessitates a fundamental reconsideration of our methodology. | This means we need to rethink our approach. |

---

## How to Use This Playbook

During Phase 3, make three focused passes:

1. **Cut pass**: Look for patterns 1, 3, 8, 9, 10 -- things to delete or compress
2. **Sharpen pass**: Look for patterns 2, 4, 5, 11, 12 -- things to make concrete or direct
3. **Structure pass**: Look for patterns 6, 7 -- things to reorganize for impact

Three focused passes catch more than one chaotic one.
