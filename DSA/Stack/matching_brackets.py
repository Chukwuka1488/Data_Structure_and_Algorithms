from collections import deque
from stack import Stack


def match(expressions):
    my_stack = deque()
    error = False
    for i in expressions:
        if i == "(":
            my_stack.append(i)
        elif i == ")":
            if my_stack:
                my_stack.pop()
            else:
                print("ERROR")
                exit()
    if my_stack:
        error = True
    print("ERROR" if error else "OK")


if __name__ == '__main__':
    expression = input()
    match(expression)
