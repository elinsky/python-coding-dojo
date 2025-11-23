# Connect Tail to Node (Make Cycle)

**Q:** How do I connect the tail of a list to another node (make cycle)? What is the time complexity?

**A:** Set tail.next to the target node. Time: O(1)

```python
tail.next = target_node
```
