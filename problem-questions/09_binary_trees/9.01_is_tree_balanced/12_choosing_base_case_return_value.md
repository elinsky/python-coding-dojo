# Choosing Base Case Return Value

**Q:** How do you decide what value to return in the base case (`if not tree`)?

**A:** Ask: **"What should an empty tree contribute to my calculation?"**

**Examples:**

**Count nodes:** Empty tree has 0 nodes
```python
if not tree: return 0
```

**Compute height:** Empty tree has height -1 (so leaf has height 0)
```python
if not tree: return -1
```

**Sum values:** Empty tree contributes 0 to sum
```python
if not tree: return 0
```

**Is balanced:** Empty tree is balanced (trivially true), height -1
```python
if not tree: return (True, -1)
```

**Contains value:** Empty tree doesn't contain the value
```python
if not tree: return False
```

**Method:** Work backward from a simple case:
1. Think about a **leaf node**
2. What should its children (both None) return so the combine step works?

**Example for height:**
- Leaf should have height 0
- Combine: `max(left_height, right_height) + 1`
- For leaf: `max(-1, -1) + 1 = 0` ✓
- So None returns -1

**Example for count:**
- Leaf should have count 1
- Combine: `left_count + right_count + 1`
- For leaf: `0 + 0 + 1 = 1` ✓
- So None returns 0
