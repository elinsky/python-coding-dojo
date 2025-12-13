# Move Node to Front (Concept)

**Q:** What are the steps to move a node to the front of the sublist (no code)?

**A:**
1. Save a pointer to the node to move (the one after `sublist_iter`)
2. Cut it out of the chain
3. Splice it in at the front (right after `sublist_head`)
