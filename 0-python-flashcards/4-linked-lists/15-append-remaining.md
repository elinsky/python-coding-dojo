# Append Remaining Nodes

**Q:** How do I append remaining nodes from L1 or L2? What is the time complexity?

**A:** Use or operator (takes first truthy value). Time: O(1)

```python
tail.next = L1 or L2
```
