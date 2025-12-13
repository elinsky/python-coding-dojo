# Partition Around Pivot: Core Loop Action (Conceptual)

**Q:** For each element during the scan, what comparison is made and what are the cases?

**A:**

**Comparison:** Check whether the current element belongs on the "preferred" side:
Does `comp(A[i], pivot_value)` hold?

**Cases:**
- **Case 1 – True:** Element satisfies `comp` → move it to the left partition and advance the boundary (`new_pivot_idx`)
- **Case 2 – False:** Element does not satisfy `comp` → leave it in place; continue scanning
