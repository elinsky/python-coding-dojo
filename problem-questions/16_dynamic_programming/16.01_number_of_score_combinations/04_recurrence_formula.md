# Recurrence Formula

**Q:** In words, how do you calculate the number of ways to make score S using plays 0 through P?

**A:** Add two values:

1. **Ways to make score S without using play P** → look at previous row (same score)
2. **Ways to make score S using play P at least once** → look at score (S minus play P's value) in the same row

If there's no previous row, case 1 is 0.
If the score is smaller than play P's value, case 2 is 0.
