class Solution:
    def __init__(self):
        self.memo = []

    def minDistance(self, word1: str, word2: str) -> int:
        self.memo = [[None for _ in range(len(word2))] for _ in range(len(word1))]
        return self.dp(word1, len(word1) - 1, word2, len(word2) - 1)

    def dp(self, word1: str, i: int, word2: str, j: int) -> int:
        if i < 0 or j < 0:
            return max(i, j) + 1

        if self.memo[i][j] is not None:
            return self.memo[i][j]

        if word1[i] == word2[j]:
            self.memo[i][j] = self.dp(word1, i - 1, word2, j - 1)
        else:
            self.memo[i][j] = min(
                self.dp(word1, i, word2, j - 1) + 1,  # 插入
                self.dp(word1, i - 1, word2, j) + 1,  # 删除
                self.dp(word1, i - 1, word2, j - 1) + 1  # 替换
            )
        return self.memo[i][j]