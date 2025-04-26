# Problem: Min Stack - https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.stack = []
        self.mstack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mstack  or self.mstack[-1] >= val:
            self.mstack.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if self.mstack[-1] == popped:
            self.mstack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.mstack[-1]


        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()