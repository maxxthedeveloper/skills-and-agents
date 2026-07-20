#!/usr/bin/env python3
"""
Scan text for banned AI-isms from taboo-phrases.md.
Returns violations with line numbers. Zero tolerance: any match = FAIL.

Usage:
    python3 banned_phrase_scan.py < text.txt
    python3 banned_phrase_scan.py text.txt
    python3 banned_phrase_scan.py text.txt --taboo ../references/taboo-phrases.md
"""

import re
import sys
import os
import json


# Default taboo phrases organized by category.
# These are compiled from references/taboo-phrases.md.
TABOO_PHRASES = {
    "Hedging/Qualification": [
        "it's important to note that",
        "it's worth noting that",
        "it should be noted that",
        "it depends on your specific needs",
        "it's crucial to understand that",
        "it bears mentioning that",
        "one could argue that",
        "it goes without saying",
        "there are several factors to consider",
        "this is particularly important because",
        "it's essential to recognize that",
        "while there's no one-size-fits-all",
        "the answer isn't straightforward",
        "that said, it's important to",
        "results may vary depending on",
    ],
    "Filler Transitions": [
        "moreover",
        "furthermore",
        "additionally",
        "in addition to this",
        "let's dive in",
        "let's dive deeper",
        "let's unpack this",
        "let's explore",
        "without further ado",
        "with that being said",
        "that being said",
        "having said that",
        "it's also worth mentioning",
        "on the other hand",
        "by the same token",
        "in light of this",
        "in the same vein",
        "moving forward",
    ],
    "Corporate Buzzwords": [
        "leverage",
        "robust",
        "seamless",
        "seamlessly",
        "empower",
        "scalable",
        "cutting-edge",
        "game-changer",
        "game-changing",
        "best-in-class",
        "world-class",
        "synergy",
        "paradigm shift",
        "holistic",
        "ecosystem",
        "innovative",
        "revolutionize",
        "streamline",
        "streamlined",
        "optimize",
        "optimized",
        "elevate",
        "transform",
        "transformative",
        "harness",
        "unlock",
        "drive growth",
        "actionable insights",
        "thought leader",
        "thought leadership",
        "disruptive",
    ],
    "AI-Typical Openers": [
        "in today's rapidly evolving",
        "in today's fast-paced",
        "in today's digital age",
        "in today's world",
        "in an era of",
        "in the ever-changing landscape",
        "imagine a world where",
        "picture this:",
        "have you ever wondered",
        "are you tired of",
        "when it comes to",
        "in the realm of",
    ],
    "AI-Typical Closers": [
        "in conclusion",
        "to sum up",
        "to summarize",
        "in summary",
        "all in all",
        "at the end of the day",
        "embrace the power of",
        "the future is now",
        "the possibilities are endless",
        "start your journey today",
        "take the first step",
        "ready to transform",
        "don't miss out",
        "the ball is in your court",
    ],
    "AI Sentence Starters": [
        "essentially,",
        "interestingly,",
        "firstly,",
        "secondly,",
        "thirdly,",
        "importantly,",
        "notably,",
        "significantly,",
        "fundamentally,",
        "ultimately,",
        "consequently,",
        "accordingly,",
    ],
    "Empty Emphasis": [
        "comprehensive",
        "myriad",
        "plethora",
        "multifaceted",
        "unparalleled",
        "unmatched",
        "unprecedented",
        "groundbreaking",
        "a wide range of",
        "a variety of",
    ],
    "Delve & Family": [
        "delve",
        "delving",
        "deep dive",
        "dive deep",
        "navigate challenges",
        "navigate the complexities",
        "navigate this landscape",
        "tapestry",
        "rich tapestry",
        "intricate tapestry",
        "at the forefront",
        "realm",
        "the intricacies of",
        "foster",
    ],
}

# Single-word phrases that need word-boundary matching to avoid false positives
WORD_BOUNDARY_PHRASES = {
    "very", "incredibly", "extremely", "highly", "truly", "really",
    "absolutely", "utterly", "realm", "foster", "delve", "delving",
    "robust", "leverage", "seamless", "seamlessly", "empower",
    "scalable", "holistic", "innovative", "elevate", "harness",
    "unlock", "transform", "transformative", "disruptive",
    "moreover", "furthermore", "additionally", "essentially,",
    "optimize", "optimized", "streamline", "streamlined",
    "comprehensive", "myriad", "plethora", "multifaceted",
    "unparalleled", "unmatched", "unprecedented", "groundbreaking",
    "revolutionize",
}


def load_taboo_from_file(filepath):
    """Parse taboo-phrases.md to extract phrases."""
    phrases = {}
    current_category = None

    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            # Category headers: ## 1. Hedging / Qualification
            cat_match = re.match(r'^##\s+\d+\.\s+(.+?)(?:\s*\(.*\))?\s*$', line)
            if cat_match:
                current_category = cat_match.group(1).strip()
                phrases[current_category] = []
                continue
            # Phrase lines: - phrase text
            if current_category and line.startswith('- '):
                phrase = line[2:].strip().strip('"').strip("'").lower()
                if phrase:
                    phrases[current_category].append(phrase)

    return phrases if phrases else None


def scan_text(text, taboo_dict=None):
    """Scan text for banned phrases. Returns list of violations."""
    if taboo_dict is None:
        taboo_dict = TABOO_PHRASES

    lines = text.split('\n')
    violations = []

    for category, phrases in taboo_dict.items():
        for phrase in phrases:
            phrase_lower = phrase.lower().rstrip(',')
            # Determine if we need word-boundary matching
            needs_boundary = phrase_lower in {p.lower().rstrip(',') for p in WORD_BOUNDARY_PHRASES}

            if needs_boundary:
                pattern = r'\b' + re.escape(phrase_lower) + r'\b'
            else:
                pattern = re.escape(phrase_lower)

            for line_num, line in enumerate(lines, 1):
                for match in re.finditer(pattern, line.lower()):
                    violations.append({
                        'phrase': phrase,
                        'category': category,
                        'line': line_num,
                        'column': match.start() + 1,
                        'context': line.strip()[:120],
                    })

    return violations


def main():
    # Parse arguments
    text_file = None
    taboo_file = None

    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == '--taboo' and i + 1 < len(args):
            taboo_file = args[i + 1]
            i += 2
        elif not text_file:
            text_file = args[i]
            i += 1
        else:
            i += 1

    # Read text
    if text_file:
        with open(text_file, 'r') as f:
            text = f.read()
    else:
        text = sys.stdin.read()

    # Load taboo phrases
    taboo_dict = TABOO_PHRASES
    if taboo_file:
        loaded = load_taboo_from_file(taboo_file)
        if loaded:
            taboo_dict = loaded

    # Auto-detect taboo file relative to script
    if not taboo_file:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        default_taboo = os.path.join(script_dir, '..', 'references', 'taboo-phrases.md')
        if os.path.exists(default_taboo):
            loaded = load_taboo_from_file(default_taboo)
            if loaded:
                taboo_dict = loaded

    # Scan
    violations = scan_text(text, taboo_dict)

    # Output
    result = {
        'status': 'PASS' if len(violations) == 0 else 'FAIL',
        'violation_count': len(violations),
        'violations': violations,
        'summary': {}
    }

    # Summarize by category
    for v in violations:
        cat = v['category']
        result['summary'][cat] = result['summary'].get(cat, 0) + 1

    print(json.dumps(result, indent=2))

    # Exit code
    sys.exit(0 if len(violations) == 0 else 1)


if __name__ == '__main__':
    main()
