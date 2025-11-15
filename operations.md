# What Are Operations?

⏺ An operation is:

1. No control flow - No loops, no conditionals, no recursion
2. Single expression - Usually 1 line, max 2-3 operations chained together
3. Constant time - O(1), not dependent on input size
4. Atomic conceptually - Solves exactly one micro-task ("get this bit", "set this bit", "flip these bits")

## Examples

### Operations:

- `x & 1` ✓
- `(x >> i) & 1` ✓ (get bit - conceptually one thing despite 2 ops)
- `x & (x - 1)` ✓ (clear lowest bit - single expression)

### Not Operations:

- `while x: x &= (x-1)` ✗ (has loop - this is a pattern)
- `result |= (1 << i)` inside a loop ✗ (the loop makes it a pattern)

## The Boundary

If it has `while`, `for`, or `if` at the structural level → it's a **pattern**, not an **operation**.
