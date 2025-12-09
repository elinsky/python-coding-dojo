# pushpop vs replace

**Q:** When do you use heappushpop vs heapreplace? Give an example of each.

**A:**

**heappushpop** - "compete to get in" (new element might lose)
- Use case: Streaming top-k. Push new element, pop smallest. If new element is smallest, it's returned immediately.

**heapreplace** - "swap out" (old min is definitely leaving)
- Use case: Merging k sorted lists. Pop smallest to output, push next element from that list.
