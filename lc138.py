# https://leetcode.cn/problems/copy-list-with-random-pointer/submissions/575426649/?envType=study-plan-v2&envId=top-interview-150
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        if not head:
            return None
        node_ls=[]
        obj2idx={}
        idx=0

        while(head):
            node_ls.append(head)
            obj2idx[id(head)]=idx
            head=head.next
            idx+=1

        new_ls=[Node(node.val) for node in node_ls]

        for i in range(idx):
            if i+1<idx:
                new_ls[i].next=new_ls[i+1]
            if node_ls[i].random:
                new_ls[i].random=new_ls[obj2idx[id(node_ls[i].random)]]
        
        return new_ls[0]
        
