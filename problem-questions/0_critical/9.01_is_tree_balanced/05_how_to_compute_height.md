# How to Compute Height

**Q:** How do you compute the height of the current node from its children's heights?

**A:** `height = max(left_result.height, right_result.height) + 1`

Take the taller child's height and add 1 for the current level.
