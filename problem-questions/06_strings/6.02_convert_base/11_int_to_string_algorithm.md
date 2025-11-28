# Int to String Algorithm

**Q:** Describe the algorithm to convert a base 10 int to a string in base b.

**A:**
1. Start with empty list
2. While num > 0:
   - Extract least significant digit (num % base)
   - Convert digit value (base 10) to character (base b) using hexdigits lookup
   - Append character to list
   - Remove least significant digit (num // base)
3. Reverse list and join into string
