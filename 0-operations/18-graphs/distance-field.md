# Initialize Distance Field in Vertex

**Q:** How do I initialize a distance/level field for BFS?

**A:** Add distance field to vertex class, initialize to -1 or 0

```python
class GraphVertex:
    def __init__(self):
        self.d = -1  # -1 means unvisited
        self.edges = []
```
