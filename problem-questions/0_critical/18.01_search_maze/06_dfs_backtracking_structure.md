# DFS Backtracking Structure

**Q:** What's the structure of a recursive DFS backtracking function for path-finding?

**A:**
```
mark current as visited
add current to path
if current is goal:
    return True
for each neighbor:
    if valid and unvisited:
        if recurse(neighbor) returns True:
            return True
pop from path
return False
```
