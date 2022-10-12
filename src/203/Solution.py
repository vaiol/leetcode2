# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        sentinel = ListNode(0, head)
        
        ch = sentinel
        while ch and ch.next:
            if ch.next.val == val:
                next_node = ch.next.next
                ch.next.next = None
                ch.next = next_node
            else:
                ch = ch.next
        
        new_head = sentinel.next
        sentinel.next = None
        
        return new_head
            