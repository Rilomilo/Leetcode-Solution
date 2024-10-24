# https://leetcode.cn/problems/add-two-numbers/description/?envType=study-plan-v2&envId=top-interview-150

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
      
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1=0
        num2=0
        cnt=0

        while l1:
            num1=num1+l1.val*10**cnt
            l1=l1.next
            cnt+=1
        cnt=0
        while l2:
            num2=num2+l2.val*10**cnt
            l2=l2.next
            cnt+=1

        sum=num1+num2

        head=ListNode()
        p=head
        if sum==0:
            return head
        while sum:
            digit=sum%10
            sum=sum//10
            p.next=ListNode(digit)
            p=p.next
        return head.next