# Minimize Waiting Time

**Q:** How do you minimize total waiting time when processing queries?

**A:** Sort by service time (ascending) and process shortest first.

```python
service_times.sort()
total_waiting = 0
for i, time in enumerate(service_times):
    num_remaining = len(service_times) - (i + 1)
    total_waiting += time * num_remaining
```
