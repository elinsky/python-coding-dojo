# Track Index of Min/Max

**Q:** How do you track both the minimum value and where it occurred?

**A:** Use tuple or namedtuple to store both value and index.

```python
min_city, min_gas = 0, 0
for i in range(num_cities):
    remaining_gas += gallons[i] - distance[i]
    if remaining_gas < min_gas:
        min_city, min_gas = i, remaining_gas
return min_city
```
