from typing import List

"""
方法1：二分
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            index = self.bin_search(numbers, i, target - num)
            if index != len(numbers) and numbers[index] == target - num:
                return [i + 1, index + 1]

    def bin_search(self, nums: List[int], left: int, x: int):
        right = len(nums)
        while left + 1 != right:
            mid = (left + right) // 2
            if nums[mid] < x:
                left = mid
            else:
                right = mid
        return right
"""


# 使用双指针

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []
