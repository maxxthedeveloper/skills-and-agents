# Interface Polish Principles — Animation Reference

11 animation and interaction principles for motion, timing, and responsiveness.

For visual design principles (1-2, 4-5, 9-11), see `interface-polish-principles.md`.

---

## 3. Contextual Icon Animation

Animate icons smoothly when they swap in response to user actions.

**CSS-only approach:**
```css
.icon-swap {
  transition: opacity 150ms ease, transform 150ms ease, filter 150ms ease;
}
.icon-swap.entering {
  opacity: 0;
  transform: scale(0.8);
  filter: blur(4px);
}
.icon-swap.visible {
  opacity: 1;
  transform: scale(1);
  filter: blur(0px);
}
```

**Framer Motion approach:**
```tsx
<AnimatePresence mode="wait">
  <motion.div
    key={isCopied ? "check" : "copy"}
    initial={{ opacity: 0, scale: 0.8, filter: "blur(4px)" }}
    animate={{ opacity: 1, scale: 1, filter: "blur(0px)" }}
    exit={{ opacity: 0, scale: 0.8, filter: "blur(4px)" }}
    transition={{ type: "spring", duration: 0.2, bounce: 0 }}
  >
    {isCopied ? <CheckIcon /> : <CopyIcon />}
  </motion.div>
</AnimatePresence>
```

**When to apply:**
- Copy/paste confirmation icons
- Toggle state icons (play/pause, expand/collapse)
- Status indicator changes
- NOT for decorative icons or static UI elements

---

## 6. Interruptible Animations

Use CSS transitions for interactive elements so users can interrupt mid-animation.

**Why transitions over keyframes:**
- CSS transitions interpolate toward the latest target state when interrupted
- Keyframe animations run on a fixed timeline and cannot retarget
- Transitions feel responsive; keyframes feel mechanical

**Good (interruptible):**
```css
.dropdown {
  transition: opacity 200ms ease-out, transform 200ms ease-out;
}
.dropdown.open {
  opacity: 1;
  transform: translateY(0);
}
.dropdown.closed {
  opacity: 0;
  transform: translateY(-8px);
}
```

**Bad (not interruptible):**
```css
@keyframes slideDown {
  from { opacity: 0; transform: translateY(-8px); }
  to   { opacity: 1; transform: translateY(0); }
}
.dropdown.open {
  animation: slideDown 200ms ease-out forwards;
}
```

**When keyframes ARE appropriate:**
- Staged sequences where multiple phases must play in order
- Looping animations (spinners, progress indicators)
- Animations that should NOT be interrupted

---

## 7. Staggered Enter Animations

Break complex enter animations into smaller, sequenced elements.

**CSS approach with custom properties:**
```css
.stagger-item {
  opacity: 0;
  transform: translateY(8px);
  filter: blur(5px);
  animation: stagger-in 400ms ease-out forwards;
  animation-delay: calc(var(--stagger-index) * 80ms);
}

@keyframes stagger-in {
  to {
    opacity: 1;
    transform: translateY(0);
    filter: blur(0);
  }
}
```

```html
<div style="--stagger-index: 0" class="stagger-item">Title</div>
<div style="--stagger-index: 1" class="stagger-item">Description</div>
<div style="--stagger-index: 2" class="stagger-item">Button</div>
```

**Framer Motion approach:**
```tsx
const container = {
  animate: { transition: { staggerChildren: 0.08 } }
};

const item = {
  initial: { opacity: 0, y: 8, filter: "blur(5px)" },
  animate: { opacity: 1, y: 0, filter: "blur(0px)" },
};

<motion.div variants={container} initial="initial" animate="animate">
  <motion.h2 variants={item}>Title</motion.h2>
  <motion.p variants={item}>Description</motion.p>
  <motion.button variants={item}>Action</motion.button>
</motion.div>
```

**Guidelines:**
- 80-100ms delay between elements
- Animate opacity + translateY (8px) + blur (5px)
- Keep total sequence under 400ms
- Group related elements (don't stagger every single word)

---

## 8. Subtle Exit Animations

Exit transitions should be less pronounced than entries.

**Framer Motion example:**
```tsx
// Subtle exit (preferred)
<motion.div
  exit={{ opacity: 0, y: -12 }}
  transition={{ duration: 0.15 }}
/>

// Full exit (avoid for most UI)
<motion.div
  exit={{ opacity: 0, y: "calc(-100% - 4px)" }}
  transition={{ duration: 0.2 }}
/>
```

**Guidelines:**
- Exit duration ~20% shorter than enter duration
- Use fixed small values (8-12px) instead of percentage-based movement
- Maintain directional indication (exit upward if entered from above)
- Opacity fade is usually sufficient — movement is optional

---

## 12. Transform Origin Awareness

Scale and animate overlays FROM their trigger point, not from center.

**Tailwind / CSS:**
```html
<!-- Dropdown anchored to top-left trigger -->
<div class="origin-top-left scale-95 opacity-0 transition data-[open]:scale-100 data-[open]:opacity-100">
  Dropdown content
</div>

<!-- Popover from a bottom button -->
<div class="origin-bottom">
  Popover content
</div>
```

**Radix UI (automatic via CSS variable):**
```css
[data-radix-popper-content-wrapper] {
  transform-origin: var(--radix-popover-content-transform-origin);
}
```

**Framer Motion:**
```tsx
<motion.div
  style={{ transformOrigin: "top left" }}
  initial={{ opacity: 0, scale: 0.95 }}
  animate={{ opacity: 1, scale: 1 }}
  exit={{ opacity: 0, scale: 0.95 }}
/>
```

**When to apply:**
- Dropdown menus: `origin-top` or `origin-top-left` depending on alignment
- Tooltips: origin toward the trigger element
- Popovers: use Radix's `--radix-popover-content-transform-origin` when available
- Context menus: origin at the cursor position
- NOT for modals/dialogs (center origin is correct for center-screen overlays)

---

## 13. Active Press Feedback

Apply a subtle scale-down on `:active` for all clickable elements.

**Tailwind:**
```html
<button class="active:scale-[0.97] transition-transform">
  Click me
</button>

<!-- Card with press feedback -->
<div class="cursor-pointer active:scale-[0.98] transition-transform">
  Clickable card
</div>
```

**CSS equivalent:**
```css
button, .clickable {
  transition: transform 100ms ease;
}
button:active, .clickable:active {
  transform: scale(0.97);
}
```

**Guidelines:**
- Buttons: `scale(0.97)` — noticeable but not jarring
- Cards/larger surfaces: `scale(0.98)` — subtler for bigger elements
- List items: `scale(0.98)` or `scale(0.99)` depending on size
- The transition should be very short (~100ms) or instant — press feedback must feel mechanical
- Never scale from `0` on entrance animations — minimum is `scale(0.9)` to avoid a "popping out of nothing" effect
- Apply to: buttons, cards, list items, toggles, chips, tags

---

## 14. Custom Easing Curves

Use intentional easing curves instead of CSS defaults.

**Recommended curves:**
```css
:root {
  /* Smooth spring — good default for entrances */
  --ease-spring: cubic-bezier(0.22, 1, 0.36, 1);
  /* Snappy — for quick, responsive interactions */
  --ease-snappy: cubic-bezier(0.16, 1, 0.3, 1);
  /* Gentle deceleration — for subtle movements */
  --ease-out-soft: cubic-bezier(0.25, 1, 0.5, 1);
}
```

**Tailwind (arbitrary values):**
```html
<!-- Entrance animation -->
<div class="transition-all duration-200 ease-[cubic-bezier(0.22,1,0.36,1)]">
  Content entering
</div>

<!-- Exit animation -->
<div class="transition-all duration-150 ease-in">
  Content exiting
</div>
```

**Rules:**
- **Entrances:** Use `ease-out` or custom deceleration curves (element arrives and settles)
- **Exits:** Use `ease-in` (element accelerates away)
- **Never use `linear`** for UI elements — it feels robotic (exception: progress bars, loading indicators)
- **Never use default `ease`** — it's a compromise that's not ideal for either entrance or exit
- Built-in `ease-in-out` is acceptable for hover states and symmetric interactions

---

## 15. Performance-Safe Properties

Only animate properties that the GPU can composite without layout reflow.

**Safe to animate (GPU-composited):**
```css
.animated {
  transition: transform 200ms ease-out, opacity 200ms ease-out;
}
```

**Never animate (triggers layout reflow):**
```css
/* BAD — triggers reflow every frame */
.bad {
  transition: height 200ms, width 200ms, top 200ms, left 200ms,
              margin 200ms, padding 200ms;
}
```

**Height reveal with clip-path (hardware-accelerated):**
```css
/* Instead of animating height */
.reveal {
  clip-path: inset(0 0 100% 0);
  transition: clip-path 300ms cubic-bezier(0.22, 1, 0.36, 1);
}
.reveal.open {
  clip-path: inset(0 0 0 0);
}
```

**Framer Motion equivalent:**
```tsx
// BAD — animating height
<motion.div animate={{ height: isOpen ? "auto" : 0 }} />

// GOOD — use clip-path or AnimatePresence with opacity + transform
<motion.div
  initial={{ opacity: 0, y: -8 }}
  animate={{ opacity: 1, y: 0 }}
  exit={{ opacity: 0, y: -8 }}
/>
```

**Key rules:**
- `transform` and `opacity` are the only safe bets for 60fps animation
- `filter` (blur, brightness) is usually GPU-composited but test on target devices
- Avoid updating CSS custom properties per-frame — causes style recalc on all children
- When you need to animate dimensions, use `clip-path: inset()` as a hardware-accelerated alternative
- For color transitions, `background-color` and `color` are acceptable at low frequency (hover states) but not for per-frame animation

---

## 16. Animation Restraint

Not everything needs to animate. Prioritize responsiveness over showiness.

**The 300ms ceiling:**
```css
/* UI transitions should NEVER exceed 300ms */
.ui-transition {
  transition-duration: 200ms; /* ideal for most UI */
}

/* Complex orchestrations (staggered sequences): max 600ms total */
.stagger-item {
  animation-delay: calc(var(--i) * 80ms);
  animation-duration: 300ms;
  /* 5 items × 80ms stagger + 300ms duration ≈ 700ms, push it to 4 items or reduce delay */
}
```

**When NOT to animate:**
- Keyboard-initiated actions (feels slow and disconnected when the user already knows what happened)
- High-frequency actions (toggling, selecting from a list done hundreds of times/day)
- Text input responses (typing, autocomplete selection)

**Exit vs entrance timing:**
```tsx
// Entrance: 200ms
<motion.div
  initial={{ opacity: 0, y: 8 }}
  animate={{ opacity: 1, y: 0 }}
  transition={{ duration: 0.2 }}
/>

// Exit: ~20% shorter = 160ms
<motion.div
  exit={{ opacity: 0, y: -8 }}
  transition={{ duration: 0.16 }}
/>
```

---

## 17. Sequential Tooltip Delays

When moving between tooltip triggers, eliminate the delay after the first tooltip opens.

**Implementation pattern:**
```tsx
// Shared tooltip group — first shows with delay, subsequent are instant
const TOOLTIP_DELAY = 300; // ms
const TOOLTIP_SKIP_WINDOW = 400; // ms after last close

let lastCloseTime = 0;

function getTooltipDelay(): number {
  const timeSinceClose = Date.now() - lastCloseTime;
  return timeSinceClose < TOOLTIP_SKIP_WINDOW ? 0 : TOOLTIP_DELAY;
}

function onTooltipClose() {
  lastCloseTime = Date.now();
}
```

**CSS/HTML approach with `data-instant`:**
```css
[data-tooltip] {
  --tooltip-delay: 300ms;
}
[data-tooltip][data-instant] {
  --tooltip-delay: 0ms;
  /* Also remove transition for instant feel */
  --tooltip-transition: 0ms;
}
```

**Radix Tooltip (built-in support):**
```tsx
<TooltipProvider delayDuration={300} skipDelayDuration={400}>
  <Tooltip>...</Tooltip>
  <Tooltip>...</Tooltip>
</TooltipProvider>
```

**When to apply:**
- Toolbar icon tooltips
- Navigation icon labels
- Any row of elements with individual tooltips
- The key insight: zero delay AND zero transition for subsequent tooltips — both must be instant

---

## 18. Respect Reduced Motion

`prefers-reduced-motion: reduce` is non-negotiable accessibility.

**Global CSS reset:**
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

**Tailwind (built-in modifier):**
```html
<!-- Animation only plays when motion is OK -->
<div class="motion-safe:animate-fadeIn">Content</div>

<!-- Transition removed when reduced motion is preferred -->
<div class="transition-transform motion-reduce:transition-none active:scale-[0.97] motion-reduce:active:scale-100">
  Button
</div>
```

**Framer Motion:**
```tsx
import { useReducedMotion } from "motion/react";

function AnimatedCard() {
  const shouldReduceMotion = useReducedMotion();

  return (
    <motion.div
      initial={shouldReduceMotion ? false : { opacity: 0, y: 8 }}
      animate={{ opacity: 1, y: 0 }}
      transition={shouldReduceMotion ? { duration: 0 } : { duration: 0.2 }}
    />
  );
}
```

**Guidelines:**
- Keep opacity changes (fades) — they're generally safe for motion-sensitive users
- Remove all movement (translateX/Y), scale, and rotation
- Remove parallax effects entirely
- Keep layout shifts and content changes — just remove the animated transition
- Test by enabling "Reduce motion" in macOS System Settings > Accessibility > Display

---

## Compounding Effect

These animation principles work in concert with the 7 design principles in `interface-polish-principles.md`. No single detail makes or breaks an interface. But their collective, consistent application is what separates interfaces that feel "fine" from interfaces that feel crafted. Apply all of them, all the time.
