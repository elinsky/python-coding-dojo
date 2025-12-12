# When to Pop

**Q:** In recursive DFS backtracking, when does a node get popped from the path?

**A:** Each recursive call pops the node it added, but only after all its neighbors have been tried and failed.
