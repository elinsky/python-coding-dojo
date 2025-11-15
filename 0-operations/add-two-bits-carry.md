# Q: When do two bits generate a carry?

# A: When BOTH are 1 (AND)

```python
a & b

# Examples:
# 0 + 0 → no carry → 0 & 0 = 0 ✓
# 0 + 1 → no carry → 0 & 1 = 0 ✓
# 1 + 0 → no carry → 1 & 0 = 0 ✓
# 1 + 1 → carry!  → 1 & 1 = 1 ✓
```
