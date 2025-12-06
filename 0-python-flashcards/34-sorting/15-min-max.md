# Find Min/Max Element

**Q:** How do I find the min/max element?

**A:** Use min() or max() with optional key

```python
A = [3, 1, 4, 1, 5]
min(A)  # 1
max(A)  # 5

# With key
shortest = min(words, key=len)
oldest = max(students, key=lambda s: s.age)
```
