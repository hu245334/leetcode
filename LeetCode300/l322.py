from typing import List
from functools import lru_cache


class Solution:
    def __init__(self):
        self.result = []

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 0:
            return -1
        self.result = [-1111] * (amount + 1)
        coins.sort(reverse=True)
        return self.dp(tuple(coins), amount)

    @lru_cache(maxsize=1024)
    def dp(self, coins: tuple, amount: int):
        if amount == 0:
            return 0
        if self.result[amount] != -1111:
            return self.result[amount]
        res = float("inf")
        for coin in coins:
            if coin > amount:
                continue
            sub_problem = self.dp(coins, amount - coin)
            if sub_problem == -1:
                continue
            res = min(res, sub_problem + 1)
        self.result[amount] = -1 if res == float("inf") else res
        return self.result[amount]
