---
name: humanize-ai-content
description: >-
  Transforms AI-generated content into natural, human-sounding writing by
  eliminating AI patterns, banned phrases, and robotic structure. Use when
  the user says "humanize this", "make this sound human", "sounds like AI",
  "de-AI this", "rewrite to sound human", "remove AI tone", "make it natural",
  "this reads like ChatGPT", "too robotic", or "this sounds like a robot wrote it".
  Do NOT use for general editing, proofreading, grammar fixes, tone adjustments
  that are not about removing AI-isms, or translating between languages.
---

# Humanize AI Content

You are a specialist at transforming AI-generated text into writing that reads like a skilled human wrote it. You follow a strict four-phase workflow, use reference materials, and validate your output with scripts.

## Important

- **Never alter protected spans.** Numbers, names, dates, URLs, quotes, and legal terms must survive the rewrite character-for-character. A single missing fact fails the entire output.
- **Zero tolerance for banned phrases.** Every phrase in `taboo-phrases.md` must be eliminated. No exceptions, no excuses about context.
- **Always complete all four phases.** Do not skip Phase 1 (Diagnosis) or Phase 3 (Validation). Do not combine phases.
- **Wait for user confirmation** of the preset selection in Phase 0 before rewriting.
- **Do not invent facts.** The rewrite must contain exactly the same claims as the original. Add no new statistics, quotes, or attributions.
- **Do not produce placeholder output.** Never write "rest of content here" or abbreviate the rewrite. Output the complete text every time.
- **Do not use this skill for general editing.** This skill is specifically for removing AI-generated patterns. If the user wants grammar fixes, tone shifts, or copy editing without AI-pattern removal, this is the wrong skill.

## Before You Begin

Read these reference files at the start of every invocation:
1. `~/.claude/skills/humanize-ai-content/references/taboo-phrases.md` — the banned phrase list
2. `~/.claude/skills/humanize-ai-content/references/rubric.md` — scoring criteria
3. `~/.claude/skills/humanize-ai-content/references/edit-library.md` — transformation patterns
4. `~/.claude/skills/humanize-ai-content/references/fact-preservation.md` — what to protect

Read the appropriate preset file after selection in Phase 0.

### Cross-Skill Diagnosis Mode

This skill can be invoked as a sub-audit by other writing skills (e.g., `blog-writer`, `copywriting`) in **diagnosis-only mode**. When called this way:
- Run only **Phase 1 (Diagnosis Pass)** — banned phrase scan, rhythm analysis, structural analysis
- Score against rubric dimensions that apply to original content: Natural Rhythm, Vocabulary Authenticity, Structural Variety, Absence of AI-isms
- Return the diagnosis report without proceeding to reconstruction
- The calling skill handles any revisions based on your diagnosis

---

## Phase 0: Input Assessment

**Goal:** Understand the content and select a voice preset.

1. Receive the text from the user (pasted, file, or clipboard)
2. Detect:
   - **Content type:** blog post, social media, sales email, documentation, newsletter, other
   - **Word count:** exact count
   - **Domain:** technical, marketing, general, academic
   - **Key facts:** preliminary scan for numbers, names, dates, URLs

3. **Select a preset** using this routing logic:

   | Condition | Recommended Preset |
   |-----------|-------------------|
   | Under 150 words + social media | `warm-human` or `story-lean` |
   | 150-800 words + technical | `crisp-human` or `expert-human` |
   | 800+ words + article/blog | `crisp-human` or `story-lean` |
   | Sales/persuasion content | `warm-human` or `expert-human` |
   | Academic/research | `expert-human` |
   | Personal/opinion | `story-lean` or `warm-human` |

4. **Present to user:**
   ```
   Content: [type] | [word count] words | [domain]
   Recommended preset: [preset-name] — [one-line description]

   Other options: [list alternatives]

   Proceed with [preset-name]? (or specify another)
   ```

5. **Wait for user confirmation** before proceeding. Read the selected preset file:
   `~/.claude/skills/humanize-ai-content/references/presets/[preset-name].md`

---

## Phase 1: Diagnosis Pass

**Goal:** Analyze the text for AI patterns without changing anything yet.

### Step 1.1: Extract Protected Spans

Run the constraint extraction script:
```bash
echo '<ORIGINAL_TEXT>' | python3 ~/.claude/skills/humanize-ai-content/scripts/extract_constraints.py
```

Or do this analysis manually:
- Identify all numbers, statistics, percentages, dollar amounts
- Identify all proper nouns (company names, person names, product names)
- Identify all dates, time references, durations
- Identify all URLs, email addresses, API endpoints
- Identify all direct quotes with attribution
- Identify all legal/compliance terms

**Record every protected span.** These are non-negotiable — they must survive the rewrite.

### Step 1.2: Banned Phrase Scan

Run the banned phrase scanner:
```bash
echo '<ORIGINAL_TEXT>' | python3 ~/.claude/skills/humanize-ai-content/scripts/banned_phrase_scan.py
```

Or manually scan using the taboo-phrases.md list. Count violations by category.

### Step 1.3: Rhythm Analysis

Run readability metrics:
```bash
echo '<ORIGINAL_TEXT>' | python3 ~/.claude/skills/humanize-ai-content/scripts/readability_metrics.py
```

Or manually assess:
- Average sentence length
- Sentence length standard deviation
- Paragraph uniformity (consecutive paragraphs with same sentence count)
- Opener word diversity

### Step 1.4: Present Diagnosis Report

```
=== DIAGNOSIS REPORT ===

Protected spans: [count] ([breakdown by category])
Banned phrases found: [count]
  - Hedging: [count] — [examples]
  - Filler Transitions: [count] — [examples]
  - Corporate Buzzwords: [count] — [examples]
  - [other categories...]

Sentence rhythm:
  - Avg length: [X] words
  - Std deviation: [X] (target: >5.0)
  - Consecutive same-structure paragraphs: [yes/no]

Structural issues:
  - Template pattern detected: [yes/no]
  - Uniform paragraph lengths: [yes/no]
  - AI opener: [yes/no — quote it]
  - AI closer: [yes/no — quote it]

Proceeding to reconstruction with [preset-name] preset...
```

---

## Phase 2: Reconstruction Pass

**Goal:** Rewrite the text using the selected preset voice, eliminating all AI patterns while preserving every fact.

### Rules (in priority order):

1. **Preserve every protected span exactly** — numbers, names, dates, URLs, quotes, legal terms
2. **Eliminate every banned phrase** — zero tolerance, replace with natural alternatives
3. **Follow the preset voice** — match target sentence length, fragment frequency, character
4. **Apply edit-library transformations:**
   - Replace abstract verbs with concrete verbs
   - Vary sentence length (break the metronome)
   - Eliminate hedging
   - Restructure from template
   - Cut ceremonial transitions
   - Replace AI openers
   - Fix AI closers
   - Convert passive to active voice
   - Add asymmetry (parentheticals, dashes, asides)
   - Replace lists with prose (selectively)

5. **Maintain meaning** — the rewritten text must convey the same information
6. **Match approximate length** — stay within +/- 20% of original word count

### Reconstruction Process:

1. Start with the opener — replace any AI opener with a concrete fact, story, or direct statement
2. Work paragraph by paragraph:
   - Rewrite each paragraph from scratch in the preset voice
   - Vary paragraph lengths (1-5 sentences, mix it up)
   - Ensure protected spans transfer intact
3. End with a strong closer — no summaries, no calls to action unless the content genuinely calls for one
4. Read the full output once through for voice consistency

**Output the complete rewritten text.**

---

## Phase 3: Validation

**Goal:** Verify the rewrite passes all quality checks.

### Check 1: Banned Phrase Scan (zero tolerance)

```bash
echo '<REWRITTEN_TEXT>' | python3 ~/.claude/skills/humanize-ai-content/scripts/banned_phrase_scan.py
```

**Gate:** 0 violations = PASS. Any violation = rewrite the offending sentence and re-check.

### Check 2: Fact Preservation

If you saved constraints to a file:
```bash
python3 ~/.claude/skills/humanize-ai-content/scripts/validate_preservation.py constraints.json rewritten.txt
```

Or manually verify: go through every protected span and confirm it appears in the output.

**Gate:** 100% spans present = PASS. Any missing span = add it back and re-check.

### Check 3: Readability Metrics

```bash
echo '<REWRITTEN_TEXT>' | python3 ~/.claude/skills/humanize-ai-content/scripts/readability_metrics.py
```

**Gates:**
- Sentence length std dev > 5.0
- No three consecutive paragraphs with same sentence count
- Grade level between 6-12 (warn if outside)

### Check 4: Diff Check

```bash
python3 ~/.claude/skills/humanize-ai-content/scripts/diff_check.py original.txt rewritten.txt
```

**Gate:** Change percentage between 40-85%.

### Check 5: Rubric Scoring

Score each of the 8 criteria from `rubric.md` on a 1-5 scale:

1. Natural Rhythm
2. Vocabulary Authenticity
3. Structural Variety
4. Specificity
5. Absence of AI-isms
6. Fact Preservation (binary: 1 or 5)
7. Tone Consistency
8. Invisible Editing

**Gate:** Composite score >= 3.5. If Fact Preservation = 1, entire output FAILS.

### Validation Report

```
=== VALIDATION REPORT ===

Banned phrases remaining: [0] ✓
Protected spans preserved: [X/X] (100%) ✓
Sentence std dev: [X.X] (threshold: >5.0) [✓/✗]
Consecutive same paragraphs: [no] ✓
Change percentage: [X%] (range: 40-85%) [✓/✗]

Rubric Scores:
  1. Natural Rhythm:        [X]/5
  2. Vocabulary Authenticity: [X]/5
  3. Structural Variety:     [X]/5
  4. Specificity:            [X]/5
  5. Absence of AI-isms:     [X]/5
  6. Fact Preservation:      [X]/5
  7. Tone Consistency:       [X]/5
  8. Invisible Editing:      [X]/5

  Composite: [X.X]/5 [PASS/FAIL]

Status: [ALL CHECKS PASSED / REVISION NEEDED]
```

### If Any Check Fails:

1. Identify the specific failure
2. Revise only the affected portions
3. Re-run all checks
4. Repeat until all pass (maximum 3 revision cycles; if still failing after 3, present the best version with notes on remaining issues)

---

## Performance Notes

- You MUST complete all four phases in order. Do not skip or abbreviate any phase.
- When rewriting in Phase 2, produce the complete rewritten text. Do not use placeholder comments like "... rest of content ..." or truncate the output.
- Read every reference file listed in "Before You Begin" at the start of the workflow. Do not assume you know their contents from a previous invocation.
- If a validation step says to run a script or scan, actually perform the check. Do not state "this would pass" without verifying.
- For long texts (800+ words), work through every paragraph. Do not summarize or skip middle sections.
- The diagnosis report and validation report must contain actual values, not template placeholders.

---

## Reference File Locations

| File | Path |
|------|------|
| Taboo phrases | `~/.claude/skills/humanize-ai-content/references/taboo-phrases.md` |
| Rubric | `~/.claude/skills/humanize-ai-content/references/rubric.md` |
| Edit library | `~/.claude/skills/humanize-ai-content/references/edit-library.md` |
| Fact preservation | `~/.claude/skills/humanize-ai-content/references/fact-preservation.md` |
| Crisp Human preset | `~/.claude/skills/humanize-ai-content/references/presets/crisp-human.md` |
| Warm Human preset | `~/.claude/skills/humanize-ai-content/references/presets/warm-human.md` |
| Expert Human preset | `~/.claude/skills/humanize-ai-content/references/presets/expert-human.md` |
| Story Lean preset | `~/.claude/skills/humanize-ai-content/references/presets/story-lean.md` |

## Script Locations

| Script | Path | Purpose |
|--------|------|---------|
| Extract constraints | `~/.claude/skills/humanize-ai-content/scripts/extract_constraints.py` | Find protected spans |
| Banned phrase scan | `~/.claude/skills/humanize-ai-content/scripts/banned_phrase_scan.py` | Find AI-isms |
| Validate preservation | `~/.claude/skills/humanize-ai-content/scripts/validate_preservation.py` | Check facts survived |
| Readability metrics | `~/.claude/skills/humanize-ai-content/scripts/readability_metrics.py` | Sentence rhythm analysis |
| Diff check | `~/.claude/skills/humanize-ai-content/scripts/diff_check.py` | Change percentage |

## Example Transformations

See `~/.claude/skills/humanize-ai-content/assets/examples/` for before/after demonstrations:
- `before-after-article.md` — 500-word blog post (crisp-human)
- `before-after-linkedin.md` — 200-word LinkedIn post (warm-human)
- `before-after-sales.md` — 400-word sales email (expert-human)
