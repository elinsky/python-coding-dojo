# Open with Path Object

**Q:** Can I pass a Path object directly to open()?

**A:** Yes

```python
p = Path('data.csv')
with open(p) as f:
```
