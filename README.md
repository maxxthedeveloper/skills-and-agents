# Skills & Agents

Reusable [Claude Code](https://claude.ai/code) skills and agents for design, development, and content workflows.

## What's the difference?

| | Skill | Agent |
|---|---|---|
| Runs in | Main conversation (inline) | Isolated context window |
| Best for | Reference material, conventions, `/slash-command` workflows | Self-contained jobs, parallel work, structured reports |
| Invoked via | `/skill-name` or auto-discovery | `Task` tool delegation |

**Rule of thumb:** If it's knowledge you apply while working, it's a skill. If it's a job you hand off, it's an agent.

## Agents

Custom subagents spawned via the `Task` tool. Each runs in its own context with a focused system prompt.

| Agent | Purpose |
|---|---|
| `design-lead` | Orchestrate parallel design reviews with 5-6 specialist auditors |
| `design-auditor` | Comprehensive design audit (hierarchy, density, patterns, accessibility) |
| `info-arch-auditor` | Information architecture, visual hierarchy, 3-second test |
| `aesthetics-auditor` | Visual polish, color harmony, typography rhythm, cohesion |
| `copy-auditor` | Audit user-facing text for clarity and benefit framing |
| `interaction-auditor` | Touch targets, affordances, state coverage, animation quality |
| `systems-auditor` | Design system tokens, spacing scales, component patterns |
| `react-auditor` | React/Next.js resilience patterns and performance |
| `mobile-ux-auditor` | Mobile UX audit (cognitive load, spacing, consistency) |
| `feature-research` | Research libraries, frameworks, and technical approaches |

### Design review team

The `design-lead` agent orchestrates a full parallel review by spawning these specialists simultaneously:

```
design-lead
  ├── systems-auditor
  ├── aesthetics-auditor
  ├── info-arch-auditor (highest priority)
  ├── copy-auditor
  ├── interaction-auditor
  └── react-auditor (if React/Next.js detected)
```

Each auditor reports findings independently. The design-lead deduplicates, resolves conflicts, and delivers a ship/don't-ship verdict.

## Skills

Inline knowledge and workflows that run in the main conversation context.

### `skills/framer/` — Framer voice and copy

| Skill | Purpose |
|---|---|
| `framer-ux-writer` | Write and audit in-product UX copy for Framer Studio (toasts, buttons, empty states, dialogs) |
| `framer-email-writer` | Write the emails Framer sends via Loops (releases, onboarding, changelog, lifecycle) |

### `skills/personal/` — general-purpose

| Skill | Purpose |
|---|---|
| `design-engineer` | Production-grade frontend interfaces with 18 interface polish principles |
| `web-typography` | Audit, generate, and systematize web typography |
| `humanize-ai-content` | Turn AI-generated content into natural, human-sounding writing |

## Installation

### Agents

```bash
# Global (all projects)
cp agents/design-lead.md ~/.claude/agents/

# Project-specific
cp agents/design-auditor.md .claude/agents/
```

### Skills

```bash
# Global
cp -R skills/framer/framer-ux-writer ~/.claude/skills/

# Project-specific
cp -R skills/personal/web-typography .claude/skills/
```
