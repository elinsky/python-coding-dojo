# Helper Function Signature

**Q:** What does the helper function do, and what are its inputs and output?

**A:**
**Purpose:** Build a subtree from portions of the preorder and inorder arrays

**Inputs:** 4 indices defining the current subtree's range in each array
- `preorder_start`, `preorder_end`
- `inorder_start`, `inorder_end`

**Output:** A `BinaryTreeNode` (or None if range is empty)
