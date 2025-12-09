# Quickselect Search Space

**Q:** In quickselect, what are we searching for and what do `left` and `right` represent?

**A:**
- **Searching for**: the element that belongs at index `k-1` (when sorted descending)
- **`left, right`**: inclusive bounds of indices that could still contain the k-th largest

The array becomes partially sorted as we go:
- Elements outside `[left, right]` are in their correct relative positions
- We just don't know exactly which element belongs at `k-1` yet
