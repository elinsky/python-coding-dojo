# Missing IP Problem - Core Insight

**Q:** Given ~1 billion 32-bit IP addresses in a file with limited RAM, what's the key insight to find a missing IP?

**A:** Split the 32-bit space into buckets by upper bits. Count IPs per bucket. A bucket with fewer than max capacity must be missing at least one IP. Then search within that bucket.
