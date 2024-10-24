# https://leetcode.cn/problems/linked-list-cycle/?envType=study-plan-v2&envId=top-interview-150

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        while head.next:
            if head.val is None:
                return True
            head.val=None
            head=head.next
        return False