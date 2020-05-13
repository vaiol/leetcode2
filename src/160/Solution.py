# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNodeSet(self, headA: ListNode, headB: ListNode) -> ListNode:
        s = set()
        currA = headA
        currB = headB
        while currA or currB:
            if currA:
                if currA in s:
                    return currA
                s.add(currA)
                currA = currA.next
            if currB:
                if currB in s:
                    return currB
                s.add(currB)
                currB = currB.next
        return None

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        currA = headA
        currB = headB
        while currA != currB:
            currA = currA.next if currA else headB
            currB = currB.next if currB else headA
        return currA

headA = ListNode(1)
headA.next = ListNode(2)

headB = ListNode(3)
headB.next = headA

S = Solution()
print(S.getIntersectionNodeSet(headA, headB))
