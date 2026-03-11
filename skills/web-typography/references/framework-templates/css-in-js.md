# CSS-in-JS Type System Template

For styled-components, Emotion, Stitches, Vanilla Extract, or any theme-object-based system.

## Theme Object

```typescript
export const typography = {
  fonts: {
    sans: '"Inter", ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif',
    serif: 'ui-serif, Georgia, Cambria, "Times New Roman", Times, serif',
    mono: '"Geist Mono", ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", "Courier New", monospace',
  },

  // Static sizes (never fluid)
  fontSizes: {
    xs: "0.75rem",     // 12px
    sm: "0.875rem",    // 14px
    base: "1rem",      // 16px

    // Fluid sizes
    lg: "clamp(1rem, 0.95rem + 0.19vw, 1.125rem)",
    xl: "clamp(1.125rem, 1.08rem + 0.19vw, 1.25rem)",
    "2xl": "clamp(1.25rem, 1.16rem + 0.38vw, 1.5rem)",
    "3xl": "clamp(1.5rem, 1.36rem + 0.56vw, 1.875rem)",
    "4xl": "clamp(1.75rem, 1.57rem + 0.75vw, 2.25rem)",
    "5xl": "clamp(2rem, 1.63rem + 1.5vw, 3rem)",
    "6xl": "clamp(2.25rem, 1.69rem + 2.25vw, 3.75rem)",
    "7xl": "clamp(2.5rem, 1.75rem + 3.01vw, 4.5rem)",
    "8xl": "clamp(3rem, 1.87rem + 4.51vw, 6rem)",
  },

  lineHeights: {
    none: 1,
    tight: 1.15,
    snug: 1.3,
    normal: 1.5,
    relaxed: 1.6,
    loose: 1.75,
  },

  letterSpacings: {
    tighter: "-0.025em",
    tight: "-0.015em",
    slight: "-0.01em",
    normal: "0",
    wide: "0.05em",
    wider: "0.08em",
    widest: "0.1em",
  },

  fontWeights: {
    normal: 400,
    medium: 500,
    semibold: 600,
    bold: 700,
    extrabold: 800,
    black: 900,
  },

  measures: {
    narrow: "45ch",
    base: "65ch",
    wide: "75ch",
  },
} as const;

export type Typography = typeof typography;
```

## Semantic Text Styles

```typescript
/** Composite text style definitions */
export const textStyles = {
  caption: {
    fontSize: typography.fontSizes.xs,
    fontWeight: typography.fontWeights.normal,
    lineHeight: typography.lineHeights.snug,
    letterSpacing: typography.letterSpacings.normal,
  },

  label: {
    fontSize: typography.fontSizes.sm,
    fontWeight: typography.fontWeights.medium,
    lineHeight: typography.lineHeights.snug,
    letterSpacing: typography.letterSpacings.normal,
  },

  overline: {
    fontSize: typography.fontSizes.xs,
    fontWeight: typography.fontWeights.semibold,
    lineHeight: typography.lineHeights.snug,
    letterSpacing: typography.letterSpacings.widest,
    textTransform: "uppercase" as const,
  },

  body: {
    fontSize: typography.fontSizes.base,
    fontWeight: typography.fontWeights.normal,
    lineHeight: typography.lineHeights.normal,
    letterSpacing: typography.letterSpacings.normal,
  },

  bodyLg: {
    fontSize: typography.fontSizes.lg,
    fontWeight: typography.fontWeights.normal,
    lineHeight: typography.lineHeights.normal,
    letterSpacing: typography.letterSpacings.normal,
  },

  headingSm: {
    fontSize: typography.fontSizes.xl,
    fontWeight: typography.fontWeights.semibold,
    lineHeight: typography.lineHeights.snug,
    letterSpacing: typography.letterSpacings.slight,
  },

  heading: {
    fontSize: typography.fontSizes["2xl"],
    fontWeight: typography.fontWeights.semibold,
    lineHeight: typography.lineHeights.snug,
    letterSpacing: typography.letterSpacings.tight,
  },

  headingLg: {
    fontSize: typography.fontSizes["3xl"],
    fontWeight: typography.fontWeights.bold,
    lineHeight: typography.lineHeights.tight,
    letterSpacing: typography.letterSpacings.tight,
  },

  title: {
    fontSize: typography.fontSizes["4xl"],
    fontWeight: typography.fontWeights.bold,
    lineHeight: typography.lineHeights.tight,
    letterSpacing: typography.letterSpacings.tighter,
  },

  displaySm: {
    fontSize: typography.fontSizes["5xl"],
    fontWeight: typography.fontWeights.bold,
    lineHeight: typography.lineHeights.none,
    letterSpacing: typography.letterSpacings.tighter,
  },

  display: {
    fontSize: typography.fontSizes["6xl"],
    fontWeight: typography.fontWeights.bold,
    lineHeight: typography.lineHeights.none,
    letterSpacing: typography.letterSpacings.tighter,
  },

  displayLg: {
    fontSize: typography.fontSizes["7xl"],
    fontWeight: typography.fontWeights.extrabold,
    lineHeight: typography.lineHeights.none,
    letterSpacing: typography.letterSpacings.tighter,
  },

  displayXl: {
    fontSize: typography.fontSizes["8xl"],
    fontWeight: typography.fontWeights.black,
    lineHeight: typography.lineHeights.none,
    letterSpacing: typography.letterSpacings.tighter,
  },
} as const;

export type TextStyle = keyof typeof textStyles;
```

## styled-components Usage

```typescript
import styled, { ThemeProvider, css } from "styled-components";
import { typography, textStyles, type TextStyle } from "./typography";

// Add typography to your theme
const theme = {
  ...typography,
  textStyles,
};

// Utility: apply a named text style
function applyTextStyle(style: TextStyle) {
  const s = textStyles[style];
  return css`
    font-size: ${s.fontSize};
    font-weight: ${s.fontWeight};
    line-height: ${s.lineHeight};
    letter-spacing: ${s.letterSpacing};
    ${"textTransform" in s ? `text-transform: ${s.textTransform};` : ""}
  `;
}

// Components
const Title = styled.h1`
  ${applyTextStyle("title")}
  text-wrap: balance;
`;

const Heading = styled.h2`
  ${applyTextStyle("headingLg")}
  text-wrap: balance;
`;

const Body = styled.p`
  ${applyTextStyle("body")}
  text-wrap: pretty;
`;

const Prose = styled.div`
  max-width: ${({ theme }) => theme.measures.base};
`;

const Caption = styled.span`
  ${applyTextStyle("caption")}
`;

const Overline = styled.span`
  ${applyTextStyle("overline")}
`;

// Generic Text component
interface TextProps {
  variant?: TextStyle;
}

const Text = styled.span<TextProps>`
  ${({ variant = "body" }) => applyTextStyle(variant)}
`;
```

## Emotion Usage

```typescript
import { css, Global } from "@emotion/react";
import styled from "@emotion/styled";
import { typography, textStyles, type TextStyle } from "./typography";

// Global base styles
const globalStyles = css`
  html {
    font-size: 100%;
    -webkit-text-size-adjust: 100%;
    text-size-adjust: 100%;
    font-optical-sizing: auto;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }

  body {
    font-family: ${typography.fonts.sans};
    font-size: ${typography.fontSizes.base};
    font-weight: ${typography.fontWeights.normal};
    line-height: ${typography.lineHeights.normal};
  }

  h1, h2, h3 {
    text-wrap: balance;
  }

  p {
    text-wrap: pretty;
  }

  code, pre, kbd {
    font-family: ${typography.fonts.mono};
  }

  table td, [data-numeric] {
    font-variant-numeric: tabular-nums;
  }
`;

function GlobalTypography() {
  return <Global styles={globalStyles} />;
}
```

## Vanilla Extract Usage

```typescript
// typography.css.ts
import { createGlobalTheme, style, styleVariants } from "@vanilla-extract/css";

export const vars = createGlobalTheme(":root", {
  font: {
    sans: '"Inter", ui-sans-serif, system-ui, -apple-system, sans-serif',
    serif: 'ui-serif, Georgia, Cambria, serif',
    mono: '"Geist Mono", ui-monospace, monospace',
  },
  fontSize: {
    xs: "0.75rem",
    sm: "0.875rem",
    base: "1rem",
    lg: "clamp(1rem, 0.95rem + 0.19vw, 1.125rem)",
    xl: "clamp(1.125rem, 1.08rem + 0.19vw, 1.25rem)",
    "2xl": "clamp(1.25rem, 1.16rem + 0.38vw, 1.5rem)",
    "3xl": "clamp(1.5rem, 1.36rem + 0.56vw, 1.875rem)",
    "4xl": "clamp(1.75rem, 1.57rem + 0.75vw, 2.25rem)",
    "5xl": "clamp(2rem, 1.63rem + 1.5vw, 3rem)",
    "6xl": "clamp(2.25rem, 1.69rem + 2.25vw, 3.75rem)",
    "7xl": "clamp(2.5rem, 1.75rem + 3.01vw, 4.5rem)",
    "8xl": "clamp(3rem, 1.87rem + 4.51vw, 6rem)",
  },
  lineHeight: {
    none: "1",
    tight: "1.15",
    snug: "1.3",
    normal: "1.5",
    relaxed: "1.6",
  },
  letterSpacing: {
    tighter: "-0.025em",
    tight: "-0.015em",
    normal: "0",
    wide: "0.05em",
    widest: "0.1em",
  },
  fontWeight: {
    normal: "400",
    medium: "500",
    semibold: "600",
    bold: "700",
    extrabold: "800",
  },
  measure: {
    narrow: "45ch",
    base: "65ch",
    wide: "75ch",
  },
});

// Semantic text style variants
export const text = styleVariants({
  caption: {
    fontSize: vars.fontSize.xs,
    fontWeight: vars.fontWeight.normal,
    lineHeight: vars.lineHeight.snug,
  },
  label: {
    fontSize: vars.fontSize.sm,
    fontWeight: vars.fontWeight.medium,
    lineHeight: vars.lineHeight.snug,
  },
  body: {
    fontSize: vars.fontSize.base,
    fontWeight: vars.fontWeight.normal,
    lineHeight: vars.lineHeight.normal,
  },
  heading: {
    fontSize: vars.fontSize["2xl"],
    fontWeight: vars.fontWeight.semibold,
    lineHeight: vars.lineHeight.snug,
    letterSpacing: vars.letterSpacing.tight,
  },
  title: {
    fontSize: vars.fontSize["4xl"],
    fontWeight: vars.fontWeight.bold,
    lineHeight: vars.lineHeight.tight,
    letterSpacing: vars.letterSpacing.tighter,
  },
  display: {
    fontSize: vars.fontSize["6xl"],
    fontWeight: vars.fontWeight.bold,
    lineHeight: vars.lineHeight.none,
    letterSpacing: vars.letterSpacing.tighter,
  },
});
```
