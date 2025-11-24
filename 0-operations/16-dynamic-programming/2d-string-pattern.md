# 2D DP String Pattern

**Q:** What's the pattern for DP comparing two strings (A and B)?

**A:** Use dp[i][j] for prefixes A[0:i] and B[0:j]

```python
# dp[i][j] = answer for A[0:i] and B[0:j]
dp = [[0] * (len(B)+1) for _ in range(len(A)+1)]

# Base cases: i=0 or j=0
for i in range(len(A)+1):
    dp[i][0] = base_i

for j in range(len(B)+1):
    dp[0][j] = base_j

# Fill table
for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        # Compare A[i-1] with B[j-1]
        if A[i-1] == B[j-1]:
            dp[i][j] = # ...
        else:
            dp[i][j] = # ...
```
