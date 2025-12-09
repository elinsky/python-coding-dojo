# Partition Around Pivot: Major Steps (Big Picture)

**Q:** What are the major steps of `partition_around_pivot` in rough pseudocode?

**A:**
1. Move the pivot element to the end of the range
2. Loop over all elements from `left` to `right - 1`
3. For each element:
   - If it satisfies `comp(A[i], pivot_value)`, swap it to the left partition and advance the boundary
4. After the loop, move the pivot value into its final position between the two partitions
5. Return the pivot's new index
