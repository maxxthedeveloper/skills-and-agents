# Test: Systematic Debugging Skill - BEFORE

## Test Date
2026-01-15

## Current Configuration
No debugging methodology skill defined.

## Test Scenario
User reports a bug: "The processInput function crashes when passed null"

## Test File
```typescript
// src/index.ts
export function processInput(input: string) {
  const trimmed = input.trim();  // Crashes here on null
  return trimmed.toLowerCase();
}
```

## Test Prompt
"Debug why the processInput function crashes when passed null"

## Expected Behavior (Without Skill)
Typical ad-hoc debugging approach:
1. Look at the error
2. Immediately add a null check
3. If that doesn't work, try another quick fix
4. Repeat until something works

## Simulated Response Without Skill
```
Looking at processInput, I can see the issue - it's calling .trim() on null.
Let me fix it by adding a null check:

export function processInput(input: string) {
  if (!input) return '';  // Quick fix
  const trimmed = input.trim();
  return trimmed.toLowerCase();
}
```

## Issues With Ad-Hoc Approach
1. **No root cause investigation**: Jumped straight to a fix
2. **No hypothesis**: Didn't verify the actual error
3. **No test first**: No failing test to prove the bug exists
4. **Potential regression**: The fix might have unintended consequences
5. **Incomplete solution**: Didn't consider undefined, empty string, etc.

## Risk Assessment
- **Medium Risk**: Quick fixes often address symptoms, not causes
- **Issue**: May introduce new bugs or mask deeper issues
- **Impact**: Recurring similar bugs, technical debt

## What Showcase Has
A systematic-debugging skill that enforces:
1. Root cause investigation BEFORE fixing
2. Hypothesis formation and testing
3. Write failing test first
4. Maximum 3 fix attempts before stopping
5. Pattern analysis comparing broken vs working code
