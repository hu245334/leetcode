from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.pre = [0] * (len(nums) + 1)
        for i, num in enumerate(self.nums):
            self.pre[i + 1] = self.pre[i] + num

    def sumRange(self, left: int, right: int) -> int:
        return self.pre[right + 1] - self.pre[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
