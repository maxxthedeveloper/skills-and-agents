# Quality Checklist for Claude Code Skills

Run through every item before considering the skill complete.

## Before You Start

- [ ] **Clear use case:** Can you describe what this skill does in one sentence?
- [ ] **Not duplicate:** Does a similar skill already exist? Check `~/.claude/skills/` for overlaps.
- [ ] **Right scope:** Is this one focused skill, not 3 skills crammed together?
- [ ] **Tool availability:** Are all required tools (built-in or MCP) available and tested?

## During Development

### Frontmatter
- [ ] `SKILL.md` is exactly `SKILL.md` (case-sensitive)
- [ ] Folder name is kebab-case (no spaces, underscores, or capitals)
- [ ] `name` field matches folder name exactly
- [ ] `name` does not contain "claude" or "anthropic"
- [ ] `description` is under 1,024 characters
- [ ] `description` includes what the skill does
- [ ] `description` includes trigger phrases (natural language users would actually say)
- [ ] `description` includes negative triggers if risk of over-triggering
- [ ] No XML angle brackets (`<`, `>`) in frontmatter values
- [ ] YAML frontmatter is valid (properly indented, quoted if special characters)

### Instructions
- [ ] Role/identity statement is present and clear
- [ ] `## Important` section exists with critical rules
- [ ] Workflow steps are numbered and ordered
- [ ] Each step has specific, verifiable outputs
- [ ] Validation gates exist between major steps
- [ ] Error handling covers common failure modes with specific solutions
- [ ] Instructions are specific and actionable (not vague)
- [ ] Both "do this" and "don't do that" instructions are included
- [ ] References to bundled files include exact file paths
- [ ] SKILL.md is under 5,000 words
- [ ] Performance notes address potential skipping/abbreviation

### Bundled Resources
- [ ] All referenced files actually exist in the skill folder
- [ ] File paths in instructions match actual file locations
- [ ] Reference files contain useful detail (not just repeating SKILL.md)
- [ ] No README.md in the skill folder

## Before Upload

- [ ] **Trigger test:** Read the description and list 3-5 phrases that should trigger it
- [ ] **Negative trigger test:** List 3 phrases that should NOT trigger it
- [ ] **Specificity test:** Would this description win over other enabled skills for its trigger phrases?
- [ ] **Completeness test:** Walk through the entire workflow mentally — are any steps missing?
- [ ] **Edge case test:** What happens if the user provides unexpected input at each step?
- [ ] **Context size test:** Is the total skill content (SKILL.md + referenced files) reasonable? Will it leave enough context for the actual task?

## After Upload / Installation

- [ ] **Activation test:** Say a trigger phrase — does the skill activate?
- [ ] **Non-activation test:** Say an unrelated phrase — does the skill stay inactive?
- [ ] **Full workflow test:** Walk through the complete workflow with a real use case
- [ ] **Error path test:** Intentionally trigger an error condition — does the error handling work?
- [ ] **Output quality test:** Does the final output match what was promised in the description?
