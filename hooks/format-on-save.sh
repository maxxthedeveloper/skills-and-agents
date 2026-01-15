#!/bin/bash
# Auto-format TypeScript/JavaScript files after edit
# Called by Claude Code as a PostToolUse hook

FILE_PATH="$1"

# Only run on JS/TS files
if [[ ! "$FILE_PATH" =~ \.(js|jsx|ts|tsx)$ ]]; then
  exit 0
fi

# Check if prettier is available
if command -v npx &> /dev/null; then
  npx prettier --write "$FILE_PATH" 2>/dev/null
  if [ $? -eq 0 ]; then
    echo "Formatted: $FILE_PATH"
  fi
fi

exit 0
