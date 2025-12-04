from typing import List

from test_framework import generic_test
import heapq


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]
    # Keep the following invariants during partitioning:
    # bottom group: A[:smaller].
    # middle group: A[smaller:equal].
    # unclassified group: A[equal:larger].
    # top group: A[larger:].
    smaller, equal, larger = 0, 0, len(A)
    # Keep iterating as long as there is an unclassified element.
    while equal < larger:
        # A[equal] is the incoming unclassified element.
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else:  # A[equal] > pivot.
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int]) -> int:
    # i really have no idea how to approach this one.
    # I guess i could sort. That would take O(n log(n)) time. 
    # would take no space. then i can just return the k-th value
    # presumably threres a faster way thah thatthough
    # could use a heap. would get time complexity of O(n).
    # spce complexity would be k
    # probably an answer with space complexity of 1, but going with this soltuion
    heap = []
    for idx in range(0, k):
        heapq.heappush(heap, A[idx]) 
    for idx in range(k, len(A)):
        heapq.heappush(heap, A[idx])
        heapq.heappop(heap)
    # for _ in range(0, k-1):
    #     heapq.heappop(heap)

    return heapq.heappop(heap)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
