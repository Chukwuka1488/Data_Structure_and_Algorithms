"""
To remove the nth node from the end of the linked list, you can use the following approach:

1. Initialize a pointer ptr to the head of the linked list.
2. Initialize a counter count to 0.
3. Move ptr one node at a time until it reaches the end of the linked list.
4. While ptr is not None, increment count and move ptr to the next node.
5. Set ptr to the head of the linked list.
6. Move ptr count - n - 1 times to reach the node before the nth node from the end.
7. Set the next pointer of ptr to the node after the nth node from the end.

"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Initialize a pointer ptr to the head of the linked list.
        ptr = head

        # Initialize a counter count to 0.
        counter = 0

        # Move ptr one node at a time until it reaches the end of the linked list.
        while ptr is not None:
            counter += 1
            ptr = ptr.next

        # Set the pointer to the head of the linked list
        ptr = head

        # If the nth node from the end is the first node, return the second node as the head
        if n == counter:
            return head.next

        # Move the pointer to the node before the nth node from the end
        for _ in range(counter - n - 1):
            ptr = ptr.next

        # Set the next pointer of the node before the nth node from the end to the node after it
        ptr.next = ptr.next.next

        # Initialize an array to store the values of the linked list
        # arr = []
        #
        # # Add the values of the linked list to the array
        # ptr = head
        # while ptr is not None:
        #     arr.append(ptr.val)
        #     ptr = ptr.next

        # return arr
        return head


sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

res = sol.removeNthFromEnd(head, 2)
print(res)