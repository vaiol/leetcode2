class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.maxStack = []
        

    def push(self, x: int) -> None:
        if len(self.maxStack):
            m = max(self.peekMax(), x)
            self.maxStack.append(m)
        else:
            self.maxStack.append(x)
        self.stack.append(x)
        
        

    def pop(self) -> int:
        self.maxStack.pop()
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1] if len(self.stack) else None
        

    def peekMax(self) -> int:
        return self.maxStack[-1] if len(self.maxStack) else None
        

    def popMax(self) -> int:
        res = self.peekMax()
        buffer = []
        while self.top() != self.peekMax():
            buffer.append(self.pop())
        self.pop()
        while buffer:
            self.push(buffer.pop())
        return res
            
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()