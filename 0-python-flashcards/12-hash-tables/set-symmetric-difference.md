# Set Symmetric Difference

**Q:** How do I get elements in either set but not both (XOR)? What is the time complexity?

**A:** Use ^ operator or symmetric_difference(). Time: O(len(s) + len(t))

```python
diff = s ^ t
diff = s.symmetric_difference(t)
```
