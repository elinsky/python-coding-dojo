# Which Counter to Create

**Q:** When checking if you can construct a letter from a magazine, should you create a Counter for the letter, the magazine, or both?

**A:** **Only the letter!**

```python
# GOOD - O(n) space
letter_counts = Counter(letter_text)
# Then iterate through magazine, decrementing counts

# BAD - O(n + m) space
letter_counts = Counter(letter_text)
magazine_counts = Counter(magazine_text)  # ← Unnecessary!
```

**Why:**
- You only need to track what characters you're **looking for** (from the letter)
- The magazine can be scanned once, decrementing the counter as you find matches
- Creating a Counter for the magazine wastes space

**Space complexity:**
- One Counter: O(n) where n = letter length
- Two Counters: O(n + m) where m = magazine length (worse!)

**When this matters:**
Magazine is typically much larger than the letter (m >> n), so avoiding the magazine Counter saves significant space.
