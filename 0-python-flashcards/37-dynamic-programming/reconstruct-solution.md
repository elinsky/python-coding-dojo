# Reconstruct Solution Pattern

**Q:** How do you reconstruct the actual solution, not just the optimal value?

**A:** Store parent/choice at each state, then backtrack

```python
# During DP, store which choice led to optimal
parent = [None] * n

for i in range(n):
    best_choice = # ... compute best
    dp[i] = # ... optimal value
    parent[i] = best_choice

# Reconstruct by following parents
path = []
i = n-1
while i >= 0:
    path.append(i)
    i = parent[i]
path.reverse()
```
