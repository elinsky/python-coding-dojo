# Bit Manipulation Primitives

## Mastered

### Single Bit Operations
```python
# How do you get bit at position i?
(x >> i) & 1

# How do you set bit at position i?
x | (1 << i)

# How do you toggle bit at position i?
x ^ (1 << i)

# How do you swap bits at positions i and j?
x ^ ((1 << i) | (1 << j))  # Toggle both bits simultaneously

# Q: How do I clear bit at position i?
# A: AND with NOT of (1 shifted left by i)
x & ~(1 << i)
```

### XOR Properties
```python
# Q: How do I cancel/eliminate pairs of the same number?
# A: XOR them together (x ^ x = 0)
x ^ x == 0

# Q: What's the identity element for XOR? (How do I start XOR accumulation?)
# A: 0 (because x ^ 0 = x)
x ^ 0 == x

# Q: Can I reorder/rearrange XOR operations to group duplicates together?
# A: Yes, XOR is commutative (x ^ y = y ^ x)
x ^ y == y ^ x

# Q: How do I find which bits differ between x and y?
# A: XOR them
x ^ y
```

### Consecutive Bit Operations
```python
# Q: How do I find positions where consecutive bits differ?
# A: XOR with right-shifted self
x ^ (x >> 1)  # Each set bit marks where neighbors differ

# Example: x = 0b110 (6)
#   x >> 1 = 0b011 (3)
#   x ^ (x >> 1) = 0b101 (positions 0 and 2 have different neighbors)
```

### Lowest Set Bit Operations
```python
# Q: How do I clear/remove the lowest set bit?
# A: AND with (x - 1)
x & (x - 1)

# Q: How do I isolate the lowest set bit?
# A: AND with negative (two's complement)
x & -x
```

### Masks & Checks
```python
# Q: How do I create a mask of k ones? (e.g., 0b111 for k=3)
# A: (1 << k) - 1
(1 << k) - 1

# Q: How do I check if x is a power of 2?
# A: Check if clearing lowest set bit gives 0 (and x != 0)
x & (x - 1) == 0
```

### Two's Complement
```python
# Q: How do I get the negative of x (two's complement)?
# A: Flip all bits and add 1
-x  # (or equivalently: ~x + 1)
```

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
