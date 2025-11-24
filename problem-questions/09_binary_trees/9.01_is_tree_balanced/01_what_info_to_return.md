# What Information to Return

**Q:** What two pieces of information do you need to return from each recursive call?

**A:**
1. **Is balanced?** (boolean) - whether the subtree is balanced
2. **Height** (int) - the height of the subtree

Without height, you can't check if parent node is balanced.
