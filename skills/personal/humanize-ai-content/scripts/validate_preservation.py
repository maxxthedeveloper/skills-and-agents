#!/usr/bin/env python3
"""
Validate that all protected spans from extract_constraints survived rewriting.
Reads constraints JSON and checks each span against the rewritten text.

Usage:
    python3 validate_preservation.py constraints.json rewritten.txt
    python3 validate_preservation.py constraints.json < rewritten.txt
"""

import re
import json
import sys


def normalize_whitespace(text):
    """Collapse whitespace for flexible matching."""
    return re.sub(r'\s+', ' ', text.strip())


def find_span_in_text(span_text, text):
    """Check if a protected span exists in the rewritten text.
    Uses exact match first, then normalized whitespace match.
    Returns (found: bool, match_type: str).
    """
    # Exact match
    if span_text in text:
        return True, 'exact'

    # Normalized whitespace match
    norm_span = normalize_whitespace(span_text)
    norm_text = normalize_whitespace(text)
    if norm_span in norm_text:
        return True, 'whitespace_normalized'

    # Case-insensitive match (for proper nouns that might shift case)
    if norm_span.lower() in norm_text.lower():
        return True, 'case_insensitive'

    # For numbers, try without commas (1,000 vs 1000)
    if re.match(r'^[\d,$%.x\-–/]+', span_text):
        stripped = span_text.replace(',', '')
        if stripped in text or stripped in text.replace(',', ''):
            return True, 'numeric_normalized'

    return False, 'missing'


def validate(constraints, rewritten_text):
    """Validate all protected spans against rewritten text."""
    results = []
    spans = constraints.get('protected_spans', [])

    for span in spans:
        span_text = span['text']
        found, match_type = find_span_in_text(span_text, rewritten_text)

        results.append({
            'text': span_text,
            'category': span.get('category', 'unknown'),
            'found': found,
            'match_type': match_type,
            'context': span.get('context', ''),
        })

    passed = sum(1 for r in results if r['found'])
    total = len(results)

    return {
        'status': 'PASS' if passed == total else 'FAIL',
        'passed': passed,
        'total': total,
        'percentage': round(passed / max(total, 1) * 100, 1),
        'results': results,
        'missing': [r for r in results if not r['found']],
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 validate_preservation.py constraints.json [rewritten.txt]")
        print("       python3 validate_preservation.py constraints.json < rewritten.txt")
        sys.exit(2)

    # Load constraints
    constraints_file = sys.argv[1]
    with open(constraints_file, 'r') as f:
        constraints = json.load(f)

    # Load rewritten text
    if len(sys.argv) > 2:
        with open(sys.argv[2], 'r') as f:
            rewritten_text = f.read()
    else:
        rewritten_text = sys.stdin.read()

    # Validate
    result = validate(constraints, rewritten_text)

    print(json.dumps(result, indent=2))

    # Print summary
    print(f"\n--- Preservation Summary ---")
    print(f"Status: {result['status']}")
    print(f"Spans preserved: {result['passed']}/{result['total']} ({result['percentage']}%)")

    if result['missing']:
        print(f"\nMISSING SPANS ({len(result['missing'])}):")
        for m in result['missing']:
            print(f"  [{m['category']}] \"{m['text']}\"")
            if m['context']:
                print(f"    Context: {m['context'][:80]}...")

    sys.exit(0 if result['status'] == 'PASS' else 1)


if __name__ == '__main__':
    main()
