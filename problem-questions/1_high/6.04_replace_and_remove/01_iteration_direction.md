# Iteration Direction

**Q:** In replace_and_remove, which direction do you iterate for deletions? For expansions? Why?

**A:**
- Deletions: left to right (compacting toward the front)
- Expansions: right to left (expanding into the extra space at the end, so you don't overwrite unread data)
