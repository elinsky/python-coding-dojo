# Interval Covering Problem

**Q:** How do you find minimum points to cover all intervals?

**A:** Sort by right endpoint, greedily select right endpoint of earliest-ending uncovered interval.

```python
intervals.sort(key=lambda x: x[1])  # Sort by right endpoint
last_visit = float('-inf')
visits = 0
for interval in intervals:
    if interval[0] > last_visit:  # Not covered
        last_visit = interval[1]  # Pick right endpoint
        visits += 1
```
