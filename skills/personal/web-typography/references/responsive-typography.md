# Responsive Typography

## The clamp() Formula

```
font-size: clamp(min, preferred, max)
```

- **min**: Smallest acceptable size (in rem). The floor.
- **preferred**: Fluid value that scales with viewport (uses vw + rem). The slope.
- **max**: Largest acceptable size (in rem). The ceiling.

### Calculating clamp() Values

Given a minimum viewport (375px) and maximum viewport (1440px):

```
slope = (maxSize - minSize) / (maxViewport - minViewport)
intercept = minSize - slope * minViewport
preferred = intercept(rem) + slope(vw)
```

**Example**: Scale from 36px (2.25rem) at 375px to 72px (4.5rem) at 1440px:
```
slope = (72 - 36) / (1440 - 375) = 36 / 1065 = 0.0338 = 3.38vw
intercept = 36 - (0.0338 * 375) = 36 - 12.66 = 23.34px = 1.459rem
→ font-size: clamp(2.25rem, 1.46rem + 3.38vw, 4.5rem)
```

## Pre-Calculated Fluid Scale

Based on 375px min → 1440px max viewport, 16px base:

| Step | Min (px) | Max (px) | clamp() value |
|------|----------|----------|---------------|
| xs   | 12       | 12       | 0.75rem (static, don't scale caption text) |
| sm   | 14       | 14       | 0.875rem (static, don't scale label text) |
| base | 16       | 16       | 1rem (static, never scale body text) |
| lg   | 16       | 18       | clamp(1rem, 0.95rem + 0.19vw, 1.125rem) |
| xl   | 18       | 20       | clamp(1.125rem, 1.08rem + 0.19vw, 1.25rem) |
| 2xl  | 20       | 24       | clamp(1.25rem, 1.16rem + 0.38vw, 1.5rem) |
| 3xl  | 24       | 30       | clamp(1.5rem, 1.36rem + 0.56vw, 1.875rem) |
| 4xl  | 28       | 36       | clamp(1.75rem, 1.57rem + 0.75vw, 2.25rem) |
| 5xl  | 32       | 48       | clamp(2rem, 1.63rem + 1.50vw, 3rem) |
| 6xl  | 36       | 60       | clamp(2.25rem, 1.69rem + 2.25vw, 3.75rem) |
| 7xl  | 40       | 72       | clamp(2.5rem, 1.75rem + 3.01vw, 4.5rem) |
| 8xl  | 48       | 96       | clamp(3rem, 1.87rem + 4.51vw, 6rem) |

**Key rule**: xs, sm, and base are STATIC. Never fluid-scale body text or small text. Only headings and display text get `clamp()`.

## Responsive Line Height

Line height should also adjust responsively for large text:

```css
/* Heading that goes from 30px to 60px */
h1 {
  font-size: clamp(1.875rem, 1.69rem + 2.25vw, 3.75rem);
  line-height: clamp(1.1, 1.0 + 0.2vw, 1.3);
}
```

At small viewport: size is 30px, line-height ~1.3 (more breathing room on small screen).
At large viewport: size is 60px, line-height ~1.1 (tighter for display text).

## Baseline Grid

### 4px Grid
All spacing and sizing should align to a 4px baseline grid:

- Body line height: 16px * 1.5 = **24px** (6 * 4px)
- Small line height: 14px * 1.43 = **20px** (5 * 4px)
- Caption line height: 12px * 1.33 = **16px** (4 * 4px)
- Heading line height: 24px * 1.33 = **32px** (8 * 4px)
- Spacing between paragraphs: **16px** or **24px** (4 or 6 * 4px)

### Vertical Rhythm
Maintain consistent vertical spacing by ensuring all text blocks and their margins sum to multiples of the base line height (24px for 16px/1.5 body):

```css
p {
  font-size: 1rem;        /* 16px */
  line-height: 1.5;        /* 24px */
  margin-bottom: 1.5rem;   /* 24px — one line of body text */
}

h2 {
  font-size: 1.5rem;       /* 24px */
  line-height: 1.33;       /* 32px */
  margin-top: 3rem;         /* 48px — two lines of body text */
  margin-bottom: 1rem;      /* 16px */
  /* Total space: 48 + 32 + 16 = 96px = 4 * 24px */
}
```

## Breakpoint Strategy

If not using `clamp()`, use these breakpoints for type adjustments:

| Breakpoint | Viewport | Adjustments |
|-----------|----------|-------------|
| sm | 640px | Reduce display text 15-20%. Body stays 16px. |
| md | 768px | Intermediate sizes. Headings at ~80% of desktop. |
| lg | 1024px | Near-desktop sizes. Headings at ~90%. |
| xl | 1280px | Full desktop sizes. |
| 2xl | 1536px | Cap sizes here. Don't let text grow infinitely. |

### Tailwind Example
```html
<h1 class="text-3xl md:text-4xl lg:text-5xl xl:text-6xl">
  Hero Heading
</h1>
```

**Prefer `clamp()`** over breakpoints. `clamp()` gives smooth scaling. Breakpoints create visible jumps.

## Container Queries for Typography

For component-level responsive type (e.g., a card that appears in different column widths):

```css
.card {
  container-type: inline-size;
}

@container (min-width: 400px) {
  .card-title {
    font-size: 1.5rem;
  }
}

@container (min-width: 600px) {
  .card-title {
    font-size: 1.875rem;
  }
}
```

## Modern CSS Typography Properties

### text-wrap: balance
Balances line lengths in headings to avoid orphans:
```css
h1, h2, h3 {
  text-wrap: balance;
}
```
**Browser support**: Chrome 114+, Firefox 121+, Safari 17.5+. Progressive enhancement — safe to use now.

### text-wrap: pretty
Prevents orphans in body text by adjusting line breaks:
```css
p {
  text-wrap: pretty;
}
```
**Browser support**: Chrome 117+, Safari 17.5+. Progressive enhancement.

### font-variant-numeric: tabular-nums
Ensures numbers are monospaced width for alignment in tables and data:
```css
.data-table td,
.price,
.stat {
  font-variant-numeric: tabular-nums;
}
```

### text-size-adjust: 100%
Prevents iOS Safari from inflating font sizes in landscape:
```css
html {
  -webkit-text-size-adjust: 100%;
  text-size-adjust: 100%;
}
```

### font-optical-sizing: auto
Enables optical size variations in variable fonts that support it:
```css
body {
  font-optical-sizing: auto;
}
```
