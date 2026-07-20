# Font Pairing Rules

## Core Principles

### 1. Contrast, Not Conflict
Pair fonts that are clearly different in character but share structural qualities. A geometric sans with a humanist serif creates contrast. Two geometric sans-serifs fight.

### 2. Match x-Height
Fonts with similar x-heights look harmonious together at the same size. Mismatched x-heights create visual discord even when the font-size value is identical.

### 3. One is Enough (Usually)
A single well-chosen typeface family with multiple weights and optical sizes handles most product UI. A second font is a luxury for headings or editorial. Three is the maximum.

### 4. Functionality > Aesthetics
The heading font gets attention. The body font does the work. Never sacrifice body readability for a trendy heading pairing.

### 5. Variable First
Prefer variable fonts. One file, all weights, better performance. A single variable font eliminates font loading complexity.

---

## Curated Pairings

### Pairing 1: Inter + System Serif
**Heading**: Inter (sans-serif)
**Body**: System serif stack
**Tone**: Clean, professional, fast-loading
**Best for**: SaaS products, dashboards, developer tools
**CSS**:
```css
--font-heading: "Inter", ui-sans-serif, system-ui, -apple-system, sans-serif;
--font-body: ui-serif, Georgia, Cambria, "Times New Roman", Times, serif;
```
**Google Fonts**: `Inter:wght@400;500;600;700`
**Why it works**: Inter is the workhorse of modern UI. System serif adds warmth to long-form content without any additional font downloads.

### Pairing 2: Inter (Solo)
**All text**: Inter variable
**Tone**: Neutral, systematic, Tailwind-native
**Best for**: Product UI, admin panels, tools, anything that needs to feel functional
**CSS**:
```css
--font-sans: "Inter", ui-sans-serif, system-ui, -apple-system, sans-serif;
```
**Google Fonts**: `Inter:wght@400..700`
**Why it works**: Inter was designed for screens. Its large x-height, open apertures, and tabular number support make it ideal for data-heavy interfaces.

### Pairing 3: Geist + Geist Mono
**Heading/Body**: Geist (sans-serif)
**Code**: Geist Mono (monospace)
**Tone**: Technical, modern, Vercel/Next.js aesthetic
**Best for**: Developer-facing products, documentation, technical SaaS
**CSS**:
```css
--font-sans: "Geist", ui-sans-serif, system-ui, -apple-system, sans-serif;
--font-mono: "Geist Mono", ui-monospace, "Cascadia Code", "Source Code Pro", monospace;
```
**Why it works**: Geist was built by Vercel specifically for digital interfaces. Its mono companion maintains the same visual rhythm.

### Pairing 4: Cal Sans + Inter
**Heading**: Cal Sans (display sans-serif)
**Body**: Inter (sans-serif)
**Tone**: Bold, confident, Cal.com aesthetic
**Best for**: SaaS landing pages, marketing sites, bold product positioning
**CSS**:
```css
--font-heading: "Cal Sans", ui-sans-serif, system-ui, sans-serif;
--font-body: "Inter", ui-sans-serif, system-ui, -apple-system, sans-serif;
```
**Why it works**: Cal Sans provides distinctive headings while Inter handles readability. The contrast between display and text optical sizes is strong.

### Pairing 5: Source Serif 4 + Source Sans 3
**Heading/Editorial**: Source Serif 4 (serif)
**Body/UI**: Source Sans 3 (sans-serif)
**Code**: Source Code Pro (monospace)
**Tone**: Editorial, authoritative, Adobe-quality
**Best for**: Blogs, documentation sites, content-heavy platforms, editorial products
**CSS**:
```css
--font-serif: "Source Serif 4", ui-serif, Georgia, serif;
--font-sans: "Source Sans 3", ui-sans-serif, system-ui, -apple-system, sans-serif;
--font-mono: "Source Code Pro", ui-monospace, monospace;
```
**Google Fonts**: All three in Source superfamily
**Why it works**: Designed as a superfamily — they share structural DNA and harmonize effortlessly. Three optical roles from one design system.

### Pairing 6: System UI Stack (Zero-Download)
**All text**: System fonts only
**Tone**: Native, fast, familiar
**Best for**: Performance-critical apps, native-feel web apps, tools where branding comes from UI, not type
**CSS**:
```css
--font-sans: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
--font-serif: ui-serif, Georgia, Cambria, "Times New Roman", Times, serif;
--font-mono: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", "Courier New", monospace;
```
**Why it works**: Zero font downloads. The OS provides battle-tested typography. San Francisco on Apple, Segoe UI on Windows, Roboto on Android.

---

## Monospace Recommendations

Always include a monospace font for code blocks, data, and technical content:

| Font | Source | Character |
|------|--------|-----------|
| Geist Mono | Vercel | Modern, clean, wide |
| JetBrains Mono | JetBrains | Ligatures, developer-favorite |
| Source Code Pro | Adobe | Classic, neutral |
| Fira Code | Mozilla | Ligatures, open source |
| Berkeley Mono | Berkeley Graphics | Premium, beautiful |
| System mono | Built-in | SF Mono (Mac), Cascadia Code (Win) |

**CSS fallback stack**:
```css
--font-mono: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", "Courier New", monospace;
```

---

## Font Loading Best Practices

### 1. Use `font-display: swap`
```css
@font-face {
  font-family: "Inter";
  src: url("/fonts/inter-var.woff2") format("woff2");
  font-weight: 100 900;
  font-display: swap;
}
```

### 2. Preload Critical Fonts
```html
<link rel="preload" href="/fonts/inter-var.woff2" as="font" type="font/woff2" crossorigin>
```

### 3. Subset When Possible
Only load the character sets you need. For English-only: `latin` subset saves ~50% file size.

### 4. Use `size-adjust` for CLS Prevention
```css
@font-face {
  font-family: "Inter Fallback";
  src: local("Arial");
  size-adjust: 107%;
  ascent-override: 90%;
  descent-override: 22%;
  line-gap-override: 0%;
}
```

### 5. Variable Fonts > Multiple Files
One variable font file replaces 4-6 static font files. Modern browser support is >95%.
