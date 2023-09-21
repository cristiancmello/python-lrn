import array


class Stack:
    def __init__(self):
        self._elements = array.array('I', list(0 for _ in range(2)))
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def push(self, element):
        self._size += 1
        self._elements[self._size - 1] = element

    def pop(self) -> int:
        if self._size == 0:
            raise Underflow('Underflow error!')

        self._size -= 1
        return self._elements[self._size]

    def size(self):
        return self._size


class Underflow(RuntimeError):
    pass
