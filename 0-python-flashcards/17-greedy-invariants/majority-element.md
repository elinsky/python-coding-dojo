# Majority Element (Boyer-Moore)

**Q:** How do you find the majority element (>n/2 occurrences) in one pass with O(1) space?

**A:** Use Boyer-Moore voting: track candidate and count, cancel pairs of different elements.

```python
candidate, count = None, 0
for element in stream:
    if count == 0:
        candidate, count = element, 1
    elif candidate == element:
        count += 1
    else:
        count -= 1  # Cancel out
return candidate
```
