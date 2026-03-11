# Skill Patterns

Five proven patterns for structuring Claude Code skills. Choose the one that best fits your use case.

## 1. Sequential Workflow Orchestration

**Use when:** The task follows a predictable series of steps where each step depends on the previous one.

**Examples:** Code scaffolding, migration workflows, release processes, document generation.

**Structure:**
```markdown
## Workflow

### Step 1: Gather Requirements
- Ask the user for [specific inputs]
- Validate inputs: [specific checks]
- If invalid, explain what's wrong and ask again

### Step 2: [Prepare/Analyze]
- Read [specific files/context]
- Determine [decisions based on context]
- **Gate:** Confirm approach with user before proceeding

### Step 3: [Generate/Execute]
- Perform the main action
- [Specific sub-steps]

### Step 4: [Validate]
- Run [specific validation]
- If issues found, fix and re-validate
- Present results to user
```

**Key characteristics:**
- Numbered steps with clear ordering
- Validation gates between major steps
- User confirmation at decision points
- Each step has specific, verifiable outputs

## 2. Multi-MCP Coordination

**Use when:** The skill needs to orchestrate multiple MCP tools together to accomplish a goal.

**Examples:** PR review (GitHub + Linear), deployment (Vercel + Slack), data pipeline (DB + API + notification).

**Structure:**
```markdown
## Important

- Requires [MCP server 1] and [MCP server 2] to be connected
- If an MCP server is not available, inform the user and suggest alternatives

## Workflow

### Step 1: Verify MCP Connections
- Check that [MCP server 1] is accessible by calling [simple test tool]
- Check that [MCP server 2] is accessible by calling [simple test tool]
- If either fails, stop and inform the user

### Step 2: Gather Data from [Source 1]
- Use [mcp_tool_1] to fetch [data]
- Extract [specific fields]

### Step 3: Process and Transform
- Transform the data for [destination format]
- [Specific transformation logic]

### Step 4: Push to [Destination]
- Use [mcp_tool_2] to send [transformed data]
- Verify the operation succeeded

### Step 5: Confirm and Notify
- Use [mcp_tool_3] to send confirmation (if applicable)
- Present summary to user
```

**Key characteristics:**
- Upfront MCP connection verification
- Clear data flow between MCP tools
- Fallback behavior when tools are unavailable
- Explicit tool names (not generic references)

## 3. Iterative Refinement

**Use when:** The output needs multiple rounds of improvement, or quality is assessed against specific criteria.

**Examples:** Code review, content writing, design iteration, test improvement.

**Structure:**
```markdown
## Workflow

### Step 1: Produce Initial Output
- Generate the first version of [output]
- Base it on [specific inputs/context]

### Step 2: Evaluate Against Criteria
Check the output against these criteria:
- [ ] [Criterion 1]: [specific check]
- [ ] [Criterion 2]: [specific check]
- [ ] [Criterion 3]: [specific check]
- [ ] [Criterion 4]: [specific check]

### Step 3: Refine
- For each failed criterion, make specific improvements
- Do not change aspects that already pass

### Step 4: Re-evaluate
- Run the criteria check again
- If all pass, proceed to Step 5
- If still failing after 3 iterations, present current state and ask user for guidance

### Step 5: Present Final Output
- Show the final version
- List which criteria pass/fail
- Note any trade-offs made
```

**Key characteristics:**
- Explicit quality criteria (checklist)
- Bounded iteration (max attempts)
- Targeted refinement (don't change what works)
- Escape hatch when iteration isn't converging

## 4. Context-Aware Tool Selection

**Use when:** The skill needs to choose different tools or approaches based on the user's environment or context.

**Examples:** Package management (npm vs yarn vs pnpm), testing (Jest vs Vitest vs Mocha), deployment (Vercel vs AWS vs Netlify).

**Structure:**
```markdown
## Workflow

### Step 1: Detect Context
Read the following to determine the environment:
- `package.json` — check for package manager, test framework, build tools
- `.github/workflows/` — check for CI configuration
- `tsconfig.json` — check for TypeScript settings
- [Other context-specific files]

### Step 2: Select Approach
Based on detected context:

**If [condition A]:**
- Use [tool/approach A]
- [Specific instructions for A]

**If [condition B]:**
- Use [tool/approach B]
- [Specific instructions for B]

**If [condition C] or context is unclear:**
- Ask the user which approach they prefer
- Default to [safest option] if no preference

### Step 3: Execute
- Follow the selected approach
- [Common steps regardless of approach]

### Step 4: Verify
- Run [approach-specific validation]
- Confirm output matches expected format
```

**Key characteristics:**
- Explicit context detection steps (read specific files)
- Decision tree with clear conditions
- Fallback to user input when ambiguous
- Approach-specific instructions for each branch

## 5. Domain-Specific Intelligence

**Use when:** The skill encodes expert knowledge about a specific domain (e.g., accessibility, security, database design).

**Examples:** Security audit, accessibility review, database schema design, API design review.

**Structure:**
```markdown
# [Domain] Expert

You are an expert in [domain] with deep knowledge of [specific areas].

## Important

- [Critical domain rules that must never be violated]
- [Common mistakes to always check for]

## Knowledge Base

Read `references/[domain]-rules.md` for the complete rule set.

Key principles:
1. [Principle 1] — [brief explanation]
2. [Principle 2] — [brief explanation]
3. [Principle 3] — [brief explanation]

## Workflow

### Step 1: Analyze
- Read the relevant code/files
- Identify [domain-specific concerns]
- Categorize findings by severity: Critical / Warning / Info

### Step 2: Report
For each finding:
- **Location:** file:line_number
- **Severity:** Critical / Warning / Info
- **Issue:** What's wrong
- **Why it matters:** Impact in [domain] terms
- **Fix:** Specific code change to resolve it

### Step 3: Prioritize
- Present Critical issues first
- Group related issues together
- Offer to fix issues automatically (with user approval)

## Common Patterns

### [Pattern 1 Name]
- **Detect:** [how to identify this pattern]
- **Issue:** [what's wrong with it]
- **Fix:** [specific solution]

### [Pattern 2 Name]
...
```

**Key characteristics:**
- Strong role/identity statement
- Reference files for deep domain knowledge
- Severity-based categorization
- Specific patterns with detect/issue/fix structure
- Expert framing (not generic assistant)

## Choosing the Right Pattern

| Pattern | Best For | Key Signal |
|---------|----------|------------|
| Sequential Workflow | Step-by-step processes | "First do X, then Y, then Z" |
| Multi-MCP Coordination | Cross-tool orchestration | "Get data from A, send to B" |
| Iterative Refinement | Quality-focused output | "Make it better until it meets criteria" |
| Context-Aware Tool Selection | Environment-dependent tasks | "Use the right tool for their setup" |
| Domain-Specific Intelligence | Expert knowledge application | "Apply [domain] best practices" |

You can combine patterns. For example, a Sequential Workflow might include Context-Aware Tool Selection in one of its steps, or a Domain-Specific Intelligence skill might use Iterative Refinement for its analysis.
