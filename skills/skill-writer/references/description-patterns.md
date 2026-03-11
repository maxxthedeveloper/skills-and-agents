# Description Patterns for Claude Code Skills

## The Formula

A great description follows this structure:

```
[What it does] + [When to use it / trigger phrases] + [Key capabilities if space allows]
```

The description is the single most important part of your skill. It determines whether Claude selects your skill for a given user request. A perfect skill with a bad description will never be used.

## Good Examples

### Example 1: Specific + Trigger-Rich
```
Generates comprehensive API documentation from source code. Use when the user says "document this API", "generate API docs", "write endpoint documentation", or "create API reference". Supports REST and GraphQL endpoints, includes request/response examples, and outputs OpenAPI-compatible markdown.
```
Why it works: States what it does, lists natural trigger phrases, mentions key capabilities.

### Example 2: Clear Scope + Negative Triggers
```
Scaffolds new React components with TypeScript, tests, and Storybook stories. Use when the user says "create a component", "new component", "scaffold component", or "component for [feature]". Do NOT use for refactoring existing components or for non-React frameworks.
```
Why it works: Clear scope, natural triggers, explicit boundaries to prevent over-triggering.

### Example 3: Workflow-Oriented
```
Interactive code review assistant that checks for bugs, performance issues, security vulnerabilities, and style violations. Use when the user says "review this code", "code review", "check this PR", "review my changes", or "find issues in this code". Provides actionable feedback with severity levels and fix suggestions.
```
Why it works: Describes the workflow, lists many trigger phrases, explains output format.

## Bad Examples

### Bad Example 1: Too Vague
```
Helps with documentation.
```
Why it fails: No trigger phrases, no specifics about what kind of documentation, competes with everything.

### Bad Example 2: Too Technical / No Triggers
```
Parses AST nodes using tree-sitter to extract function signatures and generate JSDoc annotations with parameter types inferred from TypeScript's type checker.
```
Why it fails: Describes implementation, not use cases. No trigger phrases. A user would never say "parse AST nodes."

### Bad Example 3: Too Long / Kitchen Sink
```
A comprehensive tool that does code review, documentation generation, test writing, refactoring suggestions, performance optimization, security auditing, accessibility checking, SEO improvements, database query optimization, API design review, and more. Use for anything code-related.
```
Why it fails: Does too much, triggers on everything, provides no clear signal for when to use it.

## Tips for Writing Descriptions

### Include Natural Trigger Phrases
Think about what a user would actually type. Not "invoke documentation generation" but "write docs for this" or "document this function."

List 3-6 trigger phrases using the pattern: `Use when the user says "phrase 1", "phrase 2", "phrase 3", or "phrase 4".`

### Use Negative Triggers to Prevent Over-Triggering
If your skill might match too broadly, add explicit exclusions:
- `Do NOT use when the user asks about [related but different thing].`
- `Do NOT use for [out-of-scope task].`
- `Only use when [specific condition].`

### Keep It Under 1,024 Characters
This is a hard limit. If you can't fit everything, prioritize:
1. What it does (required)
2. Trigger phrases (required)
3. Negative triggers (if needed)
4. Key capabilities (nice to have)

### Test Your Description
Ask yourself: "If a user said '[trigger phrase]', would Claude pick this skill over all other enabled skills?"

Debug by asking Claude directly: "When would you use the [skill-name] skill?" If the answer doesn't match your intent, revise the description.

## Description Templates

### For Document/Asset Creation Skills
```
Creates [output type] from [input]. Use when the user says "[trigger 1]", "[trigger 2]", or "[trigger 3]". Outputs [format] with [key features].
```

### For Workflow Automation Skills
```
[Action verb] workflow for [domain]. Use when the user says "[trigger 1]", "[trigger 2]", or "[trigger 3]". Steps through [key phases] with [validation/output].
```

### For MCP Enhancement Skills
```
Coordinates [MCP tools] to [achieve goal]. Use when the user says "[trigger 1]", "[trigger 2]", or "[trigger 3]". Requires [MCP server]. Do NOT use for [out-of-scope].
```
