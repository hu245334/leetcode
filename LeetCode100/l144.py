from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.track = []

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.preorder(root)
        return self.track

    def preorder(self, root: Optional[TreeNode]):
        if root is None:
            return
        self.track.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
