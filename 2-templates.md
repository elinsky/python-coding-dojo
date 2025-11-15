# Layer 2: Templates = Complete Algorithms

## What it is

A complete algorithm solving a well-defined computational problem

## Criteria

- ✓ Complete - Has clear input → output specification
- ✓ Standalone - Solves a problem on its own (though might be used as subroutine)
- ✓ Describes WHAT - "What problem does this solve?"
- ✓ Larger - Combines multiple patterns; 10-30+ lines
- ✓ Has problem statement - "Given X, compute Y"

## Template Structure

Each template should include:

1. **Problem statement** - What are we solving?
2. **High-level strategy** - The core insight (1-2 sentences)
3. **Detailed pseudocode** - Complete algorithm you memorize
4. **Patterns used** - Which Layer 1 patterns appear
5. **Memory hooks** - Mnemonics to aid recall

## Examples

### Template: Binary Addition (without +)

**Problem:** Given two integers a and b, return a + b using only bitwise operations

**Strategy:** Use full adder logic for each bit, propagate carry until no carries remain

**Detailed pseudocode:**

```python
ADD(a, b):
  while b:
    carry = (a & b) << 1  # E: Extract carries, shift left
    a = a ^ b             # A: Add without carry (XOR)
    b = carry             # S: Set b to carry
                          # A: Again (loop)
  return a
```

**Memory hook:** EASA (Extract, Add, Set, Again)

**Uses patterns:** "Ripple carry"

**Uses templates:** None (base template)

---

### Template: Binary Multiplication (without *)

**Problem:** Given two integers a and b, return a * b using only bitwise operations

**Strategy:** Grade school multiplication - add shifted copies when bit is 1

**Detailed pseudocode:**

```python
MULTIPLY(a, b):
  result = 0
  while b:
    if b & 1:
      result = ADD(result, a)  # calls ADD template
    a <<= 1
    b >>= 1
  return result
```

**Memory hook:** "Shift multiplicand LEFT, shift multiplier RIGHT"

**Uses patterns:** "Shift-and-conditional-accumulate"

**Uses templates:** "Binary Addition" (as subroutine)

---

### Template: Count Set Bits

**Problem:** Given integer x, return number of 1-bits

**Strategy:** Either iterate all bits, or iterate only set bits (more efficient)

**Detailed pseudocode (efficient version):**

```python
COUNT_BITS(x):
  count = 0
  while x:
    count += 1
    x &= (x - 1)  # Clear lowest set bit
  return count
```

**Memory hook:** "Each iteration removes exactly one bit"

**Uses patterns:** "Iterate through set bits"

**Uses templates:** None

---

## Key Distinction Tests

### Ask: "Does this have a clear problem statement with inputs/outputs?"

- YES → Layer 2 (Template)
- NO → Layer 1 (Pattern)

### Ask: "Would I use this code chunk in multiple different algorithms?"

- YES → Layer 1 (Pattern)
- NO, it's specific to one problem → Layer 2 (Template)

---

## Gray Area Resolution

### What about "Binary addition" - is it pattern or template?

If you're implementing multiply and you need to add intermediate results:

- Multiplication (Layer 2) calls Addition (also Layer 2)
- Templates can use other templates as subroutines

**The distinction:** Addition has a complete problem statement. "Ripple carry" doesn't - it's just the carry propagation mechanism within addition.

---

## Comparison Example

### Pattern (Layer 1): "Ripple carry"

- **Used IN:** addition, subtraction, increment, decrement algorithms
- **Just a mechanism** for propagating carries
- **No standalone purpose**

### Template (Layer 2): "Binary addition"

- **Solves:** "Add two numbers without +"
- **Uses:** Ripple carry pattern
- **Can be called** as subroutine in multiplication

---

## Both Layers Have Pseudocode

### Layer 1: Mechanism pseudocode (generic, reusable)

Example: "Shift-and-conditional-accumulate" works for multiply, power, etc.

```python
result = 0
while selector:
    if selector & 1:
        result += current_value
    current_value <<= 1
    selector >>= 1
```

### Layer 2: Algorithm pseudocode (specific problem, complete solution)

Example: EASA pseudocode is specific to addition, includes setup, loop details, finalization, and memory hooks

---

## Naming Convention

Name pattern: Problem name or "Algorithm for X"

- "Binary addition algorithm"
- "Multiplication without multiply operator"
- "Count set bits"
