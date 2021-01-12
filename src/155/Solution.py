class Node:
    def __init__(self, val: int, minVal: int):
        self.val = val
        self.min = minVal
        self.next = None


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = None

    def push(self, x: int) -> None:
        if self.head == None:
            node = Node(x, x)
            self.head = node
        else:
            node = Node(x, min(self.head.min, x))
            node.next = self.head
            self.head = node

    def pop(self) -> None:
        if self.head == None:
            return
        self.head = self.head.next

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()