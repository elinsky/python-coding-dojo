# Handle Empty List Case

**Q:** How do I handle the case where list might be empty? What is the time complexity?

**A:** Check if L is None before accessing. Time: O(1)

```python
if not L:
    return None
```
