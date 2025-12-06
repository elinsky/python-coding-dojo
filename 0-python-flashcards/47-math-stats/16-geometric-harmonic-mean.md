# Geometric and Harmonic Mean

**Q:** When and how to use geometric/harmonic mean?

**A:** Use for rates, ratios, and growth calculations

```python
from statistics import geometric_mean, harmonic_mean

# Geometric mean - for growth rates, ratios
geometric_mean([1, 2, 4, 8])  # 2.828... (4th root of 64)

# Harmonic mean - for rates (speed, prices)
harmonic_mean([40, 60])  # 48.0 (average speed)

# Example: drive 60mph one way, 40mph return
# Harmonic mean gives correct average speed
```
