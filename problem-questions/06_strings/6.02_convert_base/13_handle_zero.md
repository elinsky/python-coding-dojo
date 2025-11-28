# Handling Zero

**Q:** Why do you need a special case for zero when converting int to string?

**A:** The while loop (`while num > 0`) never runs when num = 0, so you'd return empty string. Must return '0' explicitly.
