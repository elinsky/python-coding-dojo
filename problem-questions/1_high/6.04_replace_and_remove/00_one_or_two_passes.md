# One or Two Passes

**Q:** In replace_and_remove (delete 'b', replace 'a' with 'dd'), can you do it in one pass? Why or why not?

**A:** No. Deletions shrink, expansions grow. One pass can't handle both - write pointer would either fall behind or get ahead, overwriting needed data.
