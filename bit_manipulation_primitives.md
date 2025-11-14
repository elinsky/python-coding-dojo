# Bit Manipulation Primitives

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

## Essential Primitives (Memorize These!)

### Single Bit Operations
```python
(x >> i) & 1              # Get bit at position i
x | (1 << i)              # Set bit at position i
x & ~(1 << i)             # Clear bit at position i
x ^ (1 << i)              # Toggle bit at position i
```

### Lowest Set Bit Operations
```python
x & (x - 1)               # Clear lowest set bit
x & ~(x - 1)              # Isolate lowest set bit
x & -x                    # Isolate lowest set bit (alternative)
```

### Masks
```python
(1 << k) - 1              # Create mask with k 1's (e.g., 0b111)
~((1 << k) - 1)           # Create mask with k 0's on right
```

### Common Checks
```python
x & (x - 1) == 0          # Is power of 2? (if x != 0)
x ^ y                     # Find bits that differ between x and y
x & ((1 << k) - 1)        # x mod 2^k (mod by power of 2)
```

### Propagation
```python
x | (x - 1)               # Right propagate rightmost set bit
x & (x + 1)               # Turn off rightmost string of 1s
```

## Quick XOR Identities
```python
x ^ x = 0
x ^ 0 = x
x ^ y = y ^ x             # Commutative
```

## Common Patterns & Algorithms

### Iteration Patterns

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

### Swap Patterns

**Swap bits at positions i and j**
```python
if ((x >> i) & 1) != ((x >> j) & 1):  # Only if they differ
    x ^= (1 << i) | (1 << j)           # Toggle both
```

**Swap without temp variable**
```python
x ^= y
y ^= x
x ^= y
```

### Parity (even/odd number of 1-bits)

**Compute parity by processing all bits**
```python
parity = 0
while x:
    parity ^= 1
    x &= (x - 1)  # Clear lowest set bit
return parity
```

**Compute parity using XOR reduction**
```python
x ^= x >> 32
x ^= x >> 16
x ^= x >> 8
x ^= x >> 4
x ^= x >> 2
x ^= x >> 1
return x & 1
```

### Counting Bits

**Count set bits (naive)**
```python
count = 0
while x:
    count += x & 1
    x >>= 1
```

**Count set bits (efficient - clear lowest)**
```python
count = 0
while x:
    count += 1
    x &= (x - 1)
```

### Reverse Patterns

**Reverse bits (swap symmetrically)**
```python
# Swap pairs, then nibbles, then bytes, etc.
# Process in log(n) stages
```

**Reverse a k-bit number**
```python
result = 0
for _ in range(k):
    result = (result << 1) | (x & 1)
    x >>= 1
```

### Lookup Tables / Caching

**Precompute results for small bit widths**
```python
# Example: Cache parity for all 16-bit numbers
PRECOMPUTED_PARITY = [compute_parity(i) for i in range(1 << 16)]

# For 64-bit number, break into 16-bit chunks
def parity_64bit(x):
    MASK = 0xFFFF
    return (PRECOMPUTED_PARITY[x >> 48] ^
            PRECOMPUTED_PARITY[(x >> 32) & MASK] ^
            PRECOMPUTED_PARITY[(x >> 16) & MASK] ^
            PRECOMPUTED_PARITY[x & MASK])
```

**Key insight:** Process multiple bits at once by:
- Caching results for small bit patterns (2-bit, 16-bit, etc.)
- Using associativity to combine cached results
- Trade space for time (e.g., 2^16 = 65536 entries is feasible)

## Performance Tips

1. **Use cache for repeated operations** - Precompute and store results for small inputs
2. **Exploit associativity** - XOR, AND, OR are associative; can process in any grouping
3. **Exploit commutativity** - Can reorder operations for parallel processing
4. **Process sparse inputs efficiently** - Use `x &= (x - 1)` to skip zeros
5. **Combine techniques** - Mix caching with word-level operations for best performance

## Key Insight
Most bit manipulation problems are just **combining these primitives creatively**. Once you have these memorized, you can pattern-match problems to the right combination of operations.
