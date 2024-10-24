# https://leetcode.cn/problems/merge-two-sorted-lists/submissions/575403341/?envType=study-plan-v2&envId=top-interview-150
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1=list1
        p2=list2

        if not p1:
            return p2
        if not p2:
            return p1

        head=ListNode()
        p=head

        while p1 and p2:
            if p1.val<=p2.val:
                t=p1
                p1=p1.next
            else:
                t=p2
                p2=p2.next
            p.next=t
            p=p.next
        if p1:
            p.next=p1
        if p2:
            p.next=p2

        return head.next
