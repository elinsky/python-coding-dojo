# Sort Stability

**Q:** Is Python's sort stable?

**A:** Yes, both sorted() and list.sort() are stable

```python
# Stable: equal elements keep original order
# [(A,2), (B,1), (C,2)] sorted by value
# Result: [(B,1), (A,2), (C,2)]  # A before C preserved

# Use stability for multi-key sort:
students.sort(key=lambda s: s.name)  # First by name
students.sort(key=lambda s: s.grade)  # Then by grade
```
