from typing import List

class Solution:

    def __init__(self):
        self.memo = []

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        result = float('inf')
        self.memo = [[11111 for _ in range(n)] for _ in range(n)]
        for j in range(n):
            result = min(result, self.dp(matrix, n - 1, j))
        return result

    def dp(self, matrix: List[List[int]], i:int, j:int):
        if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
            return 99999
        if i == 0:
            return matrix[0][j]
        if self.memo[i][j] != 11111:
            return self.memo[i][j]
        self.memo[i][j] = matrix[i][j] + min(
            self.dp(matrix, i - 1, j),
            self.dp(matrix, i - 1, j - 1) if j > 0 else 99999,
            self.dp(matrix, i - 1, j + 1) if j < len(matrix[0]) - 1 else 99999
        )
        return self.memo[i][j]