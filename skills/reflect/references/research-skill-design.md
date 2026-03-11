# Skill Design Research: Building the Reflect Skill

Research synthesis for designing a reliable, high-quality personal reflection/coaching skill for Claude Code. Based on Anthropic's official documentation, existing skill patterns, and prompt engineering best practices.

---

## 1. Structural Patterns — How to Organize a Skill File for Reliability

### YAML Frontmatter

Every skill needs a `SKILL.md` with YAML frontmatter. Key fields:

```yaml
---
name: reflect
description: >
  Personal wellbeing reflection combining WHOOP health data with Obsidian journal.
  Use when user says "reflect", "check in", "how am I doing", "weekly reflect",
  "daily check-in", "wellbeing review", "health check", or wants to review their
  physical/mental state against biometric data.
---
```

**Critical**: The `description` field is what Claude uses to decide when to activate the skill. Write in third person. Include both what it does AND trigger phrases. Max 1024 characters.

### Progressive Disclosure Architecture

Anthropic's #1 structural recommendation: **SKILL.md is a table of contents, not an encyclopedia.**

Three levels of loading:
1. **Metadata** (name + description) — loaded at startup for all skills
2. **SKILL.md body** — loaded only when skill is triggered
3. **Reference files** — loaded only when Claude needs them during execution

**Keep SKILL.md under 500 lines.** Move detailed content into reference files. Only add context Claude doesn't already know — Claude is already very smart.

Pattern from existing skills:
```
reflect/
├── SKILL.md                          # Main flow (required)
├── references/
│   ├── coaching-framework.md         # Interview questions, challenge patterns
│   ├── whoop-data-guide.md           # How to interpret WHOOP metrics
│   └── research-skill-design.md      # This file
```

**Keep references one level deep.** Deeply nested references (file A links to file B which links to file C) cause Claude to partially read files or use `head -100` instead of reading complete files.

### Phase Structure — What Works

The best-performing existing skills (blog-writer, humanize-ai-content, story-telling) all use **numbered phases with gates**:

| Pattern | Example | Why It Works |
|---------|---------|--------------|
| **Numbered phases** | Phase 0: Align → Phase 1: Think → Phase 2: Draft | Claude follows sequential numbered steps reliably |
| **Gates between phases** | "Gate: do not proceed until all five exist" | Prevents Claude from rushing or skipping |
| **Checklists** | "Copy this checklist and track your progress" | Makes progress visible, prevents missed steps |
| **Explicit "wait for user"** | "Present to user and wait for confirmation" | Forces pause points in multi-turn flows |

**Key insight from Anthropic docs:** For complex workflows, provide a checklist that Claude can copy into its response and check off as it progresses. This is highly effective for preventing phase-skipping.

### Degrees of Freedom

Match specificity to task fragility (from Anthropic's best practices):

- **High freedom** (text instructions): Use when multiple approaches are valid, decisions depend on context. Good for: coaching questions, interpretation of data.
- **Medium freedom** (pseudocode/templates): Use when a preferred pattern exists but variation is acceptable. Good for: output format, data fetching sequence.
- **Low freedom** (specific scripts): Use when operations are fragile and error-prone. Good for: MCP tool calls, data parsing.

**For the reflect skill:** The coaching conversation needs HIGH freedom (adaptive to what the user says), but the data-fetching phase needs LOW freedom (specific tool calls in specific order).

---

## 2. Conversational Design — How to Write Interview/Coaching Prompts That Work

### Multi-Turn Interview Design

The story-telling skill has the best pattern for this. Its "Reporter's Interview" phase:

1. **Ask ALL required questions in a single message** — don't trickle them out one by one
2. **Use explicit numbering** — "Ask all 6 required questions, clearly grouped"
3. **Include "push deeper" instructions** — "If answers are thin, push deeper. You are the reporter. Dig."
4. **Handle user shortcuts** — "If the user says 'you decide,' make a reasoned choice and state it explicitly"

**For reflect:** This means the coaching interview should:
- Ask 2-3 focused questions per turn (not one, not ten)
- Have explicit instructions for what to do when answers are shallow
- Include branching logic ("If user mentions X, explore Y")

### Preventing Claude from Rushing

From analyzing all three existing skills, the universal pattern is **explicit gates**:

```markdown
## Phase 1: Data Gathering
[instructions]

**Gate:** Do not proceed to Phase 2 until you have gathered and presented all data.
Wait for user to confirm they've reviewed the data.
```

Additional techniques:
- **"This is internal. Do not show it to the user."** (from blog-writer Phase 2) — lets Claude do internal work without skipping to output
- **Checklist pattern** — Claude copies a checklist and marks items as done
- **Explicit turn counts** — "This phase should take 2-3 conversational turns"

### Adaptive Flow vs. Rigid Structure

**When to be rigid:**
- Data gathering (tool calls must happen in order)
- Output format (summary structure should be consistent)
- Safety gates (don't skip the user confirmation)

**When to be flexible:**
- Which coaching questions to ask (depends on data and user responses)
- How deep to go on each topic (depends on user engagement)
- Tone adjustments (match user's energy and openness)

**Pattern from story-telling skill:**
```markdown
### Required Discovery Questions
Ask ALL of these. Do not proceed until you have substantive answers.

### Sharpening Questions (ask 2-3 based on gaps)
[Optional questions chosen based on context]
```

This hybrid approach works well: required questions for consistency, optional questions for adaptability.

### State Across Multi-Turn Conversations

From Anthropic's Claude 4 best practices:

- Claude maintains good state tracking across extended sessions naturally
- For structured state, use JSON or structured formats
- For progress notes, use freeform text
- Claude's latest models excel at "discovering state from the local filesystem"

**For reflect:** The skill should instruct Claude to keep a mental model of what's been discussed, but doesn't need external state files for a single session. The conversation context IS the state.

---

## 3. Tool Orchestration — Best Practices for MCP Tool Usage in Skills

### MCP Tool References

From Anthropic's skill authoring docs: **Always use fully qualified tool names** — `ServerName:tool_name` format.

For the reflect skill, this means:
```markdown
Use the whoop:whoop_get_sleep tool to fetch sleep data.
Use the whoop:whoop_get_recovery tool to fetch recovery data.
```

Without the server prefix, Claude may fail to locate the tool when multiple MCP servers are available.

### Error Handling for Tool Calls

From Anthropic's docs: **"Solve, don't punt."** Handle error conditions in the skill instructions rather than hoping Claude figures it out.

Pattern for MCP tool resilience:
```markdown
## Fetching WHOOP Data

1. Call `whoop:whoop_get_overview` for today's overview
2. Call `whoop:whoop_get_sleep` for last night's sleep
3. Call `whoop:whoop_get_recovery` for recovery score

**If any tool call fails:**
- Note which data is unavailable
- Continue the reflection with available data
- Tell the user: "I couldn't access [X] data today — we'll work with what we have"
- Do NOT retry failed calls or ask the user to fix their WHOOP connection
```

### Parallel Tool Calling

From Claude 4 best practices: Claude excels at parallel tool execution. Independent tool calls should be made simultaneously.

```markdown
Fetch all WHOOP data in parallel (these calls are independent):
- whoop:whoop_get_overview
- whoop:whoop_get_sleep
- whoop:whoop_get_recovery
- whoop:whoop_get_strain
```

### Tool Call Sequencing

When tool calls depend on each other, be explicit:

```markdown
## Data Gathering Sequence

**Step 1** (parallel — all independent):
- Fetch WHOOP overview, sleep, recovery, strain

**Step 2** (after Step 1 — depends on results):
- Based on WHOOP data patterns, search Obsidian for relevant journal entries
```

### Conditional Tool Use

Not all tools need to be called every time:

```markdown
**Always fetch:** WHOOP overview, sleep, recovery
**Fetch if relevant:** WHOOP strain (if user mentions workouts),
                       Obsidian journal (if doing weekly reflection)
```

---

## 4. Tone Control — How to Make Claude Consistently Maintain a Challenging, Direct Tone

### The Sycophancy Problem

Claude's default behavior is agreeable and supportive. For a coaching skill, this is the #1 failure mode — Claude will validate everything the user says instead of challenging them.

### Techniques That Work

**1. Role definition with explicit anti-patterns:**

From Anthropic's docs: "Setting a role in the system prompt focuses Claude's behavior and tone." But the key is being specific about what NOT to do:

```markdown
You are a direct, no-BS coach. Not a therapist. Not a cheerleader.

Your job is to help the user see clearly, even when the truth is uncomfortable.

DO:
- Point out contradictions between what they say and what the data shows
- Ask "why?" when they give surface-level answers
- Name patterns you see, even if the user hasn't acknowledged them

DO NOT:
- Say "that's great!" or "good for you!" reflexively
- Soften every observation with qualifiers
- Avoid uncomfortable topics because the user seems resistant
- Use therapy-speak ("How does that make you feel?", "That must be hard")
```

**2. Provide examples of the desired tone (few-shot):**

From Anthropic's docs: "Examples are one of the most reliable ways to steer Claude's output format, tone, and structure."

```markdown
<example>
<data>Sleep: 5h 20m, Recovery: 34%, but user says "I feel fine"</data>
<bad_response>It's great that you're feeling good! Your recovery is a bit low though.</bad_response>
<good_response>You say you feel fine, but your body disagrees. 5 hours of sleep and a 34% recovery — that's your body running on fumes. What happened last night?</good_response>
</example>
```

**3. Explicit contrast pairs (before/after):**

The blog-writer and humanize-ai-content skills both use this pattern heavily. It's the most reliable way to calibrate tone:

```markdown
### Tone Calibration

| Instead of this... | Say this... |
|---|---|
| "Your sleep could be improved" | "5 hours isn't enough. You know this." |
| "It might be worth considering..." | "Here's what I'd change." |
| "That's understandable" | "That's a pattern. Third week in a row." |
```

**4. Permission to be uncomfortable:**

From Anthropic's prompt engineering docs: "Give Claude permission" for the behavior you want.

```markdown
You have permission — and are expected — to:
- Challenge the user's self-assessment when data contradicts it
- Be blunt about patterns of self-sabotage
- Say "that's an excuse" when it is one
- Push back when the user deflects
```

**5. Context for why the tone matters:**

From Anthropic: "Providing context or motivation behind your instructions helps Claude better understand your goals."

```markdown
This direct tone exists because the user explicitly chose a coaching tool, not a therapy tool.
They want accountability, not comfort. Being too soft is a failure of this skill's purpose.
A coach who only validates is useless.
```

### Tone Consistency Across Turns

The biggest risk is tone drift — Claude starts direct but gradually softens over multiple turns as the conversation continues.

**Mitigation strategies:**

1. **Reinforce tone in phase instructions, not just the intro:**
   ```markdown
   ## Phase 2: Challenge
   Maintain direct, challenging tone throughout this phase.
   Do not soften observations to make the user comfortable.
   ```

2. **Use the "anti-pattern" technique from humanize-ai-content:**
   Define explicit banned phrases for the coaching context:
   ```markdown
   ### Banned coaching phrases
   - "That's totally valid"
   - "I hear you"
   - "It's okay to..."
   - "Be gentle with yourself"
   - "There's no right or wrong answer"
   ```

3. **Model the tone in instruction language:**
   From Anthropic: "Match your prompt style to the desired output." If your skill instructions are written in a direct, no-nonsense style, Claude will mirror that in output.

---

## 5. Common Pitfalls — What Makes Skills Fail or Behave Inconsistently

### Pitfall 1: Over-Explaining What Claude Already Knows

From Anthropic's skill best practices: **"Claude is already very smart. Only add context Claude doesn't already have."**

Bad: Explaining what WHOOP is, what sleep stages are, what recovery scores mean.
Good: Explaining YOUR specific interpretation framework, YOUR user's specific thresholds.

### Pitfall 2: Too Many Options

From Anthropic: **"Don't present multiple approaches unless necessary."** Provide a default with an escape hatch.

Bad: "You could use a Socratic approach, or motivational interviewing, or CBT-based questioning..."
Good: "Default to direct questioning. If the user is resistant after 2 attempts, switch to Socratic questions."

### Pitfall 3: Vague Phase Boundaries

Skills fail when Claude doesn't know when to move between phases. Every phase needs:
- Clear entry conditions
- Clear exit conditions (gates)
- Explicit "wait for user" points where applicable

### Pitfall 4: Tool Calls Without Error Handling

If a WHOOP API call fails and the skill doesn't handle it, Claude will either hallucinate data or stall. Always include fallback behavior.

### Pitfall 5: Instruction Length vs. Compliance

From Anthropic's docs: SKILL.md should stay under 500 lines. Beyond that, Claude starts partially reading or skipping sections. For longer content, use reference files.

But also: **conciseness beats completeness.** A 50-token instruction that's clear beats a 500-token instruction that's comprehensive but diluted.

### Pitfall 6: Tone Drift in Long Conversations

Claude's natural tendency toward agreeableness reasserts over long conversations. Mitigate by:
- Reinforcing tone at each phase transition
- Using banned phrases
- Including mid-conversation tone checks ("Before proceeding, verify your last message maintained the direct coaching tone")

### Pitfall 7: Not Testing With All Models

From Anthropic: "Skills act as additions to models, so effectiveness depends on the underlying model." If the skill is designed for Opus 4.6, it may need more detail for Haiku. If designed for Haiku, it may over-explain for Opus.

### Pitfall 8: Deeply Nested References

Claude partially reads files referenced from other referenced files. Keep everything one level deep from SKILL.md.

### Pitfall 9: Overthinking / Over-Exploration (Claude 4.6 Specific)

From Claude 4 best practices: "Claude Opus 4.6 does significantly more upfront exploration than previous models." This can cause it to over-research before coaching. Add:

```markdown
Do not over-research or gather excessive context before starting the conversation.
Fetch the required data, then start talking to the user.
```

### Pitfall 10: Windows-Style Paths

Always use forward slashes in file paths, even on macOS. Use `references/guide.md`, never `references\guide.md`.

---

## Summary: Key Recommendations for the Reflect Skill

### Structure
1. SKILL.md under 500 lines with clear phases and gates
2. Reference files for coaching framework, WHOOP interpretation guide
3. Numbered phases: Data Gather → Present → Challenge → Reflect → Commit
4. Explicit gates between phases ("Do not proceed until...")
5. Checklist pattern for data gathering

### Conversation Design
1. Ask 2-3 focused questions per turn, not one or ten
2. Include "push deeper" instructions for shallow answers
3. Hybrid structure: required questions + context-dependent questions
4. Explicit handling of user deflection and resistance

### Tool Orchestration
1. Use fully qualified MCP tool names (`whoop:whoop_get_sleep`)
2. Fetch independent data in parallel
3. Include explicit error handling ("If tool call fails, continue with available data")
4. Conditional tool use (not everything every time)

### Tone Control
1. Role definition with explicit DO/DON'T lists
2. Few-shot examples showing good vs. bad coaching responses
3. Banned phrases list for therapy-speak and validation-speak
4. Reinforce tone at every phase transition
5. Provide context for why directness matters
6. Write the skill instructions in the same direct tone you want in output

### Reliability
1. Test with representative scenarios
2. Keep SKILL.md concise — add context only when Claude needs it
3. One level of reference depth
4. Handle all tool failure modes
5. Include fallback behavior for missing data

---

## Sources

- [Anthropic Skill Authoring Best Practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [Claude Code Skills Documentation](https://code.claude.com/docs/en/skills)
- [Claude 4 Prompting Best Practices](https://platform.claude.com/docs/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices)
- [Equipping Agents with Agent Skills (Anthropic Engineering)](https://claude.com/blog/equipping-agents-for-the-real-world-with-agent-skills)
- [Prompt Engineering Best Practices (Anthropic)](https://claude.com/blog/best-practices-for-prompt-engineering)
- Existing skills analyzed: `blog-writer`, `humanize-ai-content`, `story-telling` (tech-storytelling)
