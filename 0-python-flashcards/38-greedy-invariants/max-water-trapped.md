# Maximum Water Trapped by Two Lines

**Q:** How do you find two lines that trap the most water?

**A:** Two pointers from ends, move pointer with shorter height. Time: O(n)

```python
i, j = 0, len(heights) - 1
max_water = 0
while i < j:
    width = j - i
    max_water = max(max_water, width * min(heights[i], heights[j]))
    if heights[i] > heights[j]:
        j -= 1  # Move shorter side
    else:
        i += 1
return max_water
```
