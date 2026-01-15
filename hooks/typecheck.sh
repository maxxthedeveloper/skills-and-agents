#!/bin/bash
# Type check TypeScript files after edit
# Called by Claude Code as a PostToolUse hook

FILE_PATH="$1"

# Only run on TypeScript files
if [[ ! "$FILE_PATH" =~ \.tsx?$ ]]; then
  exit 0
fi

# Find the nearest tsconfig.json
DIR=$(dirname "$FILE_PATH")
while [[ "$DIR" != "/" ]]; do
  if [[ -f "$DIR/tsconfig.json" ]]; then
    cd "$DIR"
    npx tsc --noEmit 2>&1
    exit $?
  fi
  DIR=$(dirname "$DIR")
done

exit 0
