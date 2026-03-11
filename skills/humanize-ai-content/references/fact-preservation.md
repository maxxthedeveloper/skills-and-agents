# Fact Preservation Rules

Protected spans are untouchable. Every number, name, date, URL, quote, and legal phrase in the original must survive rewriting **exactly**. This file defines what to protect and how.

---

## 6 Protected Categories

### 1. Numbers & Statistics

**Protected:** All numeric values, percentages, dollar amounts, measurements, counts, ratios, ranges.

- `$4.2 million` — exact amount preserved
- `37%` — no rounding, no rephrasing as "about a third"
- `3x faster` — multiplier preserved
- `100,000 users` — no approximation to "hundreds of thousands"
- `18-24 months` — range preserved exactly

**Rules:**
- Never round, approximate, or rephrase a number
- Preserve the original format (%, $, units)
- Keep numeric context ("up from 12% last year" — both numbers protected)

### 2. Proper Nouns

**Protected:** Company names, product names, person names, brand names, place names, organization names.

- `OpenAI` — exact casing
- `John Martinez, VP of Engineering` — full name + title
- `Kubernetes` — not "K8s" unless original used that
- `San Francisco Bay Area` — full place name

**Rules:**
- Preserve exact spelling and capitalization
- Keep titles and affiliations attached to names
- Never abbreviate or expand unless the original did

### 3. Dates & Times

**Protected:** All temporal references — specific dates, years, quarters, deadlines, durations.

- `Q3 2024` — exact quarter + year
- `March 15, 2025` — exact date
- `within 6 weeks` — exact duration
- `since 2019` — exact year

**Rules:**
- Never convert formats (don't change "March 15" to "3/15")
- Preserve relative time references exactly
- Keep timezone references if present

### 4. URLs & Links

**Protected:** All URLs, email addresses, file paths, API endpoints.

- `https://example.com/docs/v2/auth` — full URL
- `team@company.com` — exact email
- `/api/v2/users` — exact path

**Rules:**
- Character-for-character preservation
- Never shorten or expand URLs
- Preserve anchor fragments and query parameters

### 5. Direct Quotes

**Protected:** Any text in quotation marks attributed to a person or source.

- `"We expect to double revenue by Q4," said CEO Jane Smith` — exact wording + attribution

**Rules:**
- Quote text is verbatim — zero changes
- Attribution (who said it) preserved
- Context around the quote can be rewritten

### 6. Legal & Compliance Text

**Protected:** Disclaimers, regulatory references, license terms, compliance statements.

- `SOC 2 Type II certified` — exact certification
- `GDPR-compliant` — exact standard
- `under Section 230` — exact legal reference

**Rules:**
- Never paraphrase legal/regulatory language
- Preserve acronyms and standard names exactly
- Keep version numbers for standards/certifications

---

## Granularity Rules

### Context Preservation
Protected spans include their immediate context when that context affects meaning:
- "grew **37%** year-over-year" — "year-over-year" is part of the stat's meaning
- "**$4.2M** in Series A" — "in Series A" is part of the amount's context

### Attribution Preservation
When a fact is attributed, the attribution is also protected:
- "**according to Gartner**" — source attribution stays
- "**a McKinsey study found**" — source reference stays

### Precision Preservation
Never trade precision for readability:
- "128-bit encryption" stays "128-bit encryption" (not "strong encryption")
- "99.99% uptime" stays "99.99% uptime" (not "near-perfect uptime")

---

## Extraction Format

The `extract_constraints.py` script outputs protected spans as JSON:

```json
{
  "protected_spans": [
    {
      "category": "number",
      "text": "$4.2 million",
      "context": "raised $4.2 million in Series A",
      "position": [45, 57]
    }
  ],
  "statistics": {
    "total_spans": 12,
    "by_category": {
      "number": 5,
      "proper_noun": 3,
      "date": 2,
      "url": 1,
      "quote": 1,
      "legal": 0
    }
  }
}
```

Every span in this JSON must appear in the rewritten output. The `validate_preservation.py` script checks this.
