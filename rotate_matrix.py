from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        PROBLEM: Rotate an n x n 2D matrix by 90 degrees (clockwise) in-place.
        METHOD: O(n^2) Time, O(1) Space. Linear Algebra Trick:
        1. Transpose: Swap `matrix[i][j]` with `matrix[j][i]` (diagonal flip).
        2. Reverse: Reverse each row to achieve 90-degree rotation.
        """
        n = len(matrix)

        # Step 1: Transpose (Rows become Columns)
        for i in range(n):
            for j in range(i, n):  # Start from i to avoid double-swapping
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row (Left becomes Right)
        for i in range(n):
            matrix[i].reverse()

# --- Main Execution ---
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: 3x3 Matrix
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    sol.rotate(matrix1)
    print(f"Test 1: {matrix1}") 
    # Expected: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    # Test Case 2: 4x4 Matrix
    matrix2 = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    sol.rotate(matrix2)
    print(f"Test 2: {matrix2}") 
    # Expected: [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]