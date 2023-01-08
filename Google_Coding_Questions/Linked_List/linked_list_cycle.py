"""
To solve this problem, you can use the Floyd's cycle detection algorithm also known as the tortoise and hare algorithm.

This algorithm works by using two pointers, one of which moves faster than the other. The idea is to have the fast
pointer catch up to the slow pointer. If the fast pointer catches up to the slow pointer and they are the same, then
there is a cycle.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def has_cycle(head):
    # Initialize the fast and slow pointers
    fast = head
    slow = head

    # Move the fast pointer two steps and the slow pointer one step at a time
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        # If the fast and slow pointers are pointing to the same node, return True
        if fast == slow:
            return True

    # If the fast pointer reaches the end of the linked list, return False
    return False


# Create a linked list with a cycle
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next

# Test the has_cycle function
result = has_cycle(head)
print(result)  # True
