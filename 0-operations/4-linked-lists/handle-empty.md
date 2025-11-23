# Handle Empty List Case

**Q:** How do I check if a list is empty (head is None) before accessing it? What is the time complexity?

**A:** Check if L is None before accessing. Time: O(1)

```python
if not L:
    return None
```
