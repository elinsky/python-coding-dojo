# Partition for K-th Largest

**Q:** When finding the k-th **largest**, how should elements be arranged after partitioning?

**A:** Descending order (largest first):
- Elements **> pivot** go LEFT
- Elements **< pivot** go RIGHT
- Pivot ends up in the middle at its "sorted position"

This way index 0 = 1st largest, index k-1 = k-th largest.
