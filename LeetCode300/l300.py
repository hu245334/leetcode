import bisect
from collections import deque
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = deque()
        for num in nums:
            if len(dp) == 0 or dp[-1] < num:
                dp.append(num)
            else:
                index = self.bin_search(dp, num)
                dp[index] = num
        return len(dp)

    def bin_search(self, dp, target):
        return bisect.bisect_left(dp, target)


sol = Solution().lengthOfLIS([4, 8, 9, 5, 6, 7, 2, 7])
