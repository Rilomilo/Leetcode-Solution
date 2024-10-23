# https://leetcode.cn/problems/simplify-path/submissions/575188868/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        ls=path.split("/")

        for item in ls:
            if item!="" and item!=".":
                if item=="..":
                    if len(stack)!=0:
                        stack.pop()
                else:
                    stack.append(item)

        return '/'+'/'.join(stack)