# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        prev, slow, fast = head, head, head
        
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        next_head = prev.next.next
        prev.next.next = None
        prev.next = next_head
        return head
    
        