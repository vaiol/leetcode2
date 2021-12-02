# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList0(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        odd_head = odd_cur = head
        even_head = even_cur = head.next
        while even_cur and even_cur.next:
            odd_next = odd_cur.next.next if odd_cur.next else None
            even_next = even_cur.next.next if even_cur.next else None
            odd_cur.next = odd_next
            even_cur.next = even_next
            odd_cur = odd_next
            even_cur = even_next
        odd_cur.next = even_head
        return odd_head

    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        odd = head
        even_head = even = head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head

    def oddEvenList_1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 02.12.2021
        if not head or not head.next or not head.next.next:
            return head

        second_head = head.next
        current_odd_node = head
        current_even_node = head.next

        while current_even_node and current_even_node.next:
            next_odd_node = current_even_node.next
            next_even_node = next_odd_node.next

            current_odd_node.next = next_odd_node
            current_even_node.next = next_even_node

            current_odd_node = next_odd_node
            current_even_node = next_even_node


        current_odd_node.next = second_head
        return head
