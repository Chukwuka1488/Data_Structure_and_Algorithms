"""
Applications of Stack Data Structure
Although stack is a simple data structure to implement, it is very powerful. The most common uses of a stack are:

To reverse a word - Put all the letters in a stack and pop them out. Because of the LIFO order of stack, you will get
the letters in reverse order. In compilers - Compilers use the stack to calculate the value of expressions
like 2 + 4 / 5 * (7 - 9) by converting the expression to prefix or postfix form.
In browsers - The back button in a browser saves all the URLs you have visited previously in a stack. Each time you
visit a new page, it is added on top of the stack. When you press the back button, the current URL is removed from
the stack, and the previous URL is accessed.

*************** Disadvantages *****************
using list as a stack isn't a good idea because it can lead to some memory issues. Due to the way lists are implemented
in the Python source code, the time complexity of some operations may not be that consistent. When the list grows
bigger, Python might need to find a large block of memory to relocate it to, which can slow down some append() calls.

The problem described above can be avoided by using deque.

Deque is a linear data structure that supports adding and removing elements from both sides. In Python,
you can find deque implementation in the collections module.
"""

from collections import deque


class Stack:
    def __init__(self):
        self.__arr = deque()

    def push(self, n):
        print(f"pushed item: {n}")
        return self.__arr.append(n)

    def remove(self):
        if Stack.isEmpty(self):
            return "stack is empty"
        else:
            return self.__arr.pop()

    def __len__(self):
        return len(self.__stack)

    def isEmpty(self):
        return self.__arr == []

    # __repr__ a developer - friendly one
    def __repr__(self):
        return f"Stack('{self.__arr}')"

    # __str__ should produce a user-friendly result
    def __str__(self):
        return f"description text: {self.__arr}"


if __name__ == '__main__':
    new_stack = Stack()
    # print(str(new_stack))
    # new_stack.push(5)
    # new_stack.push(4)
    # new_stack.push(3)
    # new_stack.push(2)
    # new_stack.push(1)
    # print(f"1: {repr(new_stack)}")
    # new_stack.remove()
    # print(f"2: {repr(new_stack)}")
    # new_stack.remove()
    # print(f"3: {repr(new_stack)}")
    # print(new_stack.isEmpty())
    # print(f"4: {repr(new_stack)}")
