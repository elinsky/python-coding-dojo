# Get Hash Value

**Q:** How do I get the hash value of an object?

**A:** Use hash() function (object must be hashable)

```python
hash("hello")  # Some integer
hash((1, 2, 3))  # Tuples are hashable
# hash([1, 2, 3])  # TypeError - lists not hashable
```
