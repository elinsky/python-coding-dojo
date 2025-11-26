# Combinations vs Permutations

**Q:** How do you ensure you count combinations (not permutations) when counting ways to reach a score?

**A:** Process one play type at a time.

- By iterating through play types in the outer loop, once you're "past" a play type, you never use it again
- This prevents counting {2,3} and {3,2} as different
- Order of play types doesn't matter - you can shuffle and get the same answer
