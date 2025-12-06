# Get N Smallest/Largest

**Q:** How do I efficiently get the n smallest/largest elements?

**A:** Use heapq.nsmallest() or nlargest()

```python
import heapq

data = [5, 2, 8, 1, 9, 3, 7]
smallest = heapq.nsmallest(3, data)  # [1, 2, 3]
largest = heapq.nlargest(3, data)  # [9, 8, 7]

# With key
top = heapq.nlargest(3, students, key=lambda s: s.gpa)
```
