import bisect
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = bisect.bisect_left(nums, target)
        if result == len(nums) or nums[result] != target:
            return -1
        return result
