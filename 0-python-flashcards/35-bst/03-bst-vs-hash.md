# BST vs Hash Table

**Q:** When should I use a BST instead of a hash table?

**A:** When you need ordering: min/max, successor/predecessor, range queries

```python
# BST advantages:
# - Iterate in sorted order: O(n)
# - Find min/max: O(log n)
# - Find successor/predecessor: O(log n)
# - Range queries: O(m + log n)
#
# Hash table advantages:
# - Lookup/insert/delete: O(1) average
```
