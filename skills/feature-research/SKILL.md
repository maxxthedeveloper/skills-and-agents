---
name: feature-research
description: Research best practices, evaluate technical approaches, and make informed decisions before implementing new features. Use this skill when the user needs to research libraries, frameworks, design patterns, API integrations, authentication strategies, state management, database choices, or any technical decision that benefits from understanding current industry standards and tradeoffs. Triggers on: "should I use", "which library", "best approach for", "how should I implement", "what's the best way to", "compare X vs Y", "evaluate options for", "research", "tradeoffs", "pros and cons", architecture decisions, technology selection, stack choices, migration planning, performance strategy, scaling decisions.
---

# Feature Research

A structured methodology for researching and evaluating technical approaches before writing code. Prevents premature implementation by ensuring decisions are informed by current best practices, real-world tradeoffs, and project-specific constraints.

## When to Use This Skill

Use this skill when the user:

- Needs to choose between libraries, frameworks, or tools
- Is planning a new feature and wants to evaluate approaches
- Asks "should I use X or Y?"
- Needs to understand tradeoffs before committing to an architecture
- Is considering a migration or technology change
- Wants to understand current best practices for a specific problem domain

## Research Process

Follow this structured process for every research task:

### Step 1: Define the Decision

Before researching, clarify exactly what needs to be decided:

- What is the specific technical decision?
- What are the constraints (budget, timeline, team expertise, existing stack)?
- What are the non-negotiable requirements vs. nice-to-haves?
- What scale does this need to support (users, data volume, request rate)?

Ask the user clarifying questions if any of these are unclear. Do not proceed with vague requirements.

### Step 2: Identify Candidates

List 2-4 realistic options. For each candidate, gather:

- **What it is**: One-sentence description
- **Adoption**: GitHub stars, npm weekly downloads, last release date
- **Maintenance**: Active maintainers, release frequency, open issue count
- **Ecosystem**: Integration with the user's existing stack

Do not include options that are clearly unsuitable for the constraints identified in Step 1.

### Step 3: Evaluate Against Criteria

Use this evaluation framework, adapting criteria to the specific decision:

| Criteria | Weight | Option A | Option B | Option C |
|---|---|---|---|---|
| Fits existing stack | High | | | |
| Learning curve | Medium | | | |
| Performance | Varies | | | |
| Bundle size / overhead | Varies | | | |
| Community & docs | Medium | | | |
| Long-term maintenance | High | | | |
| Type safety | Varies | | | |

Rate each option: Strong, Good, Acceptable, Weak.

Adjust weights based on the user's specific constraints. Not every criterion matters equally for every decision.

### Step 4: Identify Risks

For each viable option, identify:

- **Migration risk**: How hard is it to switch away later?
- **Scaling risk**: Where will this break under growth?
- **Maintenance risk**: What happens if the project loses maintainers?
- **Integration risk**: What could go wrong with the existing stack?

### Step 5: Make a Recommendation

Provide a clear recommendation with reasoning:

```
Recommendation: [Option]
Confidence: [High/Medium/Low]
Reasoning: [2-3 sentences explaining why]
Risks to monitor: [Key risks to watch]
```

If confidence is Low, explain what additional information would increase it.

## Output Format

Present research findings in this structure:

```markdown
## Research: [Decision Title]

### Context
[What we're deciding and why]

### Constraints
- [Constraint 1]
- [Constraint 2]

### Options Evaluated

#### Option A: [Name]
- **What**: [Description]
- **Strengths**: [Key advantages]
- **Weaknesses**: [Key disadvantages]
- **Best for**: [When to choose this]

#### Option B: [Name]
[Same structure]

### Comparison

| Criteria | Option A | Option B |
|---|---|---|
| [Criterion] | [Rating] | [Rating] |

### Recommendation
[Clear recommendation with reasoning]

### Next Steps
- [Concrete action item 1]
- [Concrete action item 2]
```

## Research Principles

1. **Prefer boring technology.** Well-established solutions with known tradeoffs beat cutting-edge options with unknown failure modes. Only recommend newer tools when they solve a specific problem the established options cannot.

2. **Optimize for the team.** The best technical choice is the one the team can execute well. A "worse" technology that the team knows deeply often outperforms a "better" one they're learning.

3. **Consider the exit cost.** Every technology choice has a switching cost. Favor options that are either (a) easy to migrate away from, or (b) so well-established that migration is unlikely to be needed.

4. **Separate fact from opinion.** Clearly distinguish between objective measurements (benchmarks, bundle sizes, API surface) and subjective assessments (developer experience, code readability).

5. **Check recency.** The ecosystem moves fast. Verify that benchmarks, recommendations, and comparisons are from the last 12 months. Flag any older sources.

6. **Scope the research.** Don't boil the ocean. Spend research effort proportional to the decision's impact and reversibility. A state management choice for a core app deserves more research than picking a date formatting library.

## Common Research Areas

### Libraries & Packages
- Check npm trends, GitHub activity, and release history
- Read the "Why not X?" sections in competitor docs
- Look for migration guides (indicates maturity)
- Check TypeScript support quality (not just "has types")

### Architecture Patterns
- Look for production case studies, not just tutorials
- Evaluate complexity vs. the actual problem size
- Consider what happens when requirements change
- Check if the pattern is well-supported by the framework

### API & Integration Design
- Review the provider's status page history and uptime
- Check rate limits, pricing tiers, and usage caps
- Look for official SDKs vs. community wrappers
- Evaluate authentication complexity and security model

### Performance Decisions
- Require actual benchmarks, not theoretical advantages
- Test with realistic data volumes, not toy examples
- Consider cold start, p99 latency, not just averages
- Factor in developer productivity, not just runtime speed
