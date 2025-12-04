# Tuple as Dict Key

**Q:** Why can tuples be used as dict keys?

**A:** Tuples are immutable and hashable (if all elements are hashable)

```python
locations = {
    (0, 0): "origin",
    (1, 2): "point A",
}

coords = {(0, 0), (1, 1)}  # Set of tuples
```
