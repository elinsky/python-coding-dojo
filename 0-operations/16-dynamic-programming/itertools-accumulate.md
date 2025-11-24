# Using itertools.accumulate in DP

**Q:** How do you use itertools.accumulate for running sums in DP?

**A:** accumulate returns iterator of cumulative values

```python
import itertools

# Running sum
A = [1, 2, 3, 4]
running_sums = list(itertools.accumulate(A))
# [1, 3, 6, 10]

# Common DP pattern: track min/max while iterating
min_sum = max_sum = 0
for running_sum in itertools.accumulate(A):
    min_sum = min(min_sum, running_sum)
    max_sum = max(max_sum, running_sum - min_sum)
```

**From book:** Used in maximum subarray problem (find_maximum_subarray)
