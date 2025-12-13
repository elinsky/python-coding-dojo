# Two Pointers for Reversal

**Q:** In reverse_sublist, what two pointers do you need for the reversal, and where do they point?

**A:**
- `sublist_head`: node BEFORE the sublist (stays fixed)
- `sublist_iter`: first node OF the sublist (stays on same node, ends up last)
