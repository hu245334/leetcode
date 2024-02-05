import bisect
from typing import List


class Solution:
    def countTarget(self, scores: List[int], target: int) -> int:
        return (self.serch_right(scores, target) -
                self.serch_left(scores, target))

    def serch_left(self, scores: List[int], target: int) -> int:
        left = bisect.bisect_left(scores, target)
        if left == len(scores) or scores[left] != target:
            return -1
        return left

    def serch_right(self, scores: List[int], target: int) -> int:
        right = bisect.bisect_right(scores, target)
        if right == 0 or scores[right - 1] != target:
            return -1
        return right
