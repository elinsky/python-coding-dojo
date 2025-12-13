# Return Structure

**Q:** What's a clean way to return both balanced status and height?

**A:** Use a `namedtuple`:

```python
BalancedStatusWithHeight = collections.namedtuple(
    'BalancedStatusWithHeight', ('balanced', 'height'))

return BalancedStatusWithHeight(is_balanced, height)
```

This makes the code more readable than returning `(bool, int)`.
