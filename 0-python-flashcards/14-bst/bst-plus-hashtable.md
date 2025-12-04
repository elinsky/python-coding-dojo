# BST Combined with Hash Table

**Q:** When should I combine BST with hash table?

**A:** When you need both ordering and fast lookup by different key

```python
# Example: Students ordered by GPA, but lookup by name
bst_by_gpa = bintrees.RBTree()  # Key: GPA
hash_by_name = {}                # Key: name -> student object

# Fast lookup by name, but maintains GPA ordering
```
