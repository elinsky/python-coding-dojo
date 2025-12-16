# Missing IP Problem - Pigeonhole Principle

**Q:** In the missing IP problem, why is at least one bucket guaranteed to have count < 65,536?

**A:** ~1 billion IPs spread across 65,536 buckets, but each bucket can only hold 65,536 unique IPs. If all buckets were full, we'd have 2^32 = 4 billion IPs. Since we only have ~1 billion, many buckets are incomplete.
