# Finding Subtree Roots

**Q:** Given the original arrays, what is the root of the left subtree? The right subtree?
- Preorder: `[1, 2, 4, 5, 3, 6, 7]`
- Inorder: `[4, 2, 5, 1, 6, 3, 7]`

**A:**
```
Preorder: [ 1 | 2, 4, 5 | 3, 6, 7 ]
            ^   ^         ^
           root L-root    R-root

Inorder:  [ 4, 2, 5 | 1 | 6, 3, 7 ]
            -------   ^   -------
            L-tree   root  R-tree
```
- Left subtree root = 2
- Right subtree root = 3
