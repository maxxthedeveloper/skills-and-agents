---
name: systematic-debugging
description: Structured debugging methodology for investigating and fixing bugs. Use when debugging errors, investigating failures, or fixing bugs. Enforces root cause investigation before fixing and prevents shotgun debugging.
---

# Systematic Debugging Methodology

## Core Principle

**Never fix problems solely where errors appear—always trace to the original trigger.**

If THREE or more fix attempts fail consecutively, STOP. This signals architectural problems requiring discussion, not more patches.

## The Four-Phase Framework

### Phase 1: Root Cause Investigation

Before attempting ANY fix:

1. **Read the error carefully**
   - What is the actual error message?
   - Where does the stack trace point?
   - What is the trigger condition?

2. **Reproduce the issue**
   - Can you consistently trigger the bug?
   - What are the exact steps?
   - What input causes the failure?

3. **Trace data flow backward**
   - Where does the problematic data come from?
   - What transforms it along the way?
   - Where is the FIRST point of corruption?

4. **Document your findings**
   ```
   ERROR: [exact error message]
   TRIGGER: [what causes it]
   LOCATION: [where it fails]
   ROOT CAUSE: [where the problem originates]
   ```

### Phase 2: Pattern Analysis

Compare broken implementation against working examples:

1. Find similar working code in the codebase
2. Identify specific differences
3. Note dependencies and assumptions
4. Check recent changes to the affected area

Questions to ask:
- What changed recently that could cause this?
- Does this work in other contexts?
- What assumptions is the code making?

### Phase 3: Hypothesis and Testing

Apply scientific methodology:

1. **Form ONE clear hypothesis**
   - "The bug occurs because X is null when it should be Y"
   - Be specific—vague hypotheses lead to vague fixes

2. **Design a minimal test**
   - Write a failing test that demonstrates the bug
   - The test should pass when the bug is fixed
   - Keep the test focused on the specific issue

3. **Predict the outcome**
   - What do you expect to happen when you apply the fix?
   - How will you verify it worked?

4. **Iterate based on results**
   - If hypothesis was wrong, update understanding
   - Return to Phase 1 if needed

### Phase 4: Implementation

Only after completing Phases 1-3:

1. **Write a failing test case**
   ```typescript
   it('should handle null input gracefully', () => {
     expect(() => processInput(null)).not.toThrow();
     expect(processInput(null)).toBe('');
   });
   ```

2. **Implement the targeted fix**
   - Fix should address root cause, not symptom
   - Change should be minimal and focused
   - Avoid "while I'm here" cleanup

3. **Verify the fix**
   - Test passes
   - No new test failures
   - Manual verification if needed

4. **Run full test suite**
   - Catch potential regressions
   - Ensure fix doesn't break other areas

## Red Flags - STOP If You See These

- [ ] Attempting quick fix without understanding the issue
- [ ] Multiple failed fix attempts (3+ consecutive failures)
- [ ] Fix addresses symptom but not cause
- [ ] "I'm not sure why this works but it does"
- [ ] Changing code you don't fully understand

## Anti-Patterns to Avoid

### Shotgun Debugging
Trying random fixes hoping one works.
**Instead**: Investigate first, fix second.

### Symptom-Based Fixing
Adding null checks without understanding why null appears.
**Instead**: Trace the source of null values.

### Scope Creep
"While I'm here, let me also fix X, Y, Z..."
**Instead**: One bug, one fix, one commit.

### Untested Fixes
Deploying fixes without verification.
**Instead**: Write test first, then fix, then verify.

## Output Format

When debugging, always document:

```markdown
## Bug Investigation

### Error Details
- Error: [message]
- Location: [file:line]
- Trigger: [conditions]

### Root Cause Analysis
[Investigation findings]

### Hypothesis
[Your theory about the cause]

### Test Case
[Failing test that proves the bug]

### Fix
[The actual code change]

### Verification
[How you confirmed the fix works]
```

## Integration with Testing

After fixing a bug:
1. The test you wrote should now pass
2. All other tests should still pass
3. Consider adding edge case tests
4. Document the fix for future reference
