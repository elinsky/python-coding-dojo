# Return Type

**Q:** What does `compute_tower_hanoi(n)` return?

**A:** A `List[List[int]]` - a list of moves, where each move is `[from_peg, to_peg]`.

- Pegs are indexed 0, 1, 2
- Example: `[[0, 2], [0, 1], [2, 1]]` means:
  1. Move top ring from peg 0 to peg 2
  2. Move top ring from peg 0 to peg 1
  3. Move top ring from peg 2 to peg 1
