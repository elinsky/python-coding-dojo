# Why Preorder Is Harder To Split

**Q:** Why can't you split preorder the same way you split inorder?
```
Preorder: [ 1 | 2, 4, 5 | 3, 6, 7 ]
            ^                     ^
    preorder_start            preorder_end

Inorder:  [ 4, 2, 5 | 1 | 6, 3, 7 ]
            ^         ^           ^
      inorder_start  root_idx   inorder_end
```

**A:** In inorder, the root sits between left and right subtrees - it's a natural divider.

In preorder, root comes first, then left, then right - but there's no marker showing where left ends and right begins. You need to know the *size* of the left subtree to know where to split.
