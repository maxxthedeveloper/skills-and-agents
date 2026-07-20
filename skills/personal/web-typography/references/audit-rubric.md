# Typography Audit Rubric

## Scoring System

Each dimension scores 1-5. Composite score = mean of all 8 dimensions. Headline score = `(composite / 5) * 100`.

| Score | Label     | Meaning |
|-------|-----------|---------|
| 5     | Excellent | Best-in-class, Apple/Linear quality |
| 4     | Good      | Solid, minor refinements possible |
| 3     | Adequate  | Functional but not polished |
| 2     | Poor      | Visible problems, needs attention |
| 1     | Critical  | Broken or harmful to UX |

## Verdicts

| Condition | Verdict | Symbol |
|-----------|---------|--------|
| Score 70+ AND no Critical issues | SHIP | SHIP |
| Score 50-69 OR has Major issues (no Critical) | SHIP WITH FIXES | SHIP WITH FIXES |
| Score <50 OR any Critical issue | DON'T SHIP | DON'T SHIP |

## Severity Levels

| Severity | Meaning | Examples |
|----------|---------|---------|
| Critical | Breaks readability, accessibility, or usability | Body line-height <1.4, no responsive type, contrast failure |
| Major    | Degrades polish and professionalism | Arbitrary sizes, >80ch measure, >8 weights |
| Minor    | Refinement opportunity | Suboptimal letter-spacing, missing text-wrap: balance |
| Info     | Observation or suggestion | Could benefit from tabular-nums on data |

---

## Dimension 1: Scale Consistency

**Question**: Do font sizes come from a defined scale or are they arbitrary?

| Score | Criteria |
|-------|----------|
| 5 | All sizes map to a mathematical scale (Minor Third, Major Third, or custom ratio). Zero arbitrary values. |
| 4 | 1-2 one-off sizes with clear justification (e.g., browser chrome constraints, design system convention). |
| 3 | Mix of scale sizes and arbitrary values. Some consistency visible. |
| 2 | Mostly arbitrary sizes. No discernible pattern. |
| 1 | Random sizes everywhere. 13px, 15px, 17px, 19px without rationale. |

**Critical threshold**: >3 arbitrary (non-scale) font sizes = **Critical**

**What to check**:
- Count unique font-size values
- Map each to nearest scale step
- Flag sizes that don't match any scale (e.g., 13px, 15px, 17px, 19px, 22px)
- Check for `!important` on font sizes (indicates override chaos)
- Tailwind: check for arbitrary values like `text-[15px]`

**Intentional deviation**: 1-2 off-scale sizes with clear purpose (e.g., fitting a specific UI constraint, matching a design system's established convention) should score 4, not 3. The test is whether the deviation is deliberate and documented, not whether every value is mathematically perfect. Modular scales are tools, not dogma (Tim Brown).

---

## Dimension 2: Line Height

**Question**: Is line height appropriate for each text size?

| Score | Criteria |
|-------|----------|
| 5 | Every text element has size-appropriate line height. Body 1.5, headings 1.1-1.3. |
| 4 | Mostly correct. 1-2 elements slightly off. |
| 3 | Body is correct but headings use body line height (too loose). |
| 2 | Some readable text has line-height below 1.4. |
| 1 | Body text with line-height <1.3 or headings with line-height >1.6. |

**Critical threshold**: Any body/paragraph text with line-height < 1.4 = **Critical**

**What to check**:
- Body text (p, li, dd, blockquote): line-height >= 1.5
- Small text (12-14px): line-height >= 1.4
- Headings (h1-h6): line-height 1.1-1.3 (tighter is better for large sizes)
- Display text (48px+): line-height 1.0-1.1
- No unitless values < 1.0 anywhere
- Check for `line-height: 1` on multi-line text (valid only on single-line display text)

---

## Dimension 3: Hierarchy Clarity

**Question**: Can a user instantly perceive the visual hierarchy of text elements?

| Score | Criteria |
|-------|----------|
| 5 | Clear hierarchy through 2+ axes per level transition. Size, weight, color, and spacing all reinforce the same ranking. Squint test passes — primary heading dominates the blurred view. |
| 4 | Good hierarchy, occasional single-axis transition (1 pair differs by size only). Overall reads clearly. Body clearly subordinate to all headings. |
| 3 | Hierarchy relies primarily on size. Weight and color differentiation is inconsistent. Some transitions use 2 axes, others only 1. |
| 2 | Single-axis hierarchy (size only). Adjacent levels <1.15x ratio, or body competes with headings in visual weight. |
| 1 | Flat hierarchy. Most text has similar visual weight. Or hierarchy is contradicted by spacing or color (spacing/color work against what size/weight establish). |

**Critical threshold**: Adjacent heading levels with < 1.2x size ratio = **Critical**. Squint test failure = caps verdict at **SHIP WITH FIXES**.

**What to check**:
- Calculate size ratios between adjacent heading levels (h1/h2, h2/h3, etc.)
- Minimum 1.25x ratio recommended, 1.2x minimum acceptable
- **Count axes per transition**: for each adjacent level pair, count how many axes change (size, weight, color, spacing). Flag single-axis pairs.
- **Verify body subordination**: body text must be clearly below all heading levels in visual prominence. Body weight must be 400. Prominence gap between body and lowest heading > 0.10.
- **Check color alignment**: heading colors must be primary (near-black), not lighter than body. Color layers should reinforce type hierarchy, not contradict it.
- **Check spacing asymmetry**: heading margin-top should be > margin-bottom (ratio >= 1.5). Headings should bind to their content.
- **Run squint test** (browser mode): rank styles by prominence, verify primary heading dominates the prominence ranking. Flag non-heading styles that outrank headings.
- Check for HAP-1 through HAP-7 (see anti-patterns.md, Hierarchy Anti-Patterns section)

---

## Dimension 4: Measure (Line Length)

**Question**: Are text containers constrained to readable line lengths?

| Score | Criteria |
|-------|----------|
| 5 | All readable text between 50-75ch. Main body near 66ch. max-width set explicitly. |
| 4 | Most text well-constrained. 1-2 edge cases slightly outside range. |
| 3 | Some text constrained but inconsistent. Wide containers exist. |
| 2 | Most text containers are too wide (>80ch). |
| 1 | Full-width text at 100%. No measure constraints. |

**Critical threshold**: Any text container > 80ch with no max-width = **Major**

**What to check**:
- Look for `max-width` on text containers (prose, article, content wrappers)
- Check for `max-w-prose` (Tailwind, ~65ch), `max-w-2xl` (~42rem/672px)
- Verify `ch` units or equivalent pixel values
- Check that headings and body share the same container width
- Flag any full-width text blocks without constraints

---

## Dimension 5: Weight System

**Question**: Are font weights used intentionally and systematically?

| Score | Criteria |
|-------|----------|
| 5 | 3-5 weights with clear semantic roles (body, emphasis, heading, display). |
| 4 | 4-6 weights, mostly intentional. One weight might lack clear purpose. |
| 3 | 5-7 weights. Some redundancy (e.g., both 500 and 600 for similar roles). |
| 2 | 7-8 weights. Inconsistent usage across components. |
| 1 | >8 weights or weight applied arbitrarily. |

**Critical threshold**: >8 distinct font weights = **Major**

**What to check**:
- Count unique font-weight values
- Map each weight to a semantic role
- Check that the loaded font files support the weights used
- Flag weights without clear differentiation (e.g., 400 + 500 used interchangeably)
- Verify variable fonts load appropriate weight range

---

## Dimension 6: Letter Spacing

**Question**: Is letter spacing applied appropriately based on size?

| Score | Criteria |
|-------|----------|
| 5 | Default body tracking. Progressive tightening on headings. Positive tracking only on caps/overlines. |
| 4 | Mostly correct. 1-2 elements could be tighter or looser. |
| 3 | No letter-spacing applied (neutral default). Technically fine but not polished. |
| 2 | Incorrect tracking (positive on body, or no tightening on display). |
| 1 | Positive letter-spacing on body text or extremely tight body. |

**Critical threshold**: Positive letter-spacing on body text = **Major**

**What to check**:
- Body text: letter-spacing should be 0 or normal
- Headings 20-30px: slight negative (-0.01em to -0.015em)
- Display 36px+: tighter (-0.02em to -0.025em)
- Uppercase text/labels: positive tracking (0.05em-0.1em)
- No letter-spacing on text that shouldn't have it
- Tailwind: check for `tracking-tight`, `tracking-tighter` on appropriate elements

---

## Dimension 7: Responsive Typography

**Question**: Does typography adapt gracefully across viewport sizes?

| Score | Criteria |
|-------|----------|
| 5 | Fluid type using `clamp()` for display/heading sizes. Base size stable. Tested at 375px and 1440px. |
| 4 | Breakpoint-based sizing that works well. Not fluid but correct at each breakpoint. |
| 3 | Some responsive adjustments. Display text might overflow on mobile. |
| 2 | Minimal responsiveness. Large text breaks on small screens. |
| 1 | No responsive typography at all. Desktop sizes on mobile. |

**Critical threshold**: No responsive type adjustments at all = **Major**

**What to check**:
- `clamp()` on heading/display sizes
- Media queries adjusting font sizes
- Text doesn't overflow viewport at 375px
- Base body size stays 16px (don't shrink body text on mobile)
- Heading sizes reduce meaningfully on mobile (not just 2px smaller)
- Check for `text-wrap: balance` on headings (modern browsers)

---

## Dimension 8: Accessibility

**Question**: Does the typography meet accessibility standards?

| Score | Criteria |
|-------|----------|
| 5 | 4.5:1+ contrast, text scales to 200%, text-wrap applied, tabular-nums on data, proper heading hierarchy. |
| 4 | Meets contrast requirements. Text scales correctly. Missing 1-2 refinements. |
| 3 | Contrast passes but text scaling partially breaks. |
| 2 | Some contrast failures or text doesn't scale properly. |
| 1 | Widespread contrast failures or text breaks at 200% zoom. |

**Critical threshold**: Any contrast ratio < 4.5:1 on body text = **Critical**

**What to check**:
- Color contrast ratios (body text must be 4.5:1+, large text 3:1+)
- `rem` / `em` units (not `px`) for font sizes so text scales with user settings
- Text remains readable at 200% browser zoom
- `text-wrap: balance` on headings and short text blocks
- `font-variant-numeric: tabular-nums` on data tables, dashboards, numbers
- Proper heading hierarchy (no skipped levels: h1 -> h3)
- `lang` attribute on html element (affects hyphenation and screen readers)
- `text-size-adjust: 100%` for iOS Safari
- Dark mode: `font-weight` may need +50-100 bump to compensate for halation (light text on dark bg appears thinner). Check if dark mode styles adjust weight or `-webkit-font-smoothing: antialiased`
- Micro-typography: straight quotes vs curly, fake ellipsis, hyphen-dash confusion (see AP-26 through AP-29)
