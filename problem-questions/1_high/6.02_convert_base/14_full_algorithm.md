# Full Algorithm

**Q:** Describe the full algorithm for convert_base(num_as_string, b1, b2).

**A:**
1. Handle negative: check for '-', strip it, remember for later
2. **String → Int (base b1 → base 10):**
   - For each character left to right:
     - Convert char to digit (hexdigits lookup)
     - Shift result left (multiply by b1)
     - Add digit
3. If num is 0, return '0'
4. **Int → String (base 10 → base b2):**
   - While num > 0:
     - Extract least significant digit (num % b2)
     - Convert digit to char (hexdigits lookup)
     - Append to list
     - Remove digit (num // b2)
   - Reverse list and join
5. Prepend '-' if was negative
