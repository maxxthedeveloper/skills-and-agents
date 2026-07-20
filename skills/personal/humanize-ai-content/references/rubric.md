# Humanization Rubric — 8 Criteria, Scored 1-5

Score each criterion independently. Composite = average of all 8. Minimum passing composite: **3.5**.

---

## 1. Natural Rhythm (1-5)

Does the sentence length vary like real human writing?

| Score | Criteria |
|-------|----------|
| 1 | Nearly uniform sentence lengths (std dev < 3) |
| 2 | Slight variation, still feels mechanical (std dev 3-4) |
| 3 | Moderate variation, some long/short contrast (std dev 4-5) |
| 4 | Good variation, feels natural (std dev 5-6) |
| 5 | Excellent variation, rhythmic and alive (std dev > 6) |

**Measurement:** Standard deviation of word counts per sentence.

---

## 2. Vocabulary Authenticity (1-5)

Are the word choices natural for a human writer in this domain?

| Score | Criteria |
|-------|----------|
| 1 | 5+ banned phrases remain; vocabulary feels synthetic |
| 2 | 2-4 banned phrases remain; occasional AI-isms |
| 3 | 1 banned phrase remains; mostly natural vocabulary |
| 4 | Zero banned phrases; vocabulary appropriate but safe |
| 5 | Zero banned phrases; vocabulary feels genuinely personal and domain-natural |

**Measurement:** Banned phrase count + subjective domain-fit assessment.

---

## 3. Structural Variety (1-5)

Do paragraphs, openers, and section formats vary?

| Score | Criteria |
|-------|----------|
| 1 | Every paragraph follows the same structure (claim → evidence → transition) |
| 2 | Minor variations but a dominant template is obvious |
| 3 | Mix of structures, but some repetitive patterns remain |
| 4 | Good structural variety; paragraphs feel distinct |
| 5 | Each paragraph feels like its own unit; no template visible |

**Measurement:** Paragraph length variance, opener word diversity, no 3+ consecutive paragraphs with same sentence count.

---

## 4. Specificity (1-5)

Are abstract claims replaced with concrete, verifiable details?

| Score | Criteria |
|-------|----------|
| 1 | Mostly abstract ("improve efficiency," "drive results") |
| 2 | Some specifics mixed with vague claims |
| 3 | More specific than abstract; concrete verbs present |
| 4 | Predominantly specific; few remaining abstractions |
| 5 | Every claim grounded in concrete detail, action, or example |

**Measurement:** Ratio of concrete verbs (built, cut, shipped, measured) to abstract verbs (leverage, optimize, transform).

---

## 5. Absence of AI-isms (1-5)

Is the text free from patterns that signal AI generation?

| Score | Criteria |
|-------|----------|
| 1 | Reads like raw ChatGPT output |
| 2 | Some AI patterns removed but structure still feels templated |
| 3 | Most AI patterns gone; occasional tell remains |
| 4 | No obvious AI markers; might pass casual inspection |
| 5 | Indistinguishable from human-written content; zero tells |

**Measurement:** Combination of banned phrase scan, structural analysis, and opener/closer inspection.

---

## 6. Fact Preservation (1-5) — BINARY

Did every protected span survive the rewrite?

| Score | Criteria |
|-------|----------|
| 1 | Any protected span is missing, altered, or approximated |
| 5 | Every number, name, date, URL, quote, and legal term is intact |

**There is no 2, 3, or 4.** This is pass/fail. A single missing fact = score 1.

**Measurement:** `validate_preservation.py` output — 100% spans present = score 5.

---

## 7. Tone Consistency (1-5)

Does the output maintain the selected preset voice throughout?

| Score | Criteria |
|-------|----------|
| 1 | Voice shifts dramatically between sections |
| 2 | Mostly one voice but slips into AI-formal in spots |
| 3 | Consistent voice with minor inconsistencies |
| 4 | Strong voice throughout; rare slips |
| 5 | Voice is unmistakable and sustained from first word to last |

**Measurement:** Check against preset parameters (avg sentence length, fragment frequency, character description).

---

## 8. Invisible Editing (1-5)

Does the output feel like original writing, not a processed rewrite?

| Score | Criteria |
|-------|----------|
| 1 | Clearly a "cleaned up" version — sanitized, safe, flat |
| 2 | Feels edited but still somewhat mechanical |
| 3 | Reads naturally but lacks personality |
| 4 | Feels like a competent human wrote it |
| 5 | Feels like a first draft with genuine voice — quirks, opinions, personality |

**Measurement:** Subjective assessment — does the reader forget this was rewritten?

---

## Scoring Summary

```
Composite Score = (C1 + C2 + C3 + C4 + C5 + C6 + C7 + C8) / 8

Pass threshold: >= 3.5
Excellent: >= 4.0
Outstanding: >= 4.5
```

**If Fact Preservation (C6) = 1, the entire output FAILS regardless of composite score.** Facts are non-negotiable.
