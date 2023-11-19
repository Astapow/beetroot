from node import Node


class UnsortedList:

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current = self._head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def __repr__(self):
        representation = "<UnsortedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"

    def append(self, item):
        self.add(item)

    def index(self, elem):
        current = self._head
        index = 0

        while current is not None:
            if current.get_data() == elem:  # [1, 2, 3, None]
                return index
            else:
                current = current.get_next()
                index += 1

        raise ValueError("Item not in list")

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty list")
        else:
            data = self._head.get_data()  # [1, 2, 3, None]
            self._head = self._head.get_next()  # [1, 2, None, None]
            return data

    def insert(self, index, item):
        if index == 0:
            self.add(item)
        else:
            current = self._head
            previous = None
            current_index = 0
            while current_index < index and current is not None:
                previous = current
                current = current.get_next()
                current_index += 1

            if current is None and current_index < index:
                raise IndexError("Index out of range")

            new_node = Node(item)
            new_node.set_next(current)
            previous.set_next(new_node)

    def slice(self, start, stop):
        if start > stop:
            return None

        current = self._head
        index = 0
        sliced_list = UnsortedList()

        while current is not None:
            if start <= index < stop:
                sliced_list.append(current.get_data())
            index += 1
            current = current.get_next()

        return sliced_list


if __name__ == "__main__":
    my_list = UnsortedList()

    my_list.append(12)
    my_list.append(15)
    my_list.append(122)
    print("index: ", my_list.index(15))
    print("index: ", my_list.index(12))
    print("size: ", my_list.size())
    print("pop ", my_list.pop())
    print("size: ", my_list.size())
    my_list.insert(0, 222)
    my_list.insert(0, 333)
    print(my_list)
    print("slice:", my_list.slice(1, 2))



