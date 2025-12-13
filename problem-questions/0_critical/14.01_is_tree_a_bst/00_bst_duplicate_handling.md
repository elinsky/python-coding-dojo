# BST Duplicate Handling

**Q:** When validating a BST, should the comparisons be strict (`<` and `>`) or allow equality (`<=` and `>=`)?

**A:** **Allow equality** (`<=` and `>=`)

```python
# CORRECT - allows duplicates
if largest_left <= curr_val and smallest_right >= curr_val:
    is_bst = True

# WRONG - too strict, rejects valid BSTs with duplicates
if largest_left < curr_val and smallest_right > curr_val:
    is_bst = True
```

**Why:**
BSTs can contain duplicate values. The BST property allows:
- Left subtree values ≤ current node
- Right subtree values ≥ current node

**Example that breaks with strict inequality:**
```
    -107
   /    \
 -115  -104
  \      \
  -112  -104  ← Duplicate -104!
```

With strict `<`, this valid BST would be rejected because `-104 < -104` is false.

**Rule:** Use `<=` and `>=` to handle duplicates correctly.
