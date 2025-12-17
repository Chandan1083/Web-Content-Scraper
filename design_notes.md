# Design Notes

## Static vs JS Fallback
- Static scrape attempted first.
- If too few sections or missing text, Playwright is used.

## Wait Strategy for JS
- Network idle + timed scrolls (3)

## Click & Scroll Strategy
- Infinite scroll via mouse wheel
- Depth = 3

## Section Grouping & Labels
- Based on semantic tags and headings
- Labels derived from first words

## Noise Filtering & Truncation
- HTML truncated to 1000 chars
- Overlays ignored implicitly
