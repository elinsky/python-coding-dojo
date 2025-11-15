# Check if Node Exists and is Leaf

**Q:** How do I check if node exists and is a leaf?

**A:** Chain all conditions with 'and'

```python
node and not node.left and not node.right
```
