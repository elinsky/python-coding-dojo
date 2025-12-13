# Move Node to Front (Code)

**Q:** What are the 4 pointer operations to move `sublist_iter.next` to the front of the sublist?

**A:**
```python
node_to_move = sublist_iter.next          # 1. save pointer to node to move
sublist_iter.next = node_to_move.next     # 2. cut it out of chain
node_to_move.next = sublist_head.next     # 3. splice: point to current front
sublist_head.next = node_to_move          # 4. splice: becomes new front
```
