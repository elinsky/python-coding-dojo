# Check if Exactly One Child Exists

**Q:** How do I check if exactly one child exists?

**A:** XOR logic on children

```python
bool(node.left) != bool(node.right)
```
