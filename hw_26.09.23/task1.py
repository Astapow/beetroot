def my_enumerate(iterable, start=0):
    count = start
    for item in iterable:
        yield count, item
        count += 1


print(list(my_enumerate([1, 2, 3], 2)))
