# Custom Delimiter

**Q:** How do I use a different delimiter (tab, pipe, etc.) with csv.reader or csv.writer?

**A:**

```python
reader = csv.reader(f, delimiter='\t')
writer = csv.writer(f, delimiter='|')
```
