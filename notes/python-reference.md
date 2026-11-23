# Python quick reference

## Collections

- list: ordered mutable sequence.
- tuple: ordered immutable sequence.
- dict: keyed mapping, preserving insertion order.
- set: unique unordered elements.

## A few useful patterns

Use enumerate(items) when both index and value are needed.
Use zip(left, right) to process two iterables together.
Use pathlib.Path to manipulate file-system paths.
Use csv.DictReader for named columns.
Use collections.Counter for frequency tables.

## Testing

The standard library includes unittest. Prefer small pure functions and
assert known example values for each edge case.
