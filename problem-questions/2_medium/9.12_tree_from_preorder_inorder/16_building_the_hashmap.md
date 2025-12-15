# Building the Hashmap

**Q:** What hashmap do you build, and why?

**A:**
**Key:** inorder value
**Value:** index in inorder array

`{value: index for index, value in enumerate(inorder)}`

**Why:** To find the root's position in inorder in O(1). Without it, you'd search linearly each recursion, making the algorithm O(n²) instead of O(n).
