# Sort by Specific Attribute

**Q:** How do you sort objects by a specific attribute in greedy algorithms?

**A:** Use key parameter with operator.attrgetter or lambda.

```python
import operator

# Using attrgetter (faster):
intervals.sort(key=operator.attrgetter('right'))

# Using lambda:
intervals.sort(key=lambda x: x.right)
intervals.sort(key=lambda x: (x.end, x.start))  # Multiple keys
```
