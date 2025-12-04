# Reverse Next Pointers During Traversal

**Q:** How do I reverse the next pointers during traversal? What is the time complexity?

**A:** Save next, redirect current, advance prev and current. Time: O(1)

```python
temp = curr.next
curr.next = prev
prev, curr = curr, temp
```
