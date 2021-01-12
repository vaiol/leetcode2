# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseListHelper(self, curr: ListNode, pred: ListNode) -> ListNode:
        if not curr:
            return pred
        succ = curr.next
        curr.next = pred
        return self.reverseListHelper(succ, curr)

    def reverseListRecursion(self, head: ListNode) -> ListNode:
        if not head:
            return None
        node = self.reverseListHelper(head.next, head)
        head.next = None
        return node

    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        pred = head
        curr = head.next
        head.next = None
        while curr:
            head = curr
            succ = curr.next
            curr.next = pred
            pred = curr
            curr = succ
        return head
