# Handling Negative Numbers

**Q:** How do you handle negative numbers in base conversion?

**A:**
1. Check if first char is '-': `is_negative = s[0] == '-'`
2. Skip the sign when parsing: `s[1:]` or `s[is_negative:]`
3. Prepend '-' to result if was negative
