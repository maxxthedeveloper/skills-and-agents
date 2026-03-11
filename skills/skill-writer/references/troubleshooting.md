# Troubleshooting Claude Code Skills

## Skill Won't Upload

### SKILL.md naming issue
**Symptom:** Upload fails or skill isn't recognized.
**Cause:** File is not named exactly `SKILL.md`.
**Fix:** Rename to exactly `SKILL.md`. Check for:
- Wrong case: `skill.md`, `Skill.md`, `SKILLS.md`
- Extra extensions: `SKILL.md.txt`
- Hidden characters in the filename

### Invalid frontmatter
**Symptom:** Upload fails with YAML parsing error.
**Cause:** Frontmatter YAML is malformed.
**Fix:** Check for:
- Missing `---` delimiters (need one above and one below)
- Unquoted special characters in values (`:`, `#`, `{`, `}`, `[`, `]`, `,`, `&`, `*`, `?`, `|`, `-`, `<`, `>`, `=`, `!`, `%`, `@`, `` ` ``)
- Improper indentation (YAML is indent-sensitive)
- XML angle brackets (`<`, `>`) in description — these are not allowed
- Tab characters instead of spaces

### Invalid skill name
**Symptom:** Upload rejected with name validation error.
**Cause:** Name violates naming rules.
**Fix:** Ensure the `name` field:
- Uses only lowercase letters, numbers, and hyphens (kebab-case)
- Does not contain "claude" or "anthropic"
- Matches the folder name exactly
- Does not start or end with a hyphen

## Skill Doesn't Trigger

### Description too generic
**Symptom:** Skill is never selected, even when you say the right things.
**Cause:** Description doesn't include specific trigger phrases that match what users say.
**Fix:**
1. Add explicit trigger phrases: `Use when the user says "phrase 1", "phrase 2", "phrase 3"`
2. Make the description more specific about what the skill does
3. Test by asking Claude: "When would you use the [skill-name] skill?"

### Missing trigger phrases
**Symptom:** Skill only triggers for some phrasings but not others.
**Cause:** Description only covers limited language patterns.
**Fix:** Add more diverse trigger phrases. Think about:
- Different verb forms: "create", "build", "make", "generate", "write"
- Different contexts: "I need a...", "Can you...", "Help me..."
- Abbreviated forms: "new component" vs "create a new React component"

### Competing with other skills
**Symptom:** A different skill gets selected instead.
**Cause:** Another skill's description is a better match for the trigger phrase.
**Fix:**
1. Make your description more specific to your use case
2. Add negative triggers to the competing skill if appropriate
3. Use more distinctive trigger phrases
4. Consider if the skills should be merged

## Skill Triggers Too Often

### Description too broad
**Symptom:** Skill activates for unrelated requests.
**Cause:** Description matches too many user inputs.
**Fix:**
1. Add negative triggers: `Do NOT use when the user asks about [unrelated thing]`
2. Narrow the scope: Instead of "helps with code" say "generates unit tests for React components"
3. Remove generic phrases from triggers
4. Clarify the specific domain: "Only use for [specific domain]"

### Overlapping with built-in capabilities
**Symptom:** Skill triggers when Claude should use its built-in behavior.
**Cause:** Skill description covers tasks Claude already handles well.
**Fix:**
1. Add negative triggers for built-in behaviors
2. Focus the skill on the specific value-add beyond built-in capabilities
3. Consider if the skill is even needed

## Instructions Not Followed

### Too verbose / buried instructions
**Symptom:** Claude follows some instructions but ignores others, especially later ones.
**Cause:** Important instructions are buried in long text. Claude pays more attention to earlier content.
**Fix:**
1. Move critical rules to `## Important` at the top
2. Use bullet points, not paragraphs
3. Keep SKILL.md under 5,000 words
4. Move detailed reference material to `references/` files

### Ambiguous instructions
**Symptom:** Claude interprets instructions differently than intended.
**Cause:** Instructions use vague language open to interpretation.
**Fix:**
1. Replace vague with specific:
   - "Handle errors" → "If the API returns 401, tell the user to check their API key"
   - "Create the file" → "Create a file at `src/utils/helpers.ts`"
   - "Test it" → "Run `npm test -- --coverage` and verify coverage exceeds 80%"
2. Include examples of expected behavior
3. Add "do NOT" instructions to block common misinterpretations

### Model laziness / skipping steps
**Symptom:** Claude abbreviates steps, uses placeholder comments, or skips validation.
**Cause:** Complex skills with many steps can trigger abbreviation behavior.
**Fix:**
1. Add explicit anti-laziness instructions:
   ```
   ## Performance Notes
   - Complete ALL steps. Do not skip or abbreviate.
   - Generate complete code. No placeholder comments.
   - Actually run validations. Do not assume they pass.
   ```
2. Use validation scripts instead of language instructions for critical checks
3. Add checkpoints: "After completing this step, confirm to the user what was done"

## MCP Connection Issues

### MCP server not connected
**Symptom:** Tools from an MCP server are not available.
**Fix:**
1. Have the skill check for MCP tool availability early in the workflow
2. Provide clear error message: "This skill requires the [name] MCP server. Please connect it in Settings > MCP Servers."
3. Suggest alternative approaches if the MCP server is optional

### Authentication failures
**Symptom:** MCP tool calls fail with auth errors.
**Fix:**
1. Include auth troubleshooting in the skill's error handling
2. Suggest checking API keys, tokens, or OAuth connections
3. Reference the specific MCP server's setup documentation

### Wrong tool names
**Symptom:** Skill references MCP tools that don't exist.
**Cause:** Tool names changed or are different than expected.
**Fix:**
1. Use exact tool names from the MCP server (they're usually prefixed: `mcp__servername__toolname`)
2. Test tool availability before using them
3. Add a note in `compatibility` field about required MCP server version

## Large Context Issues

### Skill uses too much context
**Symptom:** Claude runs out of context or becomes less effective when skill is active.
**Cause:** SKILL.md and referenced files are too large.
**Fix:**
1. Keep SKILL.md under 5,000 words
2. Only read reference files when specifically needed (not all at once)
3. Move rarely-needed information to reference files
4. Consider splitting into multiple focused skills
5. Remove redundant or repetitive content

### Too many skills enabled
**Symptom:** Claude's performance degrades or skills compete with each other.
**Cause:** Every enabled skill's description is loaded into context.
**Fix:**
1. Disable skills you're not currently using
2. Keep skill descriptions concise
3. Avoid overlapping skills that compete for the same triggers
