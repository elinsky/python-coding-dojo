# Heap Approach: Which Type?

**Q:** For finding the k-th largest with a heap of size k, which type of heap should you use and why?

**A:** Use a **min-heap**.

The heap holds the k largest elements seen so far. The smallest of those k (the heap's min) is the k-th largest overall.

- Min-heap gives O(1) access to the smallest element
- When a new element is larger than the min, swap it in
- Max-heap would give the 1st largest, not the k-th
