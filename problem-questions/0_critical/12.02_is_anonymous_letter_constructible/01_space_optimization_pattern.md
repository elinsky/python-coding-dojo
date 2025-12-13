# Space Optimization Pattern

**Q:** What's the general pattern for optimizing space when checking if one collection contains enough elements to satisfy another?

**A:** **Create a counter for the SMALLER/NEEDED collection, not the LARGER/AVAILABLE one**

**Pattern:**
```python
# Track what you NEED (smaller)
needs = Counter(needed_items)

# Scan what you HAVE (larger), decrementing needs
for item in available_items:
    if item in needs:
        needs[item] -= 1
        if needs[item] == 0:
            del needs[item]

# Check if all needs satisfied
return not needs
```

**Why:**
- The "available" collection is often much larger
- You only care about items that appear in the "needed" collection
- Creating a counter for the larger collection wastes space on irrelevant items

**Examples:**
- Letter from magazine: Track letter (small), scan magazine (large)
- Anagram check: Track one string, scan the other
- Inventory check: Track order items (what you need), scan warehouse (what you have)

**Space saved:** O(m) → O(n) when m >> n
