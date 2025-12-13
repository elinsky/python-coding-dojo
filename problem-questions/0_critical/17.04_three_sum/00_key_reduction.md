# Key Reduction

**Q:** What's the key insight for solving 3-sum optimally?

**A:** Reduce 3-sum to 2-sum.

- For each element `a`, check if two elements sum to `(target - a)`
- 2-sum can be solved in O(n) time
- Doing 2-sum n times gives O(n²) total
