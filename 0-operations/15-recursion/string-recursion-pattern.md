# String Recursion Pattern

**Q:** What are common patterns for recursing on strings?

**A:** Process first/last char, recurse on substring OR use indices

```python
# Pattern 1: First char + rest
def is_palindrome(s):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and is_palindrome(s[1:-1])

# Pattern 2: Index-based (avoids string copies)
def is_palindrome_idx(s, left=0, right=None):
    if right is None:
        right = len(s) - 1
    if left >= right:
        return True
    return s[left] == s[right] and is_palindrome_idx(s, left + 1, right - 1)
```
