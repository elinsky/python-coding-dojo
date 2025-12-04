# Sort with Custom Key

**Q:** How do I sort using a custom key function?

**A:** Use the key parameter

```python
A.sort(key=len)  # Sort by length
A.sort(key=str.lower)  # Case-insensitive
A.sort(key=lambda x: x.grade)  # By attribute
```
