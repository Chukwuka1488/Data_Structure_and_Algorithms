"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

To reverse a linked list, you can use the following approach:

1. Initialize a pointer ptr to the head of the linked list.
2. Initialize a previous pointer prev to None.
3. Iterate through the linked list, starting from the head, and do the following:
4. Save the next node in a temporary variable temp.
5. Set the next pointer of the current node to the previous node.
6. Set the previous node to the current node.
7 .Set the current node to the saved next node.
8 .Return the previous node as the head of the reversed linked list.

"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        prev = None
        while ptr is not None:
            temp = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = temp
        return prev


# Create the linked list
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

sol = Solution()
# Test the reverse_linked_list function
result = sol.reverseList(head)

# Print the linked list
ptr = result
while ptr is not None:
    print(ptr.val)
    ptr = ptr.next
