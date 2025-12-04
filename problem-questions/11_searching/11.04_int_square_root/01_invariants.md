# Binary Search Invariants for Largest Valid

**Q:** What are the invariants when searching for the largest value where `mid * mid <= k`?

**A:**
- `[left, right]` = unchecked candidates
- Everything `< left` has been checked and is **valid**
- Everything `> right` has been checked and is **invalid**
