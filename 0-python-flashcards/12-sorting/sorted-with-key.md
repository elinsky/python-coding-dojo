# Get Sorted Copy with Key

**Q:** How do I get a sorted copy using a custom key?

**A:** Use sorted() with key parameter

```python
# Original unchanged, returns new list
students_by_name = sorted(students)

# Sort by custom key
students_by_gpa = sorted(students,
    key=lambda s: s.grade_point_average)
```
