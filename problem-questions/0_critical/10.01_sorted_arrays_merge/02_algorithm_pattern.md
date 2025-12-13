# The Merge Algorithm Pattern

**Q:** What's the step-by-step pattern for merging k sorted arrays with a heap?

**A:**

**Setup:**
1. Create empty min-heap
2. Add first element from each array to heap (with metadata)
3. Create empty result list

**Main loop (while heap not empty):**
1. Pop minimum element from heap
2. Add its value to result
3. If that array has more elements:
   - Get next element from same array
   - Push to heap (with updated index)
4. Repeat


**Key insight:** At each step, heap contains at most one element from each array (the next unprocessed one).