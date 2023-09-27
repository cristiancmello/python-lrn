from array import array


class Stack:
    def __init__(self):
        self.__elements = array('I', list(0 for _ in range(2)))
        self.__size = 0

    def is_empty(self):
        return self.__size == 0

    def push(self, e: int):
        self.__elements[self.__size] = e
        self.__size += 1

    def size(self):
        return self.__size

    def pop(self):
        if self.__size == 0:
            raise StackUnderflowError

        self.__size -= 1
        return self.__elements[self.__size]


class StackUnderflowError(RuntimeError):
    pass
