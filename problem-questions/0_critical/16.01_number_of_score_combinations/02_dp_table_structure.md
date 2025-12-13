# DP Table Structure

**Q:** What do the rows and columns represent in the score combinations DP table?

**A:**
- **Rows:** Each play type (e.g., row 0 = only 2s, row 1 = 2s and 3s)
- **Columns:** Target scores from 0 to final_score
- **Cell value:** Number of ways to make that score using plays from rows 0 to current row
