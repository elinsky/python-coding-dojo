# The Two Cases

**Q:** For each cell in the DP table, what two cases do you consider?

**A:**
1. **Don't use this play type at all** → look at row above, same column
2. **Use at least one of this play type** → look at same row, column minus play value

You **add** both cases together (they're mutually exclusive and exhaustive).
