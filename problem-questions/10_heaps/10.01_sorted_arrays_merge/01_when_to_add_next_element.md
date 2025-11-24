# When to Add Next Element

**Q:** After popping the min element from the heap, when should you add the next element from that array?

**A:** Check if there IS a next element first:

```python
smallest = heappop(heap)
result.append(smallest.value)

# Get next element from same array
next_idx = smallest.element_idx + 1
if next_idx < len(arrays[smallest.array_idx]):  # ← Check bounds!
    next_val = arrays[smallest.array_idx][next_idx]
    heappush(heap, (next_val, smallest.array_idx, next_idx))
```

**Key point:** Only add if the array has more elements. If you're at the end of that array, don't add anything - let the heap shrink.

**Pattern:**
1. Pop min element
2. Add to result
3. Check if that array has more elements
4. If yes, push next element to heap
5. If no, do nothing (heap gets smaller)
