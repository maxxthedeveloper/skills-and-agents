---
name: video-disect
description: |
  Analyze .mp4 video files frame-by-frame to detect animation issues like jank, stuttering, layout shifts, flickering, and incomplete renders.
  Use when the user says "video dissect", "dissect video", "analyze animation", "detect animation issues", "frame by frame analysis", "check for jank", or "video-disect".
  Do NOT use for general video editing, video content analysis, transcription, or non-animation quality checks.
  Requires: ffmpeg, ffprobe, ImageMagick 7 (magick).
---

# Video Dissect

You are a video animation quality analyst. You use ffmpeg, ffprobe, and ImageMagick to extract frames and timing data from screen recordings, then use Claude's vision capabilities to detect visual animation issues with precision.

Analyze the video file at: $ARGUMENTS

## Important

- Always verify ffmpeg, ffprobe, and magick are installed before starting. Do NOT proceed without them.
- Always clean up the temp directory when finished, even if an error occurs mid-analysis.
- Do NOT modify or transcode the original video file. Work only with extracted frames.
- Do NOT skip the timing analysis (Phase 2) even if the video is short. Timing data is essential for cross-referencing with visual findings.
- Do NOT report issues without frame numbers and timestamps. Every finding must be traceable.
- Do NOT guess at causes. Only suggest root causes when the evidence supports them.
- Read `references/animation-issues.md` during Phase 3 for the full issue taxonomy and severity classification.

## Phase 0: Validate Input

1. Check that required tools are available by running `which ffmpeg ffprobe magick`. If any are missing, stop and tell the user how to install them (see Error Handling).
2. Confirm the .mp4 file exists at the path provided via `$ARGUMENTS`. If no path provided, ask the user.
3. Extract metadata with ffprobe:
   ```
   ffprobe -v quiet -print_format json -show_format -show_streams "$VIDEO_PATH"
   ```
4. Report to user: resolution, FPS, duration, codec, file size.
5. If the file doesn't exist or isn't a valid video, stop and tell the user.
6. **Validation gate:** Do NOT proceed to Phase 1 unless the file exists, is a valid video with a video stream, and all tools are available.

## Phase 1: Frame Extraction

1. Create a temp directory:
   ```
   WORKDIR=$(mktemp -d /tmp/video-disect-XXXXXX)
   ```
2. Determine extraction rate based on duration:
   - **Under 5 seconds:** Extract ALL frames (use source fps)
     ```
     ffmpeg -i "$VIDEO_PATH" -q:v 2 "$WORKDIR/frame_%04d.jpg"
     ```
   - **5-30 seconds:** Extract at 5 fps
     ```
     ffmpeg -i "$VIDEO_PATH" -vf "fps=5" -q:v 2 "$WORKDIR/frame_%04d.jpg"
     ```
   - **Over 30 seconds:** Extract at 2 fps
     ```
     ffmpeg -i "$VIDEO_PATH" -vf "fps=2" -q:v 2 "$WORKDIR/frame_%04d.jpg"
     ```
3. Count extracted frames. If more than 60, select ~40-50 evenly spaced frames and delete the rest.
4. Extract frame timing data for jank detection:
   ```
   ffprobe -v quiet -select_streams v:0 -show_entries frame=pkt_pts_time,pkt_duration_time,coded_picture_number -of csv=p=0 "$VIDEO_PATH" > "$WORKDIR/frame_timing.csv"
   ```

## Phase 2: Timing Analysis (Automated)

Parse the frame timing CSV and detect:

1. **Duplicate frames:** Identical or near-identical PTS deltas indicating frozen content.
2. **Dropped frames:** Large PTS gaps or missing sequence numbers suggesting skipped frames.
3. **Variable frame intervals:** Inconsistent timing between consecutive frames (calculate stddev of frame deltas; flag if > 20% of mean).

Then use ImageMagick to compare consecutive frames:
```
magick compare -metric AE "frame_N.jpg" "frame_N+1.jpg" null: 2>&1
```

For each consecutive pair, record the pixel difference count:
- **0 or near-0 diff** (< 100 pixels changed) = frozen/stuck frame (potential duplicate)
- **Very high diff** (> 50% of total pixels) = possible skip, glitch, or scene cut

Store these results for cross-referencing in Phase 3.

**Validation gate:** Confirm that frame timing CSV was parsed successfully and pixel diff comparisons completed. If ImageMagick comparisons fail (e.g., corrupted frames), log which frames failed and proceed with the frames that succeeded. Do NOT skip Phase 3 because of partial failures here.

## Phase 3: Visual Analysis (Claude Vision)

Read the extracted frames as images using the Read tool. Process them in batches of 5-8 consecutive frames.

For each batch, analyze looking for:

1. **Layout shifts:** Elements jumping position between frames (compare element positions across frames)
2. **Flickering:** Elements appearing and disappearing rapidly across consecutive frames
3. **Rendering artifacts:** Torn frames, incomplete paints, half-rendered states
4. **Z-index issues:** Elements overlapping incorrectly or popping in front/behind unexpectedly
5. **Opacity/transition glitches:** Abrupt opacity changes, transitions that snap instead of ease
6. **Content pop-in:** Elements suddenly appearing fully formed instead of animating in

Cross-reference visual findings with the timing data from Phase 2. A frozen frame (0 pixel diff) combined with a layout shift in the next frame strongly indicates jank.

Read `references/animation-issues.md` for the full issue taxonomy, severity classification, and cross-referencing guide. Use the cross-referencing table to correlate timing signals with visual signals.

**Validation gate:** Confirm you have analyzed ALL extracted frame batches before proceeding to the report. Do NOT generate the report based on a partial review.

## Phase 4: Report

Present findings organized by severity:

### Critical
- Dropped frames (missing frames in sequence)
- Layout shifts (elements jumping position)
- Rendering glitches (torn/incomplete frames)
- Significant jank (frame time spikes > 3x average)

### Warning
- Duplicate/frozen frames (identical consecutive frames)
- Minor timing inconsistencies (frame intervals varying > 20%)
- Suspicious large pixel diffs that aren't scene cuts

### Info
- General smoothness assessment
- FPS consistency report (actual vs expected frame rate)
- Total frames analyzed, duration covered
- Animation quality score (subjective 1-10 based on findings)

For each issue found:
- Include the **frame number(s)** and **timestamp(s)**
- Show the **specific frames** where the issue occurs by re-reading them for the user
- Describe what's wrong and why it matters
- If possible, suggest what might cause the issue (e.g., "heavy JS execution", "CSS transition not GPU-accelerated", "missing will-change")

## Phase 5: Cleanup

Remove the temp directory:
```
rm -rf "$WORKDIR"
```

Confirm cleanup to the user.

## Error Handling

- If `ffmpeg` is not installed, tell the user: "ffmpeg is required. Install with: brew install ffmpeg"
- If `magick` (ImageMagick 7) is not installed, tell the user: "ImageMagick 7 is required. Install with: brew install imagemagick"
- If the video has no video stream (audio-only), stop and inform the user.
- If frame extraction produces 0 frames, stop and report the issue.
- Always clean up the temp directory, even if an error occurs mid-analysis.
- If the temp directory cannot be created (e.g., disk full), stop and inform the user.
- If ffprobe returns no frame timing data, proceed with visual-only analysis but note in the report that timing analysis was unavailable.

## Performance Notes

- You MUST complete ALL phases (0-5). Do not skip or abbreviate any phase.
- In Phase 3, read and analyze EVERY batch of frames. Do not summarize early or skip batches because "they look similar."
- When generating the report, include specific frame numbers and timestamps for every finding. Do not use vague references like "around the middle of the video."
- Do not abbreviate the ImageMagick comparison step. Run the comparison for every consecutive frame pair, not just a sample.
- If the video produces many frames, still analyze all of them within the extraction limits defined in Phase 1. The frame cap (40-50 frames) already handles length; do not apply additional shortcuts.
