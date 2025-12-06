# Path Relative to Script

**Q:** How do I get a path relative to the script file (not cwd)?

**A:**

```python
script_dir = Path(__file__).parent
data_path = script_dir / 'data.txt'
```
