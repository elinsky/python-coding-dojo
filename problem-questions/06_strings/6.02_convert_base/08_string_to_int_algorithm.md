# String to Int Algorithm

**Q:** Describe the algorithm to convert a string in base b to a base 10 int.

**A:**
1. Start with result = 0
2. For each character left to right:
   - Convert character (base b) to digit value (base 10) using hexdigits lookup
   - Shift result left (multiply by base)
   - Add digit to result
3. Return result
