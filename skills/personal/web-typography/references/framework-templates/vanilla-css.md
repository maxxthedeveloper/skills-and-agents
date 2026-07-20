# Vanilla CSS Type System Template

## CSS Custom Properties Type System

```css
/* ==========================================================================
   Type System — CSS Custom Properties
   Scale: Minor Third (1.2), Base: 16px
   Viewport: 375px (min) → 1440px (max)
   ========================================================================== */

:root {
  /* ── Font Families ────────────────────────────────────────────────────── */
  --font-sans: "Inter", ui-sans-serif, system-ui, -apple-system,
    BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-serif: ui-serif, Georgia, Cambria, "Times New Roman", Times, serif;
  --font-mono: "Geist Mono", ui-monospace, SFMono-Regular, "SF Mono", Menlo,
    Consolas, "Liberation Mono", "Courier New", monospace;

  /* ── Font Sizes (Static) ──────────────────────────────────────────────── */
  --text-xs: 0.75rem;   /* 12px */
  --text-sm: 0.875rem;  /* 14px */
  --text-base: 1rem;    /* 16px */

  /* ── Font Sizes (Fluid) ──────────────────────────────────────────────── */
  --text-lg: clamp(1rem, 0.95rem + 0.19vw, 1.125rem);
  --text-xl: clamp(1.125rem, 1.08rem + 0.19vw, 1.25rem);
  --text-2xl: clamp(1.25rem, 1.16rem + 0.38vw, 1.5rem);
  --text-3xl: clamp(1.5rem, 1.36rem + 0.56vw, 1.875rem);
  --text-4xl: clamp(1.75rem, 1.57rem + 0.75vw, 2.25rem);
  --text-5xl: clamp(2rem, 1.63rem + 1.5vw, 3rem);
  --text-6xl: clamp(2.25rem, 1.69rem + 2.25vw, 3.75rem);
  --text-7xl: clamp(2.5rem, 1.75rem + 3.01vw, 4.5rem);
  --text-8xl: clamp(3rem, 1.87rem + 4.51vw, 6rem);

  /* ── Line Heights ─────────────────────────────────────────────────────── */
  --leading-none: 1;
  --leading-tight: 1.15;
  --leading-snug: 1.3;
  --leading-normal: 1.5;
  --leading-relaxed: 1.6;
  --leading-loose: 1.75;

  /* ── Letter Spacing ───────────────────────────────────────────────────── */
  --tracking-tighter: -0.025em;
  --tracking-tight: -0.015em;
  --tracking-slight: -0.01em;
  --tracking-normal: 0;
  --tracking-wide: 0.05em;
  --tracking-wider: 0.08em;
  --tracking-widest: 0.1em;

  /* ── Font Weights ─────────────────────────────────────────────────────── */
  --weight-normal: 400;
  --weight-medium: 500;
  --weight-semibold: 600;
  --weight-bold: 700;
  --weight-extrabold: 800;
  --weight-black: 900;

  /* ── Measure (Line Length) ────────────────────────────────────────────── */
  --measure-narrow: 45ch;
  --measure-base: 65ch;
  --measure-wide: 75ch;
}

/* ==========================================================================
   Base Reset
   ========================================================================== */

html {
  font-size: 100%; /* 16px — never change this */
  -webkit-text-size-adjust: 100%;
  text-size-adjust: 100%;
  font-optical-sizing: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

body {
  font-family: var(--font-sans);
  font-size: var(--text-base);
  font-weight: var(--weight-normal);
  line-height: var(--leading-normal);
  letter-spacing: var(--tracking-normal);
}

/* ==========================================================================
   Semantic Type Classes
   ========================================================================== */

/* Caption — timestamps, metadata, helper text */
.type-caption {
  font-size: var(--text-xs);
  font-weight: var(--weight-normal);
  line-height: var(--leading-snug);
  letter-spacing: var(--tracking-normal);
}

/* Label — form labels, nav items, badges */
.type-label {
  font-size: var(--text-sm);
  font-weight: var(--weight-medium);
  line-height: var(--leading-snug);
  letter-spacing: var(--tracking-normal);
}

/* Overline — uppercase small labels */
.type-overline {
  font-size: var(--text-xs);
  font-weight: var(--weight-semibold);
  line-height: var(--leading-snug);
  letter-spacing: var(--tracking-widest);
  text-transform: uppercase;
}

/* Body — paragraphs, descriptions, lists */
.type-body {
  font-size: var(--text-base);
  font-weight: var(--weight-normal);
  line-height: var(--leading-normal);
  letter-spacing: var(--tracking-normal);
}

/* Body Large — lead paragraphs */
.type-body-lg {
  font-size: var(--text-lg);
  font-weight: var(--weight-normal);
  line-height: var(--leading-normal);
  letter-spacing: var(--tracking-normal);
}

/* Heading Small — card titles, section labels */
.type-heading-sm {
  font-size: var(--text-xl);
  font-weight: var(--weight-semibold);
  line-height: var(--leading-snug);
  letter-spacing: var(--tracking-slight);
}

/* Heading — H3 equivalent */
.type-heading {
  font-size: var(--text-2xl);
  font-weight: var(--weight-semibold);
  line-height: var(--leading-snug);
  letter-spacing: var(--tracking-tight);
}

/* Heading Large — H2 equivalent */
.type-heading-lg {
  font-size: var(--text-3xl);
  font-weight: var(--weight-bold);
  line-height: var(--leading-tight);
  letter-spacing: var(--tracking-tight);
}

/* Title — H1 equivalent */
.type-title {
  font-size: var(--text-4xl);
  font-weight: var(--weight-bold);
  line-height: var(--leading-tight);
  letter-spacing: var(--tracking-tighter);
}

/* Display Small — hero subtitles, feature callouts */
.type-display-sm {
  font-size: var(--text-5xl);
  font-weight: var(--weight-bold);
  line-height: var(--leading-none);
  letter-spacing: var(--tracking-tighter);
}

/* Display — hero headlines */
.type-display {
  font-size: var(--text-6xl);
  font-weight: var(--weight-bold);
  line-height: var(--leading-none);
  letter-spacing: var(--tracking-tighter);
}

/* Display Large — landing heroes */
.type-display-lg {
  font-size: var(--text-7xl);
  font-weight: var(--weight-extrabold);
  line-height: var(--leading-none);
  letter-spacing: var(--tracking-tighter);
}

/* Display XL — statement pieces */
.type-display-xl {
  font-size: var(--text-8xl);
  font-weight: var(--weight-black);
  line-height: var(--leading-none);
  letter-spacing: var(--tracking-tighter);
}

/* ==========================================================================
   Text Containers
   ========================================================================== */

.type-prose {
  max-width: var(--measure-base);
}

.type-prose-narrow {
  max-width: var(--measure-narrow);
}

.type-prose-wide {
  max-width: var(--measure-wide);
}

/* ==========================================================================
   Modern Enhancements (Progressive)
   ========================================================================== */

h1, h2, h3 {
  text-wrap: balance;
}

p {
  text-wrap: pretty;
}

/* Tabular numbers in data contexts */
table td,
[data-numeric] {
  font-variant-numeric: tabular-nums;
}

/* Code blocks */
code, pre, kbd, samp {
  font-family: var(--font-mono);
}
```

## Dark Mode Extension

```css
@media (prefers-color-scheme: dark) {
  :root {
    /* Slightly increase font weight in dark mode to compensate for
       halation (light text on dark bg appears thinner) */
    --weight-normal: 400;
    --weight-medium: 500;

    /* Slightly reduce antialiasing strength */
    -webkit-font-smoothing: auto;
  }
}
```

## Usage Example

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <link rel="stylesheet" href="type-system.css">
  <link rel="preload" href="/fonts/inter-var.woff2" as="font" type="font/woff2" crossorigin>
</head>
<body>
  <article class="type-prose" style="margin: 0 auto; padding: 0 1rem;">
    <p class="type-overline" style="color: var(--color-primary);">Announcing</p>
    <h1 class="type-title" style="margin-bottom: 1rem;">Page Title Here</h1>
    <p class="type-body-lg" style="color: var(--color-muted);">
      Lead paragraph introducing the content.
    </p>

    <h2 class="type-heading-lg" style="margin-top: 3rem;">Section Title</h2>
    <p class="type-body">
      Body text at the optimal reading width with proper line height.
    </p>

    <h3 class="type-heading" style="margin-top: 2rem;">Subsection</h3>
    <p class="type-body">More content here.</p>
  </article>
</body>
</html>
```
