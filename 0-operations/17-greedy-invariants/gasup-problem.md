# Gasup Problem - Find Ample City

**Q:** How do you find the starting city where you can complete a circular route?

**A:** Find city where remaining gas is minimum - that's the ample city. Time: O(n)

```python
remaining_gas = 0
min_city, min_gas = 0, 0
for i in range(1, num_cities):
    remaining_gas += gallons[i-1] - distance[i-1] // MPG
    if remaining_gas < min_gas:
        min_city, min_gas = i, remaining_gas
return min_city
```
