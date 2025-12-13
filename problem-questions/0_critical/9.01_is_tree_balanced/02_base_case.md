# Base Case

**Q:** What should you return for an empty tree (None)?

**A:** `(balanced=True, height=-1)`

- **Balanced**: True (an empty tree is trivially balanced)
- **Height**: -1 (so a leaf node has height 0 = max(-1, -1) + 1)
