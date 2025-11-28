# Pass 2 Indices Setup

**Q:** In replace_and_remove, after pass 1 (deletions), how do you set up readidx and writeidx for pass 2 (expansions)?

**A:**
- `readidx = writeidx - 1` (end of compacted data from pass 1)
- `writeidx = final_size - 1` (end of final result)

Save pass 1's writeidx before overwriting it.
