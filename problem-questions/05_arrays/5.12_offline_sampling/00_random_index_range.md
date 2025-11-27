# Random Sampling: Random Index Range

**Q:** When generating a random sample of size k by swapping elements into positions `0, 1, 2, ... k-1`, what range should you pick the random index from when filling position `i`?

**A:** `[i, n-1]` - only select from the unseen portion.

Why not `[0, n-1]`:
- An element placed at position 0 could get swapped out when filling later positions
- This changes the probabilities and destroys uniformity

Elements in `[0, i-1]` are "locked in" - each gets exactly one opportunity to land in each position.
