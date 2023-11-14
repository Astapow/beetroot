class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

    def get_from_stack(self, element):
        found = False
        temp_stack = Stack()

        while not self.is_empty():
            item = self.pop()
            if item == element:
                found = True
                break
            temp_stack.push(item)

        while not temp_stack.is_empty():
            self.push(temp_stack.pop())

        if found:
            return item
        else:
            raise ValueError(f"Element '{element}' not found in the stack")


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(30)
    stack.push(54)

    print(stack.get_from_stack(30))
    print(stack.get_from_stack(54))
    print(stack.get_from_stack(15))
