# Flush Buffer

**Q:** How do I force write buffer to disk?

**A:** Use flush()

```python
with open('log.txt', 'w') as f:
    f.write('Important log entry')
    f.flush()  # Force write to disk now

# Useful for:
# - Real-time logging
# - Long-running processes
# - When you need data visible to other processes
```

Note: close() and exiting 'with' also flush automatically.
