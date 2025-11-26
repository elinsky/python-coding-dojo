# Recursive Formula

**Q:** What is the recursive "formula" for Hanoi (like `fib(n) = fib(n-1) + fib(n-2)`)?

**A:**
```
hanoi(n, from, to, aux) =
    hanoi(n-1, from, aux, to)   # move n-1 rings to auxiliary
    + [[from, to]]               # move bottom ring (record this move)
    + hanoi(n-1, aux, to, from)  # move n-1 rings to destination
```

The result is a **concatenation of move lists**, not a sum of numbers.
