class MyIter:
    def __init__(self, iteration):
        self.iteration = list(iteration)
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < len(self.iteration):
            self.current += 1
            return self.iteration[self.current - 1]
        else:
            raise StopIteration


iterable_list = ["one", "two", "three", "four"]

some_dict = {"one": 1, "two": 2}

my_tuple_itr = 1, 2, 3, 4, 5,

my_dict = MyIter(some_dict.items())
my_list = MyIter(iterable_list)
my_tuple = MyIter(my_tuple_itr)

for item, val in my_dict:
    print(item, val)

print()

for i in my_list:
    print(i)

print()

for item in my_tuple:
    print(item)
