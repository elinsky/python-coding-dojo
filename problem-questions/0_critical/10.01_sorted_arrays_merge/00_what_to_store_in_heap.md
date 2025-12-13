# What to Store in Heap

**Q:** When merging k sorted arrays with a min-heap, what information must each heap entry contain?

**A:** Three pieces of information:
1. **Value** - the actual element (for comparison/ordering)
2. **Array index** - which array this element came from
3. **Element index** - position in that array (so you can find the next element)

**Example:**
```python
heap_entry = (value, array_idx, element_idx)
# or using namedtuple:
ArrayEntry = namedtuple('ArrayEntry', ['value', 'array_idx', 'element_idx'])
heap_entry = ArrayEntry(value=3, array_idx=0, element_idx=2)
```

**Why each field:**
- **Value**: Heap needs this to maintain min-heap property
- **Array index**: When you pop this element, you need to know which array to get the next element from
- **Element index**: You need to know which position to access next in that array

**Common mistake:** Storing the value twice instead of storing the element index.
