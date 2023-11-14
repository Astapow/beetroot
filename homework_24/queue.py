class Queue:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return bool(self._items)

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

    def __repr__(self):
        representation = "<Queue>\n"
        for ind, item in enumerate(reversed(self._items), start=1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    q = Queue()
    q.enqueue(4)  # [4]
    q.enqueue('dog')  # ['dog', 4]
    q.enqueue(True)  # [True, 'dog', 4]
    print(q.size())  # 3
    print(q)
    print(q.dequeue())  # [True, 'dog']
    print(q.dequeue())  # [True]
    print(q.dequeue())  # []
