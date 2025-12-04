# Quickselect Search Space

**Q:** In quickselect, what are we searching for and what do `left` and `right` represent?

**A:**
- **Searching for**: index `k-1` (where the k-th largest will end up)
- **`left, right`**: inclusive bounds of indices that could still be position `k-1`

The array becomes partially sorted as we go:
- Elements outside `[left, right]` are in their correct relative positions
- We just don't know exactly which element belongs at `k-1` yet
