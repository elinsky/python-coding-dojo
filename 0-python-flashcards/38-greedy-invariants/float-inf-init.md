# Initialize with -inf/+inf

**Q:** How do you initialize min/max tracking variables?

**A:** Use float('-inf') for max, float('inf') for min.

```python
max_value = float('-inf')  # Will be replaced by any value
min_value = float('inf')   # Will be replaced by any value

last_visit_time = float('-inf')  # Start before everything
```
