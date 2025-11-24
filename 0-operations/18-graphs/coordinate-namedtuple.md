# Create Coordinate Named Tuple

**Q:** How do I create a Coordinate namedtuple for grid problems?

**A:** Use collections.namedtuple with x and y fields

```python
Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))
coord = Coordinate(row, col)
```
