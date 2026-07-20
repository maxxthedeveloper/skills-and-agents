# Edit Library — 10 Transformation Types

Each transformation includes the pattern to spot, the fix, and 3 before/after examples.

---

## 1. Replace Abstract Verbs with Concrete Verbs

**Pattern:** Vague verbs that could mean anything (leverage, utilize, optimize, facilitate, implement, enable).

**Fix:** Swap for a verb that creates a mental image of the actual action.

| Before | After |
|--------|-------|
| We leveraged machine learning to optimize our pipeline. | We added a gradient-boosted classifier to the intake step. Cut processing time by 40%. |
| The platform enables teams to collaborate seamlessly. | Teams edit the same document at the same time. Changes show up in under a second. |
| We implemented a solution to address user pain points. | We added a search bar to the settings page. Support tickets dropped 30% that week. |

---

## 2. Vary Sentence Length (Break the Metronome)

**Pattern:** Every sentence is 15-20 words. The rhythm is flat. Nothing punches. Nothing breathes.

**Fix:** Follow a long sentence with a short one. Use fragments. Let a 5-word sentence land after a 30-word setup.

| Before | After |
|--------|-------|
| The team worked on the migration for three months. They encountered several challenges along the way. The project was completed on schedule despite the difficulties. | The migration took three months. Not because it was hard — the schema changes were straightforward. The real problem was data. Fourteen years of it, full of edge cases nobody documented. But we shipped on time. |
| Users can create custom dashboards with multiple widgets. They can also share these dashboards with team members. The sharing feature supports different permission levels. | Users build their own dashboards. Drag in widgets, arrange them, done. Want to share one? Drop in an email address and pick a permission level — view, edit, or admin. |
| The system processes approximately ten thousand requests per second. It handles peak loads effectively during high-traffic periods. Auto-scaling ensures consistent performance. | Ten thousand requests per second. That's the baseline. During peaks — Black Friday, product launches — it scales to 3x that without manual intervention. We haven't paged anyone for capacity in 18 months. |

---

## 3. Eliminate Hedging

**Pattern:** Qualifiers that weaken every statement: "It's important to note," "It's worth mentioning," "essentially," "in many cases."

**Fix:** Delete the hedge. State the thing. If it's uncertain, say why — don't just sprinkle doubt.

| Before | After |
|--------|-------|
| It's important to note that performance may vary depending on your specific configuration. | Performance depends on your configuration. A 4-core machine runs this 2x slower than an 8-core one. |
| Essentially, the framework provides a way to manage state across components. | The framework manages state across components. |
| In many cases, teams find that automated testing can significantly reduce bug counts. | Teams that adopt automated testing see 40-60% fewer production bugs. The ones that don't, don't. |

---

## 4. Restructure from Template

**Pattern:** The "claim → evidence → transition" template repeated paragraph after paragraph.

**Fix:** Vary paragraph structure. Some paragraphs are all evidence. Some are all opinion. Some start with the conclusion. Mix it up.

| Before | After |
|--------|-------|
| Microservices offer many benefits. They allow teams to deploy independently. This leads to faster development cycles. However, there are also challenges to consider. | Independent deployments are the reason people adopt microservices. Everything else — scaling, fault isolation, technology diversity — those are bonuses. The cost: your networking layer becomes your biggest source of bugs. |
| Remote work has transformed the workplace. Studies show that remote workers are often more productive. This has led many companies to adopt hybrid models. | 37% of U.S. employees worked remotely at least part-time in 2024. The productivity question is settled — remote workers ship more code, close more tickets, attend fewer meetings. What's not settled: how you build culture when half your team has never met in person. |
| Security is a critical concern for modern applications. Many organizations face increasing threats from cybercriminals. Implementing a zero-trust architecture can help mitigate these risks. | Last year, the average cost of a data breach hit $4.45 million. Zero-trust architecture — where nothing inside or outside your network is trusted by default — cuts that number. Not to zero. But the companies using it report 35% lower breach costs. The catch: it takes 18-24 months to implement properly. |

---

## 5. Cut Ceremonial Transitions

**Pattern:** "Moreover," "Furthermore," "In addition to this," "Let's dive deeper," "With that being said."

**Fix:** Delete the transition entirely. Start the next sentence with the actual content. The paragraph break is the transition.

| Before | After |
|--------|-------|
| The API supports REST and GraphQL. Furthermore, it also provides WebSocket connections for real-time data. | The API supports REST and GraphQL. For real-time data, there are WebSocket connections. |
| Caching improved our response times. Moreover, it reduced database load by 60%. | Caching improved our response times and cut database load by 60%. |
| Let's dive deeper into the authentication flow. When a user logs in, the system first validates their credentials. | When a user logs in, the system validates their credentials against the auth store. |

---

## 6. Replace AI Openers

**Pattern:** "In today's rapidly evolving landscape," "In the world of," "When it comes to," "Imagine a world where."

**Fix:** Start with a fact, a number, a name, or an action. Something concrete.

| Before | After |
|--------|-------|
| In today's rapidly evolving tech landscape, artificial intelligence is transforming how businesses operate. | Stripe replaced 30% of its customer support workflows with AI agents last quarter. Response times dropped from 4 hours to 11 minutes. |
| When it comes to choosing a programming language, there are many factors to consider. | Python runs 50x slower than C. Most teams don't care — and they're right. |
| Imagine a world where your code deploys itself without human intervention. | Our CI pipeline deploys to production 47 times a day. No human touches it after the PR merges. |

---

## 7. Fix AI Closers

**Pattern:** "In conclusion," "Embrace the power of," "The future is now," "Start your journey today."

**Fix:** End with the strongest specific point. Or a short sentence that lands. Never summarize what you just said.

| Before | After |
|--------|-------|
| In conclusion, adopting DevOps practices can significantly improve your team's productivity and deployment frequency. Embrace the power of automation to stay competitive. | We went from monthly deploys to daily ones. The team is smaller now. They ship more. |
| The possibilities are endless when you combine AI with modern data infrastructure. The future of data engineering is bright and full of opportunity. | The stack works. It costs $2,400/month for 50 million events per day. That's the number that matters. |
| Start your journey toward better code quality today by implementing these testing strategies. | Write the first test. Make it pass. The rest follows from there. |

---

## 8. Convert Passive to Active

**Pattern:** "was implemented," "has been observed," "can be achieved," "is being developed."

**Fix:** Find the actor. Make them the subject. If there's no actor, pick the most concrete noun available.

| Before | After |
|--------|-------|
| The feature was implemented by the backend team in Q3. | The backend team shipped the feature in Q3. |
| It has been observed that response times increase during peak hours. | Response times spike during peak hours — 340ms average jumps to 900ms between 9-11am EST. |
| Significant cost savings can be achieved through proper resource allocation. | Right-sizing our EC2 instances saved $14,000/month. |

---

## 9. Add Asymmetry (Parentheticals, Dashes, Asides)

**Pattern:** Every sentence is a clean subject-verb-object structure. No texture. No human quirks.

**Fix:** Add the things real writers use — dashes for pivots, parentheses for asides, sentence fragments for emphasis.

| Before | After |
|--------|-------|
| The migration was complex. It took six weeks and required coordination across three teams. | The migration took six weeks — and that was with three teams running in parallel. (The original estimate was two weeks. Nobody mentions that anymore.) |
| TypeScript adoption improved our code quality. We caught more bugs at compile time. | TypeScript caught bugs we didn't know we had. Not runtime bugs — the subtle ones, where you pass a string where a number should be. Those. |
| The database handles 10,000 queries per second. This meets our current requirements. | The database handles 10,000 queries per second. Enough for now — barely. |

---

## 10. Replace Lists with Prose (Selectively)

**Pattern:** Every set of 3+ related points becomes a bulleted list. Lists are fine sometimes, but AI overuses them.

**Fix:** When the items are short and related, weave them into a sentence or short paragraph. Keep lists only when items are long or genuinely parallel.

| Before | After |
|--------|-------|
| Benefits of the new system: • Faster deployment times • Reduced error rates • Better monitoring • Lower infrastructure costs | The new system deploys faster, breaks less, and costs about 40% less to run. The monitoring is better too — we actually get alerts before users complain now. |
| Key features include: • Real-time collaboration • Version history • Role-based access control • API integrations | It's a collaborative editor with version history and role-based access. You can also pipe data in and out through the API, which is how most teams actually use it. |
| The technology stack consists of: • React for the frontend • Node.js for the backend • PostgreSQL for the database • Redis for caching | The frontend is React, backed by Node.js and PostgreSQL. Redis handles caching — mostly session data and the dashboard's real-time counters. |
