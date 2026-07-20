# Canonical Type Scale

## Minor Third Scale (ratio 1.2, base 16px)

Use for **product UI** (SaaS, dashboards, apps, tools).

| Step  | Name  | Size (px) | Size (rem) | Line Height | Letter Spacing | Weight Range |
|-------|-------|-----------|------------|-------------|----------------|--------------|
| -2    | xs    | 12        | 0.75       | 1.33 (16px) | 0              | 400          |
| -1    | sm    | 14        | 0.875      | 1.43 (20px) | 0              | 400          |
| 0     | base  | 16        | 1          | 1.5 (24px)  | 0              | 400          |
| 1     | lg    | 18        | 1.125      | 1.56 (28px) | 0              | 400-500      |
| 2     | xl    | 20        | 1.25       | 1.4 (28px)  | -0.01em        | 500-600      |
| 3     | 2xl   | 24        | 1.5        | 1.33 (32px) | -0.015em       | 600-700      |
| 4     | 3xl   | 30        | 1.875      | 1.2 (36px)  | -0.02em        | 700          |
| 5     | 4xl   | 36        | 2.25       | 1.11 (40px) | -0.02em        | 700          |
| 6     | 5xl   | 48        | 3          | 1.0 (48px)  | -0.025em       | 700          |
| 7     | 6xl   | 60        | 3.75       | 1.0 (60px)  | -0.025em       | 700-800      |
| 8     | 7xl   | 72        | 4.5        | 1.0 (72px)  | -0.025em       | 700-900      |
| 9     | 8xl   | 96        | 6          | 1.0 (96px)  | -0.025em       | 700-900      |

## Major Third Scale (ratio 1.25, base 16px)

Use for **marketing sites**, editorial, and landing pages where stronger visual hierarchy is needed.

| Step  | Name  | Size (px) | Size (rem) | Line Height | Letter Spacing | Weight Range |
|-------|-------|-----------|------------|-------------|----------------|--------------|
| -2    | xs    | 10        | 0.625      | 1.6 (16px)  | 0.02em         | 400-500      |
| -1    | sm    | 13        | 0.8125     | 1.54 (20px) | 0              | 400          |
| 0     | base  | 16        | 1          | 1.5 (24px)  | 0              | 400          |
| 1     | lg    | 20        | 1.25       | 1.4 (28px)  | -0.01em        | 400-500      |
| 2     | xl    | 25        | 1.5625     | 1.36 (34px) | -0.015em       | 500-600      |
| 3     | 2xl   | 31        | 1.9375     | 1.29 (40px) | -0.02em        | 600-700      |
| 4     | 3xl   | 39        | 2.4375     | 1.23 (48px) | -0.02em        | 700          |
| 5     | 4xl   | 49        | 3.0625     | 1.14 (56px) | -0.025em       | 700          |
| 6     | 5xl   | 61        | 3.8125     | 1.05 (64px) | -0.025em       | 700-800      |
| 7     | 6xl   | 76        | 4.75       | 1.0 (76px)  | -0.03em        | 700-900      |
| 8     | 7xl   | 95        | 5.9375     | 1.0 (95px)  | -0.03em        | 700-900      |
| 9     | 8xl   | 119       | 7.4375     | 1.0 (119px) | -0.03em        | 700-900      |

## Line-Height Rules

The relationship between font size and line height is inverse and continuous:

| Size Range | Line Height | Rationale |
|------------|-------------|-----------|
| 12-14px    | 1.4-1.5     | Small text needs more leading for legibility |
| 16px (base)| 1.5         | Optimal body text readability |
| 18-20px    | 1.4         | Transition zone |
| 24-30px    | 1.2-1.33    | Heading territory, tighten to maintain cohesion |
| 36-48px    | 1.1-1.15    | Display sizes, tight leading looks intentional |
| 48px+      | 1.0-1.1     | Hero/display, near-solid leading |

**Rule**: Never use a unitless line-height below 1.4 on text meant to be read in paragraphs.

## Letter-Spacing Rules

Letter spacing tightens progressively as size increases:

| Size Range | Letter Spacing | CSS Value |
|------------|---------------|-----------|
| 12-16px    | Normal        | 0         |
| 18-20px    | Slight tight  | -0.01em   |
| 24px       | Tight         | -0.015em  |
| 30-36px    | Tighter       | -0.02em   |
| 48px+      | Tightest      | -0.025em  |
| Uppercase  | Wide          | 0.05-0.1em |

**Rule**: Never apply positive letter-spacing to body text. Only caps/overlines/labels get positive tracking.

## Weight Mapping

| Role       | Weight | Tailwind  |
|------------|--------|-----------|
| Body       | 400    | font-normal |
| Emphasis   | 500    | font-medium |
| Subheading | 600    | font-semibold |
| Heading    | 700    | font-bold |
| Display    | 800    | font-extrabold |
| Hero       | 900    | font-black |

**Rule**: Use 4-6 weights maximum in any project. Every weight must have a clear semantic role.

## Semantic Mapping

| Token/Class | Scale Step | Typical Use |
|-------------|-----------|-------------|
| caption     | xs (12px) | Timestamps, metadata, helper text |
| label       | sm (14px) | Form labels, nav items, badges, tags |
| body        | base (16px) | Paragraph text, descriptions, list items |
| body-lg     | lg (18px) | Lead paragraphs, featured body text |
| heading-sm  | xl (20px) | Card titles, section labels |
| heading     | 2xl (24px) | Section headings (H3) |
| heading-lg  | 3xl (30px) | Page sub-sections (H2) |
| title       | 4xl (36px) | Page titles (H1) |
| display-sm  | 5xl (48px) | Hero subtitles, feature callouts |
| display     | 6xl (60px) | Hero headlines |
| display-lg  | 7xl (72px) | Landing page heroes |
| display-xl  | 8xl (96px) | Statement pieces, single words |
