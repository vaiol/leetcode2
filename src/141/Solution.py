# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycleHash(self, head: ListNode) -> bool:
        d = dict()
        curr = head
        while curr:
            if curr in d:
                return True
            d[curr] = True
            curr = curr.next
        return False

    def hasCycle(self, head: ListNode) -> bool:
        first, second = head, head
        while first and first.next:
            first = first.next.next
            second = second.next
            if first == second:
                return True
        return False

