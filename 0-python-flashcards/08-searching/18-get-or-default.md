# Get Element at Index or Default

**Q:** How do I get element at index or default?

**A:** Use ternary with bounds check

```python
A[i] if 0 <= i < len(A) else default
```
