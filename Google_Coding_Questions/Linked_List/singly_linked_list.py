class SinglyListNode:

    def __init__(self):
        # set head to none
        self.head = None
        # set the next value after head to none
        self.nodes = []
        # set size of linked list to zero
        self.size = len(self.nodes)

        self.tail = None

    def get(self, index):
        # check if the index of the value to be gotten exists
        if index < 0 or index >= len(self.nodes):
            return -1
        return self.nodes[index]

    def addAtHead(self, val):
        # to add at the head, get a new node, # set the next value to the head
        self.nodes = [val] + self.nodes
        # check if tail value exists, if it doesn't then set tail to new node
        if self.tail is None:
            self.tail = self.nodes[0]
        self.head = self.nodes[0]

    def addAtTail(self, val):
        self.nodes.append(val)
        self.tail = val

    def addAtIndex(self, index, val):
        # to add value at an index, check if the index is reasonable
        if index > len(self.nodes):
            return
        elif index == len(self.nodes):
            self.nodes.append(val)
            self.tail = val
        else:
            self.nodes = self.nodes[:index] + [val] + self.nodes[index:]
            if index == 0:
                self.head == self.nodes[0]

    def deleteAtIndex(self, index):

        if index < 0 or index >= len(self.nodes):
            return
        if len(self.nodes) == 1:
            self.nodes = []
            self.head = None
            self.tail = None
            return
        if index == 0:
            self.head = self.nodes[index + 1]
            self.nodes = self.nodes[index + 1:]
            return
        if index == len(self.nodes) - 1:
            self.tail = self.nodes[index - 1]
            self.nodes = self.nodes[:index]
            return
        self.nodes = self.nodes[:index] + self.nodes[index + 1:]


import unittest


# class TestMyLinkedList(unittest.TestCase):
#     def setUp(self):
#         self.linked_list = SinglyListNode()
#
#     def test_add_at_head(self):
#         self.linked_list.addAtHead(1)
#         self.assertEqual(self.linked_list.get(0), 1)
#         self.linked_list.addAtHead(2)
#         self.assertEqual(self.linked_list.get(0), 2)
#
#     def test_add_at_tail(self):
#         self.linked_list.addAtTail(1)
#         self.assertEqual(self.linked_list.get(0), 1)
#         self.linked_list.addAtTail(2)
#         self.assertEqual(self.linked_list.get(1), 2)
#
#     def test_add_at_index(self):
#         self.linked_list.addAtIndex(0, 1)
#         self.assertEqual(self.linked_list.get(0), 1)
#         self.linked_list.addAtIndex(1, 2)
#         self.assertEqual(self.linked_list.get(1), 2)
#         self.linked_list.addAtIndex(2, 3)
#         self.assertEqual(self.linked_list.get(2), 3)
#
#     def test_delete_at_index(self):
#         self.linked_list.addAtIndex(0, 1)
#         self.linked_list.addAtIndex(1, 2)
#         self.linked_list.addAtIndex(2, 3)
#         self.linked_list.deleteAtIndex(1)
#         self.assertEqual(self.linked_list.get(1), 3)
#         self.linked_list.deleteAtIndex(1)
#         self.assertEqual(self.linked_list.get(1), -1)
#
#     def test_get(self):
#         self.assertEqual(self.linked_list.get(0), -1)
#         self.linked_list.addAtIndex(0, 1)
#         self.assertEqual(self.linked_list.get(0), 1)
#         self.assertEqual(self.linked_list.get(1), -1)


if __name__ == '__main__':
    # unittest.main(verbosity=2)
    linked_list = SinglyListNode()

    # Add an element to the head of the list
    linked_list.addAtHead(1)

    # Add an element to the tail of the list
    linked_list.addAtTail(3)

    # Add an element at index 1
    linked_list.addAtIndex(1, 2)

    # Get the value at index 1
    print(linked_list.get(1))  # Output: 2

    # Delete the element at index 1
    linked_list.deleteAtIndex(1)

    # Get the value at index 1
    print(linked_list.get(1))
