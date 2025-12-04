# Check Sort Stability

**Q:** Which Python sorts are stable?

**A:** sorted() and list.sort() are both stable

```python
# Stable: equal elements keep original order
# Example: [(A,2), (B,1), (C,2)] sorted by value
# Result: [(B,1), (A,2), (C,2)]  # A before C preserved

students.sort(key=lambda s: s.grade)  # Stable
sorted_students = sorted(students, key=lambda s: s.grade)  # Stable
```
