# Create Hash Map for Vertex Tracking

**Q:** How do I create a hash map to track vertex states or mappings?

**A:** Use a dictionary mapping vertices to values

```python
vertex_map = {}
vertex_map[v] = some_value
# or for cloning
vertex_map = {original: GraphVertex(original.label)}
```
