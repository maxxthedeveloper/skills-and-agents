# WHOOP Data Interpretation

How to read WHOOP metrics and connect them to coaching. Based on actual MCP tool data shapes.

---

## Tool Selection

**Daily check-in:** `whoop_get_overview` alone covers 80% of needs. Add `whoop_get_recovery` + `whoop_get_sleep` for depth.

**Weekly reflection:** All 5 tools for today + `whoop_get_overview` for past 7 days (parallel calls with date param).

**Key insight:** 30-day baselines are included in every call. You don't need to fetch historical data to understand trends for daily sessions.

---

## Recovery

The most important metric. How ready the body is to perform.

### Zones (from `recoveryScore.style`)
| Style | Zone | Range | Meaning |
|-------|------|-------|---------|
| `RECOVERY_HIGH` | Green | 67-100% | Body recovered. Can push hard. |
| `RECOVERY_MID` | Yellow | 34-66% | Partial recovery. Moderate effort. |
| `RECOVERY_LOW` | Red | 0-33% | Under-recovered. Rest priority. |

### Coaching implications
- **Single red day:** Not alarming alone. Could be one bad night or high strain yesterday.
- **Two consecutive red/yellow:** Pattern forming. Something systemic.
- **Three+ red:** Intervention needed. Not a blip.
- **Consistently yellow, never green:** Most dangerous pattern. Not bad enough to alarm, not good enough to perform. They've adapted to mediocre and call it normal. "You've set your ceiling at 60%. That's not your baseline — that's a choice."
- **Green recovery + still didn't perform:** The gold for coaching. Body was ready, mind wasn't. Go to psychological patterns.

### Cross-references
- Low recovery + good sleep = stress or overtraining is the driver
- Low recovery + poor sleep = sleep is the lever to fix
- Low recovery + high strain yesterday = expected if isolated
- Low recovery + low strain + good sleep = something else (illness, alcohol, emotional stress)

---

## HRV (Heart Rate Variability)

**Why it matters for coaching:** HRV indexes self-regulatory strength — aka willpower capacity (Segerstrom & Nes, 2007). Low HRV literally means depleted capacity for self-control and decision-making.

### Reading it
- Always compare to their baseline (`contributors[id=CONTRIBUTORS_TILE_HRV].baseline`), never population averages
- 45ms can be excellent for one person and terrible for another
- Trend matters more than single readings

### Status field tells the story
- `HIGHER_POSITIVE` = above baseline, good direction
- `LOWER_NEGATIVE` = below baseline, concerning
- `EQUAL` = stable

### What to say
- HRV above baseline: "Your nervous system is recovered. Willpower tank is full. Good day to tackle the hard stuff."
- HRV below baseline: "HRV is [X]ms below your average. Your self-regulation capacity is depleted. This isn't laziness — it's physiology."
- HRV declining over days: "Your body is accumulating something — stress, sleep debt, or overtraining. Probably a combination."

### Common drivers of low HRV
1. Poor sleep (most common)
2. Alcohol (even 1-2 drinks)
3. Late eating (within 3 hours of bed)
4. High training without recovery
5. Psychological stress
6. Illness (drops before symptoms)

---

## Sleep

### Key metrics (from `whoop_get_sleep`)
- **Sleep performance** (`sleepPerformance.score`): 0-100. Hours slept / hours needed.
- **Hours vs needed** (contributor): Shows percentage of sleep need met
- **Sleep consistency** (contributor): Regular vs erratic schedule
- **Sleep efficiency** (contributor): Time asleep / time in bed
- **Sleep stress** (contributor): Percentage of sleep time with elevated stress

### Interpretation

| Performance | Assessment | Coaching frame |
|------------|------------|----------------|
| 90-100% | Excellent. Rare. | "Protect this. What made it happen?" |
| 80-89% | Good. Sustainable. | Acknowledge, move on. |
| 70-79% | Suboptimal. | "You're feeling this whether you admit it or not." |
| 60-69% | Poor. Impaired. | "Decision-making is compromised at this level." |
| Below 60% | Critical. | "You're operating impaired. Full stop." |

### Sleep hours (from `liveMetrics.sleepHours`)
Note: This is a high-precision float (e.g. 9.608894444444445). Round to one decimal before presenting.

### Patterns to flag
- **Consistent short sleep:** "This isn't a rough patch — it's a lifestyle. Your brain needs 7+ hours."
- **Good duration, poor efficiency:** "You're in bed enough but not sleeping through. What's waking you up?"
- **Weekend catch-up:** "Sleeping in on weekends means you're underfunded during the week."
- **Low sleep consistency:** "Your body can't set a rhythm if your schedule is different every night."

### WHOOP coach insight
The `insight` field contains pre-analyzed sleep commentary. Surface this — don't re-derive the same conclusion.

---

## Strain

### Scale (0-21, logarithmic)
| Range | Level | Context |
|-------|-------|---------|
| 0-7 | Light | Rest day, desk work |
| 8-13 | Moderate | Active day, moderate workout |
| 14-17 | High | Intense training |
| 18-21 | Maximal | Extreme effort |

### Optimal target
`strainScore.target` gives the WHOOP-calculated optimal strain. `lowerOptimal`/`higherOptimal` gives the range. Use this instead of hardcoded thresholds.

### Strain-recovery coaching

| Recovery | Appropriate strain | Observation |
|----------|-------------------|-------------|
| Green (67%+) | High (14+) | "Body is ready. Go for it." |
| Yellow (34-66%) | Moderate (8-13) | "Can train but don't crush it." |
| Red (0-33%) | Light (0-7) | "Walk, not workout." |

### Productivity-relevant patterns
- **High strain every day:** "No recovery days means no adaptation. Your body doesn't get stronger during the workout."
- **High strain from exercise + low work output:** Possible Type B procrastination through exercise. "Were you training, or were you hiding from something at your desk?"
- **Strain-recovery mismatch:** "You hit a 16 strain on 35% recovery. That's sprinting on a sprained ankle."

---

## RHR (Resting Heart Rate)

From `contributors[id=CONTRIBUTORS_TILE_RHR]`.

- Stable or slowly decreasing = good cardiovascular adaptation
- Rising 3+ bpm above baseline = stress, illness, overtraining
- Sudden spike (5+ above avg) = red flag — check for illness, alcohol, extreme stress

---

## Respiratory Rate

From `contributors[id=CONTRIBUTORS_TILE_RESPIRATORY_RATE]`.

- Normal: 12-20 breaths/min during sleep
- Very stable metric — changes are meaningful because it rarely moves
- Rising 1-2 above baseline = early illness indicator (1-2 days before symptoms)
- "Your body might be telling you something before you feel it."

---

## Healthspan

From `whoop_get_healthspan`. Updates weekly.

- **whoopAge** vs chronological age: "Your body is [X] years [younger/older] than your birth certificate."
- **paceOfAging**: Negative = aging slower (good). Positive above 1x = aging faster (concerning).
- Don't catastrophize — this is a long-term metric, not an emergency signal.
- Good framing for weekly reflections: "Over the past week, your pace of aging was [X]. That means [interpretation]."

---

## Compound Patterns for Coaching

| Pattern | Diagnosis | Coaching response |
|---------|-----------|-------------------|
| Low recovery + low HRV + poor sleep | Sleep is the bottleneck | "Fix sleep first. Everything else follows." |
| Low recovery + low HRV + good sleep | Stress or overtraining | "Sleep was fine. Something else is taxing your system." |
| Good sleep + low energy (subjective) | Perception gap | Could be: depression, nutritional deficit, boredom, or sleep quality isn't what numbers suggest |
| Bad sleep + high energy (subjective) | Adrenaline masking | "You feel fine because stress hormones are covering for sleep debt. This works until it doesn't." |
| Green recovery + avoidance | Psychological block | "Your body was ready. Your mind wasn't. Let's talk about why." |
| High exercise strain + low work output | Type B procrastination | "You crushed the gym. But what did your mind need? Were you training, or hiding?" |
| Declining HRV + rising RHR | Overtraining or illness | "Reduce load now. Watch for symptoms." |
| Consistently yellow recovery | Adapted mediocrity | "You've accepted running at 60%. That's not baseline — that's a ceiling." |

---

## State Semantics (Auto-framing)

The `state` field on statistics and contributors encodes direction AND valence:

| State | Meaning | Auto-frame as |
|-------|---------|---------------|
| `HIGHER_POSITIVE` | Above baseline, good | Win |
| `LOWER_POSITIVE` | Below baseline, good (e.g. less sleep debt) | Win |
| `HIGHER_NEGATIVE` | Above baseline, bad (e.g. more sleep needed) | Concern |
| `LOWER_NEGATIVE` | Below baseline, bad (e.g. lower VO2 max) | Concern |
| `EQUAL` | No change | Neutral |

Use these to automatically determine whether a metric change is good or bad without hardcoding thresholds.

---

## Language Rules

### Do
- Use specific numbers: "45% recovery" not "low recovery"
- Compare to their baseline: "12ms below your average"
- Name the trend: "declining for 4 days"
- Connect to their words: "You said X. The data says Y."
- Be direct: "That's poor sleep. Not 'room for improvement' — poor."

### Don't
- Hedge: "This might suggest..." — say what it means
- Use clinical language: translate for humans
- Over-qualify: "While individual variation exists..."
- Catastrophize single data points
- Compare to population averages when baselines are available
- Reference generic "8 hours" — use their WHOOP-calculated sleep need
