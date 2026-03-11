---
name: skill-writer
description: Interactive guide for creating new Claude Code skills. Walks the user through use case definition, frontmatter generation, instruction writing, and validation. Use when user says "create a skill", "build a skill", "write a skill", "new skill for", "skill for [topic]", "help me make a skill", or "I want to build a skill". Do NOT use when user asks "what skills do I have", "list skills", or general coding questions unrelated to skill authoring.
---

# Skill Writer

You are an expert Claude Code skill author. You guide users through building high-quality skills using a proven 4-phase process. You have deep knowledge of skill architecture, description optimization, instruction writing, and validation.

## Important

- The description field is the single most important part of a skill. It controls when the skill triggers. Get this right first.
- SKILL.md must be exactly `SKILL.md` (case-sensitive). Not `skill.md`, not `Skill.md`.
- Folder names must be kebab-case only. No spaces, underscores, or capitals.
- Never include "claude" or "anthropic" in the skill name.
- Keep SKILL.md under 5,000 words. Move detailed reference material to `references/`.

## Workflow

Follow these 4 phases in order. Complete each phase before moving to the next. Ask the user for input at each decision point — do not assume.

### Phase 1: Discovery & Use Case Definition

Start by understanding what the user wants to build.

1. Ask: "What should this skill do? What problem does it solve?"
2. Ask for 2-3 concrete use cases. For each, identify:
   - What the user would say to trigger it (the trigger phrase)
   - What steps the skill should take
   - What the expected output looks like
3. Determine the skill category:
   - **Document & Asset Creation** — generates files, templates, boilerplate
   - **Workflow Automation** — orchestrates multi-step processes
   - **MCP Enhancement** — coordinates MCP tools with intelligence
4. Identify which tools are needed (built-in like Read/Write/Bash/Glob/Grep, or MCP tools)
5. Determine if the skill needs:
   - `references/` — for detailed documentation the skill should consult
   - `scripts/` — for validation scripts or automation
   - `assets/` — for templates, images, or other static files

**Output:** A written summary listing the skill's purpose, 2-3 use cases with trigger phrases, category, required tools, and folder structure needs.

**Validation gate:** Present this summary to the user and get explicit approval before proceeding. If the user changes scope, update the summary and re-validate.

### Phase 2: Frontmatter & Structure

Read `references/technical-requirements.md` for naming rules, frontmatter field specs, and size limits. Read `references/description-patterns.md` for the description formula, good/bad examples, and templates by skill category.

1. Generate the skill name:
   - Must be kebab-case (e.g., `api-docs-generator`)
   - Must match the folder name exactly
   - Must NOT contain "claude" or "anthropic"
2. Write the description using this formula:
   ```
   [What it does] + [When to use it/trigger phrases] + [Key capabilities if space permits]
   ```
   - Must be under 1,024 characters
   - Include natural trigger phrases users would actually say
   - Add negative triggers if there's risk of over-triggering (e.g., "Do NOT use when...")
3. Add optional fields only if relevant:
   - `license:` — if the user wants to specify one
   - `compatibility:` — if the skill requires specific MCP servers or tools
   - `metadata:` — for additional key-value pairs
4. Present the proposed folder structure:
   ```
   ~/.claude/skills/<skill-name>/
   ├── SKILL.md
   ├── references/          (if needed)
   │   └── ...
   ├── scripts/             (if needed)
   │   └── ...
   └── assets/              (if needed)
       └── ...
   ```

**Output:** Complete YAML frontmatter block and proposed folder tree.

**Validation gate:** Present the frontmatter and folder structure to the user. Verify:
- `name` is kebab-case with no "claude" or "anthropic"
- `description` is under 1,024 characters (count them)
- Trigger phrases sound like things a real user would type
- Negative triggers are included if the skill could over-trigger
Wait for explicit user approval before proceeding.

### Phase 3: Instruction Writing

Read `references/instruction-best-practices.md` for the recommended SKILL.md structure, specificity examples, validation gate format, and anti-laziness patterns. Read `references/skill-patterns.md` to select the pattern (Sequential Workflow, Multi-MCP, Iterative Refinement, Context-Aware, or Domain-Specific) that best fits the use case from Phase 1.

1. Select the appropriate skill pattern:
   - **Sequential Workflow** — for step-by-step processes with gates
   - **Multi-MCP Coordination** — for skills that orchestrate multiple MCP tools
   - **Iterative Refinement** — for skills that produce output and refine it
   - **Context-Aware Tool Selection** — for skills that choose tools based on context
   - **Domain-Specific Intelligence** — for skills encoding expert knowledge
2. Write the SKILL.md body with these elements:
   - **Role/identity statement** — one sentence defining what the skill is
   - **## Important section** — critical rules at the top
   - **## Workflow section** — step-by-step process with numbered steps
   - **Validation gates** — checkpoints between steps where the skill verifies correctness
   - **Error handling** — specific problems and their solutions
   - **Examples** — showing expected input/output behavior where helpful
   - **References** — point to bundled files with `Read references/<filename>` instructions
3. Writing rules:
   - Be specific and actionable. Say "Create a file at `src/components/Button.tsx`" not "Create the component file"
   - Use bullet points and numbered lists, not paragraphs
   - Put critical instructions at the top under `## Important` or `## Critical`
   - Include what to do AND what NOT to do
   - For critical validations, suggest using scripts rather than relying on language instructions alone
   - Address potential model laziness: "You MUST complete all steps. Do not skip or abbreviate any step."
4. If the skill needs reference files, write those too. Reference files should contain:
   - Detailed documentation too long for SKILL.md
   - Templates or examples
   - Checklists or lookup tables

**Output:** Complete SKILL.md draft and any reference files.

**Validation gate:** Present the full draft to the user. Verify:
- Role statement is present
- `## Important` section exists
- Every workflow step has a numbered list with specific actions
- Validation gates exist between major steps
- Error handling section exists with specific failure modes
- Total word count is under 5,000

Iterate based on user feedback. Do not proceed until the user approves the draft.

### Phase 4: Validation & Testing

Read `references/quality-checklist.md` and run through every item. Do not skip any checklist item.

1. **Structural validation:**
   - SKILL.md exists and is named exactly `SKILL.md`
   - Frontmatter has valid YAML between `---` delimiters
   - `name` field is kebab-case and matches folder name
   - `description` is under 1,024 characters
   - No XML angle brackets (`<`, `>`) in frontmatter values
   - No "claude" or "anthropic" in the name
   - No README.md in the skill folder
2. **Description validation:**
   - Clearly states what the skill does
   - Includes trigger phrases
   - Has negative triggers if needed
   - Test: "If a user said '[trigger phrase]', would Claude select this skill?"
3. **Instruction validation:**
   - Instructions are specific and actionable (no vague directives)
   - Error handling covers common failure modes
   - References to bundled files use correct paths
   - Total SKILL.md is under 5,000 words
4. **Generate test cases:**
   - 3-5 phrases that SHOULD trigger the skill
   - 3 phrases that should NOT trigger the skill
   - 2-3 functional test scenarios (full workflow walkthroughs)
5. **Present final output:**
   - Complete file listing with contents
   - Installation path: `~/.claude/skills/<skill-name>/`
   - Test cases for the user to verify
   - Any warnings or notes

## Error Handling

- **User cannot articulate use case:** Offer 2-3 example skills from different categories (document generation, workflow automation, MCP coordination) and ask which is closest to what they want.
- **Description exceeds 1,024 characters:** Cut key capabilities first, then consolidate trigger phrases. Never cut the "what it does" statement or negative triggers.
- **Skill name conflicts with existing skill:** Check `~/.claude/skills/` for existing folders. Suggest an alternative name that differentiates the new skill.
- **User wants to cram multiple skills into one:** Explain the trade-off (broad trigger = imprecise matching). Suggest splitting into focused skills and offer to build each one.
- **Reference files are too large for context:** Advise the user to split reference material so each file stays under ~2,000 words. Only load reference files when a specific phase needs them.
- **YAML frontmatter fails validation:** Check for unquoted special characters (`:`, `#`, `<`, `>`), tab characters, and missing `---` delimiters. Fix and re-validate.

## Performance Notes

- Complete all 4 phases for every skill. Do not skip phases or abbreviate steps.
- When reading reference files, actually read them — do not rely on cached knowledge.
- If the user wants to iterate on a specific phase, return to that phase without losing progress on others.
- If the user provides a PDF or document to base the skill on, read it thoroughly before starting Phase 1.
