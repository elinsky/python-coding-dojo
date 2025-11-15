# Reverse Next Pointers During Traversal

**Q:** How do I reverse the next pointers during traversal?

**A:** Save next, redirect current, advance prev and current

```python
temp = curr.next
curr.next = prev
prev, curr = curr, temp
```
