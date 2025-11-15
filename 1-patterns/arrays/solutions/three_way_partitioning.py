def dutch_flag_partition(pivot_index: int, A: list[int]) -> None:
    """
    Pattern: Three-Way Partitioning with Invariants

    Goal: Partition into 3 regions (less/equal/greater) in one pass

    When to use: Categorizing elements into multiple groups
    Problems that use it: Dutch flag, sort colors, 3-way quicksort partition
    Key insight: Maintain invariants for 4 regions: bottom/middle/unclassified/top
    """
    pivot = A[pivot_index]
    smaller, equal, larger = 0, 0, len(A)

    # Invariants:
    # A[:smaller] = elements < pivot
    # A[smaller:equal] = elements == pivot
    # A[equal:larger] = unclassified
    # A[larger:] = elements > pivot

    while equal < larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller += 1
            equal += 1
        elif A[equal] == pivot:
            equal += 1
        else:  # A[equal] > pivot
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]
