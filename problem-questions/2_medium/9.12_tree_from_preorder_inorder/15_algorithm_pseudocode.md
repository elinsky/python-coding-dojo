# Algorithm Pseudocode

**Q:** Write the pseudocode for reconstructing a tree from preorder and inorder.

**A:**
```
Build hashmap of inorder values to indices

Define helper(preorder_start, preorder_end, inorder_start, inorder_end):
    If range is empty, return None

    Get root value (first element of current preorder range)
    Find root's index in inorder using hashmap
    Calculate left subtree size from inorder

    Calculate left/right subtree indices for both arrays
    Build left subtree by recursing on left portions
    Build right subtree by recursing on right portions

    Return node with root, left child, right child

Call helper with full array indices
```
