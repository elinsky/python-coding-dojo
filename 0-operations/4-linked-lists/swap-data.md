# Swap Node Data

**Q:** How do I swap the data of two nodes? What is the time complexity?

**A:** Use tuple unpacking. Time: O(1)

```python
node1.data, node2.data = node2.data, node1.data
```
