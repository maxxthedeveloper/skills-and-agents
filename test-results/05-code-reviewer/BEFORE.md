# Test: Code Reviewer Agent - BEFORE

## Test Date
2026-01-15

## Current Configuration
No dedicated code review agent.

## Test Scenario
User asks for a code review of recent changes.

## Test Code to Review
```typescript
// src/components/DeleteButton.tsx
export function DeleteButton({ onDelete, item }) {
  const handleClick = () => {
    onDelete(item.id);
  };

  return (
    <button onClick={handleClick}>
      Delete
    </button>
  );
}
```

## Test Prompt
"Review this code for issues"

## Expected Behavior (Without Agent)
Generic review without structured checklist:
- May miss critical issues
- Inconsistent feedback format
- No prioritization of issues
- No specific standards applied

## Simulated Response Without Agent
```
Looking at the code, I notice:
- The props should have TypeScript types
- Consider adding a confirmation before delete
- Maybe add some styling
```

## Issues With Ad-Hoc Review
1. **No prioritization**: Critical vs nice-to-have not distinguished
2. **Missing checks**: No security, accessibility, or state handling review
3. **Inconsistent format**: Each review structured differently
4. **No checklist**: Easy to miss common issues
5. **Vague feedback**: "Consider" doesn't give clear guidance

## What We Want
A code reviewer agent that:
- Uses a consistent checklist
- Prioritizes issues (Critical > Warning > Suggestion)
- Checks TypeScript, accessibility, state handling, tests
- Provides specific, actionable feedback
- Follows established coding standards
