class Deque:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return self._items == []

    def add_front(self, item):
        self._items.append(item)

    def add_rear(self, item):
        self._items.insert(0, item)

    def remove_front(self):
        return self._items.pop()

    def remove_rear(self):
        return self._items.pop(0)

    def size(self):
        return len(self._items)

    def __repr__(self):
        return f"<Deque: `rear` {self._items} `front`>"

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    d = Deque()
    print(d.is_empty())  # True
    d.add_rear(4)  # [4]
    d.add_rear('dog')  # ['dog', 4]
    d.add_front('cat')  # ['dog', 4, 'cat']
    d.add_front(True)  # ['dog', 4, 'cat', True]
    print(d.size())  # 4
    print(d.is_empty())  # False
    d.add_rear(8.4)  # [8.4 ,'dog', 4, 'cat', True]
    print(d.remove_rear())  # ['dog', 4, 'cat', True]
    print(d.remove_front())  # ['dog', 4, 'cat']
    print(d)
