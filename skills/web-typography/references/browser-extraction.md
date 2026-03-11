# Browser Typography Extraction

JavaScript snippets for extracting computed typography from a live page via `mcp__claude-in-chrome__javascript_tool`.

## Primary Extraction Script

Execute this via `mcp__claude-in-chrome__javascript_tool` to capture all typography data from the current page:

```javascript
(() => {
  const textElements = document.querySelectorAll(
    'h1, h2, h3, h4, h5, h6, p, span, a, li, td, th, label, button, ' +
    'input, textarea, blockquote, figcaption, cite, code, pre, ' +
    'small, strong, em, dt, dd, summary, legend, caption, ' +
    '[class*="text"], [class*="title"], [class*="heading"], ' +
    '[class*="body"], [class*="caption"], [class*="label"]'
  );

  const seen = new Set();
  const results = [];

  textElements.forEach(el => {
    const text = el.textContent?.trim();
    if (!text || text.length === 0) return;

    const style = window.getComputedStyle(el);
    const fontSize = style.fontSize;
    const lineHeight = style.lineHeight;
    const fontWeight = style.fontWeight;
    const fontFamily = style.fontFamily;
    const letterSpacing = style.letterSpacing;
    const color = style.color;
    const bgColor = style.backgroundColor;
    const textTransform = style.textTransform;
    const textWrap = style.textWrap || 'none';
    const maxWidth = style.maxWidth;
    const fontVariantNumeric = style.fontVariantNumeric;

    // Fingerprint for dedup
    const fp = `${el.tagName}|${fontSize}|${lineHeight}|${fontWeight}|${fontFamily}|${letterSpacing}|${color}|${textTransform}`;
    if (seen.has(fp)) return;
    seen.add(fp);

    // Calculate line-height ratio
    const fontSizePx = parseFloat(fontSize);
    const lineHeightPx = lineHeight === 'normal' ? fontSizePx * 1.2 : parseFloat(lineHeight);
    const lineHeightRatio = (lineHeightPx / fontSizePx).toFixed(3);

    // Get container width for measure calculation
    const container = el.closest('article, section, main, [class*="content"], [class*="prose"]') || el.parentElement;
    const containerWidth = container ? parseFloat(window.getComputedStyle(container).width) : null;

    // Approximate characters per line (rough, assumes average char width ~ 0.5em)
    const approxCharsPerLine = containerWidth ? Math.round(containerWidth / (fontSizePx * 0.5)) : null;

    // Get classes for source mapping
    const classes = el.className && typeof el.className === 'string'
      ? el.className.split(/\s+/).filter(c => c).slice(0, 5).join(' ')
      : '';

    results.push({
      tag: el.tagName.toLowerCase(),
      classes,
      fontSize,
      fontSizePx: fontSizePx,
      lineHeight,
      lineHeightRatio: parseFloat(lineHeightRatio),
      fontWeight,
      fontFamily: fontFamily.split(',')[0].replace(/['"]/g, '').trim(),
      fontFamilyFull: fontFamily,
      letterSpacing,
      color,
      bgColor,
      textTransform,
      textWrap,
      maxWidth,
      fontVariantNumeric,
      containerWidthPx: containerWidth ? Math.round(containerWidth) : null,
      approxCharsPerLine,
      sampleText: text.substring(0, 60) + (text.length > 60 ? '...' : '')
    });
  });

  // Sort by font size descending
  results.sort((a, b) => b.fontSizePx - a.fontSizePx);

  return JSON.stringify(results, null, 2);
})()
```

## Font Loading Check

Execute this to see which fonts are actually loaded on the page:

```javascript
(() => {
  const fonts = [];
  document.fonts.forEach(font => {
    fonts.push({
      family: font.family,
      weight: font.weight,
      style: font.style,
      status: font.status,
      unicodeRange: font.unicodeRange
    });
  });

  // Group by family
  const grouped = {};
  fonts.forEach(f => {
    const key = f.family.replace(/['"]/g, '');
    if (!grouped[key]) grouped[key] = [];
    grouped[key].push({ weight: f.weight, style: f.style, status: f.status });
  });

  return JSON.stringify(grouped, null, 2);
})()
```

## Contrast Check

Execute this to check contrast ratios for all text elements:

```javascript
(() => {
  function luminance(r, g, b) {
    const a = [r, g, b].map(v => {
      v /= 255;
      return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
    });
    return 0.2126 * a[0] + 0.7152 * a[1] + 0.0722 * a[2];
  }

  function parseColor(color) {
    const m = color.match(/rgba?\((\d+),\s*(\d+),\s*(\d+)/);
    return m ? [parseInt(m[1]), parseInt(m[2]), parseInt(m[3])] : null;
  }

  function contrastRatio(fg, bg) {
    const l1 = luminance(...fg);
    const l2 = luminance(...bg);
    const lighter = Math.max(l1, l2);
    const darker = Math.min(l1, l2);
    return ((lighter + 0.05) / (darker + 0.05)).toFixed(2);
  }

  function getEffectiveBg(el) {
    let current = el;
    while (current) {
      const bg = window.getComputedStyle(current).backgroundColor;
      const parsed = parseColor(bg);
      if (parsed && !(parsed[0] === 0 && parsed[1] === 0 && parsed[2] === 0 && bg.includes('0)'))) {
        return parsed;
      }
      current = current.parentElement;
    }
    return [255, 255, 255]; // default white
  }

  const elements = document.querySelectorAll('h1,h2,h3,h4,h5,h6,p,span,a,li,label,button,td,th');
  const seen = new Set();
  const failures = [];

  elements.forEach(el => {
    const text = el.textContent?.trim();
    if (!text) return;

    const style = window.getComputedStyle(el);
    const fg = parseColor(style.color);
    if (!fg) return;

    const bg = getEffectiveBg(el);
    const ratio = parseFloat(contrastRatio(fg, bg));
    const fontSize = parseFloat(style.fontSize);
    const isLarge = fontSize >= 24 || (fontSize >= 18.66 && parseInt(style.fontWeight) >= 700);
    const required = isLarge ? 3 : 4.5;

    const fp = `${style.color}|${bg.join(',')}|${fontSize}`;
    if (seen.has(fp)) return;
    seen.add(fp);

    if (ratio < required) {
      failures.push({
        tag: el.tagName.toLowerCase(),
        text: text.substring(0, 40),
        color: style.color,
        bgColor: `rgb(${bg.join(',')})`,
        ratio,
        required,
        fontSize: style.fontSize,
        isLargeText: isLarge,
        classes: typeof el.className === 'string' ? el.className.split(/\s+/).slice(0, 3).join(' ') : ''
      });
    }
  });

  return JSON.stringify({
    totalFailures: failures.length,
    failures: failures.sort((a, b) => a.ratio - b.ratio)
  }, null, 2);
})()
```

## Heading Hierarchy Check

Execute to verify heading level usage:

```javascript
(() => {
  const headings = document.querySelectorAll('h1, h2, h3, h4, h5, h6');
  const result = [];
  let prevLevel = 0;
  const issues = [];

  headings.forEach(h => {
    const level = parseInt(h.tagName[1]);
    const style = window.getComputedStyle(h);

    if (prevLevel > 0 && level > prevLevel + 1) {
      issues.push(`Skipped from h${prevLevel} to h${level}`);
    }

    result.push({
      tag: h.tagName.toLowerCase(),
      level,
      fontSize: style.fontSize,
      fontWeight: style.fontWeight,
      lineHeight: style.lineHeight,
      letterSpacing: style.letterSpacing,
      text: h.textContent?.trim().substring(0, 50)
    });

    prevLevel = level;
  });

  // Check for size ratio between adjacent levels
  for (let i = 0; i < result.length - 1; i++) {
    const current = result[i];
    const next = result[i + 1];
    if (next.level === current.level + 1) {
      const ratio = parseFloat(current.fontSize) / parseFloat(next.fontSize);
      if (ratio < 1.2) {
        issues.push(`h${current.level} (${current.fontSize}) to h${next.level} (${next.fontSize}) ratio: ${ratio.toFixed(2)} (< 1.2)`);
      }
    }
  }

  return JSON.stringify({ headings: result, issues }, null, 2);
})()
```

## Vertical Spacing Extraction

Execute this to capture spacing relationships between adjacent text elements and heading spacing asymmetry:

```javascript
(() => {
  const selectors = 'h1,h2,h3,h4,h5,h6,p,li,blockquote,figcaption,dt,dd,label,legend,summary,[class*="text"],[class*="title"],[class*="heading"],[class*="body"],[class*="caption"]';
  const elements = Array.from(document.querySelectorAll(selectors)).filter(el => {
    const r = el.getBoundingClientRect();
    const s = window.getComputedStyle(el);
    return r.height > 0 && r.width > 0 && s.display !== 'none' && s.visibility !== 'hidden' && el.textContent.trim().length > 0;
  });

  // Sort by vertical position
  elements.sort((a, b) => a.getBoundingClientRect().top - b.getBoundingClientRect().top);

  // Adjacent pairs with vertical gaps
  const pairs = [];
  for (let i = 0; i < elements.length - 1; i++) {
    const a = elements[i];
    const b = elements[i + 1];
    const rectA = a.getBoundingClientRect();
    const rectB = b.getBoundingClientRect();
    const gap = rectB.top - rectA.bottom;
    if (gap >= 0 && gap < 200) {
      pairs.push({
        elementA: { tag: a.tagName.toLowerCase(), text: a.textContent.trim().substring(0, 40) },
        elementB: { tag: b.tagName.toLowerCase(), text: b.textContent.trim().substring(0, 40) },
        gapPx: Math.round(gap)
      });
    }
  }

  // Heading spacing: margin-top vs margin-bottom ratio
  const headingSpacing = [];
  document.querySelectorAll('h1,h2,h3,h4,h5,h6').forEach(h => {
    const s = window.getComputedStyle(h);
    const mt = parseFloat(s.marginTop) || 0;
    const mb = parseFloat(s.marginBottom) || 0;
    headingSpacing.push({
      tag: h.tagName.toLowerCase(),
      text: h.textContent.trim().substring(0, 40),
      marginTop: Math.round(mt),
      marginBottom: Math.round(mb),
      ratio: mb > 0 ? parseFloat((mt / mb).toFixed(2)) : mt > 0 ? Infinity : 1
    });
  });

  // Detect rhythm base (most common gap)
  const gapCounts = {};
  pairs.forEach(p => {
    const rounded = Math.round(p.gapPx / 4) * 4;
    gapCounts[rounded] = (gapCounts[rounded] || 0) + 1;
  });
  const rhythmBase = Object.entries(gapCounts).sort((a, b) => b[1] - a[1])[0];

  return JSON.stringify({
    pairs: pairs.slice(0, 40),
    headingSpacing,
    rhythmBase: rhythmBase ? parseInt(rhythmBase[0]) : null,
    totalPairs: pairs.length
  }, null, 2);
})()
```

## Color Hierarchy Extraction

Execute this to analyze text color distribution and detect hierarchy contradictions:

```javascript
(() => {
  function relativeLuminance(r, g, b) {
    const a = [r, g, b].map(v => {
      v /= 255;
      return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
    });
    return 0.2126 * a[0] + 0.7152 * a[1] + 0.0722 * a[2];
  }

  function parseRGB(color) {
    const m = color.match(/rgba?\((\d+),\s*(\d+),\s*(\d+)/);
    return m ? [parseInt(m[1]), parseInt(m[2]), parseInt(m[3])] : null;
  }

  const selectors = 'h1,h2,h3,h4,h5,h6,p,span,a,li,label,button,td,th,blockquote,figcaption,small,dt,dd,summary';
  const elements = document.querySelectorAll(selectors);
  const colorMap = {};

  elements.forEach(el => {
    const text = el.textContent?.trim();
    if (!text || text.length === 0) return;
    const s = window.getComputedStyle(el);
    if (s.display === 'none' || s.visibility === 'hidden') return;
    const color = s.color;
    const rgb = parseRGB(color);
    if (!rgb) return;
    const lum = relativeLuminance(...rgb);

    if (!colorMap[color]) {
      colorMap[color] = { color, rgb, luminance: parseFloat(lum.toFixed(4)), elements: [] };
    }
    const tag = el.tagName.toLowerCase();
    if (!colorMap[color].elements.includes(tag)) {
      colorMap[color].elements.push(tag);
    }
  });

  const colors = Object.values(colorMap);

  // Bucket into layers
  const layers = {
    primary: colors.filter(c => c.luminance < 0.15),
    secondary: colors.filter(c => c.luminance >= 0.15 && c.luminance < 0.40),
    tertiary: colors.filter(c => c.luminance >= 0.40 && c.luminance < 0.60),
    faint: colors.filter(c => c.luminance >= 0.60)
  };

  // Detect contradictions: headings lighter than body
  const issues = [];
  const headingTags = ['h1','h2','h3','h4','h5','h6'];
  const bodyTags = ['p','li','blockquote','dd'];
  const headingColors = colors.filter(c => c.elements.some(e => headingTags.includes(e)));
  const bodyColors = colors.filter(c => c.elements.some(e => bodyTags.includes(e)));

  headingColors.forEach(hc => {
    bodyColors.forEach(bc => {
      if (hc.luminance > bc.luminance + 0.05) {
        issues.push({
          type: 'heading-lighter-than-body',
          headingColor: hc.color,
          headingLuminance: hc.luminance,
          bodyColor: bc.color,
          bodyLuminance: bc.luminance,
          detail: `Heading color (lum ${hc.luminance.toFixed(3)}) is lighter than body color (lum ${bc.luminance.toFixed(3)})`
        });
      }
    });
  });

  return JSON.stringify({
    layers: {
      primary: layers.primary.map(c => ({ color: c.color, luminance: c.luminance, usedBy: c.elements })),
      secondary: layers.secondary.map(c => ({ color: c.color, luminance: c.luminance, usedBy: c.elements })),
      tertiary: layers.tertiary.map(c => ({ color: c.color, luminance: c.luminance, usedBy: c.elements })),
      faint: layers.faint.map(c => ({ color: c.color, luminance: c.luminance, usedBy: c.elements }))
    },
    totalUniqueColors: colors.length,
    issues
  }, null, 2);
})()
```

## Visual Weight Map

Execute this to compute a prominence score for each unique text style and run the squint test:

```javascript
(() => {
  function parseRGB(color) {
    const m = color.match(/rgba?\((\d+),\s*(\d+),\s*(\d+)/);
    return m ? [parseInt(m[1]), parseInt(m[2]), parseInt(m[3])] : null;
  }

  function relativeLuminance(r, g, b) {
    const a = [r, g, b].map(v => {
      v /= 255;
      return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
    });
    return 0.2126 * a[0] + 0.7152 * a[1] + 0.0722 * a[2];
  }

  const selectors = 'h1,h2,h3,h4,h5,h6,p,span,a,li,label,button,td,th,blockquote,figcaption,small,dt,dd,summary';
  const elements = document.querySelectorAll(selectors);
  const fingerprints = {};

  elements.forEach(el => {
    const text = el.textContent?.trim();
    if (!text || text.length === 0) return;
    const s = window.getComputedStyle(el);
    if (s.display === 'none' || s.visibility === 'hidden') return;

    const fontSize = parseFloat(s.fontSize);
    const fontWeight = parseInt(s.fontWeight) || 400;
    const color = s.color;
    const rgb = parseRGB(color);
    if (!rgb) return;

    const fp = `${fontSize}|${fontWeight}|${color}`;
    if (!fingerprints[fp]) {
      const lum = relativeLuminance(...rgb);
      // Darkness factor: 0 = white (invisible), 1 = black (maximum contrast)
      const colorDarkness = 1 - lum;
      // Size factor: normalize to 0-1 range (12px=0, 72px=1)
      const sizeFactor = Math.min(Math.max((fontSize - 12) / 60, 0), 1);
      // Weight factor: normalize 100-900 to 0-1
      const weightFactor = Math.min(Math.max((fontWeight - 100) / 800, 0), 1);
      // Prominence = weighted combination
      const prominence = parseFloat((sizeFactor * 0.4 + weightFactor * 0.3 + colorDarkness * 0.3).toFixed(3));

      fingerprints[fp] = {
        fontSize,
        fontWeight,
        color,
        colorDarkness: parseFloat(colorDarkness.toFixed(3)),
        prominence,
        tags: [],
        isHeading: false,
        sampleText: ''
      };
    }

    const tag = el.tagName.toLowerCase();
    if (!fingerprints[fp].tags.includes(tag)) {
      fingerprints[fp].tags.push(tag);
    }
    if (['h1','h2','h3','h4','h5','h6'].includes(tag)) {
      fingerprints[fp].isHeading = true;
    }
    if (!fingerprints[fp].sampleText) {
      fingerprints[fp].sampleText = text.substring(0, 50);
    }
  });

  const styles = Object.values(fingerprints);
  styles.sort((a, b) => b.prominence - a.prominence);

  // Squint test: check if any non-heading style outranks the top heading
  const topHeading = styles.find(s => s.isHeading);
  const issues = [];
  let squintTestResult = 'pass';

  if (topHeading) {
    styles.forEach(s => {
      if (!s.isHeading && s.prominence > topHeading.prominence) {
        squintTestResult = 'fail';
        issues.push({
          type: 'non-heading-dominates',
          nonHeading: { tags: s.tags, fontSize: s.fontSize, fontWeight: s.fontWeight, prominence: s.prominence, sample: s.sampleText },
          topHeading: { tags: topHeading.tags, fontSize: topHeading.fontSize, fontWeight: topHeading.fontWeight, prominence: topHeading.prominence, sample: topHeading.sampleText },
          detail: `Non-heading (${s.tags.join(',')}, prominence ${s.prominence}) visually dominates top heading (prominence ${topHeading.prominence})`
        });
      }
    });
  }

  // Count distinct hierarchy levels (styles with >0.05 prominence gap)
  let levels = 1;
  for (let i = 1; i < styles.length; i++) {
    if (styles[i - 1].prominence - styles[i].prominence > 0.05) levels++;
  }

  return JSON.stringify({
    styles: styles.slice(0, 20).map(s => ({
      fontSize: s.fontSize,
      fontWeight: s.fontWeight,
      color: s.color,
      prominence: s.prominence,
      isHeading: s.isHeading,
      tags: s.tags,
      sampleText: s.sampleText
    })),
    prominenceRanking: styles.slice(0, 10).map(s => `${s.tags.join('/')} ${s.fontSize}px w${s.fontWeight} → ${s.prominence}`),
    squintTestResult,
    hierarchyLevels: levels,
    issues
  }, null, 2);
})()
```

## Usage in Audit Flow

1. **Take screenshot first** — `mcp__claude-in-chrome__computer` with `action: "screenshot"` to see what we're working with
2. **Run primary extraction** — Captures all text styles, deduplicates, sorts by size
3. **Run font loading check** — Verifies what fonts are actually loaded vs. declared
4. **Run contrast check** — Flags any WCAG failures
5. **Run heading hierarchy check** — Verifies proper heading structure
6. **Run vertical spacing extraction** — Captures spacing between elements, heading margin asymmetry, rhythm base
7. **Run color hierarchy extraction** — Buckets text colors into hierarchy layers, flags contradictions
8. **Run visual weight map** — Computes prominence scores per style, runs squint test, counts hierarchy levels
9. **Cross-reference with source** — Use Grep/Glob to find the CSS classes from extraction in source files
