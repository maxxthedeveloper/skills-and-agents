# Interface Polish Principles — Design Reference

7 visual design principles for static polish and visual refinement.

For animation and interaction principles (3, 6-8, 12-18), see `animation-principles.md`.

---

## 1. Text Wrapping Balance

Distribute text evenly across lines to prevent orphaned words.

**Tailwind:**
```html
<h2 class="text-balance">Your heading text here</h2>
<p class="text-pretty">Body paragraph text that should wrap nicely without orphans.</p>
```

**CSS equivalent:**
```css
h2 { text-wrap: balance; }
p  { text-wrap: pretty; }
```

**When to apply:**
- `text-balance` on all headings (h1-h6) and short display text
- `text-pretty` on body paragraphs and longer text blocks
- `text-balance` is more aggressive — good for short text, headings
- `text-pretty` is lighter — good for multi-line paragraphs

---

## 2. Concentric Border Radius

Nested elements should have proportional border radii.

**Formula:** `outer_radius = inner_radius + gap_between_elements`

**Examples:**
```html
<!-- Inner: rounded-xl (12px), Padding: p-2 (8px), Outer: 20px -->
<div class="rounded-[20px] p-2 bg-gray-100">
  <div class="rounded-xl bg-white p-4">
    Inner content
  </div>
</div>

<!-- Inner: rounded-lg (8px), Padding: p-1.5 (6px), Outer: 14px -->
<div class="rounded-[14px] p-1.5 bg-gray-100">
  <button class="rounded-lg bg-blue-500 px-4 py-2">Click me</button>
</div>
```

**Common Tailwind radius values:**
- `rounded-sm` = 2px
- `rounded` = 4px
- `rounded-md` = 6px
- `rounded-lg` = 8px
- `rounded-xl` = 12px
- `rounded-2xl` = 16px
- `rounded-3xl` = 24px

---

## 4. Crispy Text

Render thinner, crisper text on macOS.

**Tailwind (apply to layout root):**
```html
<body class="antialiased">
```

**CSS equivalent:**
```css
body {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
```

**Important:** Apply once at the layout root level so all text inherits it. Do not apply per-component.

---

## 5. Tabular Numbers

Prevent number shifting when values update by using monospaced digits.

**Tailwind:**
```html
<span class="tabular-nums">1,234.56</span>
<div class="tabular-nums text-2xl font-semibold">03:45:12</div>
```

**CSS equivalent:**
```css
.numeric-display {
  font-variant-numeric: tabular-nums;
}
```

**When to apply:**
- Timers and countdowns
- Prices and financial data
- Dashboard metrics and counters
- Table columns with numbers
- Any number that updates in real-time

**Caveat:** Some fonts like Inter change the appearance of certain numerals (especially 6 and 9) when tabular-nums is applied. Test with your font.

---

## 9. Optical Alignment

Adjust spacing for visual balance rather than mathematical precision.

**Button with icon — optical padding:**
```html
<!-- Geometrically equal padding (looks unbalanced) -->
<button class="px-4 py-2">
  <span>Label</span>
  <ChevronRight />
</button>

<!-- Optically adjusted (looks balanced) -->
<button class="pl-4 pr-3 py-2">
  <span>Label</span>
  <ChevronRight />
</button>
```

**Icon in circle — optical centering:**
```html
<!-- Play icon needs slight right offset to look centered -->
<div class="flex items-center justify-center size-10 rounded-full bg-blue-500">
  <PlayIcon class="size-4 translate-x-[1px]" />
</div>
```

**Common optical adjustments:**
- Play/arrow icons: shift 1-2px in the pointing direction
- Text + icon buttons: reduce padding on the icon side by 2-4px
- Checkbox + label: adjust vertical alignment by 1px when font metrics differ
- Cards with mixed content: adjust internal spacing for visual weight balance

**Best practice:** Fix optical issues in the SVG source when possible. Adjust the viewBox or internal positioning rather than CSS transforms.

---

## 10. Shadows Over Borders

Use layered box-shadows instead of solid borders for depth.

**Three-layer shadow composition:**
```html
<!-- Tailwind (arbitrary shadow) -->
<div class="shadow-[0px_0px_0px_1px_rgba(0,0,0,0.06),0px_1px_2px_-1px_rgba(0,0,0,0.06),0px_2px_4px_0px_rgba(0,0,0,0.04)]">
  Card content
</div>

<!-- With hover state -->
<div class="
  shadow-[0px_0px_0px_1px_rgba(0,0,0,0.06),0px_1px_2px_-1px_rgba(0,0,0,0.06),0px_2px_4px_0px_rgba(0,0,0,0.04)]
  hover:shadow-[0px_0px_0px_1px_rgba(0,0,0,0.08),0px_2px_4px_-1px_rgba(0,0,0,0.08),0px_4px_8px_0px_rgba(0,0,0,0.06)]
  transition-shadow
">
  Hoverable card
</div>
```

**CSS equivalent:**
```css
.card {
  box-shadow:
    0px 0px 0px 1px rgba(0, 0, 0, 0.06),
    0px 1px 2px -1px rgba(0, 0, 0, 0.06),
    0px 2px 4px 0px rgba(0, 0, 0, 0.04);
  transition: box-shadow 150ms ease;
}
.card:hover {
  box-shadow:
    0px 0px 0px 1px rgba(0, 0, 0, 0.08),
    0px 2px 4px -1px rgba(0, 0, 0, 0.08),
    0px 4px 8px 0px rgba(0, 0, 0, 0.06);
}
```

**The three layers:**
1. `0px 0px 0px 1px` — outline/border replacement (spread-only, no blur)
2. `0px 1px 2px -1px` — soft near shadow (adds subtle depth)
3. `0px 2px 4px 0px` — ambient shadow (grounds the element)

**Why shadows over borders:**
- Transparent rgba values adapt to any background color
- Layered shadows create more natural depth
- `box-shadow` doesn't affect layout (unlike `border`)
- Smooth hover transitions are trivial with `transition-shadow`

---

## 11. Image Outlines

Apply subtle outlines to images for visual containment.

**Tailwind:**
```html
<!-- Light mode -->
<img
  src="photo.jpg"
  class="rounded-lg outline outline-1 outline-black/10 -outline-offset-1"
/>

<!-- Dark mode aware -->
<img
  src="photo.jpg"
  class="rounded-lg outline outline-1 outline-black/10 dark:outline-white/10 -outline-offset-1"
/>
```

**CSS equivalent:**
```css
img {
  outline: 1px solid rgba(0, 0, 0, 0.1);
  outline-offset: -1px;
}

@media (prefers-color-scheme: dark) {
  img {
    outline-color: rgba(255, 255, 255, 0.1);
  }
}
```

**Why outline instead of border:**
- `outline` doesn't affect layout or sizing
- `-outline-offset-1` places it inside the image bounds
- Works with `border-radius` (since outline follows it in modern browsers)
- Consistent visual boundary for images on both light and dark backgrounds

---

## Compounding Effect

These design principles work in concert with the 11 animation principles in `animation-principles.md`. No single detail makes or breaks an interface. But their collective, consistent application is what separates interfaces that feel "fine" from interfaces that feel crafted. Apply all of them, all the time.
