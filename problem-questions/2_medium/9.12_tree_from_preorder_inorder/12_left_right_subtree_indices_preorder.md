# Left and Right Subtree Indices - Preorder

**Q:** Given these indices for the full tree, what are the preorder indices for the left and right subtrees?
```
Preorder: [ 1 | 2, 4, 5 | 3, 6, 7 ]
            ^                     ^
    preorder_start            preorder_end
            0                     7
```
You know `left_subtree_size = 3` and `right_subtree_size = 3`.

**A:**
Left subtree:
- `preorder_start` = `preorder_start + 1` (skip the root)
- `preorder_end` = `preorder_start + 1 + left_subtree_size`

Right subtree:
- `preorder_start` = `preorder_start + 1 + left_subtree_size`
- `preorder_end` = `preorder_end` (unchanged)
