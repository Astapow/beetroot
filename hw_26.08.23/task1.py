import random

random_list = []

count = 0
while count < 10:
    random_list.append(random.randint(1, 10))
    count += 1
print(max(random_list))
