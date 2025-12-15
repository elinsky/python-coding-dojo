# Recursive Calls

**Q:** When values match, what do you recurse on in the is_symmetric helper?

**A:**
- `helper(left.left, right.right)`
- `helper(left.right, right.left)`

Compare outer children together, inner children together.
