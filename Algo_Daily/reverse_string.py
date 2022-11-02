import unittest

import running_time


def reverse_string(str1):
    # str_arr = list(filter(lambda i: (i in str1), str1))
    str_arr = list(str1)
    start = 0
    end = len(str1) - 1

    while start <= end:
        temp = str_arr[start]
        str_arr[start] = str_arr[end]
        str_arr[end] = temp
        start += 1
        end -= 1
    return "".join(str_arr)
    # return str_arr
    # return str1[::-1]


# class Test(unittest.TestCase):
#     def test_1(self):
#         assert reverse_string("njnschnjkdasn j32 uida") == "adiu 23j nsadkjnhcsnjn"
#         print(
#             "PASSED: reverse_string('njnschnjkdasn j32 uida') should return 'adiu 23j nsadkjnhcsnjn'"
#         )
#
#     def test_2(self):
#         assert reverse_string("timbuktu12") == "21utkubmit"
#         print("PASSED: reverse_string('timbuktu12') should return '21utkubmit'")
#
#     def test_3(self):
#         assert reverse_string("") == ""
#         print("PASSED: reverse_string('') should return ''")
#
#     def test_4(self):
#         assert reverse_string("reverseastring") == "gnirtsaesrever"
#         print("PASSED: reverse_string('reverseastring') should return 'gnirtsaesrever'")


if __name__ == "__main__":
    # unittest.main(verbosity=2)
    print("Nice job, 4/4 tests passed!")
    print(reverse_string(
        'PneumonoultramicroscopicsilicovolcanoconiosisPneumonoultramicroscopicsilicovolcanoconiosis'
        'PneumonoultramicroscopicsilicovolcanoconiosisPneumonoultramicroscopicsilicovolcanoconiosis'
        'PneumonoultramicroscopicsilicovolcanoconiosisPneumonoultramicroscopicsilicovolcanoconiosis'
        'PneumonoultramicroscopicsilicovolcanoconiosisPneumonoultramicroscopicsilicovolcanoconiosis'
        'PneumonoultramicroscopicsilicovolcanoconiosisPneumonoultramicroscopicsilicovolcanoconiosis'
        'PneumonoultramicroscopicsilicovolcanoconiosisPneumonoultramicroscopicsilicovolcanoconiosis'
        'PneumonoultramicroscopicsilicovolcanoconiosisPneumonoultramicroscopicsilicovolcanoconiosis'
        'PneumonoultramicroscopicsilicovolcanoconiosisPneumonoultramicroscopicsilicovolcanoconiosis'
        'PneumonoultramicroscopicsilicovolcanoconiosisPneumonoultramicroscopicsilicovolcanoconiosis'
        'PneumonoultramicroscopicsilicovolcanoconiosisPneumonoultramicroscopicsilicovolcanoconiosis'
        'PneumonoultramicroscopicsilicovolcanoconiosisPneumonoultramicroscopicsilicovolcanoconiosis'
        'PneumonoultramicroscopicsilicovolcanoconiosisPneumonoultramicroscopicsilicovolcanoconiosis'
        'PneumonoultramicroscopicsilicovolcanoconiosisPneumonoultramicroscopicsilicovolcanoconiosis'
        'PneumonoultramicroscopicsilicovolcanoconiosisPneumonoultramicroscopicsilicovolcanoconiosis'
        'PneumonoultramicroscopicsilicovolcanoconiosisPneumonoultramicroscopicsilicovolcanoconiosis'
        'Pneumonoultramicroscopicsilicovolcanoconiosis'))
    running_time.time_to_run()
