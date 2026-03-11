---
name: add-work-tile
description: >-
  Add new tiles, images, and videos to the portfolio work page grid. Use when
  the user says "add a tile", "add an image", "add a video", "new work item",
  "add this to the grid", "wire up this image", "wire up this video", "add work
  tile", or drops new assets into public/work/. ALWAYS asks the user for layout
  type, naming, hover state, and grid position before making changes. Handles
  both image-only and video tiles with poster extraction and format optimization.
  Do NOT use for modifying existing tiles, changing the grid system itself, or
  editing the Tile component.
compatibility: >-
  Requires Node.js and sharp (for image optimization scripts). Video tiles
  require ffmpeg for poster extraction and WebM encoding.
---

# Add Work Tile

You are a design-aware assistant specialized in adding new tiles to the portfolio work page. You understand the 5-layout tile system, aspect ratios, video pipeline, and presentation conventions. You NEVER assume — you always ask.

## Important

- ALWAYS ask the user for clarification before editing any files. Never guess layout type, naming, or position.
- Read `app/work/data.ts` first to understand the current grid state and next available ID.
- Read `references/layout-system.md` when you need to check the WorkItem interface, layout specs, asset naming conventions, or video tile requirements.
- Images go in `public/work/`. Reference them as `/work/filename.ext` in `imageSrc`.
- Video tiles require BOTH `imageSrc` (poster) and `videoSrc` (.mp4 path). Never add a video tile without a poster image.
- Keep `<img>` tags (not `next/image`) — tiles use clip-path which conflicts with Next.js image optimization.
- Never set `hoverBarTheme` on contained layouts (`desktop-contained`, `mobile-contained`) — the hover bar sits on the outer background where default dark text is always correct.

## Workflow

### Step 1: Discover assets

1. Read `app/work/data.ts` to understand the current grid state, next available ID, and which assets are already wired up.
2. Glob `public/work/` to list all images and videos on disk.
3. Compare the two lists to identify new/unwired assets.

If the user mentions a specific file, locate it. If no new assets are found, ask the user where the asset is.

### Step 2: Ask for tile details

For EACH new tile, ask the user ALL of the following. Present them as a numbered list — do not skip any:

1. **Layout type** — show this quick reference:
   - `desktop-contained` — 3:2 outer, 16:10 inner mockup, spans 2 cols (desktop screenshots)
   - `desktop-full` — 3:2 outer, full-bleed, spans 2 cols (wide images)
   - `mobile-contained` — 2:3 outer, 9:19.5 inner mockup, spans 1 col (phone screenshots)
   - `portrait-full` — 2:3 outer, full-bleed, spans 1 col (tall images)
   - `component` — 1:1 outer, full-bleed, spans 1 col (square UI/component showcases)

2. **Project name** — display name for the hover bar. Empty string `""` = no hover state.

3. **Project type** — subtitle tag like "Waitlist Page", "Design System", "UI Kit" (or skip)

4. **Hover bar theme** — only ask for full-bleed layouts (`desktop-full`, `portrait-full`, `component`):
   - `"light"` — white text, for dark images
   - `"dark"` — black text, for light images
   - Skip this question entirely for contained layouts — default is always correct.

5. **Video** — is this a video tile? Check if the discovered asset from Step 1 is an `.mp4` and pre-fill this answer. If yes, the user must have a `.mp4` in `public/work/`. A poster image is also required (user-provided or extracted from the video in Step 4).

6. **Inner border radius** — only ask for contained layouts if the default 20px doesn't match the content (e.g., macOS windows use ~10px, iOS screens use ~38px). Skip for full-bleed layouts.

7. **Built with** — collaborator credit? If yes, ask for name, URL, and optional label (defaults to "Built by").

8. **Grid position** — show the current grid order so the user can pick where to insert.

Wait for the user to answer ALL questions before proceeding.

### Step 3: Confirm the tile config

Before editing any files, present a summary back to the user:

```
Tile summary:
- Image: /work/filename.jpg
- Video: /work/filename.mp4 (if applicable)
- Layout: desktop-contained (3:2 outer, 16:10 inner, 2 cols)
- Project: "Grids" / "Builder"
- Hover bar theme: (default / light / dark)
- Position: after item 3
```

Ask: "Does this look right?" Only proceed after explicit confirmation.

### Step 4: Process assets

#### Image-only tiles:

Run the optimization pipeline for any new image in `public/work/`:

```bash
node scripts/optimize-images.mjs   # generates .avif and .webp variants
node scripts/generate-lqip.mjs     # regenerates app/work/blur-data.ts
```

#### Video tiles:

Video tiles need BOTH `imageSrc` (poster) and `videoSrc`. If the user doesn't provide a poster image:

1. **Extract a poster frame** via ffmpeg (skip 0.5s to avoid fade-in frames):
   ```bash
   ffmpeg -ss 0.5 -i public/work/video-name.mp4 -frames:v 1 -q:v 2 "public/work/video-name-poster.jpg"
   ```

2. **Generate a WebM variant** for smaller file size:
   ```bash
   ffmpeg -i public/work/video-name.mp4 -c:v libvpx-vp9 -crf 35 -b:v 0 -an public/work/video-name.webm
   ```
   VP9 encoding is CPU-intensive. Run in background for large files (>5MB).

3. **Run the image optimization pipeline** for the poster:
   ```bash
   node scripts/optimize-images.mjs   # generates .avif and .webp for poster
   node scripts/generate-lqip.mjs     # regenerates blur-data.ts
   ```

**Validation gate:** After processing, verify all required files exist using Glob:
- For image tiles: `.jpg` (or `.png`) + `.avif` + `.webp`
- For video tiles: `.mp4` + `.webm` + poster `.jpg` + poster `.avif` + poster `.webp`

If any file is missing, diagnose and fix before proceeding.

### Step 5: Edit data.ts

1. Read `app/work/data.ts` (re-read it — do not rely on what you read in Step 1)
2. Add the new WorkItem at the confirmed position in the `workItems` array
3. For video tiles, set BOTH `imageSrc` (poster path) and `videoSrc` (video path)
4. Re-number all `id` fields sequentially ("1", "2", "3"...)
5. Verify no duplicate IDs exist

### Step 6: Verify

Read the updated `app/work/data.ts` back and confirm ALL of the following:
- The new item is at the correct position
- All IDs are sequential with no gaps or duplicates
- `imageSrc` path matches an actual file in `public/work/`
- If video tile: `videoSrc` path matches an actual `.mp4` in `public/work/`
- If video tile: `.webm` variant exists alongside the `.mp4`
- Optimized image variants exist (`.avif` + `.webp` alongside the source image)
- Layout type is one of the 5 valid values
- `hoverBarTheme` is NOT set on contained layouts

Present the final grid order to the user.

## Error Handling

- **Image not found in `public/work/`:** Ask the user to confirm the file path. Check for typos and spaces in filenames (spaces in filenames are valid in this project).
- **Unknown layout type:** Show the 5 valid options and ask again.
- **User unsure about layout:** Ask what the image looks like (desktop screenshot? phone screen? square component? wide photo?) and suggest the best fit based on the content.
- **Duplicate image:** Warn the user if the image is already referenced in an existing work item.
- **ffmpeg not found:** Tell the user to install ffmpeg (`brew install ffmpeg` on macOS).
- **WebM encoding too slow:** For files >20MB, suggest running the ffmpeg command in background and proceeding with the data.ts edit while it encodes.
- **Optimization script fails:** Check that `sharp` is installed (`npm ls sharp`). If missing, run `npm install`.

## Performance Notes

- You MUST ask all questions in Step 2 before making any edits. Do not skip the confirmation step.
- Always re-read `data.ts` before editing to avoid stale state.
- When adding multiple tiles at once, gather info for all tiles first, then make all edits together.
- Do not skip the validation gate in Step 4 — actually verify the files exist.
- Do not skip Step 6 verification — actually read the file back and check each item.
