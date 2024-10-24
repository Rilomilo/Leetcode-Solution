# https://leetcode.cn/problems/basic-calculator/submissions/575356029/?envType=study-plan-v2&envId=top-interview-150

def compute(nums, ops):
    if len(ops)>0 and ops[-1]!='(':
        op=ops.pop()
        b=nums.pop()
        a=nums.pop()
        if op=="+":
            res=a+b
        elif op=="-":
            res=a-b
        elif op=="*":
            res=a*b
        elif op=="/":
            res=a//b
        nums.append(res)

class Solution:
    def calculate(self, s: str) -> int:
        ops=[]
        nums=[]
        idx=0
        op_flag=True

        while idx < len(s):
            if s[idx]==" ":
                pass
            elif s[idx] =='(':
                ops.append(s[idx])
            elif s[idx] ==")":
                ops.pop()
                compute(nums, ops)
                op_flag=False
            elif s[idx] in ['+','-','*','/']:
                if s[idx]=='-' and op_flag==True:
                    nums.append(0)
                ops.append(s[idx])
                op_flag=True
            else:
                idx1=idx+1
                while idx1<len(s) and s[idx1].isdigit():
                    idx1+=1
                num=int(s[idx:idx1])
                nums.append(num)
                idx=idx1-1
                op_flag=False

                compute(nums, ops)
            idx+=1

        return nums[0]
        
