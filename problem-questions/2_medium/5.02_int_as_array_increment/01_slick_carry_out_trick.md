# The Slick Carry-Out Trick

**Q:** When `plus_one` on `[9,9,9]` produces a carry-out, how do you grow the array in O(1) time instead of inserting at the front?

**A:** After the carry loop, `A[0] == 10` means carry-out. Since the result must be `10...0`:
```python
A[0] = 1
A.append(0)
```
Appending is O(1) amortized vs O(n) for inserting at index 0.
