from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1] if not self.is_empty() else 0

    def is_empty(self):
        return len(self.container) == 0


def getMax(operations):
    s = Stack()
    res = []
    for operation in operations:
        if len(operation.split()) == 2:
            query, value = operation.split()
        else:
            query = operation
        if query == '1':
            s.push(max(int(value), s.peek()))
        elif query == '2':
            if not s.is_empty():
                s.pop()
        else:
            res.append(s.peek())
    return res


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    print('\n'.join(map(str, res)))
    print('\n')
    #
    # fptr.close()
# 10
# 1 97
# 2
# 1 20
# 2
# 1 26
# 1 20
# 2
# 3
# 1 91
# 3
