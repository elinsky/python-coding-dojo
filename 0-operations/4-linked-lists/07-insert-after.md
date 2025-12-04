# Insert Node After Current

**Q:** How do I insert a new_node after an existing node? What is the time complexity?

**A:** Set new_node.next to node.next, then update node.next. Time: O(1)

```python
new_node.next = node.next
node.next = new_node
```
