# Why No Ring Size Tracking

**Q:** Why doesn't the algorithm need to track ring sizes/widths?

**A:** The recursion guarantees legal moves by construction.

- You're always moving the **top ring** of a given peg
- At each recursive level, you only think about moving n rings from A to B
- You never choose between multiple rings - the structure dictates which ring moves
- If you follow the recursive pattern, you'll never violate the "no larger on smaller" rule
