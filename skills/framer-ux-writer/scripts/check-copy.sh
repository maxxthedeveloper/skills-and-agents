#!/bin/bash
# Deterministic mechanics check for Framer UX copy drafts.
# Usage: check-copy.sh <file-with-strings>   (or pipe strings on stdin, one per line)
# Checks displayed-copy rules only — don't feed it code identifiers or translation keys.
# Reports every hit with a line number; exits 1 if anything fails. Judgment items stay manual.

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

report "straight apostrophe (use ’)" "[a-zA-Z]'[a-zA-Z]"
report 'straight double quote (use “ ”)' '"'
report "double hyphen (use — or –)" '\-\-'
report "exclamation mark" '!'
report "three-dot ellipsis (use …)" '\.\.\.'
report "banned word (see framer-voice.md)" '\b(easy|simple|just|simply|oops|uh-oh|awesome|amazing|incredible|powerful|revolutionary|leverage|utilize|seamless)\b' "-inE"
report "Error: prefix" '\bError:' "-nE"
report "first-person system voice (no we/us/our; see mechanics.md — pronouns)" "\b(we('|’)?(re|ve|ll)?|us|our)\b" "-inE"

# AI-giveaway constructions (catalog: references/ai-tells.md)
report "negation-pivot / contrast frame" "(not (just|only) |isn.t (just|about) |not because|say (goodbye|hello) to|s not [^.!?]*— ?it.s)" "-inE"
report "participial benefit tail (…, ensuring X)" ", (ensuring|empowering|enabling|allowing you|highlighting|underscoring|showcasing|emphasizing|reflecting|demonstrating|fostering|elevating)\b" "-inE"
report "staccato stack (No X. No Y.)" "no [a-z]+\. no [a-z]+" "-inE"
report "self-answering question (The result? Y.)" "the (result|best part|kicker|upshot)\?" "-inE"
report "performed casualness" "(here.s the kicker|let.s be (real|honest)|no fluff|wild ride|chef.s kiss|at your fingertips|think of it as|in your pocket|whether you.re a)" "-inE"
report "hollow significance" "(plays a (vital|crucial|pivotal|key) role|stands as|serves as|testament to|marking a (pivotal|significant|new)|in today.s|fast.paced)" "-inE"
report "AI-register word (see ai-tells.md)" '\b(delve|delving|tapestry|testament|realm|elevate|supercharge|effortless(ly)?|game.chang(er|ing)|cutting.edge|robust|harness|empower(s|ing|ed)?|streamlin(e|es|ing|ed)|transformative|revolutionize|boasts?|showcasing|underscor(e|es|ing)|enhanc(e|es|ed|ing)|paradigm|synergy)\b' "-inE"
report "two em dashes in one string" '—[^.!?]*—'

EMOJI=$(printf '%s\n' "$DRAFT" | perl -CSD -ne 'print "$.:$_" if /[\x{1F000}-\x{1FAFF}\x{2600}-\x{27BF}\x{2B00}-\x{2BFF}\x{FE0F}]/' || true)
if [ -n "$EMOJI" ]; then
  FAIL=1
  echo "FAIL: emoji"
  echo "$EMOJI" | sed 's/^/  /'
  echo
fi

if [ "$FAIL" -eq 0 ]; then
  echo "PASS: mechanics clean (balance, casing, and voice items still manual)"
fi
exit $FAIL
