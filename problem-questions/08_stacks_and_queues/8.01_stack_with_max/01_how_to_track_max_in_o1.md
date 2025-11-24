# How to Track Max in O(1)

**Q:** How can you track the maximum of a stack in O(1) time?

**A:** Maintain a second "max stack" that only stores maximums. Push when new max arrives, pop when current max is removed.
