# Optimization Strategy for Slow Operations

**Q:** When augmenting a data structure with a new operation that would otherwise be slow (e.g., O(n) max on a stack), what's the key strategy?

**A:** Cache/precompute the result using auxiliary space. Trade space for time.

Note: This applies when you're constrained to a particular data structure but need to add an operation. If you can change the data structure entirely, consider using a more suitable one instead.
