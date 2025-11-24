# Append Sentinel Value

**Q:** How do you uniformly handle remaining stack elements after iteration?

**A:** Append sentinel value (like 0 or float('inf')) to trigger final processing.

```python
# For skyline problem:
for i, h in enumerate(heights + [0]):  # 0 blocks all remaining
    while stack and heights[stack[-1]] >= h:
        process(stack.pop())
    stack.append(i)
# No need for separate loop to flush stack
```
