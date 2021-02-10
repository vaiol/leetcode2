"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        curr = head
        while curr:
            curr_next = curr.next
            new_curr = Node(curr.val, curr.next, curr.random)
            curr.next = new_curr
            curr = curr_next
        curr = head.next
        while curr:
            curr.random = curr.random.next if curr.random else None
            curr = curr.next.next if curr.next else None
        new_head = head.next
        curr = head
        while curr:
            new_item = curr.next
            curr.next = curr.next.next
            new_item.next = new_item.next.next if new_item.next else None
            curr = curr.next
        curr = head
        while curr:
            r_val = curr.random.val if curr.random else None
            curr = curr.next
        curr = new_head
        while curr:
            r_val = curr.random.val if curr.random else None
            curr = curr.next
        return new_head
        