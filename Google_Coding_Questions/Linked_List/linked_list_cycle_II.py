# Definition for singly-linked list.
"""
To find the node where the cycle begins, you can use the Floyd's cycle detection algorithm to find the first node that is part of the cycle.

Once you find the first node that is part of the cycle, you can use the following steps to find the node where the cycle begins:

1. Initialize two pointers, ptr1 and ptr2, to the head of the linked list.
2. Move ptr1 to the next node and ptr2 to the node after that.
3. Calculate the length of the cycle by moving ptr2 around the cycle until it becomes equal to ptr1. Let the length of the cycle be L.
4. Set ptr2 to the head of the linked list.
5. Move ptr1 and ptr2 at a pace of one node per iteration. When ptr2 reaches the node where the cycle begins, ptr1 will be L nodes behind.
6. Move ptr1 to the head of the linked list.
7. Move both pointers at a pace of one node per iteration until they meet at the node where the cycle begins.
"""
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Find the first node that is part of the cycle
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        # If there is no cycle, return None
        if fast is None or fast.next is None:
            return None

        # Calculate the length of the cycle
        cycle_length = 1
        fast = fast.next
        while fast != slow:
            fast = fast.next
            cycle_length += 1

        # Find the node where the cycle begins
        ptr1 = head
        ptr2 = head
        for _ in range(cycle_length):
            ptr2 = ptr2.next
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1
