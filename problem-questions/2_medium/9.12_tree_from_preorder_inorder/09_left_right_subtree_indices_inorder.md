# Left and Right Subtree Indices - Inorder

**Q:** Given these indices for the full tree, what are the inorder indices for the left and right subtrees?
```
Inorder:  [ 4, 2, 5 | 1 | 6, 3, 7 ]
            ^         ^           ^
      inorder_start  root_idx   inorder_end
            0         3           7
```

**A:**
Left subtree:
- `inorder_start` = `inorder_start` (unchanged)
- `inorder_end` = `root_idx`

Right subtree:
- `inorder_start` = `root_idx + 1`
- `inorder_end` = `inorder_end` (unchanged)
