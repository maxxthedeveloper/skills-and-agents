# Example Video Scripts

Annotated example scripts demonstrating tone archetypes and narrative structure. These are hypothetical products created solely to illustrate the script format and storytelling principles.

---

## Example 1: "Conduit" -- API Monitoring Platform

**Archetype**: Technical Confidence (Stripe-like)
**Duration**: 65 seconds (11 scenes)
**Framework**: Raskin Strategic Narrative

### Narrative Foundation

- **The Shift**: APIs now carry revenue. A broken endpoint is a broken business.
- **The Stakes**: Teams without API observability lose customers silently -- no crash report, no error page, just a timeout and a churned user.
- **The Hero**: Backend engineer at a growing SaaS company. Ships 20+ endpoints. Monitors with logs and hope.
- **The Villain**: Scattered logs, silent failures, the 2 AM "is the API down?" Slack message from a customer.
- **Magic Gifts**: (1) Real-time error detection per endpoint. (2) Latency tracking with automatic anomaly alerts. (3) One-click shareable incident reports.
- **The Wow Moment**: A latency spike detected, root cause identified, and incident report shared -- all before the customer notices.
- **The Hook**: A counter showing API calls per second, one of them turning red.

---

### Script

| Field | Content |
|-------|---------|
| **Scene** | 1 -- The Counter |
| **Act** | Hook |
| **Duration** | 5s |
| **On Screen** | Dark screen. A live counter showing API calls: 2,847/sec. Numbers ticking upward. One request flashes red and disappears. Then another. |
| **Text Overlay** | -- |
| **Voiceover** | "Two thousand API calls a second. Do you know which ones are failing?" |
| **Music/Sound** | Low ambient hum. Subtle tick sound on each red flash. |
| **Emotional Beat** | Unease. Something is wrong and no one is watching. |
| **Transition** | Counter dissolves into a dashboard view. |

<!-- ANNOTATION: The hook uses a specific, concrete visual (a counter with red flashes) rather than an abstract statement. The question in the VO creates tension without being dramatic. Technical Confidence archetype: understated, precise. -->

| Field | Content |
|-------|---------|
| **Scene** | 2 -- The Silent Failure |
| **Act** | Escalation |
| **Duration** | 7s |
| **On Screen** | Split view. Left: server logs scrolling fast, a 504 error buried in noise. Right: a user staring at a loading spinner, then closing the tab. |
| **Text Overlay** | "No crash report. No error page." |
| **Voiceover** | "Your API timed out. Your user left. Your logs say nothing useful." |
| **Music/Sound** | Low tension building. Muted click of tab closing. |
| **Emotional Beat** | Recognition. This has happened to you. |
| **Transition** | Hard cut to black. |

<!-- ANNOTATION: The villain is shown concretely: logs that don't help, users who leave silently. The split screen visually connects the technical failure to the human consequence. No jargon, no abstraction. -->

| Field | Content |
|-------|---------|
| **Scene** | 3 -- The Cost |
| **Act** | Escalation |
| **Duration** | 5s |
| **On Screen** | Black screen. Text appears line by line: "No alert. No ticket. Just a churned user you will never hear from." |
| **Text Overlay** | (the text IS the visual) |
| **Voiceover** | [silence] |
| **Music/Sound** | Music drops to near silence. One sustained low note. |
| **Emotional Beat** | Weight. The cost of not knowing. |
| **Transition** | Text fades. Beat of silence. |

<!-- ANNOTATION: A scene with no voiceover. Letting the text sit in silence gives it more gravity than narration would. The pause before the turn makes the reveal land harder. -->

| Field | Content |
|-------|---------|
| **Scene** | 4 -- The Reveal |
| **Act** | Turn |
| **Duration** | 5s |
| **On Screen** | Conduit dashboard fades in. Clean, dark UI. Endpoints listed with real-time status indicators -- green dots, latency numbers, request counts. |
| **Text Overlay** | "Conduit" |
| **Voiceover** | "Conduit monitors every endpoint, every request, in real time." |
| **Music/Sound** | Music shifts upward. Clean synth note. |
| **Emotional Beat** | Relief. Clarity after ambiguity. |
| **Transition** | Continuous -- camera pushes into the dashboard. |

<!-- ANNOTATION: The product appears as the answer to the tension built in scenes 1-3. The VO is one clean sentence. No "introducing" or "meet Conduit" -- just a statement of what it does. -->

| Field | Content |
|-------|---------|
| **Scene** | 5 -- Magic Gift 1: Error Detection |
| **Act** | Demonstration |
| **Duration** | 7s |
| **On Screen** | Dashboard zooms into one endpoint. Error rate spikes from 0.1% to 4.2%. Red highlight. Alert card slides in from the right: "POST /checkout -- error rate 4.2% -- started 90 seconds ago." |
| **Text Overlay** | -- |
| **Voiceover** | "Error rate on your checkout endpoint just hit four percent. You know in ninety seconds, not ninety minutes." |
| **Music/Sound** | Building energy. Alert chime -- clean, not alarming. |
| **Emotional Beat** | Control. You see the problem as it starts. |
| **Transition** | Cut to latency view. |

| Field | Content |
|-------|---------|
| **Scene** | 6 -- Magic Gift 2: Latency Tracking |
| **Act** | Demonstration |
| **Duration** | 6s |
| **On Screen** | Latency graph for /search endpoint. P99 creeping up over 48 hours. Conduit draws an anomaly boundary line. The moment latency crosses it, an annotation appears: "Anomaly detected -- correlates with deploy #847." |
| **Text Overlay** | -- |
| **Voiceover** | "Latency creeping on search? Conduit traces it to the deploy that caused it." |
| **Music/Sound** | Steady forward momentum. Subtle whoosh on annotation appearance. |
| **Emotional Beat** | Precision. Root cause found, not hunted. |
| **Transition** | Dashboard pulls back to show full endpoint list. |

| Field | Content |
|-------|---------|
| **Scene** | 7 -- Magic Gift 3: Incident Reports |
| **Act** | Demonstration |
| **Duration** | 6s |
| **On Screen** | User clicks "Share Report" button on the alert card. A clean incident report generates: timeline, affected endpoints, error samples, probable cause. URL copied to clipboard. |
| **Text Overlay** | -- |
| **Voiceover** | [silence] |
| **Music/Sound** | Soft click sound. Music sustains. |
| **Emotional Beat** | Effortless. One click, done. |
| **Transition** | Cut to the wow moment. |

<!-- ANNOTATION: Another silent scene. The UI action (one click, report generated, URL copied) speaks for itself. Adding VO here would reduce the impact of seeing how simple it is. -->

| Field | Content |
|-------|---------|
| **Scene** | 8 -- The Wow Moment |
| **Act** | Demonstration |
| **Duration** | 8s |
| **On Screen** | Timeline view. Left side: "3:41:12 PM -- Latency anomaly detected." Center: "3:41:18 PM -- Root cause identified: deploy #847." Right: "3:41:22 PM -- Incident report shared to #backend." Below: "Customer impact: 0. Time to resolution: 10 seconds." |
| **Text Overlay** | "10 seconds." |
| **Voiceover** | "Detected, diagnosed, and shared in ten seconds. Before your customer refreshed the page." |
| **Music/Sound** | Music peaks. Clean, confident. |
| **Emotional Beat** | The punch. This is what fast looks like. |
| **Transition** | Dissolve to closing. |

<!-- ANNOTATION: The wow moment is the narrative climax. Everything built to this. The specific timeline (10 seconds, three steps) makes it tangible. "Before your customer refreshed the page" gives the metric a human anchor. -->

| Field | Content |
|-------|---------|
| **Scene** | 9 -- The Proof |
| **Act** | Promised Land |
| **Duration** | 5s |
| **On Screen** | Three metric cards animate in: "94% faster incident detection" / "67% reduction in customer-facing errors" / "Teams ship 2x more endpoints with confidence" |
| **Text Overlay** | (metrics ARE the visual) |
| **Voiceover** | "Teams on Conduit catch issues ninety-four percent faster." |
| **Music/Sound** | Music settling into confident sustain. |
| **Emotional Beat** | Credibility. The numbers are real. |
| **Transition** | Metrics fade. |

| Field | Content |
|-------|---------|
| **Scene** | 10 -- The Promised Land |
| **Act** | Promised Land |
| **Duration** | 6s |
| **On Screen** | Clean dark screen. Text fades in: "Know before your customers do." |
| **Text Overlay** | "Know before your customers do." |
| **Voiceover** | "Know before your customers do." |
| **Music/Sound** | Music resolves. Single sustained chord. |
| **Emotional Beat** | Aspiration. This is your new standard. |
| **Transition** | Fade to end card. |

<!-- ANNOTATION: Aspirational close. Not "sign up at conduit.io" -- that's for the end card. The last thing the viewer hears is a statement about THEM and their new capability, not about the product. -->

| Field | Content |
|-------|---------|
| **Scene** | 11 -- End Card |
| **Act** | Promised Land |
| **Duration** | 5s |
| **On Screen** | Conduit logo centered. Below: "conduit.dev" and "Start monitoring in 5 minutes." |
| **Text Overlay** | "conduit.dev" / "Start monitoring in 5 minutes." |
| **Voiceover** | [silence] |
| **Music/Sound** | Music fades out. |
| **Emotional Beat** | Clear next step. |
| **Transition** | End. |

---

## Example 2: "Undo" -- Git History Rewriter

**Archetype**: Playful Rebellion (Arc-like)
**Duration**: 55 seconds (9 scenes)
**Framework**: Before-After-Bridge

### Narrative Foundation

- **The Shift**: Every developer has mass-committed with a message they regret. Git history is a mess and everyone pretends it's fine.
- **The Stakes**: Messy git history makes debugging harder, onboarding slower, and blame meaningless.
- **The Hero**: Developer who writes great code but treats git commits like a save button.
- **The Villain**: `git commit -m "fix"`, `git commit -m "stuff"`, `git commit -m "please work"`.
- **Magic Gifts**: (1) AI rewrites commit messages based on actual diffs. (2) Squashes related commits into logical units. (3) One command, entire branch cleaned.
- **The Wow Moment**: A branch with 23 commits like "wip", "fix", "ugh" transformed into 5 clean, descriptive commits in one command.
- **The Hook**: A real git log that everyone has seen in their own repos.

---

### Script

| Field | Content |
|-------|---------|
| **Scene** | 1 -- The Log of Shame |
| **Act** | Hook |
| **Duration** | 5s |
| **On Screen** | Terminal. `git log --oneline` output scrolling: "fix", "wip", "stuff", "please work", "final final", "ok actually final", "WHY", "tuesday". |
| **Text Overlay** | -- |
| **Voiceover** | "You've seen this git log. You've written this git log." |
| **Music/Sound** | Upbeat indie electronic. Playful energy from the start. |
| **Emotional Beat** | Recognition. A laugh of guilt. |
| **Transition** | Terminal stays, cursor blinks. |

<!-- ANNOTATION: Playful Rebellion opens with shared embarrassment, not pain. The tone is "we all do this, it's fine, but also... what if we didn't?" The specific commit messages are funnier and more relatable than any description of the problem. -->

| Field | Content |
|-------|---------|
| **Scene** | 2 -- The Consequences |
| **Act** | Escalation |
| **Duration** | 7s |
| **On Screen** | Three quick cuts: (1) `git blame` showing "fix" as the commit message for a critical line. (2) New team member scrolling through incomprehensible history trying to understand a feature. (3) PR review comment: "Can you clean up these commits before merge?" |
| **Text Overlay** | -- |
| **Voiceover** | "Until someone runs git blame. Or a new hire reads your history. Or your PR gets sent back." |
| **Music/Sound** | Music continues, slight comedic timing on each cut. |
| **Emotional Beat** | Escalating cringe. It's funny but it's also real. |
| **Transition** | Quick cut to black. |

| Field | Content |
|-------|---------|
| **Scene** | 3 -- The After (shown early) |
| **Act** | Escalation |
| **Duration** | 5s |
| **On Screen** | Same terminal. Same branch. But the git log now reads: "Add rate limiting to /api/search", "Refactor auth middleware for token refresh", "Fix edge case in pagination when cursor is null", "Update search index schema for v2 fields", "Add integration tests for rate-limited endpoints". Clean, descriptive, logical. |
| **Text Overlay** | -- |
| **Voiceover** | [silence] |
| **Music/Sound** | Music lifts. Moment of clarity. |
| **Emotional Beat** | Desire. You want YOUR log to look like this. |
| **Transition** | Hold for 2 beats. Then cut. |

<!-- ANNOTATION: BAB framework: show the "after" before explaining how. The silence lets the viewer compare the two logs in their head. No VO needed -- the contrast does all the work. -->

| Field | Content |
|-------|---------|
| **Scene** | 4 -- The Bridge |
| **Act** | Turn |
| **Duration** | 4s |
| **On Screen** | Terminal. User types: `undo clean`. Cursor blinks. Enter. |
| **Text Overlay** | "One command." |
| **Voiceover** | "One command. Your entire branch, rewritten." |
| **Music/Sound** | Beat drop. Energy kicks up. |
| **Emotional Beat** | Surprise. That's it? |
| **Transition** | Terminal begins processing. |

| Field | Content |
|-------|---------|
| **Scene** | 5 -- Magic Gift 1: AI Rewrite |
| **Act** | Demonstration |
| **Duration** | 7s |
| **On Screen** | Terminal shows Undo processing. Each old commit message appears, then morphs into a new one. "fix" becomes "Fix null pointer in cursor-based pagination". "stuff" becomes "Add rate limiting middleware to search endpoints". Each rewrite based on the actual diff shown briefly beside it. |
| **Text Overlay** | -- |
| **Voiceover** | "Undo reads every diff and writes the commit message you would have written if you weren't debugging at midnight." |
| **Music/Sound** | Building. Rhythmic pulse matching the rewrites. |
| **Emotional Beat** | Delight. Watching messy work become clean. |
| **Transition** | Continuous terminal recording. |

<!-- ANNOTATION: "the commit message you would have written if you weren't debugging at midnight" -- this is Playful Rebellion voice. It's empathetic, specific, and a little funny. It frames the tool as understanding the developer, not judging them. -->

| Field | Content |
|-------|---------|
| **Scene** | 6 -- Magic Gift 2: Smart Squash |
| **Act** | Demonstration |
| **Duration** | 6s |
| **On Screen** | Visual: 23 commits on the left, arrows grouping related ones, 5 clean commits on the right. Animation shows commits sliding together into logical groups. |
| **Text Overlay** | "23 commits. 5 logical changes." |
| **Voiceover** | "Twenty-three commits become five. Grouped by what they actually changed, not when you hit save." |
| **Music/Sound** | Satisfying merge sounds. Music building. |
| **Emotional Beat** | Satisfaction. Order from chaos. |
| **Transition** | Cut to the wow moment. |

| Field | Content |
|-------|---------|
| **Scene** | 7 -- The Wow Moment |
| **Act** | Demonstration |
| **Duration** | 7s |
| **On Screen** | Full before/after split. Left: the original 23-commit log of shame. Right: the cleaned 5-commit log. Terminal shows: "Done. 23 commits rewritten to 5. Branch history cleaned." Elapsed time counter at bottom: "2.3 seconds." |
| **Text Overlay** | "2.3 seconds." |
| **Voiceover** | [silence] |
| **Music/Sound** | Music peaks. Clean resolution. |
| **Emotional Beat** | The punch. Messy to clean in 2 seconds. |
| **Transition** | Hold for a beat. Dissolve. |

<!-- ANNOTATION: The wow moment is silent. The visual contrast (23 messy vs 5 clean) and the timer (2.3 seconds) tell the entire story. VO would diminish it. This is the scene the viewer remembers and tells someone about. -->

| Field | Content |
|-------|---------|
| **Scene** | 8 -- The Promise |
| **Act** | Promised Land |
| **Duration** | 6s |
| **On Screen** | Clean terminal. Cursor blinking after a fresh `git log --oneline` showing beautiful, descriptive commits. |
| **Text Overlay** | "Write messy. Ship clean." |
| **Voiceover** | "Write messy. Ship clean." |
| **Music/Sound** | Music resolving. Warm, confident. |
| **Emotional Beat** | Permission. It's okay to be messy -- now there's a way out. |
| **Transition** | Fade to end card. |

<!-- ANNOTATION: "Write messy. Ship clean." -- aspirational, not logistical. It reframes the product as permission to work the way you already work, without guilt. The close is about the developer's workflow, not the product's features. -->

| Field | Content |
|-------|---------|
| **Scene** | 9 -- End Card |
| **Act** | Promised Land |
| **Duration** | 8s |
| **On Screen** | Undo logo. Below: `brew install undo` and "Free for personal use." |
| **Text Overlay** | `brew install undo` / "Free for personal use." |
| **Voiceover** | [silence] |
| **Music/Sound** | Music fades. |
| **Emotional Beat** | Low barrier. Try it now. |
| **Transition** | End. |

---

## Annotations Key

The inline comments throughout these scripts explain the narrative principles in action:

- **Hook technique** -- How the opening creates tension or recognition in under 5 seconds.
- **Villain specificity** -- The old way is shown concretely, not described abstractly.
- **Silence as tool** -- Scenes without voiceover that let UI or text carry the moment.
- **Wow moment construction** -- How the script builds to one climactic beat.
- **Aspirational close** -- Ending on what the viewer gains, not what the product does.
- **Voice archetype consistency** -- How word choice and tone maintain the chosen archetype throughout.

When creating new scripts, use these examples as structural references but always find the authentic voice for the specific product and audience.
