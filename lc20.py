# https://leetcode.cn/problems/valid-parentheses/submissions/575182242/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        for c in s:
            if c=="(" or c=="{" or c=="[":
                stack.append(c)
            else:
                if len(stack)>0:
                    cc=stack[-1]
                else:
                    return False
                if cc=="(" and c==")" or cc=="{" and c=="}" or cc=="[" and c=="]":
                    stack.pop()
                else:
                    return False
    
        return len(stack)==0