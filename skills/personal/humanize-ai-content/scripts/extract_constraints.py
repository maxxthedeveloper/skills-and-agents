#!/usr/bin/env python3
"""
Extract protected spans from input text.
Outputs JSON of numbers, proper nouns, dates, URLs, quotes, and legal terms.

Usage:
    python3 extract_constraints.py < input.txt
    python3 extract_constraints.py input.txt
    python3 extract_constraints.py input.txt -o constraints.json
"""

import re
import json
import sys


def extract_numbers(text):
    """Extract numbers, percentages, dollar amounts, measurements, ranges."""
    spans = []
    patterns = [
        # Dollar amounts: $4.2 million, $500K, $14,000/month
        (r'\$[\d,]+(?:\.\d+)?(?:\s*(?:million|billion|trillion|[KMBkmb]))?(?:/\w+)?', 'number'),
        # Percentages: 37%, 99.99%
        (r'\d+(?:\.\d+)?%', 'number'),
        # Multipliers: 3x, 4x faster
        (r'\d+(?:\.\d+)?x\b', 'number'),
        # Ranges with units: 18-24 months, 3-7 minutes
        (r'\d+(?:\.\d+)?[-–]\d+(?:\.\d+)?(?:\s*(?:months?|weeks?|days?|hours?|minutes?|seconds?|ms|years?|instances?|users?|nodes?|pods?))?', 'number'),
        # Numbers with units: 100,000 users, 340ms, 85ms, 15 hours
        (r'[\d,]+(?:\.\d+)?(?:\s*(?:ms|seconds?|minutes?|hours?|days?|weeks?|months?|years?|users?|requests?|nodes?|pods?|instances?|queries|events?|engineers?|teams?|clients?))\b', 'number'),
        # p-values: p99, p95, p50
        (r'p\d+', 'number'),
        # Standalone significant numbers (4+ digits or decimals)
        (r'\b\d{4,}(?:,\d{3})*(?:\.\d+)?\b', 'number'),
    ]

    for pattern, category in patterns:
        for match in re.finditer(pattern, text, re.IGNORECASE):
            start, end = match.span()
            # Grab surrounding context (up to 40 chars each side)
            ctx_start = max(0, start - 40)
            ctx_end = min(len(text), end + 40)
            context = text[ctx_start:ctx_end].strip()
            spans.append({
                'category': category,
                'text': match.group(),
                'context': context,
                'position': [start, end]
            })

    return spans


def extract_proper_nouns(text):
    """Extract likely proper nouns (capitalized words not at sentence start)."""
    spans = []
    # Multi-word proper nouns and single capitalized words mid-sentence
    # Skip common sentence starters
    skip = {'The', 'A', 'An', 'This', 'That', 'These', 'Those', 'It', 'We',
            'They', 'He', 'She', 'I', 'You', 'Our', 'My', 'His', 'Her',
            'Its', 'Their', 'Your', 'If', 'When', 'While', 'But', 'And',
            'Or', 'So', 'Not', 'No', 'In', 'On', 'At', 'To', 'For',
            'With', 'From', 'By', 'As', 'Of', 'Do', 'Does', 'Did',
            'First', 'Second', 'Third', 'Most', 'Some', 'Many', 'Each',
            'Every', 'Here', 'There', 'What', 'How', 'Why', 'Where'}

    # Find capitalized sequences that look like proper nouns
    for match in re.finditer(r'(?:(?<=[.!?]\s)|(?<=^))([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)', text, re.MULTILINE):
        word = match.group(1)
        if word.split()[0] not in skip:
            start, end = match.span(1)
            ctx_start = max(0, start - 40)
            ctx_end = min(len(text), end + 40)
            spans.append({
                'category': 'proper_noun',
                'text': word,
                'context': text[ctx_start:ctx_end].strip(),
                'position': [start, end]
            })

    # Mid-sentence capitalized words (not after period)
    for match in re.finditer(r'(?<=[a-z,;:] )([A-Z][a-zA-Z]*(?:\s+[A-Z][a-zA-Z]*)*)', text):
        word = match.group()
        if word.split()[0] not in skip and len(word) > 1:
            start, end = match.span()
            ctx_start = max(0, start - 40)
            ctx_end = min(len(text), end + 40)
            spans.append({
                'category': 'proper_noun',
                'text': word,
                'context': text[ctx_start:ctx_end].strip(),
                'position': [start, end]
            })

    # Known patterns: VP of X, CEO, CTO, etc.
    for match in re.finditer(r'(?:CEO|CTO|CFO|COO|VP|SVP|EVP|Director|Manager|Head)\s+(?:of\s+)?[A-Z][a-zA-Z\s]*', text):
        start, end = match.span()
        ctx_start = max(0, start - 40)
        ctx_end = min(len(text), end + 40)
        spans.append({
            'category': 'proper_noun',
            'text': match.group().strip(),
            'context': text[ctx_start:ctx_end].strip(),
            'position': [start, end]
        })

    return spans


def extract_dates(text):
    """Extract dates, times, quarters, durations."""
    spans = []
    patterns = [
        # Quarters: Q3 2024
        r'Q[1-4]\s*\d{4}',
        # Full dates: March 15, 2025 / January 2024
        r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(?:,\s*\d{4})?',
        r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}',
        # Numeric dates: 2024-03-15, 03/15/2024
        r'\d{4}[-/]\d{2}[-/]\d{2}',
        r'\d{2}/\d{2}/\d{4}',
        # Years: since 2019, in 2024
        r'(?:since|in|by|from|until|before|after)\s+\d{4}\b',
        # Durations: within 6 weeks, for 3 months
        r'(?:within|for|over|past|last|next)\s+\d+\s+(?:seconds?|minutes?|hours?|days?|weeks?|months?|years?)',
    ]

    for pattern in patterns:
        for match in re.finditer(pattern, text, re.IGNORECASE):
            start, end = match.span()
            ctx_start = max(0, start - 40)
            ctx_end = min(len(text), end + 40)
            spans.append({
                'category': 'date',
                'text': match.group(),
                'context': text[ctx_start:ctx_end].strip(),
                'position': [start, end]
            })

    return spans


def extract_urls(text):
    """Extract URLs, email addresses, file paths, API endpoints."""
    spans = []
    patterns = [
        # URLs
        (r'https?://[^\s<>"\')\]]+', 'url'),
        # Email addresses
        (r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', 'url'),
        # API endpoints: /api/v2/users
        (r'(?<!\w)/(?:api|v\d)/[^\s<>"\')\]]*', 'url'),
    ]

    for pattern, category in patterns:
        for match in re.finditer(pattern, text):
            start, end = match.span()
            ctx_start = max(0, start - 40)
            ctx_end = min(len(text), end + 40)
            spans.append({
                'category': category,
                'text': match.group(),
                'context': text[ctx_start:ctx_end].strip(),
                'position': [start, end]
            })

    return spans


def extract_quotes(text):
    """Extract direct quotes (text in quotation marks with attribution)."""
    spans = []
    # Quoted text
    for match in re.finditer(r'["\u201c]([^"\u201d]+)["\u201d]', text):
        quote_text = match.group()
        start, end = match.span()
        ctx_start = max(0, start - 60)
        ctx_end = min(len(text), end + 60)
        context = text[ctx_start:ctx_end].strip()
        # Check if there's attribution nearby (said, according to, etc.)
        if re.search(r'(?:said|says|stated|noted|according to|wrote|explained)', context, re.IGNORECASE):
            spans.append({
                'category': 'quote',
                'text': quote_text,
                'context': context,
                'position': [start, end]
            })

    return spans


def extract_legal(text):
    """Extract legal/compliance terms, certifications, regulatory references."""
    spans = []
    patterns = [
        r'SOC\s*[12]\s*(?:Type\s*(?:I{1,2}|[12]))?',
        r'GDPR(?:-compliant)?',
        r'HIPAA(?:-compliant)?',
        r'PCI[\s-]DSS',
        r'ISO\s*\d{4,5}',
        r'(?:under|per|pursuant to)\s+Section\s+\d+[A-Za-z]?',
        r'(?:CCPA|COPPA|FERPA|SOX|GLBA)',
        r'(?:FedRAMP|FISMA|NIST)',
    ]

    for pattern in patterns:
        for match in re.finditer(pattern, text, re.IGNORECASE):
            start, end = match.span()
            ctx_start = max(0, start - 40)
            ctx_end = min(len(text), end + 40)
            spans.append({
                'category': 'legal',
                'text': match.group(),
                'context': text[ctx_start:ctx_end].strip(),
                'position': [start, end]
            })

    return spans


def compute_statistics(text):
    """Compute basic text statistics."""
    sentences = re.split(r'[.!?]+\s+', text.strip())
    sentences = [s for s in sentences if s.strip()]
    words = text.split()
    paragraphs = [p for p in text.split('\n\n') if p.strip()]

    return {
        'word_count': len(words),
        'sentence_count': len(sentences),
        'paragraph_count': len(paragraphs),
        'avg_sentence_length': round(len(words) / max(len(sentences), 1), 1),
    }


def deduplicate_spans(spans):
    """Remove overlapping spans, keeping the longer match."""
    if not spans:
        return spans

    # Sort by position start, then by length (longer first)
    spans.sort(key=lambda s: (s['position'][0], -(s['position'][1] - s['position'][0])))

    result = []
    last_end = -1
    for span in spans:
        if span['position'][0] >= last_end:
            result.append(span)
            last_end = span['position'][1]

    return result


def main():
    # Read input
    if len(sys.argv) > 1 and sys.argv[1] != '-o':
        with open(sys.argv[1], 'r') as f:
            text = f.read()
    else:
        text = sys.stdin.read()

    # Extract all spans
    all_spans = []
    all_spans.extend(extract_numbers(text))
    all_spans.extend(extract_proper_nouns(text))
    all_spans.extend(extract_dates(text))
    all_spans.extend(extract_urls(text))
    all_spans.extend(extract_quotes(text))
    all_spans.extend(extract_legal(text))

    # Deduplicate
    all_spans = deduplicate_spans(all_spans)

    # Count by category
    by_category = {}
    for span in all_spans:
        cat = span['category']
        by_category[cat] = by_category.get(cat, 0) + 1

    output = {
        'protected_spans': all_spans,
        'statistics': {
            'total_spans': len(all_spans),
            'by_category': by_category,
            'text_stats': compute_statistics(text),
        }
    }

    result = json.dumps(output, indent=2)

    # Write output
    if '-o' in sys.argv:
        idx = sys.argv.index('-o')
        if idx + 1 < len(sys.argv):
            with open(sys.argv[idx + 1], 'w') as f:
                f.write(result)
            print(f"Wrote constraints to {sys.argv[idx + 1]}")
            return

    print(result)


if __name__ == '__main__':
    main()
