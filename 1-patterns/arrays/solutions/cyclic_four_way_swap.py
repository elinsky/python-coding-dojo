def rotate_matrix(square_matrix: list[list[int]]) -> None:
    """
    Pattern: Cyclic Four-Way Swap

    Goal: Rotate 4 elements simultaneously in circular pattern

    When to use: Matrix rotation in-place, cyclic permutations
    Problems that use it: Rotate matrix 90°, cyclic array rotation
    Key insight: One temp variable rotates 4 positions; avoids extra space
    """
    matrix_size = len(square_matrix) - 1
    for i in range(len(square_matrix) // 2):
        for j in range(i, matrix_size - i):
            # 4-way rotation: top→right→bottom→left→top
            (square_matrix[i][j],
             square_matrix[~j][i],
             square_matrix[~i][~j],
             square_matrix[j][~i]) = (
                square_matrix[~j][i],
                square_matrix[~i][~j],
                square_matrix[j][~i],
                square_matrix[i][j])
