# Mark Cell as Visited In-Place

**Q:** How do I mark a cell as visited in-place (for grid problems)?

**A:** Flip or change the cell value to indicate visited

```python
grid[x][y] = BLACK  # or any marker value
# or flip boolean
grid[x][y] = 1 - grid[x][y]
```
