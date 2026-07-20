# Visual Hierarchy Principles

How to judge whether typographic hierarchy actually works — not by checking numbers, but by reading the page as a design director would.

---

## Layer 1: Mental Model

Hierarchy is contrast across multiple axes simultaneously: size, weight, color, spacing, and typeface. A single axis — size alone — creates fragile hierarchy that collapses when squinted at. The strongest hierarchies use 2-3 axes per level transition.

Weight is the most striking axis. A 17pt Regular sitting next to a 17pt Semibold creates an unmistakable level break without touching size at all. Weight changes register faster than size changes because the stroke contrast is immediately visible.

Body text is the anchor. Set it first. Every other level derives from body — headings push up in size and weight, metadata pushes down in color and size. If body isn't locked, nothing above or below it will feel grounded.

Restraint creates hierarchy as much as emphasis does. Quiet elements — light grays, small sizes, reduced weight — make the loud elements work. A page where everything demands attention has no hierarchy at all.

Limit to 5 active hierarchy levels maximum. If a page needs more than 5 visually distinct text levels, it has a structure problem, not a type problem. Most well-designed pages use 3-4: heading, subheading, body, metadata.

The order of axes by perceptual impact: weight > size > color > spacing > typeface. Weight and size together account for ~70% of perceived hierarchy. Color is the third lever. Spacing reinforces but rarely creates hierarchy on its own. Typeface changes (sans to serif) create the strongest break but should be used sparingly.

---

## Layer 2: Diagnostic Toolkit

### The Squint Test

Blur the page mentally — or literally squint. What dominates? What recedes? The visual weight distribution in the blurred view should match the importance ranking of the content. If a secondary element (a sidebar label, a metadata line) has more visual weight than a primary heading when squinted, hierarchy is broken.

The squint test catches problems that numeric checks miss: a heading that's technically larger but uses a light weight and light color, making it visually subordinate to bold body text.

### Functional Categories

Think in functional roles, not abstract size levels. Every text element on a page serves one of these roles:

- **Headings** — section titles, page titles, card titles. Must dominate their context.
- **Labels** — navigation, form labels, sidebar items. Functional, not decorative. Medium weight, smaller size.
- **Copy** — body text, descriptions, paragraphs. The reading voice. Regular weight, comfortable size.
- **Actions** — buttons, links, CTAs. Must be identifiable without reading. Weight and color carry them.
- **Metadata** — timestamps, bylines, status indicators, footnotes. Must recede. Lighter color, smaller size.

A hierarchy problem often means two functional categories share the same visual treatment. When labels look like headings, or metadata competes with copy, the page loses its navigational logic.

### Spacing as Hierarchy

Spacing is the silent hierarchy axis. A heading must have more space above it than below it — this binds the heading to the content it introduces rather than floating ambiguously between sections. When margin-top equals margin-bottom on a heading, it belongs to neither the section above nor below. This is one of the most common hierarchy failures.

Proximity equals grouping. Elements closer together are perceived as related. A heading 8px from its body but 32px from the previous section clearly introduces that body. A heading equidistant from both creates confusion.

Rhythm breaks signal hierarchy transitions. Consistent spacing within a section (body paragraphs all 16px apart) establishes a rhythm. Breaking that rhythm (40px gap before a new heading) signals a level change. Dense, tool-like interfaces (dashboards, IDEs) use tight, precise alignment rather than dramatic spacing contrast — but the proximity principle still holds.

### Color as Hierarchy

Color operates in three layers for text hierarchy:

- **Primary** — near-black (#111, #1a1a1a). Headings and body text. The structural voice of the page.
- **Secondary** — medium gray (#666, #6b7280). Descriptions, supporting text, form help text. Clearly subordinate.
- **Tertiary** — light gray (#999, #9ca3af). Metadata, timestamps, placeholders. Intentionally quiet.

Color must reinforce the type hierarchy, never contradict it. When headings use a lighter color than body, or when accent colors on metadata make it louder than structural text, the color layer undermines what size and weight established.

### The Correct-vs-Good Gap

A type system can follow every rule — proper scale, correct line-heights, good weights — and still feel flat and lifeless. "Correct" checks boxes. "Good" creates an experience. The gap between them comes from:

- **Intentional emphasis and restraint** — knowing what to make loud AND what to make quiet
- **Rhythm and pacing** — the way spacing, size, and weight create a reading flow across the page
- **Hierarchy within hierarchy** — components have their own internal hierarchy (card title > card description > card metadata) nested inside the page hierarchy
- **Purposeful rule-breaking** — an oversized pull quote, a display-weight number, a color accent on a single word. Rules exist so breaking them is meaningful.

---

## Layer 3: Seven Perceptual Anti-Patterns

### HAP-1: Everything Screaming

All text sits at similar visual weight. Bold body, bold headings, bold labels — or conversely, all light, all the same size. No quiet elements exist to create contrast. The page reads as a wall of equally-important text. Fix: identify the 2-3 elements that matter most, make everything else quieter.

### HAP-2: Single-Axis Differentiation

Hierarchy levels differ only by size — same weight, same color, same spacing. Squint and the levels collapse into each other because size differences below 1.3x are hard to perceive without weight or color reinforcement. Fix: add a second axis. If h2 and h3 differ only by 4px, also change weight (Semibold vs Regular) or color (primary vs secondary).

### HAP-3: Body-Heading Collision

Body text is too close in visual weight to the lowest heading level. This happens when body uses medium weight (500) or when h4/h5 headings aren't differentiated enough from body. The bottom of the hierarchy muddles together, making it unclear what's a heading and what's body text. Fix: body must be 400 weight. Lowest heading must have either a weight bump or a color distinction from body.

### HAP-4: Level Inflation

More than 5 distinct hierarchy levels on a single page. Each level is a decision the reader must process — "is this more or less important than that?" Beyond 5, the cognitive load of parsing the hierarchy outweighs its organizational benefit. Common cause: using h1 through h6 literally instead of consolidating to 3-4 visual levels. Fix: merge adjacent levels that serve similar functions.

### HAP-5: Spacing Contradiction

Heading has margin-top less than or equal to margin-bottom, causing it to float between sections rather than binding to its content. Or: spacing within a section equals spacing between sections, eliminating proximity-based grouping. Fix: heading margin-top should be 1.5-2x its margin-bottom. Inter-section spacing should be clearly larger than intra-section spacing.

### HAP-6: Inconsistent Pattern

The same semantic role is styled differently in different parts of the page. Card titles in one section are 18px Semibold, in another section they're 16px Bold. Or section headings alternate between two different treatments. This signals a missing design system, not an intentional choice. Fix: audit each functional role and unify its treatment across all instances.

### HAP-7: Color Undermining Type

The color hierarchy contradicts the type hierarchy. Common manifestations: body text darker than headings, accent colors on metadata making it louder than body, secondary text in a saturated brand color while headings use plain gray. The eye follows color before it follows size — so color misalignment overrides even well-structured size/weight hierarchy. Fix: map color layers (primary/secondary/tertiary) to functional categories and verify alignment.
