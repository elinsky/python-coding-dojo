# Check Grid Bounds

**Q:** How do I check if coordinates (x, y) are within bounds of a 2D grid?

**A:** Check that both indices are within valid range

```python
if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
    # in bounds
```
