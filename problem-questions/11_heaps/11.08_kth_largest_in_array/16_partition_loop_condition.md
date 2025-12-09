# Partition Around Pivot: Loop Condition

**Q:** What is the loop condition in `partition_around_pivot`?

**A:**
```python
for i in range(left, right):
```

The loop scans all elements from `left` up to `right - 1`, stopping before the pivot (which sits temporarily at `A[right]`).
