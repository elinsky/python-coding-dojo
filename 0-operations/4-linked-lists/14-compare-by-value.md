# Compare Nodes by Value

**Q:** How do I compare nodes by value rather than identity? What is the time complexity?

**A:** Use == on data fields. Time: O(1)

```python
if node1.data == node2.data:
```
