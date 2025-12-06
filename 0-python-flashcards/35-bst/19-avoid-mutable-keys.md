# Mutable Objects in BST

**Q:** Can I put mutable objects in a BST?

**A:** Avoid it — if the key changes, the BST ordering breaks. If you must update a key, remove the node first, update it, then re-insert.
