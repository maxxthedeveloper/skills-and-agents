# Test: PostToolUse Code Quality Hooks - AFTER

## Test Date
2026-01-15

## New Configuration
Added PostToolUse hooks for formatting and type checking.

```json
// Updated settings.json - hooks section
"hooks": {
  "Notification": [...],
  "PreToolUse": [...],
  "PostToolUse": [
    {
      "matcher": "Edit|Write",
      "hooks": [
        {
          "type": "command",
          "command": "/Users/maxx/.claude/hooks/format-on-save.sh \"$CLAUDE_FILE_PATH\"",
          "timeout": 10000
        }
      ]
    },
    {
      "matcher": "Edit|Write",
      "hooks": [
        {
          "type": "command",
          "command": "/Users/maxx/.claude/hooks/typecheck.sh \"$CLAUDE_FILE_PATH\"",
          "timeout": 30000
        }
      ]
    }
  ]
}
```

## Hook Scripts
- `/Users/maxx/.claude/hooks/format-on-save.sh` - Auto-formats JS/TS files with Prettier
- `/Users/maxx/.claude/hooks/typecheck.sh` - Runs TypeScript type checking

## Test Prompt
"Fix the typo in src/index.ts - change 'Helo World' to 'Hello World'"

## Expected Behavior (With Hooks)
1. Claude edits the file
2. PostToolUse hook triggers automatically
3. Prettier formats the file (consistent style)
4. TypeScript compiler checks for type errors
5. Any issues are reported back to Claude
6. Code quality is enforced without manual intervention

## Simulated Workflow
```
[Claude edits src/index.ts]
  |
  v
[PostToolUse: format-on-save.sh runs]
  -> "Formatted: src/index.ts"
  |
  v
[PostToolUse: typecheck.sh runs]
  -> No errors (or reports type issues)
  |
  v
[Edit complete with quality gates passed]
```

## Impact Assessment

### Benefits
- **Automatic Formatting**: Consistent code style across all edits
- **Type Safety**: Immediate feedback on type errors
- **Developer Experience**: No manual quality checks needed
- **Code Review**: Cleaner diffs, fewer style discussions

### Considerations
- **Performance**: Adds ~1-2s to each edit operation
- **Dependencies**: Requires Prettier and TypeScript in project
- **Timeout**: May need adjustment for large projects

## Trade-offs
- Slight slowdown on each edit (formatting + type check)
- Requires project to have Prettier/TSC configured
- May surface many existing issues in legacy code

## Conclusion
**Recommendation: IMPLEMENT WITH CAUTION**

This is a high-value addition but should be configured per-project. Consider:
1. Making hooks project-aware (check for package.json presence)
2. Using `onSuccess: "suppress"` to hide successful runs
3. Using `onFailure: "feedback"` for type errors
4. Adding timeout configuration for larger projects

For global settings, recommend a lighter version that only runs on explicit request.
