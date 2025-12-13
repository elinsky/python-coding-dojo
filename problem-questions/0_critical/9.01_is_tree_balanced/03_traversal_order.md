# Traversal Order

**Q:** What traversal order should you use and why?

**A:** **Post-order** (left, right, process)

You need the left and right subtree results (balanced + height) **before** you can determine if the current node is balanced.
