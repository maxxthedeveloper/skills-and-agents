# Typography Audit Examples

Reference examples for audit output quality. Read this file the first time you perform an audit in a session.

---

## Example 1: Complete Audit Report (Score 65, SHIP WITH FIXES)

```
## Typography Audit: Acme Dashboard
### Stack: Tailwind
### Score: 65/100 — SHIP WITH FIXES

### Dimension Scores
| # | Dimension           | Score | Notes |
|---|---------------------|-------|-------|
| 1 | Scale Consistency   | 4/5   | 11 sizes, all map to Tailwind scale except 15px sidebar label |
| 2 | Line Height         | 3/5   | Body correct at 1.5, but all headings inherit 1.5 (too loose) |
| 3 | Hierarchy Clarity   | 3/5   | Size-only differentiation between h2/h3. Body competes with h4. |
| 4 | Measure             | 2/5   | Settings page paragraphs run full-width (~110ch) |
| 5 | Weight System       | 4/5   | 4 weights (400/500/600/700), clear roles |
| 6 | Letter Spacing      | 3/5   | No letter-spacing applied anywhere — neutral but unpolished |
| 7 | Responsive          | 4/5   | clamp() on hero, breakpoints on h1-h3. Body stays 16px. |
| 8 | Accessibility       | 3/5   | rem throughout, but sidebar metadata at 3.8:1 contrast |

### Critical Issues

**[AP-7] Unbounded text width on settings page**
**Severity**: Major
**Found**: `.settings-content` has no max-width, computed ~110ch on 1440px viewport
**File**: `src/pages/settings.tsx:42`
**Principle**: Lines >80ch cause readers to lose their place. Optimal measure is 50-75ch (Butterick).
**Fix (Tailwind)**:
```html
<div class="settings-content max-w-prose">
```

### Major Issues

**[AP-5] Uniform line-height on headings**
**Severity**: Major
**Found**: All headings inherit `leading-normal` (1.5) from base. h1 at 36px/1.5 = 54px line box.
**File**: `src/app/globals.css:8`
**Principle**: Heading line-height should tighten as size grows (1.1-1.3). 36px at 1.5 creates 18px gaps between lines.
**Fix (Tailwind)**:
```html
<h1 class="text-4xl leading-tight">   <!-- 1.25 -->
<h2 class="text-2xl leading-snug">    <!-- 1.375 -->
<h3 class="text-xl leading-snug">     <!-- 1.375 -->
```

**[HAP-2] Single-axis h2/h3 transition**
**Severity**: Major
**Found**: h2 (24px/600/#111) → h3 (20px/600/#111). Only size differs. 1.2x ratio is borderline.
**File**: computed
**Principle**: Adjacent levels need 2+ axes of change to register perceptually (size + weight, or size + color).
**Fix (Tailwind)**:
```html
<h2 class="text-2xl font-semibold text-gray-900">  <!-- keep -->
<h3 class="text-xl font-medium text-gray-700">     <!-- drop weight + lighten color -->
```

### Minor Issues

**[AP-13] No tracking on display text**
**Severity**: Minor
**Found**: Hero heading at 48px uses default letter-spacing
**File**: `src/components/Hero.tsx:12`
**Principle**: Display text (30px+) needs negative tracking for optical balance.
**Fix (Tailwind)**:
```html
<h1 class="text-5xl tracking-tight">
```

### What's Working
- Clean 4-weight system with clear semantic roles (body/emphasis/subheading/heading)
- Responsive hero scales well from 375px to 1440px using clamp()
- rem units throughout — text scales properly with user font-size preferences
- Good font loading: Inter with swap and complete fallback stack
```

---

## Example 2: Hierarchy Review — Good vs Bad

### Bad (vague, checklist-like, no specifics)

> The hierarchy is okay. Headings are larger than body text. Some transitions could be better. The spacing looks fine. Consider adjusting the colors.

### Good (design-director voice, specific, grounded in values)

> **The Overall Read** — Your page is top-heavy. The h1 at 48px/700 commands attention correctly, but below it the hierarchy compresses: h2 (24px/600), h3 (20px/600), and body (16px/400) are too close together. In a squint test, the h1 pops but everything below it blurs into a single gray band. The sidebar navigation at 14px/600 actually outweighs your h3 in prominence — bold small text reads louder than regular medium text.
>
> **The Strongest Transition** — Your h1 to h2 transition works. You're dropping from 48px/700 to 24px/600 — that's a 2x size jump plus a weight drop, creating an unmistakable level break. The 48px top-margin on h2 also helps: it signals "new section" before the reader even processes the text.
>
> **The Weakest Transition** — h3 to body is nearly invisible. 20px/600 to 16px/400 is a 1.25x size ratio with a weight drop, which should work, but you've given both the same color (#111) and identical 16px bottom margins. The weight drop is doing all the work, and at these sizes it's subtle. Your h3 reads as slightly-bolder body text, not as a structural element.
>
> **Spacing and Color** — Your heading spacing is symmetric: h2 and h3 both use 24px top and 16px bottom (1.5:1 ratio), which is correct. But the inter-section gap (24px) barely exceeds the intra-section gap (16px). Push h2 margin-top to 32-40px to create a clearer section break. Color is flat — everything is #111 except metadata at #666. Adding a #333 middle layer for h3/h4 would create three distinct tiers.
>
> **The Single Change** — Change your h3 from `text-xl font-semibold text-gray-900` to `text-xl font-medium text-gray-700`. That weight drop + color shift separates it from h2 above and body below, creating a three-tier system (dark bold → medium gray → regular dark) for almost zero effort.

---

## Example 3: Critical Finding Format

A critical finding must include: (1) the anti-pattern ID, (2) exact measured value, (3) file location, (4) a "why it matters" grounded in a specific standard, and (5) a copy-pasteable fix.

```
**[AP-4] Body text with dangerously tight leading**
**Severity**: Critical
**Found**: `.prose p` has `line-height: 1.2` — computed 19.2px line-height on 16px text
**File**: `src/styles/typography.css:34`
**Principle**: WCAG SC 1.4.12 requires body line-height >= 1.5. Below 1.4, readability
degrades significantly for users with dyslexia or visual impairments. Current value of 1.2
creates only 3.2px of interline space — half what's needed.
**Fix (CSS)**:
```css
.prose p {
  line-height: 1.5; /* was 1.2 */
}
```
```

Note the fix is a single, exact change — not "consider adjusting" or "try increasing."
