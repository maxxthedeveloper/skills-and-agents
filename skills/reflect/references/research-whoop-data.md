# WHOOP MCP Data Shapes — Research Document

> Analyzed from `/Users/maxx/Documents/cursor/whoop-mcp/` source code + live API calls on 2026-02-28.

## Architecture

The WHOOP MCP server is a proxy chain:
- `proxy.mjs` — local stdio proxy that forwards to a remote Vercel endpoint
- `index.ts` — Express server on Vercel that creates per-request `WhoopClient` instances
- `src/whoop-client.ts` — authenticates via Cognito, calls WHOOP's private iOS API (`api.prod.whoop.com`)
- `src/tools/*.ts` — five tool handlers that transform raw API responses into structured output

All tools accept a single optional `date` param (YYYY-MM-DD, defaults to today).

---

## 1. Tool-by-Tool Data Shapes

### `whoop_get_overview` (home.ts)

The most comprehensive tool. Returns cycle info, live metrics, gauges, activities, and key statistics with 30-day comparisons.

**Structured output shape:**
```ts
{
  cycleInfo: {
    cycleId: number,          // e.g. 1337909037
    cycleDay: string,         // "2026-02-28"
    cycleDateDisplay: string, // "TODAY" | "YESTERDAY" | "Feb 26"
    sleepState: string,       // "complete" | "pending" | etc.
  },
  liveMetrics: {
    recoveryScore: number,    // 0-100, e.g. 82
    dayStrain: number,        // 0-21 scale, e.g. 11.1
    sleepHours: number,       // decimal hours, e.g. 9.608894444444445 (converted from ms_of_sleep)
    calories: number,         // e.g. 2360
  },
  gauges: [                   // Typically 3: SLEEP, RECOVERY, STRAIN
    {
      title: string,          // "SLEEP" | "RECOVERY" | "STRAIN"
      scoreDisplay: string,   // "79" | "82" | "11.1"
      scoreSuffix: string | null, // "%" for sleep/recovery, null for strain
      fillPercentage: number, // 0-1 float, e.g. 0.79
      progressStyle: string,  // "SLEEP" | "RECOVERY_HIGH" | "RECOVERY_LOW" | "RECOVERY_MID" | "STRAIN"
    }
  ],
  journal: {
    completed: boolean,
    hasRecovery: boolean,
    enabled: boolean,
  },
  activities: [               // Today's logged activities
    {
      title: string,          // "SLEEP" | "Running" | "Cycling" etc.
      type: string,           // "SLEEP" | "WORKOUT" etc.
      scoreDisplay: string,   // "9:36" (duration) or strain score
      startTime: string,      // "[Fri] 8:49 PM"
      endTime: string,        // "7:20 AM"
      status: string,         // "COMPLETE" | "IN_PROGRESS"
    }
  ],
  statistics: [               // Key stats with 30-day baselines
    {
      title: string,          // "SLEEP PERFORMANCE" | "VO₂ MAX" | "SLEEP DEBT" etc.
      currentValue: string,   // "79%" | "49" | "0:26"
      thirtyDayAverage: string, // "80%" | "50" | "0:54"
      state: string,          // "LOWER_NEGATIVE" | "LOWER_POSITIVE" | "HIGHER_POSITIVE" | "HIGHER_NEGATIVE" | "EQUAL"
    }
  ],
}
```

**Known statistics titles (from live data):**
- `SLEEP PERFORMANCE` — percentage
- `SLEEP CONSISTENCY` — percentage
- `RESTORATIVE SLEEP (%)` — percentage
- `SLEEP DEBT` — H:MM format
- `SLEEP NEEDED` — H:MM format
- `TIME IN BED` — H:MM format
- `VO₂ MAX` — integer

**State semantics:**
- `LOWER_POSITIVE` = lower than baseline AND that's good (e.g. less sleep debt)
- `LOWER_NEGATIVE` = lower than baseline AND that's bad (e.g. lower VO2 max)
- `HIGHER_POSITIVE` = higher than baseline AND that's good (e.g. more time in bed)
- `HIGHER_NEGATIVE` = higher than baseline AND that's bad (e.g. more sleep needed)
- `EQUAL` = same as baseline

---

### `whoop_get_sleep` (sleep.ts)

Returns sleep performance score, four sleep contributors, and a coach insight.

**Output shape (returned as JSON string in text content):**
```ts
{
  sleepPerformance: {
    score: number,            // 0-100, e.g. 79 (derived from fillPercentage * 100)
    scoreDisplay: string,     // "79"
    fillPercentage: number,   // 0-1, e.g. 0.79
  },
  contributors: [
    {
      id: string,             // "CONTRIBUTORS_TILE_HOURS_V_NEEDED"
      icon: string,           // "HOURS_OF_SLEEP"
      title: string,          // "HOURS VS. NEEDED"
      status: string,         // "94%" — the actual value
      statusSubtitle: string | null, // null for sleep (no baseline shown)
      metricStyle: string,    // "DATA"
    }
  ],
  insight: string | undefined, // Coach VOW text, e.g. "Your Sleep Performance is sufficient..."
}
```

**Known contributor IDs and what they measure:**
| ID | Title | Example Value |
|---|---|---|
| `CONTRIBUTORS_TILE_HOURS_V_NEEDED` | HOURS VS. NEEDED | "94%" |
| `CONTRIBUTORS_TILE_SLEEP_CONSISTENCY` | SLEEP CONSISTENCY | "48%" |
| `CONTRIBUTORS_TILE_IN_SLEEP_EFFICIENCY` | SLEEP EFFICIENCY | "91%" |
| `CONTRIBUTORS_TILE_HIGH_STRESS_SLEEP_DURATION` | HIGH SLEEP STRESS | "0%" |

**Important:** Sleep contributors do NOT include a `statusSubtitle` (baseline), unlike recovery/strain. The `status` field contains the metric value as a pre-formatted string.

---

### `whoop_get_recovery` (recovery.ts)

Returns recovery score, four recovery contributors with 30-day baselines, and a coach insight.

**Structured output shape:**
```ts
{
  title: string,              // "TODAY" | "YESTERDAY" | date display
  recoveryScore: {
    score: string,            // "82" (NOTE: string, not number)
    percentage: number,       // 0-1, e.g. 0.82
    style: string,            // "RECOVERY_HIGH" | "RECOVERY_MID" | "RECOVERY_LOW"
  },
  contributors: [
    {
      id: string,             // "CONTRIBUTORS_TILE_HRV"
      title: string,          // "Heart Rate Variability"
      value: string,          // "74" — current value (from metric.status)
      baseline: string,       // "71" — 30-day avg (from metric.status_subtitle)
      status: string,         // "HIGHER_POSITIVE" | "LOWER_POSITIVE" | "LOWER_NEGATIVE" etc.
      icon: string,           // "HRV_OUTLINE"
    }
  ],
  coachInsight: string | null, // "Your HRV, RHR, and Sleep Performance indicate..."
}
```

**Known contributor IDs and what they measure:**
| ID | Title | Example Value | Example Baseline |
|---|---|---|---|
| `CONTRIBUTORS_TILE_HRV` | Heart Rate Variability | "74" (ms) | "71" |
| `CONTRIBUTORS_TILE_RHR` | Resting Heart Rate | "45" (bpm) | "46" |
| `CONTRIBUTORS_TILE_RESPIRATORY_RATE` | RESPIRATORY RATE | "15.8" (brpm) | "16.0" |
| `CONTRIBUTORS_TILE_SLEEP_PERFORMANCE` | SLEEP PERFORMANCE | "79%" | "80%" |

**Recovery style mapping:**
- `RECOVERY_HIGH` = green zone (67-100%)
- `RECOVERY_MID` = yellow zone (34-66%)
- `RECOVERY_LOW` = red zone (0-33%)

---

### `whoop_get_strain` (strain.ts)

Returns strain score with optimal targets, four contributors with baselines, activities, and coach insight.

**Structured output shape:**
```ts
{
  title: string,              // "TODAY"
  strainScore: {
    score: string,            // "11.1" (NOTE: string)
    percentage: number,       // 0-1 float, e.g. 0.5268
    target: number | null,    // 0-1 optimal target, e.g. 0.657
    lowerOptimal: number | null, // 0-1 lower bound, e.g. 0.562
    higherOptimal: number | null, // 0-1 upper bound, e.g. 0.788
  },
  contributors: [
    {
      id: string,             // "CONTRIBUTORS_TILE_HR_ZONES_1_3"
      title: string,          // "HEART RATE ZONES 1-3"
      value: string,          // "0:00" — H:MM format for time, or "17,317" for steps
      baseline: string,       // "0:32" — 30-day average
      status: string,         // "LOWER_NEGATIVE" | "HIGHER_POSITIVE" etc.
      icon: string,           // "HR_ZONES_1_3"
    }
  ],
  activities: [
    {
      title: string,          // "Morning Run"
      strainScore: string,    // "14.2"
      startTime: string,      // "7:30 AM"
      endTime: string,        // "8:15 AM"
      type: string,           // "WORKOUT"
      status: string,         // "COMPLETE"
    }
  ],
  coachInsight: string | null, // "You're close to your optimal Strain range..."
}
```

**Known contributor IDs:**
| ID | Title | Format | Example |
|---|---|---|---|
| `CONTRIBUTORS_TILE_HR_ZONES_1_3` | HEART RATE ZONES 1-3 | H:MM | "0:00" / "0:32" |
| `CONTRIBUTORS_TILE_HR_ZONES_4_5` | HEART RATE ZONES 4-5 | H:MM | "0:00" / "0:01" |
| `CONTRIBUTORS_TILE_STRENGTH_TRAINING_TIME` | STRENGTH ACTIVITY TIME | H:MM | "0:00" / "0:07" |
| `CONTRIBUTORS_TILE_STEPS` | STEPS (BETA) | comma-formatted int | "17,317" / "11,390" |

---

### `whoop_get_healthspan` (healthspan.ts)

Returns biological age, pace of aging, and comparison with previous period.

**Structured output shape:**
```ts
{
  navigationTitle: string,    // "HEALTHSPAN"
  navigationSubtitle: string, // "NEXT UPDATE IN 1 DAY"
  dateRange: string,          // "Feb 22 - Feb 28" (weekly measurement period)
  isCalibrating: boolean,     // true if not enough data yet
  currentPeriod: {
    whoopAge: string,         // "25.0" (biological age)
    ageStatus: string,        // "3.1 years younger" | "X years older"
    yearsDifference: string,  // "3.1"
    paceOfAging: string,      // "-0.5x" (negative = aging slower)
  },
  previousPeriod: {
    whoopAge: string,         // "25.1"
    paceOfAging: string,      // "-0.3x"
  },
}
```

**Pace of aging interpretation:**
- Negative values (e.g. "-0.5x") = aging slower than average (good)
- "0x" or "1.0x" = aging at average pace
- Positive values above 1x = aging faster than average (concerning)

**Note:** Healthspan updates weekly, not daily. The `dateRange` shows the measurement week.

---

## 2. Key Metrics Map — Quick Reference

| Metric | Tool | Field Path | Format |
|---|---|---|---|
| **Recovery %** | `whoop_get_overview` | `liveMetrics.recoveryScore` | integer 0-100 |
| **Recovery % (alt)** | `whoop_get_recovery` | `recoveryScore.score` | string "82" |
| **Recovery zone** | `whoop_get_recovery` | `recoveryScore.style` | "RECOVERY_HIGH"/"MID"/"LOW" |
| **HRV (ms)** | `whoop_get_recovery` | `contributors[id=CONTRIBUTORS_TILE_HRV].value` | string "74" |
| **HRV baseline** | `whoop_get_recovery` | `contributors[id=CONTRIBUTORS_TILE_HRV].baseline` | string "71" |
| **RHR (bpm)** | `whoop_get_recovery` | `contributors[id=CONTRIBUTORS_TILE_RHR].value` | string "45" |
| **RHR baseline** | `whoop_get_recovery` | `contributors[id=CONTRIBUTORS_TILE_RHR].baseline` | string "46" |
| **Day Strain** | `whoop_get_overview` | `liveMetrics.dayStrain` | float 0-21 |
| **Strain target** | `whoop_get_strain` | `strainScore.target` | float 0-1 |
| **Strain optimal range** | `whoop_get_strain` | `strainScore.lowerOptimal` / `higherOptimal` | float 0-1 |
| **Sleep hours** | `whoop_get_overview` | `liveMetrics.sleepHours` | float (high precision) |
| **Sleep performance %** | `whoop_get_sleep` | `sleepPerformance.score` | integer 0-100 |
| **Sleep efficiency** | `whoop_get_sleep` | `contributors[id=..._IN_SLEEP_EFFICIENCY].status` | string "91%" |
| **Sleep consistency** | `whoop_get_sleep` | `contributors[id=..._SLEEP_CONSISTENCY].status` | string "48%" |
| **Sleep stress** | `whoop_get_sleep` | `contributors[id=..._HIGH_STRESS_SLEEP_DURATION].status` | string "0%" |
| **Calories** | `whoop_get_overview` | `liveMetrics.calories` | integer |
| **Steps** | `whoop_get_strain` | `contributors[id=CONTRIBUTORS_TILE_STEPS].value` | string "17,317" |
| **VO2 Max** | `whoop_get_overview` | `statistics[title=VO₂ MAX].currentValue` | string "49" |
| **Biological age** | `whoop_get_healthspan` | `currentPeriod.whoopAge` | string "25.0" |
| **Pace of aging** | `whoop_get_healthspan` | `currentPeriod.paceOfAging` | string "-0.5x" |
| **Resp. rate** | `whoop_get_recovery` | `contributors[id=CONTRIBUTORS_TILE_RESPIRATORY_RATE].value` | string "15.8" |

---

## 3. Trend Data Availability

### What's available per-call
- **30-day baselines** are included in:
  - `whoop_get_overview` → `statistics[].thirtyDayAverage` (with state comparison)
  - `whoop_get_recovery` → `contributors[].baseline` (30-day avg for HRV, RHR, resp rate, sleep perf)
  - `whoop_get_strain` → `contributors[].baseline` (30-day avg for HR zones, steps, strength time)
- **Week-over-week** for healthspan only: `currentPeriod` vs `previousPeriod`

### What's NOT available
- No multi-day array/history — each call returns a **single-day snapshot**
- No weekly/monthly trend arrays
- No time-series data (no "last 7 days of HRV")

### How to build multi-day trends
To get multi-day data, you must **make separate calls per day**:
```
whoop_get_overview({ date: "2026-02-28" })
whoop_get_overview({ date: "2026-02-27" })
whoop_get_overview({ date: "2026-02-26" })
// ... etc.
```

**Recommendation for the reflect skill:** For a daily check-in, call today's data only — the 30-day baselines already provide trend context. For a weekly reflection, consider calling the last 7 days to show trajectory. Be mindful of API rate limits; 7 parallel calls is feasible, but 30 is excessive.

---

## 4. Formatting Notes

### Return format varies by tool
| Tool | `content[0].text` format | `structuredContent` |
|---|---|---|
| `whoop_get_overview` | Emoji-formatted text block | Yes (camelCase object) |
| `whoop_get_sleep` | `JSON.stringify(result, null, 2)` | No |
| `whoop_get_recovery` | Emoji-formatted text block | Yes (camelCase object) |
| `whoop_get_strain` | Emoji-formatted text block | Yes (camelCase object) |
| `whoop_get_healthspan` | Emoji-formatted text block | Yes (camelCase object) |

### Data type gotchas
- **Recovery score** is a string `"82"` in recovery tool, but a number `82` in overview tool
- **Sleep hours** is high-precision float `9.608894444444445` — round before displaying
- **Strain score** is a string `"11.1"` in strain tool, but a number `11.1` in overview
- **All contributor values** are pre-formatted strings (percentages include "%", times are "H:MM", integers have commas)
- **Healthspan pace of aging** format changed: was described as "0.5x" in README but actual data shows "-0.5x" with negative sign indicating slower aging

### Accessing the right data
The `content[0].text` field contains the human-readable formatted text. For the sleep tool, this is JSON. For all others, it's an emoji-laden text block. The `structuredContent` field (when present) contains the clean typed object — **prefer using structuredContent for programmatic access**.

However, since the reflect skill is an LLM consuming this data (not code parsing it), the text content is perfectly usable. The LLM can extract metrics from either format.

---

## 5. Recommendations for the Reflect Skill

### Optimal tool selection by use case

**Daily check-in (quick):**
- Call `whoop_get_overview` alone — it contains recovery %, strain, sleep hours, calories, activities, AND 30-day baselines for all key stats
- This single call provides enough data for a meaningful reflection

**Daily check-in (deep):**
- Call `whoop_get_overview` + `whoop_get_recovery` + `whoop_get_sleep`
- Overview for the big picture, recovery for HRV/RHR detail, sleep for efficiency/consistency detail
- Skip strain unless the user is physically active that day

**Weekly reflection:**
- Call all 5 tools for today's data
- Optionally call `whoop_get_overview` for each of the past 7 days to build a trend narrative
- Healthspan is weekly-scoped so it naturally fits

### How to reference fields reliably

Since the LLM reads the text output (not structured JSON), write the skill prompt to look for specific patterns:
- Recovery: look for "Recovery: XX%" or "recovery_score"
- HRV: look for "Heart Rate Variability" → "Current: XX"
- Strain: look for "Strain: XX.X" or the strain score line
- Sleep: parse the JSON blob for `sleepPerformance.score`

### Coach insights are gold
Every tool except overview includes a `coachInsight` (or `insight` for sleep) field containing personalized WHOOP coach analysis. These are high-quality, contextualized observations — the reflect skill should incorporate them rather than trying to re-derive the same insights.

### Recovery zone coloring
Use `recoveryScore.style` to determine the emotional framing:
- `RECOVERY_HIGH` (green, 67-100%) → body is ready, can push hard
- `RECOVERY_MID` (yellow, 34-66%) → moderate day, be mindful
- `RECOVERY_LOW` (red, 0-33%) → prioritize rest and recovery

### State comparison semantics
The `state` field on statistics tells you both direction AND valence:
- `_POSITIVE` suffix = this direction is good for health
- `_NEGATIVE` suffix = this direction is concerning
- `EQUAL` = no change from baseline

This lets the skill automatically frame metrics as wins vs. concerns without hardcoding thresholds.
