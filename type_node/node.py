# class Node:
#     def __init__(self, data):  # 31, None, 77, None
#         self._data = data  #
#         self._next = None
#
#     def get_data(self):
#         return self._data
#
#     def get_next(self):
#         return self._next
#
#     def set_data(self, data):
#         self._data = data
#
#     def set_next(self, new_next):
#         self._next = new_next
#
#
# my_list = [54, 26, 93, 17, 77, 31, None]
# order = [17, 26, 31, 54, 77, 93, 100, None] # 100 18

"""
Hash algorithm properties:
1. "Avalanche effect" - the tiniest change in incoming data changes the result completely
2. The possibility of each resulting checksum (hash) is the same to any other
3. You can not recreate the original contents from the checksum easily
"""
import random
from string import ascii_letters
from matplotlib import pyplot


def my_hash(key: str):
    result = 0
    max_int = 32

    for symbol in key:
        result = (result * max_int + ord(symbol)) % 100

    return result


def gen_random_string():
    result_len = random.randint(0, 10)
    all_characters = ascii_letters + '0123456789'

    return ''.join([random.choice(all_characters) for _ in range(result_len)])


result_range = range(101)
data = dict.fromkeys(result_range, 0)
for _ in range(1000):
    key = my_hash(gen_random_string())
    data[key] = data[key] + 1


names = list(data.keys())
values = list(data.values())

pyplot.bar(range(len(data)), values, tick_label=names)
pyplot.show()
