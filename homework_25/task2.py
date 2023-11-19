from node import Node


class Stack:

    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def push(self, item):
        new_node = Node(item)
        new_node.set_next(self._top)
        self._top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        data = self._top.get_data()
        self._top = self._top.get_next()

        return data

    def peek(self):
        if self.is_empty():
            return None
        return self._top.get_data()

    def size(self):
        if self.is_empty():
            return None

        current = self._top
        count = 0
        while current is not None:
            count += 1
            current.get_next()

        return count

    def __repr__(self):
        representation = "<Stack>\n"
        current = self._top
        while current is not None:
            representation += f"{str(current.get_data())}\n"
            current = current.get_next()
        return representation

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(stack.peek())

    print(stack.pop())
    print(stack.pop())

    print(stack.peek())

    print(stack.pop())
    print(stack.is_empty())
