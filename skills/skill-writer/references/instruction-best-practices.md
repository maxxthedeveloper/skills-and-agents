# Instruction Best Practices for Claude Code Skills

## Recommended SKILL.md Structure

```markdown
---
name: my-skill
description: ...
---

# Skill Title

One sentence defining what this skill is and its role.

## Important

Critical rules that must never be violated. Put the most important constraints here.

## Workflow

Step-by-step process. Numbered steps with clear validation gates.

### Step 1: [Name]
...

### Step 2: [Name]
...

## Error Handling

Common problems and their specific solutions.

## Performance Notes

Instructions to prevent skipping, abbreviating, or lazy behavior.
```

## Be Specific and Actionable

Every instruction should tell Claude exactly what to do. Vague instructions get interpreted inconsistently.

### Good (Specific)
- "Create a file at `src/components/Button.tsx` with a React functional component that accepts `label` and `onClick` props"
- "Run `npm test -- --coverage` and check that coverage is above 80%"
- "Read the user's `package.json` to determine if they use yarn, npm, or pnpm, then use the correct package manager for all install commands"
- "If the API returns a 401 error, tell the user to check their API key in `.env` and verify it hasn't expired"

### Bad (Vague)
- "Create the component file"
- "Make sure tests pass"
- "Use the right package manager"
- "Handle errors appropriately"

## Include What To Do AND What Not To Do

Claude follows instructions better when it knows both the positive and negative boundaries.

```markdown
## Important

- Always use TypeScript for new files. Never generate plain JavaScript.
- Always read existing files before modifying them. Never assume file contents.
- Use the Edit tool for modifications. Do NOT use sed, awk, or Bash for file editing.
- Ask the user before deleting any files. Do NOT delete files without confirmation.
```

## Use Validation Gates

Between major steps, add checkpoints where the skill verifies its own work.

```markdown
### Step 2: Generate Component

1. Create the component file at the determined path
2. **Validation gate:** Read the file back and verify:
   - It exports a named component (not default)
   - Props interface is defined and exported
   - No TypeScript errors (run `npx tsc --noEmit` on the file)
3. If validation fails, fix the issues before proceeding to Step 3
```

## Error Handling with Specific Solutions

Don't just say "handle errors." Specify which errors can occur and what to do about each one.

```markdown
## Error Handling

- **File already exists:** Ask the user if they want to overwrite or choose a different name. Do not overwrite without permission.
- **Missing dependency:** Run `npm install <package>` automatically. If install fails, tell the user the exact package and version needed.
- **TypeScript compilation error:** Read the error message, identify the issue, fix it, and re-run the type checker. If the error persists after 2 attempts, show the error to the user and ask for guidance.
- **Test failure:** Read the test output, identify which test failed and why, then fix the implementation (not the test) unless the test expectation is wrong.
```

## Reference Bundled Resources Clearly

When your skill includes reference files, tell Claude exactly when and how to use them.

```markdown
### Step 1: Determine the appropriate pattern

Read `references/patterns.md` to review the available patterns. Select the one that best matches the user's use case based on the decision criteria in that file.
```

Don't say "consult the references" — say which file, when to read it, and what to look for.

## Progressive Disclosure

Structure information in layers:
1. **Frontmatter** — just enough to trigger correctly (description)
2. **SKILL.md body** — the complete workflow with key instructions
3. **references/** — detailed documentation, examples, lookup tables

This means SKILL.md should contain the workflow and key rules, while deep reference material lives in separate files that are only loaded when needed.

## Use Headers and Lists, Not Paragraphs

Claude processes structured content more reliably than prose paragraphs.

### Good
```markdown
## Naming Conventions

- Components: PascalCase (e.g., `UserProfile`)
- Files: kebab-case (e.g., `user-profile.tsx`)
- Props: camelCase (e.g., `userName`)
- CSS classes: kebab-case (e.g., `user-profile-header`)
```

### Bad
```markdown
When naming things, components should use PascalCase like UserProfile, while files
should be kebab-case like user-profile.tsx. Props use camelCase such as userName and
CSS classes use kebab-case like user-profile-header.
```

## Put Critical Instructions at the Top

Use `## Important` or `## Critical` headers at the top of SKILL.md, right after the role statement. Claude pays more attention to instructions that appear early.

## Address Model Laziness

For complex skills with many steps, Claude may try to abbreviate or skip steps. Counter this explicitly:

```markdown
## Performance Notes

- You MUST complete all steps in the workflow. Do not skip or abbreviate any step.
- When generating code, produce the complete implementation. Do not use placeholder comments like "// ... rest of implementation" or "// TODO: implement this."
- Read every file referenced in the workflow. Do not assume you know their contents.
- If a step says to validate, actually run the validation. Do not just state that it would pass.
```

## Use Scripts for Critical Validations

Language instructions can be missed. For truly critical validations, include a script:

```markdown
### Step 4: Validate Output

Run `bash scripts/validate.sh` to check the generated output. This script verifies:
- All required files exist
- YAML frontmatter is valid
- No prohibited patterns are present

If the script reports errors, fix them before presenting the output to the user.
```

This is more reliable than "check that the YAML is valid" because the script will catch what the model might miss.
