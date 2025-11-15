# Q: How do I add two single bits (0 or 1) without carry?

# A: XOR gives the sum bit

```python
a ^ b

# Examples:
# 0 + 0 = 0 → 0 ^ 0 = 0 ✓
# 0 + 1 = 1 → 0 ^ 1 = 1 ✓
# 1 + 0 = 1 → 1 ^ 0 = 1 ✓
# 1 + 1 = 0 (carry 1) → 1 ^ 1 = 0 ✓ (sum bit only)
```
