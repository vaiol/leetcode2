# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n == 0:
            return head
        slow, fast = None, head
        while fast:
            fast = fast.next
            if n > 0:
                n -= 1
            else:
                slow = head if not slow else slow.next
        if slow:
            nxt = slow.next.next
            slow.next.next = None
            slow.next = nxt
        else:
            head = head.next
        return head
