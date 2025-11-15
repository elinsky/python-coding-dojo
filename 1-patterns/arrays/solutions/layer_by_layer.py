def matrix_in_spiral_order(square_matrix: list[list[int]]) -> list[int]:
    """
    Pattern: Layer-by-Layer Processing

    Goal: Process 2D array boundary-by-boundary from outside to center

    When to use: Spiral traversal, matrix rotation, boundary operations
    Problems that use it: Spiral order, rotate matrix, frame extraction
    Key insight: Process outer boundary, recurse on inner (n-2)×(n-2) matrix
    """
    spiral_ordering = []

    for offset in range((len(square_matrix) + 1) // 2):
        if offset == len(square_matrix) - offset - 1:
            # Odd dimension, center element
            spiral_ordering.append(square_matrix[offset][offset])
            continue

        # Process boundary at this offset
        # Top edge (left to right)
        spiral_ordering.extend(square_matrix[offset][offset:-1-offset])
        # Right edge (top to bottom)
        spiral_ordering.extend(list(zip(*square_matrix))[-1-offset][offset:-1-offset])
        # Bottom edge (right to left)
        spiral_ordering.extend(square_matrix[-1-offset][-1-offset:offset:-1])
        # Left edge (bottom to top)
        spiral_ordering.extend(list(zip(*square_matrix))[offset][-1-offset:offset:-1])

    return spiral_ordering
