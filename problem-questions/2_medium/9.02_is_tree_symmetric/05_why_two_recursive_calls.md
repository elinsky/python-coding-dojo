# Why Two Recursive Calls

**Q:** Why do you need two recursive calls in is_symmetric?

**A:** The helper checks if two nodes are mirrors. To confirm the children are also mirrors, you must ask both questions:
1. Does left.left mirror right.right? (outer children)
2. Does left.right mirror right.left? (inner children)

Both must be true for the subtrees to be symmetric.
