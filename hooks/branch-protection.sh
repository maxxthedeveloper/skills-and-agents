#!/bin/bash
# Branch protection hook - blocks edits on main/master branch
# Usage: Called by Claude Code as a PreToolUse hook for Edit/Write tools

# Get the current branch (if in a git repo)
current_branch=$(git rev-parse --abbrev-ref HEAD 2>/dev/null)

# Check if we're on a protected branch
if [[ "$current_branch" == "main" || "$current_branch" == "master" ]]; then
  echo '{"decision": "block", "reason": "Cannot edit files on main/master branch. Create a feature branch first with: git checkout -b feature/your-feature-name"}'
  exit 0
fi

# Allow the operation
echo '{"decision": "allow"}'
exit 0
