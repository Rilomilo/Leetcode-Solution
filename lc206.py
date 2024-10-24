# https://leetcode.cn/problems/reverse-linked-list/

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack=[]
        while head:
            stack.append(head)
            head=head.next
        head=ListNode()
        p=head

        while len(stack)>0:
            node=stack.pop()
            p.next=node
            p=p.next
        p.next=None # MLE
        return head.next
    
if __name__=="__main__":
    head=ListNode()
    p1=ListNode()
    head.next=p1
    solution=Solution()
    solution.reverseList(head)