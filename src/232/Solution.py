class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        

    def push(self, x: int) -> None:
        self.s1.append(x)
        

    def pop(self) -> int:
        if not self.s2:
            self.repop()
        if not self.s2:
            return None
        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2:
            self.repop()
        if not self.s2:
            return None
        item = self.s2.pop()
        self.s2.append(item)
        return item
            
    
    def repop(self) -> None:
        while self.s1:
            self.s2.append(self.s1.pop())
        
        

    def empty(self) -> bool:
        return not self.s1 and not self.s2
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()