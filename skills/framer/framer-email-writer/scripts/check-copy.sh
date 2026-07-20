#!/bin/bash
# Deterministic mechanics check for Framer email drafts.
# Usage: check-copy.sh <draft-file>   (or pipe the draft on stdin)
# Reports every hit with a line number; exits 1 if anything fails.
# Judgment calls (balanced lines, blameless framing, calibration) stay manual.

set -u
INPUT="${1:-/dev/stdin}"
DRAFT="$(cat "$INPUT")"
FAIL=0

report() { # label, grep-pattern, [grep-flags]
  local label="$1" pattern="$2" flags="${3:--nE}"
  local hits
  hits=$(printf '%s\n' "$DRAFT" | grep $flags "$pattern" || true)
  if [ -n "$hits" ]; then
    FAIL=1
    echo "FAIL: $label"
    echo "$hits" | sed 's/^/  /'
    echo
  fi
}

# Straight quotes in displayed copy (curly ‘ ’ “ ” required) — zero tolerance.
# Flag EVERY straight single quote, not just mid-word ones: word-boundary cases
# (designers’, ’twas, ’26) and quotation marks are just as wrong. LMX attributes
# (href="…") and code use straight quotes legitimately — judge hits inside tags.
report "straight single quote (use ’ or ‘)" "'"
report 'straight double quote (use “ ”)' '"'
# Double hyphen instead of em/en dash
report "double hyphen (use — or –)" '\-\-'
# Exclamation marks
report "exclamation mark" '!'
# Ellipsis as three dots
report "three-dot ellipsis (use …)" '\.\.\.'
# Emoji (common ranges) — perl for unicode ranges; macOS grep has no -P
EMOJI=$(printf '%s\n' "$DRAFT" | perl -CSD -ne 'print "$.:$_" if /[\x{1F000}-\x{1FAFF}\x{2600}-\x{27BF}\x{2B00}-\x{2BFF}\x{FE0F}]/' || true)
if [ -n "$EMOJI" ]; then
  FAIL=1
  echo "FAIL: emoji"
  echo "$EMOJI" | sed 's/^/  /'
  echo
fi
# Banned words (canonical list: references/email-voice.md)
report "banned word" '\b(easy|simple|just|simply|oops|uh-oh|awesome|amazing|incredible|powerful|revolutionary|leverage|utilize|seamless)\b' "-inE"
report "banned phrase" "(we.re (excited|thrilled)|exciting news|don.t miss out|act now)" "-inE"

# AI-giveaway constructions (catalog: references/ai-tells.md)
report "negation-pivot / contrast frame" "(not (just|only) |isn.t (just|about) |not because|say (goodbye|hello) to|s not [^.!?]*— ?it.s)" "-inE"
report "participial benefit tail (…, ensuring X)" ", (ensuring|empowering|enabling|allowing you|highlighting|underscoring|showcasing|emphasizing|reflecting|demonstrating|fostering|elevating)\b" "-inE"
report "staccato stack (No X. No Y.)" "no [a-z]+\. no [a-z]+" "-inE"
report "self-answering question (The result? Y.)" "the (result|best part|kicker|upshot)\?" "-inE"
report "performed casualness" "(here.s the kicker|let.s be (real|honest)|no fluff|wild ride|chef.s kiss|at your fingertips|think of it as|in your pocket|whether you.re a)" "-inE"
report "hollow significance" "(plays a (vital|crucial|pivotal|key) role|stands as|serves as|testament to|marking a (pivotal|significant|new)|in today.s|fast.paced)" "-inE"
report "AI-register word (see ai-tells.md)" '\b(delve|delving|tapestry|testament|realm|elevate|supercharge|effortless(ly)?|game.chang(er|ing)|cutting.edge|robust|harness|empower(s|ing|ed)?|streamlin(e|es|ing|ed)|transformative|revolutionize|boasts?|showcasing|underscor(e|es|ing)|enhanc(e|es|ed|ing)|paradigm|synergy)\b' "-inE"

# Em-dash checks: max 2 per email, never 2 in one sentence (house style keeps em dashes; density is the tell).
# Spec scaffolding ("Send as: Campaign — audience: …") is excluded from both.
COPY=$(printf '%s\n' "$DRAFT" | grep -v '^Send as:')
TWODASH=$(printf '%s\n' "$COPY" | grep -nE '—[^.!?]*—' || true)
if [ -n "$TWODASH" ]; then
  FAIL=1
  echo "FAIL: two em dashes in one sentence"
  echo "$TWODASH" | sed 's/^/  /'
  echo
fi
EMDASH_COUNT=$(printf '%s\n' "$COPY" | grep -o '—' | wc -l | tr -d ' ')
if [ "$EMDASH_COUNT" -gt 2 ]; then
  FAIL=1
  echo "FAIL: em-dash density ($EMDASH_COUNT em dashes; max 2 per email)"
  echo
fi

# Subject length: a line "Subject: ..." over 60 chars of content
SUBJ=$(printf '%s\n' "$DRAFT" | grep -nE '^Subject:' || true)
if [ -n "$SUBJ" ]; then
  while IFS= read -r line; do
    content=$(echo "$line" | sed -E 's/^[0-9]+:Subject:[[:space:]]*//')
    len=${#content}
    if [ "$len" -gt 60 ]; then
      FAIL=1
      echo "FAIL: subject over 60 chars ($len): $content"
      echo
    fi
  done <<< "$SUBJ"
fi

if [ "$FAIL" -eq 0 ]; then
  echo "PASS: mechanics clean (judgment items still manual)"
fi
exit $FAIL
