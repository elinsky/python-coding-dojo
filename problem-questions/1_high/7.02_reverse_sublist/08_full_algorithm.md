# Full Algorithm

**Q:** Describe the full algorithm for reverse_sublist(L, start, finish).

**A:**
1. Create dummy node pointing to L
2. Advance `start - 1` times to position `sublist_head` (node before sublist)
3. Set `sublist_iter = sublist_head.next` (first node of sublist)
4. Loop `finish - start` times:
   - Save pointer to node after `sublist_iter`
   - Cut it out of chain
   - Splice it in at front (after `sublist_head`)
5. Return `dummy.next`
