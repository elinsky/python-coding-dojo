# Check if Set is Subset

**Q:** How do I check if set s is a subset of set t? What is the time complexity?

**A:** Use <= operator or issubset() method. Time: O(len(s)) average

```python
if s <= t:
    # s is subset of t
if s.issubset(t):
    # s is subset of t
```
