# Calculating Subtree Sizes

**Q:** How do you calculate the left and right subtree sizes? Use these indices:
```
Preorder: [ 1 | 2, 4, 5 | 3, 6, 7 ]
            ^                     ^
    preorder_start            preorder_end

Inorder:  [ 4, 2, 5 | 1 | 6, 3, 7 ]
            ^         ^           ^
      inorder_start  root_idx   inorder_end
```

**A:**
- `left_subtree_size = root_idx - inorder_start` (3 - 0 = 3)
- `right_subtree_size = inorder_end - root_idx - 1` (7 - 3 - 1 = 3)
