from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        dp = nums[0]
        result = dp
        for i in range(1, n):
            dp = max(dp + nums[i], nums[i])
            result = max(result, dp)
        return result
