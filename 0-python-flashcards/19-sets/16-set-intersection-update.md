# Set Intersection Update (In-place)

**Q:** How do I keep only elements also in another set (in-place)?

**A:** Use &= operator or intersection_update()

```python
s &= t
s.intersection_update(t)
```
