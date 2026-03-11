#!/usr/bin/env python3
"""
Compute readability metrics for text: sentence variance, grade level, repetition score.

Usage:
    python3 readability_metrics.py < text.txt
    python3 readability_metrics.py text.txt
"""

import re
import json
import sys
import math


def split_sentences(text):
    """Split text into sentences. Handles common abbreviations."""
    # Protect common abbreviations
    text = re.sub(r'\b(Mr|Mrs|Ms|Dr|Prof|Sr|Jr|vs|etc|i\.e|e\.g)\.',
                  lambda m: m.group().replace('.', '<DOT>'), text)

    # Split on sentence-ending punctuation followed by space + capital or end of string
    sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z"\u201c])', text)

    # Restore dots
    sentences = [s.replace('<DOT>', '.').strip() for s in sentences]

    # Filter empty
    sentences = [s for s in sentences if s and len(s.split()) > 0]

    return sentences


def count_syllables(word):
    """Estimate syllable count for English words."""
    word = word.lower().strip(".,;:!?\"'()-")
    if not word:
        return 0
    if len(word) <= 2:
        return 1

    # Count vowel groups
    count = len(re.findall(r'[aeiouy]+', word))

    # Subtract silent e
    if word.endswith('e') and not word.endswith('le'):
        count = max(1, count - 1)

    # Handle special endings
    if word.endswith('ed') and len(word) > 3:
        if word[-3] not in 'td':
            count = max(1, count - 1)

    return max(1, count)


def flesch_kincaid_grade(total_words, total_sentences, total_syllables):
    """Calculate Flesch-Kincaid grade level."""
    if total_sentences == 0 or total_words == 0:
        return 0.0
    return (0.39 * (total_words / total_sentences) +
            11.8 * (total_syllables / total_words) - 15.59)


def analyze_sentence_rhythm(sentences):
    """Analyze sentence length variation."""
    if not sentences:
        return {'std_dev': 0, 'mean': 0, 'min': 0, 'max': 0, 'lengths': []}

    lengths = [len(s.split()) for s in sentences]
    mean = sum(lengths) / len(lengths)
    variance = sum((l - mean) ** 2 for l in lengths) / max(len(lengths) - 1, 1)
    std_dev = math.sqrt(variance)

    return {
        'std_dev': round(std_dev, 2),
        'mean': round(mean, 1),
        'min': min(lengths),
        'max': max(lengths),
        'range': max(lengths) - min(lengths),
        'lengths': lengths,
    }


def analyze_paragraph_rhythm(text):
    """Check for repetitive paragraph structure."""
    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
    if not paragraphs:
        return {'count': 0, 'consecutive_same_sentence_count': False}

    para_sentence_counts = []
    for para in paragraphs:
        sentences = split_sentences(para)
        para_sentence_counts.append(len(sentences))

    # Check for 3+ consecutive paragraphs with same sentence count
    consecutive_same = False
    for i in range(len(para_sentence_counts) - 2):
        if (para_sentence_counts[i] == para_sentence_counts[i+1] ==
                para_sentence_counts[i+2]):
            consecutive_same = True
            break

    return {
        'count': len(paragraphs),
        'sentence_counts': para_sentence_counts,
        'consecutive_same_sentence_count': consecutive_same,
    }


def analyze_opener_diversity(sentences):
    """Check how varied sentence openers are."""
    if not sentences:
        return {'unique_ratio': 0, 'openers': []}

    openers = []
    for s in sentences:
        words = s.split()
        if words:
            opener = words[0].lower().strip('"\'')
            openers.append(opener)

    unique = len(set(openers))
    total = len(openers)

    # Find repeated openers
    from collections import Counter
    counts = Counter(openers)
    repeated = {word: count for word, count in counts.items() if count > 2}

    return {
        'unique_ratio': round(unique / max(total, 1), 2),
        'total_openers': total,
        'unique_openers': unique,
        'repeated_openers': repeated,
    }


def analyze_repetition(text):
    """Check for word and phrase repetition."""
    words = re.findall(r'\b[a-z]+\b', text.lower())
    if not words:
        return {'word_repetition_score': 0}

    # Filter stop words
    stop_words = {'the', 'a', 'an', 'is', 'are', 'was', 'were', 'be', 'been',
                  'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will',
                  'would', 'could', 'should', 'may', 'might', 'shall', 'can',
                  'to', 'of', 'in', 'for', 'on', 'with', 'at', 'by', 'from',
                  'as', 'into', 'through', 'during', 'before', 'after', 'and',
                  'but', 'or', 'nor', 'not', 'so', 'yet', 'both', 'either',
                  'neither', 'each', 'every', 'all', 'any', 'few', 'more',
                  'most', 'other', 'some', 'such', 'no', 'only', 'own',
                  'same', 'than', 'too', 'very', 'just', 'because', 'if',
                  'when', 'while', 'that', 'this', 'these', 'those', 'it',
                  'its', 'we', 'our', 'they', 'their', 'them', 'i', 'my',
                  'me', 'you', 'your', 'he', 'she', 'his', 'her'}

    content_words = [w for w in words if w not in stop_words and len(w) > 3]

    if not content_words:
        return {'word_repetition_score': 0}

    from collections import Counter
    counts = Counter(content_words)
    total_content = len(content_words)
    unique_content = len(set(content_words))

    # Repetition score: higher = more repetitive (0-1 scale)
    repetition_score = 1 - (unique_content / max(total_content, 1))

    # Find overused words (>3 occurrences in 500 words)
    threshold = max(3, total_content // 150)
    overused = {word: count for word, count in counts.most_common(20)
                if count > threshold}

    return {
        'word_repetition_score': round(repetition_score, 3),
        'unique_content_words': unique_content,
        'total_content_words': total_content,
        'overused_words': overused,
    }


def main():
    # Read input
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            text = f.read()
    else:
        text = sys.stdin.read()

    text = text.strip()
    if not text:
        print(json.dumps({'error': 'Empty input'}))
        sys.exit(1)

    # Split sentences
    sentences = split_sentences(text)

    # Count totals
    words = text.split()
    total_words = len(words)
    total_sentences = len(sentences)
    total_syllables = sum(count_syllables(w) for w in words)

    # Compute metrics
    grade = flesch_kincaid_grade(total_words, total_sentences, total_syllables)
    rhythm = analyze_sentence_rhythm(sentences)
    para_rhythm = analyze_paragraph_rhythm(text)
    openers = analyze_opener_diversity(sentences)
    repetition = analyze_repetition(text)

    # Determine pass/fail
    checks = {
        'sentence_std_dev': {
            'value': rhythm['std_dev'],
            'threshold': 5.0,
            'status': 'PASS' if rhythm['std_dev'] > 5.0 else 'FAIL',
        },
        'grade_level': {
            'value': round(grade, 1),
            'range': '6-12',
            'status': 'PASS' if 6 <= grade <= 12 else 'WARN',
        },
        'consecutive_same_paragraphs': {
            'value': para_rhythm['consecutive_same_sentence_count'],
            'threshold': False,
            'status': 'FAIL' if para_rhythm['consecutive_same_sentence_count'] else 'PASS',
        },
    }

    all_pass = all(c['status'] == 'PASS' for c in checks.values())

    result = {
        'status': 'PASS' if all_pass else 'FAIL',
        'metrics': {
            'total_words': total_words,
            'total_sentences': total_sentences,
            'flesch_kincaid_grade': round(grade, 1),
            'sentence_rhythm': rhythm,
            'paragraph_rhythm': para_rhythm,
            'opener_diversity': openers,
            'repetition': repetition,
        },
        'checks': checks,
    }

    # Remove raw lengths for cleaner output
    if 'lengths' in result['metrics']['sentence_rhythm']:
        lengths = result['metrics']['sentence_rhythm']['lengths']
        if len(lengths) > 20:
            result['metrics']['sentence_rhythm']['lengths'] = (
                lengths[:10] + ['...'] + lengths[-5:]
            )

    print(json.dumps(result, indent=2))

    sys.exit(0 if all_pass else 1)


if __name__ == '__main__':
    main()
