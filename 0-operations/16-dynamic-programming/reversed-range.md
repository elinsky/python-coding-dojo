# Using reversed() in DP

**Q:** When do you use reversed(range()) in DP?

**A:** When you need to iterate backwards to check previous values

```python
# Iterate forward (common)
for i in range(n):
    # look at dp[0..i-1]

# Iterate backward
for i in reversed(range(n)):
    # useful when you need to look at dp[i+1..n-1]

# Common in word break problem
for j in reversed(range(i)):
    if can_break_at_j:
        # ...
        break
```

**From book:** Used in decompose_into_dictionary_words to find valid word breaks
