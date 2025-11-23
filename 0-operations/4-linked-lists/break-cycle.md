# Break Cycle / Make New Tail

**Q:** How do I break a cycle/make a node the new tail? What is the time complexity?

**A:** Set its next to None. Time: O(1)

```python
node.next = None
```
