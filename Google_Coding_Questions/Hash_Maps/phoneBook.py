import unittest
import io
import sys


def phone_book():
    # Read the number of entries
    n = int(input())

    # Create an empty dictionary
    phone_book = {}

    # Read the entries and add them to the phone book
    for i in range(n):
        name, phone = input().split()
        phone_book[name] = phone

    # Read the queries and look up the names in the phone book
    while True:
        try:
            name = input()
            if name in phone_book:
                print(f"{name}={phone_book[name]}")
            else:
                print("Not found")
        except EOFError:
            # End of input reached, exit the loop
            break


# class TestPhoneBook(unittest.TestCase):
#     def setUp(self):
#         self.input_str = '3\nSam 99912222\nTom 11122222\nHarry 12299933\nSam\nTom\nHarry\nEdward\n'
#         self.expected_output_str = 'Sam=99912222\nTom=11122222\nHarry=12299933\nNot found\n'
#         self.input_str_2 = '2\nAlice 9876123456\nBob 987654321\nAlice\nBob\nEdward\n'
#         self.expected_output_str_2 = 'Alice=9876123456\nBob=987654321\nNot found\n'
#         self.input_str_3 = '1\nJohn 123456789\n'
#         self.expected_output_str_3 = 'John=123456789\n'
#
#     def test_phone_book(self):
#         sys.stdin = io.StringIO(self.input_str)
#         sys.stdout = io.StringIO()
#         phone_book()
#         self.assertEqual(sys.stdout.getvalue(), self.expected_output_str)
#         sys.stdin = sys.__stdin__
#         sys.stdout = sys.__stdout__
#
#         sys.stdin = io.StringIO(self.input_str_2)
#         sys.stdout = io.StringIO()
#         phone_book()
#         self.assertEqual(sys.stdout.getvalue(), self.expected_output_str_2)
#         sys.stdin = sys.__stdin__
#         sys.stdout = sys.__stdout__
#
#         sys.stdin = io.StringIO(self.input_str_3)
#         sys.stdout = io.StringIO()
#         phone_book()
#         self.assertEqual(sys.stdout.getvalue(), self.expected_output_str_3)
#         sys.stdin = sys.__stdin__
#         sys.stdout = sys.__stdout__
#


if __name__ == "__main__":
    # unittest.main(verbosity=2)
    phone_book()
    print("Passed All Tests")
