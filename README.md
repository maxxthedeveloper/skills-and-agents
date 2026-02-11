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
| `design-engineer` | Implement and refine UI components with pixel-perfect detail |
| `design-lead` | Orchestrate parallel design reviews with 5-6 specialist auditors |
| `design-auditor` | Comprehensive design audit (hierarchy, density, patterns, accessibility) |
| `info-arch-auditor` | Information architecture, visual hierarchy, 3-second test |
| `aesthetics-auditor` | Visual polish, color harmony, typography rhythm, cohesion |
| `copy-auditor` | Audit user-facing text for clarity and benefit framing |
| `interaction-auditor` | Touch targets, affordances, state coverage, animation quality |
| `systems-auditor` | Design system tokens, spacing scales, component patterns |
| `react-auditor` | React/Next.js resilience patterns and performance |
| `mobile-ux-auditor` | Mobile UX audit (cognitive load, spacing, consistency) |
| `ux-copywriter` | Write UX microcopy (buttons, errors, empty states, tooltips) |
| `feature-research` | Research libraries, frameworks, and technical approaches |
| `code-reviewer` | Structured code review with prioritized issues |
| `system-prompt-engineer` | Debug and iterate on AI system prompts |

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

| Skill | Location | Purpose |
|---|---|---|
| `copywriting` | `skills/copywriter/` | Marketing page copy — headlines, CTAs, page structure frameworks |
| `tech-storytelling` | Root `SKILL.md` | Video script workflow for product announcements |

## Installation

### Agents

Copy individual agent files to your Claude Code agents directory:

```bash
# Global (all projects)
cp agents/design-engineer.md ~/.claude/agents/

# Project-specific
cp agents/code-reviewer.md .claude/agents/
```

### Skills

Copy skill directories to your Claude Code skills directory:

```bash
# Global
cp -r skills/copywriter ~/.claude/skills/

# Project-specific
cp -r skills/copywriter .claude/skills/
```

## License

MIT
