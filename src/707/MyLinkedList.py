class Node:
    def __init__(self, val):
        self.val = val
        self.next: Node or None = None
        self.prev: Node or None = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head: Node = Node(0)
        self.tail: Node = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

    def getNode(self, index: int) -> Node:
        if index <= self.length - index:
            curr = self.head.next
            for _ in range(index):
                curr = curr.next
        else:
            rev_index = self.length - index - 1
            curr = self.tail.prev
            for _ in range(rev_index):
                curr = curr.prev
        return curr

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.length or index < 0:
            return -1
        node = self.getNode(index)
        return node.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val)
        self.length += 1

        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = Node(val)
        self.length += 1

        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.length:
            return
        if index < 0:
            index = 0

        if index == self.length:
            return self.addAtTail(val)
        elif index == 0:
            return self.addAtHead(val)

        curr = self.getNode(index)

        node = Node(val)
        self.length += 1

        node.next = curr
        node.prev = curr.prev
        curr.prev.next = node
        curr.prev = node

        return curr.val

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.length or index < 0:
            return

        curr = self.getNode(index)
        self.length -= 1
        pred = curr.prev
        succ = curr.next
        curr.next = None
        curr.prev = None
        pred.next = succ
        succ.prev = pred

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)