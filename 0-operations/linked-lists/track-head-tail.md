# Track Both Head and Tail

**Q:** How do I track both head and tail of a growing list?

**A:** Keep two pointers, update tail when appending

```python
head = tail = ListNode()
# When appending:
tail.next = new_node
tail = tail.next
```
