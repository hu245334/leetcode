from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 递归终止条件
        if head is None or head.next is None:
            return head
        last = self.reverseList(head.next)
        # reverse之后的最后一个的next指向head
        head.next.next = head
        head.next = None
        return last
