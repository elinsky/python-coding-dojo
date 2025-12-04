# Sort by Multiple Keys

**Q:** How do I sort by multiple criteria?

**A:** Return tuple from key function

```python
# Sort by grade (ascending), then name (ascending)
students.sort(key=lambda s: (s.grade, s.name))

# Sort by grade (descending), then name (ascending)
students.sort(key=lambda s: (-s.grade, s.name))
```
