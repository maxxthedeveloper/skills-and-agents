#!/usr/bin/env python3
"""
Compare original and rewritten text. Flag if change percentage is <40% or >85%.

Usage:
    python3 diff_check.py original.txt rewritten.txt
"""

import re
import json
import sys
import difflib


def tokenize(text):
    """Split text into words for comparison."""
    return re.findall(r'\S+', text.strip())


def compute_change_percentage(original, rewritten):
    """Compute what percentage of the text changed using SequenceMatcher."""
    orig_tokens = tokenize(original)
    new_tokens = tokenize(rewritten)

    if not orig_tokens and not new_tokens:
        return 0.0

    matcher = difflib.SequenceMatcher(None, orig_tokens, new_tokens)
    similarity = matcher.ratio()
    change_pct = (1 - similarity) * 100

    return round(change_pct, 1)


def compute_line_diff(original, rewritten):
    """Generate a human-readable line diff summary."""
    orig_lines = original.strip().splitlines()
    new_lines = rewritten.strip().splitlines()

    differ = difflib.unified_diff(orig_lines, new_lines,
                                   fromfile='original', tofile='rewritten',
                                   lineterm='')

    diff_lines = list(differ)
    added = sum(1 for l in diff_lines if l.startswith('+') and not l.startswith('+++'))
    removed = sum(1 for l in diff_lines if l.startswith('-') and not l.startswith('---'))

    return {
        'lines_added': added,
        'lines_removed': removed,
        'diff_line_count': len(diff_lines),
    }


def main():
    if len(sys.argv) < 3:
        print("Usage: python3 diff_check.py original.txt rewritten.txt")
        sys.exit(2)

    with open(sys.argv[1], 'r') as f:
        original = f.read()
    with open(sys.argv[2], 'r') as f:
        rewritten = f.read()

    change_pct = compute_change_percentage(original, rewritten)
    line_diff = compute_line_diff(original, rewritten)

    # Determine status
    if change_pct < 40:
        status = 'FAIL'
        reason = f'Too few changes ({change_pct}% < 40%). The rewrite is too close to the original.'
    elif change_pct > 85:
        status = 'FAIL'
        reason = f'Too many changes ({change_pct}% > 85%). The rewrite may have lost the original meaning.'
    else:
        status = 'PASS'
        reason = f'Change percentage {change_pct}% is within the 40-85% acceptable range.'

    result = {
        'status': status,
        'change_percentage': change_pct,
        'acceptable_range': '40-85%',
        'reason': reason,
        'word_counts': {
            'original': len(tokenize(original)),
            'rewritten': len(tokenize(rewritten)),
        },
        'line_diff': line_diff,
    }

    print(json.dumps(result, indent=2))

    sys.exit(0 if status == 'PASS' else 1)


if __name__ == '__main__':
    main()
