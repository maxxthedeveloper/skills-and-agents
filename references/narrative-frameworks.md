# Narrative Frameworks for Tech Video

Three frameworks for structuring product announcement videos, each suited to different contexts. The primary framework (Raskin's Strategic Narrative) maps directly to the 5-act video structure used in this skill.

---

## 1. Andy Raskin's Strategic Narrative (Primary)

The core framework. Best for videos 60 seconds and longer where you have room to build a full arc.

### The 5 Steps

1. **Name a big, relevant change in the world** -- Not about your product. About a shift that is happening whether or not your product exists.
2. **Show there will be winners and losers** -- Stakes. If you adapt, you win. If you don't, you fall behind.
3. **Tease the promised land** -- The future state for those who adapt. Concrete and desirable.
4. **Introduce magic gifts** -- Your product's capabilities, framed as tools that get the hero to the promised land.
5. **Show proof** -- Evidence that the promised land is real and achievable.

### Mapping to Video Acts

| Raskin Step | Video Act | Purpose in Video |
|-------------|-----------|-----------------|
| Name the change | Hook | The opening line or visual that names the shift |
| Winners and losers | Escalation | Show the old way, the frustration, the cost of inaction |
| Tease promised land | The Turn | The moment the product appears as the bridge to the future |
| Magic gifts | Demonstration | Product walkthrough, feature highlights, the wow moment |
| Show proof | Promised Land | Evidence + aspirational close |

### Worked Example: "CodeLens" (hypothetical AI code review tool)

**The Shift**: "Codebases doubled in size in the last three years. Code review did not keep up."

**Winners and Losers**: Teams that still review code the old way -- file-by-file, line-by-line, three days per PR -- ship slower every quarter. Teams that adapted review 10x the code in half the time.

**Promised Land**: Every pull request reviewed in minutes, not days. Critical bugs caught before they reach staging. Your senior engineers spend time designing systems, not reading diffs.

**Magic Gifts**:
1. [Before: Read every line of a 2,000-line PR] -> [After: AI highlights the 40 lines that matter]
2. [Before: Context-switch to understand unfamiliar code] -> [After: Inline explanations of intent and risk]
3. [Before: Bugs found in staging or production] -> [After: Logic errors flagged at PR time with fix suggestions]

**Proof**: "Teams using CodeLens merge PRs 3x faster with 60% fewer production bugs in the first 90 days."

**How this becomes a video script**:

- **Hook (0-5s)**: Text card -- "Codebases doubled. Code review didn't." Dark screen, stark typography.
- **Escalation (5-18s)**: Split screen. Left: developer scrolling through a massive diff, rubbing eyes, clock spinning. Right: Slack messages piling up -- "is this PR approved yet?" VO: "The average pull request takes three days to review. Your best engineers spend more time reading code than writing it."
- **Turn (18-24s)**: Screen clears. CodeLens logo fades in. VO: "CodeLens reads every line so your team reviews what matters."
- **Demonstration (24-48s)**: Screen recording of CodeLens in action. PR opens, AI highlights 40 critical lines out of 2,000. Inline annotation explains a subtle race condition. One-click fix suggestion applied. [silence] as the UI animates. **Wow moment at ~40s**: Side-by-side -- the same PR, one reviewed manually in fragments over 3 days, one reviewed with CodeLens in 8 minutes.
- **Promised Land (48-60s)**: VO: "Ship on Friday. Not next Tuesday." Metric card: "3x faster merges. 60% fewer production bugs." End card with logo.

---

## 2. Before-After-Bridge (Secondary)

Best for short videos under 45 seconds where you need to move fast. Three-part structure.

### The 3 Steps

1. **Before** -- Show the current painful reality. Make the audience nod in recognition.
2. **After** -- Show the transformed state. Make it feel tangible and desirable.
3. **Bridge** -- Reveal the product as the bridge between before and after.

### Mapping to Video Acts

| BAB Step | Video Act | Timing |
|----------|-----------|--------|
| Before | Hook + Escalation | 0-35% |
| After | Promised Land (shown early) | 35-50% |
| Bridge | Turn + Demonstration | 50-100% |

Note: In BAB, you show the "after" before explaining how you get there. This creates desire before revealing the mechanism.

### Worked Example: "DraftTable" (hypothetical database UI builder)

**Duration**: 35 seconds

- **Before (0-12s)**: Screen recording of a developer writing SQL queries, copying results into a spreadsheet, formatting cells, sharing a Google Sheet link. VO: "Every internal tool starts the same way. Query, copy, paste, format, share, repeat."
- **After (12-18s)**: Clean UI showing a polished data table with filters, sorting, inline editing. VO: "What if the query was the tool?" [silence] as the interface animates.
- **Bridge (18-35s)**: DraftTable demo. Write a SQL query, hit enter, get a shareable app with auth and permissions. VO: "DraftTable turns any query into a production tool. No frontend. No deploy. Just the data your team needs." End card.

### When to Use BAB

- Social media ads (15-45 seconds)
- Feature update teasers
- Product Hunt launch videos
- Any context where you need maximum impact in minimum time

---

## 3. Problem-Agitate-Solve (Tertiary)

Best when the audience already feels the pain. You lean into the frustration before offering relief.

### The 3 Steps

1. **Problem** -- State the problem clearly and specifically.
2. **Agitate** -- Twist the knife. Show the consequences, the cascading failures, the hidden costs.
3. **Solve** -- Present the product as the resolution.

### Mapping to Video Acts

| PAS Step | Video Act | Timing |
|----------|-----------|--------|
| Problem | Hook | 0-15% |
| Agitate | Escalation (extended) | 15-40% |
| Solve | Turn + Demonstration + Promised Land | 40-100% |

Note: PAS spends more time on the problem than the other frameworks. The agitation phase is where the emotional energy lives.

### Worked Example: "NightOwl" (hypothetical on-call management tool)

**Duration**: 75 seconds

- **Problem (0-10s)**: Phone buzzes at 3:17 AM. Screen lights up a dark room. Alert: "CPU usage > 95% on prod-api-3." VO: "Nobody becomes an engineer to get woken up at 3 AM."
- **Agitate (10-30s)**: Montage of escalation. Engineer opens laptop, squints at dashboard. Wrong runbook. Pings the wrong Slack channel. Incident drags to 47 minutes. Next morning: bleary standup, missed context, same alert fires again Tuesday. VO: "The alert is never just the alert. It's the wrong runbook, the missing context, the 47-minute scramble, and the same page next week because nothing changed." [silence, 2 seconds] Text overlay: "It does not have to be this way."
- **Solve -- Turn (30-38s)**: NightOwl interface appears. Same alert, different response. VO: "NightOwl gives every alert the context to fix it."
- **Solve -- Demonstration (38-62s)**: Alert fires. NightOwl shows: likely root cause (deploy 23 minutes ago), relevant runbook auto-attached, previous incidents with this service, suggested fix. Engineer applies fix from phone. Incident resolved in 6 minutes. **Wow moment**: Timeline view -- every incident this quarter, average resolution dropping from 40 minutes to 8. [silence] as the graph animates.
- **Solve -- Promised Land (62-75s)**: VO: "Sleep through the night. Fix what matters in minutes, not hours. And stop fighting the same fires." End card with logo and metric: "8-minute average resolution."

### When to Use PAS

- Audiences who are actively frustrated (infra engineers, ops teams, anyone with pager fatigue)
- Products replacing painful legacy tools
- B2B videos targeting mid-market and enterprise buyers who live with the pain daily
- Videos shown in sales sequences where the viewer has already expressed interest

---

## Choosing a Framework

| Context | Framework | Why |
|---------|-----------|-----|
| Full product launch, 60s+ | Raskin Strategic Narrative | Room for the full arc, builds strategic context |
| Short social/teaser, under 45s | Before-After-Bridge | Maximum impact, minimum time, desire before mechanism |
| Audience already in pain | Problem-Agitate-Solve | Validates their frustration, earns trust through empathy |
| Changelog or feature update | BAB or abbreviated Raskin | Skip the grand shift, focus on before/after of the specific feature |
| Paradigm-shift product | Raskin (full) | The shift framing is essential when the category is new |
