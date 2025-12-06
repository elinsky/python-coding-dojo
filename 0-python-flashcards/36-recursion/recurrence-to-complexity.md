# Recurrence to Time Complexity

**Q:** How do I solve common recurrences for time complexity?

**A:** Learn standard patterns

```python
# T(n) = T(n-1) + O(1) → O(n)
# Example: factorial, linear search

# T(n) = T(n-1) + O(n) → O(n²)
# Example: bubble sort, selection sort

# T(n) = 2T(n-1) + O(1) → O(2^n)
# Example: fibonacci (naive), generating subsets

# T(n) = 2T(n/2) + O(n) → O(n log n)
# Example: merge sort

# T(n) = T(n/2) + O(1) → O(log n)
# Example: binary search
```
