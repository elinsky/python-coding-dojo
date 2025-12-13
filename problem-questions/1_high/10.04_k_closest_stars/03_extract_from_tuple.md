# Extract from Tuple

**Q:** When using tuples in a heap like `(-distance, item)`, how do you extract just the item after `heappop`?

**A:** Index into the tuple: `heappop(heap)[1]`
