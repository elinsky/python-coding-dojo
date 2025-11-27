# Handling Negative Exponents

**Q:** How do you handle negative exponents in x^y?

**A:** Convert to a positive exponent problem:

```python
if y < 0:
    x = 1.0 / x
    y = -y
```

Then compute x^y with y now positive.

**Why it works:** x^(-y) = 1/(x^y) = (1/x)^y
