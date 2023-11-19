from node import Node


class Queue:

    def __init__(self):
        self._front = None
        self._rear = None

    def is_empty(self):
        return self._front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self._rear is None:
            self._front = self._rear = new_node
            return

        self._rear.set_next(new_node)
        self._rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None

        data = self._front
        self._front = data.get_next()

        if self._front is None:
            self._rear = None

        return data.get_data()

    def size(self):
        count = 0
        current = self._front

        while current:
            count += 1
            current = current.get_next()

        return count

    def __repr__(self):
        representation = "<Queue>\n"
        current = self._front
        while current:
            representation += f"{str(current.get_data())}\n"
            current = current.get_next()
        return representation

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print(queue)

    print("pop item:", queue.dequeue())

    print("size:", queue.size())
