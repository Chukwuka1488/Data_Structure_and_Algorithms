"""
Given a linked list of size N, your task is to complete the function isLengthEvenOrOdd() which contains head of the
linked list and check whether the length of linked list is even or odd.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def isLengthEvenOrOdd(head):
    ptr = head
    counter = 0

    while ptr is not None:
        ptr = ptr.next
        counter += 1

    if counter % 2 == 0:
        return 'Even'
    return 'Odd'


# Create a linked list
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

# Test the is_length_even_or_odd function
result = isLengthEvenOrOdd(head)
print(result)  # odd

# Create a linked list
head = ListNode(1)
head.next = ListNode(2)

# Test the is_length_even_or_odd function
result = isLengthEvenOrOdd(head)
print(result)  # even
