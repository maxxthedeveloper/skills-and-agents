# Tailwind CSS Type System Template

## Complete tailwind.config.ts Extension

```typescript
import type { Config } from "tailwindcss";

const config: Config = {
  theme: {
    extend: {
      fontFamily: {
        sans: [
          "Inter",
          "ui-sans-serif",
          "system-ui",
          "-apple-system",
          "BlinkMacSystemFont",
          "Segoe UI",
          "Roboto",
          "Helvetica Neue",
          "Arial",
          "sans-serif",
        ],
        serif: [
          "ui-serif",
          "Georgia",
          "Cambria",
          "Times New Roman",
          "Times",
          "serif",
        ],
        mono: [
          "Geist Mono",
          "ui-monospace",
          "SFMono-Regular",
          "SF Mono",
          "Menlo",
          "Consolas",
          "Liberation Mono",
          "Courier New",
          "monospace",
        ],
      },

      fontSize: {
        // Static sizes (xs through base never scale)
        xs: ["0.75rem", { lineHeight: "1rem", letterSpacing: "0" }],
        sm: ["0.875rem", { lineHeight: "1.25rem", letterSpacing: "0" }],
        base: ["1rem", { lineHeight: "1.5rem", letterSpacing: "0" }],

        // Fluid sizes (lg through 8xl use clamp)
        lg: [
          "clamp(1rem, 0.95rem + 0.19vw, 1.125rem)",
          { lineHeight: "1.75rem", letterSpacing: "0" },
        ],
        xl: [
          "clamp(1.125rem, 1.08rem + 0.19vw, 1.25rem)",
          { lineHeight: "1.75rem", letterSpacing: "-0.01em" },
        ],
        "2xl": [
          "clamp(1.25rem, 1.16rem + 0.38vw, 1.5rem)",
          { lineHeight: "2rem", letterSpacing: "-0.015em" },
        ],
        "3xl": [
          "clamp(1.5rem, 1.36rem + 0.56vw, 1.875rem)",
          { lineHeight: "2.25rem", letterSpacing: "-0.02em" },
        ],
        "4xl": [
          "clamp(1.75rem, 1.57rem + 0.75vw, 2.25rem)",
          { lineHeight: "2.5rem", letterSpacing: "-0.02em" },
        ],
        "5xl": [
          "clamp(2rem, 1.63rem + 1.5vw, 3rem)",
          { lineHeight: "1", letterSpacing: "-0.025em" },
        ],
        "6xl": [
          "clamp(2.25rem, 1.69rem + 2.25vw, 3.75rem)",
          { lineHeight: "1", letterSpacing: "-0.025em" },
        ],
        "7xl": [
          "clamp(2.5rem, 1.75rem + 3.01vw, 4.5rem)",
          { lineHeight: "1", letterSpacing: "-0.025em" },
        ],
        "8xl": [
          "clamp(3rem, 1.87rem + 4.51vw, 6rem)",
          { lineHeight: "1", letterSpacing: "-0.025em" },
        ],
      },
    },
  },
};

export default config;
```

## Utility Classes Reference

### Semantic Typography Classes (globals.css or Tailwind plugin)

```css
@layer components {
  /* Captions & metadata */
  .type-caption {
    @apply text-xs font-normal tracking-normal;
  }

  /* Labels, nav items, badges */
  .type-label {
    @apply text-sm font-medium tracking-normal;
  }

  /* Overlines (uppercase small labels) */
  .type-overline {
    @apply text-xs font-semibold uppercase tracking-widest;
  }

  /* Body text */
  .type-body {
    @apply text-base font-normal leading-relaxed tracking-normal;
  }

  /* Lead / large body */
  .type-body-lg {
    @apply text-lg font-normal tracking-normal;
  }

  /* Card titles, section labels */
  .type-heading-sm {
    @apply text-xl font-semibold tracking-tight;
  }

  /* Section headings — H3 */
  .type-heading {
    @apply text-2xl font-semibold tracking-tight;
  }

  /* Page sub-sections — H2 */
  .type-heading-lg {
    @apply text-3xl font-bold tracking-tight;
  }

  /* Page titles — H1 */
  .type-title {
    @apply text-4xl font-bold tracking-tighter;
  }

  /* Hero subtitles */
  .type-display-sm {
    @apply text-5xl font-bold tracking-tighter;
  }

  /* Hero headlines */
  .type-display {
    @apply text-6xl font-bold tracking-tighter;
  }

  /* Landing heroes */
  .type-display-lg {
    @apply text-7xl font-extrabold tracking-tighter;
  }

  /* Statement pieces */
  .type-display-xl {
    @apply text-8xl font-black tracking-tighter;
  }
}
```

### Text Container Classes

```css
@layer components {
  /* Prose container — optimal reading width */
  .type-prose {
    @apply max-w-prose; /* ~65ch */
  }

  /* Narrow prose — sidebars, cards */
  .type-prose-narrow {
    @apply max-w-lg; /* ~32rem / ~55ch */
  }

  /* Wide prose — full-width content areas */
  .type-prose-wide {
    @apply max-w-3xl; /* ~48rem / ~75ch */
  }
}
```

### Typography Reset

```css
@layer base {
  html {
    @apply text-base antialiased;
    -webkit-text-size-adjust: 100%;
    text-size-adjust: 100%;
    font-optical-sizing: auto;
  }

  body {
    @apply font-sans text-base font-normal leading-relaxed text-gray-900 dark:text-gray-100;
  }

  h1, h2, h3 {
    text-wrap: balance;
  }

  p {
    text-wrap: pretty;
  }

  /* Tabular numbers in data contexts */
  table td,
  [data-numeric],
  .tabular-nums {
    font-variant-numeric: tabular-nums;
  }
}
```

## Usage Examples

### Page Layout
```html
<article class="type-prose mx-auto px-4">
  <h1 class="type-title mb-4">Page Title</h1>
  <p class="type-body-lg text-gray-600 mb-8">
    Lead paragraph with larger, lighter text.
  </p>
  <h2 class="type-heading-lg mt-12 mb-4">Section Title</h2>
  <p class="type-body mb-4">
    Regular body text in the optimal reading width.
  </p>
</article>
```

### Hero Section
```html
<section class="text-center">
  <p class="type-overline text-blue-600 mb-4">Announcing v2.0</p>
  <h1 class="type-display mb-6">
    Build faster with<br>better typography
  </h1>
  <p class="type-body-lg text-gray-600 max-w-2xl mx-auto">
    A complete type system for modern web applications.
  </p>
</section>
```

### Data Table
```html
<table>
  <thead>
    <tr>
      <th class="type-label text-left">Name</th>
      <th class="type-label text-right tabular-nums">Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="type-body">Product A</td>
      <td class="type-body text-right tabular-nums">$12,450.00</td>
    </tr>
  </tbody>
</table>
```
