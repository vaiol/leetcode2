# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        if not list1 and not list2:
            return head
        if not list2:
            return list1
        if not list1:
            return list2
        
        sentinel = ListNode()

        c1 = list1
        c2 = list2
        ch = sentinel
        while ch:
            if not c2 and not c1:
                break
            if not c2 or (c1 and c1.val < c2.val):
                tmp = c1
                c1 = c1.next
            else:
                tmp = c2
                c2 = c2.next
            tmp.next = None
            ch.next = tmp
            ch = ch.next
        
        head = sentinel.next
        sentinel.next = None
        return head
        
        
        
        
        