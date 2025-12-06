# Common DP Mistake: Splitting in Half

**Q:** Why is splitting the problem in half (like quicksort) usually wrong for DP?

**A:** Splitting [0, n] into [0, n/2] and [n/2+1, n] usually doesn't provide enough info to solve original problem

```python
# WRONG approach (divide and conquer style)
def solve(arr, left, right):
    mid = (left + right) // 2
    left_result = solve(arr, left, mid)
    right_result = solve(arr, mid+1, right)
    # Usually can't combine these to get answer!
    return combine(left_result, right_result)

# RIGHT approach: relate to previous elements
def solve(arr):
    dp = [0] * len(arr)
    for i in range(len(arr)):
        # Use dp[i-1], dp[i-2], etc.
        dp[i] = f(dp[i-1], dp[i-2], arr[i])
```

**Tip from book:** "A common mistake is trying to split into two equal halves"
