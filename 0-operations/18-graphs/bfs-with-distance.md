# BFS with Distance Tracking

**Q:** How do I track distance/level during BFS?

**A:** Use a namedtuple or pair to store (vertex, distance)

```python
VertexWithDistance = collections.namedtuple(
    'VertexWithDistance', ('vertex', 'distance'))
q = collections.deque([VertexWithDistance(s, 0)])
```
