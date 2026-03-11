# Technical Requirements for Claude Code Skills

## File Structure

A skill lives in a single folder under `~/.claude/skills/`:

```
~/.claude/skills/<skill-name>/
├── SKILL.md                    # Required. The main skill file.
├── references/                 # Optional. Detailed docs, guides, lookup tables.
│   └── *.md
├── scripts/                    # Optional. Validation or automation scripts.
│   └── *.sh / *.py / *.js
└── assets/                     # Optional. Templates, images, static files.
    └── *
```

## SKILL.md Naming

- Must be exactly `SKILL.md` — case-sensitive
- Not `skill.md`, `Skill.md`, `SKILLS.md`, or any variation
- There must be exactly one `SKILL.md` per skill folder
- Do NOT include a `README.md` inside the skill folder

## Folder Naming

- Must be kebab-case: lowercase letters, numbers, and hyphens only
- No spaces, underscores, capitals, or special characters
- Must match the `name` field in the frontmatter exactly
- Good: `api-docs-generator`, `react-component-builder`, `git-workflow`
- Bad: `API_Docs_Generator`, `react component builder`, `gitWorkflow`

## YAML Frontmatter

The frontmatter goes at the very top of SKILL.md, between `---` delimiters:

```yaml
---
name: my-skill-name
description: What this skill does. When to use it (trigger phrases). Key capabilities.
---
```

### Required Fields

#### `name`
- Type: string
- Must be kebab-case
- Must match the folder name exactly
- Must NOT contain "claude" or "anthropic" (rejected on upload)
- Examples: `api-docs-generator`, `test-writer`, `deploy-helper`

#### `description`
- Type: string
- Maximum: 1,024 characters
- This is the most important field — it controls when the skill is triggered
- Must include: WHAT the skill does + WHEN to use it (trigger phrases)
- Can optionally include: key capabilities, negative triggers
- No XML angle brackets (`<`, `>`) allowed in the value
- Can be a multi-line YAML string using `>-` or `|` if needed

### Optional Fields

#### `license`
- Type: string
- SPDX license identifier (e.g., `MIT`, `Apache-2.0`)

#### `compatibility`
- Type: string
- Maximum: 500 characters
- Describe required MCP servers, tools, or environment requirements
- Example: `Requires GitHub MCP server for PR operations`

#### `metadata`
- Type: object (key-value pairs)
- For additional structured information
- Example:
  ```yaml
  metadata:
    author: jane-doe
    version: "1.0"
    category: workflow
  ```

## Security Rules

1. **No XML angle brackets in frontmatter** — `<` and `>` characters in frontmatter values will cause upload rejection
2. **No "claude" or "anthropic" in skill name** — these are reserved and will be rejected
3. **No prompt injection attempts** — skills are reviewed; attempts to override system behavior will be rejected
4. **Bundled files are read-only context** — files in references/, scripts/, assets/ are available for the skill to read but cannot modify the user's system without explicit tool calls

## Size Guidelines

- SKILL.md should be under 5,000 words
- If you need more detail, put it in `references/` files and have SKILL.md reference them
- Each enabled skill adds to Claude's context window, so keep skills focused and concise
- Consider: would you rather have one 5,000-word skill or five 1,000-word skills that each do one thing well?

## How Skills Are Loaded

1. When a user sends a message, Claude reads all enabled skill descriptions
2. Claude selects the most relevant skill(s) based on description match
3. Claude reads the full SKILL.md of selected skill(s)
4. If SKILL.md references bundled files, Claude reads those too
5. Claude follows the skill's instructions to complete the task

This means:
- The description must be good enough to trigger selection (Phase 1)
- SKILL.md must be clear enough to follow without ambiguity (Phase 2)
- Referenced files are only loaded when needed, saving context (Phase 3)
