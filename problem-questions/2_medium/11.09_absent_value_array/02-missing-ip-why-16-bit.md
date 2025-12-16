# Missing IP Problem - Why 16-bit Split

**Q:** Why split 32-bit IPs into upper 16 and lower 16 bits for the missing IP problem?

**A:** Creates 2^16 = 65,536 buckets, each holding up to 65,536 IPs. Counter array needs only 65,536 integers. Small enough for limited RAM while still narrowing the search space.
