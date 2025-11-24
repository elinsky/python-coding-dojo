# Graph Vertex Coloring (3-Color DFS)

**Q:** How do I set up 3-color vertex marking for DFS (white/gray/black)?

**A:** Use an enum or constants: WHITE (unvisited), GRAY (processing), BLACK (finished)

```python
WHITE, GRAY, BLACK = range(3)
# or
class GraphVertex:
    white, gray, black = range(3)
    def __init__(self):
        self.color = GraphVertex.white
```
