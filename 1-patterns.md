# Layer 1: Patterns = Mechanisms

## What it is

A reusable technique/mechanism that appears in multiple algorithms

## Criteria

- ✓ Incomplete - Not a standalone algorithm; needs a problem context
- ✓ Reusable - Used as a building block in multiple different algorithms
- ✓ Describes HOW - "How to iterate", "How to propagate", "How to accumulate"
- ✓ Small - Typically 3-10 lines of code
- ✓ No problem statement - It's a technique, not a solution

## Examples

### Pattern: Ripple carry

```python
while b:
    carry = (a & b) << 1
    a = a ^ b
    b = carry
```

### Pattern: Iterate through set bits

```python
while x:
    # do something
    x &= (x - 1)
```

### Pattern: Shift and accumulate

```python
while multiplier:
    if multiplier & 1:
        result += value
    value <<= 1
    multiplier >>= 1
```

## Naming Convention

Name pattern: "How to X" or "X-ing pattern"

- "How to propagate carries"
- "Set-bit iteration pattern"
