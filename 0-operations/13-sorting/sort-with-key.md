# Sort with Custom Key

**Q:** How do I sort using a custom key function?

**A:** Use the key parameter with a lambda or function

```python
# Sort by string representation
A.sort(key=lambda x: str(x))

# Sort students by GPA
students.sort(key=lambda student: student.grade_point_average)

# Sort by absolute value
A.sort(key=abs)
```
