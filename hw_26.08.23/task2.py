import random

first_list = []
second_list = []

count = 0
while count < 10:
    first_list.append(random.randint(1, 10))
    second_list.append(random.randint(1, 10))
    count += 1

final_list = list(set(first_list + second_list))

print(final_list)
