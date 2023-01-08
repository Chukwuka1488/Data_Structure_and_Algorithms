"""
To solve this problem, you can use the following approach:

Traverse the linked list headA and calculate its length lenA.
Traverse the linked list headB and calculate its length lenB.
Set two pointers, ptr1 and ptr2, to the head of headA and headB, respectively.
If lenA is greater than lenB, move ptr1 ahead by lenA - lenB nodes.
If lenB is greater than lenA, move ptr2 ahead by lenB - lenA nodes.
Move ptr1 and ptr2 one node at a time until they meet or reach the end of their respective linked lists.

"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Calculate the lengths of the linked lists
        lenA = 0
        lenB = 0
        # set pointer to first value in the array A
        ptr = headA
        # create linked list for all elements in the array A
        while ptr is not None:
            # get the length of the linked list A
            lenA += 1
            ptr = ptr.next
        # set pointer to first value in the array B
        ptr = headB
        # create linked list for all elements in the array B
        while ptr is not None:
            # get the length of the linked list A
            lenB += 1
            ptr = ptr.next

        # Set the pointers to the head of the linked lists
        ptr1 = headA
        ptr2 = headB

        # Move the pointers ahead by the difference in lengths
        if lenA > lenB:
            for _ in range(lenA - lenB):
                ptr1 = ptr1.next
        elif lenB > lenA:
            for _ in range(lenB - lenA):
                ptr2 = ptr2.next

        # Move the pointers one node at a time until they meet or reach the end of their respective linked lists
        while ptr1 is not None and ptr2 is not None:
            if ptr1 == ptr2:
                return ptr1
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return None


# create an instance of the class
sol = Solution()
# Create the first linked list
headA = ListNode(1)
headA.next = ListNode(9)
headA.next.next = ListNode(1)
headA.next.next.next = ListNode(2)
headA.next.next.next.next = ListNode(4)

# Create the second linked list
headB = ListNode(3)
headB.next = headA.next.next.next

# Test the find_intersection function
result = sol.getIntersectionNode(headA, headB)
print(result.val)  # 2
