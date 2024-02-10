from typing import List


class Solution:
    def __init__(self):
        self.wordDict = set()
        self.memo = []

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.wordDict = set(wordDict)
        self.memo = [-1 for _ in range(len(s))]
        return self.dp(s, 0)

    def dp(self, s, i):
        if i == len(s):
            return True
        if self.memo[i] != -1:
            return False if self.memo[i] == 0 else True

        # 遍历s
        for length in range(1, len(s) - i + 1):
            prefix = s[i: length + i]
            if prefix in self.wordDict:
                sub_problem = self.dp(s, i + length)
                if sub_problem:
                    self.memo[i] = 1
                    return True
        self.memo[i] = 0
        return False
