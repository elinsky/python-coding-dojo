# Converting Recursion to Iteration for O(1) Space

**Q:** Your recursive power solution uses O(log y) space from the call stack. How do you convert it to O(1) space?

**A:** Use a while loop with bit manipulation:

```python
result = 1.0
while y:
    if y & 1:        # if y is odd
        result *= x
    x *= x           # square x
    y >>= 1          # halve y
return result
```

**Key insight:** Instead of recursing down and building up, iterate through bits of y from LSB to MSB. Each bit position corresponds to a power of 2 in the exponent.
