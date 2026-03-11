# Animation Issue Taxonomy & Detection Guide

## Issue Types

### 1. Jank (Frame Time Spikes)

**What it is:** Individual frames that take significantly longer to render than the target frame budget, causing visible stuttering.

**Detection methods:**
- **Timing analysis:** Frame duration > 2x the average frame duration (e.g., > 33ms at 60fps when average is ~16.7ms)
- **Pixel diff:** Normal pixel diff preceded or followed by a large pixel diff (indicates catch-up frame)
- **Visual:** Motion that appears to "jump" rather than flow smoothly

**Severity:** Critical if > 3x average frame time. Warning if 2-3x.

**Common causes:** Heavy JavaScript execution, forced synchronous layouts, paint storms, garbage collection pauses.

---

### 2. Layout Shifts (CLS)

**What it is:** Elements changing position abruptly without animation, causing the page to "jump."

**Detection methods:**
- **Visual comparison:** Look for UI elements (text, buttons, images) that are in different positions between consecutive frames without a smooth transition path
- **Pixel diff pattern:** Moderate-to-high pixel diff concentrated in specific regions rather than distributed evenly
- **Key indicator:** An element is at position A in frame N, absent or partially visible in frame N+1, and at position B in frame N+2

**Severity:** Always Critical. Layout shifts are one of the most jarring animation issues.

**Common causes:** Late-loading content (images without dimensions, async content insertion), font swaps (FOUT/FOIT), dynamic content injection above the viewport.

---

### 3. Flickering

**What it is:** Elements rapidly appearing and disappearing across consecutive frames.

**Detection methods:**
- **Pixel diff oscillation:** Frame pairs showing alternating high/low pixel diffs in the same region
- **Visual:** An element visible in frame N, gone in frame N+1, visible again in frame N+2
- **Pattern:** Look for a "blink" pattern: present -> absent -> present within 3-5 frames

**Severity:** Critical if affects primary content. Warning if subtle (e.g., a border flickering).

**Common causes:** Conflicting CSS transitions, React re-renders toggling visibility, z-index battles, GPU compositing layer issues, conditional rendering based on rapidly-changing state.

---

### 4. Dropped Frames

**What it is:** Frames that should exist in the sequence but are missing entirely.

**Detection methods:**
- **Timing analysis:** PTS gaps larger than 2x the expected frame interval
- **Sequence analysis:** Missing coded_picture_numbers in the frame data
- **Pixel diff:** Unusually large pixel diff between "consecutive" frames (because intermediate frames are missing)

**Severity:** Critical if multiple consecutive frames are dropped. Warning if isolated single drops.

**Common causes:** Encoder issues, screen recording software overload, system resource contention during capture, heavy GPU load.

---

### 5. Duplicate/Frozen Frames

**What it is:** Consecutive frames that are identical, indicating the animation stalled.

**Detection methods:**
- **Pixel diff:** 0 or near-0 pixel difference (< 100 changed pixels) between consecutive frames
- **Timing analysis:** Frame present in sequence but content unchanged
- **Duration:** Count consecutive frozen frames to measure stall duration

**Severity:** Warning if 2-3 consecutive duplicates. Critical if > 5 consecutive duplicates (visible freeze).

**Common causes:** Main thread blocking (long tasks), requestAnimationFrame not firing, tab backgrounded during recording, animation paused state.

---

### 6. Rendering Artifacts

**What it is:** Visual glitches from incomplete or corrupted frame rendering.

**Detection methods:**
- **Visual:** Look for:
  - Horizontal/vertical lines cutting through the frame (tearing)
  - Partially rendered elements (half-painted)
  - Color corruption or blocks of wrong colors
  - Ghosting (previous frame content bleeding through)
- **Pixel diff:** Unusual patterns - very high diff in a horizontal band (tearing) or checkerboard pattern (GPU issues)

**Severity:** Always Critical.

**Common causes:** Missing vsync, GPU driver issues, compositor bugs, CSS transform rendering bugs, will-change misuse causing layer explosion.

---

### 7. Transition/Animation Glitches

**What it is:** CSS transitions or JS animations that don't execute smoothly.

**Detection methods:**
- **Visual:** Look for:
  - Elements snapping to final position instead of animating
  - Animations that start mid-way (missing first frames)
  - Easing that looks wrong (linear when it should ease, or vice versa)
  - Animations that overshoot and snap back
- **Timing pattern:** Very short animation duration (1-2 frames) when a smooth transition is expected

**Severity:** Warning for minor easing issues. Critical for snap/teleport behavior.

**Common causes:** Transition property not set, animating non-compositable properties (top/left instead of transform), forced layout during animation, animation cancelled and restarted.

---

## Severity Classification Guide

| Severity | Criteria | User Impact |
|----------|----------|-------------|
| **Critical** | Clearly visible to users, disrupts experience | Layout shifts, dropped frames (3+), rendering artifacts, severe jank (>50ms frames) |
| **Warning** | Noticeable on close inspection | Duplicate frames (2-3), minor timing variance, subtle flickering |
| **Info** | Technical note, not user-visible | Single frame timing outlier, expected scene transitions, minor FPS variation |

## Cross-Referencing Signals

The strongest issue detection comes from correlating multiple signals:

| Timing Signal | Visual Signal | Likely Issue |
|---------------|--------------|--------------|
| Large PTS gap | Big pixel diff | Dropped frames |
| Zero PTS delta | Zero pixel diff | Frozen/duplicate frame |
| Spike in frame time | Layout elements moved | Jank + layout shift |
| Normal timing | Oscillating pixel diff | Flickering |
| Normal timing | Moderate diff in bands | Tearing/artifact |
| Very short transition | Element teleported | Broken animation |
