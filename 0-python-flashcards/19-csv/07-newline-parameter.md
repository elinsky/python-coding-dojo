# CSV newline Parameter

**Q:** Why must you use newline='' when opening CSV files?

**A:** Prevents double newlines on Windows and lets csv module handle line endings correctly

```python
# CORRECT
with open('data.csv', newline='') as f:
    reader = csv.reader(f)

# WRONG - may cause issues with quoted fields containing newlines
with open('data.csv') as f:
    reader = csv.reader(f)
```
