"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert_new(self, head: 'Node', curr: 'Node', val: int):
        curr.next = Node(val, curr.next)
        return head
        
    def insert_smallest_or_biggest(self, head: 'Node', val: int) -> 'Node':
        curr = head.next
        while curr.val <= curr.next.val:
            curr = curr.next
            if curr == head:
                return self.insert_new(head, curr, val)
        
        return self.insert_new(head, curr, val)
    

    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        
        if not head:
            node = Node(insertVal)
            node.next = node
            return node

        curr = head.next
        while curr.val > insertVal:
            if curr == head:
                return self.insert_smallest_or_biggest(head, insertVal)
            curr = curr.next
        
        while curr.next.val < insertVal:
            if curr == head:
                return self.insert_smallest_or_biggest(head, insertVal)
            curr = curr.next

        return self.insert_new(head, curr, insertVal)
        