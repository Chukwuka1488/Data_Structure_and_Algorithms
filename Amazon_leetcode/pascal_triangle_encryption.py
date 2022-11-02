"""
In order to ensure maximum security, the developers at amazon em
"""
import running_time


def getEncryptedNumber(numbers):
    temp_storage = []
    n = len(numbers)

    if n < 1:
        return ""

    if n <= 1:
        return str(numbers[0])

    while n != 2:
        for i in range(n - 1):
            new_item = numbers[i] + numbers[i + 1]
            if new_item > 9:
                new_item = new_item % 10
            temp_storage.append(new_item)
        numbers = temp_storage
        print(numbers)
        temp_storage = []
        n = len(numbers)
    return str(numbers[0]) + str(numbers[1])


if __name__ == '__main__':
    arr = [4, 5, 6, 7, 6, 7, 5, 4, 5, 6, 7, 6, 43]
    arr1 = []
    print(getEncryptedNumber(arr))
    running_time.time_to_run()
