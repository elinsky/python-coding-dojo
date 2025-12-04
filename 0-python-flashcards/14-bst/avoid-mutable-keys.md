# Mutable Objects in BST

**Q:** Can I put mutable objects in a BST?

**A:** Avoid it; if needed, remove before updating, then re-insert

```python
# WRONG: updating object in BST breaks ordering
obj.value = new_value  # BST doesn't know to reposition

# CORRECT: remove, update, re-insert
bst.remove(obj)
obj.value = new_value
bst.insert(obj)
```
