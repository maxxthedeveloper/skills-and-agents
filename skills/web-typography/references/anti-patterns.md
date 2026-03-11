# Typography Anti-Patterns

Banned patterns organized by category. Each includes: what it is, why it's harmful, and the correct alternative.

---

## Scale Violations

### AP-1: Magic Number Font Sizes
**Pattern**: `font-size: 13px`, `font-size: 15px`, `font-size: 17px`, `text-[15px]`
**Why it's banned**: Arbitrary sizes that don't belong to any scale create visual inconsistency. They suggest design decisions were made ad-hoc rather than systematically.
**Fix**: Map to nearest scale value. 13px -> 12px (xs) or 14px (sm). 15px -> 14px (sm) or 16px (base). 17px -> 16px (base) or 18px (lg).
**Exception**: Browser chrome constraints (min 12px on some platforms) or legacy system integration.

### AP-2: Too Many Sizes
**Pattern**: More than 12 distinct font-size values across the project.
**Why it's banned**: Indicates a missing type scale. Every additional size fragments the visual system.
**Fix**: Audit all sizes, map to 8-12 scale steps, refactor outliers.

### AP-3: Base Size != 16px
**Pattern**: `html { font-size: 14px }`, `html { font-size: 62.5% }` (10px trick)
**Why it's banned**: 16px is the browser default and the accessibility baseline. Changing it breaks user expectations and rem calculations. The 62.5% trick creates confusion and breaks third-party components.
**Fix**: Keep html font-size at 16px (100%). Adjust component sizes using the scale.
**Exception**: Asian-language sites may use 15px base for CJK readability.

---

## Line Height Violations

### AP-4: Body Text with Tight Leading
**Pattern**: `p { line-height: 1.2 }`, `.content { line-height: 1.3 }`
**Why it's banned**: Body text below 1.4 line-height is difficult to read, especially for users with dyslexia or visual impairments. WCAG SC 1.4.12 requires at least 1.5x for body text.
**Fix**: Body text: line-height 1.5. Minimum for any readable text: 1.4.

### AP-5: Uniform Line Height
**Pattern**: `* { line-height: 1.5 }` or all text elements sharing one line-height value.
**Why it's banned**: 1.5 is correct for body text but too loose for headings (makes them look disconnected). Display text at 48px+ with 1.5 line-height creates 24px gaps between lines.
**Fix**: Pair line-height to size. See type-scale.md for the size-to-line-height mapping.

### AP-6: Line Height in px on Scalable Text
**Pattern**: `p { font-size: 1rem; line-height: 24px }`
**Why it's banned**: If the user increases their browser font size, the line-height stays fixed at 24px, eventually causing text overlap.
**Fix**: Use unitless line-height: `line-height: 1.5`. It multiplies by the computed font-size.

---

## Measure Violations

### AP-7: Unbounded Text Width
**Pattern**: Full-width paragraphs with no `max-width`, `max-w-prose`, or `ch`-based constraint.
**Why it's banned**: Lines exceeding 80 characters cause readers to lose their place when returning to the next line. Research shows 50-75 characters per line is optimal.
**Fix**: Add `max-width: 65ch` or Tailwind's `max-w-prose` to text containers.

### AP-8: Narrow Measure
**Pattern**: `max-width: 30ch` or constrained below 45 characters on body text.
**Why it's banned**: Too-narrow text creates excessive line breaks, a jagged right edge, and slows reading. Only acceptable for captions or sidebar annotations.
**Fix**: Minimum 45ch for body text. Optimal 60-70ch.

---

## Weight Violations

### AP-9: Weight Soup
**Pattern**: Using 7+ different font-weight values without clear semantic mapping.
**Why it's banned**: Users can barely distinguish adjacent weights (400 vs 500). Using too many weights creates visual noise and increases font file downloads.
**Fix**: Pick 4-5 weights with clear roles: 400 (body), 500 (emphasis), 600 (subheading), 700 (heading), 800 (display if needed).

### AP-10: Bold Body Text
**Pattern**: `p { font-weight: 500 }` or `body { font-weight: 500 }`
**Why it's banned**: Medium/semi-bold as default body weight reduces contrast between emphasis and normal text, flattening the hierarchy.
**Fix**: Body text should be weight 400 (normal/regular).

### AP-11: Faux Bold
**Pattern**: Browser-synthesized bold on fonts that don't include a bold weight.
**Why it's banned**: The browser artificially thickens glyphs, creating ugly, inconsistent results. Characters look smeared rather than designed.
**Fix**: Ensure loaded font files include every weight used. Check `@font-face` declarations or Google Fonts includes.

---

## Letter Spacing Violations

### AP-12: Positive Tracking on Body
**Pattern**: `p { letter-spacing: 0.05em }`, `.content { letter-spacing: 1px }`
**Why it's banned**: Positive letter-spacing on body text disrupts natural reading rhythm. Letters are designed to fit together at their default spacing.
**Fix**: Body letter-spacing should be 0/normal. Only apply positive tracking to uppercase labels, overlines, and small caps.

### AP-13: No Tracking on Display
**Pattern**: Large headings (30px+) with default letter-spacing.
**Why it's banned**: At large sizes, the optical spacing between letters appears too wide. Professional typography always tightens tracking on display text.
**Fix**: Apply progressively tighter tracking. See type-scale.md for exact values per size.

---

## Font Loading Violations

### AP-14: Flash of Invisible Text (FOIT)
**Pattern**: `font-display: block` or no `font-display` declaration on custom fonts.
**Why it's banned**: Text becomes invisible while the font loads. Users see a blank page. Some browsers block rendering for up to 3 seconds.
**Fix**: Use `font-display: swap` (or `optional` for non-critical fonts). Ensure a good fallback stack.

### AP-15: No Fallback Stack
**Pattern**: `font-family: "Inter"` with no fallback fonts.
**Why it's banned**: If the font fails to load, the browser falls back to its default serif font, which looks broken.
**Fix**: Always include a complete fallback stack: `font-family: "Inter", ui-sans-serif, system-ui, -apple-system, sans-serif`.

### AP-16: Too Many Font Families
**Pattern**: More than 3 font families loaded on a page.
**Why it's banned**: Each font family adds HTTP requests and rendering time. More than 2-3 families also creates visual chaos.
**Fix**: 1 font for body + 1 for headings (optional). Monospace for code (3 total max).

---

## Responsive Violations

### AP-17: Desktop Sizes on Mobile
**Pattern**: A 72px hero heading with no responsive reduction.
**Why it's banned**: Large text overflows, wraps awkwardly, or dominates the entire viewport on mobile. A 72px heading might take up 80% of a 375px screen.
**Fix**: Use `clamp()` to scale down: `font-size: clamp(2.25rem, 5vw + 1rem, 4.5rem)`.

### AP-18: Shrinking Body Text on Mobile
**Pattern**: `@media (max-width: 768px) { body { font-size: 14px } }`
**Why it's banned**: Body text should remain 16px on all viewports. Smaller screens need the same (or better) readability, not less. Users hold phones closer, partially compensating for screen size.
**Fix**: Keep base size at 16px. Only reduce heading/display sizes.

### AP-19: vw-Only Font Sizing
**Pattern**: `font-size: 5vw` with no min/max bounds.
**Why it's banned**: At 375px viewport, 5vw = 18.75px (maybe ok). At 2560px, 5vw = 128px (way too large). At 320px, it might be too small. No bounds means broken extremes.
**Fix**: Always use `clamp()`: `font-size: clamp(1rem, 2.5vw + 0.5rem, 3rem)`.

---

## Accessibility Violations

### AP-20: px-Only Font Sizes
**Pattern**: All font sizes in `px` with no `rem` or `em` usage.
**Why it's banned**: Users who set a custom browser font size (e.g., 20px default for low vision) see no change because px values are absolute. This is an accessibility failure.
**Fix**: Use `rem` for font sizes. `clamp()` can mix rem and vw.

### AP-21: Low Contrast Text
**Pattern**: Light gray text on white background. `color: #999` on `background: #fff` (2.8:1 ratio).
**Why it's banned**: Fails WCAG AA (4.5:1 for normal text, 3:1 for large text). Unreadable for users with moderate vision loss.
**Fix**: Minimum `#595959` on white for 7:1 (AAA). Minimum `#767676` for 4.5:1 (AA).

### AP-22: Skipped Heading Levels
**Pattern**: Page has h1, then h3 (skipping h2). Or h2 followed by h4.
**Why it's banned**: Screen readers use heading levels for navigation. Skipped levels confuse the document outline and make the page harder to navigate for assistive technology users.
**Fix**: Always use sequential heading levels. Style visually with classes, not heading tags.

---

## Stylistic Anti-Patterns

### AP-23: Justified Text on Web
**Pattern**: `text-align: justify` without hyphenation.
**Why it's banned**: Without browser hyphenation support, justified text creates "rivers" of whitespace that harm readability. Even with `hyphens: auto`, results are inconsistent across browsers.
**Fix**: Use `text-align: left` (or `start`). If justification is truly needed, add `hyphens: auto` and `text-wrap: pretty`.

### AP-24: All-Caps Body Text
**Pattern**: `text-transform: uppercase` on paragraphs or long text.
**Why it's banned**: All-caps text reduces reading speed by ~10-20%. Letter shapes become uniform rectangles, removing the word-shape cues that enable fast scanning. Acceptable only for short labels, buttons, and overlines.
**Fix**: Reserve `uppercase` for labels, badges, overlines, and navigation items. Never on text longer than ~5 words.

### AP-25: Decorative Fonts for Body
**Pattern**: Display or handwriting fonts used for body text.
**Why it's banned**: Decorative fonts are designed for large sizes and short runs. At body sizes, they're hard to read and slow comprehension.
**Fix**: Use a well-designed text font for body. Reserve decorative fonts for headings or hero text.

---

## Hierarchy Anti-Patterns (Browser Mode)

These patterns are detected during browser audits using the visual weight map, spacing extraction, and color hierarchy data. They assess whether hierarchy *works perceptually*, not just whether numbers are correct.

### HAP-1: Everything Screaming
**Pattern**: All text elements sit within a narrow visual prominence range (top and bottom prominence scores differ by < 0.15). No quiet elements exist — everything is bold, everything is dark, everything is similarly sized.
**Why it's harmful**: Without quiet elements, there is no contrast. The reader has no entry point and no navigational cues. The page reads as a wall of equally-important text.
**Detection**: Visual weight map shows all styles clustered within a 0.15 prominence band. Or: >70% of text elements share the same weight (e.g., all 600+).
**Fix**: Identify the 2-3 most important elements and give them full visual weight (dark color, heavier weight, larger size). Push everything else down: lighter color, regular weight, default size. Metadata should be noticeably quiet.

### HAP-2: Single-Axis Differentiation
**Pattern**: Adjacent hierarchy levels differ on only one axis — typically size. Same weight, same color, same spacing between levels. H2 is 24px and H3 is 20px, but both are 600 weight, both #111, both with identical margins.
**Why it's harmful**: Size differences below 1.3x are subtle. Without weight or color reinforcement, levels blur together, especially at reading distance. The hierarchy technically exists but doesn't register perceptually.
**Detection**: For each adjacent level pair in the prominence ranking, count how many axes change (size, weight, color). Flag pairs where only 1 axis changes.
**Fix**: Add a second axis per transition. If h2 and h3 differ only by size, also differentiate by weight (Semibold vs Regular) or color (primary vs secondary gray).

### HAP-3: Body-Heading Collision
**Pattern**: Body text is too close in visual weight to the lowest heading level. Body uses weight 500, or the lowest heading (h4/h5) uses the same weight and color as body with minimal size difference.
**Why it's harmful**: The bottom of the hierarchy muddles. Readers can't tell at a glance what's a heading and what's body text. This undermines the organizational purpose of headings.
**Detection**: Visual weight map shows prominence difference < 0.08 between body text style and lowest heading style. Or: body weight >= 500 while lowest heading weight <= 500.
**Fix**: Body text must use weight 400. The lowest heading must have either a weight increase (500+) or a color distinction from body. A clear prominence gap (> 0.10) between body and the lowest heading is the target.

### HAP-4: Level Inflation
**Pattern**: More than 5 distinct visual hierarchy levels on a single page. Often caused by using h1 through h6 literally, each with its own distinct styling, plus body text and metadata.
**Why it's harmful**: Each hierarchy level is a decision the reader must make — "is this more or less important than that?" Beyond 5 levels, the cognitive cost of parsing the hierarchy outweighs its organizational benefit. Readers stop tracking levels and start ignoring them.
**Detection**: Visual weight map reports hierarchyLevels > 5 (counting styles with >0.05 prominence gap between them).
**Fix**: Merge adjacent levels that serve similar functions. Most pages need only 3-4 visual levels: primary heading, secondary heading, body, metadata. Style h4/h5/h6 identically to h3 or body-bold if they must exist in the DOM.

### HAP-5: Spacing Contradiction
**Pattern**: Heading has margin-top less than or equal to margin-bottom, making it float equidistant between the previous section and its own content. Or: spacing within a section equals spacing between sections, eliminating proximity-based grouping.
**Why it's harmful**: Headings that don't bind to their content lose their organizational function. The reader can't tell whether the heading belongs to what's above or below. This breaks the most fundamental typographic grouping principle — proximity equals relationship.
**Detection**: Heading spacing data shows ratio (margin-top / margin-bottom) <= 1.0 for any heading. Or: the most common vertical gap between intra-section elements equals the gap before headings.
**Fix**: Heading margin-top should be 1.5-2x its margin-bottom. Example: if margin-bottom is 16px, margin-top should be 24-32px. Inter-section gaps should be clearly larger than intra-section gaps.

### HAP-6: Inconsistent Pattern
**Pattern**: The same semantic role is styled differently across the page. Card titles in one section are 18px Semibold, in another they're 16px Bold. Section headings alternate between treatments. Same-level list items use different sizes.
**Why it's harmful**: Inconsistency signals a missing or broken design system. It forces the reader to re-learn the hierarchy in each section. Trust in the visual system erodes — if the same role looks different, how can the reader trust that different roles will look different?
**Detection**: Primary extraction shows multiple distinct style fingerprints mapped to the same semantic tag/role at the same heading level. E.g., two different h2 treatments on the same page.
**Fix**: Audit each functional role (card title, section heading, metadata) and unify its treatment across all instances. One style per role, no exceptions.

### HAP-7: Color Undermining Type
**Pattern**: The color hierarchy contradicts the type hierarchy. Body text is darker than headings. Accent colors on metadata make it louder than structural text. Secondary descriptions use a saturated brand color while headings use neutral gray.
**Why it's harmful**: The eye follows color contrast before it follows size. A bright blue metadata line will draw attention away from a gray heading, regardless of size difference. Color misalignment overrides even well-structured size and weight hierarchy.
**Detection**: Color hierarchy extraction flags heading-lighter-than-body issues. Or: elements in the tertiary/faint color layer are mapped to structurally important tags. Or: accent/saturated colors appear on metadata or secondary elements.
**Fix**: Map the three color layers (primary, secondary, tertiary) to functional categories: headings and body get primary (near-black), descriptions get secondary (medium gray), metadata gets tertiary (light gray). Accent colors should appear only on interactive elements (links, buttons), never on structural hierarchy.

---

## Micro-Typography Anti-Patterns

### AP-26: Straight Quotes
**Pattern**: `"Hello"` or `'world'` — using typewriter quotes (`"` `'`) instead of proper curly quotes (`"` `"` `'` `'`).
**Why it's banned**: Straight quotes are a vestige of typewriters. They signal unpolished typography and read as code, not prose. Professional sites (Apple, Stripe, Linear) always use curly quotes in marketing and editorial content.
**Fix**: Use `&ldquo;` / `&rdquo;` in HTML, or configure your CMS/renderer to auto-convert (e.g., SmartyPants, remark-smartypants). Product UI with user-generated content is exempt.
**Severity**: Minor

### AP-27: Fake Ellipsis
**Pattern**: Three dots `...` instead of the ellipsis character `…` (`&hellip;`).
**Why it's banned**: Three periods have incorrect spacing (too wide). The ellipsis character is a single glyph designed for this purpose. This matters most in editorial/marketing content.
**Fix**: Use `&hellip;` in HTML or `…` (Unicode U+2026). Most build tools and CMS systems can auto-convert.
**Severity**: Minor

### AP-28: Missing Tabular Figures on Data
**Pattern**: Number columns, prices, or data tables without `font-variant-numeric: tabular-nums`.
**Why it's banned**: Proportional (default) figures have variable widths — "1" is narrower than "0". In tables, dashboards, and price lists, this causes columns to misalign and numbers to jitter on update.
**Fix**: Add `font-variant-numeric: tabular-nums` (CSS) or `tabular-nums` (Tailwind) to any element displaying aligned numbers: tables, price columns, timers, statistics.
**Severity**: Minor (data-heavy pages: Major)

### AP-29: Hyphen-Dash Confusion
**Pattern**: Using hyphens `-` where en-dashes `–` or em-dashes `—` are needed. Common: "2020-2024" (should be "2020–2024"), "the result - a success" (should be "the result — a success").
**Why it's banned**: Hyphens, en-dashes, and em-dashes serve different functions. Misuse signals typographic carelessness and can affect meaning (a hyphen joins, a dash separates).
**Fix**: Ranges use en-dash (`&ndash;`, `–`). Parenthetical breaks use em-dash (`&mdash;`, `—`). Compound words use hyphen (`-`). Auto-conversion via CMS is ideal.
**Severity**: Minor
