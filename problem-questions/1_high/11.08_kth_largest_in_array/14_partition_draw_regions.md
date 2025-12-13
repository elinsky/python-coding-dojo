# Partition Around Pivot: Draw Regions and Pointers

**Q:** During `partition_around_pivot`, draw the array regions and show the key pointers.

**A:**
```
[ satisfies comp | doesn't satisfy | unprocessed | pivot ]
 ^               ^                  ^             ^
 left            new_pivot_idx      i             right
```
