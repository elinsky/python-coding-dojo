# Peg Role Swapping

**Q:** For `hanoi(n, FROM, TO, AUX)`, what are the parameters for the two recursive calls?

**A:**

| Step | Call | FROM | TO | AUX |
|------|------|------|-----|-----|
| 1 | `hanoi(n-1, ...)` | FROM | AUX | TO |
| 2 | `append([FROM, TO])` | - | - | - |
| 3 | `hanoi(n-1, ...)` | AUX | TO | FROM |

- Step 1: destination becomes aux, aux becomes destination
- Step 3: source becomes aux, aux becomes source
