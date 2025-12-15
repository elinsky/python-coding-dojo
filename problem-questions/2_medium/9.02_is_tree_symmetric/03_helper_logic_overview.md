# Helper Logic Overview

**Q:** What are the cases to handle in the is_symmetric helper (high-level)?

**A:**
1. Base case: both None → True
2. One None, other not → False
3. Values don't match → False
4. Values match → recurse on mirror children
