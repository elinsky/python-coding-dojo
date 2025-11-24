# When Greedy Fails

**Q:** What should you remember about greedy algorithms?

**A:** Greedy doesn't always produce optimal solution - must prove correctness or find counterexample.

```python
# Coin change for {1,6,3,4} with target 6:
# Greedy: 6 (one coin)
# Greedy for {30,24,12,6,3,1} with target 48:
# Wrong: 30+12+6 (3 coins)
# Optimal: 24+24 (2 coins)
```
