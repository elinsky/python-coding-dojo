# Bit Manipulation Primitives

## Mastered

---

## Core Bitwise Operators

```python
&        # AND       - Both bits must be 1
|        # OR        - At least one bit must be 1
^        # XOR       - Exactly one bit must be 1 (exclusive or)
~        # NOT       - Flip all bits (complement)
<<       # Left shift - Multiply by 2^n
>>       # Right shift - Divide by 2^n (arithmetic shift)
```

**Examples:**
```python
6 & 4    # 0b110 & 0b100 = 0b100 = 4
1 | 2    # 0b001 | 0b010 = 0b011 = 3
15 ^ x   # Flip the lower 4 bits of x
~0       # All 1's (-1 in two's complement)
1 << 10  # 2^10 = 1024
8 >> 1   # 8 / 2 = 4
-16 >> 2 # -16 / 4 = -4 (sign is preserved)
```

**Important notes:**
- Python integers have unlimited precision (no overflow)
- Negative numbers use two's complement representation
- Right shift preserves sign (arithmetic shift)
- There is no unsigned shift in Python

## Common Patterns & Algorithms

### Iteration Patterns

**Scan bit positions from right to left (fixed width)**
```python
for i in range(64):  # or range(32) for 32-bit
    bit = (x >> i) & 1
    # Process bit at position i
```

**Iterate through all bits (right to left)**
```python
while x:
    if x & 1:
        # Process this bit
    x >>= 1
```

**Iterate through only set bits (efficient!)**
```python
while x:
    # Process x (has at least one bit set)
    x &= (x - 1)  # Clear lowest set bit
```

**Iterate through all subsets of a mask**
```python
subset = mask
while True:
    # Process subset
    subset = (subset - 1) & mask
    if subset == mask:
        break
```

## Key Insight
Most bit manipulation problems are just **combining these primitives creatively**. Once you have these memorized, you can pattern-match problems to the right combination of operations.
