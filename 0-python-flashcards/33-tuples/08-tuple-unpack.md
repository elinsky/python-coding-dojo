# Unpack Tuple

**Q:** How do I unpack tuple elements into variables?

**A:** Use assignment with matching number of variables

```python
t = (1, 2, 3)
a, b, c = t  # a=1, b=2, c=3

# Extended unpacking with *
first, *middle, last = (1, 2, 3, 4, 5)
# first=1, middle=[2, 3, 4], last=5

# Swap
a, b = b, a
```
