# Get Sorted Copy

**Q:** How do I get a sorted copy without modifying the original?

**A:** Use sorted() function

```python
A = [3, 1, 4, 1, 5]
B = sorted(A)  # [1, 1, 3, 4, 5]
# A is unchanged

# Works on any iterable
sorted("hello")  # ['e', 'h', 'l', 'l', 'o']
```
