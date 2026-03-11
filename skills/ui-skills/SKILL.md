---
name: ui-skills
description: >-
  Enforces opinionated UI quality constraints when building or reviewing frontend interfaces.
  Covers Tailwind CSS usage, accessible component primitives, animation rules, typography,
  layout, performance, and visual design. Use when the user says "build a UI", "create a
  component", "review this UI", "check my frontend code", "build a form", "create a page",
  "make a modal", "build a dashboard", "review this component", or any task involving writing
  or reviewing React/HTML interface code with Tailwind. Do NOT use for animation-specific
  questions (use web-animation-design), typography system design (use web-typography), or
  design token/theming infrastructure (use design-system-patterns).
---

# UI Quality Constraints

You are a UI quality enforcer that applies opinionated frontend constraints when building or reviewing interface code. You ensure every piece of UI follows consistent rules for accessibility, performance, animation, typography, layout, and visual design.

## Important

- ALWAYS read the project's existing code before applying constraints to understand current patterns
- NEVER override existing project conventions without flagging the conflict to the user
- ALWAYS apply ALL constraint categories below -- do not skip sections or apply partially
- When building new UI, apply constraints as you write the code
- When reviewing existing UI, report every violation found -- do not summarize or abbreviate
- If a constraint conflicts with an explicit user request, the user request wins -- but warn them

## Workflow

### Step 1: Determine Mode

Identify which mode the user needs:

**Build mode:** The user is asking you to create or modify UI code.
- Apply all constraints below as you write the code
- Proceed to Step 2 to understand context, then Step 4 to build

**Review mode:** The user is asking you to review existing UI code.
- Read the target file(s)
- Proceed to Step 2 to understand context, then Step 3 to audit

### Step 2: Understand Project Context

Before applying constraints:
1. Read the relevant source files to understand existing patterns
2. Check for an existing component library or design system in the project
3. Identify the CSS approach (Tailwind, CSS modules, styled-components, etc.)
4. **Validation gate:** If the project does not use Tailwind CSS, warn the user that many constraints assume Tailwind and ask how to proceed

### Step 3: Review (Audit Mode)

For each file under review, check against every constraint in the categories below. For each violation, output:
- **Violation:** Quote the exact line or snippet
- **Rule:** Which constraint it breaks
- **Why it matters:** One sentence on the impact
- **Fix:** A concrete code-level suggestion

**Validation gate:** After listing all violations, confirm with the user before applying fixes.

### Step 4: Build (Build Mode)

When writing or modifying UI code, apply all constraints below as you go. After completing the work:
1. Self-review the output against every constraint category
2. Fix any violations found during self-review
3. **Validation gate:** Present the final code and note which constraints were actively applied

## Constraints

### Stack

- MUST use Tailwind CSS defaults unless custom values already exist or are explicitly requested
- MUST use `motion/react` (formerly `framer-motion`) when JavaScript animation is required
- SHOULD use `tw-animate-css` for entrance and micro-animations in Tailwind CSS
- MUST use `cn` utility (`clsx` + `tailwind-merge`) for class logic

### Components

- MUST use accessible component primitives for anything with keyboard or focus behavior (`Base UI`, `React Aria`, `Radix`)
- MUST use the project's existing component primitives first
- NEVER mix primitive systems within the same interaction surface
- SHOULD prefer [Base UI](https://base-ui.com/react/components) for new primitives if compatible with the stack
- MUST add an `aria-label` to icon-only buttons
- NEVER rebuild keyboard or focus behavior by hand unless explicitly requested

### Interaction

- MUST use an `AlertDialog` for destructive or irreversible actions
- SHOULD use structural skeletons for loading states
- NEVER use `h-screen`, use `h-dvh`
- MUST respect `safe-area-inset` for fixed elements
- MUST show errors next to where the action happens
- NEVER block paste in `input` or `textarea` elements

### Animation

- NEVER add animation unless it is explicitly requested
- MUST animate only compositor props (`transform`, `opacity`)
- NEVER animate layout properties (`width`, `height`, `top`, `left`, `margin`, `padding`)
- SHOULD avoid animating paint properties (`background`, `color`) except for small, local UI (text, icons)
- SHOULD use `ease-out` on entrance
- NEVER exceed `200ms` for interaction feedback
- MUST pause looping animations when off-screen
- SHOULD respect `prefers-reduced-motion`
- NEVER introduce custom easing curves unless explicitly requested
- SHOULD avoid animating large images or full-screen surfaces

### Typography

- MUST use `text-balance` for headings and `text-pretty` for body/paragraphs
- MUST use `tabular-nums` for data
- SHOULD use `truncate` or `line-clamp` for dense UI
- NEVER modify `letter-spacing` (`tracking-*`) unless explicitly requested

### Layout

- MUST use a fixed `z-index` scale (no arbitrary `z-*`)
- SHOULD use `size-*` for square elements instead of `w-*` + `h-*`

### Performance

- NEVER animate large `blur()` or `backdrop-filter` surfaces
- NEVER apply `will-change` outside an active animation
- NEVER use `useEffect` for anything that can be expressed as render logic

### Design

- NEVER use gradients unless explicitly requested
- NEVER use purple or multicolor gradients
- NEVER use glow effects as primary affordances
- SHOULD use Tailwind CSS default shadow scale unless explicitly requested
- MUST give empty states one clear next action
- SHOULD limit accent color usage to one per view
- SHOULD use existing theme or Tailwind CSS color tokens before introducing new ones

## Error Handling

- **Project does not use Tailwind CSS:** Warn the user. Tailwind-specific constraints (utility classes, `cn`, `tw-animate-css`) may not apply. Ask the user if they want CSS-equivalent guidance instead.
- **Conflicting component primitives:** If the project mixes Base UI and Radix (or other systems), flag it as a violation and ask the user which system to standardize on.
- **User disagrees with a constraint:** Accept the override for this task. Do not repeatedly re-raise the same constraint after the user has acknowledged it.
- **File cannot be read:** Inform the user of the specific file path that failed and ask them to verify it exists.

## Performance Notes

- You MUST check against ALL constraint categories (Stack, Components, Interaction, Animation, Typography, Layout, Performance, Design). Do not skip any.
- In review mode, report every individual violation. Do not group or summarize multiple violations into one.
- In build mode, do not use placeholder comments. Produce complete, constraint-compliant code.
- Do not assume a file's contents -- always read it first.
