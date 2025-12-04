# Sort in Descending Order

**Q:** How do I sort in descending order?

**A:** Use reverse=True parameter

```python
# In-place descending sort
A.sort(reverse=True)

# Return new sorted list (descending)
sorted_desc = sorted(A, reverse=True)

# With custom key
A.sort(key=lambda x: x.value, reverse=True)
```
