# Choosing the Base Case

**Q:** How do you decide if the base case should be None, leaf, or parent-of-leaf?

**A:** Ask: **"What's the simplest input where I know the answer immediately?"**

For is_tree_balanced:
- **None (empty tree)**: ✓ I know it's balanced (trivially true) and height (-1)
- **Leaf**: I could compute it, but it requires checking `not tree.left and not tree.right`
- **Parent of leaf**: Too complex, would need to check children

**Rule of thumb:** Choose None when possible. It's:
- Simplest to check (`if not tree`)
- Handles edge cases (tree with only one node has two None children)
- Most common in tree recursion

**When to use leaf as base case:**
- Only if the problem specifically requires processing leaf nodes differently
- Example: "sum all leaf values" - you need to identify leaves
