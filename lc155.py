# https://leetcode.cn/problems/min-stack/?envType=study-plan-v2&envId=top-interview-150

class MinStack:
    def __init__(self):
        self.minimum=[]
        self.stack=[]

    def __len__(self):
        return len(self.stack)

    def push(self, val: int) -> None:
        if len(self)!=0:
            self.minimum.append(min(val, self.minimum[-1]))
        else:
            self.minimum.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if len(self)!=0:
            self.stack.pop()
            self.minimum.pop()
        
    def top(self) -> int:
        if len(self)!=0:
            r=self.stack[-1]
        else:
            r=None
        return r

    def getMin(self) -> int:
        if len(self)!=0:
            r=self.minimum[-1]
        else:
            r=None
        return r


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()