# Trust the Recursion Mindset

**Q:** What is the mental model for reasoning about Hanoi recursion?

**A:** Only think about the **bottom ring** of your current subproblem.

- "I need to move the bottom ring from A to B"
- "I can't do that until all rings above it are gone"
- "I'll trust recursion to move those n-1 rings to C"
- "Now I move the bottom ring"
- "I'll trust recursion to move those n-1 rings from C to B"

You never think about individual moves within the recursive calls - that's handled for you.
