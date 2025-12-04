# Reverse a List

**Q:** How do I reverse a list (not sort in reverse)?

**A:** Use reverse() method or reversed() function

```python
A = [1, 2, 3, 4, 5]

A.reverse()  # In-place: [5, 4, 3, 2, 1]

rev = list(reversed(A))  # New list
rev = A[::-1]  # Slice (new list)
```
