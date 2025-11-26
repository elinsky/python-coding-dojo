# Why Compute Smaller Scores

**Q:** If I only want the answer for score 6, why do I need to compute scores 0, 1, 2, 3, 4, 5?

**A:** Larger scores depend on smaller scores.

To compute "ways to make 6 using a 3", you need "ways to make 3" first.

- To know score 6, I need score 3 (if I use a 3)
- To know score 3, I need score 0 (if I use a 3)
- Score 0 is the base case (1 way: do nothing)

This is the essence of dynamic programming: build up from smaller subproblems.
