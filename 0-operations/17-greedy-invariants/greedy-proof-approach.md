# Proving Greedy Correctness

**Q:** How do you prove a greedy algorithm is optimal?

**A:** Show you can swap any non-greedy choice with greedy choice without making solution worse (exchange argument).

```python
# Proof strategy:
# 1. Consider any optimal solution
# 2. Show greedy choice appears in some optimal solution
# 3. Prove remaining subproblem is also optimal
# 4. Use induction
```
