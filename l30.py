import bisect
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.serch_left(nums, target), self.serch_right(nums, target)]

    def serch_left(self, nums: List[int], target: int) -> int:
        left = bisect.bisect_left(nums, target)
        if left == len(nums) or nums[left] != target:
            return -1
        return left

    def serch_right(self, nums: List[int], target: int) -> int:
        right = bisect.bisect_right(nums, target)
        if right == 0 or nums[right - 1] != target:
            return -1
        return right - 1
