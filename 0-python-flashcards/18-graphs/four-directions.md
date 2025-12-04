# Four Directional Neighbors

**Q:** How do I get all 4 adjacent neighbors (up, down, left, right) in a grid?

**A:** Use direction offsets: (0, 1), (0, -1), (1, 0), (-1, 0)

```python
for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
    next_x, next_y = x + dx, y + dy
```
