# https://leetcode.cn/problems/evaluate-reverse-polish-notation/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:
            if token in ['+','-','*','/']:
                b=stack.pop()
                a=stack.pop()
                stack.append(int(eval(f"{a}{token}{b}")))
            else:
                stack.append(token)
        return int(stack[0])