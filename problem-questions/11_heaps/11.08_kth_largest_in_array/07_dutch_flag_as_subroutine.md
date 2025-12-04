# Dutch Flag as Subroutine

**Q:** How does Dutch Flag partition relate to quickselect?

**A:** Dutch Flag is the partition subroutine. It:
1. Takes a pivot index and array bounds `[left, right]`
2. Rearranges so elements > pivot go left, < pivot go right
3. Returns the pivot's final position

For quickselect, treat it as a black box: "put pivot in sorted position, return that position."
