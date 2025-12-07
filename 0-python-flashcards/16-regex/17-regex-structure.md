# Regex Pattern Structure

**Q:** What is the general order of components in a regex pattern?

**A:**

1. `^` (optional start anchor)
2. One or more pattern pieces, each: (what to match)(quantifier)
3. `$` (optional end anchor)

Example: `^\d{3}-\d{4}$`
- `^` start
- `\d{3}` three digits
- `-` literal dash
- `\d{4}` four digits
- `$` end
