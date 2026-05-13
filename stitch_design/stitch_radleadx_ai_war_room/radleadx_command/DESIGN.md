---
name: RADLEADX Command
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#c1c6d7'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#8b90a0'
  outline-variant: '#414755'
  surface-tint: '#adc6ff'
  primary: '#adc6ff'
  on-primary: '#002e69'
  primary-container: '#4b8eff'
  on-primary-container: '#00285c'
  inverse-primary: '#005bc1'
  secondary: '#53e16f'
  on-secondary: '#003911'
  secondary-container: '#05b046'
  on-secondary-container: '#003a11'
  tertiary: '#e8b3ff'
  on-tertiary: '#510074'
  tertiary-container: '#c567f4'
  on-tertiary-container: '#460066'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d8e2ff'
  primary-fixed-dim: '#adc6ff'
  on-primary-fixed: '#001a41'
  on-primary-fixed-variant: '#004493'
  secondary-fixed: '#72fe88'
  secondary-fixed-dim: '#53e16f'
  on-secondary-fixed: '#002107'
  on-secondary-fixed-variant: '#00531c'
  tertiary-fixed: '#f6d9ff'
  tertiary-fixed-dim: '#e8b3ff'
  on-tertiary-fixed: '#310048'
  on-tertiary-fixed-variant: '#7201a2'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  body-main:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  data-mono:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.05em
  headline-md-mobile:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 24px
  margin-safe: 32px
  panel-gap: 16px
---

## Brand & Style
The design system embodies an **Industrial-Technological** aesthetic tailored for high-stakes commercial intelligence. It transforms a standard dashboard into a "War Room" environment, evoking feelings of absolute control, precision, and strategic superiority.

The visual style is a hybrid of **Minimalist Dark Mode** and **Functional Industrialism**. It prioritizes high information density without clutter, using deep atmospheric backgrounds and vibrant "signal" accents to represent autonomous agents. The target audience is sophisticated operators and executives who require real-time, actionable intelligence presented with the gravity of a military command center.

## Colors
The palette is rooted in a **Deep Charcoal and Obsidian** foundation to minimize eye strain during long "watch" sessions.

- **Foundation:** The background uses `#080808`, while elevated panels use `#161616` to create a subtle sense of depth.
- **Agent Accents:**
    - **NLU (Natural Language):** Electric Blue (`#007AFF`)
    - **Outreach:** Tactical Green (`#34C759`)
    - **Business Intel:** Regal Purple (`#AF52DE`)
- **Signals:** Progress bars and heatmaps utilize a spectrum from High-Confidence Green to Critical Red to denote data reliability and urgency.

## Typography
This design system utilizes a dual-font strategy to balance readability with technical authenticity.

- **Inter:** Used for all primary UI interactions, navigational elements, and descriptive text. It provides a clean, professional "SaaS" bridge to the otherwise industrial aesthetic.
- **JetBrains Mono:** Reserved for technical data, logs, confidence percentages, and agent status labels. All monospaced text should be rendered with slightly increased tracking (letter-spacing) when in all-caps to enhance the "readout" feel.

## Layout & Spacing
The layout follows a **Rigid Grid System** inspired by modular tactical displays.

- **Grid:** A 12-column grid for desktop, collapsing to 4 columns on mobile. Panels should feel like "docked" modules within a single viewport, minimizing the need for vertical scrolling where possible.
- **Rhythm:** A 4px baseline grid ensures tight alignment of data rows and monospaced strings.
- **Density:** High-density spacing is encouraged for data-heavy views, using 8px or 12px padding inside data modules to maximize information visible "above the fold."

## Elevation & Depth
In this design system, depth is achieved through **Tonal Layering** rather than traditional shadows.

- **Surface Levels:** The base layer is the darkest. Each interactive or floating container is one shade lighter (e.g., `#161616` on `#080808`).
- **Subtle Outlines:** Instead of drop shadows, use 1px solid borders (`#2C2C2E`) to define panel boundaries.
- **Glow Effects:** Critical alerts or active agents can emit a very soft, low-opacity outer glow (15-20% opacity) of their respective accent color to indicate "active" or "transmitting" status.

## Shapes
Despite the industrial nature, the system utilizes **Large Radius Corners** to create a sophisticated, hardware-inspired look (similar to high-end modern instrumentation).

- **Containers:** Main dashboard panels use `rounded-xl` (1.5rem / 24px) to soften the "War Room" intensity.
- **Buttons/Inputs:** Use `rounded-lg` (1rem / 16px) for a comfortable, modern touch.
- **Status Pills:** Fully rounded (pill-shaped) for agent tags and status indicators.

## Components
- **Command Buttons:** Large, high-contrast buttons with heavy-weight Inter text. Primary actions for agents use their specific accent color; secondary actions use an outlined style.
- **Signal Confidence Bars:** Custom progress bars using a segmented "cell" design rather than a smooth fill. Higher confidence levels light up more segments in the agent's color.
- **Data Cards:** Modules with a monospaced "Header" section containing a timestamp or UUID, followed by the main data body in Inter.
- **Heatmap Visuals:** Used for territory or market density. Colors should bleed into the charcoal background using soft radial gradients rather than hard-edged cells.
- **Input Fields:** Darker than the panel background, with the border becoming the agent's accent color on focus to signal which part of the system the user is interacting with.
- **Agent Logs:** A dedicated terminal-style component using JetBrains Mono, with color-coded syntax highlighting for "Success," "Error," and "Transmitting."